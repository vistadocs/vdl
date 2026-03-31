---
title: Nutrition & Food Services Version 5.5 Manager/ADPAC Guide (Revised Sept 2007)
doc_type: UG
doc_label: Manager/ADPAC Guide
doc_layer: anchor
doc_subject: (Revised Sept 2007)
app_code: FH
app_name: Nutrition and Food Service
section: CLI
app_status: active
pkg_ns: FH
patch_ver: 5.5
patch_id: FH*5.5
group_key: "FH:FH:5.5"
file_numbers: []
security_keys: []
menu_options: 209
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - blockquote
  - class
  - colspan
  - style
  - width
  - even
  - table
  - strong
  - header
  - colgroup
page_count: 0
word_count: 60296
section_count: 38
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5p8ag.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5p8ag.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=67"
---

> ![](nutrition-food-services-version-5-5-manager-adpac-guide-revised-sept-2007/001.png)

Nutrition and Food Service Manager/ADPAC Guide

![](nutrition-food-services-version-5-5-manager-adpac-guide-revised-sept-2007/002.png)

> *Version 5.5*

> *February 2005*

> Revised September 2007 for FH\*5.5\*8

> *Department of Veterans Affairs*

> *VistA Health System Design and Development*

> Revision History

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 47%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Page</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>September 2007</p>
</blockquote></td>
<td><blockquote>
<p>FH*5.5*8</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Added new options to the FP Food Preference Management menu.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#ep-enteredit-food-preferences-fhsel1">12</a></p>
</blockquote></td>
<td><blockquote>
<p>Modified information for the option: EP Enter/Edit Food Preferences.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#lp-list-food-preferences-fhsel2">15</a></p>
</blockquote></td>
<td><blockquote>
<p>Modified the information for option: LP List Food Preferences.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#mp-allergyfood-preference-map-fhself1">18</a></p>
</blockquote></td>
<td><blockquote>
<p>Added information on the new option: MP Allergy/Food Preference Map.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#cp-createmap-food-preferences-to-allergies-fhsela1">19</a></p>
</blockquote></td>
<td><blockquote>
<p>Added information on the new option: CP Create/Map Food Preferences to Allergies.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#up-update-all-patients-allergyfood-prefs-fhselu1">21</a></p>
</blockquote></td>
<td><blockquote>
<p>Added information for the new option: UP Update All Patients Allergy/Food Prefs.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#_PT_Print_Tray_Tickets_[FHMTKP]">120</a></p>
</blockquote></td>
<td><blockquote>
<p>Modified the PT option to remove allergy-type food preferences from the tray tickets.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#rl-list-recipes-fhrec3">145</a></p>
</blockquote></td>
<td><blockquote>
<p>Added a column, Recipes Embedded? to the List Recipes report.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>213</p>
</blockquote></td>
<td><blockquote>
<p>Expanded the Drug Classification field in the Clinical Site Parameters option.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>291</p>
</blockquote></td>
<td><blockquote>
<p>Changed the Clinician field to Clinician(s) in the Enter/Edit Nutrition Locations option.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>May 2007</p>
</blockquote></td>
<td><blockquote>
<p>FH*5.5*5</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_DP_Enter/Edit_Diet_Patterns_[FHMTKS]">113</a></p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Diet Patterns [FHMTKS]</p>
<p>Revised the descriptions columns for this option.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>220</p>
</blockquote></td>
<td><blockquote>
<p>The ENTER/EDIT DIETS [FHORD6] option</p>
<p>provides functionality to automatically update Diet Pattern names when a Diet is modified. Diet Pattern names are built by using the Abbreviated Label field of each Diet in the pattern. If the Abbreviated Label is changed it will now automatically update all Diet Pattern names that contain the modified Diet.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#te-enteredit-tubefeeding-products-fhortf1">226</a></p>
</blockquote></td>
<td><blockquote>
<p>In the Enter/Edit Tubefeeding Products [FHORTF1], the AMT/UNIT field of the TUBEFEEDING file (#118.2) allows the entry of values less than 10.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#sp-modify-site-parameters-fhsite">288</a></p>
</blockquote></td>
<td><blockquote>
<p>In the Modify Site Parameters [FHSITE] option, ten more Authorizer fields have been added to the FH SITE PARAMETERS (#119.9) file, a total of 15.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 47%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Page</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>291</p>
</blockquote></td>
<td><blockquote>
<p>The Enter/Edit Nutrition Locations [FHPRO2] option must be used to set up Room-Beds for Outpatient Locations. Once Room-Beds are set up for outpatient locations, then the Recurring, Special, and Guest meal order options can be used to select a Room-Bed when ordering outpatient meals. The outpatient Room-Bed will then be displayed on Tray Tickets and Diet Cards as well as other reports and display options.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>November 2006</p>
</blockquote></td>
<td><blockquote>
<p>FH*5.5*4</p>
</blockquote></td>
<td><blockquote>
<p><a href="#wl-list-nutrition-locations-fhpro6-1">298</a></p>
</blockquote></td>
<td><blockquote>
<p>The "Also Send Alert To" column added to lists the names of any other clinicians who are also assigned to this Nutrition Location.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>January 2006</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><a href="#gm-guest-meals-menu-fhomgmgr">299</a></p>
</blockquote></td>
<td><blockquote>
<p>Added Implementation for Outpatient Meals section to the ADPAC Guide.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>January 2006</p>
</blockquote></td>
<td><blockquote>
<p>FH*5.5*3</p>
</blockquote></td>
<td><blockquote>
<p>271</p>
</blockquote></td>
<td><blockquote>
<p>The PRODUCTION FACILITY: REMOTE</p>
<p>KITCHEN// prompt was added to enter/edit a Production Facility.</p>
<p>To print a specific Communication Office report, a link must be established between a specific Production Facility and a Communication Office.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>January 2006</p>
</blockquote></td>
<td><blockquote>
<p>FH*5.5*2</p>
</blockquote></td>
<td><blockquote>
<p>301</p>
</blockquote></td>
<td><blockquote>
<p>Ten more Outpatient Meals Diets have been added to the FH SITE PARAMETERS (#119.9)</p>
<p>file, a total of 15. Also, the fields OUTPATIENT MEALS DIET2 through OUTPATIENT MEALS</p>
<p>DIET15 are deleted if the OUTPATIENT MEALS DIET1 field is deleted and no data entry is allowed for the 2-15 DIET fields if there is no data in the OUTPATIENT MEALS DIET1 field. This fixes a discrepancy in functionality between the VISTA/server side and the GUI.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> [WP Print Weekly Menu \[FHPRC7\] 83](#wp-print-weekly-menu-fhprc7)

> [WR Print Weekly Menu Blocks \[FHPRC12\] 84](#wr-print-weekly-menu-blocks-fhprc12)

> [WL List Nutrition Locations \[FHPRO6\] 122](#wl-list-nutrition-locations-fhpro6)

> [WE Enter/Edit Location Assignments \[FHORC5\] 255](#we-enteredit-location-assignments-fhorc5)

> [WL List Location Assignments \[FHORC6\] 256](#wl-list-location-assignments-fhorc6)

> viii Nutrition and Food Service February 2005

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Notice of Service Name Change](#notice-of-service-name-change)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Scope](#scope)
  - [Security Key](#security-key)
  - [Menu Option Assignment](#menu-option-assignment)
- [Patch FH\5.5\8 Functionality Changes/Enhancements](#patch-fh558-functionality-changesenhancements)
- [DM Dietetics Management \[FHMGR\]](#dm-dietetics-management-fhmgr)
  - [AD Dietetic Administration \[FHMGRA\]](#ad-dietetic-administration-fhmgra)
    - [FP Food Preference Management \[FHSELX\]<sup>1</sup>](#fp-food-preference-management-fhselxsup1sup)
    - [MP Allergy/Food Preference Map \[FHSELF\]<sup>1</sup>](#mp-allergyfood-preference-map-fhselfsup1sup)
    - [SO Standing Order Management \[FHSPX\]](#so-standing-order-management-fhspx)
    - [XI Ingredient Management \[FHINGM\]](#xi-ingredient-management-fhingm)
    - [XM Menu Cycle Management \[FHPRCM\]](#xm-menu-cycle-management-fhprcm)
    - [XP Production Management \[FHPROM\]](#xp-production-management-fhprom)
    - [XR Recipe Management \[FHRECM\]](#xr-recipe-management-fhrecm)
    - [XX Annual Report Management \[FHADRR\]](#xx-annual-report-management-fhadrr)
- [CM Clinical Management \[FHMGRC\]](#cm-clinical-management-fhmgrc)
  - [DM Patient Data Log \[FHDMP\]](#dm-patient-data-log-fhdmp)
  - [XC Clinical Management Menu \[FHASCX\]](#xc-clinical-management-menu-fhascx)
    - [CR Clinical Management Report \[FHASNRR\]](#cr-clinical-management-report-fhasnrr)
    - [EC Enter/Edit Nutrition Classifications \[FHASC1\]](#ec-enteredit-nutrition-classifications-fhasc1)
    - [EP Enter/Edit Nutrition Plans \[FHASC9\]](#ep-enteredit-nutrition-plans-fhasc9)
    - [ET Enter/Edit Encounter Types \[FHASE1\]](#et-enteredit-encounter-types-fhase1)
    - [LC List Nutrition Classifications \[FHASC2\]](#lc-list-nutrition-classifications-fhasc2)
    - [LP List Nutrition Plans \[FHASC10\]](#lp-list-nutrition-plans-fhasc10)
    - [LS List Nutrition Statuses \[FHASC4\]](#ls-list-nutrition-statuses-fhasc4)
    - [LT List Encounter Types \[FHASE2\]](#lt-list-encounter-types-fhase2)
    - [XD Display Selected Drug Classifications \[FHSYP2\]](#xd-display-selected-drug-classifications-fhsyp2)
    - [XL Display Selected Lab Tests \[FHSYP1\]](#xl-display-selected-lab-tests-fhsyp1)
    - [XP Enter/Edit Clinical Site Parameters \[FHASC8\]](#xp-enteredit-clinical-site-parameters-fhasc8)
    - [XD Diet Order Management \[FHORDX\]](#xd-diet-order-management-fhordx)
  - [XE Energy/Nutrient Management \[FHNUX\]](#xe-energynutrient-management-fhnux)
    - [Managing Energy and Nutrients](#managing-energy-and-nutrients)
    - [ML List User Menus \[FHNU3\]](#ml-list-user-menus-fhnu3)
    - [NE Enter/Edit Nutrients \[FHNU6\]](#ne-enteredit-nutrients-fhnu6)
    - [NG Enter Nutrients (Common Units) \[FHNU12\]](#ng-enter-nutrients-common-units-fhnu12)
    - [NL List Nutrient File \[FHNU7\]](#nl-list-nutrient-file-fhnu7)
    - [RE Recipe Analysis \[FHNU11\]](#re-recipe-analysis-fhnu11)
    - [RL List DRI Values \[FHNU9\]](#rl-list-dri-values-fhnu9)
  - [XM Consult Management \[FHORCX\]](#xm-consult-management-fhorcx)
    - [Managing Consults](#managing-consults)
    - [CE Enter/Edit Consult Types \[FHORC7\]](#ce-enteredit-consult-types-fhorc7)
    - [CL List Consult Types \[FHORC8\]](#cl-list-consult-types-fhorc8)
    - [CR Re-Assign Active Consults \[FHORC9\]](#cr-re-assign-active-consults-fhorc9)
    - [CX Consult Statistics \[FHORC10\]](#cx-consult-statistics-fhorc10)
    - [WE Enter/Edit Location Assignments \[FHORC5\]](#we-enteredit-location-assignments-fhorc5)
    - [WL List Location Assignments \[FHORC6\]](#wl-list-location-assignments-fhorc6)
  - [XS Supplemental Feeding Management \[FHNOX\]](#xs-supplemental-feeding-management-fhnox)
    - [Managing Supplemental Feeding](#managing-supplemental-feeding)
    - [BE Enter/Edit Bulk Location Feedings \[FHNO8\]](#be-enteredit-bulk-location-feedings-fhno8)
    - [ME Enter/Edit Supplemental Feeding Menus \[FHNO6\]](#me-enteredit-supplemental-feeding-menus-fhno6)
    - [ML List Supplemental Feeding Menus \[FHNO7\]](#ml-list-supplemental-feeding-menus-fhno7)
    - [SE Enter/Edit Supplemental Feedings \[FHNO4\]](#se-enteredit-supplemental-feedings-fhno4)
    - [SL List Supplemental Feedings \[FHNO5\]](#sl-list-supplemental-feedings-fhno5)
- [DF Dietetic Facilities \[FHPRG\]](#df-dietetic-facilities-fhprg)
  - [Managing Dietetic Facilities](#managing-dietetic-facilities)
  - [CE Enter/Edit Communication Offices \[FHPRO9\]](#ce-enteredit-communication-offices-fhpro9)
  - [FE Enter/Edit Production Facilities \[FHPRO7\]](#fe-enteredit-production-facilities-fhpro7)
  - [NE Enter/Edit Supplemental Fdg. Sites \[FHPRO11\]](#ne-enteredit-supplemental-fdg-sites-fhpro11)
  - [SE Enter/Edit Service Points \[FHPRO8\]](#se-enteredit-service-points-fhpro8)
  - [SL List Production/Service/Communications Facilities \[FHPRO10\]](#sl-list-productionservicecommunications-facilities-fhpro10)
  - [SP Modify Site Parameters \[FHSITE\]](#sp-modify-site-parameters-fhsite)
  - [WE Enter/Edit Nutrition Locations \[FHPRO2\]](#we-enteredit-nutrition-locations-fhpro2)
  - [WL List Nutrition Locations \[FHPRO6\]](#wl-list-nutrition-locations-fhpro6)
- [OM Outpatient Meals \[FHMGROM\]](#om-outpatient-meals-fhmgrom)
    - [Implementation for Outpatient Meals<sup>1</sup>](#implementation-for-outpatient-mealssup1sup)
  - [SM Special Meals Menu \[FHOMSMGR\]](#sm-special-meals-menu-fhomsmgr)
    - [RO Request a Meal \[FHOMSR\]](#ro-request-a-meal-fhomsr)
  - [RM Recurring Meals Menu \[FHOMRMGR\]](#rm-recurring-meals-menu-fhomrmgr)
  - [GM Guest Meals Menu \[FHOMGMGR\]](#gm-guest-meals-menu-fhomgmgr)
- [SM System Management \[FHSYSM\]](#sm-system-management-fhsysm)
  - [Managing the System](#managing-the-system)
  - [DF Create Nutrition File entry for all Inpatients \[FHX4\]](#df-create-nutrition-file-entry-for-all-inpatients-fhx4)
  - [DL Update Patient Nutrition Location \[FHX5\]](#dl-update-patient-nutrition-location-fhx5)
  - [FP Check File Pointers \[FHX3\]](#fp-check-file-pointers-fhx3)
  - [PD Purge Nutrition Data \[FHPURGE\]](#pd-purge-nutrition-data-fhpurge)
  - [RD Recode Diets for all Inpatients \[FHX2\]](#rd-recode-diets-for-all-inpatients-fhx2)
  - [RI Check Integrity of Routines \[FHX1\]](#ri-check-integrity-of-routines-fhx1)
- [XF File Manager \[FHFILM\]](#xf-file-manager-fhfilm)
  - [FD File Dictionaries \[FHFIL4\]](#fd-file-dictionaries-fhfil4)
  - [IE Inquire to Files \[FHFIL3\]](#ie-inquire-to-files-fhfil3)
  - [PE Print File Entries \[FHFIL1\]](#pe-print-file-entries-fhfil1)
  - [SE Search File Entries \[FHFIL2\]](#se-search-file-entries-fhfil2)
- [Glossary](#glossary)
  - [Acronyms and Definitions](#acronyms-and-definitions)
  - [Terms and Definitions](#terms-and-definitions)
> In the past, all Nutrition information was classified according to inpatient Medical Administration Service (MAS) defined ward location and Delivery Points. These two categories functioned very well for some reports for many facilities but did not reflect the needs of all production areas and diet offices in all facilities. It also did not account for the changing needs of many facilities to track outpatient meal ordering data.

## Notice of Service Name Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pursuant to Department of Veterans Affairs VHA Directive 10-05-031, Nutrition and Food Service (N&FS) will be the official nomenclature used as the new service name for Dietetic Service in VHA Central Office and at Department of Veterans Affairs healthcare facilities.

> Therefore, all supporting documentation and customer education materials will use the Nutrition and Food Service nomenclature in place of the former Dietetic Service in all contexts. The change aligns this program more closely with the nomenclature recognized by national accrediting bodies, professional organizations, and other healthcare agencies. Additionally, the change is appropriate for the program that functions most directly in support of the nutrition and food services.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Nutrition and Food Service Outpatient Meals Manager/ADPAC Manual is designed as a reference guide for all Administrative and Clinical Nutrition Managers and/or the Nutrition and Food Service Application Coordinators who build, implement, and maintain Nutrition VistA files. This manual provides information necessary for the establishment and implementation of all Nutrition program files, including the Outpatient Meals enhancement. The Outpatient Meals software enhancement integrates the automation of the Outpatient Meals ordering process and many Clinical Nutrition and Food Management functions.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual is intended for use by the Nutrition and Food Service Clinical and Administrative Chiefs, and the Nutrition and Food Service Application Coordinators.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Nutrition and Food Service (NFS) Manager/ADPAC Manual is a guide designed to support the VistA Nutrition and Food Service, Version 5.5 program. This version includes the Outpatient Meals enhancement, which automates outpatient functions, adds new functionality and Clinical Quality Care monitoring activities to the existing NFS application. This manual provides complete documentation for previous and new functionality used by the Nutrition and Food Service Manager/ADPAC.

> <span id="_bookmark1" class="anchor"></span>The NFS software integrates the automation of many Clinical Nutrition and Food Service and Food Management functions. The Clinical Nutrition and Food Service activities of Nutrition and Food Service Screening, Nutrition and Food Service Assessment, Diet Order Entry, Tubefeeding and Supplemental Feeding Orders, Patient Food Preferences, Specific Diet Pattern Calculations, Nutrient Analysis of meals, Consult Reporting, Encounter Tracking, and Quality Care Monitoring are all available in this program. Complete automation of food production activities, service and distribution, inventory and cost management, recipe expansion, menu and recipe nutrient analysis, meal and diet pattern development and implementation, diet card and tray ticket printing, quality service tracking, and annual management reports are also available. The new functionality contained in this software includes the following capabilities:

- Provides electronic order entry of meals to authorized outpatients when they are kept over mealtimes.
- Enables electronic order entry of meals for other authorized users such as residents, without compensation employees and volunteers.
- Facilitates and tracks the number of meals for each Enhanced Sharing Agreement (selling of meal services), such as a childcare center, or a Meals-on Wheels program.
- Provide tracking, reporting and projection features currently for Inpatients Nutrition and Food Service Package will also include Outpatient.
- Ability to request, authorize, print, cancel, and view status of Outpatient Special Meals.
- Ability to request and print Guest Meals.
- Ability to request Recurring Meals for a regularly scheduled outpatient including a patient profile, meal status, early/late trays, and tubefeeding.
- Creation of new reports and modification of some existing Nutrition options to include Outpatient data.

> Functionality and activity processing for this software is divided into two major areas:

- Manager/ADPAC options used to build files, set parameters, review data, and generate reports.
- General user options used for normal day-to-day automated Nutrition functions.

> The Nutrition Manager/ADPAC is responsible for the coordination of all aspects of the VistA Nutrition and Food Service program. Therefore, all file building options are included in this manual. All or parts or all of the menus/modules can be assigned to selected users.

## Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A FHAUTH key has been created for the Outpatient Meals portion. The Manager/ADPAC is the only person who should hold the Nutrition and Food Service security key. The FHMGR key allows for Nutrition package files deletions but does not automatically protect the program from errors. The key holder must know the file inter-relationships in order to avoid system errors.

## Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Modify menu assignments to suit your needs. You can select a primary menu and enhance it by adding a secondary menu to it or you can modify a primary menu by removing or adding options as needed. Customize through the Site Manager.

> The menu options included in this manual are tailored to a variety of nutrition functions. Information about the options is located in both the User Manual and Manager/ADPAC Guide.

- External names of the options display first (the names that display at sign on to VistA).
- Internal names display within brackets "\[ \]".
- Series of three periods following a menu/option, means the menu/option displays a list of additional options.

> Note: It is recommended that you establish user groups for each Nutrition function and create lists of the main menus/options for those functions.

# Patch FH\*5.5\*8 Functionality Changes/Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Mapped GMR ALLERGIES (#120.82) file entries to specific allergy-type FOOD PREFERENCES (#115.2) file entries. You automatically add specific allergy-type food preferences to a patient's nutrition record as specific GMRA food-type allergies are added to the patient's medical record.
- Updated nutrition reports and ordering options, in order to display allergy data and to display the \*ALG indication on labels for patients with allergies.
- Resolved the issue in which Recipes with Embedded Recipes was not removed when printing tray tickets. A patient has an allergy or food preference; exclude the recipe from the tray ticket. Because the excluded recipe is embedded, the tray ticket code was not removing or replacing the food item.
- Expanded the Clinician field in the NUTRITION LOCATION (#119.6) file to a multiple to allow diet, tubefeeding, and consult bulletins to go to multiple RD's rather than one single individual.
- Updated and expanded the Nutrition Assessment option to allow the editing of the Work in Progress Assessment. Also, added additional necessary fields and new calculations to the option.
- Added Body Mass Index (BMI) to the Nutrition Profile and Screening Report.
- Made the inpatient Nutrition Assessment available as a Progress Note to TIU. When a Nutrition Assessment is marked as *Complete*, the assessment is created as a Progress Note in TIU.
- Added new fields to the API provided to Health Summary: Patient Allergies, Nutrition Assessment Patient Follow-up Date, and Comments. This is for inpatients only. The new fields are viewable in the Health Summary with patch GMTS\*2.7\*83; patch 8 only passes the new fields to Health Summary.
- Added new alerts for Nutrition Assessment Follow-up Date and Food/Drug Classification.

# DM Dietetics Management \[FHMGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AD</p>
</blockquote></th>
<th><blockquote>
<p>Dietetic Administration… [FHMGRA]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Management… [FHMGRC]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DF</p>
</blockquote></td>
<td><blockquote>
<p>Dietetic Facilities… [FHPRG]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OM</p>
</blockquote></td>
<td><blockquote>
<p>Outpatient Meals… [FHMGROM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SM</p>
</blockquote></td>
<td><blockquote>
<p>System Management… [FHSYSM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XF</p>
</blockquote></td>
<td><blockquote>
<p>File Manager… [FHFILM]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Dietetics Management provides access to all options within the Nutrition and Food Service System, both administrative and clinical, plus access to all maintenance and system management options. Package ADPACs and/or managers are the users of this menu.

## AD Dietetic Administration \[FHMGRA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AM</p>
</blockquote></th>
<th><blockquote>
<p>Administrative Menu… [FHADMR] (User Manual)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FP</p>
</blockquote></td>
<td><blockquote>
<p>Food Preference Management… [FHSELX]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PR</p>
</blockquote></td>
<td><blockquote>
<p>Production Reports… [FHADMR] (User Manual)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SO</p>
</blockquote></td>
<td><blockquote>
<p>Standing Order Management… [FHSPX]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XF</p>
</blockquote></td>
<td><blockquote>
<p>File Manager… [FHFILM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XI</p>
</blockquote></td>
<td><blockquote>
<p>Ingredient Management… [FHINGM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM</p>
</blockquote></td>
<td><blockquote>
<p>Menu Cycle Management… [FHPRCM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XP</p>
</blockquote></td>
<td><blockquote>
<p>Production Management… [FHPROM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XR</p>
</blockquote></td>
<td><blockquote>
<p>Recipe Management… [FHRECM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XX</p>
</blockquote></td>
<td><blockquote>
<p>Annual Report Management… [FHADRR]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Dietetics Administration provides access to all administrative management functions. Administrative Section Chiefs and Administrative Dietitians are the users of this menu.

> Reports for dietetic administration include outpatient meals and locations based on the type of information requested.

### FP Food Preference Management \[FHSELX\][<sup>1</sup>](#_bookmark6)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EP</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Food Preferences [FHSEL1]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>LP</p>
</blockquote></td>
<td><blockquote>
<p>List Food Preferences [FHSEL2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MP</p>
</blockquote></td>
<td><blockquote>
<p>Allergy/Food Preference Map [FHSELF]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>Create/Map Food Preferences to Allergies [FHSELA]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UP</p>
</blockquote></td>
<td><blockquote>
<p>Update All Patients Allergy/Food Prefs [FHSELU]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Food Preference Management allows you to build a site-specific listing of honored patient food preferences. You order preferences for specific patients. Recipes are associated with each dislike food preference, allowing for the automation of food preferences in Menu Management. Once the list is established, you can tabulate food preferences for use in meal production calculations; as well as appropriately substitute preferences within the printed diet card and tray ticket options.

#### Managing Food Preferences

> The Food Preference options are used at different levels. The simplest level is to order a preference for a patient to store in the computer. Ordering the preference in the computer alerts the diet office through the Diet Activity Report/Labels (DA).

> The next level is to use information from the program to adjust the tally when forecasting production needs. The program does not automatically adjust the Meal Production Report (Meal Production Reports (MR) option). However, it does tally preferences by meal, using the Tabulate Patient Meal Preferences (TP) option within the Production Reports (PR) menu. This list can be printed menu-specific or non-menu specific.

> The most complex level is using food preferences in the Diet Card and Tray Ticket programs.

- If you choose to use the computer generated Diet Card, under the Print Diet Cards (PD) option of the Tray Tickets (TT) menu, food preferences automatically print on the Diet Card.
- If you choose to use the Print Tray Tickets (PT) option in the same menu, food preferences automatically delete the “Dislike” recipes, add the “Like” recipes, and substitute the acceptable alternate recipes. (See Tray Tickets (TT) in the User Manual.)

> Food Preference changes when tray tickets are implemented. Only bread and beverage likes and all dislikes are handled under food preference. All other likes served, regardless of restrictions, must be entered as standing orders. Diet restrictions are stored as dislikes in the FOOD PREFERENCES file. Once you create the diet patterns, add the restrictions to each inpatient’s food preference entries if the diet applies. You can do this by answering YES to the question “Update All Diet Restrictions?”. The program only adds the entry if none exists and deletes it if the diet order is changed and the restrictions no longer apply. If you modify the preference through the Food Preference menu, the restriction stays with the patient after the diet order is changed.

> <span id="_bookmark6" class="anchor"></span><sup>1</sup> Patch FH\*5.5\*8 September 2007 Added new options to the FP Food Preference Management menu.

> Food preferences are stored in the computer even after the patient is discharged. When the patient is re-admitted, the following actions occur:

- All of the patient's past food preferences are viewed using the Patient Profile (PP) option under the Diet Orders (DO) menu, Print Nutrition Profile (PP) under the Nutrition Patient Management (NM) menu, Display Patient Preferences (DP) under the Food Preferences (FP) menu, or Patient Data Log (DM).
- “Dislike” food preferences only print on the Diet Activity Report/Labels with the patient's first diet order.
- If the automated Print Diet Cards (PD) option is used, all the patient's preferences in the file print on the Diet Card.
- If the automated Print Tray Tickets (PT) option is used, all the patient's preferences in the file are used to determine what food items print on a ticket for each meal.

> Data for the Food Preference Program is stored in the FOOD PREFERENCES file (#115.2). It uses data in the RECIPE file (#114). Make sure the RECIPE file (#114) is complete before using the Enter/Edit Food Preferences (EP) option.

#### Diagram of the Relationship

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#)</p>
<p>POINTER FIELD</p>
</blockquote></th>
<th><p>POINTER</p>
<p>TYPE</p></th>
<th><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>NUTRITION PERSON (#115.09) | | FOOD PREFERENCES ..... (N )-&gt; | 115.2 <strong>FOOD PREFERENCES</strong></p>
<p>| RECIPE |-&gt; <strong>RECIPE</strong></p>
<p>| m EXCLUD:EXCLUD* |-&gt; <strong>RECIPE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Steps to follow

1.  Review the contents of the FOOD PREFERENCES file using the List Food Preferences (LP) option.
2.  Determine food preference needs.
3.  Enter all recipes to exclude for dislikes in the FOOD PREFERENCES file using the Enter/Edit Food Preference (EP) option.
4.  Add to the FOOD PREFERENCES file as needed.

> To have the patient's bread and beverage replace the bread and beverage in the meal use the two fields, BREAD/BEVERAGE DEFAULT? and MEALS in the FOOD PREFERENCES file.

5.  Create a food preference for each bread and beverage you serve to replace with the inpatient’s bread and beverage. Specify the food preferences are bread and beverage defaults and the meal (B, N, E, or A) in which they belong.

> Example

> If whole wheat bread, white bread, white toast, and decaf coffee are served in the meal for breakfast, add a food preference for each of them.

6.  Create a food preference for the inpatient and assign it.

> Example

> Inpatient prefers rye bread and tea for breakfast, instead of the usual whole wheat bread and decaf coffee. Add rye bread and tea, and assign them to the patient.

#### EP Enter/Edit Food Preferences \[FHSEL1\]

> The Enter/Edit Food Preferences option allows you to enter data in the FOOD PREFERENCES file (#115.2) to accommodate all patients food likes and dislikes that the facility honors. It is not necessary to add a food item that your facility does not serve. All item entries are classified as “Like” or “Dislike” food preferences, which you associate with corresponding recipes for accurate tallies and/or tray ticket substitutions.

> You use this option to rename any existing allergy-type food preferences.[<sup>1</sup>](#_bookmark9) Because each site may use different naming conventions, it is *very important* that allergy-type food preferences be renamed using the specified convention.

> ALLERGY – \[name\]

> Example

> There is an allergy-type food preference called "NO FISH - ALLERGY". You must change it to "ALLERGY - FISH".

> You can also use this option to create a SYNONYM for allergy-type food preferences with old names, such as "NO FISH - ALLERGY". This allows you to look up and display the food preferences by the old names.

> A preference is a “Like” when a patient wants a food item daily for a specific meal or for all meals. You must create all “Like” food items that your facility wants to honor. You must assign a single corresponding recipe to each “Like”. If you use automated diet cards or tray tickets, you need to identify the default Bread and Beverage “Like” that is served at your facility.

> A preference is a “Dislike” when a patient does not want a food item on the tray. When using this option, all foods included for that “Dislike” are linked with the preference by listing those recipes.

#### Example

> “No Fish” includes baked fish, fish almandine, tuna salad, diet tuna salad, and so on. Whenever the computer finds one of these items to serve to a patient who has a “No Fish” preference, it is listed on the Tabulate Patient Meal Preferences (TP) report.

> The field “Food Preferences” uses food preferences when entering data for a patient. In turn, the Food Preferences “Recipe:” and “Excluded Recipe:” fields use data from the RECIPE file (#114).

> Food Preferences Name: This field is 3 - 30 characters in length, not numeric, and not starting with punctuation. The name is descriptive of the food preference. Dislikes are prefaced with “NO” in the name field.

> <span id="_bookmark9" class="anchor"></span><sup>1</sup> Patch FH\*5.5\*8 September 2007 Modified information for the option: EP Enter/Edit Food Preferences.

#### Examples

- No Orange Juice
- No Fish
- Choc Milk
- Tea

> Like or Dislike: This is a required field and indicates whether the preference is a “Like” or a Dislike”.

> If you enter “Dislike”, a prompt displays, “Select EXCLUDED RECIPES:”. You can enter multiple recipes that contain the food item for the selected dislike.

> Excluded Recipe: This field points to the RECIPE file (#114) and only displays when “Dislike” is entered. You can enter multiple recipes that contain the disliked food item. To illustrate, if the dislike is “No Potatoes”, enter all recipes that contain any kind of potatoes as excluded recipes. “No Mashed Potatoes” excludes only recipes containing Mashed Potatoes, such as LS Mashed Potatoes, Duchess Potatoes, LS Duchess Potatoes, Snowflake Potatoes, and so on.

> Recipe: This field points to the RECIPE file (#114) and only displays when “Like” is entered. Select one recipe from the file to display on the Diet Card or Tray Ticket to provide the preference.

> Bread/Beverage Default: This prompt displays only when you select “Like”. A “Yes” entry indicates this is the normally served item. A “No” entry indicates it is not a normally served “Like”, but one that can be entered specifically for a patient.

> Meals: This prompt displays only when you enter “Yes” under the Bread/Beverage Default field. This allows the food item to be the default preference for only certain meals or all meals. Meal letter identifiers (B, N, E) can be entered in multiples, such as “BN”, “BE”, “BNE”, or “A” for all meals.

> Inactive Field: This field indicates whether the Food Preference is currently inactive. For various reasons, a facility may not be able to accommodate certain Food Preferences on a permanent or temporary basis. Selecting “Yes” inactivates a Food Preference without deleting it from the file. If an inactive Food Preference is entered for a patient, “\*\* INACTIVE \*\*” displays in the name of the selected item, indicating that this Food Preference will not be honored at this time. The manager can re-activate a food preference by entering “No” at this prompt.

> Note: To view a list of the existing Food Preferences, enter ?? at the ‘Select FOOD PREFERENCES NAME:’ prompt.

> Enter data in the FOOD PREFERENCES file (#115.2) to accommodate all patients' food likes and dislikes

> Note: For a Yes or No answer, when there is no default, pressing \<RET\> is the same as No.

#### LP List Food Preferences \[FHSEL2\]

> The List Food Preferences option is an 80-column report that lists all the data in the FOOD PREFERENCES file (#115.2) and entered using the Enter/Edit Food Preferences (EP) option. Provided you have renamed any existing allergy-type Food Preferences with the new naming convention, your allergy-type food preferences display in alphabetical order.[<sup>1</sup>](#_bookmark12)

#### Example of LP with renamed allergy-type food preferences

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 25%" />
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><blockquote>
<p>Select Food Preference Management Option: LP List Food Preferences</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="7"><blockquote>
<p>DEVICE: TELNET Right Margin: 80//</p>
<p>PATIENT PREFERENCES JUN 26, 2007 14:42 PAGE 1 NAME TYPE INA DEF MEAL</p>
<p>RECIPE</p>
<p>EXCLUDED RECIPES</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ALLERGY</p>
</blockquote></th>
<th><blockquote>
<p>–</p>
</blockquote></th>
<th><blockquote>
<p>BEANS, LENTILS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ALLERGY</p>
</blockquote></th>
<th><blockquote>
<p>–</p>
</blockquote></th>
<th><blockquote>
<p>ALCOHOL, WINE DIS</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>PINEAPPLE</p>
</blockquote></th>
<th><blockquote>
<p>PIE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ALLERGY</p>
</blockquote></th>
<th><blockquote>
<p>–</p>
</blockquote></th>
<th><blockquote>
<p>ALFALFA SPROUTS</p>
</blockquote></th>
<th><blockquote>
<p>DIS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ALLERGY</p>
</blockquote></th>
<th><blockquote>
<p>–</p>
</blockquote></th>
<th><blockquote>
<p>APPLES</p>
</blockquote></th>
<th><blockquote>
<p>DIS</p>
</blockquote></th>
<th>BNE</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example of the LP List Food Preferences option

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 12%" />
<col style="width: 49%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE:</p>
</blockquote></th>
<th></th>
<th></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PATIENT PREFERENCES NAME</p>
</blockquote></th>
<th>TYPE</th>
<th><blockquote>
<p>MAR 8,2005 14:14 PAGE 1 INA DEF MEAL</p>
<p>RECIPE</p>
<p>EXCLUDED RECIPES</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NO APPLE JUICE</p>
</blockquote></th>
<th>DIS</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th><blockquote>
<p>APPLE JUICE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NO APPLESAUCE</p>
</blockquote></th>
<th>DIS</th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NO APRICOTS</p>
</blockquote></th>
<th>DIS</th>
<th><blockquote>
<p>APPLESAUCE</p>
<p>CINNAMON APPLESAUCE DB APPLESAUCE</p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>PUREED APRICOTS APRICOT PRUNE SALAD APRICOT SALAD APRICOT NECTAR</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NO ASPARAGUS</p>
</blockquote></th>
<th>DIS</th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="_bookmark12" class="anchor"></span><sup>1</sup> Patch FH\*5.5\*8 September 2007 Modified the information for option: LP List Food Preferences

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 29%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>ASPARAGUS, CANNED LS ASPARAGUS</p>
</blockquote></th>
<th rowspan="17"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NO BACON</p>
</blockquote></th>
<th><blockquote>
<p>DIS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>BACON</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NO BAKED FISH</p>
</blockquote></th>
<th><blockquote>
<p>DIS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>BAKED FISH FILLETS BAKED FISH PARISIENNE LS BAKED FISH FILLETS</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NO BAKED POTATO</p>
</blockquote></th>
<th><blockquote>
<p>DIS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>BAKED POTATO</p>
<p>LS BAKED POTATO</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NO CHICKEN</p>
</blockquote></th>
<th><blockquote>
<p>DIS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>FRIED CHICKEN</p>
<p>OVEN FRIED CHICKEN CHICKEN TETRAZINI GROUND PULLED CHICKEN CHICKEN ALA KING CHICKEN ALA MARYLAND CHICKEN DRUMSTICK</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PATIENT PREFERENCES</p>
<p>NAME</p>
</blockquote></th>
<th><blockquote>
<p>TYPE</p>
</blockquote></th>
<th><blockquote>
<p>INA</p>
</blockquote></th>
<th><blockquote>
<p>DEF</p>
</blockquote></th>
<th><blockquote>
<p>MAR MEAL</p>
</blockquote></th>
<th><blockquote>
<p>8,2005 14:14 PAGE 2</p>
<p>RECIPE</p>
<p>EXCLUDED RECIPES</p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>CHICKEN PATTY ON BUN CHICKEN POT PIE</p>
<p>LS FRIED CHICKEN</p>
<p>LS OVEN FRIED CHICKEN LS CHICKEN ALA KING LS CHICKEN DRUMSTICK LS CHICKEN TETRAZINI</p>
<p>COUNTRY CREAMED CHICKEN CHICKEN CACCIATORE</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>BREAD,RYE</p>
</blockquote></th>
<th><blockquote>
<p>LIK</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>RYE BREAD - 1 SLICE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>BREAD,WG</p>
</blockquote></th>
<th><blockquote>
<p>LIK</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>NATURAL WW BREAD - 2 SL</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>BREAD,WHITE</p>
</blockquote></th>
<th><blockquote>
<p>LIK</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>YES</p>
</blockquote></th>
<th><blockquote>
<p>BNE</p>
</blockquote></th>
<th><blockquote>
<p>WHITE BREAD</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>BROTH</p>
</blockquote></th>
<th><blockquote>
<p>LIK</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>BROTH, VARIETY</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CANNED FRUIT,DB</p>
</blockquote></th>
<th><blockquote>
<p>LIK</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>DB APPLESAUCE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CANNED FRUIT,REG</p>
</blockquote></th>
<th><blockquote>
<p>LIK</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>APPLESAUCE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MP Allergy/Food Preference Map \[FHSELF\][<sup>1</sup>](#_bookmark15)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Allergy/Food Preference Map option provides two lists.

1.  Enter A to view the food-type GMR ALLERGIES (#120.82) file entries with corresponding allergy-type FOOD PREFERENCES (#115.2) file entries.
2.  Enter F to view the allergy-type FOOD PREFERENCES (#115.2) file entries with corresponding food-type GMR ALLERGIES (#120.82) file entries.

> <span id="_bookmark15" class="anchor"></span><sup>1</sup> Patch FH\*5.5\*8 September 2007 Added information on the new option: MP Allergy/Food Preference Map

#### CP Create/Map Food Preferences to Allergies \[FHSELA\][<sup>1</sup>](#_bookmark18)

> The Create/Map Food Preference to Allergies option allows you to create or map food preferences to allergies automatically.

- Use the CP option to display an alphabetical listing of the allergy-type Food Preferences that do not yet exist at your site.
- Select any food preference from the list and add it to the FOOD PREFERENCES file, like adding a new food preference with the EP option.

> Note: Do not use CP, when an item in the list already exists and was not renamed or was not renamed correctly; rather use EP.

> Do not duplicate food preferences names.

#### Example

> When the "ALLERGY - FISH" Food Preference shows up on the allergy- type Food Preferences list and you know that it already exists as a Food Preference, return to the EP option and rename it "ALLERGY - FISH". It probably was not yet renamed or there is a typo in the name, such as "AALERGY - FISH".

#### The naming convention must be exact, "ALLERGY - \[TYPE\]".

> <span id="_bookmark18" class="anchor"></span><sup>1</sup> Patch FH\*5.5\*8 September 2007 Added information on the new option: CP Create/Map Food Preferences to Allergies.

#### UP Update All Patients Allergy/Food Prefs \[FHSELU\][<sup>1</sup>](#_bookmark21)

> The Update All Patients Allergy/Food Prefs option allows you to update food preferences to allergies automatically, provided you have renamed any existing allergy-type Food Preferences with the new naming convention. When you run this option, all inpatients are checked for any existing GMR Allergies *without* corresponding Food Preferences. If any food preferences are missing, but the link between GMR Allergies and the Food Preferences exists, this option adds the necessary food preferences.

> <span id="_bookmark21" class="anchor"></span><sup>1</sup> Patch FH\*5.5\*8 September 2007 Added information for the new option: UP Update All Patients Allergy/Food Prefs.

### SO Standing Order Management \[FHSPX\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>LS</p>
</blockquote></th>
<th><blockquote>
<p>List Standing Order File [FHSP2]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Standing Order File [FHSP1]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Standing Order Management allows you to create a listing that honors patients' requests or dietary requirements for specific food items or utensils. You can select standing orders for any patient for any meal or quantity. You can generate labels for each item and patient, as well as a consolidated listing for production purposes of items necessary for each service point and meal.

#### Managing Standing Orders

> Standing orders are separated into two types, individual and diet-associated. Individual standing orders are orders ordered through the Standing Order menu. These orders are not cancelled when the diet order is changed. All individual standing orders are denoted by an “(I)” on the Location Diet Order List, Diet Activity, etc.

> The diet-associated standing orders are tied to the diet pattern, which is added to any newly admitted patient when the diet is ordered. This also applies to the current inpatients that have diet order changes. When a diet order changes, the old diet-associated standing orders are cancelled and the new diet order becomes effective.

> Only current inpatients that already have the existing diet order before the pattern is created will not have the standing orders added to the file. You need to reorder the diet order for the inpatient, if you want the standing orders to become effective. Otherwise, consider modifying the patient’s standing orders, so that the patient does not have duplicates or more standing orders than needed when a diet order is changed. The reason behind this is that right after installation, existing inpatients already have existing standing orders. We cannot update existing inpatient standing order files after a pattern is created, because it might cause duplicates that need to be cancelled.

> Therefore, before automatically adding more standing orders to an inpatient, review the difference between individual standing orders and diet-associated standing orders. Determine if there is any need to modify the inpatient’s standing orders.

> When an inpatient has diet order changes, there will be fewer orders to modify. On the tray ticket, both types of standing orders are considered standing orders. Once an associated standing order is added to an inpatient’s file and modified through the option Enter/Edit Standing Orders (SE), it becomes an individual standing order and remains with the inpatient.

> Standing Orders are tabulated for each Service Point per meal, using the Tabulate Standing Orders (SO) option under the Production Reports (PR) or the Nutrition Lists/Reports menu. This list is used by the production staff for preparation and distribution. The option to print a label for each standing order identifies which patient receives the Standing Order item. The option to print labels is Print Standing Order Labels (SL) of the Production Reports (PR) and the Nutrition Lists/Reports (DR) menus.

> The STANDING ORDERS file (#118.3) does not use data from other files, but its data is used when setting up the DIET PATTERNS file.

#### Diagram of the Relationship

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#)</p>
<p>POINTER FIELD</p>
</blockquote></th>
<th><p>POINTER</p>
<p>TYPE</p></th>
<th><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p><strong>DIET PATTERNS</strong> (#111.11) | | ASSOCIATED STANDING OR* (N )-&gt; | 118.3 <strong>STANDING ORDERS</strong> ASSOCIATED STANDING OR* (N )-&gt; | |</p>
<p>ASSOCIATED STANDING OR* (N )-&gt; | |</p>
</blockquote>
<p>NUTRITION PERSON (#115.08) | |</p>
<p>ADMIS:STANDIN:ORDER* . (N C )-&gt; | |</p></td>
</tr>
</tbody>
</table>

- Standing Orders automatically generated as part of the diet pattern are deleted if the diet order changes. Diet-Associated Standing Orders do not have any parentheses after the name.
- Changing a diet does not affect the Standing Order that is individualized for a patient. It displays as a Standing Order (I).
- An existing entry on the list of Standing Orders cannot be deleted. Use the Inactive field.
- To accommodate items not served daily, the Standing Order name can include the time or days, such as “Cold Sandwich (MWF only)”. This displays each day for the meal. The production employees need to ignore this on the “other” days or diet office personnel can line through this before taking it to the production areas.
- Try to enter the item the same way it is ordered. For example, it is probably best to list “Soup, Reg” and “Soup, LS” instead of “Reg Soup” and “LS Soup”.
- The order in which the standing orders display on lists are planned, e.g., cold foods can be preceded with “Cold” or “C”, so that they are grouped together. Entries with numbers display first, followed by letters in alphabetical order.
- There is some overlap in the functionality of the Standing Orders Program and the Food Preference Program. Consider the functions of each program before building the files.
- Standing Orders print on the automated Tray Ticket and/or Diet Card.

> There are steps necessary to build the data in the STANDING ORDERS file (#118.3) that supports the Standing Orders Program. A Standing Order is a special request for an item that is not normally produced or available at a given meal. It is similar to a Food Preference, but Food Preferences generally refer to patient likes and dislikes, and requests for items that are routinely available. Standing Orders are entered for a patient by the clinician or automatically generated as part of the diet pattern, and created under the Enter/Edit Patient Diet Pattern (DP) option.

#### Steps to Follow

1.  Review the STANDING ORDERS file using the List Standing Order File (LS) option.
2.  Review diet card/manual system for needs.
3.  Determine the need for individualized standing orders versus the automated diet-associated standing orders. The automated associated standing orders go away when diet order is changed.
4.  Assign needed (if necessary) individual standing order to inpatients.

#### LS List Standing Order File \[FHSP2\]

> The List Standing Order File option is an 80-column report that lists all items in the STANDING ORDERS file (#118.3) and is created using the Enter/Edit Standing Order File (SE) option.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><blockquote>
<p>DEVICE: (Printer name)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>STANDING ORDERS</p>
</blockquote></td>
<td colspan="2">MAR</td>
<td><blockquote>
<p>8,2005</p>
</blockquote></td>
<td><blockquote>
<p>11:23</p>
</blockquote></td>
<td><blockquote>
<p>PAGE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>INACTIVE?</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>LABEL?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>C-4 OZ NDC</p>
<p>C-APPLESAUCE, DIABETIC</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C-APPLESAUCE, REG</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>C-COTTAGE CHEESE C-CRANBERRY JUICE C-DB CANNED FRUIT</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C-FRESH APPLE ONLY</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>C-FRESH FRUIT</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ol start="6" type="A">
<li><p>RESH ORANGE ONLY C-FRUIT ICE</p></li>
<li><blockquote>
<p>ELATIN, DB</p>
</blockquote></li>
</ol></td>
<td></td>
<td colspan="5"><blockquote>
<p>NO</p>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ol start="7" type="A">
<li><p>ELATIN, REG C-GRAPE JUICE</p></li>
<li><p>ALF AND HALF - 4OZ C-ICE CREAM</p></li>
</ol>
<blockquote>
<p>C-ICE CREAM, VANILLA ONLY C-JUICE OF DAY</p>
<p>C-LEMONADE</p>
<p>C-LETTUCE SALAD</p>
<p>C-PUDDING, REGULAR C-PUREED FRUIT</p>
<p>C-REG CND FRUIT</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>NO YES NO</p>
<p>YES</p>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H-BAKED FISH M-W-F ONLY</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H-BEEF PATTY H-BROTH, LS</p>
<p>H-BROTH, REGULAR</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H-CHEESE, REG. 1 OZ H-CREAM SOUP</p>
<p>H-EGG, HARD BOILED H-EGG, SCRAMBLED</p>
<p>H-GRAVY</p>
<p>H-GRAVY, LS</p>
<p>H-LS CREAM SOUP</p>
</blockquote>
<ol start="12" type="A">
<li><p>S HOT CEREAL-NO OATMEAL H-LS SOUP-NO CREAM</p></li>
<li><blockquote>
<p>ASHED POTATOES</p>
</blockquote></li>
<li><blockquote>
<p>O BEEF-NO CHEESE</p>
</blockquote></li>
</ol>
<blockquote>
<p>H-NO GRND BEEF-GIVE CHEESE</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES YES</p>
<p>NO</p>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H-NO GRND BEEF-GIVE COTT CHEZ</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H-NO GRND BEEF-GIVE LS CHEZ</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H-NO RST BEEF-GIVE CHEESE</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H-NO RST BEEF-GIVE COTT CHEZ</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H-NO RST BEEF-GIVE LS CHEESE H-OATMEAL, REGULAR</p>
<p>H-PEANUT BUTTER - 2 TBSP</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H-PLAIN GRND MEAT H-PLAIN MEAT</p>
<p>H-POTATO</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>NO</p>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H-SAND COLD MEAT W/CONDIMENTS</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### SE Enter/Edit Standing Order File \[FHSP1\]

> The Enter/Edit Standing Order File option allows you to enter and edit data in the STANDING ORDERS file (#118.3). The file contains the names of food items/preferences and produces a selection list when a standing order is entered for a patient, using the Enter/Edit Standing Orders (SE) option. It is also used when a standing order is created as part of a diet pattern under the Enter/Edit Diet Patterns option in Tray Tickets/Diet Cards Management.

> Standing Orders Name: Item names must be 3-30 characters in length. There is no limit to the number of food items you can enter.

> To accommodate items not served daily, the Standing Order name can include the time or days, such as “Cold Sandwich (MWF only)”. This displays each day for the meal designated.

> You can view Standing Orders on the Location Diet List (WL), Patient Profile (PP), and Nutrition and Food Service Profile (NP). A Standing Order displays by name only if it is part of the diet pattern. If it is a Standing Order individualized for a patient, that is not part of the diet pattern, it displays with (I) following the name. This is to indicate that the clinician entered a Standing Order for the patient. This nomenclature is similar to that used for Supplemental Feedings.

#### Examples

- Applesauce, DB
- Broth, LS
- Cold Meat Sandwich (M W F)
- Cottage Cheese
- Cottage Cheese
- Egg, Hard boiled
- Grilled Cheese sandwich
- No Fish
- No Liver

> In order to handle non-routine requests needed for patient care, you can create a “Specials” entry as part of this file. Use it for the occasional order allowed for a particular patient, but is not a routinely approved standing order. Manually write the name of the item on the Tabulated Standing Orders List.

> Label: This field identifies whether a computer-generated label for the item prints. The appropriate response is “YES” (Y) or “NO” (N). The label includes all patient identification and location, as well as the Standing Order item name and meal.

> Inactive: This field indicates whether the Standing Order is currently inactive. For various reasons, a facility may not be able to accommodate certain Standing Orders on a permanent or temporary basis. Selecting “YES” inactivates a Standing Order without deleting it from the file. A “NO” reactivates the Standing Order. If anyone holding the key FHMGR enters an inactive

> Standing Order for a patient, “\*\* INACTIVE \*\*” displays in the name of the selected item, indicating that this Standing Order is not honored. This warning does not display without this level of access, without which you could not select an inactive Standing Order.

### XI Ingredient Management \[FHINGM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>IE</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Ingredients [FHING3]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IN</p>
</blockquote></td>
<td><blockquote>
<p>List Ingredients - Nutrient Data [FHING52]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IP</p>
</blockquote></td>
<td><blockquote>
<p>List Ingredients - Purchasing Data [FHING51]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IR</p>
</blockquote></td>
<td><blockquote>
<p>List Ingredients - Recipe Data [FHING5]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Storage Locations [FHING4]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LL</p>
</blockquote></td>
<td><blockquote>
<p>List Storage Locations [FHING8]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Current Ingredient QOH [FHING12]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QW</p>
</blockquote></td>
<td><blockquote>
<p>Display Ingredient Inventory List [FHING13]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>List Recipes Containing an Ingredient [FHING11]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Units [FHING1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UL</p>
</blockquote></td>
<td><blockquote>
<p>List Units [FHING6]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Vendor File [FHING2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VL</p>
</blockquote></td>
<td><blockquote>
<p>List Vendors [FHING7]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Ingredient Management allows you to enter data that controls all aspects of ingredient usage within the Nutrition and Food Service program. Each ingredient is associated with its vendor, storage location, purchasing data (cost and unit), issuing and recipe unit conversions, nutrient references and weight conversions. Lists are generated containing all data fields, as well as listing of all recipes containing a particular ingredient. An ingredient inventory module exists to allow for tracking, recording, and calculating physical inventory on hand on a monthly basis.

> The Ingredient Management Program is the foundation of Food Management. The program consists of an extensive INGREDIENT file (#113) and three smaller data files: UNITS file (#119.1). STORAGE LOCATION file (#113.1) and VENDOR file (#113.2). Approximately 1000 ingredients, common to most VA medical centers, come with the program in the INGREDIENT file (#113). In addition, some basic data comes in the UNITS file (#119.1). Both of these files can have additional information entered and can be edited. The STORAGE LOCATION file (#113.1) and VENDOR file (#113.2) come without data.

> It is highly recommended that the data in all Ingredient Management files be carefully reviewed and data entered or edited before proceeding on to other options. Every ingredient in a recipe and every single food item required to prepare and serve a meal, e.g., creamer, sugar substitute, bread and milk, must be contained in the INGREDIENT file (#113).

> The Inventory Management Program and Energy Nutrient data links for Nutritional analysis are new to the INGREDIENT file (#113) in this version. The Inventory Management Program generates worksheets by food groups or storage locations for ease of data collection when doing physical inventories. Current costs and quantities on hand can be updated easily as the program loops through the INGREDIENT file (#113). Finally, an Inventory Cost Report is generated with subtotals by food groups.

> The new nutrient-ingredient link was added to facilitate recipe and meal analysis. All recipes and meals can now be quickly analyzed with a minimal effort. Each ingredient must be linked to a nutrient from the FOOD NUTRIENTS file (#112); this then becomes the default nutrient in the recipe analysis program. This nutrient can be edited for any recipe as needed.

> A field for IFCAP Master Items Number (MINS) was added to the INGREDIENT file (#113) for better item identification and to facilitate future links with IFCAP.

> The RECIPE file (#114) to the left uses data from the INGREDIENT file (#113) and the INGREDIENT file (#113) uses data in those files listed on the right (VENDOR, UNITS, STORAGE LOCATION, FOOD NUTRIENTS, and ITEM MASTER).

#### Diagram of the Relationship

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#)</p>
<p>POINTER FIELD</p>
</blockquote></th>
<th><p>POINTER</p>
<p>TYPE</p></th>
<th><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p><strong>RECIPE</strong> (#114.01) | | INGREDIENT ........... (N )-&gt; | 113 <strong>INGREDIENT</strong> |</p>
<p>| VENDOR |-&gt; <strong>VENDOR</strong></p>
<p>| NUTRITION UNIT* |-&gt; <strong>UNITS</strong></p>
<p>| STORAGE LOCATI* |-&gt; <strong>STORAGE LOCATION</strong></p>
<p>| NUTRIENT DATA * |-&gt; <strong>FOOD NUTRIENTS</strong></p>
<p>| MASTER ITEM # |-&gt; <strong>ITEM MASTER</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### IE Enter/Edit Ingredients \[FHING3\]

> The Enter/Edit Ingredients option allows you to create new ingredients or edit existing ingredients in the INGREDIENT file (#113) to correspond to the facility needs. You can add or delete ingredients from the file at any time.

> Warning: Before deleting an ingredient, make sure it is not used in a recipe. Use the List Recipes Containing an Ingredient (RL) option to check every ingredient you want to delete.

> If it is not in a recipe, delete the ingredient immediately.

> If it is in a recipe(s), you must delete the ingredient from the recipe(s) before deleting the ingredient. Failure to delete an ingredient from a recipe before deletion from the INGREDIENT file (#113) results in program errors.

> Before any changes are made to INGREDIENT file (#113), review all data pertinent to each ingredient and identify any changes or additions needed to make this file appropriate to the facility. Because there are 21 data fields associated with each ingredient, this file must be printed in three separate lists:

- List Ingredients - Nutrient Data (IN),
- List Ingredients - Purchasing Data (IP), and
- List Ingredients - Recipe Data (IR).

> Combined, these lists provide all the data relevant to each ingredient. Review all data fields carefully. Nine of the fields are required for the Food Production Program. Other fields are utilized for optional reports and analysis, such as inventory and nutrient analysis. Other fields in the file are there in preparation for future program routines, such as thaw days, and linking to IFCAP.

> The INGREDIENT file (#113) points to/uses data from four other files: UNITS, VENDOR, STORAGE LOCATION and FOOD NUTRIENTS. The Units and Vendor names can be entered under Enter/Edit Units (UE) and Enter/Edit Vendor File (VE) options or entered in the fields “VENDOR:” and “Nutrition Unit of Issue:” using the option Enter/Edit Ingredients. You can add and edit the basic data sent with the UNITS file (#119.1). Print a List Units (UL) as a reference tool when editing the INGREDIENT file (#113). Data for the STORAGE LOCATION file (#113.1) must be created under Enter/Edit Storage Locations (LE) prior to building the INGREDIENT file (#113). Data is sent with the FOOD NUTRIENTS file (#112) and is updated with each new Nutrition VistA version. (See the Energy/Nutrient Management Section.)

> The validity and completeness of the INGREDIENT file (#113) is essential in generating accurate adjusted recipes, storeroom requisitions, and meal production reports. Any change in an ingredient name, type, or unit of purchase or issue will drastically affect other ingredient data, such as recipe unit, nutrient reference, etc. Therefore, if you change any data for an ingredient, be sure to check all other fields for accuracy.

> Ingredient Name: The name must be 3-50 characters in length. Write ingredient names in the same terminology as stated in recipes. This enables the person entering recipes to find ingredients more easily. You can edit the name field of an ingredient that is already in the INGREDIENT file (#113).

> Master Item \#: This 4-digit number is the IFCAP Master Item Number (MIN) for this ingredient at the facility. This number prints on the inventory worksheet and report for item identification. Ingredient MINs are unique to each facility. This field accepts a short item name, NSN, NDC or Vendor stock number as a cross reference to IFCAP to facilitate data entry. If a name or other number is entered, the MIN is displayed and only the MIN is stored with the ingredient in the file.

> Supply Description: The supply description is a required entry and must be 3-21 characters in length. Descriptive names on national stock numbered ingredients in the file are derived from approved Federal Item Identifications, which you cannot change. The supply description should include details about the item in an appropriate format. Descriptions of new items added to the file should include product information such as, can size (No. 303), frozen (frz), etc. This field is not used at this time but is for the future for food ordering and inventory.

> Vendor: The vendor is not a required entry. Vendor entries must be 3-30 characters in length. A vendor is the source that supplies an ingredient. Each ingredient can have only one vendor. If more than one vendor supplies an item, such as is with bid items, you can create a “Bid” vendor. Add new vendors to the VENDOR file (#113.2) through this field or through Enter/Edit Vendor (VE). You can sort many reports by vendor, when this field is completed for all ingredients*.*

> Stock Number: The stock number is not a required entry. It may be 1-16 characters in length. Federal Stock Numbers are on DLA and Depot Federal supply items in the file. Enter a stock number, if available, on any added ingredients. This field is currently not used, but is for a future version for food ordering and inventory. This field also accepts alphabetical characters to use to enter a specific brand name as an added identifier for an ingredient.

> Unit of Purchase (U/P): The Unit of Purchase (U/P) is a required entry that must be two characters in length. The U/P is the unit in which an ingredient is purchased from the vendor. This unit is the same as the “Unit of Purchase” on each item in the Nutrition Cost Report. It is the unit received by the stock employee.

> Note: Any changes to purchase units may affect issue and recipe units.

#### Examples

- BG – bag
- CN – can
- JR - jar
- BT – bottle
- CO – container
- QT - quart

> Date Cost Last Updated: This field contains the date the cost of the ingredient was last updated.

- If the cost is updated through the Enter/Edit Ingredient option, you must enter a new date.
- If cost is updated through Inventory, the Enter/Edit Current Ingredient QOH option, this date is automatically updated.
- When adding a new ingredient, today's date displays.
- When editing cost through this option, enter a new date.

> Price/Unit of Purchase: The Price/Unit of Purchase is not a required entry. Enter a cost 0-9999, to 3 decimals, for a purchase unit of this ingredient. However, if entered, it is used in computing Total Ingredient Cost as listed on the Projected Usage (PU) production report, Recipe (portion) Cost as displayed under List Recipes (RL), and Inventory On Hand cost as listed on the Inventory Worksheet/Report (PW). Remember to edit the “Date Cost Last Updated:” field if cost is edited.

> Ordering Multiple (of U/P): The ordering multiple is the number of purchase units by which you must order an item. Enter vendor-required ordering multiple, 0-9999 with no decimals. This is not a required entry but may be used in the future when linked to IFCAP.

#### Example

> If purchasing chocolate syrup in \#10 cans from a local vendor, you normally have to purchase a case of six \#10 cans. If the purchase unit is CN, the ordering multiple entered is 6 (six). If the purchase unit is CS, the ordering multiple is 1 (one).

> Nutrition Unit of Issue: The Nutrition Unit of Issue is a required entry that must be 2-12 characters in length. The unit of issue designates the unit in which an ingredient is requisitioned from the Nutrition Storeroom or the way the Ingredient Control Unit employee removes items from the shelf. Approximately 180 entries are provided with the UNITS file (#119.1). Create new issue units through this field or through the Enter/Edit Units (UE) option.

#### Examples

> o CS – 1000

- 2# CAN
- 12-oz PKG
- 1# BOX
- 20 oz BTL
- 16-oz CAN

> The Nutrition Unit of Issue may be the same unit as the Unit of Purchase, but is usually described in more detail.

> No. of Issue Units in a U/P: This field is a required entry that designates how many Nutrition Units of Issue are in a Unit of Purchase (U/P). Enter a number between 0 and 9999 for issue units in a unit of purchase for this ingredient.

#### Examples

- If the Nutrition Unit of Issue is a 50 oz can of soup and the Unit of Purchase is a CN, then the number of Issue Units in a U/P is 1.
- If the Nutrition Unit of Issue is PKG (package) for sugar substitute and the Unit of Purchase is a CS (that contains 1000 pkgs), then the number of Issue Units in a U/P is 1000.
- If the Nutrition Unit of Issue is LB for sugar and the Unit of Purchase is a BG (that contains 25# of sugar), then the number of Issue Units in a U/P is 25.
- If the Nutrition Unit of Issue is LB for frozen beef stew and the Unit of Purchase is LB, then the number of Issue Units in a U/P is 1.

> It is recommended that if a food item is received in different package weights each time it is ordered, e.g., Frozen Beef Stew, then it is best to enter the Nutrition Unit of Issue in LBs and the Unit of Purchase in LBs so that the database does not continuously need changing.

> This field is also used to generate purchase order amounts on Projected Usage (PU).

> Recipe Unit: This is a required field. Recipe unit specifies the types of measure that you can apply to an ingredient in a recipe. There are three types of measures: GAL (volume), LB (weight) or Each. Each ingredient in the INGREDIENT file (#113) has one corresponding Recipe Unit. The Recipe Unit restricts that ingredient to the one type of measure for all recipes. If a recipe requires the same ingredient measured in a different way, create a new ingredient with a different recipe unit.

#### Example

> The Recipe Unit for bulk soy sauce is GAL (gallon). This establishes volume as the type of measure. All recipes containing soy sauce must be written in one of the various volumetric units, e.g., gallons, quarts, pints, cups, ounces. Recipes requiring soy sauce in any other measure would require a separate soy sauce ingredient with a different Recipe Unit, e.g., EACH for individually packaged soy sauce.

> Do not change the recipe units for ingredients sent with the Nutrition and Food Service package without considering the impact on the RECIPE file (#114).

> Whenever a Recipe Unit is entered or changed, an audible “beep” is sounded and a warning prompt displays.

> Warning: A change in the Recipe Unit impacts the RECIPE data considerably!

> \# of Rec Units/Issue Unit: This a required entry that represents the number of recipe units (LB, GAL, EACH) per Nutrition Issue Unit. It is a number between .001 and 9999.

#### Examples

- If the recipe unit for oatmeal is LB (pound) and the Nutrition Storeroom Clerk issues (pulls) a 2 LB carton of oatmeal from the shelf, the \# of Recipe Units/Issue Unit is 2.
- If the Recipe Unit for Ketchup is EACH and the Nutrition Storeroom Clerk issues a CS of 2000, then the \# of Recipe Units/Issue Unit is 2000.
- If the Recipe Unit for milk is GAL (gallon) and the Nutrition Storeroom Clerk issues in QT containers, then the \# of Recipe Units/Issue Unit is .25.
- If the Nutrition issue unit is changed, also adjust the \# of Recipe Units/Issue Unit.

> This field is very important because it describes the relationship between ingredient quantities in recipes and total quantities pulled from storerooms.

> Note: Quantity errors on storeroom reports may be due to errors in this field.

> Weight of Recipe Unit in Lbs.: The data in this field is required to perform nutrient analysis of recipes. It is not a required field but you may want to automate recipe and meal analysis. Enter a weight of 0-999 with up to 3 decimals. For each ingredient, enter the actual weight in pounds.

#### Examples

- If the recipe unit is pound, enter 1 for weight.
- If recipe unit is gallon, enter 8 (eight pounds per gallon). This is the standard for water; if the ingredient is heavier or lighter than water, a different weight is entered.
- If the recipe unit is Each, such as 1-each 4 oz juice, or 1-each 1 oz syrup, or 1-each 1/2 oz catsup, enter the weight as follows, .25 for juice, .062 for syrup or .031 for catsup. When Each units are expressed as volume, again consider whether the item is heavier or lighter than water, and weigh if necessary.

> Nutrient Data Reference: The Nutrient Data Reference field uses data in the FOOD NUTRIENTS file (#112). Enter the Food Nutrient item that most closely approximates this cooked ingredient. This entry is the default nutrient when performing a nutrient analysis of a recipe containing this ingredient. If this ingredient is always served as a raw ingredient, enter a raw food nutrient item rather than a cooked one. The nutrient program automatically makes adjustments for edible portion. Edit the default nutrient as necessary.

> Storage Location: The storage location is not a required entry. This field represents the location where ingredients are stored. It must be a location already created in the STORAGE LOCATION file (#113.1). If this field is completed for all ingredients, you can sort many reports by Storage Location, such as the inventory worksheet. Create new storage areas only through the Enter/Edit Storage Locations (LE) option.

> Thaw Days: This field is not a required entry and is currently not functional. A list of items to thaw prior to production days is planned for the future, including the number of days required to thaw the ingredient. The Thaw Days field is a number, 0-3 with no decimals.

> Food Group: The Food Group is a required entry. It designates the Nutrition Food Group number and must be a whole number between 1 and 6 with no decimals. It is used to sort ingredients in reports, such as the Inventory Report.

> Inventory: This field is not a required entry but must be completed to use the Nutrition Inventory options. Enter YES if this ingredient is an inventoried item and you want it to display on the Inventory Worksheet. If answered YES, the On - Hand Issue units field displays. A NO entry or entering a return indicates that this item will not be inventoried and the prompt sequence ends. Seasonal items, or one time use items purchased and used within the same month, may be items you do not want inventoried.

> Date QOH Last Updated: This field contains the date the quantity-on-hand was last updated. To update the quantity through this option, you must enter a new date. If you update the quantity using the Enter/Edit Current Ingredient QOH (QE) option, this date is automatically updated.

> On Hand (In U/P): This field contains the number of units of purchase that are currently in inventory for this ingredient. Enter a quantity 0-99999 with two decimals.

> Do you want to re-cost recipes?: It is a required field. This prompt displays each time an ingredient or group of ingredients is added or edited. This is a reminder to keep the RECIPE file (#114) updated with the most current ingredient costs.

- If YES is entered, the program automatically re-costs all recipes. “Done ...” displays when re-costing is complete.
- If cost or unit fields are not changed, enter NO to skip re-costing recipes.

> AMERICAN BAKERIES AMERICAN HOSPITAL SUPPLY

> ....

> FLAVO-O-RICH

> MARIO'S DISTRIBUTORS MILIANI

> '^' TO STOP: ^

> You may enter a new VENDOR NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH PUNCTUATION

> VENDOR: NFSMEAL,One DISTRIBUTORS

> STOCK NUMBER: \<RET\>

> UNIT OF PURCHASE (U/P): LB// \<RET\>

> DATE COST LAST UPDATED: MAR 23,2005// \<RET\> (MAR 23, 2005)

> PRICE/UNIT OF PURCHASE: 2.39

> ORDERING MULTIPLE (OF U/P): 1

> NUTRITION UNIT OF ISSUE: LB// \<RET\>

> NO. OF ISSUE UNITS IN A U/P: 1// \<RET\>

> RECIPE UNIT: LB// \<RET\>

> \# OF REC UNITS/ISSUE UNIT: 1// \<RET\>

> WEIGHT OF RECIPE UNIT IN LBS.: 1// \<RET\>

> NUTRIENT DATA REFERENCE: BEEF, COMPOSITE OF TRIMMED CUTS, ALL GRADES, COOKED// \<RET\>

> STORAGE LOCATION: FREEZER 1

> THAW DAYS: \<RET\>

> FOOD GROUP: 1// \<RET\>

> INVENTORY?: Y YES

> DATE QOH LAST UPDATED: MAR 23,2005// \<RET\> (MAR 23, 2005) ON HAND (IN U/P): 10

> Select INGREDIENT NAME: \<RET\>

#### IN List Ingredients - Nutrient Data \[FHING52\]

> The List Ingredients – Nutrient Data option is a 132-column report that lists the nutrient data from the INGREDIENT file (#113). Data from the following fields are included: Ingredient Name, Nutrient Data Reference, and its associated Recipe Unit and Weight of Recipe Unit in Lbs. You can sort this list A (Alphabetically), F (Food Group), or V (Vendor).

#### Example - alphabetical

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Select OPTION NAME: FHING52 List Ingredients - Nutrient Data List Ingredients - Nutrient Data</p>
<p>Sort: (A=Alphabetically F=Food Group V=Vendor) F// A The list requires a 132 column printer.</p>
<p>Select LIST Printer: HOME// TELNET</p>
<p>3-Feb-05 8:13am I N G R E D I E N T N U T R I E N T D A T A Page</p>
<p>1</p>
<p>NAME NUTRIENT DATA REFERENCE</p>
<p>REC UNIT WT IN LBS.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>--</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALLSPICE</p>
</blockquote></td>
<td><blockquote>
<p>ALLSPICE, GROUND</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AMIN-AID, ORANGE</p>
</blockquote></td>
<td><blockquote>
<p>AMIN AID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EACH 0.325</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AMIN-AID, STRAWBERRY</p>
</blockquote></td>
<td><blockquote>
<p>AMIN AID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EACH 0.325</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANTIOXIDANT COMPOUND</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLE RINGS, SPICED, UNPEELED, SYRUP PAK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EACH</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLES, BKD SPICED, CND, WHOLE CORED W/SYRUP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EA</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLES, CND, SLICED, PEELED</p>
</blockquote></td>
<td><blockquote>
<p>APPLES, CND, SWEETENED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLES, DEHYD, SLICED</p>
</blockquote></td>
<td><blockquote>
<p>APPLES, DRIED, UNCKD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLES, FRESH</p>
</blockquote></td>
<td><blockquote>
<p>APPLES, RAW</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EACH 0.304</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLESAUCE, CND, DIET</p>
</blockquote></td>
<td><blockquote>
<p>APPLESAUCE, CND, UNSW, WO/VIT C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLESAUCE, CND, SWEETENED</p>
</blockquote></td>
<td><blockquote>
<p>APPLESAUCE, CND, SWEETENED,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WO/SALT LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APRICOT HALVES, CND, SYRUP PAK</p>
</blockquote></td>
<td><blockquote>
<p>APRICOTS, CND, HEAVY SIRUP,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W/SKIN LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APRICOT HALVES, CND, WATER PAK</p>
</blockquote></td>
<td><blockquote>
<p>APRICOTS, CND, WATER PACK,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W/SKIN LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APRICOT PUREE, DIETETIC</p>
</blockquote></td>
<td><blockquote>
<p>APRICOTS, PUREED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APRICOTS, WHOLE, CND, SYRUP PAK</p>
</blockquote></td>
<td><blockquote>
<p>APRICOTS, CND, HEAVY SIRUP,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W/SKIN LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ASPARAGUS PUREE, GREEN, DIET</p>
</blockquote></td>
<td><blockquote>
<p>ASPARAGUS, PUREED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### IP List Ingredients - Purchasing Data \[FHING51\]

> The List Ingredients – Purchasing Data option is a 132-column report that lists data from the INGREDIENT file (#113) associated with purchasing the item: Stock Number, Price/Unit of Purchase, Vendor, Unit of Purchase, etc. You can sort this list A (Alphabetically), F (Food Group), or V (Vendor).

#### IR List Ingredients - Recipe Data \[FHING5\]

> The List Ingredients – Recipe Data option is a 132-column report that lists all the data related to recipes in the INGREDIENT file (#113). The following fields are included: Ingredient Name, Supply Description, Stock Number, Storage Location (LOC'N), Thaw Days, Unit of Purchase (U/P), No. of Issue Unit in U/P (Iss/UP), Nutrition Unit of Issue (Issue), \# of Recipe Units/Issue Unit (REC/ISS) and Recipe Unit (REC). You can sort this list A (Alphabetically), F (Food Group), or V (Vendor).

#### Example – Food Group

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Sort: (A=Alphabetically F=Food Group V=Vendor) F// <strong>&lt;RET&gt;</strong></p>
<p>The list requires a 132 column printer. Select LIST Printer: HOME// (Printer name)</p>
<p>3-Feb-05 9:14am I N G R E D I E N T N U T R I E N T D A T A Page 1</p>
<p>Food Group: MEAT PRODUCTS</p>
<p>NAME NUTRIENT DATA REFERENCE</p>
<p>REC UNIT WT IN LBS.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>BEEF LIVER BEEF, LIVER, FRIED</p>
<p>LB 1.000</p>
<p>BEEF PUREE, W/ BEEF BROTH, DIET, LO NA BEEF, PUREED LB 1.000</p>
<p>BEEF STEW, CND, R-T-S BEEF AND VEGETABLE STEW, CND LB 1.000</p>
<p>BEEF, BONELESS, FROZEN, TOP ROUND BEEF, ROUND, TOP ROUND, GOOD, TRIMMED, B LB 1.000</p>
<p>BEEF, CORNED, FRZ BEEF, CORNED, BONELESS, CKD LB 1.000</p>
<p>BEEF, CUBED STEAKS, FRZN BEEF, COMPOSITE OF TRIMMED CUTS, ALL GRA LB 1.000</p>
<p>BEEF, GROUND, FROZEN BEEF, GROUND, REGULAR, BAKED, WELL DONE LB 1.000</p>
<p>BEEF, PATTIES, FRZ BEEF, GROUND, PATTIES, FROZEN, BROILED, EACH 0.187</p>
<p>BEEF, STEWING, FRZN RAW, DICED BEEF, COMPOSITE OF TRIMMED CUTS, ALL GRA LB 1.000</p>
<p>BEEF, TOP RND, FRESH BEEF, ROUND, TOP ROUND, GOOD, TRIMMED, B LB 1.000</p>
<p>BOLOGNA SAUSAGE, BOLOGNA, BEEF &amp; PORK</p>
<p>LB 1.000</p>
<p>CABBAGE AND BEEF ROLLS W/TOM SCE, FZN, HEAT AND SE LB</p>
<p>CHICKEN ALA KING, CND, HEAT AND SERVE LB 1.000</p>
<p>CHICKEN ALA KING, FROZEN LB</p>
<p>CHICKEN BREAST, FROZEN, READY-TO-COOK CHICKEN, BREAST, MEAT&amp;SKIN,</p>
<p>ROASTED LB 1.000</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CHICKEN LEG, FROZEN, READY-TO-COOK CHICKEN, LEG, MEAT&SKIN, ROASTED LB 1.000

> CHICKEN PUREE, W/CHICKEN BROTH, DIET LO NA CHICKEN, PUREED LB 1.000

> CHICKEN THIGHS, FZN CHICKEN, THIGH, MEAT&SKIN, ROASTED LB 1.000

> CHICKEN, CND, BONED, DICED CHICKEN, CND, MEAT ONLY, BONED, W/BROTH LB 1.000

> CHICKEN, CND, BONED, DICED, DIET LB

> CHICKEN, DRUMS, FZN LB

> CHICKEN, FROZEN, BROILER OR FRYER, READY TO COOK CHICKEN, MEAT&SKIN, ROASTED LB 1.000

> CHICKEN, FROZEN, QUARTERED, READY-TO-COOK CHICKEN, MEAT&SKIN, ROASTED LB 1.000

> CHICKEN, PULLED, UNSALTED CHICKEN, MEAT ONLY, ROASTED LB 1.000

> CHICKEN/VEGETABLES, CND, CHOW MEIN CHOW MEIN, CHICKEN, WO/NOODLES, CND LB 1.000

> CHILI CON CARNE, CND, W/BEANS CHICKEN POTPIE, FRZ, COMMERCIAL, UNHEATE LB 1.000

> CHILI CON CARNE, CND, W/O BEANS CHILI CON CARNE, CND, WO/BEANS LB 1.000

> CHIPPED BEEF W/WHITE SAUCE, CND, R-T-S BEEF, CHIPPED BEEF, DRIED, CREAMED LB 1.000

> CLAM CHOWDER, COND, MANHATTAN STYLE SOUP, CLAM CHOWDER, MANHATTAN, W/TOMATO GAL 8.854

> CLAM CHOWDER, COND, NEW ENGLAND STYLE SOUP, CLAM CHOWDER, NEW ENGLAND, W/MILK, GAL 8.854

> CLAMS, CND, MINCED CLAMS, CND, DRAINED SOLIDS LB 1.000

> COD RAW BREADED FISH STICKS, FRZ, CKD

> LB 1.000

> CORNED BEEF, CND BEEF, CORNED, BONELESS, CND LB 1.000

> EGG MIX, FROZEN, WHOLE EGGS EGGS, WHOLE, LARGE, RAW, FRESH, AND FRZ LB 1.000

> EGG MIX, POWDER FORM EGGS, WHOLE, DRIED

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>LB 1.000</p>
<p>EGG SUBSTITUTE EGG SUBSTITUTE, FRZ</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GAL</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>8.466</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>EGGS, SHELL, FRESH AND FRZ</p>
</blockquote></td>
<td><blockquote>
<p>EACH</p>
</blockquote></td>
<td><blockquote>
<p>0.097</p>
</blockquote></td>
<td><blockquote>
<p>EGGS, WHOLE, MED, RAW, FRESH,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>FARINA-DM LB</p>
<p>FRANKFURTERS, FRESH</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>FRANKFURTERS, CKD</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>LB 1.000</p>
<p>HAM PUREE, SALTED LB</p>
<p>HAM SMKD, BONELESS HAM, BONELESS, REGULAR, ROASTED LB 1.000</p>
<p>HAM, COOKED, FRZ HAM, BONELESS, REGULAR, ROASTED LB 1.000</p>
<p>HASH, CORNED BEEF, CND, COOKED BEEF, CORNED BEEF HASH, CND, W/POTATO LB 1.000</p>
<p>KNOCKWURST SAUSAGE, KNOCKWURST</p>
<p>LB 1.000</p>
<p>LAMB LEG ROAST, BONELESS, FRESH LAMB, LEG, CHOICE, TRIMMED, ROASTED LB 1.000</p>
<p>LAMB PUREE, DIET, LOW NA LB</p>
</blockquote></td>
</tr>
</tbody>
</table>

> LASAGNA WITH MEAT SAUCE, FROZEN, COOKED LB 1.000

> LIVER PUREE, DIET, LOW SODIUM LIVER, PUREED LB 1.000

> LIVER, BEEF, FRESH FROZEN BEEF, LIVER, FRIED B 1.000

> MACARONI AND CHEESE, FROZEN MACARONI AND CHEESE, BAKED FR HOME RECIP LB 1.000

> MACARONI WITH CHEESE SAUCE, CND MACARONI AND CHEESE, CND LB 1.000

> OYSTERS, CND OYSTERS, CND

> LB 1.000

> PORK CHOPS, BONELESS PORK, CENTER LOIN, TOT ED, ROASTED LB 1.000

> PORK PUREE, DIET, LO NA LB

> PORK PUREE, W/SALT ADDED LB

> PORK SLICES PORK, COMPOSITE CUTS, ROASTED

> EACH 0.265

> PORK, BOSTON BUTT, BONELESS PORK, BLADE, BOSTON, TRIMMED, ROASTED LB 1.000

> PORK, CUTLETS, FROZEN, PREFAB, BREADED, RAW LB

> PORK, GROUND FROZEN PORK, COMPOSITE CUTS, ROASTED LB 1.000

> PORK, HAM, FROZEN, UNCURED PORK, COMPOSITE CUTS, ROASTED LB 1.000

> PORK, LOIN ROAST PORK, CENTER LOIN, TRIMMED, ROASTED LB 1.000

> RAVIOLI WITH CHEESE SAUCE, CND LB

> RAVIOLI WITH MEAT SAUCE, CND LB

> SALAMI SAUSAGE, SALAMI, BEEF & PORK,

> CKD LB 1.000

> SALMON, CANNED SALMON, PINK, CND, SOL+LIQ, W/SALT LB 1.000

> SALMON, CND, DIET, WATER-PAK LO SODIUM SALMON, PINK, CND, SOL+LIQ, WO/SALT LB 1.000

> SARDINES, CND SARDINES, CND, IN OIL, DRAINED SOLIDS LB 1.000

> SAUSAGE PATTIES, RAW FZN SAUSAGE, PORK, LINKS OR BULK, CKD LB 1.000

> SAUSAGE, ITALIAN SAUSAGE, ITALIAN, CKD

> LB 1.000

> SAUSAGE, SMOKED SAUSAGE, SMOKED LINK SAUSAGE, PORK & BEE LB 1.000

> STUFFED GREEN PEPPERS IN SAUCE, CND, HEAT AND SERV STUFFED PEPPERS W/ TOM SAUCE LB 1.000

> TAMALES, BEEF, CND, W/CHILI GRAVY LB

> TUNA, CND, DIET TUNA, LIGHT MEAT, CANNED IN WATER, WO/SA LB 1.000

> TUNA, CND, LIGHT, CHUNK STYLE TUNA, LIGHT MEAT, CANNED IN OIL LB 1.000

> TURKEY BREAST, UNSALTED TURKEY BREAST, PREBASTED, MEAT&SKIN, ROA LB 1.000

> TURKEY PUREE, DIET TURKEY, PUREED

> LB 1.000

> TURKEY PUREE, W/SALT TURKEY, PUREED LB 1.000

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 9%" />
<col style="width: 16%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>TURKEY, BONELESS, FROZEN, RAW, UNSEASONED SEASONED, L LB 1.000</p>
<p>TURKEY, CND, BONED, DICED</p>
</blockquote></th>
<th><blockquote>
<p>TURKEY ROAST, BONELESS, FRZ,</p>
<p>TURKEY, CND, MEAT ONLY, W/BROTH</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VEAL PUREE, DIET</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>VEAL, PUREED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LB 1.000</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>VEGETABLE PROTEIN MEAT SUBSTITUTE LB</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### LE Enter/Edit Storage Locations \[FHING4\]

> The Enter/Edit Storage Locations option allows you to add and modify storage locations in the STORAGE LOCATION file. The STORAGE LOCATION file (#113.1) contains a list of locations within Nutrition and Food Service where perishable and non-perishable food items are stored, e.g., refrigerators, freezers, storerooms, etc. Locations include areas where you do inventory. The Storage Location field discussed under Enter/Edit Ingredients (IE) uses the data in the STORAGE LOCATION file (#113.1). Each facility must create a site-specific list of Storage Locations.

> Storage Location Name: Enter unique names 3-15 characters in length. Data in this file is not required; however, if each ingredient is assigned a storage location, you can sort specific reports by storage area. This is very useful when completing Inventory Worksheets.

> Code: This is a required field. Enter the abbreviated name for this location.

> Print Order: This is a required field. Enter a number 1-49, no decimals. This number determines the print order of reports when sorted by storage location.

#### LL List Storage Locations \[FHING8\]

> The List Storage Locations option is an 80-column report that lists all storage location names, codes, and print orders created using the Enter/Edit Storage Locations (LE) option.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 16%" />
<col style="width: 31%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE: (Printer name) STORAGE LOCATIONS</p>
<p>NAME CODE</p>
</blockquote></th>
<th><blockquote>
<p>PRINT ORDER</p>
</blockquote></th>
<th><blockquote>
<p>FEB 3,2005 10:40</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DRY STORAGE DRY</p>
</blockquote></td>
<td>1</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FREEZER FR</p>
</blockquote></td>
<td>2</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRODUCE BX A125 PROD</p>
</blockquote></td>
<td>5</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>THAW BOX A-127 THAW</p>
</blockquote></td>
<td>5</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAIRY BOX A126 DAIRY</p>
</blockquote></td>
<td>6</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KITCHEN KIT</p>
</blockquote></td>
<td>7</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MEAT FRZR MEAT</p>
</blockquote></td>
<td>10</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VEG FRZR VF</p>
</blockquote></td>
<td>11</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### QE Enter/Edit Current Ingredient QOH \[FHING12\]

> The Enter/Edit Current Ingredient QOH option allows you to build the data for the Inventory program for Nutrition Food Production. You use the Display Ingredient Inventory List (QW) option along with it to build the inventory data.

> The first step in using the Inventory program is to review the data in the INGREDIENT file(#113) using the option List Ingredients - Purchasing Data (IP) and identify all ingredients that are to be inventoried. Then use the Enter/Edit Ingredients (IE) option to enter a YES or NO at the “Inventory?” prompt. Ingredients only display on the worksheet or report if YES is entered in the Inventory field.

> You are now ready to generate the Inventory Worksheet (QW Display Ingredient Inventory List) to use for the physical inventory. This worksheet is generated by storage location to facilitate data collection. The data is entered through the Enter/Edit Current Ingredient QOH (QE) option. While entering quantity, you are also prompted to update cost for each ingredient if you elect to do both functions at one time.

> Once all data is entered, select the report prompt to generate a costed inventory report by Food Group through the Display Ingredient Inventory List (QW) option.

> Recommended Inventory Procedure:

1.  Print the Inventory Worksheet by Storage Location.
2.  Record the price changes during month in red.
3.  Use the worksheets for the physical inventory at end of the month.
4.  Select sort by Storage Location when entering current inventory on hand. Ingredients are listed in same sequence as the worksheet so data entry is quick.
5.  Edit the cost while entering quantity as needed.
6.  Print the Inventory report, sorted by Food Groups to obtain costed inventory.

> The Enter/Edit Current Ingredient QOH option provides an easy mechanism for entering inventory quantities for all ingredients. Each ingredient is displayed separately with the date the last quantity was entered. Ingredients display alphabetically, sorted by storage location or food group. You can elect to enter data for one food group or storage location at a time or loop through all groups and/or locations. Cost is updated while entering quantity if a YES is entered at the first prompt for this option. The cost per unit of purchase displays, as well as the Inventory Quantity on Hand field. Any data entered in this option automatically updates the corresponding fields in the INGREDIENT file (#113).

> Note: Data is stored in the Inventory Program only until the next update. Anytime data is entered or edited, you need to print an Inventory Report for the files. Subsequent changes delete all previous data.

> Cost with QOH: Enter YES to update price while entering quantities. Answer NO and you are not prompted for cost/price information.

> Current QOH by Individual Ingredient: This is a required field. Answer YES to enter quantity by individual ingredient. Answer NO to enter quantity by looping through all ingredients sorted by food group or storage area.

> Ingredient Name: Enter an ingredient name. The ingredient name and the date the quantity was last entered, display.

> Price/Unit of Purchase: Enter the price per purchase unit with up to 3 decimals. the last price entered displays As a default,

> Note: This prompt only displays if Y is selected at the first prompt.

> On Hand (in U/P): Enter the quantity on hand, with up to 2 decimals. The last QOH displays as the default.

> Example entry \#1:

> Example entry \#2:

> ON HAND (IN U/P): 11// \<RET\>

> Ingredient: CHEESE, AMER/SWISS

> QOH LAST UPDATED ON 21-Mar-05 ON HAND (IN U/P): 15// \<RET\>

> Ingredient: CHEESE, AMERICAN

> QOH LAST UPDATED ON 21-Mar-05 ON HAND (IN U/P): 200// \<RET\>

> Ingredient: CHEESE, CHEDDAR AGED, HARD, BRICK QOH LAST UPDATED ON 21-Mar-05

> ON HAND (IN U/P): 03// \<RET\>

> Ingredient: CHEESE, COTTAGE

> QOH LAST UPDATED ON 21-Mar-05 ON HAND (IN U/P): 5// \<RET\>

> Ingredient: CHEESE,CHEDAR, MODIFIED FAT & NA QOH LAST UPDATED ON 21-Mar-05

> ON HAND (IN U/P): 50// \<RET\>

> Ingredient: CHEESECAKE

> QOH LAST UPDATED ON 9-Dec-04 ON HAND (IN U/P): 0// \<RET\>

> Ingredient: CREAM, HALF & HALF, QUART

> QOH LAST UPDATED ON 2-Feb-05 ON HAND (IN U/P): 2// \<RET\>

> Ingredient: DESSERT CUP, BOSTON CREAM

> QOH LAST UPDATED ON 21-Mar-05 ON HAND (IN U/P): 6// \<RET\>

> Ingredient: ICE CREAM, CHOCOLATE, IND

> QOH LAST UPDATED ON 21-Mar-05 ON HAND (IN U/P): 140// \<RET\>

> Ingredient: ICE CREAM, STRAWBERRY, IND

> QOH LAST UPDATED ON 21-Mar-05 ON HAND (IN U/P): 180// \<RET\>

> Ingredient: ICE CREAM, SUNDAE, CHOCOLATE, IND QOH LAST UPDATED ON 21-Mar-05

> ON HAND (IN U/P): 24// \<RET\>

> Ingredient: ICE CREAM, SUNDAE, STRAWBERRY, IND QOH LAST UPDATED ON 21-Mar-05

> ON HAND (IN U/P): 0// \<RET\>

> Ingredient: ICE CREAM, VANILLA, IND

#### QW Display Ingredient Inventory List \[FHING13\]

> The Display Ingredient Inventory List option allows you to create an 80-column worksheet for taking physical inventories and generating a costed inventory report. This is the Inventory Worksheet. You can sort the ingredients by Food Group or Storage Area. For taking physical inventory, sorting by storage area is most useful. The worksheet consists of the IFCAP Master Item Number (MIN), name of ingredient, unit of purchase, item cost, date last updated, QOH last month, and a blank line for input of current inventory quantity on hand. All data on the worksheet comes from information stored in the INGREDIENT file (#113).

> The Inventory Report displays ingredients alphabetically, sorted and subtotaled by Food Group. The report creates columns accordingly: MIN, name of ingredient, unit of purchase, item cost, current quantity on hand and total cost. You can print this report for one food group or ALL. Total cost for all food groups only prints if ALL is used.

> The data from this report is used to complete the Cost of Meals Served Report (SP) and AMIS

> 224\. Always print this report after the ingredients are updated, because quantities are not stored. Whenever any data is changed, previous data is deleted.

> Select Food Group: This is a required field. Enter a food group number or ALL. Each group prints on a separate sheet.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>BEEF TIPS, FROZ</p>
</blockquote></th>
<th></th>
<th>CS</th>
<th>28.000</th>
<th><blockquote>
<p>19-Mar-99</p>
</blockquote></th>
<th>0.00</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2111</p>
</blockquote></td>
<td><blockquote>
<p>BEEF, CUBED STEAKS,</p>
</blockquote></td>
<td><blockquote>
<p>FROZ</p>
</blockquote></td>
<td>CS</td>
<td>29.030</td>
<td><blockquote>
<p>19-Mar-99</p>
</blockquote></td>
<td>0.00</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2351</p>
</blockquote></td>
<td><blockquote>
<p>BEEF, GROUND, FROZ</p>
</blockquote></td>
<td></td>
<td>CS</td>
<td>22.303</td>
<td><blockquote>
<p>19-Mar-99</p>
</blockquote></td>
<td>05.00</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2350</p>
</blockquote></td>
<td><blockquote>
<p>BEEF, PATTIES, FROZ</p>
</blockquote></td>
<td></td>
<td>CS</td>
<td>11.630</td>
<td><blockquote>
<p>19-Mar-99</p>
</blockquote></td>
<td>35.00</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 35%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>2110</th>
<th><blockquote>
<p>BEEF, ROAST</p>
</blockquote></th>
<th>CS</th>
<th>78.520</th>
<th><blockquote>
<p>19-Mar-99</p>
</blockquote></th>
<th>131.00</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2224</td>
<td><blockquote>
<p>CHICKEN, FROZEN, FRYER, IQF</p>
</blockquote></td>
<td>CS</td>
<td>30.700</td>
<td><blockquote>
<p>19-Mar-99</p>
</blockquote></td>
<td>1.50</td>
<td></td>
</tr>
<tr class="even">
<td>6587</td>
<td><blockquote>
<p>EGG MIX, WHOLE EGGS*</p>
</blockquote></td>
<td>CS</td>
<td>27.003</td>
<td><blockquote>
<p>19-Mar-99</p>
</blockquote></td>
<td>1.75</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>TOTAL: 3153.05</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### RL List Recipes Containing an Ingredient \[FHING11\]

> The List Recipes Containing an Ingredient option is an 80-column report that identifies all recipes in the RECIPE file (#114) containing a specific ingredient. The option first asks you to select the ingredient name and then lists all recipes containing that ingredient, the number of portions, the amount, the meals, and the menu cycle. Use the RE Enter/Edit Recipes option in Recipe Management to remove ingredients before deleting any ingredient from the INGREDIENT file (#113). Use the Enter/Edit Ingredients (IE) option to delete ingredients.

#### Example

> Some rice recipes are entered using “instant rice”. The facility decides to use only “long grain rice”. This option helps identify all recipes that have the ingredient “instant rice” which then can be replaced with a “long grain rice” ingredient.

> Note: Always print the recipe list before deleting any ingredient and refer to it when removing deleted ingredients from recipes.

<table>
<colgroup>
<col style="width: 66%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select INGREDIENT NAME: <strong>PORK CHOPS, BONELESS</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select LIST Printer: HOME// <strong>&lt;RET&gt;</strong> HYPER SPACE RIGHT</p>
</blockquote></th>
<th>MARGIN:</th>
<th><blockquote>
<p>80//</p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>5-Feb-05 10:16am I N G R E D I E N T U S A G E</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>Page</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PORK CHOPS, BONELESS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Recipe # Portions Amount</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>BAKED/GRILLED PORK CHOPS - 1 100 31 LB, 8 OZ Meal: WK1 SU LU RST BEEF</p>
<p>Cycle: TEST BLK, Day 10, Noon Cycle: TEST BLK, Day 13, Noon Cycle: TEST BLK, Day 17, Noon Cycle: TEST BLK, Day 26, Evening Cycle: TEST INA, Day 3, Noon Cycle: CYCLE TEST, Day 1, Noon Cycle: TTRAY, Day 6, Evening Cycle: CYCLE 1, Day 1, Noon</p>
<p>Cycle: CYCLE 2, Day 1, Noon</p>
<p>BAKED/GRILLED PORK CHOP - 2 100 36 LB Meal: WK1 SU LU RST BEEF</p>
<p>Cycle: TEST INA, Day 3, Noon Cycle: CYCLE TEST, Day 1, Noon Cycle: TTRAY, Day 6, Evening Cycle: CYCLE 1, Day 1, Noon</p>
<p>Cycle: CYCLE 2, Day 1, Noon Meal: WK1 SU SP CUBAN SAND</p>
<p>Cycle: MY CYCLE, Day 22, Evening Cycle: MY CYCLE, Day 24, Evening Cycle: CYCLE TEST, Day 1, Evening Cycle: CYCLE TEST, Day 5, Evening Cycle: TTRAY, Day 3, Evening Cycle: CYCLE 1, Day 1, Evening</p>
<p>Cycle: CYCLE 2, Day 1, Evening Cycle: XMAS, Day 3, Evening Cycle: CYCLE 3, Day 2, Evening</p>
<p>LO SOD/LO PRO PORK CHOPS/SYRUP 9 2 LB</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### UE Enter/Edit Units \[FHING1\]

> The Enter/Edit Units option allows you to add and modify food items handled by an ingredient control employee in a storeroom location. The UNITS file (#119.1) contains all of the different ways food items are pulled by an ingredient control employee from a storeroom location.

> Approximately 180 unit entries come with the file. Use the List Units (UL) option to obtain a printout of the contents of the file. Any unit unique to the facility is added to the already existing Units data. The Nutrition Unit of Issue field, discussed under Enter/Edit Ingredients (IE), uses the data in the UNITS file. Unit name should indicate the measurement, count, and container type used by Nutrition and Food Service when issuing for production or service.

> Select UNITS NAME: Enter the name of the units with 2-12 characters in length.

#### Examples

- \#10 CN
- 6# BX
- GAL-JR
- CASE - 200
- CASE - 24

#### UL List Units \[FHING6\]

> The List Units option is an 80-column report that lists all units in the INGREDIENT file (#113). Many units are included with the package; however, you can add units using the Enter/Edit Units (UE) option or by the field Nutrition Unit of Issue using the Enter/Edit Ingredients (IE) option.

#### VE Enter/Edit Vendor File \[FHING2\]

> The Enter/Edit Vendor File option allows you to add or modify the VENDOR file.

> The VENDOR file (#113.2) contains a list of vendors' names, addresses, telephone numbers, and contact people for the service. Each facility must create their vendor listing in the file. The Vendor field, discussed under Enter/Edit Ingredient (IE), uses the listing in the VENDOR file (#113.2). Data in this file is not required; however, if each ingredient is assigned a vendor, you can sort specific reports by vendor. This is very useful when printing Projected Usage (PU) for ordering.

> Note: Include government sources and contracts as vendors, because food items on bid are acquired from more than one vendor, such as a *Frozen Meat Bid Contract* or *Frozen Vegetable Bid Contract*.

> Name: 3-30 characters in length, not numeric or starting with punctuation.

> 1<sup>st</sup> Address Line: 1-30 characters in length. 2<sup>nd</sup> Address Line: 1-30 characters in length. 3<sup>rd</sup> Address Line: 1-30 characters in length. City, State, Zip: 1-30 characters in length. Contact: 1-30 characters in length.

> Telephone: 1-20 characters in length.

#### VL List Vendors \[FHING7\]

> The List Vendors option is an 80-column report that lists all data in the VENDOR file (#113.2) created under the Enter/Edit Vendor File (VE) and Enter/Edit Ingredients (IE) options.

> Enter a printer name or press \<RET\> to print it to the screen.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 55%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Select LIST Printer: HOME// <strong>&lt;RET&gt;</strong> HYPER SPACE RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th rowspan="26"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>5-Feb-05 10:10am V E N D O R L I S T Page 1</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>NAME ADDRESS</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>AMERICAN BAKERIES</p>
</blockquote></th>
<th><blockquote>
<p>N. 56 ST</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSMEAL<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>TAMPA, FL 33618</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000-0000</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>AMERICAN HOSPITAL SUPPLY</p>
</blockquote></th>
<th><blockquote>
<p>W. 34 ST</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSMEAL<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>TAMPA, FL 33161</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>000-0000</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ARCHWAY</p>
</blockquote></th>
<th><blockquote>
<p>E. 13 AVE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSMEAL<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>BRANDON, FL 33567</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000-0000</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>B &amp; R</p>
</blockquote></th>
<th><blockquote>
<p>N. BIRD ST</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSMEAL<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>ST PETE , FL 45623</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>000-0000</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>BREAD CONTRACT</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CFS CONTINENTAL</p>
</blockquote></th>
<th><blockquote>
<p>W. BURGER DR</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SALLY HOUSEN</p>
</blockquote></th>
<th><blockquote>
<p>NEW PORT RICHIE, FL 22345</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>000-0000</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>DANISH BAKERY</p>
</blockquote></th>
<th><blockquote>
<p>DOWN ST</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSMEAL<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>CLEARWATER, FL 43389</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000-0000</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>DEPOT</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>DIETARY SPECIALITIES</p>
</blockquote></th>
<th><blockquote>
<p>SUNSET</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSMEAL<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>SARASOTA, FL 45200</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000-0000</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### XM Menu Cycle Management \[FHPRCM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CD</p>
</blockquote></th>
<th><blockquote>
<p>Menu Cycle Effective Dates [FHPRC2]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Menu Cycle [FHPRC1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CL</p>
</blockquote></td>
<td><blockquote>
<p>List Menu Cycle [FHPRC8]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CQ</p>
</blockquote></td>
<td><blockquote>
<p>Menu Cycle Query [FHPRC3]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CR</p>
</blockquote></td>
<td><blockquote>
<p>Input Recipe Menu [FHPRC14]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM</p>
</blockquote></td>
<td><blockquote>
<p>Display Meal Analysis [FHPRC13]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DP</p>
</blockquote></td>
<td><blockquote>
<p>Print Daily Diet Menus [FHPRC11]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Holiday Meals [FHPRC5]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Meals [FHPRC4]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td><blockquote>
<p>List Meal [FHPRC6]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MP</p>
</blockquote></td>
<td><blockquote>
<p>Edit Meal Production Diets [FHPRC9]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td><blockquote>
<p>Print Weekly Menu [FHPRC7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WR</p>
</blockquote></td>
<td><blockquote>
<p>Print Weekly Menu Blocks [FHPRC12]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Menu Cycle Management provides the ability to create multiple meals and menu cycles. Meals are used in different patterns by creating different menu cycles or by creating special holiday dates within a cycle. A holiday meal overrides a specified date in a normal cycle for that date only. The cycle returns to normal after that date. Meals are created using established recipes, recipe categories, service points, and production diets. Quantities produced for a meal are manipulated by adjusting the production diet code string or service point table. Other adjustments to the meal data provide food preference automation for the tray ticket program.

> You can print lists of meals or menu cycles, as well as daily/weekly menus and menu blocks. Once nutrients are entered in the RECIPE and INGREDIENT files, automated meal or daily/weekly menu analysis is possible.

#### Managing Menu Cycles

> The Menu Cycle Management (XM) program is the final link in the creation of the Food Management Program. You use three options in this section to create/build the data in the MENU CYCLE file (#116), MEAL file (#116.1), and HOLIDAY MEALS file (#116.3). The

> three options are Enter/Edit Meals (ME), Enter/Edit Menu Cycle (CE), and Enter/Edit Holiday Meals (HE). Data is not shipped with these files, which means you must create meals, menu cycles, and holiday meals.

> When a field points to a file, it uses the data in that file for selections.

- Files listed to the left use data in the Menu Cycle Management Program files.
- Files listed to the right supply the data for fields in the Menu Cycle Management options.
- Files that are incomplete, you need to populate (create the needed data for them) before beginning this section.

#### Diagram of the Relationship

- Daily menus for each day of a menu cycle are created by entering all recipes needed for a meal and assigning production diet codes and popularity percentages to each recipe.
- Menu cycles are created by designating starting date, number of days in cycle, and specific meal to be served for each day in the cycle.
- Holiday and/or special meals are created as regular meals, but are given a specific date and meal to be served. The holiday meal feature automatically substitutes a holiday meal at the proper time and all the production reports reflect it. The normal menu cycle resumes after the holiday.

> Once the MEAL and MENU CYCLE files are built, the Food Management Program is fully operational. You can generate the reports required to run the food production units. You can print the Daily Diet and Weekly Menus according to date and production diet. Energy Nutrient Analysis of a meal, a day, or a week is formulated by the Input Recipe Menu (CR) option. You can do analysis by production now. You can edit quantities and recipes that you added or deleted, to provide a complete automated analysis for a meal, a day, or a week.

7.  Create a meal worksheet for entering meals.
    - Meal Name
    - Recipe Names
    - Production Diet Codes
    - Service Points
8.  List all recipes for the designated meal. Indicate in each production diet column whether or not to serve the recipe to that production diet. Shorthand symbols are suggested on the worksheet.
9.  When entering production diet codes, it is helpful to enter them in the same sequence all the time. This allows you to quickly review the code string for accuracy and completeness, and makes data entry easier. After entry, all codes are reordered to the print order of the production diets for easy reference.
10. Enter all meals before creating complete Menu Cycles and printing menus.
11. Once all meals are completely entered, print the Daily Diet Menu (DP). This menu can help you quickly identify wrong or missing entries. Create a hard copy master file of menus for easy reference. This is helpful if production problems occur.
12. If the Daily Diet Menu does not work, check to be sure that:
    - The printer can print in compressed mode.
    - The file pointer fields (those fields that use data in other files) are answered correctly: i.e., print order.
    - The Production Facilities (FE) option “FULL NAMES ON DAILY MENU?:” is properly set.
13. Print the List Meal (ML) to check for notes on production problems. This allows you to quickly check production codes and popularity percentages for each recipe.
14. Use the Holiday Meals (HE) option to create meals for one-time changes. This does not alter the original menu cycle permanently and avoids the work of editing a cycle for one change and remembering to go back and return to the original meals.
15. Because menu cycle effective dates can be entered far into the future it is best to review Menu Cycle Effective Dates (CD) prior to an anticipated menu cycle change to verify implementation date.
16. Add-On Meals – Create standard meals with items routinely served at certain meals. You can easily add this grouping of food to other meals with minimal data entry.

#### Example

> Standard Breakfast Meal

> This meal includes recipes such as toast, margarine, jelly, milk, coffee, condiments, etc. Each recipe has a production diet code string and popularity percentages. This meal is added at the Add-On Meal prompt for all breakfast meals created. This Add-On feature eliminates the need to enter each of these food items separately for every breakfast meal created.

17. The Add-On Meal concept is used to create new meals easily. An established meal is renamed by entering the new name, bypassing the recipe prompt, and entering an existing meal at the Add-On prompt. This new meal is edited for minor recipe changes. This method greatly reduces data entry time.

> The only file you need to modify in Menu Cycle Management is the MEAL file. The Recipe Category field is in the MEAL file. This multiple allows you to characterize a recipe with a list of different recipe categories. The field contains the production diets to which the category applies.

> After installation, the field is populated with the DEFAULT CATEGORY field of the recipe in the RECIPE file and the existing production diets in the MEAL file. You can modify each recipe category and the production diets, as well as add the alternate and diabetic recipe categories, ENTREE II, ENTREE I AND II DB-X, and associate the production diet codes with them. The Diabetic exchanges only apply to tray tickets.

#### Steps to Follow

1.  Use the option Enter/Edit Meals (ME) to modify existing meals or create new meals.
2.  Add additional Recipe Categories (if needed). Include alternate, different characterization, and Diabetic categories.
3.  Associate production diets to each.
4.  Use the option List Meal (ML) to review for accuracy.
5.  Review and modify.

#### CD Menu Cycle Effective Dates \[FHPRC2\]

> The Menu Cycle Effective Dates option is for viewing effective dates only. When selected, the option displays all effective dates and menu cycle names. Be sure to check these dates, prior to beginning any cycle.

#### Example

> Note: You should check Effective Dates periodically. In the absence of another effective date for any of the cycles, the Fall cycle continues through Winter, Summer and Fall 2004, 2005, and so on.

#### CE Enter/Edit Menu Cycle \[FHPRC1\]

> The Enter/Edit Menu Cycle option allows you to edit the data in the MENU CYCLE file (#116). The file contains the names of menu cycles, the effective date each cycle begins, the number of days in each cycle and the pre-established meals for breakfast, noon, and evening. Meals for each day of a menu must be in the MEAL file (#116.1) (Enter/Edit Meals (ME) option) before you can create a menu cycle..

> Menu Cycle Name: The name must be 3-30 characters long and not starting with punctuation. The menu name may be descriptive to identify when the cycle is used. Each facility should determine menu cycle names to correspond with its own menu cycle system.

#### Examples

- Winter Cycle 05
- Spring/Summer Cycle II
- Cycle I

> No. Days in Cycle: This is a required field and refers to the number of days that make up a menu cycle. It must be a whole number, 1-365. Therefore, a menu cycle cannot be less than 1 day or more than 365 days in length.

#### Example

> A four week menu cycle would have 28 entered in this field.

> Effective Date: This date refers to the date that a menu cycle begins and is required. The menu cycle continues to repeat until a new menu cycle with a new effective date occurs.

> Day: This refers to the Day number in a menu cycle. The first day of a menu cycle should be numbered 1, the second day should be numbered 2 and so on. The last day number in a menu cycle should match the number of days in the menu cycle (see above, No. of Days in Cycle field).

> Meal fields: Breakfast Meal, Noon Meal, and Evening Meal fields are three required fields. These fields use data in the MEAL file (#116.1). Use the same Meal names you entered in the Enter/Edit Meals (ME) option. Enter the meal name that corresponds to the meal you want to serve.

#### Example

> BREAKFAST MEAL: CYI-WKI-SU-FRD EGG

#### CL List Menu Cycle \[FHPRC8\]

> The List Menu Cycle option allows you to print an 80-column report that lists all data entered under the Enter/Edit Menu Cycle (CE) option, except the effective date; view effective dates under the Menu Cycle Effective Dates (CD) option. This list is a quick reference for verifying meals data for each day of the menu cycle. Meal names are shortened to 23 characters to allow the list to print in 80-column format. You can send this report to a printer by entering a printer name or bring it to the screen by pressing \<RET\>.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 18%" />
<col style="width: 1%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select MENU CYCLE NAME: <strong>CYCLE I -</strong></p>
</blockquote></th>
<th><strong>05</strong></th>
<th></th>
<th></th>
<th></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select LIST Printer: HOME// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th><blockquote>
<p>HOME</p>
</blockquote></th>
<th><blockquote>
<p>RIGHT MARGIN: 80//</p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>3-Feb-05 11:00am M E</p>
</blockquote></th>
<th>N U C</th>
<th><blockquote>
<p>Y C L E</p>
</blockquote></th>
<th>Page</th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Day Breakfast Noon</p>
</blockquote></th>
<th></th>
<th>Evening</th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="5"><ol type="1">
<li><p>WK1 BR SUN OMELET OJ WK1 BR SUN OMELET OJ WK1 BR SUN OMELET OJ</p></li>
<li><p>WK1 BR MON PANCK GJ WK1 BR MON PANCK GJ WK1 BR MON PANCK GJ</p></li>
<li><p>WK1 BR TUE EGG AJ WK1 BR TUE EGG AJ WK1 BR TUE EGG AJ</p></li>
<li><p>WK1 BR WED EGG OJ WK1 BR WED EGG OJ WK1 BR WED EGG OJ</p></li>
<li><p>WK1 BR THU FR OJ WK1 BR THU FR OJ WK1 BR THU FR OJ</p></li>
<li><p>WK1 BR FRI PAN AJ WK1 BR FRI PAN AJ WK1 BR FRI PAN AJ</p></li>
<li><p>WK1 BR SAT EGG HARD WK1 BR SAT EGG HARD WK1 BR SAT EGG HARD</p></li>
<li><p>WK2 BR SUN WOMELT GJ WK2 BR SUN WOMELT GJ WK2 BR SUN WOMELT GJ</p></li>
<li><p>WK2 BR MON BIS AJ WK2 BR MON BIS AJ WK2 BR MON BIS AJ</p></li>
<li><p>WK2 BR TUE FR OJ WK2 BR TUE FR OJ WK2 BR TUE FR OJ</p></li>
<li><p>WK2 BR WED EGG AJ WK2 BR WED EGG AJ WK2 BR WED EGG AJ</p></li>
<li><p>WK2 BR THR PK OJ WK2 BR THR PK OJ WK2 BR THR PK OJ</p></li>
<li><p>WK2 BR FRI FR OJ WK2 BR FRI FR OJ WK2 BR FRI FR OJ</p></li>
<li><p>WK2 BR SAT EGG AJ WK2 BR SAT EGG AJ WK2 BR SAT EGG AJ</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### CQ Menu Cycle Query \[FHPRC3\]

> The Menu Cycle Query option is used for viewing only. It allows you to quickly identify which cycle, day, and meals were created for any given date, and can verify data is correctly entered. Once a date is entered, the following displays: Menu Cycle Name, Cycle Day, and Meal Names for Breakfast, Noon, and Evening.

#### CR Input Recipe Menu \[FHPRC14\]

> The Input Recipe Menu option allows you to create and edit a menu for the USER MENU file (#112.6) that is used for meal analysis. A Recipe Menu covers seven days. Within each day, there can be six meals entered with a list of recipes along with their portions for each meal.

> Note: To view a list of choices, after a prompt enter ?? and press \<RET\>.

> User Menu Name: Enter a name for a menu of up to 30 characters in length.

> Day \#: This is a required field. Enter a day number, 1-7, for the recipe menu.

> Meal \#: This is a required field. Enter a meal number, 1-6, for which food items are entered.

> Meal: The selections for this field come from the MEAL file (#116.1) that you populated using the Enter/Edit Meals option. This meal name is a collection of all recipes that are served at a given breakfast, noon, or evening meal.

> Production Diet: This is a required field. It uses data in the PRODUCTION DIET file (#116.2) and refers to desired Production Diet to be printed.

> Recipe: This field uses data in the RECIPE file (#114). All recipes for a meal should be in this field. If a recipe is not pre-established in the RECIPE file (#114), it is not found and must be entered under the Enter/Edit Recipes (RE) option before you enter in the meal.

> After a portion is entered, you are prompted for more recipes until all for this meal are defined. You are asked for the next meal number, and so on, until all meals for that Day \# are defined. You are asked for the next Day \# and so on. After you finish each level, press \<RET\> to move up to the next or to exit.

> Select Day \#: Press \<RET\> and the program lists all of the entries.

> OK to Save the Menu: Enter Yes to save the menu and No to edit the menu.

6.  CYI-WKI-MON-FRD EGG
7.  CYI-WKI-SUN-RST PORK
8.  CYI-WKI-SUN-SCR EGG/DANISH
9.  CYI-WKI-TUE-MEAT LOAF
10. CYI-WKI-TUE-PANCAKES TYPE '^' TO STOP, OR

> CHOOSE 1-10: 6

> Select Production Diet: ?

> Answer with PRODUCTION DIET NAME, or CODE

> Do you want the entire PRODUCTION DIET List? Y (Yes) Choose from:

> 87-130/CHOL REST

> 87-130/CHOL/DIAB

> 87-130/CHOL/HF

> 87-130/DIAB

> 87-130/HF

> 87-130/MECH-DYS

> 87-130/MOD BLAND CHOL/DIAB

> CHOLESTEROL RESTRICTED CLEAR LIQUID

> ...

> '^' TO STOP: ^

> You may enter a new PRODUCTION DIET

> NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH PUNCTUATION

> Select Production Diet: REGULAR

> Select Recipe: ??

> BEEF RICE SOUP

> BLAND CREAM OF PEA SOUP BRANFLAKES 40%, IND

> ...

> WHITE BREAD

> WHOLE WHEAT BREAD

> Select Recipe: WHOLE

1.  WHOLE GRAIN CORN, FROZEN
2.  WHOLE WHEAT BREAD
3.  WHOLE WHEAT MEAL CHOOSE 1-3: 2

> Serving Portion: 1// 2

> Select Recipe: WHITE BREAD

> Serving Portion: 1// 0

> Select Recipe: \<RET\>

> Select Meal \#: \<RET\>

> Select Day \#: \<RET\>

> Day 1

> Meal 1 RG CYI-WKI-MON-FRD EGG Meal 2 RG WK1 MON SP SW STK Meal 3 RG WK1 SU SP CUBAN SAND

> MEAL \# PROD DIET MEAL NAME

> Okay to Save the Menu? YES// \<RET\>

> ...Storing Recipes and Food Nutrient

> ...Done

#### DM Display Meal Analysis \[FHPRC13\]

> The Display Meal Analysis option allows you to produce a nutrient analysis for a selected meal from the MEAL file( \#116).1 using the nutrient analysis of the recipes.

> User Menu Name: Enter the name of the menu whose meals you want to analyze. User Menus are built using the Input Recipe Menu (CR) option. You can edit the menu at the “Do you wish to EDIT this menu?” prompt. Answer Yes or No.

> RDA Category: Meals are analyzed for a specific RDA category of patient. Enter a category or bypass the prompt.

> Patient: If you want the analysis for a specific patient, enter the patient's name. A patient name is not required.

> Detailed Analysis: You can select a detailed nutritional analysis or a summary analysis. Enter Yes or No.

> The analysis requires a 132- column printer.

#### DP Print Daily Diet Menus \[FHPRC11\]

> The Print Daily Diet Menus option allows you to print a report of the regular diet, recipes, portion size, and five modified diet menus for the day printed on one page. Additional modified diets are printed on successive pages. This menu requires a 132-column paper and a printer capable of producing 16 c.p.i. (compressed) print. If you try to use a printer that does not meet these criteria, an error message displays, the menu overlaps, or data is cut off.

> Data for Print Daily Diet Menus come from the following files:

- MENU CYCLE file (#116)
- PRODUCTION DIET file (#116.2)
- PRODUCTION FACILITY file (#119.71)
- RECIPE file (#114)
- RECIPE CATEGORY file (#114.1)

> Before running this report, make sure the files are complete. If they are not, use their corresponding options to enter and or edit the data:

- Enter/Edit Menu Cycle (CE)
- Enter/Edit Production Diets (PE)
- Enter/Edit Production Facilities (FE)
- Enter/Edit Recipes (RE)
- Enter/Edit Recipe Categories (CE)

> A production facility can print this report, if the site has more than one area of production. If you have more than one production facility, the first prompt in this option asks you to specify a production facility. If there is only one production area, the first prompt asks you to select a date to print.

> There are two formats for this menu. One format prints full recipe names in every production diet column. The second format prints full recipe names in the regular diet column and prints corresponding numbers wherever the regular recipes are acceptable on a modified diet. Where the regular recipes are not acceptable on a diet, the second format prints the full name of the diet recipe. Choose your format in the Enter/Edit Production Facilities (FE) option at the “FULL NAMES ON DAILY MENU?” prompt and store it in the PRODUCTION FACILITY file (#119.71).

> Recipe names or numbers print according to the Recipe Category print order designated in the RECIPE CATEGORY file (114.1). Within the recipe category, recipes display alphabetically.

> The content of the Daily Diet Menu is also a matter of choice. You can determine which production diets display across the top of the menu and the order in which they display. Use the Enter/Edit Production Diets (PE) option, enter “YES” or “NO” at the “PRINT ON DAILY MENU?” prompt, and enter a number at the “PRINT ORDER” prompt.

#### Example

> A facility has 18 Production Diets. Sixteen (including regular) of these production diets have a “YES” in the “PRINT ON DAILY MENU?” field in the PRODUCTION DIET (#116.2). Once

> all meals are entered and a day is selected to be printed, 3 pages of a Daily Diet Menu, with the 16 Production Diets selected to be printed, are generated.

> Production Facility: This field refers to the production facility that prepares the desired menu to be printed. This prompt displays only if there is more than one Production Facility entered in the PRODUCTION FACILITY file (#119.71) in the Nutrition Facilities (DF) program.

> Date: This is a required field and refers to the date for which the daily menu is to be printed. If there is only one production facility, this prompt displays first.

> This menu requires a 132-column compressed printer.

> Note: No example of this report is provided, because of its size.

#### HE Enter/Edit Holiday Meals \[FHPRC5\]

> The Enter/Edit Holiday Meals option allows you to create a holiday (or special) meal and temporarily substitute it into the everyday menu cycle without having to delete and reenter large amounts of data. The HOLIDAY MEALS file \#116.3 contains a list of meals for a holiday, special occasion or one time meal change.

> A holiday meal with its recipes must first be pre-established using the Enter/Edit Meals (ME) option. Once entered, the holiday meal is then given the date of the holiday. The program automatically inserts the holiday meal into the menu cycle on that date. After the holiday the everyday menu cycle automatically returns to normal. This option is also useful when meal changes are required due to shortages or excesses of ingredients, deletion of high cost meat/entrees, or equipment breakdowns.

> Holiday Meal Date: This entry refers to the date of the holiday or special event (meal change).

> Holiday Meal Name: This is a required field and the name is 1-30 characters, not starting with punctuation. For ease of identification, the Holiday Meal Name should be descriptive of when the holiday or special event meal is served.

#### Examples

- Halloween 03
- Veterans Day-04-E

> Meal: Breakfast Meal, Noon Meal, and Evening Meal fields are the choices for when the holiday meal is served. The meals must be from the MEAL file. If a Holiday Meal is not entered at any of the Meal prompts, no menu substitution occurs and the usual meal for the day is served.

> Note: Meal Fields (B, N, E,) are not required entries. If no meals are entered, the normal meals for the menu cycle display as usual. You must enter a meal name for a substitution to occur.

#### ME Enter/Edit Meals \[FHPRC4\]

> The Enter/Edit Meals option allows you to create a meal by giving it a specific identification (meal name) and by entering all recipes contained in that meal. The MEAL file \#116.1 contains separate listings of all recipes for each meal of a menu cycle. The meal is stored and retrieved by using the meal name. A meal is like a block of recipes that you review, change or move from one day to another at any time.

> Each recipe within a meal is assigned a string of production diet codes. Production diets and codes must be pre-established using the Enter/Edit Production Diets (PE) option before creating meals in the MEAL file. These production diet codes represent the diets that receive these recipes. This coding of recipes results in appropriate daily/weekly diet menus and production reports. Once a meal is entered, it is stored indefinitely, unless deliberately deleted from the file.

> Meal Name: The Meal Name may be 3-30 characters, not starting with punctuation. The name selected should reflect the meal to make future reference easier. You can use cycle, week, day, meal and first choice food item, e.g., CYI WK1 SU LU SWISS STK (Cycle I Week 1 Sunday Lunch Swiss Steak) to identify the meal.

> If the same meal is used more than once in a cycle(s), you cannot use specifics in the meal name.

#### Example

> The Swiss Steak meal is in Week 1 of Cycle 1, as well as Week 3 of Cycle 2, so the name of the meal is SWISS STEAK and is entered twice in the cycle without reference to the week or cycle.

> Recipe: Recipes in this multiple field must be from the RECIPE file. All recipes for a meal should be in this field. If a recipe is not in the RECIPE file, it is not found and must be entered using the Enter/Edit Recipes (RE) option before entering this recipe for the meal.

> All recipes entered in this field are listed on all meal production reports and menus. As all ingredients are listed on production reports, this may be desirable for issuing items from stock and for projected usage. However, it may be undesirable for printing daily and weekly menus because all recipes are listed and menus can become long and cumbersome. (If Tray Tickets are used, you must enter and code all recipes for each meal for accurate meal lists per patient.)

> Evaluate the facility's needs and practices to decide if you need to list all food items (recipes) served in a meal on all documents for that meal.

> Examples of why not to enter all recipes in a meal:

- Items delivered only once daily, e.g., bulk coffee or bulk milk to a cafeteria.
- Items issued to a trayline on a par stock basis, e.g., crackers, supplements.
- Items you need but are not on the menu, e.g., “plain” meat or other food preference items.
- Tray Tickets are not used.

> Frequently-used items like bread, beverages, and condiments can be combined in an “Add-On” meal to minimize data entry.

> Service Point: This field uses the service points from the SERVICE POINT file. It allows you to assign each recipe (one for each recipe) a popularity percentage specific to a service point. A service point may be either tray or cafeteria service, but not both. This concept is used to accommodate different patient preferences at different service points. The percentages are estimates and you may need to adjust them as populations vary. If no service points are designated, the Popularity % prompt does not display. The popularity percentages entered with the production diet codes are assumed for all service points.

> Popularity %: This field displays when you enter a specific Service Point. You enter an estimated percentage between 0 and 120% for a recipe at a specified service point. This is the estimated percentage of servings of the recipe needed for this service point. It is applied to all production diet codes in the string without designated percentages.

#### Example

> A hospital has 3 different service points: tray service, cafeteria service, and a nursing home with tray service. Approximately 30% of the hospital patients on selective menu tray service select chocolate cake for dessert, 60% of the patients in the cafeteria select chocolate cake, and 03% of the nursing home patients select chocolate cake.

> The popularity percentages for chocolate cake are:

- Hospital Tray Service 30%
- Hospital Cafeteria Service 60%
- Nursing Home Tray Service 03%

> This popularity percentage field can also be useful in non-select menu settings to provide different recipe items to the same production diets and different service points.

#### Example

> In this example, the Nursing Home Tray Service is getting gelatin salad. The other service points are getting tossed salad.

> Production Diets: The Production Diets field is a required entry. For every recipe entered when building a meal, you must assign an associated production diet code (or string of codes). This string of production diet codes is the key that lets the program know which production diets receive a particular recipe.

- The code string for each production diet code must be separated by a single space.
- The field is limited to 200 characters; production diet names with greater than 200 characters are not stored.
- To view all production diets, enter ALL+.
- To edit Production Diets when using ALL+, reenter the same recipe name at the next "Select RECIPE" prompt.
- Percentages are entered to a maximum of one decimal point.

#### Example

> On the menu for a lunch meal, Diet Swiss Steak is given to these production diets:

- Low Sodium (LS)
- Cardiac (CD)
- Calorie (CA)
- Calorie Sodium (CS)

> The string of production diet codes that are entered for the Diet Swiss Steak recipe are as follows: LS CD CA CS (each separated by a single space).

> Percentages for each production diet are entered for each meal service type (T or C). This allows facilities to have different percentages of a production diet for different meal service types. The format for entering these percentages is the production diet code followed by a semicolon followed by meal service type and the percent (a number from 0-999) with no spaces.

> Note: Each Service Point has only one meal service type. Thus, percentages entered with a “T” only apply to Tray Service Points and percentages entered with a “C” only apply to Cafeteria Service Points.

> Each production diet code and percent must be separated from any other production diet code by a space. Production diets listed without specified percentages are assumed 100% of the census for both meal service types.

#### Example

- Diet Swiss Steak LS CD CA;T50 CS;T50;C10
- Production Diets: LS (Low Sodium) and CD (Cardiac). All (100%) LS and CD production diets are served Diet Swiss Steak, no matter if the food is served from a Trayline or Cafeteria Service Point.
- Production Diet: CA (Calorie). Fifty percent of the CA production diets served from the trayline will receive the Diet Swiss Steak. All (100%) of the CA production diets served from the Cafeteria will receive the Diet Swiss Steak.
- Production Diet: CS (Calorie Sodium). Fifty percent of the CS production diets served from the Trayline and 10% of the CS production diets served from the Cafeteria will receive the Diet Swiss Steak.

> If a production diet code is entered with no percentages, the program reverts to the service point percentages. If there are no service point percentages, the program assumes 100% for that production diet. This is true for each production diet in the code string.

> Use Edit Meal Production Diets or this option to edit the code string, such as to delete the few codes that do not apply or to add T or C percentages as needed. To edit under this field use the VA FileMan convention of “Replace... With”. Use only a minus sign (-) for non-sequential editing under the MP Edit Meal Production Diets option.

> Note: When the majority of production diets apply for a recipe, enter “ALL+”.

> All production diets, single-spaced and without any T or C percentages, are added to the recipe.

> Recipe Category: This field uses recipe categories from the RECIPE CATEGORY file. Enter the different recipe categories that may characterize this recipe, such as, appetizer, soup, entree. Your first entry should be the category from the previous entry and the PRODUCTION DIET are added with it.

> Refer to the Enter/Edit Recipe Categories option in the Recipe Management (XR) program for further explanation. A recipe may be a potato in one meal and a salad recipe in another meal. Recipe categories play an important role in item substitution for food preferences on the Tray Ticket program. See Print Tray Ticket for further explanation.

> Add-On Meal: This field allows you to add on an entire pre-established list of recipes to this meal. It is a quick way to create new meals that may have only two or three recipes that differ from an already created meal. This allows changes to an existing meal without losing it from the file. Once renamed, the meal is edited for the few differing recipes. If a recipe is already entered for the meal, the screen displays the recipe name and indicates it already exists for the meal. The original entry remains intact; the Add-On entry does not change the first recipe.

> Select SERVICE POINT: \<RET\>

> PRODUCTION DIETS: ALL+

> CATEGORY: SOUP// \<RET\>

1.  SOUP
2.  SOUP II CHOOSE 1-2: 1

> Select RECIPE CATEGORY: SOUP

1.  SOUP
2.  SOUP II CHOOSE 1-2: 1

> PRODUCTION DIETS: HP RG DB ME FL CL PU HP D1 D2//

> Select RECIPE CATEGORY: APPETIZER

> PRODUCTION DIETS: CA

> Select RECIPE CATEGORY: \<RET\>

> Select RECIPE: BEEF RICE SOUP

> ...OK? Yes// N (No)

1.  BEEF BARLEY SOUP
2.  BEEF CUBES AU JUS
3.  BEEF NOODLE SOUP
4.  BEEF PATTIE, FROZEN, IND
5.  BEEF STROGANOFF TYPE '^' TO STOP, OR CHOOSE 1-5: 5

> Are you adding 'BEEF STROGANOFF' as a new RECIPE (the 2ND for this MEAL)? Y

> (Yes)

> Select SERVICE POINT: \<RET\> PRODUCTION DIETS: RG CL FL HP ME CATEGORY: ENTREE I// \<RET\>

1.  ENTREE I
2.  ENTREE II
3.  ENTREE III CHOOSE 1-3: 2

> Select RECIPE CATEGORY: ENTREE I

1.  ENTREE I
2.  ENTREE II
3.  ENTREE III CHOOSE 1-3: 2

> PRODUCTION DIETS: RG CL FL HP// Select RECIPE CATEGORY: \<RET\>

> Select RECIPE: PUR

1.  PUREE MONGOL SOUP
2.  PUREED APRICOTS
3.  PUREED ASPARAGUS
4.  PUREED BEEF
5.  PUREED BEETS TYPE '^' TO STOP, OR CHOOSE 1-5: 4

> Are you adding 'PUREED BEEF' as a new RECIPE (the 3RD for this MEAL)? Y

> (Yes)

> Select SERVICE POINT: HOSPITAL TL SERVICE POINT: HOSPITAL TL// \<RET\> POPULARITY %: 15// \<RET\>

> Select SERVICE POINT: \<RET\> PRODUCTION DIETS: PU CATEGORY: ENTREE I// \<RET\>

#### ML List Meal \[FHPRC6\]

> The List Meal option is an 80-column report that lists all recipes and their categories and associated production diet codes for any selected meal.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 7%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Select MEAL NAME: 94 MLK FE</p>
<p>Select Listing Device: HOME// &lt;RET&gt; HOME RIGHT MARGIN: 80// &lt;RET&gt;</p>
<p>Meal: 94 MLK FE</p>
<p>Recipe Cat. Production Diets</p>
<p>CHICKEN BROTH - 6 OZ SO1 CL</p>
<p>SPLIT PEA SOUP, CND SO1 ME;T50 STR CREAM OF GREEN PEA SOUP SO1 PU FL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>COLD LUNCH MEAT SANDWICH</p>
</blockquote></td>
<td>EE1</td>
<td><blockquote>
<p>SR;T10</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GRILLED CHEESE SANDWICH</p>
</blockquote></td>
<td>EE1</td>
<td><blockquote>
<p>SR;T10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LS MEATLOAF</p>
</blockquote></td>
<td>EE1</td>
<td><blockquote>
<p>DD DI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MEATLOAF</p>
</blockquote></td>
<td>EE1</td>
<td><blockquote>
<p>RG HP;T150 HF MS NF CH NC HD DB;T135 ND;T135 CD;T135 ED;T135 FD;T135 N3;T135 N2;T135 N4;T135 LP EC ME NM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PIZZA</p>
</blockquote></td>
<td>EE1</td>
<td><blockquote>
<p>SR;T10</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PUREED MEATLOAF</p>
</blockquote></td>
<td>EE1</td>
<td><blockquote>
<p>PU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SPEC MEATLOAF</p>
</blockquote></td>
<td>EE1</td>
<td><blockquote>
<p>AR MB GB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BROWN GRAVY</p>
</blockquote></td>
<td>SGG</td>
<td><blockquote>
<p>RG HP HF MS NF CH NC HD DB ND CD ED FD N3 N2 N4 LP AR EC ME NM MB GB PU SE DE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LS BROWN GRAVY</p>
</blockquote></td>
<td>SGG</td>
<td><blockquote>
<p>DD DI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BAKED POTATO</p>
</blockquote></td>
<td>PS1</td>
<td><blockquote>
<p>HF NF HD FD;T110</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DUCHESS POTATOES</p>
</blockquote></td>
<td>PS1</td>
<td><blockquote>
<p>RG HP MS DB;T110 ND;T110 ED;T110 N3 AR EC ME NM MB GB PU DP SR SE SD DE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LS DUCHESS POTATOES</p>
</blockquote></td>
<td>PS1</td>
<td><blockquote>
<p>DD DI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MACARONI, PLAIN</p>
</blockquote></td>
<td>PS1</td>
<td><blockquote>
<p>DD;T50 DI;T50</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MASHED POTATOES</p>
</blockquote></td>
<td>PS1</td>
<td><blockquote>
<p>CH NC CD N2 N4 LP</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MP Edit Meal Production Diets \[FHPRC9\]

> The Edit Meal Production Diets option allows you to alter production diet codes and popularity percentages in pre-established meals. Production diet codes are added or deleted and/or popularity percentages are modified for any recipe in a meal without having to retype the entire production diet code string. This option is useful when a facility decides to add or delete a production diet after the MEAL file is populated. Codes no longer have to be adjacent to each other to be deleted.

> Meal Name: Only meals created under Enter/Edit Meals (ME) of the MEAL file are entered in this field.

> Recipe: Only recipes entered for the selected meal through the Enter/Edit Meals (ME) option may be entered in this field.

> Action: You can take three actions on the production diet code string without re-typing the entire string. However, each action must be entered separately.

1.  Add – Enter a plus “+” sign in front of the production diet code.

#### Example

> +MS – Multiple production diet codes are added at one time provided a space is placed between codes: Example: +MS HF DB.

2.  Delete – Enter a minus “-” sign in front of the production diet code.

#### Example

> -RG – Multiple Production Diet Codes are deleted at one time. They must be separated by a space, but do not need to be in sequential order.

#### Example

> \- HF DB RG

3.  Modify Popularity Percentages – Enter the production diet code and the new percentage.

#### Example

> HP;C50 – Only one production diet can be modified at a time.

> Whenever any one of these actions is used, the program checks that the action can be taken and displays an OK. If you cannot perform an entered action, the program beeps and displays the reason.

#### Example

> Note: The program may not accept a long string of additions. Always check the display of the production diet code string that all additions are accepted.

#### WP Print Weekly Menu \[FHPRC7\]

> The Print Weekly Menu option allows you to print a Weekly Menu report for any specified production diet or all production diets. When ALL is selected, the production diets print according to the print order specified in the PRODUCTION DIET file (Enter/Edit Production Diets (PE) option). One production diet is printed per page; however, if a production diet such as the Regular Diet contains numerous recipe names, the menu continues on a second page. This report requires a 132-column paper and a printing device that is capable of producing (16 c.p.i.) compressed print.

> Recipe names print according to recipe category print order as specified in the RECIPE CATEGORY file \#114.1. Within recipe categories, the recipes print in alphabetical order.

> This report is useful for verifying the accuracy of the menus and for menu revisions. Because each production diet is printed separately, this weekly menu readily identifies frequency of items on modified diets. In facilities that display menus in long term care areas or in dining rooms, the weekly menu are posted to inform patients of the current meals. This report is not a usable document, unless an entire week of menus is entered into the MENU CYCLE file using the Enter/Edit Menu Cycle (CE) option.

> Production Diet: This field uses data from the PRODUCTION DIET file and refers to the Production Diet to print. You can select all production diets. Enter a production diet name, code, or ALL.

> Sunday Date: This is a required field. Sunday is the first day that prints on the weekly menus. Enter the date of the Sunday for the requested week. The entire menu for the week prints beginning with that date.

> Note: No example of this report is provided, because of its size.

#### WR Print Weekly Menu Blocks \[FHPRC12\]

> The Print Weekly Menu Blocks option allows you to print a cycle of weekly menus for any Recipe Category of any specified Production Diet or all Production Diets. It prints all recipe names in the order specified by the meal print order for the Recipe Category.

> It prints by recipe category and production diets in weekly sequence. This list is very useful in identifying the number of times a particular recipe is used in a menu cycle. Usually, a four-week cycle menu of one recipe category for one production diet prints on one sheet. You can print all production diets at one time. The list prints the cycle menu for the designated recipe category for each production diet in the print order established in the PRODUCTION DIET file. Recipes within each category print in alphabetical order.

> Production Diet: This is a required field.

> Sunday Date: This is a required field. Enter the date of the Sunday that begins the cycle.

> This report requires a 132-column paper and a printing device that is capable of producing compressed (16 c.p.i.) print.

> Note: No example of this report is provided, because of its size.

### XP Production Management \[FHPROM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DP</p>
</blockquote></th>
<th><blockquote>
<p>List Production Diet Percentages [FHPRF4]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Other Meals [FHPRF5]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OL</p>
</blockquote></td>
<td><blockquote>
<p>List Other Meals [FHPRF6]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Production Diets [FHPRO3]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>List Production Diets [FHPRO4]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PP</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Production Diet Percentages [FHPRF1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>List Production/Service/Communication Facilities [FHPRO10]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TM</p>
</blockquote></td>
<td><blockquote>
<p>Tray Tickets/Diet Cards Management… [FHMTKMM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WL</p>
</blockquote></td>
<td><blockquote>
<p>List Nutrition Locations [FHPRO6]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Production Management controls quantities produced in the Food Management program as defined by the Diet Order program. Diet orders, food preferences, and information contained in the INGREDIENT file, help generate a forecasting tool that allows the manager to anticipate, by percentage of total census, the type and quantity of various production diets, which will be needed by any selected service point. These percentages along with the specific additional meals required for outpatients, volunteers, students, and residents help to better define the production needs of the facility.

#### Managing Production

> Information in the DIET PATTERNS file that supports this section allows you to enter the standard meal patterns for all diets and combinations of diets used at a facility.

- Each pattern has an associated production diet and groupings of recipe categories defined by meal.
- Each pattern may also have associated standing orders specific to any or all meals and an associated supplemental feeding menu.
- All associated standing orders and the associated supplemental feeding menu automatically go into effect whenever a patient diet order matches the designated diet pattern.

> The diet card generated from these patterns lists all patient identification as shown on the diet order label, any patient allergies, all recipe categories defined for each meal and standing orders or food preferences associated with the diet pattern and this patient. The tray ticket generated displays the same patient identification and allergy data, but lists specific food items (recipes) to be served to the patient based on the meal, diet pattern, and food preferences. Substitutions for food dislikes are automatic if alternate choices for a category are entered for that meal. This section generates lists of all data entered into the production files.

> The Production Management Program consists of four file building options with list capabilities that you use as integral parts of the Food Management Program.

- Enter/Edit Production Diets - PRODUCTION DIET file \#116.2
- Enter/Edit Recipe Categories - RECIPE CATEGORY file \#114.1
- Enter/Edit Diet Patterns - DIET PATTERNS file \#111.1
- Enter/Edit Meals - MEAL file \#116.1

> Production diets are diets (as ordered) grouped by the way the food is produced and is served. You build two tables: Production Diet Percentages and Other Meals to enhance the reports generated by the Food Management Program.

> Production Diet Percentages: This is the percentage of the total census for each production diet for each delivery point each day.

> Other Meals: This is the average number of meals served to anyone other than inpatients by production diet, delivery point, and day of week.

> There is a relationship between the four major files of the Production Management program and other Nutrition and Food Service files.

> Note: The files pointed to, need to contain data before you edit the four files in Production Management.

#### Diagram of the Relationship

<table style="width:100%;">
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#)</p>
<p>POINTER FIELD</p>
</blockquote></th>
<th colspan="2"><p>POINTER</p>
<p>TYPE</p></th>
<th colspan="5"><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td colspan="5"></td>
<td></td>
</tr>
<tr class="even">
<td colspan="9"><blockquote>
<p>| 111.1 <strong>DIET PATTERNS</strong></p>
<p>| DIET1 |-&gt; <strong>DIETS</strong></p>
<p>| DIET2 |-&gt; <strong>DIETS</strong></p>
<p>| DIET3 |-&gt; <strong>DIETS</strong></p>
<p>| DIET4 |-&gt; <strong>DIETS</strong></p>
<p>| DIET5 |-&gt; <strong>DIETS</strong></p>
<p>| PRODUCTION DIET |-&gt; <strong>PRODUCTION DI*</strong></p>
<p>| ASSOCIATED SF * |-&gt; <strong>SUPPLEMENTAL</strong></p>
<p>| m ASSOCI:ASSOCI* |-&gt; <strong>STANDING ORDE*</strong></p>
<p>| m BREAKF:BREAKF* |-&gt; <strong>RECIPE CATEGO*</strong></p>
<p>| m NOON M:NOON M* |-&gt; <strong>RECIPE CATEGO*</strong></p>
<p>| m EVENIN:EVENIN* |-&gt; <strong>RECIPE CATEGO*</strong></p>
<p>| m ASSOCI:ASSOCI* |-&gt; <strong>STANDING ORDE*</strong></p>
<p>| m ASSOCI:ASSOCI* |-&gt; <strong>STANDING ORDE*</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p><strong>DIET PATTERNS</strong> (#111.115)</p>
</blockquote></td>
<td>|</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>BREAKFAST MODIFICATIONS (N C )-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>114.1</p>
</blockquote></td>
<td><blockquote>
<p><strong>RECIPE</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>CATEGORY</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>NOON MODIFICATIONS ... (N C )-&gt;</p>
</blockquote></td>
<td></td>
<td>|</td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>EVENING MODIFICATIONS (N C )-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p><strong>RECIPE</strong> (#114)</p>
</blockquote></td>
<td>|</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>DEFAULT CATEGORY ..... (N )-&gt;</p>
</blockquote></td>
<td></td>
<td>|</td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p><strong>MEAL</strong> (#116.11)</p>
</blockquote></td>
<td>|</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>RECIPE:CATEGORY ...... (N )-&gt;</p>
</blockquote></td>
<td></td>
<td>|</td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>USER MENU</strong> (#112.62)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td colspan="4">|</td>
</tr>
<tr class="odd">
<td>DAY N:MEAL NU:MEAL* ..</td>
<td><blockquote>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td></td>
<td>|</td>
<td colspan="4"><blockquote>
<p>116.1 <strong>MEAL</strong> |</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MENU CYCLE</strong> (#116.01)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td colspan="4">|</td>
</tr>
<tr class="odd">
<td>DAY:BREAKFAST MEAL ...</td>
<td><blockquote>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td></td>
<td>|</td>
<td colspan="4"><blockquote>
<p>m RECIPE:RECIPE |-&gt; <strong>RECIPE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

- Before creating production diets, review existing production tallies at the facility and determine which diets and/or combination diets are most important for food production purposes. By doing this, you can limit the number of production diets you need and thus lessen the time required to build the MEAL file.
- The “NPO” and “No Order” percentages on the Diet Census are automatically calculated by the program. If these categories were ignored, the production diet percentages would be falsely elevated and could result in excess food production. The “NPO” and “No Order” percentages may not match the “Not Eating” category on the Production Diet Percentages Table. This may result from rounding or padding percentages. Remember, the “Not Eating” category is figured by the computer as the difference of the production diet percentages (for that day and service point) total sum subtracted from 100%.
- When determining the figures to be entered in the Other Meals Table, you can refer to the data compiled for the Additional Meals (AR) report.

> If combination diets exist in the DIETS file and the census projections are inaccurate, it may be necessary to completely revise the DIETS file, eliminating the combinations.

#### Production Reports \[FHADM\]

> The Production Reports menu allows access to all lists and reports used for production by first line supervisors, diet office personnel, and the ingredient control person.

> Supplemental Feeding labels and consolidated listings are printed by Supplemental Feeding site or selected Nutrition location, including outpatient locations.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BW</p>
</blockquote></th>
<th><blockquote>
<p>Print Bulk Feedings/Cost Report [FHNO10]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DP</p>
</blockquote></td>
<td><blockquote>
<p>Print Daily Diet Menus [FHPRC11]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FM</p>
</blockquote></td>
<td><blockquote>
<p>Forecasting… [FHPRFM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LA</p>
</blockquote></td>
<td><blockquote>
<p>Run SF Labels/Consolid Ingredient List [FHNO2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MR</p>
</blockquote></td>
<td><blockquote>
<p>Meal Production Reports [FHPRO5]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PU</p>
</blockquote></td>
<td><blockquote>
<p>Projected Usage [FHPRR1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RP</p>
</blockquote></td>
<td><blockquote>
<p>Print Adjusted Recipe [FHREC2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>Print Standing Orders Labels [FHSP8]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SO</p>
</blockquote></td>
<td><blockquote>
<p>Tabulate Standing Orders [FHSP5]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SP</p>
</blockquote></td>
<td><blockquote>
<p>Consolidate Standing Orders [FHSP7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TP</p>
</blockquote></td>
<td><blockquote>
<p>Tabulate Patient Meal Preferences [FHSEL5]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TR</p>
</blockquote></td>
<td><blockquote>
<p>Print Tabulated Recipe List [FHMTKTR]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WL</p>
</blockquote></td>
<td><blockquote>
<p>Ward Supplemental Feeding Lists [FHN03]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td><blockquote>
<p>Print Weekly Menu [FHPRC7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WR</p>
</blockquote></td>
<td><blockquote>
<p>Print Weekly Menu Blocks [FHPRC12]</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Food Production \[FHPRO\]

> The Food Production menu provides access to all frequently used production options and reports. It is intended for Nutrition users who need to access all recipe and menu functions plus run routine reports and lists. Suggested users are Food Production and Service Chiefs, Supervisory Cook Foremen or other supervisory Nutrition users in need of this information.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PR</p>
</blockquote></th>
<th><blockquote>
<p>Production Reports [FHADM]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XM</p>
</blockquote></td>
<td><blockquote>
<p>Menu Cycle Management [FHPRCM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XR</p>
</blockquote></td>
<td><blockquote>
<p>Recipe Management [FHRECM]</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### DP List Production Diet Percentages \[FHPRF4\]

> The List Production Diet Percentages option is an 80-column report that produces a table for each delivery/service point and shows each production diet and its percentage by day of the week. It can also show a percentage for “Not Eating”. For each production diet, a percentage, 0- 110 is permitted. There is no minimum or maximum total for all production diets. If the total percentage is less than 100%, the difference is shown as “Not Eating”. If the total is greater than 100%, there is no percentage for “Not Eating”.

> Enter a Service Point or All and printer name. To print the report to the screen, accept the printer defaults.

#### OE Enter/Edit Other Meals \[FHPRF5\]

> The Enter/Edit Other Meals option allows you to create an information table (Other Meals) that is associated with the SERVICE POINT file. The enter/edit process is similar to that of file building. This Other Meals Table is created by each facility to account for meals served to people other than inpatients, e.g., gratuitous, volunteer, O.D., paid meals. This option allows you to assign an average number of meals to a service point by day, meal, and production diet type. These numbers are automatically added into the designated production diet total on the Forecasted Diet Census (FC) and/or Actual Diet Census (DC) of the Forecasting menu when the Meal Production Reports (MR) under Production Reports menu are generated.

> In this way, you account for the other meals in the production process and appropriate types and quantities of meal items are planned for each service point. Entering additional meals in this routine eliminates the need for the cooks to “pad” meals while producing the recipes.

> Note: The number of meals entered, reflect constant numbers, not percentages of Service Point census. Therefore, periodic audits of other meals served may indicate a need to adjust these numbers.

> Service Point Name: Enter one Service Point; each Service Point can have other meals designated.

> Add, Meals Production Diet: Enter one Production Diet. All Other Meals must be assigned to production diets. You must enter each production diet.

> ADD. \<day of the week\>\<meal\>: Enter a whole number between 0 and 1000. The same prompt sequence is used for each day of the week and each meal.

#### OL List Other Meals \[FHPRF6\]

> The List Other Meals option is an 80-column report that lists all the data entered under the Enter/Edit Other Meals (OE) option.

> Enter a printer name or \<RET\> to bring the report to the screen.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="10"><blockquote>
<p>Select LIST Printer: HOME// (Printer Name)</p>
<p>O T H E R M E A L S 9-Mar-05 2:42pm</p>
<p>DR200</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Diet</p>
</blockquote></td>
<td colspan="2">Meal</td>
<td><blockquote>
<p>Sun</p>
</blockquote></td>
<td>Mon</td>
<td>Tue</td>
<td>Wed</td>
<td>Thu</td>
<td colspan="2"><blockquote>
<p>Fri Sat</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REGULAR</p>
</blockquote></td>
<td></td>
<td>Brk</td>
<td><blockquote>
<p>35</p>
</blockquote></td>
<td>43</td>
<td>39</td>
<td>44</td>
<td>47</td>
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>25</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Noon</td>
<td><blockquote>
<p>33</p>
</blockquote></td>
<td>50</td>
<td>50</td>
<td>50</td>
<td>60</td>
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>35</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Even</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>31</td>
<td>36</td>
<td>35</td>
<td>35</td>
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DIABETIC/LO</p>
</blockquote></td>
<td><blockquote>
<p>CAL</p>
</blockquote></td>
<td>Brk</td>
<td></td>
<td>10</td>
<td>10</td>
<td>10</td>
<td>20</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Noon Even</p>
</blockquote></td>
<td></td>
<td>10</td>
<td>10</td>
<td>10</td>
<td>10</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### PE Enter/Edit Production Diets \[FHPRO3\]

> The Enter/Edit Production Diets option allows you to add and edit production diets. The PRODUCTION DIET file \#116.2 is created in Diet Order Entry as a requirement for the building of data in the DIETS file \#111. It provides a general estimate for food production based on the diets ordered through Diet Order Entry.

> You need to group diets ordered into specific production diets that best represent both the hot and the cold foods to produce. The Enter/Edit Production Diets option allows for combination production diets, i.e., Calorie Sodium, Cholesterol Sodium, Mechanical Diabetic Sodium. Diet census now tallies diets that have more than one diet modification directly from Diet Order Entry. This tally of production diets is used to link diet census to menus and recipes, so that food is produced and distributed in appropriate quantities. Combination production diets are referred to as “Combo” diets.

> Production Diet Name: The Production Diets Name field (3-30 characters in length) should represent the types of foods prepared at the facility. Although clinically there are numerous diet combinations, the actual number of production diets or types of food prepared is more limited.

> Production diets can represent from one to five diet modifications. When entering a “Combo” production diet, the singular production diets must already be in the file. A facility should consider establishing a “Combo” production diet when a diet with more than one modification receives different hot and cold foods than the singular diet modifications that make up the combination diet. A good guide for determining combination production diets is any tally sheet presently used for manual production counts.

#### Examples

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 23%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Diet Hot Food Served Cold Food Served</p>
<p>Sodium Roast Beef Cheese Cake</p>
<p>Calorie Ham Diet Peaches</p>
<p>*Calorie Sodium Roast Beef Diet Peaches Mechanical Ground Ham Cheese Cake</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Mechanical Sodium Ground</p>
</blockquote></td>
<td><blockquote>
<p>Roast Beef</p>
</blockquote></td>
<td><blockquote>
<p>Cheese Cake</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Mechanical Calorie Sodium</p>
</blockquote></td>
<td><blockquote>
<p>Ground Roast Beef</p>
</blockquote></td>
<td><blockquote>
<p>Diet Peaches</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*The “Calorie Sodium” combination diet does not receive the same hot and cold foods as the singular diet modifications “Calorie” and “Sodium”; therefore, a combination production diet of “Calorie Sodium” is established.

> \*\*These two combination diets also do not receive the same hot and cold foods as their respective singular diets; therefore, these two combination diets are established as production diets.

> If these combination production diets are not established prior to the run of production reports, inaccurate quantities of each of the foods to be served are listed resulting in over or under production.

> When trying to determine which production diets are to be established, review therapeutic/modified menus and census data. The number of production diets is not limited; however, each of these diets will require input for every recipe in the MEAL file. A large number of production diets increases the data entry time significantly. Also, if some diets occur infrequently in very small numbers or vary in only one or two easily adjustable food items (i.e., milk, bread, condiments), it may not be worth the trouble of establishing a separate production diet.

> Code: This is a unique two-character code, which must be either two upper case letters or a letter followed by a number. A code cannot be assigned to more than one Production Diet. Determine a logical naming method so that the code is recognizable, i.e., LS for Low Sodium, C4 for Calorie 4 gm Sodium. This code is used extensively in the Production summary.

> \# Days to Review: Enter the number of days after which a patient on this production diet should be reviewed.

> Cafeteria %: Each production diet may have a Cafeteria Percentage assigned to indicate the usual number of patients on that production diet who eat in the cafeteria. Use this percentage only in the forecasting process to determine, on any selected day, the number of portions of the production diet served in the cafeteria. Enter any percentage up to 100%. If the facility does not have cafeteria service or if you are not planning to forecast servings for the cafeteria, ignore this field.

> Print Order: The number assigned in this field to each production diet controls the order in which production diets are listed on the diet census, forecast census and daily diet menu, from low print orders to high.

> This option enables the facility to determine how the reports display. Only a singular print order is assigned. Therefore, production diets print in the same order on all reports. It is suggested, when assigning numbers, that some be skipped to allow for future additions or adjustments to the print order. Enter a number, 1-99, with no decimals.

> Print On Daily Menu?: A “Y” (yes) or “N” (no) response is required for each production diet. A positive response lists the Production Diet on the Daily Diet Menu printout.

> Note: Only six production diets include the regular print on each page; however, unlimited pages are allowed.

> Is This A Combo Diet?: A “Y” (yes) or “N” (no) response is required for each production diet. If the production diet has only one diet modification, i.e., “Sodium” or “Calorie”, an “N” is entered. If the production diet has more than one diet modification, i.e., “Calorie Sodium” or “Mechanical Sodium Calorie,” a “Y” is entered.

> Answering Yes to this prompt, means the diet is a combination of other production diets (e.g., both low sodium and calorie restricted). Because all production diets in a combo must match the default production diets of a clinical order, such combo production diets should have a tally order less than any individual production diets contained in the combo.

> Select Singular Production Diets: This field only displays if “Y” is entered in the Combo Diet field. This is an instance where a field points to/uses data in its own file. When this field displays, select a singular, not a combo, production diet. All production diets with more than one diet modification must consist of the singular production diets that make up the combination diet. These singular production diets are already established in the PRODUCTION DIET file.

> Therefore, all singular production diets are established before creating combination production diets. A production diet can have a maximum of five singular production diets.

#### Example

> Tally Order: The tally order represents a priority numbering system and establishes the sequence in which diets are tallied for the diet census. This was previously a function of Diet Precedence, but it is now specific to the PRODUCTION DIET file. Diet Precedence still functions as a numbering system that prevents the ordering of contradictory diets and determines the label print order.

> In Tally Order, each production diet is assigned a tally order number (1-99) that represents its order of importance. The lowest number has the greatest priority and is tallied first. Each Location ordered diet is tallied once for the production diet that has the lowest tally order number, regardless of the number of diet modifications.

#### Example

> A facility assigns the following tally orders to these production diets.

> The program tallies all Location ordered diets that have the combined “Mechanical Calorie Sodium” modifications before it tallies diets that have “Mechanical Sodium” modifications. Also the “Mechanical Sodium” combination is counted before a singular “Mechanical” diet.

> When assigning tally numbers to production diets, it is recommended that you assign lower tally numbers to production diets with the greatest number of diet modifications. This prevents production diets with similar diet modifications are not tallied incorrectly. For example: If the tally order for the above example was changed to “Mech Calorie Sodium” “l0” and “Mech Sodium” “5” all the Mech Calorie Sodium diets would be counted only as “Mech Sodium”. The Calorie modification would be ignored.

> Inactive: If you answer Yes at this prompt, the diet is removed from selection lists.

#### How the Program Searches and Tallies

> A diet is ordered through Diet Order Entry. Production diet codes are assigned for each modification, thereby creating a “string” of codes. That code string is stored with that diet order. When an Actual Diet Census (DC) is requested, the program starts with the production diet with the lowest tally order number. The program searches all diet orders for the order containing that string, finds it, and counts it. That particular order is not counted again. The process starts all over with the next lowest tally order number.

> The process is the same whether the production diet is a single or a combo. For the combo production diet, the program searches for the combination of codes that represents all the different modifications.

> The following is an example from a PRODUCTION DIET file that demonstrates the steps from diet order to diet census.

#### Example

> Diets are ordered. The program assigns production diet codes for each order.

> The program starts with the production diet with the lowest tally number. Five (5) is the lowest number in our example file.

> Note: The two-letter code for the combo diet is not used. The program uses the list of singular diet codes.

> 5 Mech Sodium Calorie = (ME SO CA)

> It searches for codes that are contained in the list of codes for the diet order. The 1800 ADA, 2g Na, Mech, Hi Pro diet order is counted as a Mech Sodium Calorie. It is not counted again.

> Note: The HP modification is ignored.

> The program moves to the next lowest tally number.

> 10 Mech Sodium (ME SO)

> 5It searches for codes contained in the order, and counts it. It bypasses the 1800 ADA, 2g Na Mech, Hi Pro because it was counted. It finds a match in the 2g Na, Mech and counts it as a Mech Sodium.

> It moves to the next tally number.

> 12 Mech Calorie (ME CA)

> There are no orders.

> It moves to the next tally number.

> 14 Calorie Sodium (CA SO)

> It finds 2g Na; 1500 ADA and counts it as a Calorie Sodium.

> The program presents the tally totals in the Actual Diet Census (DC) by production diet according to printing order (not shown in the example).

> The Actual Diet Census still includes a separate tally of minor modifications as determined by diet precedence.

> This separate minor modification tally has no effect on the above search and tally process. It is presented as additional useful information. See also Diet Precedence under Enter/Edit Diets, Diet Order Management.

#### When Combination Diets Pre-Exist in the DIETS File

> For facilities that entered combination diets into the DIETS file, corresponding production diets with two letter codes and appropriate tally orders are created. However, do not answer YES to the “Combo” prompt. The program treats these diets as if they are singular production diets and tallies them according to tally order. The search and tally procedure is less complex but the result should be the same: an accurate diet census that reflects modified diets.

> The diet order program is designed to allow location users to order diets in any manner. In the following example, two combination modified diets are put together to form a patient diet.

> This diet is tallied as a Mechanical Bland and the diabetic/sodium part is ignored. To avoid this, a "Combo" production diet called "Mechanical Bland Diabetic Sodium" is created, consisting of the two "single" diets 1500 CAL ADA 2g Na (code DS) and Mechanical Bland (Code MB). This "Combo" diet has a code MS, tally order 1, and a "code string" DS MB. The program uses the more complex search process as described previously, and tallies this as an MS production diet (Mechanical Bland Diabetic Sodium) because of its tally order (1).

#### Recode Production Diets

> For facilities that are using Diet Order Entry, there are two steps to take every time changes are made to the PRODUCTION DIET file. These steps are:

1.  Review the Production Diets field of the DIETS file.
2.  Recode diets for all inpatients.

> New production diets added to the file may make the information in the Production Diet field of the DIETS file obsolete. The Actual Diet Census (DC) is incorrect. The information in this field is reviewed and updated any time changes are made to the PRODUCTION DIET file.

> Because the production diet for a diet order is designated at the time the diet is ordered and counted when the census is requested, changes to the data in the PRODUCTION DIET file are not reflected in Actual Diet Census (DC), unless all the production diets for inpatients are recoded. Do this by using option Recode Diets for all Inpatients (RD) found under System Management (SM).

#### Example

#### PL List Production Diets \[FHPRO4\]

> The List Production Diets option is a 132-column report that prints the data in the PRODUCTION DIET file entered under Enter/Edit Production Diets (PE).

<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 21%" />
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DEVICE: (Printer Name) PRODUCTION DIETS</p>
<p>9,2005 14:46 PAGE 1 TALLY</p>
<p>ORDER CODE DIET TALLIED PROD. DIETS</p>
</blockquote></th>
<th><blockquote>
<p>INACT</p>
</blockquote></th>
<th><blockquote>
<p>REV</p>
</blockquote></th>
<th><blockquote>
<p>PRINT ORDER</p>
</blockquote></th>
<th><blockquote>
<p>DAILY MENU</p>
</blockquote></th>
<th><blockquote>
<p>MAR</p>
<p>COMBO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="6"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>1 CL CLEAR LIQUID</p>
</blockquote></td>
<td colspan="2">3</td>
<td>76</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>3 FL FULL LIQUID</p>
</blockquote></td>
<td colspan="2"></td>
<td>74</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>5 PU PUREED</p>
</blockquote></td>
<td colspan="2"></td>
<td>72</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>6 AR ASPIRATION RISK REDUCTION</p>
</blockquote></td>
<td colspan="2">5</td>
<td>59</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>7 SD SELECT-DIABETIC</p>
</blockquote></td>
<td colspan="2"></td>
<td>86</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>9 N4 87/CHOL/DIAB/MECH</p>
</blockquote></td>
<td colspan="2"></td>
<td>50</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>MODERATE SODIUM (87 -130)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CHOLESTEROL RESTRICTED</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>DIABETIC/LO CAL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MECHANICAL/DYSPHAGIA</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>10 N6 87/CHOL/DIAB/HF</p>
</blockquote></td>
<td colspan="2"></td>
<td>52</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MODERATE SODIUM (87 -130)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>DIABETIC/LO CAL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CHOLESTEROL RESTRICTED</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HIGH FIBER</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>11 SE SELECT-ECC</p>
</blockquote></td>
<td colspan="2"></td>
<td>84</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>12 CM 87/CHOL/MECH</p>
</blockquote></td>
<td colspan="2"></td>
<td>26</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MODERATE SODIUM (87 -130)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CHOLESTEROL RESTRICTED</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MECHANICAL/DYSPHASIA</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>13 N1 87/CHOL/HF</p>
</blockquote></td>
<td colspan="2"></td>
<td>28</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MODERATE SODIUM (87 -130)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CHOLESTEROL RESTRICTED</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>HIGH FIBER</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>15 N2 87/CHOL/DIAB</p>
</blockquote></td>
<td colspan="2"></td>
<td>48</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MODERATE SODIUM (87 -130)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CHOLESTEROL RESTRICTED</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>DIABETIC/LO CAL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>17 N3 87/DIAB/MECH</p>
</blockquote></td>
<td colspan="2"></td>
<td>44</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MODERATE SODIUM (87 -130)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>DIABETIC/LO CAL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MECHANICAL/DYSPHAGIA</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### PP Enter/Edit Production Diet Percentages \[FHPRF1\]

> Production Diet Percentage Table

> The Production Diet Percentage fields contain a percentage of the total census for each production diet for each day and delivery/service point. Production diet percentages are an integral part of the Forecasting (FM) menu of Production Reports (PR). These percentages are applied to the Medical Administration Service (MAS) census figures for each service point and are used to project the number of servings needed for each menu item.

> Before completing these fields, all production diets are established and the inpatient database is recoded.

> You need to conduct a data collection period of two to three weeks to gather the diet percentages. The following procedure is used to collect data.

1.  Print Actual Diet Census (DC) daily for two or three weeks for all service points.
2.  The percent column on the Actual Diet Census indicates the percentage of the total census at a specific service point for that production diet for that day. Using the two or three weeks of data, average the percent of each production diet, each day of the week for each service point.
3.  The resulting number can be used as the average percentage of that production diet for that day and service point. Enter this number under this option, Enter/Edit Production Diet Percentages (PP).

#### Example

> Service Point: Hospital - Actual Diet Census

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Production</p>
</blockquote></th>
<th><blockquote>
<p>Diet</p>
</blockquote></th>
<th><blockquote>
<p>Percent</p>
</blockquote></th>
<th><blockquote>
<p>Day</p>
</blockquote></th>
<th><blockquote>
<p>Week</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Regular</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2l.3</p>
</blockquote></td>
<td><blockquote>
<p>Thursday</p>
</blockquote></td>
<td><blockquote>
<p>Week l</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Regular Regular</p>
</blockquote></td>
<td></td>
<td><p>20.8</p>
<p><u>2l.6</u></p>
<p>Avg.21.2</p></td>
<td><blockquote>
<p>Thursday Thursday</p>
</blockquote></td>
<td><blockquote>
<p>Week 2</p>
<p>Week 3</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The average percentage for the Regular production diet for Thursday in the hospital service point is 21.2%.

> Although the Actual Diet Census always indicates the percent of each diet for each service point, this information is not automatically transferred to the field. Each facility may want to review these percentages on a quarterly basis and update as needed.

> Service Point Name: Service points are pre-established under the Enter/Edit Service Points (SE) option. Each service point must have separately established production diet percentages.

> Production Diet: Production diets are pre-established under the Enter/Edit Production Diets (PE) option. Each production diet are listed separately for each delivery point.

> Select the production diet for which you are entering daily forecast percentages.

> Census Percentage: The number entered into this field represents the percentage of the total census representing this production diet for this delivery point. Enter greater than 100% (to 110%) if a facility increases (pad) the census of a production diet at a specific delivery point. This is one mechanism for accommodating double portions. Each day is entered separately. Enter a number between 0-110 for each day of the week. This is the forecasted percentage of total census for each day.

> Note: It is recommended that the percentage for each day be derived from an average of three or more of those days.

> Select FORECAST % PRODUCTION DIET: This prompt redisplays after the Saturday Census Percentage prompt. It allows you to enter additional production diets for the same service point.

#### SL List Production/Service/Communication Facilities \[FHPRO10\]

> The List Production/Service/Communication Facilities option is allow you to produce a series of reports for each of the Production Facilities, Service Points, Communication Offices, and Supplemental Feeding Sites. The reports show all parameters associated with each facility.

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select LIST Printer: HOME// (Printer Name)</p>
<p>9-Mar-05 P R O D U C T I O N F A C I L I T Y</p>
<p>MAIN KITCHEN</p>
</blockquote></th>
<th></th>
<th></th>
<th>Page 1</th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Full Names on Daily Menu: YES</p>
<p>Print Meal Distribution: YES Separate Production Summary Pages: YES Separate Recipe Preparation Pages: YES Separate Storeroom Pages: YES</p>
<p>Associated Tray Lines: B217 TL</p>
<p>Associated Cafeterias: DR200</p>
<p>Associated Supplemental Fdg. Sites:</p>
<p>NUPPER</p>
<p>SUPPLEMENTAL FEEDINGS</p>
<p>9-Mar-05 S E R V I C E P O I N T B217 TL</p>
</blockquote></th>
<th></th>
<th></th>
<th>Page 2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Type of Service: Tray Line</p>
<p>Short Name: B217 Production Facility: MAIN KITCHEN</p>
<p>Associated Nutrition Locations:</p>
<p>221 ECC 2-B</p>
<p>ECC 1-B ECC 2-C</p>
<p>ECC 1-C</p>
<p>Production Diet %: Sun Mon Tue Wed REGULAR 3.5 3.5 3.5 3.5</p>
<p>MECHANICAL/DYSPHAG 8.0 8.0 8.0 8.0</p>
<p>PUREED 10.5 10.5 10.5 10.5</p>
<p>FULL LIQUID 1.0 1.0 1.0 1.0</p>
<p>CLEAR LIQUID 0.5 0.5 0.5 0.5</p>
<p>GROUND MODIFIED BL 3.0 3.0 3.0 3.0</p>
<p>MODIFIED BLAND 0.5 0.5 0.5 0.5</p>
<p>HIGH FIBER 0.5 0.5 0.5 0.5</p>
<p>DIALYSIS/LOW NA (4 1.0 1.0 1.0 1.0</p>
<p>MODERATE SODIUM (8 2.5 2.5 2.5 2.5</p>
<p>HPHC 1.0 1.0 1.0 1.0</p>
<p>DIABETIC/LO CAL 5.0 5.0 5.0 5.0</p>
</blockquote></td>
<td><p>Thu 3.5</p>
<p>8.0</p>
<p>10.5</p>
<blockquote>
<p>1.0</p>
<p>0.5</p>
<p>3.0</p>
<p>0.5</p>
<p>0.5</p>
<p>1.0</p>
<p>2.5</p>
<p>1.0</p>
<p>5.0</p>
</blockquote></td>
<td><blockquote>
<p>Fri 3.5</p>
<p>8.0</p>
<p>10.5</p>
<p>1.0</p>
<p>0.5</p>
<p>3.0</p>
<p>0.5</p>
<p>0.5</p>
<p>1.0</p>
<p>2.5</p>
<p>1.0</p>
<p>5.0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Sat 3.5</p>
<p>8.0</p>
<p>10.5</p>
<p>1.0</p>
<p>0.5</p>
<p>3.0</p>
<p>0.5</p>
<p>0.5</p>
<p>1.0</p>
<p>2.5</p>
<p>1.0</p>
<p>5.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GERIATRIC/ECC 15.0 15.0 15.0</p>
</blockquote></th>
<th>15.0</th>
<th>15.0</th>
<th><blockquote>
<p>15.0</p>
</blockquote></th>
<th><blockquote>
<p>15.0</p>
</blockquote></th>
<th rowspan="50"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>LOW PROTEIN 1.0 1.0 1.0</p>
</blockquote></th>
<th>1.0</th>
<th>1.0</th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>87/CHOL/DIAB 1.0 1.0 1.0</p>
</blockquote></th>
<th>1.0</th>
<th>1.0</th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>87/MECH-DYS 1.0 1.0 1.0</p>
</blockquote></th>
<th>1.0</th>
<th>1.0</th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>87/CHOL 1.0 1.0 1.0</p>
</blockquote></th>
<th>1.0</th>
<th>1.0</th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>87/DIAB 2.5 2.5 2.5</p>
</blockquote></th>
<th>2.5</th>
<th>2.5</th>
<th><blockquote>
<p>2.5</p>
</blockquote></th>
<th><blockquote>
<p>2.5</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>DIAL/DIAB 0.5 0.5 0.5</p>
</blockquote></th>
<th>0.5</th>
<th>0.5</th>
<th><blockquote>
<p>0.5</p>
</blockquote></th>
<th><blockquote>
<p>0.5</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>STANDING ORDER 10.0 10.0 10.0</p>
</blockquote></th>
<th>10.0</th>
<th>10.0</th>
<th><blockquote>
<p>10.0</p>
</blockquote></th>
<th><blockquote>
<p>10.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>87/CHOL/DIAB/MECH 0.4 0.4 0.4</p>
</blockquote></th>
<th>0.4</th>
<th>0.4</th>
<th><blockquote>
<p>0.4</p>
</blockquote></th>
<th><blockquote>
<p>0.4</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>DIAB/MECH 1.5 1.5 1.5</p>
</blockquote></th>
<th>1.5</th>
<th>1.5</th>
<th><blockquote>
<p>1.5</p>
</blockquote></th>
<th><blockquote>
<p>1.5</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>DIAB/HF 0.5 0.5 0.5</p>
</blockquote></th>
<th>0.5</th>
<th>0.5</th>
<th><blockquote>
<p>0.5</p>
</blockquote></th>
<th><blockquote>
<p>0.5</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ASPIRATION RISK RE 0.5 0.5 0.5</p>
</blockquote></th>
<th>0.5</th>
<th>0.5</th>
<th><blockquote>
<p>0.5</p>
</blockquote></th>
<th><blockquote>
<p>0.5</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SELECT-ECC 15.0 15.0 15.0</p>
</blockquote></th>
<th>15.0</th>
<th>15.0</th>
<th><blockquote>
<p>15.0</p>
</blockquote></th>
<th><blockquote>
<p>15.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SELECT-REGULAR 10.0 10.0 10.0</p>
</blockquote></th>
<th>10.0</th>
<th>10.0</th>
<th><blockquote>
<p>10.0</p>
</blockquote></th>
<th><blockquote>
<p>10.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SELECT-DIABETIC 8.0 8.0 8.0</p>
</blockquote></th>
<th>8.0</th>
<th>8.0</th>
<th><blockquote>
<p>8.0</p>
</blockquote></th>
<th><blockquote>
<p>8.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ECC-DIABETIC 4.5 4.5 4.5</p>
</blockquote></th>
<th>4.5</th>
<th>4.5</th>
<th><blockquote>
<p>4.5</p>
</blockquote></th>
<th><blockquote>
<p>4.5</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Not Eating</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Total Sum 109.4 109.4 109.4</p>
</blockquote></th>
<th>109.4</th>
<th>109.4</th>
<th><blockquote>
<p>109.4</p>
</blockquote></th>
<th><blockquote>
<p>109.4</p>
</blockquote></th>
</tr>
<tr class="header">
<th>9-Mar-05 S E R V I C E P O I</th>
<th><blockquote>
<p>N T</p>
</blockquote></th>
<th></th>
<th></th>
<th>Page 3</th>
</tr>
<tr class="odd">
<th>DR200</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Type of Service: Cafeteria</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Short Name: DR200</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Production Facility: MAIN KITCHEN</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Associated Nutrition Locations:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th>4E 8E</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th>4W BRS</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Production Diet %: Sun Mon Tue</p>
</blockquote></th>
<th>Wed</th>
<th>Thu</th>
<th><blockquote>
<p>Fri</p>
</blockquote></th>
<th><blockquote>
<p>Sat</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>REGULAR 45.0 45.0 45.0</p>
</blockquote></th>
<th>45.0</th>
<th>45.0</th>
<th><blockquote>
<p>45.0</p>
</blockquote></th>
<th><blockquote>
<p>45.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>MECHANICAL/DYSPHAG 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>GROUND MODIFIED BL 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>MODIFIED BLAND 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HIGH FIBER 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>MODERATE SODIUM (8 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HPHC 1.0 1.0 1.0</p>
</blockquote></th>
<th>1.0</th>
<th>1.0</th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
<th><blockquote>
<p>1.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>DIABETIC/LO CAL 15.0 15.0 15.0</p>
</blockquote></th>
<th>15.0</th>
<th>15.0</th>
<th><blockquote>
<p>15.0</p>
</blockquote></th>
<th><blockquote>
<p>15.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CHOLESTEROL RESTRI 6.0 6.0 6.0</p>
</blockquote></th>
<th>6.0</th>
<th>6.0</th>
<th><blockquote>
<p>6.0</p>
</blockquote></th>
<th><blockquote>
<p>6.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>LOW PROTEIN 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>87/CHOL 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>87/HF 3.0 3.0 3.0</p>
</blockquote></th>
<th>3.0</th>
<th>3.0</th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>87/DIAB 10.0 10.0 10.0</p>
</blockquote></th>
<th>10.0</th>
<th>10.0</th>
<th><blockquote>
<p>10.0</p>
</blockquote></th>
<th><blockquote>
<p>10.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CHOL/DIAB 12.0 12.0 12.0</p>
</blockquote></th>
<th>12.0</th>
<th>12.0</th>
<th><blockquote>
<p>12.0</p>
</blockquote></th>
<th><blockquote>
<p>12.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Not Eating</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Total Sum 113.0 113.0 113.0</p>
</blockquote></th>
<th>113.0</th>
<th>113.0</th>
<th><blockquote>
<p>113.0</p>
</blockquote></th>
<th><blockquote>
<p>113.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Additional Meals: Meal Sun Mon</p>
</blockquote></th>
<th><blockquote>
<p>Tue</p>
</blockquote></th>
<th>Wed Thu</th>
<th>Fri Sat</th>
<th></th>
</tr>
<tr class="header">
<th>REGULAR Brk 35 43</th>
<th><blockquote>
<p>39</p>
</blockquote></th>
<th>44 47</th>
<th>32 25</th>
<th></th>
</tr>
<tr class="odd">
<th>Noon 33 50</th>
<th><blockquote>
<p>50</p>
</blockquote></th>
<th>50 60</th>
<th>50 35</th>
<th></th>
</tr>
<tr class="header">
<th>Even 20 31</th>
<th><blockquote>
<p>36</p>
</blockquote></th>
<th>35 35</th>
<th>31 22</th>
<th></th>
</tr>
<tr class="odd">
<th>DIABETIC/LO CAL Brk 10</th>
<th><blockquote>
<p>10</p>
</blockquote></th>
<th>10 20</th>
<th><blockquote>
<p>10</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th>Noon 10</th>
<th><blockquote>
<p>10</p>
</blockquote></th>
<th>10 10</th>
<th><blockquote>
<p>10</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Even</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 77%" />
<col style="width: 14%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>9-Mar-05 C O M M U N I C A T I O N O F F I C E</p>
</blockquote></th>
<th>Page 4</th>
<th rowspan="14"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>COMMUNICATION OFFICE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Provide Bagged Meals: NO</p>
</blockquote>
<p>Breakfast Noon</p>
<blockquote>
<p>Meal Time: 8:00A 12:00P</p>
<p>Early Time 1:</p>
<p>Early Time 2:</p>
<p>Early Time 3:</p>
<p>Late Time 1:</p>
<p>Late Time 2:</p>
<p>Late Time 3:</p>
<p>Late Alarm Begin:</p>
<p>Late Alarm End:</p>
<p>Associated Nutrition Locations:</p>
<p>9-Mar-05 C O M M U N I C A T I O N O F F I C E</p>
<p>C1-TCC</p>
</blockquote></th>
<th><blockquote>
<p>Evening 6:00P</p>
<p>Page 5</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Provide Bagged Meals: NO</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th>Breakfast Noon</th>
<th><blockquote>
<p>Evening</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>Meal Time: 6:20A 11:20A</th>
<th><blockquote>
<p>4:20P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Early Time 1: 6:20A 11:20A</p>
<p>Early Time 2:</p>
<p>Early Time 3:</p>
</blockquote></th>
<th><blockquote>
<p>4:20P</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Late Time 1: 7:30A 12:30P</p>
<p>Late Time 2: 8:15A 1:15P</p>
<p>Late Time 3: 10:00A 2:30P</p>
</blockquote></th>
<th><blockquote>
<p>5:30P</p>
<p>6:15P</p>
<p>7:00P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Late Alarm Begin: 6:20A 11:20A</p>
<p>Late Alarm End: 9:58A 2:28P</p>
</blockquote></th>
<th><blockquote>
<p>4:20P</p>
<p>6:58P</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Associated Nutrition Locations:</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>12E 5W</p>
<p>12W 6E</p>
<p>2A 6W</p>
<p>2B 7E</p>
<p>2D 7W</p>
<p>3E 8E</p>
<p>3W 9EI</p>
<p>4E 9E</p>
<p>4W BRS</p>
<p>5E</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th>9-Mar-05 S U P P L E M E N T A L F E E D I N G S I T E</th>
<th>Page 6</th>
</tr>
<tr class="header">
<th><blockquote>
<p>SUPPLEMENTAL FEEDINGS</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Short Name: S FDGS</p>
<p>Separate Labels: YES Items on Location Lists: YES</p>
<p>Production Facility: MAIN KITCHEN Associated Nutrition Locations:</p>
<p>9-Mar-05 S U P P L E M E N T A L F E E D I N G</p>
<p>NUPPER</p>
</blockquote></th>
<th><blockquote>
<p>S I T E</p>
</blockquote></th>
<th><blockquote>
<p>Page 7</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Short Name: NUP</p>
<p>Separate Labels: NO Items on Location Lists: YES</p>
<p>Production Facility: MAIN KITCHEN</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Associated Nutrition Locations:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>10ET 12W</p>
<p>10E 13EI</p>
<p>10WC 13E</p>
<p>10W 13W</p>
<p>11E 15E</p>
<p>11W 15WR</p>
<p>12E 15W</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### TM Tray Tickets/Diet Cards Management \[FHMTKMM\]

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CE</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Recipe Categories [FHREC4]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CL</p>
</blockquote></td>
<td><blockquote>
<p>List Recipe Categories [FHREC5]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DP</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Diet Patterns [FHMTKS]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LP</p>
</blockquote></td>
<td><blockquote>
<p>List Diet Patterns [FHMTKT]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Meals [FHPRC4]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td><blockquote>
<p>List Meal [FHPRC6]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PD</p>
</blockquote></td>
<td><blockquote>
<p>Print Diet Cards [FHDCRP]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>Print Tray Tickets [FHMTKP]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Tray Tickets/Diet Card Management option allows you to print a list of individual food items to place on the tray (tray tickets) and a list of recipe categories to serve for a given diet (diet cards). You can run them concurrently if the site does not have complicated diet modifications; otherwise, use one or the other. Tray Tickets and Diet Cards are diet pattern driven.

- A diet pattern consists of recipe categories and automatic nourishment, associated standing orders, and an associated supplemental feeding menu.
- Diet restrictions are specified along with the diet pattern.
- The diet restrictions are stored as dislikes in the FOOD PREFERENCES file.

> The Diet Cards/Tray Tickets display for outpatients. There are major differences between tray tickets and diet cards:

#### Tray Tickets:

1.  Replace the bread and beverage on the MEAL file with the patient’s bread and beverage
2.  Incorporate the dislike food preferences by listing an alternate recipe in the MEAL file
3.  Print the recipe along with the category item that is omitted for recipes with diabetic exchanges
4.  Print all the standing orders for that meal

#### Diet Cards:

1.  Print if there is no menu or meal established
2.  Print two or three cards per page
3.  Two prints:

> Diet patterns consisting of recipe categories for all three meals Standing orders for all three meals

> All dislike food preferences for all three meals

4.  Three (format like tray tickets) prints:

> Bread and beverage replaced by patient’s bread and beverage

> Standing orders for a meal

> Dislike food preferences meal-specific. If site has no menu or meal established, all dislikes print.

> Print tray tickets and diet cards on regular letter style paper 8-1/2x11. Print them on a laser printer in landscape mode. The parameter settings for Kyocera and Hewlett Packard LaserJet III are in the installation guide. You can print them on other printers, but you need to set up the landscape setting or have IRM do it.

> A diet pattern has no more than 15 recipe categories per meal. Although both diet card and tray ticket can print at least 17 items per page, they print to a second page if a patient has more items.

> Nutrition personnel need to understand that the use of tray tickets and diet cards places additional printing burdens on the service. Both require a detailed implementation process relating to food preferences, standing orders, recipe categories, and meals, etc.

> Note: Recipe categories are essential in processing the tray tickets. Do not duplicate them or delete them. Be consistent with the recipe category that you are using. This also applies to the bread and beverage default.

> The associated recipe’s category should match the pattern’s category. MEAL, RECIPE, and DIET PATTERNS files point to the RECIPE CATEGORY file.

> Create a pattern for every combination you have. You are prompted to import recipe categories from another pattern under the Enter/Edit Diet Patterns (DP) option. If you use an existing pattern in the file, import it to the pattern you are creating. Modify the needs of the diet as necessary.

> Note: When you do an import, the recipe categories, standing orders, supplemental feeding menu, and diet restrictions are all imported. Therefore, check everything and edit accordingly.

#### Steps to Follow

1.  Review the manual system pattern.
2.  Determine the pattern format and terminology. (Keep the recipe categories consistent with the recipe categories of the recipes in the meal. No need to put alternates in the diabetic exchanges.)
3.  Create single patterns (use Diet List to help) using the Enter/Edit Diet Patterns (DP) option.
4.  Determine associated standing orders, supplemental feeding, and diet restrictions.
5.  Review your entries.
6.  Establish known combo diets and create a pattern for each diet combination.
7.  Review and modify.
8.  Print a test run for a small, stable Location for one meal.
9.  Review and modify.

#### Diet Card Implementation

> Diet Cards are diet pattern driven with automatic nourishment just like tray tickets. But Diet Cards can be run for a site that does not have a menu or meal set up. Implementation is not as complex as that for tray tickets.

> CE Enter/Edit Recipe Categories \[FHREC4\]

> The Enter/Edit Recipe Categories option allows you to add or edit recipe categories in the RECIPE CATEGORY file \#114.1.

> For more information, refer to the Enter/Edit Recipe Categories option under Recipe Management.

> CL List Recipe Categories \[FHREC5\]

> The List Recipe Categories option allows you to list all of the recipe categories in the RECIPE CATEGORY file \#114.1 and their associated data elements.

> In the Device field, enter a printer name.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DEVICE: (Printer Name)</p>
<p>RECIPE CATEGORIES</p>
<p>NAME CODE</p>
</blockquote></th>
<th><blockquote>
<p>PRINT ORDER</p>
</blockquote></th>
<th><blockquote>
<p>MAR 16,2005 INACTIVE?</p>
</blockquote></th>
<th><blockquote>
<p>11:21</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JUICE I JUICE II JUICE III APPETIZER BEEF FRUIT I FRUIT II FRUIT III PORK</p>
<p>SOUP CEREAL CEREAL II</p>
<p>CEREAL III</p>
</blockquote></td>
<td><blockquote>
<p>J1 J2 J3 A1 BF1 FR1 FR2 FR3 PK1 SP1 C1 C2</p>
<p>C3</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>2</p>
<p>2</p>
<p>2</p>
<p>3</p>
<p>3</p>
<p>3</p>
<p>3</p>
<p>3</p>
<p>3</p>
<p>6</p>
<p>9</p>
<p>9</p>
<p>9</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_DP_Enter/Edit_Diet_Patterns_[FHMTKS]" class="anchor"></span>DP Enter/Edit Diet Patterns \[FHMTKS\]

> The Enter/Edit Diet Patterns option allows you to develop diet patterns for each of the diets in the file. These patterns consist of Recipe Categories with quantities you use during the printing of both diet cards and tray tickets.

> The selection of breakfast, noon, and evening associated standing orders is available. Prompts exist for diet restrictions for all meals and inactive diets, as well as for updating all diet related information for patients.

#### Diet Pattern for Single Diet

> Diets Name: This is a pointer to the DIETS file (#116.2).[<sup>1</sup>](#diet-patterns-for-combination-diets)

> Import Recipe Categories from another Diet Pattern: You can import any existing diet pattern into the current pattern and edit it for your needs.

> Production Diet: This is a pointer to the PRODUCTION DIET file (#116.2). The existing production diet displays as the default. You can change only this pattern to any other production diet.

> Breakfast Modifications: This is a multiple field. Enter all recipe Categories and the quantity to serve at each meal. Enter the quantity as whole or decimal numbers.

> Standing Orders: The identified standing orders are automatically added to the patient record and printed on the diet card or tray ticket.

> SF Menu: This field points to the SUPPLEMENTAL FEEDING MENU file (#118.1). The SF menu entered, is automatically implemented for the patient when the diet is ordered.

> Diet Restrictions: This field is a pointer to the FOOD PREFERENCES (#115.2) file. Enter any dislike food preferences to use as a Diet Restriction for the Diet Pattern. The MEALS prompt entry determines to which meals (B, N, E, or ALL) this Diet Restriction applies.

> Inactive: To update the patient information, answer YES. Corrections are applied to any diet patterns you edited/added, provided the y do not contain individual diet patterns.

> <sup>1</sup> Patch FH\*5.5\*5 May 2007 Updated the descriptions columns of this option.

#### Diet Patterns for Combination Diets

> Diet patterns for combination diets are created by selecting a combo diet name or by entering multiple diets at the sequential prompts "Select DIETS NAME:".

> LP List Diet Patterns \[FHMTKT\]

> The List Diet Patterns option allows you to list one selected Diet Pattern or all the Diet Patterns entered through Enter/Edit Diet Patterns. It is a useful tool for reviewing the work.

<table>
<colgroup>
<col style="width: 83%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Print ALL Diet Patterns? Y// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select LIST Printer: HOME// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>16-Mar-05 1:42pm D I E T P A T T E R N L I S T</p>
</blockquote></th>
<th><blockquote>
<p>Page 1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>BREAKFAST NOON EVENING</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Production Diet: CLEAR LIQUID Diet Order: CLEAR LIQ</p>
<p>Associated Supp. Fdgs. Menu: CLEAR LIQUID</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><ol type="1">
<li><p>CONDIMENT II 1 CONDIMENT II 1 CONDIMENT II</p></li>
<li><p>JUICE 1 JUICE 1 JUICE</p></li>
</ol>
<blockquote>
<p>1 SOUP 1 SOUP 1 SOUP</p>
<p>1 BEVERAGE 1 BEVERAGE 1 BEVERAGE</p>
<p>1 CITROTEIN 1 CITROTEIN 1 CITROTEIN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Note: The standing order for citrotein is included as part of the Diet Pattern. If you use any standing order designators, such as C or H, they also display.

> ME Enter/Edit Meals \[FHPRC4\]

> The Enter/Edit Meals option allows you to create or edit meals, including the associated recipes and production diets. For more information, refer to Menu Cycle Management.

> ML List Meal \[FHPRC6\]

> The List Meal option allows you to select a meal from the MEAL file (#116.1) and to print its associated recipes and production diets.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Select MEAL NAME: <strong>BREAKFAST</strong></p>
<p>Select Listing Device: HOME// <strong>&lt;RET&gt;</strong> TERMINAL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>Meal: BREAKFAST</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Recipe</p>
</blockquote></td>
<td></td>
<td>Cat.</td>
<td>Production Diets</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORANGE JUICE, HOSPITAL T</p>
</blockquote></td>
<td><blockquote>
<p>6OZ IND</p>
<p>Tray 100%</p>
</blockquote></td>
<td>A1</td>
<td><blockquote>
<p>CC RG CH CL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BACON</p>
<p>HOSPITAL T</p>
</blockquote></td>
<td><blockquote>
<p>Tray 05%</p>
</blockquote></td>
<td>BI1</td>
<td><blockquote>
<p>FL CL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EGG, FRESH HOSPITAL T</p>
</blockquote></td>
<td><blockquote>
<p>Tray 98%</p>
</blockquote></td>
<td>EG1</td>
<td><blockquote>
<p>RG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DECAF</p>
</blockquote></td>
<td></td>
<td>BV1</td>
<td><blockquote>
<p>CC RG CH</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PD Print Diet Cards \[FHDCRP\]

> The Print Diet Cards option allows you to print Diet Cards that consist of patients' diet patterns. The Diet Cards can be printed two patients per page or three per page for a selected patient, Location, Communication Office, or for all. The Diet Card requires a 132-column printer.

> <span id="_PT_Print_Tray_Tickets_[FHMTKP]" class="anchor"></span>PT Print Tray Tickets \[FHMTKP\]

> The Print Tray Tickets option allows you to print tray tickets for each meal, three patients per page, for a selected patient, Location, Communication Office, or for all three meals.

> When a food allergy is entered for a patient, it is automatically added to Food Preferences (Dislike), and Tray Tickets Management removes the relevant items from the ticket.[<sup>1</sup>](#wl-list-nutrition-locations-fhpro6)

#### Example of a tray ticket with ALLGS

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 1%" />
<col style="width: 22%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>Print by PATIENT, COMMUNICATION OFFICE, LOCATION or ALL? COMM// <strong>Patient</strong></p>
<p>Select PATIENT (Name or SSN): PATIENT1,FH</p>
<p>Sort Patients: (A=Alphabetically R=Room-Bed) R// <strong>a</strong></p>
<p>Select Date: TODAY// (JUN 25, 2007) Select MEAL (B,N,E,or ALL): <strong>ALL</strong></p>
<p>Consolidated List? Y// <strong>&lt;RET&gt;</strong></p>
<p>Select LIST Printer: HOME// (Printer name) <strong>&lt;RET&gt;</strong></p>
<p>25-Jun-07 11:40am 25-Jun-07 11:40am 25-Jun-07 11:40am</p>
<p>Breakfast 25-Jun-07 Noon 25-Jun-07 Evening 25-Jun-07 REGULAR REGULAR REGULAR</p>
<p>ALLGS.: NONE ON FILE ALLGS.: NONE ON FILE ALLGS.: NONE ON FILE</p>
<p>1 ORANGE JUICE 1 LASAGNA 1 BREADED PORK CHOP</p>
<p>1 BISCUIT 1 CAPRI VEGETABLES 1 BLACKEYED PEAS</p>
<p>1 SCRAMBLED EGG 1 CHEFS SALAD+ITALIAN DRESSING 1 SEAS MIXED GREENS+VIN PKG</p>
<p>1 GRILLED HAM 1 DINNER ROLL 1 RELISH PLATE #1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1 DRY CEREAL,ASSORTED</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>MARGARINE</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>CORNBREAD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 MARGARINE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CHEESECAKE</p>
</blockquote></td>
<td></td>
<td>2</td>
<td><blockquote>
<p>MARGARINE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 HONEY,IND</p>
<p>1 COFFEE</p>
</blockquote>
<ol type="1">
<li><p>2% MILK</p></li>
<li><p>C-CEREAL,DRY</p></li>
</ol>
<blockquote>
<p>1 C-MILK,2%</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>COFFEE</p>
<p>1 ICED TEA</p>
<p>1 ICED TEA</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>CHERRY PIE</p>
<p>1 COFFEE</p>
<p>1 2% MILK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENT1,FH(0000) P P3T 3T106-1P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>PATIENT1,FH(0000) P3T 3T106-1P</p>
</blockquote></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>PATIENT1,FH(0000) P P3T 3T106-1P</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example of a tray ticket tabulated recipe list

> <sup>1</sup> Patch FH\*5.5\*8 September 2007 Modified the PT option to remove allergy-type food preferences from the tray tickets.

#### WL List Nutrition Locations \[FHPRO6\]

> The List Nutrition Locations is an 80-column report that lists all Nutrition Locations in sequential print order by Delivery/Service Point. In addition, it shows any bulk nourishments ordered under Supplemental Feeding Management, the dietitians or technicians assigned, the default admission diet, pertinent clinical review information, and pertinent facility geography.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 40%" />
<col style="width: 10%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select LOCATION (or ALL): <strong>2A</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th rowspan="33"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select LIST Printer: HOME// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th><blockquote>
<p>HOME RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>9-Mar-05 D I E T E T I C</p>
</blockquote></th>
<th><blockquote>
<p>W A R D P R O F I L E</p>
</blockquote></th>
<th><blockquote>
<p>Page 1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p>2A</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Print Order: 3</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Assigned Clinician: MARIBELL,KATHERINE</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Tray Assembly: T200 (100%)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Cafeteria:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Dining Room:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Supplemental Fdgs.: NLOWER</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Diet Communication: C1-TCC</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Admission Diet:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Review Frequencies:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>NPO's: 3 days Admit Status: 3 days</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Tubefeedings: 7 days Supp. Fdgs.: 14 days</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Status I: 30 days Status III: 7 days</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Status II: 30 days Status IV: 7 days</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Bulk Nourishment Orders:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>1 JUICE,CRANBERRY,46CN 1 JUICE,ORANGE</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>1 JUICE,ORANGE,46CN</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Room-Beds Assigned:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>220A-1 224A-2 230A-3 235A-2</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>220A-2 224A-3 230A-4 235A-3</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>220A-3 224A-4 232A-1 235A-4</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>220A-4 229A-1 232A-2 237A-1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>222A-1 229A-2 232A-3 237A-2</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>222A-2 229A-3 232A-4 237A-3</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>222A-3 229A-4 233A-1 237A-4</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>222A-4 230A-1 234A-1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>224A-1 230A-2 235A-1</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Default MAS Locations:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>2A</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Print Cafeteria on Tray Tickets: NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### XR Recipe Management \[FHRECM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CE</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Recipe Categories [FHREC4]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CL</p>
</blockquote></td>
<td><blockquote>
<p>List Recipe Categories [FHREC5]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Equipment [FHREC8]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EL</p>
</blockquote></td>
<td><blockquote>
<p>List Equipment [FHREC9]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Analyze All Recipes [FHREC11]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ND</p>
</blockquote></td>
<td><blockquote>
<p>Display Recipe Analysis [FHREC12]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NL</p>
</blockquote></td>
<td><blockquote>
<p>Display Analyzed Recipes List [FHREC13]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Preparation Areas [FHING9]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PL</p>
</blockquote></td>
<td><blockquote>
<p>List Preparation Areas [FHING10]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RC</p>
</blockquote></td>
<td><blockquote>
<p>Re-cost Recipes [FHREC10]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Recipes [FHREC1]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>List Recipes [FHREC3]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RP</p>
</blockquote></td>
<td><blockquote>
<p>Print Adjusted Recipe [FHREC2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RU</p>
</blockquote></td>
<td><blockquote>
<p>List Recipe Usage in Meals/Cycles [FHPRC10]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Serving Utensils [FHREC6]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>List Serving Utensils [FHREC7]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Recipe Management allows you to create site-specific recipes. Recipe data include portion size, preparation area and time, equipment and serving utensils required, recipe category, ingredients and directions for preparation. Recipes are embedded in other recipes for easy preparation. Lists containing all recipe information are generated, as well as a per portion recipe cost. Nutrients for each ingredient are edited in each recipe to more accurately reflect the food item produced. All recipes are analyzed for nutrients once this information is established.

#### Managing Recipes

> The Recipe Management Program allows you to build recipes from groups of ingredients. The recipes are used to create meals. Every food item on a menu is considered a recipe and must have a corresponding recipe entered into the program. This includes all single ingredient recipes such as milk, sugar packages, bread, frozen convenience foods, etc. A master RECIPE file containing approximately 500 commonly used VA Standardized Recipes is provided. Review this file carefully and revise accordingly.

> The Recipe Management Program also consists of four other data files: RECIPE CATEGORY, EQUIPMENT, PREPARATION AREA and SERVING UTENSIL. Each recipe entered is assigned a recipe category, a preparation area, types of equipment for preparation and a utensil for serving.

> Note: The files point to (used by) the files of the Recipe Management Program.

#### Diagram of the Relationship

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#)</p>
<p>POINTER FIELD</p>
</blockquote></th>
<th><p>POINTER</p>
<p>TYPE</p></th>
<th><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p><strong>USER MENU</strong> (#112.64) | | DAY N:MEAL NU:RECIPE* (N )-&gt; | 114 <strong>RECIPE</strong> | <strong>RECIPE</strong> (#114.03) | |</p>
<p>EMBEDDED RECIPE ...... (N )-&gt; | SERVING UTENSIL |-&gt; <strong>SERVING UTEN* FOOD PREFERENCES</strong> (#115.2) | |</p>
<p>RECIPE ............... (N )-&gt; | DEFAULT CATEGO* |-&gt; <strong>RECIPE CATEG*</strong></p>
<p>EXCLUDED RECIPES ..... (N )-&gt; | PREPARATION AR* |-&gt; <strong>PREPARATION * MEAL</strong> (#116.11) | |</p>
<p>RECIPE ............... (N )-&gt; | ASSOCIATED NUT* |-&gt; <strong>FOOD NUTRIEN* SUPPLEMENTAL FEEDING</strong> (#118) | |</p>
<p>CORRESPONDING RECIPE . (N )-&gt; | m INGRED:INGRED* |-&gt; <strong>INGREDIENT TUBEFEEDING</strong> (#118.2) | |</p>
<p>CORRESPONDING RECIPE . (N )-&gt; | INGRED:ASSOCI* |-&gt; <strong>FOOD NUTRIEN*</strong></p>
<p>| m DIABET:DIABET* |-&gt; RECIPE CATEGORY</p>
<p>| m EMBEDD:EMBEDD* |-&gt; <strong>RECIPE</strong></p>
<p>| m EQUIPM:EQUIPM* |-&gt; <strong>EQUIPMENT</strong></p>
<p><strong>DIET PATTERNS</strong> (#111.115) | | BREAKFAST MODIFICATIONS (N C )-&gt; | 114.1 <strong>RECIPE CATEGORY</strong> NOON MODIFICATIONS ... (N C )-&gt; | |</p>
</blockquote>
<p>EVENING MODIFICATIONS (N C )-&gt; | |</p>
<p><strong>RECIPE</strong> (#114) | |</p>
<blockquote>
<p>DEFAULT CATEGORY ..... (N )-&gt; | |</p>
<p><strong>MEAL</strong> (#116.11) | |</p>
<p>RECIPE:CATEGORY ...... (N )-&gt; | |</p>
<p><strong>RECIPE</strong> (#114) | | PREPARATION AREA ..... (N )-&gt; | 114.2 <strong>PREPARATION AREA</strong></p>
<p><strong>RECIPE</strong> (#114) | | SERVING UTENSIL ...... (N )-&gt; | 114.3 <strong>SERVING UTENSIL</strong></p>
<p><strong>RECIPE</strong> (#114.05) | | EQUIPMENT ............ (N L)-&gt; | 114.4 <strong>EQUIPMENT</strong> |</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note: A master file for each Recipe Management files (shown in the boxes), except the PREPARATION AREA file, is provided with enter and edit capability. Each facility must create a PREPARATION AREA file. It is recommended all Recipe Management files be reviewed and developed before proceeding to other routines.

> After the installation, list the recipe categories, review the diet-card system patterns in the User Manual, and determine if you need to add any more recipe categories. Consider all the alternates you might need for each category. Use the Enter/Edit Recipe Categories (CE) option to populate the file and fill in the category code. The code consists of one to two characters and a number. If you have recipes with exchanges, create a separate category for them.

#### Example

> An entree, Chili Con Carne, has one bread, margarine, and vegetable exchanges. If you do not have these three categories, you need to add them to the RECIPE CATEGORY file. The total entries should look as follows:

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 3%" />
<col style="width: 14%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th></th>
<th colspan="2"><blockquote>
<p>Code</p>
</blockquote></th>
<th><blockquote>
<p>Print Order</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENTREE</p>
</blockquote></td>
<td><blockquote>
<p>I</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>E1</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENTREE</p>
</blockquote></td>
<td><blockquote>
<p>II(an</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>alternate) E2</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BREAD</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>BR1</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>MARGARINE</p>
</blockquote></td>
<td><blockquote>
<p>MG1</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>VEGETABLE</p>
</blockquote></td>
<td><blockquote>
<p>VG1</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>ENTREE I DB-X</p>
</blockquote></td>
<td><blockquote>
<p>E1X</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>ENTREE II DB-X</p>
</blockquote></td>
<td><blockquote>
<p>E2X</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Keep the codes consistent. If you use V1 for VEGETABLE I, use V2 for VEGETABLE II. The print order should be the same for both. It is essential to keep the codes consistent. You create the last two categories (Entrée I DB-X and Entrée II DB-X) to use in the MEAL file to specify which production diets print with the exchanges.

> Next, modify the recipes. A new multiple in the RECIPE file, called the Diabetic Exchange, points to the RECIPE CATEGORY file. Use the Enter/Edit Recipes (RE) option and add to it the categories created (bread, margarine, and vegetable) in the recipe category file and the quantities. The names assigned to the exchanges in the RECIPE CATEGORY file print on the tray ticket.

> You can view the Diabetic Exchanges entered through the Print Adjusted Recipes (RP) option.

#### Steps to Follow

1.  Review the manual diet-card system pattern.
2.  Review the diabetic exchange list.
3.  Use the option List Recipe Categories (CL).
4.  Populate the RECIPE CATEGORY file and use the Enter/Edit Recipe Categories (CE) option to establish the code and print order. Take into account exchanges and alternates you will need.
5.  The Diabetic Exchange field in the RECIPE file is associated with the RECIPE CATEGORY file. Use the Enter/Edit Recipes (RE) option to populate the diabetic exchanges that you want to display on the tray ticket.
    - Enter all recipes into the RECIPE file prior to building the MEAL file. This prevents switching back and forth between files.
    - Enter fields in the RECIPE file that are not currently in use, when first building the file. This prevents backtracking when the field becomes functional.
    - The Ingredient field of the RECIPE file is not required; a recipe may contain only embedded recipes.

#### Example

> Ground meatloaf is created by using the meatloaf recipe as an embedded recipe with no other ingredients. The directions explain how to grind the meatloaf.

- Recipes should have Ingredients or embedded recipes; it is not recommended that you leave both of these fields empty. An empty recipe prints on the menu, but there are no food items on any Meal production reports.

> When deciding how to answer the Print Recipe field under Enter/Edit Recipes (RE), consider answering NO to those recipes that always need readjustment once printed, because of food preferences or standing orders.

> When assigning a recipe to a Recipe Category under Enter/Edit Recipes (RE), consider creating a variety of Recipe Categories just for condiments, such as Entree Condiment, Salad Condiment, Bread Condiment, Breakfast Condiment, etc. This insures that all condiments are listed with associated recipes or food items on the daily/weekly menus.

#### Examples

- Ketchup assigned to Entree Condiment Category so that Ketchup is listed with Hamburger.
- Maple Syrup assigned to Breakfast Condiment Category so that Syrup is listed with Pancakes.
- Jelly assigned to Bread Condiment Category so that Jelly is listed with Toast.

> You can use VA FileMan to customize recipe reports, such as, print a list of recipes sorted by recipe category.

> There is an unusual prompt sequence for both the Ingredient and Embedded Recipe fields of the RECIPE file. It is important to understand how this prompt sequence functions in order to avoid unexpected errors in recipes. Once entries are made in these fields, any attempt to edit the entries, interrupts a prompt that shows the last entry made and requests confirmation.

> Select Ingredient: When editing a recipe, after the ingredient/embedded recipe prompts, you see a default ingredient. Enter NO to view a list of ingredients with similar names. If there are several, pick one and proceed.

> Ingredient: You can overwrite or delete this entry using VA FileMan conventions.

> Select INGREDIENT:(Ingredient name)//

> Caution: If there is only one ingredient of that type in the file, VA FileMan assumes it is the item and automatically adds it to the list of ingredients in the recipe.

> Note: When entering ingredients in a recipe, the program does not allow duplicate entries of the same ingredient.

#### Examples

> In both examples, a different amount of water is needed for different functions within the same recipe. The INGREDIENT file contains only one listing, Water, and the program only allows for one entry of each ingredient.

> The need for duplicating an ingredient entry is accomplished by creating multiple listings in the INGREDIENT file of the same ingredient with slightly different names. Ex. Water - 1, Water - 2, Water - Cold, Water - Boiling

> Using this technique, multiple listings of similar ingredients are made in the recipe.

#### CE Enter/Edit Recipe Categories \[FHREC4\]

> The Enter/Edit Recipe Categories option allows you to enter and edit data in the RECIPE CATEGORY file \#114.1. The file categorizes recipes, e.g., appetizer, soup, beverage, entree, starch, etc. Each recipe category is given a code. A master file is provided with the package, which you can print it using the List Recipe Categories (CL) option. You can enter additional recipe categories.

> The Recipe Category field in the RECIPE file uses the data in the RECIPE CATEGORY file and is a mandatory entry. A Recipe Category prompt also displays under the Enter/Edit Meals (ME) option. This recipe category prompt determines the way recipes print on diet cards and tray tickets. The recipe category allows for substitute food items to display on tray tickets. For example, if Entree 1 is Roast Pork and the patient has a No Pork food preference, the program automatically substitutes next appropriate entree. Information on production reports can be sorted by recipe categories making it easier for production personnel to follow.

> Recipe Category Name: The entry in this field should be 3-15 characters in length. It is the category to which the recipe is assigned.

> Code: This is a required field, and must be 1- 2 characters and a number or 1-2 characters, a number and an “X”. Code with an “X” means the recipe with this category has diabetic exchanges. This code is the abbreviated version of the recipe category, displays on reports, and is used on tray assembly tickets.

> Meal Print Order: This is a required field. This field establishes the print sequence in which recipes display on the weekly and daily menus. Enter a number between 1 and 99, which is the relative print order, from low to high, of recipes in this category.

#### Example

> If the meal print order for the recipe category “Entree” is 4, and the meal print order for the recipe category “Starch” is 6, all recipes with a category of Entree print before Starches on the weekly and daily menus.

> Inactive: This entry indicates whether the recipe category is inactive. A “YES” at this prompt inactivates the recipe, removing it from selection lists. Entering a Yes removes this recipe category from selection lists.

#### CL List Recipe Categories \[FHREC5\]

> The List Recipe Categories option allows you to print a list of all recipe category names, codes, and meal print orders created using Enter/Edit Recipe Categories (CE).

<table style="width:100%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DEVICE: <strong>&lt;RET&gt;</strong> HYPER SPACE</p>
<p>RECIPE CATEGORIES</p>
<p>NAME CODE</p>
</blockquote></th>
<th><blockquote>
<p>RIGHT</p>
<p>PRINT ORDER</p>
</blockquote></th>
<th><blockquote>
<p>MARGIN:</p>
</blockquote></th>
<th><blockquote>
<p>80//</p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
<p>MAR 8,2005</p>
</blockquote></th>
<th><blockquote>
<p>12:19</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BEVERAGE BREAD JUICE I JUICE II JUICE III APPETIZER FRUIT I FRUIT II FRUIT III SOUP</p>
<p>SOUP II CEREAL CEREAL II CEREAL III NEW ONE</p>
<p>BREAKFAST ITEM BRK ITEM III BRK. ENTREE BRK. ENTREE II BRKFAST ITEM II ENTREE</p>
<p>ENTREE I ENTREE II ENTREE III SAUCE/GRAVY STARCH STARCH II STARCH III VEGETABLE VEGETABLE I VEGETABLE II</p>
<p>VEGETABLE III SALAD</p>
<p>SALAD II</p>
</blockquote></td>
<td><blockquote>
<p>BV1 BR1 J1 J2 J3 A1 FR1 FR2 FR3 SP1 SP2 C1 C2 C3 NO1 BI1 BI3 BE1 BE2 BI2 E1 E1 E2 E3 SG1 ST1 ST2 ST3 V1 V1 V2 VG3</p>
<p>SA1 SA2</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>1</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>2</p>
<p>3</p>
<p>3</p>
<p>3</p>
<p>3</p>
<p>6</p>
<p>6</p>
<p>9</p>
</blockquote>
<p>9</p>
<p>9</p>
<p>9</p>
<p>12</p>
<p>12</p>
<p>12</p>
<p>12</p>
<p>12</p>
<p>15</p>
<p>15</p>
<p>15</p>
<p>15</p>
<p>18</p>
<blockquote>
<p>21</p>
<p>21</p>
<p>21</p>
<p>24</p>
<p>24</p>
<p>24</p>
<p>24</p>
<p>27</p>
<p>27</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### EE Enter/Edit Equipment \[FHREC8\]

> The Enter/Edit Equipment option allows you to enter and edit data in the EQUIPMENT file \#114.4. It contains the names of large equipment used in food preparation, e.g., steam kettle, convection oven, mixer. A master EQUIPMENT file \#114.4 9 is provided by the software and is printed using the List Equipment (EL) option. You can add additional types of equipment as needed.

> The Equipment field of the RECIPE file \#114 uses the data in this file. It is not a required field but if completed, the equipment display on the printed recipe. New equipment is entered into the EQUIPMENT file using the Enter/Edit Recipes (RE) option.

> Note: Always check to see if the piece of equipment is already in the file.

#### EL List Equipment \[FHREC9\]

> The List Equipment option allows you to print a list of all equipment in the EQUIPMENT file \#114.4.

#### NA Analyze All Recipes \[FHREC11\]

> The Analyze All Recipes option allows you to analyze all existing recipes. If the recipe has no associated nutrients, it is not analyzed. If a recipe has multiple ingredients, but not all ingredients have associated nutrients, the recipe is analyzed, but is not accurate.

> The analysis takes place by selecting the option. For more information, refer to Recipe Analysis under Energy/Nutrient Management.

#### ND Display Recipe Analysis \[FHREC12\]

> The Display Recipe Analysis option displays the nutrient analysis of one recipe. The analysis uses the associated nutrient for each ingredient in the recipe. This option is used to check if ingredients in a recipe have associated nutrients and amounts in LBS.

> Recipe Name: This recipe is a previously analyzed recipe from the RECIPE file \#114.

> RDA Category: This is an optional entry that displays the %RDAs of the recipe, if an RDA category is selected. It points to the preset RDA Category table.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 2%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="13"><blockquote>
<p>Select RECIPE NAME: <strong>CHILI MAC</strong></p>
<p>Select RDA Category: <strong>M25 MALES 25-50 YR.</strong></p>
<p>Print on Device: HOME// <strong>&lt;RET&gt;</strong> HOME RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
<p>--- Recipe Ingredient List --- CHILI MAC</p>
<p>Number of Portions: 100</p>
<p>Ingredient Amt In Lbs Associated Nutrient</p>
<p>BEEF, GROUND, FRZN 7.100 BEEF, GROUND, LEAN, BROILED, WELL CAYENNE PEPPER, GROUND, 1# CN 0.010 PEPPER, RED OR CAYENNE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>CHILI POWDER, GROUND, 1# CN</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.125</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>CHILI POWDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>GARLIC POWDER, GROUND, 1# CN</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.015</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>GARLIC POWDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>ONIONS, DICED, FRESH</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>6.480</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>ONIONS, YEL, CKD WO/SALT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>SALT, BULK</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.188</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>SALT, TABLE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>SOUP AND GRAVY BASE, BEEF</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>0.266</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>SOUP, BEEF BROTH, CUBED, DRY</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>TOMATO PASTE</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>4.313</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>TOMATO PASTE, CND, WO/SALT ADDED,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>TOMATO PUREE</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>6.750</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>TOMATO PUREE, CND, REG PK</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>TOMATOES, CND, DICED</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>6.750</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>TOMATOES, CND, REG PK, ALL STYLES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>WATER, TAP</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>6.000</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>WATER</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Embedded Recipe: MACARONI, PLAIN</p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="6"></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Ingredient</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Amt In LBS</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>Associated Nutrient</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>MACARONI, ELBOW WATER, TAP</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FORM</p>
</blockquote></td>
<td colspan="3"><p>16.625</p>
<p>*</p></td>
<td colspan="2"><blockquote>
<p>MACARONI, ENR, WATER</p>
</blockquote></td>
<td><blockquote>
<p>FIRM</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STAGE,</p>
</blockquote></td>
<td>8-10 M</td>
</tr>
<tr class="odd">
<td colspan="13"><blockquote>
<p>--- Analysis of Recipe Portion --- CHILI MAC</p>
<p>% % %</p>
<p>RDA Kcal RDA</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Calories (13)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>249 K</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>Vitamin</p>
</blockquote></td>
<td><blockquote>
<p>A (12)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>130</p>
</blockquote></td>
<td>RE</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Protein (13)</p>
</blockquote></td>
<td colspan="2"></td>
<td>14.9 Gms</td>
<td>24</td>
<td>24</td>
<td colspan="3"><blockquote>
<p>Ascorbic Acid (12)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>25.7</p>
</blockquote></td>
<td>Mg</td>
<td><blockquote>
<p>43</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Carbohydrate</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(13)</p>
</blockquote></td>
<td>33.0 Gms</td>
<td></td>
<td>52</td>
<td colspan="3"><blockquote>
<p>Vitamin E (0)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Fat (13)</p>
</blockquote></td>
<td colspan="2"></td>
<td>6.7 Gms</td>
<td></td>
<td>24</td>
<td colspan="3"><blockquote>
<p>Riboflavin (13)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0.2</p>
</blockquote></td>
<td>Mg</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Sodium (13)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>841.7 Mg</p>
</blockquote></td>
<td>168</td>
<td colspan="4"><blockquote>
<p>Thiamin (13)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0.3</p>
</blockquote></td>
<td>Mg</td>
<td><blockquote>
<p>17</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Potassium (13)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>581.2 Mg</p>
</blockquote></td>
<td>29</td>
<td colspan="4"><blockquote>
<p>Niacin (13)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>4.7</p>
</blockquote></td>
<td>Mg</td>
<td><blockquote>
<p>25</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 28%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Calcium (13)</p>
</blockquote></th>
<th></th>
<th>38.4</th>
<th><blockquote>
<p>Mg</p>
</blockquote></th>
<th>5</th>
<th><blockquote>
<p>Vitamin B6 (9)</p>
</blockquote></th>
<th>0.3</th>
<th><blockquote>
<p>Mg</p>
</blockquote></th>
<th>16</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Phosphorus (13)</p>
</blockquote></td>
<td></td>
<td>148.1</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>Vitamin B12 (12)</p>
</blockquote></td>
<td>0.9</td>
<td><blockquote>
<p>Mcg</p>
</blockquote></td>
<td>44</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Iron (13)</p>
</blockquote></td>
<td></td>
<td>3.1</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>Vitamin K (2)</p>
</blockquote></td>
<td>0.0</td>
<td><blockquote>
<p>Mcg</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Zinc (12)</p>
</blockquote></td>
<td></td>
<td>2.8</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>Folate (9)</p>
</blockquote></td>
<td>23.8</td>
<td><blockquote>
<p>Mcg</p>
</blockquote></td>
<td>12</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Magnesium (12)</p>
</blockquote></td>
<td></td>
<td>47.5</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Pantothenic Ac (9)</p>
</blockquote></td>
<td>0.6</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td>11</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Manganese (12)</p>
</blockquote></td>
<td></td>
<td>0.5</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Cholesterol (13)</p>
</blockquote></td>
<td>32.6</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Copper (12)</p>
</blockquote></td>
<td></td>
<td>0.3</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Linoleic Acid (11)</p>
</blockquote></td>
<td>0.5</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Selenium (2)</p>
</blockquote></td>
<td></td>
<td>16.3</td>
<td><blockquote>
<p>Mcg</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>Linolenic Acid (10)</p>
</blockquote></td>
<td>0.0</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Monounsat. Fat (10)</p>
</blockquote></td>
<td>2.6</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Polyunsat. Fat (10)</p>
</blockquote></td>
<td>0.6</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Water (13)</p>
</blockquote></td>
<td></td>
<td>103.0</td>
<td><blockquote>
<p>Ml</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Saturated Fat (11)</p>
</blockquote></td>
<td>2.4</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Ash (13)</p>
</blockquote></td>
<td></td>
<td>3.4</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Tryptophan (9)</p>
</blockquote></td>
<td>0.16</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Alcohol (0)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Threonine (9)</p>
</blockquote></td>
<td>0.54</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Caffeine (0)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Isoleucine (9)</p>
</blockquote></td>
<td>0.59</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Total Diet Fiber</p>
</blockquote></td>
<td><blockquote>
<p>(12)</p>
</blockquote></td>
<td>3.4</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Leucine (9)</p>
</blockquote></td>
<td>1.02</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Total Tocopherol</p>
</blockquote></td>
<td><blockquote>
<p>(0)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Lysine (9)</p>
</blockquote></td>
<td>0.89</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Capric Acid (4)</p>
</blockquote></td>
<td></td>
<td>0.01</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Methionine (9)</p>
</blockquote></td>
<td>0.30</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lauric Acid (5)</p>
</blockquote></td>
<td></td>
<td>0.01</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Cystine (9)</p>
</blockquote></td>
<td>0.22</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Myristic Acid (10)</p>
</blockquote></td>
<td>0.16</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Phenylalanine (9)</p>
</blockquote></td>
<td>0.57</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Palmitic Acid (10)</p>
</blockquote></td>
<td>1.40</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Tyrosine (9)</p>
</blockquote></td>
<td>0.43</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Palmitoleic Acid (8)</p>
</blockquote></td>
<td>0.22</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Valine (9)</p>
</blockquote></td>
<td>0.64</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Stearic Acid (10)</p>
</blockquote></td>
<td>0.70</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Arginine (9)</p>
</blockquote></td>
<td>0.79</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Oleic Acid (11)</p>
</blockquote></td>
<td>2.30</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Histidine (9)</p>
</blockquote></td>
<td>0.41</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Arachidonic Acid (3)</p>
</blockquote></td>
<td>0.02</td>
<td><blockquote>
<p>Gms</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Alanine (9)</p>
</blockquote></td>
<td>0.71</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Aspartic Acid (9)</p>
</blockquote></td>
<td>1.20</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Glutamic Acid (9)</p>
</blockquote></td>
<td>3.34</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Glycine (9)</p>
</blockquote></td>
<td>0.66</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Proline (9)</p>
</blockquote></td>
<td>0.84</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Serine (9)</p>
</blockquote></td>
<td>0.57</td>
<td colspan="2"><blockquote>
<p>Gms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Grams/Portion: 248</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

#### NL Display Analyzed Recipes List \[FHREC13\]

> The Display Analyzed Recipes List option provides a list of all recipes analyzed. The \*\* preceding a recipe name indicates the recipe is nor analyzed.

> Select LIST Printer: HOME// \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> 10-Mar-05 7:53am A N A L Y Z E D R E C I P E L I S T Page 1

> RECIPE NAME

> \*\* ALL BRAN SHREDDED, IND

> \*\* ANGEL FOOD CAKE

> APPLE JELLY DIET, IND

> \*\* APPLE JELLY, IND APPLE JUICE, 4OZ IND

> \*\* APPLE JUICE, 6OZ IND APPLE JUICE, BULK APPLE PIE

> APPLESAUCE

> \*\* APRICOT DIET JELLY, IND APRICOT HALVES

> APRICOT NECTAR, BULK APRICOT/ORANGE JUICE, BULK ASPARAGUS SPEARS, FROZEN ASPARAGUS, CUTS OR SPEARS, CND

> \*\* ASSORTED DIET JELLY, IND BACON

> BACON SEASONED SPINACH

> \*\* BAKED APPLES

> \*\* BAKED POTATO

> BAKED POTATO SUPREME BAKED SWEET POTATOES BAKED WINTER SQUASH

> BAKED/GRILLED PORK CHOP - 2 BAKED/GRILLED PORK CHOPS - 1 BAKING POWDER BISCUITS

> \*\* BANANA IND BANANA PUDDING

> BARBECUED CHICKEN

> BARBECUED SLICED BEEF ON BUN BEEF BARLEY SOUP

> BEEF CUBES AU JUS BEEF NOODLE SOUP

> \*\* BEEF PATTIE, FROZEN, IND BEEF RICE SOUP

> BEEF STROGANOFF

> '\*\*' preceding a recipe name indicates recipe not analyzed.

#### PE Enter/Edit Preparation Areas \[FHING9\]

> The Enter/Edit Preparation Areas option allows you to enter and edit data in the PREPARATION AREA file \#114.2. It contains the names of all areas in the kitchen where food preparation takes place, e.g., cooks area, salad area, desserts area, etc. Facilities need to create their own preparation areas using this option and assign a preparation area to each recipe.

> Recipes on the production sheets are sorted and printed according to preparation area, and given to the appropriate production personnel. The Preparation Area field discussed under Enter/Edit Recipes (RE) uses the preparation areas from this file. This is not a mandatory field, but is highly recommended.

> Preparation Area Name: Enter ?? to view a list of preparation areas already defined. This field is 3-15 characters in length.

> Code: Enter a code 2-5 characters in length. This code displays on reports.

> Print Order: Enter a numeric value indicating the print order (from low to high) of various preparation areas for sorting by preparation area.

#### PL List Preparation Areas \[FHING10\]

> The List Preparation Areas option gives you a listing of all preparation area names, codes and print orders in the PREPARATION AREA file \#114.2.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>DEVICE: <strong>&lt;RET&gt;</strong> HYPER SPACE RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PREPARATION</p>
</blockquote></td>
<td><blockquote>
<p>AREAS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>MAR 9,2005 14:05 PAGE 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PRINT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SALAD</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SALAD</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COLD FOODS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>COLD</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>COOKS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>COOKS</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DESSERT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DESS</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### RC Re-cost Recipes \[FHREC10\]

> The Re-cost Recipes option allows you to recalculate all recipe costs. Recipe costs are calculated from ingredient costs. After ingredient costs are updated, use this routine to recalculate the recipe costs.

> Ingredient costs are updated by answering YES to the prompt “Do you want to re-cost recipes? (Y/N)” in each of the following options:

> A “YES” entry initiates the updating. The running time of this routine depends on the number of cost changes, and the size of the RECIPE and INGREDIENT files. This is how it looks when re- costing is done:

#### RE Enter/Edit Recipes \[FHREC1\]

> The Enter/Edit Recipes option allows you to enter and edit data in the RECIPE file \#114. It contains every item found on a menu. Approximately 500 VA Standardized Recipes are already in the file and you can print them using the List Recipes (RL) option. Recipes unique to a facility are added to the file. Recipes already in the file are modified to suit local practice.

> It is recommended that an initial review of recipes in the RECIPE file be conducted to identify any changes needed on those already entered. VA Recipe numbers are entered under the Synonym field for easy identification when reviewed. This field is changed to a synonym more familiar to the facility.

> Note: Every food item on a menu must have a corresponding recipe in the computer. Recipes are required to complete the MEAL and MENU CYCLE files.

> Recipe Name: The name is 3-30 characters in length. Recipe Names are entered in the same way as printed on a menu. The Synonym Name is used for an alternate description.

#### Example

> Synonym: The Synonym is not a required entry. It can be 3-25 characters in length.

> Number of Portions: The Number of Portions is a required entry that indicates the number of portions per recipe. It should be a whole number between 1 and 1000. It is recommended that you enter the number of portions according to the amount usually produced. This does not have to be 100 portions.

> Portion Size: The Portion Size is a required field that must be a number followed by OZ, FLOZ, or EACH.

#### Examples

- 4 OZ
- 6 FLOZ
- 1 EACH

> Portion sizes multiplied by the number of recipe portions required for a meal are used to generate meal distribution weights, volumes, or quantities (each) for each recipe. If the Meal Distribution report is used, portion sizes must be accurate for type of distribution. This field is especially important for individual proportioned items, e.g., Milk, Diet Supplements, Bread Slices, Individual 4 oz Juice, etc. This concept is discussed further under Meal Production Reports (MR).

#### Example

> A facility uses individual 8 oz containers of Milk. Production Reports indicate 100 servings are needed.

- If Milk recipe portion size is 1 - EACH, the Meal Distribution Report lists 100 EACH.
- If Milk recipe portion size is 8 - FLOZ, the Meal Distribution Report lists 6.2 gal.

> Preparation Time: The Preparation Time is not required and is free text up to 10 characters in length. Preparation time does not adjust for the number of portions being prepared.

> Equipment: Equipment is not a required entry. Multiple equipment names can be entered; each name 3-21 characters in length. This field points to the EQUIPMENT file (114.4) and designates all types of equipment used in preparation of a recipe. You select a piece of equipment for this field already in the EQUIPMENT file or enter a new one. Entering a new one in this field automatically adds that piece of equipment to the EQUIPMENT file.

> Serving Utensil: Serving utensil is not a required field. This field points to the SERVING UTENSIL file that designates all types of utensils required for serving a recipe by tray line personnel or cafeteria line personnel. If the utensil is not in the list, add it using the Enter/Edit Serving Utensils (SE) option.

> Default Category: The Default Category is a required entry. This field points to the RECIPE CATEGORY file that designates categories to which recipes are assigned. New recipe categories are created through Enter/Edit Recipe Categories (CE). Only one category is entered for each recipe. The recipe category determines the order in which recipes are listed on the Print Diet Menus (DP), Print Weekly Menu (WP), Print Diet Cards (PD) and Print Tray Tickets (PT). If there is no recipe category assigned to a recipe in the MEAL file (Enter/Edit Meals (ME) option), the recipe category defaults back to the category entered in this field.

> Pre-Prep State: The Pre-Prep State is not a required entry. It designates the preparation state of a recipe. A master listing, which cannot be edited, comes with the program and can be viewed by entering a question mark (?) after this field.

> The Pre-Prep State prints on the recipe list and can be helpful when reviewing the recipes in the RECIPE file. If a facility uses both convenience and conventional food items such as Beef Stew, the Pre-Prep State can identify which items are added to the RECIPE file.

> Preparation Area: The Preparation Area is not a required entry. New preparation areas are created through the Enter/Edit Preparation Area (PE) option. Preparation areas are used to sort

> recipes that are listed on the Meal Production Reports (MR). Each recipe may only have one preparation area. Some recipes are needed in two prep areas; the area assigned to a recipe needs to reflect the best way reports are used.

#### Example

> When preparing Bean Salad, first the beans are cooked in the Cooks Prep area and then the salad is mixed and portioned in the Salad Prep area. In this example, the Bean Salad recipe is assigned to the Cooks Prep area and is shared with the Salad Prep area, as it only displays on the Cooks Prep list.

> \# Days Pre-Prep: The Number of Days Pre-Prep is not a required entry. Enter a whole number, 0-3. If the recipe contains an ingredient or partially prepared item that requires advance preparation, this field should contain the number of advance days needed for preparation.

#### Example

- Potatoes may be cooked and diced the day before making potato salad: therefore, the \#

> Days

- Pre-Prep would be 1.

> Although data in this field is not currently functional, it will be used in future programs to identify items needing advance preparation. To prevent extensive file review and back-entry of data in the future. It is recommended that this field be completed during initial data entry.

> Print Recipe: This field specifies which recipes automatically print with Meal Production Reports (MR). The Meal Production Reports (MR) routine is designed to automatically print all recipes needed for production of a meal. You can print some recipes and not others or print none at all.

> These different printing runs are controlled through different mechanisms. The selection of individual recipes to print is controlled by this field. A “YES” in this field causes the recipe to print automatically with the reports. A “NO” in this field permanently suspends printing of this recipe as an automatic part of production reports. The “NO” does not affect printing of adjusted recipes. Automatic printing of recipes can be temporarily suspended, if desired, at the time the Meal Production Reports are requested by answering “NO” at the prompt “Do you want printed recipes?”.

#### Example

> These recipes have the following Print field entries:

> At the prompt “Do you want printed recipes?”, a “YES” causes printing of recipes for Beef Stew and Beet Salad; a “NO” suspends printing of all recipes. All four items will always list on the

> Production Summary with preparation quantities, but there will not be hard-copy recipes for all of them.

> Ingredient: The Ingredient field is not required and points to/uses the ingredients from the INGREDIENT file. Enter all ingredients and quantities in a recipe in the same recipe unit as listed in the master INGREDIENT file. The appropriate recipe unit is displayed after entering the ingredient name. In order to obtain a nutritional analysis of a recipe, each ingredient must also be associated with a Nutrient and the Nutrient Amount in LBS. The Associated Nutrient field uses nutrients from the FOOD NUTRIENTS file \#112.

#### Example

> Using the above example when entering quantities, the program automatically converts the quantity of 18 oz to 1 lb. 2 oz.

> Quantity: Enter a quantity with a unit of measure. If the ingredient quantity is changed, manually recalculate and enter the Nutrient Amount in LBS.

> Associated Nutrient: and Nutrient Amount in LBS: When entering the ingredient, the program automatically enters the Associated Nutrient and the Nutrient Amount in LBS, if the Nutrient Data Reference and Weight of Recipe Unit in LBS fields are previously entered in the master INGREDIENT file.

> There is no limit to the number of ingredients, you can enter for each recipe. It is suggested that ingredients be entered in the order of appearance in the recipe. Although neither the Ingredient field nor the Embedded Recipe field (below) is required, at least one or the other must be present for reports to print properly.

> Embedded Recipe: The Embedded Recipe is not required. Recipes for this field are selected from the RECIPE file. An embedded recipe is a recipe within a recipe.

#### Example

> Cream Sauce within Delmonico Potatoes

> When an embedded recipe is entered, the portion size for the recipe is displayed and a prompt displays asking for the number of portions required. Embedded recipes usually follow the original recipe when printing only if “YES” is answered to the Print Recipe field when you created the recipe under the Enter/Edit Recipe (RE) option. The exception to this is when the embedded recipe is not only part of another recipe, but is also on the menu.

#### Example

> Chicken Broth is used as an embedded recipe in Chicken Gravy, but is also used as a recipe for Clear Liquid diets. In this example, the Chicken Broth recipe does not print following the Chicken Gravy recipe, but the program prints a Chicken Broth recipe with the sum of the quantities needed for the entire meal. The Chicken Gravy recipe states the number of portions of Chicken Broth required with an asterisk next to the Chicken Broth indicating that it is an embedded recipe.

> There is no limit to the number of embedded recipes that you can enter.

> Directions: Directions are not required. This is a free text field. All recipe directions are entered under this field. Directions do not include quantitative information, because it is free text and is not adjusted when recipe quantities are increased and/or decreased.

> Diabetic Exchange: This multiple contains the Diabetic exchanges associated with this recipe.

#### RL List Recipes \[FHREC3\]

> The List Recipes option prints a list of all recipes in the RECIPE file \#114. It includes data from the following fields: Recipe Name, Synonym, Category, Pre-Prep State, E-Prep (Early Prep), Print and Cost. The cost per portion is calculated from the entries made in the Ingredient Cost field under Enter/Edit Ingredients (IE) or Edit Ingredient Cost (IC) in the Budget Asst. Menu.

> This list is sorted by recipe category and alphabetized.

> The List Recipes report includes a column indicating whether or not a recipe contains an

> *embedded* recipe.[<sup>1</sup>](#_bookmark82)

> The list requires a 132-column printer.

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 3%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select LIST Printer: HOME// (Printer Name)</p>
<p>25-Jun-07 11:33am R E C I P E L</p>
<p>Page 1</p>
<p>NAME SYNONYM CATEGORY COST</p>
<p>RECIPES EMBEDDED?</p>
</blockquote></th>
<th><blockquote>
<p>I S T PRE-PREP</p>
</blockquote></th>
<th><blockquote>
<p>STATE</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>E-PREP PRINT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>--</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PEAS WITH PEARL ONIONS V-70 VEGETABLE 1</p>
</blockquote></td>
<td><blockquote>
<p>FROZEN</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.167</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PUREED SEAS MIXED GREENS VEGETABLE 1</p>
</blockquote></td>
<td></td>
<td colspan="2">NO</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SAUTED CABBAGE SAUT CABBAGE VEGETABLE 1</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>0.011</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SEAS CORN=VEG VEGETABLE 1</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.081</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>YES EMBEDDED RECIPES: SEAS CORN</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SEASONED YELLOW SQUASH VEGETABLE 1</p>
</blockquote></td>
<td><blockquote>
<p>FROZEN</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SEASONED YELLOW SQUASH,LS VEGETABLE 1</p>
</blockquote></td>
<td><blockquote>
<p>FROZEN</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SUCCOTASH,LS 2 OZ=1VEG VEGETABLE 1</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0.151</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>YES EMBEDDED RECIPES: BUTTERED SUCCOTASH,LS</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pureed carrots,cnd VEGETABLE 1</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <sup>1</sup> Patch FH\*5.5\*8 September 2007 Added a column, Recipes Embedded? to the List Recipes report.

#### Budget Asst. \[FHBUD\]

> The Budget Asst. menu allows access to the administrative report function and functions requiring the cost input. Suggested users of this menu are Budget Clerks.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AM</p>
</blockquote></th>
<th><blockquote>
<p>Administrative Menu [FHADMR]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IC</p>
</blockquote></td>
<td><blockquote>
<p>Edit Ingredient Cost [FHADMR8]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PU</p>
</blockquote></td>
<td><blockquote>
<p>Projected Usage [FHPRR1]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WP</p>
</blockquote></td>
<td><blockquote>
<p>Print Weekly Menu [FHPR7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XI</p>
</blockquote></td>
<td><blockquote>
<p>Ingredient Management[FHINGM]</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### RP Print Adjusted Recipe \[FHREC2\]

> The Print Adjusted Recipe option allows you to print an adjusted recipe for the exact number of portions requested. It is useful for printing a recipe that is not automatically printed or for reprinting one that needs further adjustment.

> All quantities of ingredients in a recipe are automatically adjusted for the desired yield. The units of measure for Volume, Weight and Each are as follows:

> Standard conversion measures are used to adjust ingredients in recipes e.g., 1 GAL = 4 QTS. The program also uses a conversion of 2 TBSP = 1 OZ in both volume and weight adjustments.

> Fractional quantities are adjusted down to the next two smaller measures. The smallest measure that prints is 1/8 TSP. This 1/8 TSP prints even if the recipe quantity is less than 1/8 TSP.

> Recipe Name: Enter a recipe from the RECIPE file.

> Number of Portions: This is a required field. This is the number, 1-5000, of portions to which you adjust the recipe.

#### RU List Recipe Usage in Meals/Cycles \[FHPRC10\]

> The List Recipe Usage in Meals/Cycles option gives you the ability to identify all meals/cycles in which a specific recipe is located. The Meal Name, Cycle, Day of Cycle and Meal (B, N, or E) is listed for the designated recipe. The data generated can be used to determine the frequency of a recipe in a cycle as well as its specified location.

> This information is also useful if you need to delete a recipe from the RECIPE file \#114. This option helps you identify which meals to alter before a recipe is deleted. If a recipe is deleted from the RECIPE file (Enter/Edit Recipes option) and not from the MEAL file (Enter/Edit Meals option) in which it is entered, a system error occurs when Production Reports are run. The program searches for a recipe that no longer exists. This is the principle source of unidentified errors. Using this option, all meals are listed for the designated recipe and therefore you can accurately adjust it.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 7%" />
<col style="width: 47%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Select RECIPE NAME: <strong>RASPBERRY GELATIN</strong></p>
</blockquote></th>
<th rowspan="18"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Select LIST Printer: HOME// (Printer Name)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>10-Mar-05 8:07am R E C I P E U S A G E Page 1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>RASPBERRY GELATIN</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Meal Cycle</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CYII-WKI-SUN-TURKEY</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>II - 88, Day 1, Noon</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CYIII-WKI-TUE-PORK CHP/MUSHGRY</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>III - 88, Day 3, Evening</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CYI-89-WKII-THR-BF CHOP SUEY</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 89, Day 12, Noon</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CYII-89-WKI-TUE-PORKCHOP</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>II - 89, Day 3, Evening</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CYI-03-WKII-THR-BF CHOP SUEY 03 DAY B4 HALLOWEEN</p>
<p>MERRY XMAS SUPPER 1903 1991 XMAS EVE</p>
<p>SAINT PATRICK'S DAY 02 CI-03-1-TE-SPAG/MTBALLS</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 03, Day 12, Noon</p>
<p>I - 93, Day 3, Evening</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CI-03-1-RE-FR FISH</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 5, Evening</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CI-03-1-FN-HOT TURK SAND</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 6, Noon</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CI-03-3-SE-STUFFEDPEPPER</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 15, Evening</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CI-03-2-ME-SAUERBRATEN</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 9, Evening</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CI-03-2-WB-SCR EGGS</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 11, Breakfast</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CI-03-2-FN-PIZZA BURGER</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 13, Noon</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CI-03-3-RN-SPAGHETTI</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 19, Noon</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CI-03-4-MN-TURK SAND</p>
</blockquote></th>
<th><blockquote>
<p>CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>I - 93, Day 23, Noon</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### SE Enter/Edit Serving Utensils \[FHREC6\]

> The Enter/Edit Serving Utensils option allows you to enter and edit data in the SERVING UTENSIL file \#114.3, which is a listing of the types of utensils used in food service. You can add additional utensils The Serving Utensil field of the RECIPE file points to the SERVING UTENSIL file. It is not mandatory but if completed, the serving utensil display on the printed recipe.

#### Example

> 6 OZ. LADLE, \#8 SCOOP, SPOON, etc.

> You can view the contents of this file using List Serving Utensils (SL).

> Serving Utensil Name: This field is 1-10 characters in length and refers to the types of serving utensils used in recipes.

#### SL List Serving Utensils \[FHREC7\]

> The List Serving Utensils option produces a list of all serving utensils stored in the SERVING UTENSIL file \#114.3.

### XX Annual Report Management \[FHADRR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EA</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Facility Profile [FHADR1]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EB</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Hospital Outpatient Visits [FHADR3]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EC</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Type of Service [FHADR2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ED</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Staffing FTEE [FHADR4]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EE</p>
</blockquote></td>
<td><blockquote>
<p>Enter the Snapshot date for Modified Diets [FHADR5]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EF</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Cost Per Diem [FHADR6]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EG</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Nutrition Satisfaction Survey [FHADR7]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EH</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Nutrition Service Equipment [FHADR8]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EI</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Nutritive Analysis Average [FHADR9]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PR</p>
</blockquote></td>
<td><blockquote>
<p>Print Annual Nutrition Report [FHADRP]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PU</p>
</blockquote></td>
<td><blockquote>
<p>Purge Old Annual Nutrition Data [FHADRS]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Annual Report Management allows you to enter the information required in the Annual Report that is not automatically retrieved from other Nutrition programs. Data is aggregated quarterly and annually, printing all information entered. This report is useful in tracking quarterly meals, costs, workload statistics, clinical activities, and patient satisfaction.

#### Managing Annual Reports

> This program automates the Nutrition Annual Report. The standardization of data allows for future ability to sort and retrieve data from comparable groups of facilities. A report compiles a combination of electronic data captured from VistA and manual data collection from readily available reports. A report contains aggregate data of the four quarters of the fiscal year, but is generated quarterly. This program allows you to enter, edit, and review the Facility Profile, Facility Workload Statistics, Nutrition Workload Statistics, Staffing, Nutrition Cost, Patient Satisfaction, and Service Equipment.

#### Sources of Data

> The following data is automatically retrieved/calculated from VistA records:

- Inpatient Days of Care and Total Served Meals from the VistA Nutrition Served Meal Report (RR)
- Staffing FTEE using the VistA Nutrition Staffing Data Report (PR)
- The percent modified diets using the VistA Diet Order Census at 5:55 PM
- The Nutrition Status and Clinical Encounter Categories data from the VistA Nutrition Status Summary (NS) and Nutrition Encounter Statistics (SE) programs

> If the facility is not using the options that automatically calculate data, certain parts of the Annual Report is not complete.

> The following data must be manually entered from paper records:

1.  Outpatient visits are acquired from Medical Administration Service Statistical Unit AMIS reports.
2.  The RPM classification and complexity level for the facility profile are obtained from the RPM coordinator and from Personnel Service.
3.  The Cost Per Diem data is retrieved from Nutrition and Food Service 830 Report of Costs.
4.  The Patient Satisfaction data is obtained from the VA 10-5387 Nutrition Satisfaction Surveys.

#### EA Enter/Edit Facility Profile \[FHADR1\]

> The Enter/Edit Facility Profile option allows you to enter and edit facility profile data. After the initial entry of this data, only changes to the facility profile, specialized medical programs, primary delivery, or primary production systems require editing the facility profile. The profile identifies facilities with like scope for comparison of Nutrition data.

> Facility Data: Management data required under these fields, includes facility region number, multi-division designation, RPM classification, and complexity level. The information defines the scope of the facility. The RPM number classifies facilities by size. The complexity level is determined by VACO criteria: size, complexity, and the grade on which structure is based.

> Nutrition training program data required in this profile identifies specific authorized training programs at the facility, such as VA sponsored or affiliated Nutrition Internships, affiliated or VA sponsored AP4 programs, CUPs, or Nutrition Technician programs.

> Food Management data required here identifies the primary food delivery systems used at the facility and whether or not Cook-Chill food items are served.

> Specialized Medical Programs: This data identifies the specialized medical programs authorized at the facility and the number of Clinical Nutrition FTEE assigned to each program. Nutrition Research Programs, if conducted at the facility, must be identified as funded or un- funded status. Clinical Nutrition FTEE assigned to research must also be identified.

> YR: Enter the year, not in the future.

> Station Number: Enter a station number or ? to display a list.

> Facility Data?: This is a required field.

> Region: Enter a region number, 1-7.

> RPM Classification: Enter a classification number, 1-6.

> Complexity Level: Enter a level number, 1-4.

> Primary Delivery System: Enter ? to view a list from which to select a site-specific system.

> Select 1 or 2: Enter ? to view a list of options.

> Specialized Medical Programs: Enter ? to view a list from which to select site-specific programs.

> Assigned Clinical FTEE: Enter an FTEE, a number 0-99.9.

> Areas of Research: Enter ? to view a list from which to select site-specific areas.

> Enter YR: 02

> Enter Station Number: (Station \#) Enter/Edit Facility Data? YES

> REGION \#: 2// \<RET\>

> MULTI DIVISION FACILITY?: NO// \<RET\>

> RPM CLASSIFICATION: 1// \<RET\>

> COMPLEXITY LEVEL: 1// \<RET\>

> VA SPON NUTRITION INTERNSHIP: YES// \<RET\>

> AFFILIATED AP4?: NO// \<RET\>

> AFFILIATED NUTRITION INTERN?: NO// \<RET\>

> AFFILIATED CUP?: NO// \<RET\>

> VA SPONSORED AP4?: NO// \<RET\>

> AFFILIATED NUTRITION TECH?: NO//\<RET\>

> Select PRIMARY DELIVERY SYSTEM: Pellet// \<RET\>

> DO YOU USE COOK CHILL FOODS?: Y// \<RET\> YES

> SELECT 1 OR 2: ?

> Choose from:

1.  LESS AND EQUAL 25% OF MENU ITEMS
2.  GREATER THAN 25% OF MENU ITEMS SELECT 1 OR 2: \<RET\>

> Enter/Edit Specialized Medical Programs? YES

> Select SPECIALIZED MEDICAL PROGRAMS: Substance Abuse Program // \<RET\>

> SPECIALIZED MEDICAL PROGRAMS: Substance Abuse Program // \<RET\>

> ASSIGNED CLINICAL FTEE: .5// \<RET\>

> Select SPECIALIZED MEDICAL PROGRAMS: \<RET\>

> FUNDED NUTRITION RESEARCH?: Y// \<RET\>

> ASSIGNED CLINICAL FTEE: \<RET\>

> UNFUNDED NUTRITION RESEARCH?: Y// \<RET\>

> Select AREAS OF RESEARCH: ??

> Answer with AREAS OF RESEARCH Choose from:

1.  CLINICAL
2.  COMMUNITY
3.  COST/BENEFIT
4.  EDUCATION
5.  MANAGEMENT Select AREAS OF RESEARCH: 1

> ASSIGNED TOTAL CLINICAL FTEE: .7

#### EB Enter/Edit Hospital Outpatient Visits \[FHADR3\]

> The Enter/Edit Hospital Outpatient Visits option allows you to enter a total number of hospital outpatient visits, including any satellite clinic visits. Satellite clinics are those operated away from the hospital. Hospital outpatient data is obtained from the Medical Administration Service Statistical Unit AMIS reports.

> Note: These outpatient visits refer to all hospital outpatient visits, not only nutrition visits. This data identifies facilities of comparable scope.

> Qtr/Yr: Default is the previous year.

> Outpatients Visit Hosp: Enter a number, 0-999999999.

> Number of Satellites: Enter a number, 1-5

> Satellite Loc: Enter a location, 3-20 characters in length.

> Total \# of Sat Outpat Visits: Enter a number, 0-999999999.

#### EC Enter/Edit Type of Service \[FHADR2\]

> The Enter/Edit Type of Service option allows you to identify the number (0-9999) of patient meals (average daily meals) currently served at bedside, in a cafeteria, and in a dining room area for a specified year. The dining room area is defined as a congregate eating area where trays are delivered to patients. This information is obtained from the VistA Served Meals Report (RR) option or the Location Diet Lists (WD) option. If the facility has only tray and cafeteria service, the information is found on the Served Meals Report. If the facility has dining room service, the data is tallied from the Location Diet Lists. Print the Location lists for all types of service and tally the number of bedside trays, dining room trays, and cafeteria trays.

#### ED Enter/Edit Staffing FTEE \[FHADR4\]

> The Enter/Edit Staffing FTEE option allows you to enter the Staffing FTEE data. You retrieve the FTEE data stored when the Staffing Worksheet is used and calculate the total FTEE for the quarter. The retrieved data displays as the defaults for the prompt sequence.

> Note: If you do not use the Staffing Worksheet, you need to enter the FTEE manually. You must use these options when entering data for each quarter to verify the defaults; otherwise, the data displays on the report.

> For the FTEE field definitions, refer to the Enter/Edit Staffing Data under Administrative reports.

> Qtr/Yr: Enter the quarter and year or accept the default.

> Total Daily FTEE, Clinical FTEE, Administrative FTEE, and Support Staff FTEE: Enter a number, 0-999 with up to three decimals or accept the default.

> Supervisory FTEE: Enter a number, 0-999 with up to 2 decimals.

> Staff Cert Diab: This field represents the number (0-99 with no decimals) of Nutrition staff Certified Diabetes Educators at the facility. Only those officially certified should be listed, not Nutrition Diabetes Specialists.

> Staff Cert in Nutr Supp: This field represents the number (0-99 with no decimals) of Nutrition staff officially certified in Nutrition and Food Service Support at the facility.

> Staff Reg Clin Diet Tech: This field represents the number (0-99 with no decimals) of clinical Registered Nutrition Technicians on staff at the facility.

> Staff W/Clin Privileges: This field represents the number (0-99 with no decimals) f Nutrition Staff with Clinical Privileges, such as writes diet orders, orders lab test, at the facility.

#### EE Enter the Snapshot date for Modified Diets \[FHADR5\]

> The Enter the Snapshot date for Modified Diets option allows you to automatically calculate a weekly average of modified diets per quarter. A tasked (set to run at a specific time) routine captures the number of regular diets each day at 5:55 PM. The program subtracts the regular diets from the total daily diets and the remainder are considered modified diets. The modified diet number includes NPOs, tubefeedings and passes.

> You select a Sunday date that specifies which week to use for the calculation of the weekly, modified diet average. This Sunday date can be a past date or a future date. If a future date is entered, the weekly, modified diet average does not print on the Annual Report until a week after the future date. Sunday dates are entered for each quarter and are entered in advance.

> Qtr/Yr: Enter the quarter and year or accept the default.

> Note: Past dates work only up to the date when this version of the software was loaded into the live account, because prior to this time, no data was stored.

<table style="width:100%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Enter Qtr/Yr: <strong>1 94</strong></p>
<p>Select SUNDAY Date: <strong>10/17/93</strong> (OCT 17, 1993)</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>OCT 17,1993 - OCT 23,1993</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>| X | M | T | W |</p>
<p>| Sun | Mon | Tues | Wed |</p>
</blockquote></th>
<th><blockquote>
<p>R |</p>
<p>Thur |</p>
</blockquote></th>
<th><p>F</p>
<blockquote>
<p>Fri</p>
</blockquote></th>
<th><blockquote>
<p>|</p>
<p>|</p>
</blockquote></th>
<th><p>S</p>
<blockquote>
<p>Sat</p>
</blockquote></th>
<th><blockquote>
<p>|</p>
<p>|</p>
</blockquote></th>
<th><blockquote>
<p>Total</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="7"><blockquote>
<p># Mod. Diets| 505| 505| 612| 606| 503| 594| 583| 4175</p>
<p>Total Diets | 793| 809| 822| 832| 808| 705| 779| 5638</p>
<p>Change Numbers of Modified Diets and Total Diets for that week? Y// <strong>Y</strong></p>
<p>Sun Mon Tues Wed Thur Fri Sat X M T W R F S</p>
<p>Enter string of characters for desired days of week: e.g., MWF</p>
<p>Select the Day of Week you wish to change the data on: <strong>X</strong></p>
<p>Change # of Modified Diets for Sun from 505 to: <strong>505</strong></p>
<p>Change # of Total Diets for Sun from 793 to: <strong>793</strong></p>
<p>OCT 17,1993 - OCT 23,1993</p>
<p>| X | M | T | W | R | F | S |</p>
<p>| Sun | Mon | Tues | Wed | Thur | Fri | Sat | Total</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="7"><blockquote>
<p># Mod. Diets| 505| 505| 612| 606| 503| 594| 583| 4175</p>
<p>Total Diets | 793| 809| 822| 832| 808| 705| 779| 5638</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="7"><blockquote>
<p>Change Numbers of Modified Diets and Total Diets for that week? Y// <strong>N</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### EF Enter/Edit Cost Per Diem \[FHADR6\]

> The Enter/Edit Cost Per Diem option allows you to enter or edit cost per diem per patient. Use the 830 Report of Costs for the cumulative fiscal year totals and the personal costs.

> This data is used to calculate the quarterly cumulative and year-to-date Cost Per Diem. Use the 830 Report List of Costs and FTEE Report to obtain the Nutrition cumulative fiscal year totals and the personnel costs. The Other Personnel cost is automatically calculated by subtracting the sum of personnel service, subsistence and operating supplies accounts from the total dollars.

> Qtr/Yr: Enter the quarter and year or take the default.

> Cumulative Total: Enter the cumulative fiscal year totals for the 830 report of costs.

> Personal Service: Enter total Personal Service cost.

> Personal Service-Tech: Enter the Technician's 1019 cost of Personal Service. Personal Service-Dietitian: Enter the Dietitian's 1018 cost of Personal Service. Personal Service-Wagebrd: Enter the Wageboard 1008 cost of Personal Service. Personal Service-Clerical: Enter the Clerical 1002 cost of Personal Service.

> Subsistence: Enter the Subsistence 2610 cost of Personal Service.

> Operating Supplies: Enter the Operating Supplies 2660 cost of Personal Service.

#### EG Enter/Edit Nutrition Satisfaction Survey \[FHADR7\]

> The Enter/Edit Nutrition Satisfaction Survey option allows you to enter or edit results from a Nutrition survey on a quarterly or annual basis. For those facilities that have service initiated satisfaction data, (VA 10-5387), input the number of responses for each rating, i.e., Very Good, Good, Average, Fair, and Poor. Only one set of data per quarter is stored. Those facilities who conduct monthly Nutrition patient surveys need to manually consolidate and enter results on a quarterly basis. The total number of responses and the percentage for each rating are automatically calculated on the report.

> Nutrition Survey: There are 9 Nutrition Survey categories which must have data entered in these fields. They are:

- Appetizing Food
- Taste
- Temperature
- Variety
- Cleanliness
- Courteous
- Time
- Diet Information
- Overall Rating of Nutrition Service

> Each category is rated by the following factors:

- V = Very Good
- G = Good
- A = Average
- F = Fair
- P = Poor

> Ratings are further categorized by patient population types, i.e., GM&S (General Medicine and Surgery units), NHCU ( Nursing Home Care Units), PSYCH (Psychiatry units), DOM (Domiciliary care unit), SCI (Spinal Cord Injury Unit), and Other (represents any other sub- group of patients which a facility may want to designate for satisfaction survey purposes).

> Survey responses are manually tallied with the appropriate rating data entered for each category and type.

> Survey ratings are entered by first selecting one of the 9 survey categories, and then selecting the appropriate patient population type. You are prompted to select these fields. Ratings are entered as a string in the following format: Type the first letter of the rating followed by the number of responses for that rating, type a space, and type the first letter of the next rating followed by the number of responses for that rating, and so forth.

> Qtr/Yr: Enter the quarter and year or accept the default.

> Survey Category: Enter the number of the survey category for which you want to record results.

> Service: Enter the service for which you want to record data.

> Rating string: Enter the first letter of the rating followed by the number of responses for that rating. Type a space and enter the first letter of the next rating, followed by the number of responses for that rating, and so on.

#### Example

> V20 G40 A3 P1

> This example indicates that for Very Good (V), there are 20 responses, for Good (G), there are 40 responses, for Average (A), there are 3 responses, and for Poor (P), there is 1 response.

#### EH Enter/Edit Nutrition Service Equipment \[FHADR8\]

> The Enter/Edit Nutrition Service Equipment option allows you to track specialized pieces of equipment in use throughout the system. It is used to determine the location where equipment is in use and to track the progress of technology. You enter data for each piece of equipment that the facility has on the Service Equipment list. This option also requires data entry on the total CMR equipment cost for the department. If a facility has more than one CMR, all CMRs are consolidated for the total inventory cost.

> Yr: Enter a year, but not a future year.

> Nutrition Equipment: The Nutrition Equipment field contains the pointer to the NUTRITION REPORT CATEGORY file. Enter ? to view a list of Nutrition Service Equipment. Select one that the facility has.

> Brand: Enter the brand of the Service Equipment with a name 3-45 characters in length.

> Nutrition Equipment: Enter another piece of equipment, or press \<RET\> to continue.

> CMR Equipment Inv Cost: Enter the department’s total equipment cost as stated on CMR(s) with a number, 0-999,999,999, with no decimal points.

#### EI Enter/Edit Nutritive Analysis Average \[FHADR9\]

> The Enter/Edit Nutritive Analysis Average option requires you to enter data on the average nutritive analysis for a regular diet. Data is calculated by using the Energy Nutrient Analysis (EA) options.

> Yr: Enter the year.

> Nutritive Analysis Date: This is a required entry. Enter the date the Nutritive Analysis was done.

> Calories: Type a number, 0-9999 with no decimals.

> % CHO: Type a number, 0-99 with no decimals.

> % PRO: Type a number, 0-99 with no decimals.

> % FAT: Type a number, 0-99 with no decimals.

> MG CHOL: Type a number, 0-99999 with no decimals.

> MG NA: Type a number, 0-99999 with no decimals.

#### PR Print Annual Nutrition Report \[FHADRP\]

> Nutrition Reports

> Existing reports include outpatient meals information and allow you to select single, multiple, or all for each communication office. If the report is a census, it automatically calculates and populates tabulated fields. The reports are listed in the Dietetics Lists/Reports option \[FHCDLST\].

> The Print Annual Nutrition Report option allows you to print the final report after all the data is put in for the year. Data for each section of the report is retrieved several sources.

> Section I Facility Profile: The information printed in this section comes directly from the Enter/Edit Facility Profile (EA) option.

> Section II Facility Workload Statistics: The inpatient data is retrieved from the Enter/Edit Served Meals Report (RE) option. The outpatient data comes from the Enter/Edit Hospital Outpatient Visits (EB) option.

> Section III Nutrition Workload Statistics: The Served Meals information is obtained from the Enter/Edit Served Meals Report (RE) option, and the Type of Service from the Enter/Edit Type of Service (EC) option. The Nutrition Status Summary information is retrieved automatically from the Enter Patient Nutrition Status (ES) option. The Clinical Encounter Category Summary is automatically calculated from the Enter/Edit Encounters (EE) option. However, in order for the program to categorize all encounters entered on a daily basis, the Clinical Manager must enter a clinical category on each encounter in the ENCOUNTER TYPES file \#115.6. This is done through the Enter/Edit Encounter Types (ET) option under the Clinical Management Menu. The Modified Diet Summary information is automatically calculated by entering a date under the Enter The Snapshot Dates For Modified Diets (EE) option. The program then calculates a weekly average of modified diets per quarter. The Nutritive Analysis is an average of a Regular diet for one week, which is entered under the Enter/Edit Nutritive Analysis Average (EI) option.

> Section IV Staffing: The FTEE and specialty staff information is retrieved from the Enter/Edit Staffing FTEE (ED) option. Measured FTEE is whatever is left over after subtracting each area from the total average FTEE for the quarter.

> Section V Nutrition Cost: The Cost Per Meal and the Cost Per Diem information is retrieved from the Enter/Edit Served Meals Report (RE) option and the Enter/Edit Cost Per Diem (EF) option.

> Section VI Patient Satisfaction: Information in this section is retrieved from the Enter/Edit Nutrition Survey (EG) option.

> Section VII Equipment: Equipment and CMR information in this section is retrieved from the Enter/Edit Equipment (EE) option.

> Station Number: Enter the station number or type ? to view a list.

> Yr: Enter the last two digits of the year, such as 94.

> Device: Enter the name of the printer, which can print 132 columns. This report must be queued, because it is a time consuming process.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 4%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Enter Station Number: (Station</p>
<p>Enter YR: <strong>94</strong></p>
</blockquote></th>
<th><blockquote>
<p>#)</p>
</blockquote></th>
<th colspan="2" rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>QUEUE TO PRINT ON DEVICE:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>9-Mar-05 3:14pm</p>
<p>Page 1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>D I E T E T I C</p>
</blockquote></td>
<td><blockquote>
<p>R E P O R T</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 - 4 Qtr FY 02</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 32%" />
<col style="width: 26%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Avg</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>YTD</p>
</blockquote></th>
<th><blockquote>
<p>Avg</p>
</blockquote></th>
<th><blockquote>
<p>Avg</p>
</blockquote></th>
<th><blockquote>
<p>Avg</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Status 4th Qtr</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Tot Avg</p>
</blockquote></td>
<td>1st Qtr</td>
<td>2nd Qtr</td>
<td>3rd Qtr</td>
</tr>
<tr class="even">
<td><blockquote>
<p>I NORMAL 343</p>
<p>%</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1240</p>
</blockquote></td>
<td><p>256</p>
<p>30.5</p></td>
<td><blockquote>
<p>309</p>
<p>35.5</p>
</blockquote></td>
<td><blockquote>
<p>332</p>
<p>39.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>40.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>36.4</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>II MILDLY 243</p>
<p>%</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>COMPROMISED 850</p>
</blockquote></td>
<td><p>154</p>
<p>18.3</p></td>
<td><blockquote>
<p>185</p>
<p>21.2</p>
</blockquote></td>
<td><blockquote>
<p>268</p>
<p>31.6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>28.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>24.9</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>III MODERATELY COMPROMISED 85 478</p>
<p>%</p>
</blockquote></td>
<td><p>160</p>
<p>19.0</p></td>
<td><blockquote>
<p>152</p>
<p>17.5</p>
</blockquote></td>
<td><blockquote>
<p>81</p>
<p>9.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>10.0 14.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>IV SEVERELY 24</p>
<p>%</p>
</blockquote></td>
<td><blockquote>
<p>COMPROMISED 180</p>
</blockquote></td>
<td><p>74</p>
<p>8.8</p></td>
<td><blockquote>
<p>56</p>
<p>6.4</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
<p>3.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>2.8</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>UNC UNCLASSIFIED 156 663</p>
<p>%</p>
</blockquote></td>
<td><p>196</p>
<p>23.3</p></td>
<td><blockquote>
<p>169</p>
<p>19.4</p>
</blockquote></td>
<td><blockquote>
<p>142</p>
<p>16.7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>18.3 19.4</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>TOTAL</p>
<p>851 3411</p>
</blockquote></td>
<td>840</td>
<td>871</td>
<td>849</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 17%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>9-Mar-05</p>
<p>Page 5</p>
</blockquote></th>
<th><blockquote>
<p>3:14pm</p>
</blockquote></th>
<th>D</th>
<th><blockquote>
<p>I</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th><blockquote>
<p>I C</p>
</blockquote></th>
<th>R</th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>P</p>
</blockquote></th>
<th><blockquote>
<p>O</p>
</blockquote></th>
<th><blockquote>
<p>R</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>T</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="17"><blockquote>
<p>1 - 4 Qtr FY 02</p>
<p>S E C T I O N VI P A T I E N T S A T I S F A C T I O N</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUTRITION</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURVEY</p>
</blockquote></td>
<td>1st Qtr</td>
<td colspan="6">2nd</td>
<td>Qtr</td>
<td colspan="5"><blockquote>
<p>3rd Qtr</p>
</blockquote></td>
<td><blockquote>
<p>4th</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="17"><blockquote>
<p>Qtr YTD Rtng</p>
<p>Num Rtng Num Rtng Num Rtng Num</p>
<p>Rtng ToT Avg Temperature</p>
<p>GM&amp;S 05 3.89 208</p>
<p>4.12 303 4.01</p>
<p>NHCU 100 3.70 116</p>
<p>3.73 216 3.72</p>
<p>PSYCH 106</p>
<p>3.81 106 3.81</p>
<p>DOM 22</p>
<p>3.91 22 3.91</p>
<p>SCI 32</p>
<p>3.78 32 3.78</p>
<p>OTHER 22</p>
<p>4.55 22 4.55</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PU Purge Old Annual Nutrition Data \[FHADRS\]

> The Purge Old Annual Nutrition Data option allows you to purge entries older than three years. When you select this option, the program calculates the year that is three years ago and displays the default. You can select a different year.

> Caution: Select the year with care. This program purges/removes all the entries prior to the year selected. If you are unsure, accept the default.

# CM Clinical Management \[FHMGRC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CD</p>
</blockquote></th>
<th><blockquote>
<p>Clinical Dietetics… [FHDIET] (User Manual)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DM</p>
</blockquote></td>
<td><blockquote>
<p>Patient Data Log [FHDMP]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XC</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Management Menu… [FHASCX]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XD</p>
</blockquote></td>
<td><blockquote>
<p>Diet Order Management… [FHORDX]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XE</p>
</blockquote></td>
<td><blockquote>
<p>Energy/Nutrient Management… [FHNUX]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XF</p>
</blockquote></td>
<td><blockquote>
<p>File Manager… [FHFILM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM</p>
</blockquote></td>
<td><blockquote>
<p>Consult Management… [FHORCX]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XS</p>
</blockquote></td>
<td><blockquote>
<p>Supplemental Feeding Management… [FHNOX]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Clinical Management focuses on site-specific parameters that the Nutrition and Food Service uses for assessment and screening programs, and for the Nutrition Encounters program.

> Parameters are set to each facility's specific patient population-type. The Encounters program automatically captures nutrition status, assessment events, and other designated encounter data in a statistical report used in quality management and clinical decision-making.

> Clinical Management provides access to all options pertaining to clinical Dietetics. Suggested users of this menu are Clinical Supervisors.

#### Clinical Dietetics \[FHDIET\]

> Clinical Dietetics contains all of the various options that Clinical Nutrition and Food Service staff require. Suggested users of this menu are Clinical Dietitians.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DC</p>
</blockquote></th>
<th><blockquote>
<p>Dietetic Consults [FHORCM]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DO</p>
</blockquote></td>
<td><blockquote>
<p>Diet Orders [FHORDM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DR</p>
</blockquote></td>
<td><blockquote>
<p>Dietetic Lists/Reports [FHCDLST]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EA</p>
</blockquote></td>
<td><blockquote>
<p>Energy/Nutrient Analysis [FHNUM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FP</p>
</blockquote></td>
<td><blockquote>
<p>Food Preferences [FHSELM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LE</p>
</blockquote></td>
<td><blockquote>
<p>List Encounters [FHASE7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Patient Management [FHASCM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PE</p>
</blockquote></td>
<td><blockquote>
<p>List Patient Events [FHORX2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PM</p>
</blockquote></td>
<td><blockquote>
<p>Patient Movements [FHPATM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SF</p>
</blockquote></td>
<td><blockquote>
<p>Supplemental Feedings [FHNOM]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SO</p>
</blockquote></td>
<td><blockquote>
<p>Standing Orders [FHSPM]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TF</p>
</blockquote></td>
<td><blockquote>
<p>Tickler File [FHCTF]</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Clinical Dietetics \[FHTECH\]

> The Clinical Dietetics menu is the same as the Clinical Dietetics \[FHDIET\] menu only the options are arranged in a different order. Suggested users of this menu are the Nutrition Technicians.

## DM Patient Data Log \[FHDMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Data Log option allows you to print all of the Nutrition data for an admission or an outpatient visit. It is a patient-specific record containing all diet order-entry information for a specified date range. The log contains the activity, the exact date and time of data entry, and the name of the person who entered the order, which are used for tracking diet order-entry activity and facilitate accountability for entry.

> This is especially helpful for long term care patients who may have many months of data and the user is only interested in information from the last few days. All fields display data since the date specified or the last occurrence. Also, if an NPO is canceled, the user who canceled the NPO and the date it was canceled, are saved and display in the data log.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 42%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Select Patient (Name or SSN): <strong>NFS,PATIENT ONE</strong> 01-12-41 000000001</p>
<p>COLLATERAL</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Choose from:</p>
<p>1 12-11-1903 @ 08:54:15</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Select ADMISSION (or C for CURRENT): <strong>1</strong> 2031211.085415</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Starting Date: FIRST// <strong>&lt;RET&gt;</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>DEVICE: HOME// <strong>&lt;RET&gt;</strong> HYPER SPACE RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>000-00-0001 NFS,PATIENT ONE Female Age 54 Page</p>
</blockquote>
<p>8-Mar-05 12:43pm</p></td>
<td>1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>P A T I E N T</p>
</blockquote></td>
<td><blockquote>
<p>D A T A</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Allergies: STRAWBERRIES, CHOCOLATE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Food Preferences Currently on file:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Likes</p>
</blockquote></td>
<td><blockquote>
<p>Dislikes</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>All Meals 1 GELATIN</p>
<p>Break 1 ORANGE JUICE, 2 MILK</p>
<p>Noon 1 PIZZA PUFFS</p>
<p>1 WHOLE-WHEAT BREAD</p>
<p>1 POTATO CHIPS, 1 WHITE BREAD Noon,Even 2 TANGERINE</p>
<p>Even 2 TACO</p>
</blockquote></td>
<td><blockquote>
<p>NO LIVER, NO SHRIMPS NO GREEN FOODS</p>
<p>NO PORK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>A D M I S S I O N D A T A</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Admitted: 11-Dec-03 8:54am Discharged: 24-May-04 12:09pm</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Current Diet Order: 9 Expires: Current Service: Tray</p>
<p>Current Isolation: Current Tubefeed Order:</p>
<p>Last Label Location: NEW 3 NORTH Current Supp. Fdg. Order: Last Label Room: 103-02</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 93%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>D I E T O R D E R S</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Order: 1 Effective: 17-Sep-03 12:25pm Expires:</p>
<p>Ordered by: NFSDOCTOR,ONE Ordered: 17-Sep-03 12:25pm Diet: REGULAR</p>
<p>Prod. Diet: REGULAR Service: Tray</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order: 2 Effective: 18-Sep-03 11:52am Expires:</p>
<p>Ordered by: NFSDOCTOR,ONE Ordered: 18-Sep-03 11:53am Diet: 100gm PRO</p>
<p>Prod. Diet: LOW PROTEIN Service: Tray</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-00-0001 NFS,PATIENT ONE Female Age 54 Page</p>
</blockquote>
<p>8-Mar-05 12:43pm</p></td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order: 3 Effective: 15-Oct-03 10:39am Expires:</p>
<p>Ordered by: Ordered: 15-Oct-03 10:40am</p>
<p>Diet: NO ORDER</p>
<p>Comment: Hold Tray due to Tubefeeding</p>
<p>Prod. Diet: Service:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order: 4 Effective: 13-Nov-03 8:31am Expires: 13-Nov-03 8:32am Ordered by: NFSDOCTOR,ONE Ordered: 13-Nov-03 8:32am Diet: NPO</p>
<p>Prod. Diet: Service:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order: 5 Effective: 21-Nov-03 9:51am Expires:</p>
<p>Ordered by: NFSDOCTOR,ONE Ordered: 21-Nov-03 9:52am Diet: REGULAR</p>
<p>Prod. Diet: REGULAR Service: Tray</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order: 6 Effective: 16-Dec-03 Expires:</p>
<p>Ordered by: NFSDOCTOR,ONE Ordered: 13-Dec-03 8:51am Diet: REGULAR</p>
<p>Prod. Diet: REGULAR Service: Tray</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order: 7 Effective: 14-Dec-03 2:36pm Expires:</p>
<p>Ordered by: DIET,DIET Ordered: 14-Dec-03 2:37pm Diet: NO ORDER</p>
<p>Comment: Hold Tray due to Tubefeeding</p>
<p>Prod. Diet: Service:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order: 8 Effective: 19-Dec-03 12:50pm Expires:</p>
<p>Ordered by: Ordered: 19-Dec-03 12:51pm</p>
<p>Diet: NO ORDER</p>
<p>Comment: Hold Tray due to Tubefeeding</p>
<p>Prod. Diet: Service:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order: 9 Effective: 19-Dec-03 12:52pm Expires:</p>
<p>Ordered by: NFSDOCTOR,ONE Ordered: 19-Dec-03 12:53pm Diet: NO ORDER</p>
<p>Comment: Hold Tray due to Tubefeeding</p>
<p>Prod. Diet: Service:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D I E T O R D E R S E Q U E N C E</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="17" type="1">
<li><p>Sep-03 12:25pm Order: 1</p></li>
<li><p>Sep-03 11:52am Order: 2</p></li>
</ol>
<blockquote>
<p>15-Oct-03 10:39am Order: 3</p>
<p>13-Nov-03 8:31am Order: 4</p>
<p>13-Nov-03 8:32am Order: 3</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 93%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>21-Nov-03 9:51am Order: 5</p>
</blockquote>
<ol start="13" type="1">
<li><p>Dec-03 8:51am Order: 6</p></li>
<li><p>Dec-03 2:36pm Order: 7</p></li>
</ol>
<blockquote>
<p>19-Dec-03 12:52pm Order: 8</p>
<p>19-Dec-03 12:53pm Order: 9</p>
<p>000-00-0001 NFS,PATIENT ONE Female Age 54 Page</p>
</blockquote>
<p>8-Mar-05 12:43pm</p></th>
<th>3</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>S U P P L E M E N T A L F E E D I N G S</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order: 1 Menu: INDIVIDUALIZED</p>
<p>Ordered: 10-Dec-03 10:50am By: NFSDOCTOR,ONE</p>
<p>Reviewed: 10-Dec-03 10:50am By: NFSDOCTOR,ONE</p>
<p>Cancelled: 14-Dec-03 10:03am By: NFSDOCTOR,ONE</p>
<p>Type: Dietary Diet Associated: No</p>
<p>10 Am 1 CEREAL II/BOWL/SPOON; 1 MILK, SKIM</p>
<p>2 Pm 1 CRAX PEANUT BUTTER; 1 JUICE, ORANGE 4OZ</p>
<p>8 Pm 1 SANDWICH DB HALF</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order: 2 Menu: FULL LIQUID DIAB 500</p>
<p>Ordered: 14-Dec-03 10:03am By: NFSDOCTOR,ONE</p>
<p>Reviewed: 14-Dec-03 10:03am By: NFSDOCTOR,ONE</p>
<p>Cancelled: 14-Dec-03 10:04am By: NFSDOCTOR,ONE</p>
<p>Type: Dietary Diet Associated: No</p>
<p>10 Am 1 MILKSHAKE VANILLA</p>
<p>2 Pm 1 MILKSHAKE CHOC</p>
<p>8 Pm 1 SUSTACAL P.O.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order: 3 Menu: ANTI-DUMPING</p>
<p>Ordered: 14-Dec-03 10:04am By: NFSDOCTOR,ONE</p>
<p>Reviewed: 14-Dec-03 1:56pm By: NFSDOCTOR,ONE</p>
<p>Cancelled: 14-Dec-03 2:37pm By: DIET,DIET</p>
<p>Type: Dietary Diet Associated: No</p>
<p>10 Am 1 CEREAL II/BOWL/SPOON; 1 MILK, SKIM</p>
<p>2 Pm 1 CRAX PEANUT BUTTER; 1 JUICE, ORANGE 4OZ</p>
<p>8 Pm 1 SANDWICH DB HALF</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order: 4 Menu: ANTI-DUMPING Ordered: 2-Dec-03 2:52pm By: A NFSDOCTOR,ONE</p>
<p>Reviewed: 2-Dec-03 2:52pm By: NFSDOCTOR,ONE</p>
<p>Cancelled: 24-May-04 12:09pm By: NFSDOCTOR,ONE</p>
<p>Type: Dietary Diet Associated: No</p>
<p>10 Am 1 CEREAL II/BOWL/SPOON; 1 MILK, SKIM; 2 CRAX PEANUT</p>
<p>2 Pm 1 CRAX PEANUT BUTTER; 1 JUICE, ORANGE 4OZ</p>
<p>8 Pm 1 SANDWICH DB HALF</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>T U B E F E E D I N G S</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order # 1</p>
<p>Product: SUSTACAL, Full Str., 2000 KCAL/per Day</p>
<p>Product CC's: 2000 Water CC's: 0</p>
<p>Daily CC's: Daily KCals: 2000</p>
<p>Ordered: 15-Oct-03 11:50am By: NFSDOCTOR,ONE</p>
<p>Cancelled: 21-Nov-03 12:37pm By: NFSDOCTOR,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order # 2</p>
<p>Product: OSMOLITE HN, 1/2 Str., 100 CC/per Hour</p>
<p>Product CC's: 1200 Water CC's: 1200</p>
<p>Daily CC's: Daily KCals: 1272</p>
<p>Comment: ADMINISTER OVER 18 HOUR PER DAY THRU J-TUBE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 10%" />
<col style="width: 35%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>000-00-0001 NFS,PATIENT ONE Female Age 54 Page</p>
</blockquote>
<p>8-Mar-05 12:43pm</p></th>
<th>4</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Ordered: 14-Dec-03 2:36pm By: DIET,DIET</p>
<p>Cancelled: 19-Dec-03 12:50pm By: DIET,DIET</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Order # 3</p>
<p>Product: SUSTACAL, Full Str., 2000 KCAL/per Day</p>
<p>Product CC's: 2000 Water CC's: 0 Product: ISOCAL HCN, 1/2 Str., 1000 CC per Day</p>
<p>Product CC's: 500 Water CC's: 500</p>
<p>Product: 1 CAL/CC,LS, 3/4 Str., 100 CC Every 4 Hours X (5) hours</p>
<p>Product CC's: 75 Water CC's: 25</p>
<p>Daily CC's: Daily KCals: 3075</p>
<p>Comment: NFSPAT...</p>
<p>Ordered: 19-Dec-03 12:50am By: NFSDOCTOR,ONE</p>
<p>Cancelled: 19-Dec-03 12:52am By: NFSDOCTOR,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Order # 4</p>
<p>Product: 1 CAL/CC,LS, 3/4 Str., 100 CC Every 4 Hours X (5) hours</p>
<p>Product CC's: 75 Water CC's: 25</p>
<p>Daily CC's: Daily KCals: 3075</p>
<p>Comment: NFSPAT...</p>
<p>Ordered: 19-Dec-03 1:28pm By: NFSDOCTOR,ONE</p>
<p>Cancelled: 20-Dec-03 11:19am By: NFSDOCTOR,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D I E T E T I C</p>
</blockquote></td>
<td><blockquote>
<p>C O N S</p>
</blockquote></td>
<td><blockquote>
<p>U L T S</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Request: DIET INSTRUCTION: PATIENT OR</p>
<p>Clinician: NFSDOCTOR,ONE Ordered: 18-Sep-03 11:51am Cleared: 9-Jun-02 3:46pm</p>
</blockquote></td>
<td><blockquote>
<p>FAMILY</p>
<p>By:</p>
<p>By:</p>
</blockquote></td>
<td><blockquote>
<p>Status: Complete Type: Initial</p>
<p>NFSDOCTOR,ONE NFSDOCTOR,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Request: EVALUATE FOR DINING ROOM</p>
<p>Comment: TEST CASE Clinician: NFSDOCTOR,ONE Ordered: 30-Apr-01 8:11am Cleared: 30-Apr-01 10:06am</p>
</blockquote></td>
<td><blockquote>
<p>By:</p>
<p>By:</p>
</blockquote></td>
<td><blockquote>
<p>Status: Complete</p>
<p>Type: NFSDOCTOR,ONE NFSDOCTOR,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Request: DIET INSTRUCTION: PATIENT OR</p>
<p>Comment: TEST Clinician: DIET,DIET</p>
<p>Ordered: 30-Apr-01 9:58am Cleared:</p>
</blockquote></td>
<td><blockquote>
<p>FAMILY</p>
<p>By:</p>
<p>By:</p>
</blockquote></td>
<td><blockquote>
<p>Status: Complete</p>
<p>Type: NFSDOCTOR,ONE DIET,DIET</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Request: BULIMIA DISORDER TREATMENT</p>
<p>Clinician: NFSDOCTOR,ONE Ordered: 28-Oct-02 11:12am Cleared: 21-Apr-03 11:29am</p>
</blockquote></td>
<td><blockquote>
<p>By:</p>
<p>By:</p>
</blockquote></td>
<td><blockquote>
<p>Status: Complete Type: Initial</p>
<p>NFSDOCTOR,ONE NFSDOCTOR,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Request: BULIMIA DISORDER TREATMENT</p>
<p>Clinician: NFSDOCTOR,ONE Ordered: 28-Oct-02 11:15am Cleared: 13-Apr-03 9:11am</p>
</blockquote></td>
<td><blockquote>
<p>By:</p>
<p>By:</p>
</blockquote></td>
<td><blockquote>
<p>Status: Complete Type: Initial</p>
<p>NFSDOCTOR,ONE NFSDOCTOR,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>000-00-0001 NFS,PATIENT ONE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Female Age 54 Page</p>
<p>8-Mar-05 12:43pm</p>
</blockquote></td>
<td>5</td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 72%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>E A R L Y / L A T E T R A Y S</p>
</blockquote></th>
<th></th>
<th></th>
<th rowspan="33"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 10-Nov-03 11:00am Meal: Noon Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>11:00A</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 6-Nov-03 8:18am By: NFSDOCTOR,ONE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 11-Nov-03 11:00am Meal: Noon Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>11:00A</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 6-Nov-03 8:18am By: NFSDOCTOR,ONE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 13-Dec-03 12:50pm Meal: Noon Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>12:50P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 13-Dec-03 9:19am By: NFSDOCTOR,ONE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 14-Dec-03 12:50pm Meal: Noon Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>12:50P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 13-Dec-03 9:19am By: NFSDOCTOR,ONE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 19-Aug-01 4:30pm Meal: Evening Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>4:30P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 19-Aug-01 12:10pm By: DIET,DIET</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 25-Nov-02 5:00pm Meal: Evening Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>5:00P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 24-Nov-02 12:31pm By: NFSDOCTOR,ONE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 26-Nov-02 5:00pm Meal: Evening Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>5:00P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 24-Nov-02 12:31pm By: NFSDOCTOR,ONE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Order: 1-Mar-04 11:00am Meal: Noon Bagged: No</p>
</blockquote></th>
<th><blockquote>
<p>Time:</p>
</blockquote></th>
<th><blockquote>
<p>11:00A</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Ordered: 28-Feb-04 9:13am By: NFSDOCTOR,ONE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>S T A N D I N G O R D E R S</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Order #: 1 Meals: All Meals</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Order: 2 DOUBLE PORTIONS</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Ordered: 6-Nov-03 8:17am By: DIET,DIET</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Cancelled: 14-Dec-03 2:39pm By: DIET,DIET</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Diet Associated: No</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Order #: 2 Meals: Break</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Order: 2 ORANGE JUICE</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Ordered: 6-Nov-03 8:17am By: DIET,DIET</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Cancelled: 14-Dec-03 2:39pm By: DIET,DIET</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Diet Associated: No</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>A D D I T I O N A L O R D E R S</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Order #: 1 Status: Cancelled</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Order: Double portions of dessert</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Ordered: 11-Apr-01 1:28pm By: NFSDOCTOR,ONE</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Cleared: 30-Nov-01 2:58pm By: NFSDOCTOR,ONE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## XC Clinical Management Menu \[FHASCX\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CR</p>
</blockquote></th>
<th><blockquote>
<p>Clinical Management Report… [FHASNRR]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EC</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Nutrition Classifications [FHASC1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EP</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Nutrition Plans [FHASC9]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ET</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Encounter Types [FHASE1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LC</p>
</blockquote></td>
<td><blockquote>
<p>List Nutrition Classifications [FHASC2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LP</p>
</blockquote></td>
<td><blockquote>
<p>List Nutrition Plans [FHASC10]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LS</p>
</blockquote></td>
<td><blockquote>
<p>List Nutrition Statuses [FHASC4]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LT</p>
</blockquote></td>
<td><blockquote>
<p>List Encounter Types [FHASE2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Patient Management… (See User Manual)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XD</p>
</blockquote></td>
<td><blockquote>
<p>Display Selected Drug Classifications [FHSYP2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XL</p>
</blockquote></td>
<td><blockquote>
<p>Display Selected Lab Tests [FHSYP1]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XP</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Clinical Site Parameters [FHASC8]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Clinical Management Menu allows each facility the greatest amount of flexibility in individualizing the Clinical Nutrition and Food Service functions. There are 4 files and 5 site parameters within this program which allow for individualization. There are established guidelines for the data in the NUTRITION STATUS file \#115.4, so the data is exported with the software and cannot be edited. The data in the DIETETIC NUTRITION PLAN file \#115.5, NUTRITION CLASSIFICATION file \#115.3, and the FH SITE PARAMETERS file \#119.9 are

> entered and/or edited according to the facility's needs. These files are populated with data in order for the Nutrition Screening, Nutrition Profile, and Nutrition Assessment programs to function properly.

> The ENCOUNTER TYPES file \#115.6 allows you to record a variety of patient encounters, as well as recall and tabulate for statistical purposes. The Encounters program has two defined encounter types: Nutrition Assessment and Nutrition Status. These are pre-defined, so that activity in either of these programs is automatically tallied under Encounter Statistics. Each facility defines any number of encounter types which reflect the kind of clinical services they provide and the degree of documentation needed. This Encounters program replaces the statistical management section previously included in Consult Management.

> Before building the data in the files and completing the site parameters, closely review the sample forms and the explanations for each program.

> There is a relationship between the files in this program and other Nutrition and Food Service files.

> Note: The files NUTRITION CLASSIFICATION, NUTRITION STATUS, and

> ENCOUNTER TYPES are not dependent on data in other files.

#### Diagram of the Relationship

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 24%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#) POINTER FIELD</p>
</blockquote></th>
<th><blockquote>
<p>POINTER TYPE</p>
</blockquote></th>
<th><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p><strong>NUTRITION PERSON</strong> (#115.011) | | NUTRITION:NUTRITION P* (N )-&gt; | 115.3 <strong>NUTRITION CLASSIFICATION</strong></p>
<p><strong>NUTRITION PERSON</strong> (#115.011) | | NUTRITION:RISK CATEGO* (N )-&gt; | 115.4 <strong>NUTRITION STATUS</strong> NUTRITION STATUS:STATUS (N )-&gt; | |</p>
<p><strong>NUTRITION ENCOUNTERS</strong> (#115.7) | | ENCOUNTER TYPE ....... (N )-&gt; | 115.6 <strong>ENCOUNTER TYPES</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> The Nutrition Patient Management menu is also found in the Clinical Dietetics User menu. It has its own menu of sub-options, and is explained in the User Manual.

#### Dietetic User \[FHUSR\]

> The Dietetic User menu provides access for non-nutrition personnel to the nutrition assessment option, the energy/nutrient abbreviated analysis, the nutrition patient profile, and the ability to review diet orders.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AA</p>
</blockquote></th>
<th><blockquote>
<p>Abbreviated Analysis [FHNU5]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DA</p>
</blockquote></td>
<td><blockquote>
<p>Display Assessment [FHASMR]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Review Diet Orders [FHORD2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PP</p>
</blockquote></td>
<td><blockquote>
<p>Patient Profile [FHORD9]</p>
</blockquote></td>
</tr>
</tbody>
</table>

### CR Clinical Management Report \[FHASNRR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MA</p>
</blockquote></th>
<th><blockquote>
<p>Nutrition Admission/Discharge Monitor Report [FHMNADM]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MI</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Patient Monitor Inquiry [FHMNINQ]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MM</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Monitor Brief Report [FHMNBRPT]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MR</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Monitor Statistics Report [FHMNREP]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Status Average [FHASNR5]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NS</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Status Summary FHASNR]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NZ</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition Status Matrix [FHASNR2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SE</p>
</blockquote></td>
<td><blockquote>
<p>Encounter Statistics [FHASE4]</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### MI Nutrition Monitor Inquiry \[FHMNINQ\]

> The Nutrition Monitor Inquiry option allows you to select a patient, and an admission date for that patient. The report displays any applicable monitors, as well as the Date Entered and, if applicable, the Date Cleared.

> Admission: Select the number of the admission date to use.

> Device: Select a printer or display a device.

#### MR Nutrition Monitor Statistics Report \[FHMNREP\]

> The Nutrition Monitor Statistics Report option allows you to select an admissions date range for the report. The report displays a list of patients who had an admission in that date range, and whether or not they had any monitor(s). At the end of the report, it will also display the Total Number of Admissions, Total Number with Monitors and a Percentage of Admissions with Monitors.

> Begin Date: Enter a date prior to the current date (today’s date).

> End Date: Enter a date after the begin date.

> Device: Select a printer or display a device.

> Enter beginning date: T-365 (SEP 05, 2000)

> Enter ending date: T (SEP 05, 2001) DEVICE: HOME// (Printer name)

> SEP 05, 2001 Page: 1

> Admission Patient SSN Monitor? Discharge

> ============================================================================ SEP 18,2000 NFSPATIENT,One 0000

> SEP 18,2000 NFSPATIENT,One 0000 SEP 19,2000

> SEP 19,2000 NFSPATIENT,One 0000 MAY 21,2001

> DEC 4,2000 NFSPATIENT,One 0000 DEC 4,2000

> DEC 4,2000 NFSPATIENT,One 0000 DEC 4,2000

> DEC 4,2000 NFSPATIENT,One 0000 Yes

> FEB 1,2001 NFSPATIENT,One 0000

> MAR 22,2001 NFSPATIENT,One 0000

> MAR 22,2001 NFSPATIENT,One 0000 MAR 22,2001

> MAR 22,2001 NFSPATIENT,One 0000 Yes

> MAR 22,2001 NFSPATIENT,One 0000

> MAR 22,2001 NFSPATIENT,One 0000 MAR 22,2001

> MAR 28,2001 NFSPATIENT,One 0000

> APR 9,2001 NFSPATIENT,One 0000

> APR 9,2001 NFSPATIENT,One 0000 JUL 10,2001

> APR 9,2001 NFSPATIENT,One 0000

> APR 9,2001 NFSPATIENT,One 0000

> SEP 05, 2001 Page: 2

> Admission Patient SSN Monitor? Discharge

> ============================================================================

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>APR</th>
<th><blockquote>
<p>9,2001</p>
</blockquote></th>
<th><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></th>
<th>0000</th>
<th colspan="2" rowspan="2"></th>
</tr>
<tr class="odd">
<th>MAY</th>
<th><blockquote>
<p>7,2001</p>
</blockquote></th>
<th><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></th>
<th>0000</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAY</td>
<td><blockquote>
<p>15,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td></td>
<td><blockquote>
<p>MAY 21,2001</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAY</td>
<td><blockquote>
<p>18,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td></td>
<td><blockquote>
<p>MAY 18,2001</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAY</td>
<td><blockquote>
<p>18,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>MAY</td>
<td><blockquote>
<p>21,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td></td>
<td><blockquote>
<p>MAY 21,2001</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>JUN</td>
<td><blockquote>
<p>6,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td></td>
<td><blockquote>
<p>JUN 6,2001</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JUN</td>
<td><blockquote>
<p>13,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>JUL</td>
<td><blockquote>
<p>24,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>AUG</td>
<td><blockquote>
<p>13,2001</p>
</blockquote></td>
<td><blockquote>
<p>NFSPATIENT<strong>,</strong>One</p>
</blockquote></td>
<td>0000</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>TOTAL ADMISSIONS: 27</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### NA Nutrition Status Average \[FHASNR5\]

> The Nutrition Status Average option allows you to view calculated inpatient, nutritional status averages from a start date to the end date. The program calculates the average under each level and the percentage of the workload for each Location or each clinician. The grand total is the total of the total average for each level for the designated time period for all Locations or clinicians. The grand total percentage is the average percentage of workload for each level for all Locations or clinicians for the time period.

> Print by Clinician or Location: Select the report data to be categorized by Location (W) or Clinician (C).

> Starting Date: Date the report begins to search for inpatient status levels.

> Ending Date: Date the report ends the search for inpatient status levels.

> Device: Enter the name of the printer. This report must be queued, because it is a time consuming process.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Print by CLINICIAN or LOCATION? LOCATION// <strong>&lt;RET&gt;</strong></p>
<p>Starting Date: <strong>T-7</strong> (APR 02, 2005)</p>
<p>Ending Date: <strong>T</strong> (APR 09, 2005 QUEUE TO PRINT ON</p>
<p>DEVICE: (Printer name)</p>
<p>10-Mar-05 8:58am</p>
<p>N U T R I T I O N S T A T U S A V E R A G E</p>
<p>Page 1</p>
<p>1-Jan-05 to 31-Jan-05</p>
<p>LOCATION I % II % III % IV % UNC % TOTAL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10E</p>
</blockquote></td>
<td>1 25 1 25 1 25</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 25 4</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10WC</p>
</blockquote></td>
<td><blockquote>
<p>1 100</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10W</p>
</blockquote></td>
<td>1 50</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 50 2</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11E</p>
</blockquote></td>
<td><blockquote>
<p>1 100</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13EI</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13W</p>
</blockquote></td>
<td>3 50 2 33 1 17</td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15E</p>
</blockquote></td>
<td><blockquote>
<p>1 50 1 50</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15WR</p>
</blockquote></td>
<td>1 50 1 50</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 29%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>221</p>
</blockquote></th>
<th></th>
<th>14</th>
<th>78</th>
<th>3</th>
<th>17</th>
<th>1</th>
<th>6</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2A</p>
</blockquote></td>
<td></td>
<td>4</td>
<td>33</td>
<td>6</td>
<td>50</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 17</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2D</p>
</blockquote></td>
<td></td>
<td>2</td>
<td>29</td>
<td>5</td>
<td>71</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2N</p>
<p>6</p>
</blockquote></td>
<td></td>
<td>5</td>
<td>83</td>
<td>1</td>
<td>17</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3E</p>
</blockquote></td>
<td></td>
<td>2</td>
<td>67</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 33</p>
</blockquote></td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3N</p>
</blockquote></td>
<td></td>
<td>1</td>
<td>50</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 50</p>
</blockquote></td>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3S</p>
</blockquote></td>
<td></td>
<td>3</td>
<td>100</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4E</p>
</blockquote></td>
<td></td>
<td>1</td>
<td>33</td>
<td>1</td>
<td>33</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 33</p>
</blockquote></td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4N</p>
</blockquote></td>
<td></td>
<td>1</td>
<td>100</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4S</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>100</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5E</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 100</p>
</blockquote></td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6W</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>50</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 50</p>
</blockquote></td>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7E</p>
</blockquote></td>
<td></td>
<td>1</td>
<td>33</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>33</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 33</p>
</blockquote></td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7W</p>
</blockquote></td>
<td></td>
<td>2</td>
<td>100</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9EI</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9E</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>100</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BRS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>100</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ECC 1-B</p>
</blockquote></td>
<td></td>
<td>2</td>
<td>67</td>
<td>1</td>
<td>33</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ECC 1-C</p>
</blockquote></td>
<td></td>
<td>5</td>
<td>56</td>
<td>1</td>
<td>11</td>
<td>3</td>
<td>33</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ECC 2-B</p>
</blockquote></td>
<td></td>
<td>4</td>
<td>80</td>
<td>1</td>
<td>20</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ECC 2-C</p>
</blockquote></td>
<td></td>
<td>5</td>
<td>45</td>
<td>4</td>
<td>36</td>
<td>2</td>
<td>18</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td rowspan="2">58</td>
<td rowspan="2"><blockquote>
<p>52</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>33</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>29</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>10</p>
</blockquote></td>
<td rowspan="2">9</td>
<td rowspan="2"><blockquote>
<p>1</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Grand Total</p>
<p>10 9 112</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### NS Nutrition Status Summary \[FHASNR\]

> The Nutrition Status Summary option displays or prints the current Nutrition Status Levels (I-IV) of inpatients by Location or Clinician. This report indicates at the time it prints how many patients on a Location are screened and entered the Nutrition Status into the computer. The summary also includes a column for "Unclassified" patients. This report assists Clinical Managers in determining daily workload requirements based on patients' Nutrition status levels. Location is the automatic default for printing. Select C (Clinician) for a report of the number of patients with their statuses entered by each clinician.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>Print by CLINICIAN or LOCATION? LOCATION// <strong>&lt;RET&gt;</strong></p>
<p>DEVICE: HOME// (Printer name)</p>
<p>N U T R I T I O N S T A T U S S U M M A R Y Page 1</p>
</blockquote>
<p>11-Apr-05 8:55am</p>
<blockquote>
<p>LOCATION I II III IV UNC</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10E</p>
</blockquote></td>
<td>5</td>
<td>6</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12E</p>
<p>......</p>
</blockquote></td>
<td>4</td>
<td>2</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### NZ Nutrition Status Matrix \[FHASNR2\]

> The Nutrition Status Matrix option displays the Nutrition Status levels I to IV of inpatients. Data is viewed as either Status Change Over a period of time where specific start and end dates are entered, or Status Change from Admission. These reports show the change of the status from the time of admission or during specific dates.

> Status Change: Select a timeframe for viewing nutrition status changes: Status Change Over a period of time or Status Change from Admission.

- If you choose 2, the following prompts display:
- Select LOCATION (or ALL): all
- Enter \# of Days from Admission: 100
- Response must be no greater than 99.
- Enter \# of Days from Admission: 99
- If you choose 1, the prompts in the example display.

> Location: Enter a Location name or ALL.

> Starting Date: Date the report begins to search for inpatient status levels. Ending Date: Date the report ends the search for inpatient status levels. Device: Select a printer or display device.

#### Example

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>STATUS</p>
</blockquote></th>
<th></th>
<th>TOTAL</th>
<th>I</th>
<th></th>
<th>II</th>
<th><blockquote>
<p>III</p>
</blockquote></th>
<th></th>
<th>IV</th>
<th>UNC</th>
<th>SAME</th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>UNC</p>
<p>3243</p>
</blockquote></th>
<th>NFSPATIENT<strong>,</strong>One</th>
<th>31</th>
<th>1</th>
<th><blockquote>
<p>*</p>
</blockquote></th>
<th rowspan="6"></th>
<th>1</th>
<th></th>
<th rowspan="6"></th>
<th>29</th>
<th>29</th>
</tr>
<tr class="header">
<th><blockquote>
<p>5432</p>
</blockquote></th>
<th>NFSPATIENT<strong>,</strong>One</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>*</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>9812</p>
</blockquote></th>
<th>NFSPATIENT<strong>,</strong>One</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>*</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>6512</p>
</blockquote></th>
<th>NFSPATIENT<strong>,</strong>One</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>*</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>0304</p>
</blockquote></th>
<th>NFSPATIENT<strong>,</strong>One</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>*</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>8410</p>
</blockquote></th>
<th>NFSPATIENT<strong>,</strong>One</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>*</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Total</p>
</blockquote></th>
<th></th>
<th>31</th>
<th>1</th>
<th></th>
<th>0</th>
<th>1</th>
<th></th>
<th>0</th>
<th>29</th>
<th>29</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### SE Encounter Statistics \[FHASE4\]

> The Encounter Statistics option provides a tool to enter and record specific encounters and aggregate data for statistical reports. The option tallies automatic encounters from computer entries, such as Nutritional status and Nutritional assessments, as well as the site-determined encounters entered.

> This report can be generated for any specified time period in three ways:

1.  An Encounter Statistics Summary which includes:
    - Number of each Encounter type
    - Number of inpatients, collaterals, and workload units (minutes) involved in each Encounter type
    - Number of outpatients, collaterals, and workload units involved in each encounter type
    - Number of other persons and workload units involved in each encounter type
    - Total persons and units for each encounter type
    - Grand total of encounters, patients, and units
2.  Breakdown by Clinicians, which includes all encounter data as listed in Summary for each clinician. Accept the default, because a “Yes” response provides a breakdown of encounters for all clinicians by clinician.
3.  List Individual Patient Encounters which includes:
    - All encounter data as listed in Summary
    - Breakdown of data by clinician
    - List of each patient entered for each encounter by date
    - Event comments for each encounter
    - List totals for each encounter type

> List Individual Patient Encounters displays only if the response to Breakdown by Clinicians is YES. NO is the default for List Individual Patient Encounters. If you enter YES, the report lists each clinician name and the types of encounters with the individual patient identification under each.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 1%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="16"><blockquote>
<p>Pat Col Units Pat Col Units</p>
<p>Persn Units Persn Units</p>
<p>Screening</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>STATUS/SCREENING 13 345.0</p>
<p>Subtotal</p>
</blockquote></td>
<td></td>
<td colspan="5"><blockquote>
<p>13</p>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
<p>10</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>265.4</p>
<p>265.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>3</p>
<p>3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>79.6</p>
<p>79.6</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>0 0.0 13</p>
</blockquote></td>
<td><blockquote>
<p>345.0</p>
</blockquote></td>
<td colspan="5"></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="16"><blockquote>
<p>Assessment</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>NUTRITIONAL ASSESSMENT</p>
</blockquote></td>
<td colspan="5">51</td>
<td>40</td>
<td>8</td>
<td>1835.3</td>
<td colspan="2"><blockquote>
<p>11</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>504.7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><p>59 2340.0</p>
<blockquote>
<p>Subtotal 59 2340.0</p>
</blockquote></td>
<td colspan="5">51</td>
<td>40</td>
<td>8</td>
<td>1835.3</td>
<td colspan="2"><blockquote>
<p>11</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>504.7</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Pat. Education INSTRUCTION - DIABETIC</p>
</blockquote></td>
<td colspan="5">4</td>
<td>4</td>
<td></td>
<td>125.0</td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>4 125.0</p>
</blockquote></td>
<td></td>
<td colspan="5"></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>INSTRUCTION -</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIABETIC</p>
</blockquote></td>
<td>(F)</td>
<td colspan="4">1</td>
<td>2</td>
<td colspan="2"><blockquote>
<p>100.0</p>
</blockquote></td>
<td colspan="2">1</td>
<td colspan="2"><blockquote>
<p>50.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>3 150.0</p>
<p>INSTRUCTION -</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>NORMAL NUTR</p>
</blockquote></td>
<td colspan="4">1</td>
<td>1</td>
<td colspan="6"><blockquote>
<p>35.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>1 35.0</p>
<p>INSERVICE INSTRUCTION</p>
<p>102 612.5 408 2450.0</p>
<p>CONTINUING EDUC PROG ATTENDED 8 60.0</p>
</blockquote></td>
<td colspan="4"><p>3</p>
<p>1</p></td>
<td><p>204</p>
<p>8</p></td>
<td colspan="2"><blockquote>
<p>1225.0</p>
<p>7.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>102</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>612.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Subtotal 102 612.5</p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>421 2670.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>9</td>
<td>219</td>
<td></td>
<td>1402.5</td>
<td></td>
<td><blockquote>
<p>103</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>662.5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>T O T A L 102 612.5</p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>496 3205.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>74</td>
<td>269</td>
<td>8</td>
<td>5493.2</td>
<td></td>
<td><blockquote>
<p>116</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1246.8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D I E</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td colspan="3">E T I C E N C</td>
<td>O</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>T E R</p>
</blockquote></td>
<td>S T</td>
<td>A T I</td>
<td>S T I C</td>
<td><blockquote>
<p>S</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>Page 2</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="9"><blockquote>
<p>Assessment</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0.0</td>
<td colspan="2"><blockquote>
<p>NUTRITIONAL ASSESSMENT 2 03.0</p>
<p>26-Jan-02 3333 CASE, TEST</p>
<p>26-Jan-02 5642 OUTPATIENT, NEW</p>
<p>Subtotal</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>03.0</p>
<p>03.0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
</tr>
<tr class="even">
<td>0.0</td>
<td colspan="2"><blockquote>
<p>2 03.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="9"><blockquote>
<p>DIETITIAN, LOCATION</p>
<p>Screening</p>
</blockquote></td>
</tr>
<tr class="even">
<td>0.0</td>
<td><blockquote>
<p>STATUS/SCREENING</p>
<p>2 60.0</p>
<p>24-Jan-02 3240</p>
</blockquote></td>
<td><blockquote>
<p>INPATIENT, NEW</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>60.0</td>
<td colspan="3">0.0</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>24-Jan-02 5685</p>
<p>Subtotal</p>
</blockquote></td>
<td><blockquote>
<p>INPATIENT, OLD</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>60.0</td>
<td colspan="3">0.0</td>
</tr>
<tr class="even">
<td>0.0</td>
<td><blockquote>
<p>2 60.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="9"><blockquote>
<p>Assessment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>0.0</td>
<td colspan="2"><blockquote>
<p>NUTRITIONAL ASSESSMENT 1 45.0</p>
<p>24-Jan-02 2121 NFSPATIENT<strong>,</strong>One.</p>
<p>Subtotal</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>45.0</p>
<p>45.0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
</tr>
<tr class="odd">
<td>0.0</td>
<td colspan="2"><blockquote>
<p>1 45.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>TOTAL ENCOUNTERS</p>
</blockquote></td>
<td colspan="2">11</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>403.0</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>122.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

### EC Enter/Edit Nutrition Classifications \[FHASC1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Nutrition Classification option allows you to add and modify nutrition classifications. The NUTRITION CLASSIFICATION file \#115.3 stores universally recognized Nutritional diagnoses, such as DRG Codes, ICD-9-CM Codes, Marasmus, Kwashiorkor, etc.

> These classifications are used during the nutritional assessment of a patient. A nutritional classification emphasizes the importance of Nutrition and Food Service as part of the problem list.

> The name field is free text, 3-60 characters in length. There is no limit on the number of classifications entered in the file; however, only one classification is selected for each assessment.

### EP Enter/Edit Nutrition Plans \[FHASC9\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Nutrition Plans option allows Clinical Managers to individualize, as well as standardize within their facility the Nutrition Plans section on the Screening form. Specific needs of the facility are listed, as well as providing a standardized form of recognizable planning factors.

> The plan name is 3-60 characters. There is a limit of six plans, which you can include to keep the length of the form to one page. The lines before each plan, which provide a check off capability, are automatically included in the program. Enter the information in upper and lower case letters for readability and enter it in the order in which you want the plans to print on the screening form.

> Example

### ET Enter/Edit Encounter Types \[FHASE1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Encounter Types option allows you to create and/or edit data in the ENCOUNTER TYPES file \#115.6. The establishment of data in this file is necessary to use the Encounters Program. This file allows for the collection of information on the numerous patient care activities performed by the clinical dietitians and clinical diet technicians. It also allows for data collection on activities performed by administrative dietitians. Each station can decide if they require encounters be collected from the administrative dietitians. Due to the innumerable clinical services provided, these clinical products are grouped into seven major Clinical Categories. In a cooperative effort the Clinical Staffing Study Group, Regional Coordinators, VACO, and the Clinical Ad Hoc Group developed these categories.

> The Clinical Categories are management tools that utilize the encounters as a data source. Individual encounters point to a specific Clinical Category. Data are generated for the seven established Clinical Categories.

> Definitions for the seven Clinical Categories are provided to serve as guidelines in creating the ENCOUNTER TYPES file. The definitions do not imply that you have to create encounters for all of the specific categories mentioned. If you do not create any encounters for a specific Category, data is not tallied for that Clinical Category. You can establish very broad or very specific encounters. The establishment of this file is totally dependent upon the facility's needs and desires. If you create encounters for administrative Nutrition staff, do not point the encounters to a specific Clinical Category. It is not necessary to have a clinician account for an entire period of duty.

#### Clinical Category Definitions

> Screening is a process of gathering pre-established data pertaining to the patient, in order to determine the patient's nutrition status or if the patient has obvious nutritional problems, including the documentation of such. For patients who are found not at risk, further assessment may not be required. Those patients are re-screened within the timeframe by the facility's policy and procedure. Patients, who are nutritionally compromised, may require further assessment.

> Assessment is a process that includes further review, investigation and evaluation of the patient's data including documentation of such. There are varying degrees of assessments performed. The results of an initial assessment determine whether further or more complex evaluation and/or intervention is needed.

> Patient Education is a category that includes the provision of Nutrition and Food Service education to patients and/or their caregivers as individuals or in a group setting. Instructions are further categorized by disease entities, individual instructions and group classes, utilizing the individual encounters.

#### Examples

- Instruction: Diabetic
- Class: Diabetic

> Community is a category that includes activities, such as gathering information, travel time, screening, assessment, patient education, Nutritional intervention, documentation, etc., that are associated with locations outside of the medical center setting. Examples include HBHC visits, community nursing home inspections, halfway house inspections, residential care home inspections, and community lectures.

> Nutrition and Food Service Intervention consists of all aspects of patient care other than screening, assessment, and patient education.

#### Examples

- Meal rounds
- Communication with the health care team
- Calorie counts
- Discharge planning
- Follow-up documentation
- Food preferences
- Diet card adjustments

> Food Service Operations is a category that includes the duties performed to assure that food service operations continue according to established policies and procedures. Activities may include menu writing/meal planning, daily taste panel, formal taste panel, product evaluation, energy nutrient analysis of medical center menus and plate waste studies.

> Administrative Duties is a category that consists of indirect Nutrition and Food Service care activities performed by the clinician.

#### Examples

- Quality assessment and improvement functions
- Goal planning
- Peer review
- Training of students, interns, food service employees
- Continuing education activities
- In-services
- Administrative reports, research, proposal writing, collection of data, publications, writing policies and procedures
- ADP coordinating activities
- Special assignments, participation in health fairs
- Daily organizational activities involved in planning duties/services for the day, record keeping, checking patient census, correspondence, telephone calls, compiling forms, filing
- Developing education materials
- Staff meetings

> Note: The examples are possible types of encounters that might point to a specific Clinical Category. You do not need to establish encounters for all of the examples. You can establish broad or specific encounters based upon the need of the facility.

> The Enter/Edit Encounter Types option allows you to collect information on numerous patient care activities performed by the clinical dietitians and clinical diet technicians.

> Select Encounter Types Name: Enter the name of the encounter. The encounter name must be 3-30 characters. There is no limit to the number of encounter types you can enter. Encounters are applicable to outpatients as well as inpatients.

> To determine the types of encounters to enter, each Clinical Manager should review manually kept records, definitions of the 7 Clinical Categories, and the information reported on the Annual Nutrition Report. In addition to Nutrition Assessments and Status/Screening encounters, there are other encounters appropriate to record and track.

#### Examples

- Instruction: Diabetic (etc.)
- Calorie Counts
- Class: Wt Reduction (etc.)
- Team Meetings
- HBHC Activities
- Menu Writing
- Nursing Home Inspections
- Peer Review
- Meal Rounds
- Research Proposal Writing

> This program is used to record and track a wide variety of educational and administrative activities, such as, in-service training for food service workers, continuing education programs attended, and so on. Again, review of current records aids in determining the encounter type needs.

> Initial Time: Enter the average time, in minutes, required to conduct an activity/encounter on an initial basis. This value becomes the automatic default in the Enter/Edit Encounter (EE) option and is changed at the time of entry. Type a whole number between 0 and 999. (This information is used to complete the RCS 10-0141 or conduct time studies.)

> Follow-Up Time: Enter the average time, in minutes, required to conduct an activity/encounter on a follow-up basis. This value becomes the automatic default in the Enter/Edit Encounter option and is changed at the time of entry. Type a whole number between 0 and 999.

> Ask Event Location: Enter "YES" or "NO". A "YES" response generates a prompt to enter the event location whenever this type of encounter is entered in the DIETETIC ENCOUNTERS file (115.7). You can only be able to select locations, which exist in the facility’s HOSPITAL LOCATION file. This file includes all Locations, outpatient clinics, and other hospital-wide locations of interest.

> Category: Connect the encounter to a specific Clinical Category. You can choose one of the seven Clinical Categories.

> Individual/Group/Both: This is pertinent to educational encounters. Enter either "I" for individual patient instructions, "G" for group patient classes, or "B" for both as appropriate.

> Ask Patient Name(s): Enter "YES" or "NO". A "YES" response results in the clinician is prompted to enter each patient's name whenever this type of encounter is entered into the DIETETIC ENCOUNTERS file (115.7).

> Ask \# Collaterals: This prompt displays when a "YES" response is entered under "Ask Patient Name(s)". Enter "YES" or "NO". A "YES" response generates a prompt to enter the number (0- 9) of collaterals associated with each patient when this type of encounter is entered into the DIETETIC ENCOUNTERS file (115.7). This field allows the service to keep track of the number of collaterals seen according to Encounter type.

> Ask for Patient Comment: This prompt displays only when a "YES" response is entered under "Ask Patient Name". Enter "YES" or "NO". A "YES" response prompts you to enter a patient comment, or any other information associated with this encounter when this type of encounter is entered into the DIETETIC ENCOUNTERS file (115.7).. It is free text 3-60 characters in length. This information displays in the Patient Inquiry option.

> Inactive: The only way to remove an entry from the ENCOUNTER TYPES file is to inactivate it by a "YES" in this field. Simple deletion of the entry would cause "Undefined Errors" throughout other parts of the program. Once an entry is inactivated, a non-manager cannot use it.

### LC List Nutrition Classifications \[FHASC2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Nutrition Classifications option alphabetically lists all the entries in the NUTRITION CLASSIFICATION file \#115.3. Entries to this file are made using the Enter/Edit Nutrition Classifications (EC) option. Either enter a printer name or press \<RET\> to bring the data to the screen.

### LP List Nutrition Plans \[FHASC10\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Nutrition Plans option prints a list of the entries in the DIETETIC NUTRITION PLAN file \#115.5. Use the Enter/Edit Nutrition Plans (EP) option to make entries to this file.

<table>
<colgroup>
<col style="width: 84%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE: <strong>&lt;RET&gt;</strong> RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NUTRITION AND FOOD SERVICE PLANS APR 12,2005 PAGE 1</p>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>08:31</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Further Nutrition Assessment</p>
<p>Provide basic Nutrition care services Recommend change diet to</p>
<p>Recommend Nutrition Education</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### LS List Nutrition Statuses \[FHASC4\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Nutrition Statuses option prints all items in the NUTRITION STATUS file \#115.4. The program comes with four Nutrition Status levels, which you cannot edit. However, use this option to print the Nutrition Status list.

> Nutrition Status Levels:

- I Normal
- II Mildly Compromised
- III Moderately Compromised
- IV Severely Compromised

### LT List Encounter Types \[FHASE2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Encounter Types option prints all items in the ENCOUNTER TYPES file \#115.6. Use the Enter/Edit Encounter Types (ET) option to make entries to this file.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><blockquote>
<p>DEVICE: <strong>&lt;RET&gt;</strong> RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
<p>ENCOUNTER TYPES APR 12,2005 08:53 PAGE 1 ASK</p>
<p>INITIAL FOLLOW-UP EVENT</p>
<p>NAME TIME TIME LOCATION? CATEGORY ASK</p>
<p>ASK ASK FOR</p>
<p>PATIENT # PATIENT INDIVIDUAL/GROUP/BOTH NAME(S)? COLLATERALS COMMENT? INACTIVE?</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Class - Overeaters</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pat. Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GROUP</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES</td>
<td></td>
<td>YES</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENCOUNTER TYPE A</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Pat. Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BOTH</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES</td>
<td></td>
<td>YES</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FOOD-DRUG INSTRUCTION</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Screening</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GROUP</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>YES</td>
<td></td>
<td>YES</td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NUTRITIONAL ASSESSMENT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>45</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INDIVIDUAL</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td>YES</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STATUS/SCREENING</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td>YES</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### XD Display Selected Drug Classifications \[FHSYP2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Display Selected Drug Classifications option allows you to display or print all drug classes or codes entered under the "Select Drug Classification" site parameter. Enter a printer name or press \<RET\> to bring the display to the screen.

### XL Display Selected Lab Tests \[FHSYP1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Display Selected Lab Tests option displays all laboratory tests selected under the laboratory, test site parameter. This list includes specimen type and whether or not to print the test on the screening or assessment forms.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>DEVICE: <strong>&lt;RET&gt;</strong> RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
<p>SELECTED LABORATORY TESTS APR 12,2005 09:11 PAGE 1 PRINT PRINT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>IDENT</p>
</blockquote></td>
<td><blockquote>
<p>ON</p>
</blockquote></td>
<td><blockquote>
<p>ON</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LAB TEST</p>
</blockquote></td>
<td><blockquote>
<p>SPECIMEN</p>
</blockquote></td>
<td><blockquote>
<p>GROUP</p>
</blockquote></td>
<td><blockquote>
<p>ASSESS</p>
</blockquote></td>
<td><blockquote>
<p>SCREEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALBUMIN</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CALCIUM</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CHOLESTEROL</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GLUCOSE</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GLUCOSE, OTHER</p>
</blockquote></td>
<td><blockquote>
<p>URINE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IRON</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IRON SATURATION</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LIPIDS, TOTAL</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LIPIDS, QUALITATIVE</p>
</blockquote></td>
<td><blockquote>
<p>FECES</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LACTIC ACID</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>URINE KETONES</p>
</blockquote></td>
<td><blockquote>
<p>URINE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>zzURINE PROTEIN</p>
</blockquote></td>
<td><blockquote>
<p>URINE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VITAMIN A</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VITAMIN B-12</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VITAMIN C</p>
</blockquote></td>
<td><blockquote>
<p>PLASMA</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VITAMIN E</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ESTROGEN</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INSULIN</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PHENOBARBITAL</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PROTHROMBIN TIME</p>
</blockquote></td>
<td><blockquote>
<p>PLASMA</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SICKLE CELLS</p>
</blockquote></td>
<td><blockquote>
<p>BLOOD</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TESTOSTERONE</p>
</blockquote></td>
<td><blockquote>
<p>SERUM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>THROMBIN TIME</p>
</blockquote></td>
<td><blockquote>
<p>PLASMA</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WBC</p>
</blockquote></td>
<td><blockquote>
<p>BLOOD</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

### XP Enter/Edit Clinical Site Parameters \[FHASC8\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Clinical Site Parameters option allows each facility to individualize the output on the Nutrition and Food Service Screening form and Nutrition Assessment form by defining the following site parameters. These parameters are changed whenever local policy changes. The number of laboratory tests selected should be limited if screening or assessment forms are to print on one page.

> Assessment Default Units: In all reports generated, units of measurement for patient data display in the English or Metric equivalents. Enter data in English or Metric format and the program converts it to the selected default unit. Enter "E" for results in English measurements, "M" for results in Metric equivalent measurements.

> Optional Screening Line: This field allows each facility to add one line to the Nutrition Screening form. It prints as the last line under the "S: " (Subjective) section. This is a free text entry. Use indentations or capitalization as needed. Enter one question or item to display on the screening form, which is not already included in the program.

#### Examples

> Print Profile After Screening?: This parameter controls the printing of the Nutrition Profile. Answer "YES" to print a Nutrition Profile following the Screening form. Answer "NO" if you do not want it printed. Enter an "A" (for Ask User) for a prompt that asks whether or not to print the profile.

> \# Of Days To Obtain Lab Data: Enter the number of days (1-500) to go back looking for laboratory results. The larger the number of days, the slower the system prints. (For acute care the number of days should be as low as possible). If multiple types of care exist, 03 days is a commonly selected search timeframe. The number selected applies to both screening and assessment. Only the most current laboratory value displays.

> Select Lab Test: Select the laboratory tests to display on the assessment and screening forms. The name of the laboratory test must be one of those available in the local VistA Laboratory package. After entering the name, you must identify the specimen type (serum, plasma, or urine) for each test. Some facilities identify tests by one word and require you to enter the specimen type. Other facilities use distinctive names for each type of test; others identify tests as a routine or stat, or specific to an area or machine.

> If the facility does not have distinctive names for tests, you may not be able to print both serum and urine results.

#### Example

> The lab has a test called urea. You can select urea once and indicate serum. The program does not allow you to enter urea again and select urine. Thus, you cannot be get both serum and urine values.

> Many facilities use distinctive names, i.e., BUN and UNN. You can get both results on the forms because the names are distinctive.

> If the facility has multiple named tests, i.e., Albumin-Stat, Albumin-Routine, Albumin- Outpatient, you need to select all possible tests and assign them the same "Ident Group" number. This tells the program to check all the Albumin tests for the selected time period and print only the most current result. This grouping prevents missing results, which are ordered by a different process.

> Next, you must indicate if the laboratory test value is printed on the screening form, the assessment form or both. All will print on the Nutrition Profile.

> Note: If you want the screening form to print on only one sheet, select no more than 12 laboratory tests.

> Normal ranges display on the screening and assessment forms and High (H), Low (L) and Critical (\*) values are indicated. The date the laboratory test was performed displays. An item prints only if there is a result within the number of days specified. Only the most current value displays. When you select tests that measure the same item, but use different processes, group them by the same "Ident Group" number.

> Select Drug Classifications: You can select the drug classifications the facility wants to use in the screening process. By selecting drug type classifications rather than specific drugs, a greater variety of medications are screened. The actual drug name (generic or brand) displays on the Nutrition Profile. Strength and dosage may display depending on character space availability. If a patient is on a combination of anti-hypertensives, each drug is listed. IV solutions are not included in this program.

> This site parameter uses drugs from Pharmacy's DRUG CLASSIFICATION file. For inpatients, medications displays only if the Pharmacy Unit Dose program is in use. For outpatients, medications are retrieved from the Pharmacy Outpatient program.

> In this site parameter, enter only the drug classification code. The following are samples of Drug Classifications and codes, which you could include in the screening process. Double question marks (??) display the Drug Classification codes available at the facility; however, descriptive names are not listed. For clarification of codes, refer to "VA Medication Classification System", available from the Pharmacy Service.

#### Sample Drug Classification Codes

> AD100 Alcohol Deterrents s

> nts

> n Agents

> Oxidase Inhibitors lar Medications sives

> Agents

> ents

> l Agents ids

> se Regulation Agents

> The assessment default units are used for determining the units for inputs when units are not specified and for determining which units are used for output on the assessment and screening forms. Select either English or metric.

> ASSESSMENT DEFAULT UNITS: METRIC// \<RET\>

> The Screening form makes provision for adding a site-selectable line to the form as the last line under the S: (or subjective) section. If you make an entry, consider the indenting and column usage of the existing lines in determining which line to enter. Press \<RET\> to bypass the extra line.

> OPTIONAL SCREENING LINE: Ethnic/Religious Food Pref: Replace \<RET\>

> You can print a Nutrition Profile following each Screening form. Answer YES if you wish the profile printed, NO if you do not. Answer A (for Ask user) for a prompt asking whether or not to print a profile.

> PRINT PROFILE AFTER SCREENING?: ASK USER// \<RET\>

> In selecting which laboratory results to display, the program allows for the selection of the number of days in the past for which to search data. Selecting 30 as a value and the most recent lab test results obtained in the last 30 days displays.

> \# OF DAYS TO OBTAIN LAB DATA: 180// \<RET\>

> Select only those laboratory tests in which the clinical staff is typically interested. A prompt as to whether or not the results are printed on the Assessment report and the Screening form.

> Select only those drug classifications in which the clinical staff is typically interested. The actual drug name displays for prescribed drugs. The drug classifications you select, control which drugs display.

> The clinical parameters allow for the identification of drug classes that may cause potential food/drug interactions.[<sup>1</sup>](#_bookmark119) You specify the drug classification and respond to a series of prompts. Create Alert allows you to create an alert for a potential food/drug interaction..

> Note: Press \<RET\> at this prompt, to go back to the menu.

> PRINT ON ASSESSMENT:

> You can print the expanded Drug Classification information on the Nutrition Assessment form.

> PRINT ON SCREENING/PROFILE:

> You can print the expanded Drug Classification information on the Nutrition Screening form.

> PRINT ORDER:

> You can choose the print order of the Drug information on the Nutrition Screening report.

> <sup>1</sup> Patch FH\*5.5\*8 September 2007 Expanded the Drug Classification field in the Clinical Site Parameters option.

> CREATE ALERT:

> You can set up an alert to a potential food/drug interaction using the expanded Drug Classification. It alerts the dietician to a food/drug with a potential food/drug interaction. If set to YES, an alert is created for a patient taking medication with this type of drug. You can also select drug classes for which to send an alert for education about potential food/drug interaction.

> Examples

### XD Diet Order Management \[FHORDX\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DE</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Diets [FHORD6]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DL</p>
</blockquote></td>
<td><blockquote>
<p>List Diets [FHORD7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Isolation/Precautions [FHOR1]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IL</p>
</blockquote></td>
<td><blockquote>
<p>List Isolation/Precaution Types [FHORI2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Tubefeeding Products [FHORTF1]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TL</p>
</blockquote></td>
<td><blockquote>
<p>List Tubefeeding Products FHORTF2]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Diet Order Management data controls the Diet Order Entry activity. All diets, tubefeedings, and isolation precautions particular to a facility are added through this menu. Data is entered with a variety of synonyms and/or alternate names or designations, in order to facilitate data entry.

> Before Diet Order Entry (refer to Diet Orders (DO) in the User Manual) is implemented, files must be built for the individual medical center. The Diet Order Management menu helps you do that.

#### Managing Diet Orders

> The advantage of a facility building its own DIETS file is that the diets can be defined as the facility wishes, such as deciding which diets are comparable (e.g., NAS = 4 gm Na Diet). Be aware that some location personnel may make their own incorrect interpretations of diet and/or tubefeeding orders. Therefore, it is important that the clinical staff continue to check orders received in Nutrition and Food Service against physicians' orders in the medical records.

#### Diagram of the Relationship

> Diet Orders \[FHORDM\]

> Diet Orders allows access to all Nutrition order options normally given to Location personnel and includes the ability to order diets, consults, early/late trays, NPOs, tubefeedings, and enter additional orders. Supplemental feedings and standing orders are not included as normal Location ordering functions. Suggested users of this menu are Location Clerks.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OA</p>
</blockquote></th>
<th><blockquote>
<p>Enter Additional Order [FHORO1]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OC</p>
</blockquote></td>
<td><blockquote>
<p>Order Consult [FHORC1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OD</p>
</blockquote></td>
<td><blockquote>
<p>Order Diet [FHORD1]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OE</p>
</blockquote></td>
<td><blockquote>
<p>Order Early/Late Tray [FHOREL2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ON</p>
</blockquote></td>
<td><blockquote>
<p>NPO/Hold Tray [FHORD3]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OT</p>
</blockquote></td>
<td><blockquote>
<p>Order Tubefeeding [FHORTF3]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PA</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Patient Reaction Data [GMRA PATIENT A/AR EDIT]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PH</p>
</blockquote></td>
<td><blockquote>
<p>Review Diet Orders [FHORD2]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PI</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Cancel Isolation/Precautions [FHORD4]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PP</p>
</blockquote></td>
<td><blockquote>
<p>Patient Profile [FHORD9]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XE</p>
</blockquote></td>
<td><blockquote>
<p>Cancel Early/Late Tray [FHOREL3]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XN</p>
</blockquote></td>
<td><blockquote>
<p>Cancel NPO/Withhold Order [FHORD12]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XT</p>
</blockquote></td>
<td><blockquote>
<p>Cancel Tubefeeding Order [FHORTF4]</p>
</blockquote></td>
</tr>
</tbody>
</table>

- Modify the Nutrition and Food Service User Manual for Location personnel and have one available on each Location. Include information on only those options available to Location personnel. It should emphasize examples specific to the facility.
- The modified User Manual for Nutrition and Food Service should include the additional options available in the Clinical Dietetics \[FHDIET\] menu.
- When developing policies for using the Diet Order program (Diet Order (DO) menu), include the following in planning:
- Define responsibilities and include a schedule to print lists and reports.
- Describe how each report is processed. This may be written as a Nutrition and Food Service Policy or included in the User Manual, and modified for Location or food service personnel.
- Describe the back-up system used in the event of computer failure. Which lists and reports are run and kept on file for reference? Can the current manual system serve as the back-up system? Who is responsible for updating the computer on information sent during down time? It would probably be best for Nutrition and Food Service to make the entries. Remember that the diet cards themselves are the most current source of information.
- Because of the change in the diet office procedures, job breakdowns needs revision.
- The implementation of the Diet Order Program affects the entire way in which information is communicated to the diet office. Because of this, careful planning is mandatory to ensure a smooth transition into the system.
- Coordination of training with MAS and Nursing is critical to ensure that all users understand and can use the program. Although it is time consuming, it may be an advantage for the Applications Coordinator to train Location personnel. Nutrition and Food Service may be able to present the program in a more understandable way.

> Note: Many employees have no prior experience with the computer.

- Consider hardware and furniture. With the elimination of kardexes, how will the information that was previously stored there be handled?
- Keep all affected services well informed of the changes and schedule. Include ADP, MAS, Nursing, and Nutrition and Food Service.
- In conclusion, this portion of the software will affect Nutrition and Food Service in many ways. In general, the Nutrition and Food Service VistA program will bring positive changes. It is important to remember that old problems may be resolved with this program but new ones may display. Remind Nutrition and Food Service employees that the program will not solve some perpetual problems. This includes such things as Locations not sending orders in a timely manner, or not sending them at all. These types of problems cannot be blamed on the new system.
- The diet office is greatly affected with operations streamlined and duplicate work diminished. Kardexes and small pieces of paper are replaced by computer lists. With information centralized in the computer, all interested users have access to the same information. With the decrease in paperwork and time spent transferring information onto kardexes and other cards, there displays to be a great reduction in work. It is important for diet office personnel to recognize that their tasks will change with the automated system.
- Diet office personnel must use their knowledge of diets to follow up on unusual orders rather than accepting all diets as they are entered. They should be able to identify routine errors and take action to correct them. Diet office personnel will receive numerous calls from Location personnel asking for help or saying they cannot, or do not, have time to make the entries. It would be beneficial for diet office personnel to offer assistance, but not actually make all the entries unless clearly necessary.

#### DE Enter/Edit Diets \[FHORD6\]

> The Enter/Edit Diets option allows you to enter and edit diets in the DIETS file \#111. There are several different pieces of information to establish for each diet. Four of the fields are required. In addition, Production Diets must be pre-established in the PRODUCTION DIET file \#116.2. To edit that file use the Enter/Edit Production Diets (PE) option in Production Management (XP) menu.

> Diets Name: Enter a single-modification diet name, such as 1 Gram Sodium or Low Fat. The program routine provides for combining any five single-modification names into a combination diet. Therefore, do not include multiple-modification names, such as Low Fat, 1 Gram Sodium, initially. Consider such combinations for entry after a test period, if they contribute to the efficiency of the program. Diet names, as stated in the facility diet manual, are usually the preferred terminology. Non-standard, but commonly used diet names are entered in the Alternate Name field. Names must be 3-30 characters in length. Diets having multiple calorie or mineral levels are listed as separate names.

#### Examples

- DIABETIC 1000
- 1500 KCAL DIABETIC
- 1G SODIUM
- MECHANICAL
- FULL LIQUID

> Test diets are also listed. Do not include NPO or Regular. These are handled differently by the program and are already present in the file. It is recommended that diets (e.g., 1500 KCAL Diabetic) having standard feedings have similar names in both the DIETS file and SUPPLEMENTAL FEEDING MENU file.

> In developing a list of diet names, it is important to know that the diets entered are the ones displayed when help is requested using "??". Enter a list of diets into the Diets Name field that reflect all common ordering practices at the facility. In addition, commonly used expressions and abbreviations are included, because Location clerks encounter and use them.

> Synonym: A Synonym is a short data entry form to save time. This field is not a required entry. Use common abbreviations and shortened forms of the longer name. Selection of the synonym automatically links with the correct diet name. The synonym cannot exceed 12 characters in length.

#### Example

> DIA1000, PRO20, CL, 1000NA

> Ask Expiration Date?: This field determines if the program asks for an expiration date when specified diets are ordered. It is particularly useful for test diets and the Clear Liquid diet, when ordered as a test diet. A "YES" in this field for any diet causes the program to ask for an

> expiration date. A date is not required in order for the program to proceed. The clerk may not know the duration of the test diet, but the opportunity is available for an expiration date to be entered, if known. A "NO" or a null (\<RET\>) in the field means you are not asked for an expiration date. For diets having expiration dates, the program automatically cancels the time- limited diets and reinstates the previous diet order.

> If no expiration date is entered, the test diet remains in effect until another diet is ordered. Time limitations on test diets are established in policy and clerks are taught to enter the data in training sessions.

> The program does not distinguish between a permanent Clear Liquid diet, a three-day Clear Liquid, or a one-meal Clear Liquid and does not keep track of this information. Location staff must know the difference and enter appropriate expiration dates and times.

> Diet Precedence: Diet Precedence is a priority numbering system. Assign each diet a number, which aids in categorizing the diets. This field has several very important functions:

> It prevents the ordering of contradictory diets, such as a 2400 Calorie, High Calorie Diet (i.e., diets assigned the same precedence cannot be ordered for the same patient).

> It distinguishes between primary diet modifications and minor diet modifications for food production purposes, separate from clinical significance. It determines the label print order.

> All of these functions are accomplished with a priority numbering system. Numbers of 20 or less indicate primary diet modifications. Numbers greater than 20 indicate minor modifications.

> Examples of primary modifications carrying numbers less than 20 might be regular, texture and consistency alterations, sodium-alterations, calorie-alterations, fat-alterations and fiber- alterations.

> The regular diet carries the number 20 and is already present in the file. Do not enter it into the file. Other diet precedence numbers are assigned by each facility.

#### Example

> Assign number 1 to all consistency/texture modifications (i.e., Clear Liquid, Full Liquid, Puree, Mechanical). By assigning the same precedence number to each, it becomes impossible to order a Clear Liquid-Pureed Diet. The program permits only one diet of a single precedence number. Also, by assigning number 1 to texture/consistency, we ensure that such a modification displays *first* on the diet card label used in tray assembly.

> Number 2 is assigned to all sodium alterations, number 3 to all calorie alterations (high, low and diabetic) and number 4 to all protein alterations (high or low).

> 1000 Calorie Diabetic, High Protein, 1 Gram Sodium, Mechanical Diet

> The user-entered order is reconfigured because of the precedence numbers, to display on the diet card label as:

> Mechanical, 1 Gram Sodium, 1000 Calorie Diabetic, High Protein

> The food service worker is first presented with the information most significant for tray assembly (i.e., type of food) followed by other modifications.

> Minor modifications carry numbers greater than 20, with like diets carrying the same number. Examples of minor modifications include fluid alterations, low cholesterol and test diets. Each minor modification eventually is associated with a Production Diet representing the type of food generally comprising that diet.

> Production Diet: The Production Diet is a required entry. Enter production diets first in the PRODUCTION DIET file \#116.2 using the Enter/Edit Production Diets (PE) option. Refer to Production Management.

> A production diet represents the basic type of food prepared for a diet modification. For example, the basic type of food served on a No-Added-Salt diet might be regular food. The basic food served on a Calorie-Controlled, Low Sodium diet might be low sodium food. Name a production diet for every diet name in the DIETS file. The production diet with the lowest tally number is reflected in the Actual Diet Census (DC). Associate every diet name with a production diet.

> Bulletin Clinician: The term Bulletin refers to a message sent to the dietitian through MailMan. An internal mechanism automatically triggers initiation of the message. This field determines whether a specific diet order sends an electronic message through the hospital MailMan system to the responsible dietitian assigned to the Location. Some diets may require early dietitian intervention in the food service process. Diets triggering such messages may require particular changes on a diet card, notification of calculations are done or to initiate special product preparation. The use of the medical center electronic mail system reduces the time lag between order and dietitian response for these types of occurrences.

> A "YES" in the field sends a message to the dietitian assigned to the Location. Location assignment of dietitians is accomplished through the Consult Management (XM) menu. A "NO" or null (\<RET\>) sends no message.

> Abbreviated Label:[<sup>1</sup>](#_bookmark122) This is a required entry. Write the abbreviation exactly as you want the diet pattern name to print on outputs, such as reports and labels, and so that the label is readily recognized by everyone. You automatically update diet pattern names when a diet is modified. Diet pattern names are built by using the abbreviated label field of each diet in the pattern. If the abbreviated label is changed, it automatically updates all diet pattern names that contain the modified diet.

> <sup>1</sup> Patch FH\*5.5\*5 May 2007 This option provides functionality to automatically update Diet Pattern names when a diet is modified. Diet Pattern names are built by using the Abbreviated Label field of each diet in the pattern. If the Abbreviated Label is changed, it will now automatically update all Diet Pattern names that contain the modified diet.

> Alternate Name: Caregivers frequently order diets in a variety of non-standard formats, all meaning essentially the same thing. This field provides the ability to accommodate alternate, nonstandard names for any, or all, of the standard diet names listed in the Diets Name field.

> Although alternate names are not displayed at a request for help, their selection automatically links with the correct diet name.

#### Examples

> Standard Diet Names Alternate Names

> 3-4 Gram Sodium No added Salt NAS

> Low Tyramine MAO

> Mechanical Dental Soft

> You can delete an alternate name.

> Inactive: The only way to remove an entry from this file is to inactivate it by entering a "Y" in this field. Simple deletion of the entry causes Undefined Errors throughout other parts of the program. Once an entry is inactivated, a dietician cannot select it. To reactivate requires VA FileMan access or intervention by the Site Manager.

> Text for Abbreviated Label:[<sup>1</sup>](#_bookmark123) The text explains why the Abbreviated Label for a diet changed. The diet pattern containing the diet is updated to reflect the change.

> <sup>1</sup> Patch FH\*5.5\*5 May 2007 Added text explaining why the Abbreviated Label for a diet changed.

#### DL List Diets \[FHORD7\]

> The List Diets option allows you to list all diets and any associated data contained in the DIETS file \#111.

> The list requires a 132-column printer.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 2%" />
<col style="width: 16%" />
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DEVICE: (Printer name)</p>
<p>DIETS LIST</p>
<p>MAR 8,2005 13:31 PAGE 1</p>
<p>NAME</p>
<p>MAIL INACT ALTERNATE NAME</p>
</blockquote></th>
<th><blockquote>
<p>SYNONYM</p>
</blockquote></th>
<th><blockquote>
<p>DIET PREC</p>
</blockquote></th>
<th><blockquote>
<p>ABBREV LABEL</p>
</blockquote></th>
<th><p>ASK</p>
<p>PROD DIET EXP</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="5"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>100 GM PROTEIN</p>
</blockquote></td>
<td><blockquote>
<p>100 GM PRO</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>100gm PRO</p>
</blockquote></td>
<td><blockquote>
<p>LOW PROTEIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>1000 CALORIE ADA</p>
</blockquote></td>
<td><blockquote>
<p>DB1000 ADA</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1000 CAL ADA</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>1000 CALORIE REDUCTION</p>
</blockquote></td>
<td>1000 CAL RED</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1000 CAL RED</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>1000 CC FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>1000 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>1000cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>1100 CALORIE ADA</p>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>DB1100 ADA</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1100 CAL ADA</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1100 CALORIE REDUCTION</p>
</blockquote></td>
<td>1100 CAL RED</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1100 CAL RED</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1100 CC FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>1100 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>1100cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>120 CC FLUID RESTRICTION-TRAY</p>
</blockquote></td>
<td><blockquote>
<p>120 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>120cc FR/TR</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1200 CALORIE ADA</p>
</blockquote></td>
<td><blockquote>
<p>DB1200 ADA</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1200 CAL ADA</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1200 CALORIE REDUCTION</p>
</blockquote></td>
<td>1200 CAL RED</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1200 CAL RED</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1200 CC FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>1200 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>1200cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1300 CALORIE ADA</p>
</blockquote></td>
<td><blockquote>
<p>DB1300 ADA</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1300 CAL ADA</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1300 CALORIE REDUCTION</p>
</blockquote></td>
<td>1300 CAL RED</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1300 CAL RED</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1300 CC FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>1300 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>1300cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>1400 CALORIE ADA</p>
</blockquote></td>
<td><blockquote>
<p>DB1400 ADA</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>1400 CAL ADA</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>3000 CALORIE ADA</p>
</blockquote></td>
<td><blockquote>
<p>DB3000 ADA</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>3000 CAL ADA</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>360 CC FLUID RESTRICTION-TRAY</p>
</blockquote></td>
<td><blockquote>
<p>360 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td>360cc FR/TR</td>
<td>DIALYSIS/LOW NO</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>500 CC FLUID RESTRICTION</p>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>500 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>500cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>500 MG SODIUM</p>
</blockquote></td>
<td>500 MG SOD</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>500mg SODIUM</td>
<td>87-130/CHOL</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>600 CC FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>600 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>600cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><span id="_bookmark122" class="anchor"></span>700 CC FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>700 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>700cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>800 CALORIE ADA</p>
</blockquote></td>
<td>DB 800 ADA</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>800 CAL ADA</td>
<td>87-130/HF</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 6%" />
<col style="width: 16%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>800</p>
</blockquote></th>
<th><blockquote>
<p>CALORIE REDUCTION</p>
</blockquote></th>
<th><blockquote>
<p>800 CAL RED</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>800 CAL RED</p>
</blockquote></th>
<th><blockquote>
<p>87-130/HF</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>800</p>
</blockquote></td>
<td><blockquote>
<p>CC FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>800 CC FR</p>
</blockquote></td>
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>800cc FLUID</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS/LOW NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>030</p>
</blockquote></td>
<td><blockquote>
<p>CALORIE ADA</p>
</blockquote></td>
<td><blockquote>
<p>DB 030 ADA</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>030 CAL ADA</p>
</blockquote></td>
<td><blockquote>
<p>87-130/HF NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_bookmark123" class="anchor"></span>

#### IE Enter/Edit Isolation/Precautions \[FHORI1\]

> The Enter/Edit Isolation/Precautions option allows you to enter the isolation/precaution types into the file. The ISOLATION/PRECAUTION TYPE file establishes a relationship between the standard term on the location, how the patient tray is delivered, and who delivers it. The ISOLATION/PRECAUTION TYPE file \#119.4 supports a location clerk mechanism for ordering isolation while still providing relevant information to the food service. Location clerks are generally familiar with the terms used by the infection control and nursing personnel.

> However, they often do not know what those terms mean to food service.

> This information displays on the Diet Activity Report/Labels (DA) and the diet card label as a two-letter code. The first letter is "P" for paper or "C" for china. The second letter is "F" for food service worker or "N" for nurse. A message also displays on List Early/Late Trays (EL).

> Isolation/Precaution Type Name: This field refers to the type of isolation or precaution requested.

> Paper or China: This is a required field and designates when paper service or china service is used with the isolation/precaution type.

> Delivered by Nurse or FSW: This is a required field that designates when the tray is delivered by nursing or food service personnel.

#### IL List Isolation/Precaution Types \[FHORI2\]

> The List Isolation/Precaution Types option lists all of the current entries in the ISOLATION/PRECAUTION TYPE file \#119.4 along with the associated data elements.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DEVICE: <strong>&lt;RET&gt;</strong> RIGHT MARGIN: 80//</p>
<p>ISOLATION/PRECAUTION TYPES</p>
<p>PAPER OR</p>
<p>NAME CHINA</p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;RET&gt;</strong></p>
<p>MAR DELIVERED BY NURSE</p>
<p>OR FSW</p>
</blockquote></th>
<th><blockquote>
<p>8,2005</p>
<p>INACTIVE</p>
</blockquote></th>
<th><blockquote>
<p>13:34</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AFB ISOLATION</p>
</blockquote></td>
<td>CHINA</td>
<td><blockquote>
<p>NURSE</p>
</blockquote></td>
<td colspan="3"></td>
<td rowspan="10"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BLOOD/BODY FLUID PRECAUTIONS</p>
</blockquote></td>
<td>CHINA</td>
<td><blockquote>
<p>NURSE</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONTACT</p>
</blockquote></td>
<td>CHINA</td>
<td><blockquote>
<p>FSW</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DRAINAGE/SECRETION PRECAUTIONS</p>
</blockquote></td>
<td>CHINA</td>
<td><blockquote>
<p>FSW</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENTERIC PRECAUTIONS</p>
</blockquote></td>
<td>PAPER</td>
<td><blockquote>
<p>NURSE</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PROTECTIVE PAPER</p>
</blockquote></td>
<td>PAPER</td>
<td><blockquote>
<p>NURSE</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RESPIRATORY</p>
</blockquote></td>
<td>CHINA</td>
<td><blockquote>
<p>NURSE</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>STAY OUT</p>
</blockquote></td>
<td>PAPER</td>
<td><blockquote>
<p>NURSE</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STOP SIGN</p>
</blockquote></td>
<td>CHINA</td>
<td><blockquote>
<p>FSW</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>STRICT</p>
</blockquote></td>
<td>PAPER</td>
<td><blockquote>
<p>NURSE</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
</tbody>
</table>

#### TE Enter/Edit Tubefeeding Products \[FHORTF1\]

> The Enter/Edit Tubefeeding Products option allows you to enter and edit data in the TUBEFEEDING file. The TUBEFEEDING file (#118.2) contains product names or generic designations, reflecting physician-ordering practices at each facility. It includes information on dispensing unit, KCAL/CC, and cost.

> Name: Generic identities, such as High Calorie, High Nitrogen tubefeeding are entered, as can product names such as Sustacal or Ensure Plus. If you use generic names in the Name field, they also display on printouts.

> Dispensing Unit: Dispensing unit is the most common handling unit of each product in full strength form. Prepackaged items have dispensing units such as can, bottle, bag or quart. You can consider this unit, the unit delivered to the Location. This is required field.

> Amount/Unit:[<sup>1</sup>](#_bookmark129) This field contains the number of cubic centimeters or grams of product per dispensing unit. You can enter values less than 10. For powdered products, the cubic centimeters or grams per unit must be those of one package of a full strength, reconstituted feeding.

> Powdered products are handled as full strength fluids throughout the tubefeeding routines. This is a required field.

> KCAL/CC: This field designates the calories per CC such as 1/CC or 1.5/CC. If a powdered formula is used, it is the kcals per cc of reconstituted product. This is a required field.

> Synonym: This field is for any other common name by which a product is ordered. Synonyms are accepted, but do not display for help and are not printed on outputs. Only the original tubefeeding Name field entry displays on outputs.

> Corresponding Recipe: This field associates the product with a recipe in the RECIPE file \#114. A recipe is created for a product in order for costs to be calculated, and displays on the List Tubefeedings Products (TL) report. If no recipe is created for the product, a "0.00" displays in the cost column of the report.

> Inactive?: The only way to remove an entry from this file is to inactivate it by entering a "Y" in this field.

> <sup>1</sup> Patch FH\*5.5\*5 - May 2007 – Modified the AMT/UNIT field of the TUBEFEEDING file (#118.2) to accept values that are less than 10.

#### TL List Tubefeeding Products \[FHORTF2\]

> The List Tubefeeding Products option lists all tubefeeding products in the TUBEFEEDING file \#118.2 along with all associated data elements.

> The list requires a 132-column printer.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 4%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DEVICE: (Printer name)</p>
<p>TUBEFEEDING PRODUCTS</p>
<p>MAR 8,2005 13:32 PAGE</p>
<p>NAME RECIPE</p>
<p>SYNONYM</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>DISPENSING UNIT</p>
</blockquote></th>
<th>AMT/UNIT</th>
<th>KCAL/CC</th>
<th><blockquote>
<p>COST</p>
</blockquote></th>
<th><blockquote>
<p>INACTIVE?</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="7"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>1 CAL/CC,LS</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CAN</p>
</blockquote></td>
<td>240C</td>
<td>1.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>AMIN-AID</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PKG</p>
</blockquote></td>
<td>10G</td>
<td>2.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>RENAL FAILURE SOLUT</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CITROTEIN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>POWDER</p>
</blockquote></td>
<td>240C</td>
<td>0.60</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>LOW RESIDUE/LOW FAT</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CRITICARE HN</p>
<p>HIGH NITROGEN ELEME</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>BOTTLE</p>
</blockquote></td>
<td>240C</td>
<td>1.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CRITICARE HN</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>GOOD STUFF</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CAN</p>
</blockquote></td>
<td>237C</td>
<td>1.06</td>
<td colspan="2"><blockquote>
<p>0.01</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>BAKED SWEET POTATOES</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>HEPATIC-AID</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PKG</p>
</blockquote></td>
<td>340C</td>
<td>2.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HEPATIC FAILURE SOL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>ISOCAL HCN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CAN</p>
</blockquote></td>
<td>240C</td>
<td>2.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HIGH KCAL/PRO TUBE</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>MAGNACAL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>MICROLIPID</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>BOTTLE</p>
</blockquote></td>
<td>120C</td>
<td>4.50</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>OSMOLITE</p>
<p>STANDARD TUBEFEEDIN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CAN</p>
</blockquote></td>
<td>240C</td>
<td>1.06</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>ISOCAL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>OSMOLITE HN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CAN</p>
</blockquote></td>
<td>240C</td>
<td>1.06</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>POLYCOSE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>BOTTLE</p>
</blockquote></td>
<td>120C</td>
<td>2.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PRECISION HN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PKG</p>
</blockquote></td>
<td>255C</td>
<td>1.05</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HIGH NITROGEN INTAC</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PRECISION LR</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PKG</p>
</blockquote></td>
<td>285C</td>
<td>1.11</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>INTACT PROTEIN</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PROMOD</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SCOOP</p>
</blockquote></td>
<td>5G</td>
<td>4.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PRO-MOD</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PROPAC</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PKG</p>
</blockquote></td>
<td>20C</td>
<td>3.05</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PULMOCARE PULM</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CAN</p>
</blockquote></td>
<td>240C</td>
<td>1.50</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>CARE 1</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>SUSTACAL</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CAN</p>
</blockquote></td>
<td>240C</td>
<td>1.00</td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>FRESH PEA ENSURE</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><span id="_bookmark129" class="anchor"></span>TRAVASORB LIQUID</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>STANDARD ORAL SUPPL</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SUSTACAL HC SUSTACAL HC</p>
</blockquote></th>
<th><blockquote>
<p>CAN</p>
</blockquote></th>
<th>240C</th>
<th>1.50</th>
<th><blockquote>
<p>0.00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENSURE PLUS</p>
<p>TEST FLUID RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>BOTTLES</p>
</blockquote></td>
<td>100C</td>
<td>270.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TEST CC</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FLUID CC TF</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FLUID REST</p>
<p>TUBEFEEDING HYPERTONIC1.5CALCC</p>
</blockquote></td>
<td><blockquote>
<p>TABLESPOON</p>
</blockquote></td>
<td>237C</td>
<td>1.52</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VIVONEX ELEMENTAL</p>
</blockquote></td>
<td><blockquote>
<p>PKG</p>
</blockquote></td>
<td>300C</td>
<td>1.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

## XE Energy/Nutrient Management \[FHNUX\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ML</p>
</blockquote></th>
<th><blockquote>
<p>List User Menus [FHNUX]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Nutrients [FHNU6]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NG</p>
</blockquote></td>
<td><blockquote>
<p>Enter Nutrients (Common Units) [FHNU12]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NL</p>
</blockquote></td>
<td><blockquote>
<p>List Nutrient File [FHNU7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RE</p>
</blockquote></td>
<td><blockquote>
<p>Recipe Analysis [FHNU11]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>List DRI Values [FHNU9]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Energy/Nutrient Management allows you to enter or edit the food items and nutrients included. User menus are listed and recipes not part of the Recipe Management program are analyzed and stored for future reference. The data referenced in this program are USDA, latest release \#10, selected food items from Bowes and Church, 16th Edition and additional data from research on the fiber content of some foods.

### Managing Energy and Nutrients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Because the data in USDA Handbooks 8 and 456 is considered the most reliable of its kind, this data, shipped with the software and stored in the FOOD NUTRIENTS file \#112, is "locked" to prevent users from changing nutrient values or deleting food items.

> Note: Although there are locks on this file, users with edit access to VA FileMan can edit it.

> Even though updates to this data are rarely needed, the program does allow users assigned the menu Nutrition and Food Service Management \[FHMGR} or Clinical Management \[FHMGRC\] to add food items to the file according to changes in the USDA data.

> Note: User added data and calculations are only as valid and reliable as the information entered.

> In order for users to judge reliability, a "Source of Data" field allows entry of an 80-character description of the original nutrient composition information, source and date of entry. This version contains descriptive information for most added items, as well as the facility number of the entering station and the date of entry.

> Note: It is strongly recommended that Source of Data be entered for all items added to the FOOD NUTRIENTS file.

> The Quick List concept used in Order Entry is a useful technique for minimizing search time for the Location clerk, nurse, or clinician ordering a nutrient. Customize the items displaying on the Quick List by adding or deleting quick list items to reflect those items frequently used in the facility. To locate food items by more than one name, you can create alternate names or synonyms. Installation of this version of the software does not affect any modifications made to the Quick List in previous versions.

> Recipes are analyzed for nutrient content. Recipes can be easily stored in the FOOD NUTRIENTS file for future use. This option aids in the customization of the file to meet the needs of each facility.

> Note: The FOOD NUTRIENTS file does not use data from other files. However, the data is used by the USER MENU, INGREDIENT, and RECIPE files.

#### Diagram of the Relationship

- As an aid in knowing what the FOOD NUTRIENTS file contains and which items are on the Quick List, a paper list should be printed using the List Nutrients (NL) option. It also contains the common unit and the grams/common unit. The list is lengthy and takes about 45 minutes to print using a standard printer, so it should not be run during busy times. The list needs to be reprinted only if additions are made to the FOOD NUTRIENTS file. Using the Code number on the List Nutrient File (NL) list, an item can be located in Handbook 8.
- Establish a procedure and format for data entry to the Source of Data field in Enter/Edit Nutrients (NE) at the facility before entering items. Ensure that users follow the format.
- There is no protection against accidental deletion of stored menus. Some designation in the User Menu Name can be made to call attention to the desire to retain a menu in storage for a long time. For example, 30 characters allows "CYCLE 3, WK 1, DO NOT DELETE" as the name of the menu.
- Ask users to delete their stored menus when they no longer have a use for them. This reduces unnecessary use of memory in the computer.
- If printing a Nutrient Intake Analysis for a non-patient, do not forget to enter the \* RETURN, then enter the client data.
- When entering nutrient values, enter a zero only if the nutrient value is known to be zero. If there is no value, enter \<RET\> bypass the field. Do not enter zero. There is a distinct difference between zero magnesium and no known magnesium value.
- If the same recipe is stored in the FOOD NUTRIENTS file in different portion sizes, it is suggested that the portion size be included in the name of the recipe. This makes it easier to identify the correct recipe in a search. It is also suggested that a station number be included in the name.
- Analyzed recipes can be stored in the FOOD NUTRIENTS file. However, stored recipes cannot be edited. If any changes are made to the recipe itself, it can be analyzed again in the test account, so that the automatic calculations for 100-gram portions are done. The values

> under Enter/Edit Nutrients (NE) in the test account are used as a reference to update the values in the live area for the revised recipe. Because recipes cannot be edited, it is possible to store more than one recipe with the same name. It can be confusing which is why using the above method may prevent this.

#### References

- Nutrient Data Base for Standard Reference, USDA, Release 6, 1987 (magnetic data).
- Recommended Dietary Allowances, National Academy of Sciences, 9th edition, revised, 1980.
- Watt, B. K.. and Merrill, A. L., Composition of Foods - Raw, Processed. U.S. Department of Agriculture Handbook 8 (rev), 1963.
- Adams, Catherine F., Nutritive Value of American Foods, In Common Units. U.S. Department of Agriculture Handbook No. 456, 1975.

### ML List User Menus \[FHNU3\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List User Menus option allows you to print a list of stored user menus. The list contains the name of the menu creator, the date each menu was created, the units (common or grams) in which the menu was entered, and the name of the menu. Use the list of User Menus to identify menus to delete or users who do not delete menus in a timely manner.

> The list requires a 132-column printer.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 59%" />
<col style="width: 12%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE: <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th><blockquote>
<p>RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
<th rowspan="24"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>USER MENUS</p>
</blockquote></th>
<th><blockquote>
<p>MAR 13,2005 15:14</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>REC</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>USER</p>
</blockquote></th>
<th><blockquote>
<p>CREATED UNITS USER MENU</p>
</blockquote></th>
<th><blockquote>
<p>MENU?</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>NOV 19,1903 COMMON SHU</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>NOV 21,1991 GRAMS EXAMPLE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>DEC 31,1991 GRAMS PPP</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>JAN 9,1902 COMMON MINE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>JUN 9,1902 COMMON TT1</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>JUN 23,1993 GRAMS TEST PREGO</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>SEP 24,1993 COMMON ZZZ</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>NOV 19,1993 COMMON LOCATION</p>
</blockquote></th>
<th><blockquote>
<p>YES</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>NOV 29,1993 COMMON PORT</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>DEC 8,1993 COMMON TEST1</p>
</blockquote></th>
<th><blockquote>
<p>YES</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>SEP 29,1994 COMMON MYMENU</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>MAR 13,2005 COMMON SHIRLEY</p>
</blockquote></th>
<th><blockquote>
<p>YES</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CASE,TEST</p>
</blockquote></th>
<th><blockquote>
<p>MAR 19,1987 GRAMS CHEESES</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>DIET,DIET</p>
</blockquote></th>
<th><blockquote>
<p>MAY 20,1993 COMMON JJJ</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>DIET,DIET</p>
</blockquote></th>
<th><blockquote>
<p>OCT 5,1993 COMMON JKL</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>FINAL,TWENTY</p>
</blockquote></th>
<th><blockquote>
<p>JAN 2,1987 COMMON Lynette</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>NOV 4,1989 COMMON XXXXX</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></th>
<th><blockquote>
<p>MAY 23,1903 GRAMS TEST D</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>VALIDITY,TEST</p>
</blockquote></th>
<th><blockquote>
<p>DEC 3,1986 COMMON TEXAS PINTOS</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ZZZ,XXX</p>
</blockquote></th>
<th><blockquote>
<p>SEP 14,1988 COMMON GILL</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### NE Enter/Edit Nutrients \[FHNU6\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Nutrient values in The Enter/Edit Nutrients option allows you to enter nutrient values in a per 100-gram portion. If the item is a recipe with all ingredients existing in the FOOD NUTRIENTS file, it is easier to use the option Recipe Analysis (RE) and save the recipe. When this is done, all values are automatically adjusted to the 100-gram portion, so that manual calculations are unnecessary. However, if the item is added as a convenience food, you may need mathematical calculations of the nutrient values before entry.

> Food Nutrients Name: This is a free text 3-60 characters. Use alphabetical characters, numbers, or commas. The name is the means by which a user searches for or selects the food or nutrient.

> For the quick data entry technique to work, the name of the food must be entered in a specific way. The generic name is followed by comma space (, ) followed by the rest of the name.

#### Example

> Right: SALAD, TOSSED Wrong: SALAD,TOSSED

> Common Unit: This field can be the portion size or the common household unit. Any free text common unit of 10 characters or less is established. For individual foods it might be ounce, cup, serving, 5-oz serv, or any other unit reflecting common practice. For recipes, the most convenient unit is "Serving". You can change this field at any time; but, if changed, you need to edit the Grams/Common Unit field.

> Grams/Common Unit: This is a very important field because it is the basis upon which other calculations are made. It should contain the gram weight value of the common unit entered in the Common Unit field. The gram weight value used for one ounce in established entries is 28.35 g.

> Original Name on Quick List: Only a "YES" or "NO" entry is accepted at this prompt, or it may be bypassed with a \<RET\>. A "YES" entry places the food nutrient name on the Quick List.

> Alternate Name: This field is 3-40 characters. A limit of one alternate name is entered for each food item named. It is a common expression, a regional name, or other name.

> The alternate name that is automatically associated with the food nutrient name, does not display on the screen, but you can select it.

> Alternate Name Quick List: Only a "YES" or "NO" entry is accepted. This feature allows you to put the food nutrient name on the Quick List after selecting the alternate name.

> % As Purchased: This refers to the percent that remains of a food item after preparation losses are accounted for. Sources of preparation losses include trimming and peeling fruits and vegetables, trimming and cooking losses with meat items, etc.

#### Examples

> Food Nutrient Name % As Purchased

> Lettuce 70%

> Beef, Inside Rounds 65%

> In these instances, about 70% of the lettuce is usable, or left after it is washed and trimmed of its outer leaves, and about 65% of the beef is left after it is trimmed and cooked.

> Type: This field refers to the state of the food item as it is used in analysis. The 3 options are "EDIBLE" (E), "RAW/RARE" (R) , and "RECIPE" (X).

> Nutrient: There are approximately 65 nutrients for which you are prompted while editing a new Food Nutrient. Enter all known values in 100-gram portions. Press \<RET\> to bypass the nutrient and enter a null value wherever a number is not entered.

> Source of Data: Every user-entered food item contains a Source of Data field at the end of the nutrient listing. This is free text of up to 80 characters. The format includes product literature identification, date of literature, date of entry (DOE) and station number (e.g., \#516). If adding a user-entered food item, it is strongly suggested that information be entered into the Source of Data field for all items entered

#### Example

> Data is "locked" and only a few fields are editable

> Use the Food Nutrient Data Entry Sheet to enter a new nutrient into the file. It helps to make sure you have all the data you need.

#### Food Nutrient Data Entry Sheet

> FOOD NUTRIENTS NAME: (3-60 char) COMMON UNITS: (0-10 char)

> GRAMS/COMMON UNIT:

> ORIGINAL NAME ON QUICK LIST?: (Y/N)

> ALTERNATE NAME: (3-40 char) ALT NAME QUICK LIST?: (Y/N)

> % AS PURCHASED: TYPE: (E, R, or X)

> PROTEIN; GM/100G: LIPIDS; GM/100G: CARBOHYDRATE; GM/100G: FOOD ENERGY; KCAL/100G: WATER; GM/100G: CALCIUM; MG/100G:

> IRON; MG/100G: MAGNESIUM; MG/100G: PHOSPHORUS; MG/100G: POTASSIUM; MG/100G:

> ALCOHOL; GM/100G: CAFFEINE; MG/100G:

> TOTAL DIETARY FIBER; GM/100G: TOTAL TOCOPHEROL; MG/100G: TRYPTOPHAN; GM/100G: THREONINE; GM/100G: ISOLEUCINE; GM/100G: LEUCINE; GM/100G:

> LYSINE; GM/100G: METHIONINE; GM/100G:

> Once an entry is completed, check your work. Using the Abbreviated Analysis (AA), request a 100-gram portion of the item. The resulting values that display are very close to the values entered. Rounding does take place.

#### Deleting Food Items from the FOOD NUTRIENT File

> Any food item you enter, you can also change or delete.

> USDA food items included in the file are "locked" and cannot be deleted or changed, even with the manager-level option. A user with VA FileMan access can alter anything in the file through VA FileMan; however, this is strongly discouraged unless there is a change to the USDA data.

> Deleting an item can cause "undefined" errors when reviewing or printing any stored User Menu. Therefore, it is important to review all User Menus before deleting a food item contained in one of them.

> Correction of an undefined error is done in two ways:

1.  Delete the User Menu containing the pointer to the deleted item.
2.  Ask the Site Manager to clear it.

#### Troubleshooting Errors

> Undefined Errors

> Undefined errors usually occur when viewing or printing a User Menu containing a food item that was deleted. If possible, delete the User Menu. If this is not possible, the Site Manager must clear the undefined error.

> Incorrect Calculations

> Incorrect calculations occur for a variety of reasons. Use the Enter/Edit Nutrients (NE) option to determine if the food item is a USDA item. If nutrients cannot be changed, it is a USDA food item.

> Report any errors found in the locked USDA data to the regional work group (SIUG) representative. A centralized source reports such information to the USDA. Veterans Administration users make no changes to USDA data.

> Look for sources of an error in other user-entered data in additional areas.

- Is the gram weight correct for the common unit?
- Are the nutrient values per 100-gram portion correct?
- Are conversions correct between the manufacturer's units and units required by the software?

> Food items entered by many facilities will be part of the file when the software is distributed to medical centers. To make changes or update, proceed through the Enter/Edit Nutrients (NE) option to the nutrient values. Do not forget to change the Source of Data field to reflect newer product information and entering station.

> You must report serious flaws in user-entered data to the regional work group (SIUG) representative, so you can share the information through the Nutrition SIUG Newsletter, *Bits and Bytes*, and the corrected computer tapes.

### NG Enter Nutrients (Common Units) \[FHNU12\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter Nutrients option allows you to enter nutrient analysis for a food in common units instead of grams. The prompt sequence is the same as the Enter/Edit Nutrients (NE) option, except that the Grams/Common Unit field is omitted.

> Example

### NL List Nutrient File \[FHNU7\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Nutrient File option prints a brief version of the entire 2800-item FOOD NUTRIENTS file, plus any food items the individual medical center added. This list contains the name of the food item, the USDA Handbook 8 code number (if appropriate), notation of whether it is on the Quick List, the common unit used, the grams per common unit and any alternate name in the file. The list is lengthy and requires about 45 minutes for printing on common printers. Food items are listed alphabetically. Once the printing starts, you stop it by typing \<Ctrl\> C or by asking the Site Manager.

> The list requires a 132-column printer.

<table style="width:100%;">
<colgroup>
<col style="width: 32%" />
<col style="width: 22%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE: (Printer name)</p>
<p>FOOD NUTRIENTS</p>
<p>10,2005 09:00 PAGE 1 NAME</p>
<p>NAME QUICK</p>
</blockquote></th>
<th>CODE</th>
<th><blockquote>
<p>QUICK</p>
</blockquote></th>
<th><blockquote>
<p>COMMON</p>
</blockquote></th>
<th><blockquote>
<p>GM/UNIT</p>
</blockquote></th>
<th><blockquote>
<p>MAR ALTERNATE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*1000 ISLE SALAD DRESSING</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>0.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*1ST: BRANFLAKES</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*1ST: CHEERIOS</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>0.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*1ST: CORNFLAKES</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>29.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*1ST: FARINA</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>88.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*1ST: HOMINY GRITS</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>88.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*1ST: OATMEAL</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>85.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*1ST: RAISIN BRAN</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>35.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*1ST: RICE KRISPIES</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>18.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*1ST: SHREDDED WHEAT</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*2% MILK</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>227.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*2ND: CORNFLAKES</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>29.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*2ND: FARINA</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>88.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*2ND: HOMINY GRITS</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>88.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*2ND: OATMEAL</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>05.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*2ND: SPECIAL K</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>18.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*ADIRONDACK SALAD</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>31.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*ALMOND COOKIE</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>41.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*AMERICAN CHEESE SANDWICH</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*AMERICAN FRIED POTATOES</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*ANGELFOOD CAKE</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>21.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*APPLE JELLY, IND</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>14.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*APPLE JUICE</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>113.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*APPLESAUCE</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>113.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*ASSORTED DIET JELLY, IND</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>30.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*AU GRATIN POTATOES</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>71.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BACON</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>45.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BACON SEASONED SPINACH</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>124.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BAKED BEANS</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>131.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BAKED CHICKEN</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>148.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BAKED CHICKEN BREAST</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>113.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BAKED FISH</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>85.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BAKED FISH FILLETS</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>114.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BAKED FISH PARISIENNE</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>46.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BAKED HAM</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>109.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BAKED HAMLOAF</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>58.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BAKED PORK CUTLET</p>
</blockquote></td>
<td colspan="3">svg.</td>
<td colspan="2"><blockquote>
<p>75.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>*BAKED POTATO</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>svg.</p>
</blockquote></th>
<th><blockquote>
<p>170.0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>*BARBECUE CHICKEN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>239.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BARBECUE CHICKEN BREAST ON BU</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>122.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BEEF BARLEY SOUP</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>870.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BEEF BARLEY SOUP, CND</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>200.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BEEF BISCUIT SQUARE W/GRAVY</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>159.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BEEF BROTH - 6 OZ</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>194.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BEEF CHOP SUEY</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>79.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BEEF CUBES</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>64.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BEEF CUBES AU JUS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>50.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BEEF RICE SOUP</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>172.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FOOD NUTRIENTS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>MAR</td>
</tr>
<tr class="even">
<td><blockquote>
<p>10,2005 09:00 PAGE 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td><blockquote>
<p>QUICK</p>
</blockquote></td>
<td><blockquote>
<p>COMMON</p>
</blockquote></td>
<td>GM/UNIT ALTERNATE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME QUICK</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>--</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BEEF STEW</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>170.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BEEF STRIPS IN SOUR CRM GRVY</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>114.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*BEEF STROGANOFF</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>113.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*BEEF TIPS</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>05.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*ZESTY MELON SALAD</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>140.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*ZUCCHINI</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>136.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*ZUCCHINI ITALIAN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>67.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*ed's gravy</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>svg.</p>
</blockquote></td>
<td><blockquote>
<p>102.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ABALONE, FRIED</p>
</blockquote></td>
<td><blockquote>
<p>15-156</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ACEROLA JUICE, RAW</p>
</blockquote></td>
<td><blockquote>
<p>9-002</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>floz.</p>
</blockquote></td>
<td><blockquote>
<p>30.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACEROLA, RAW</p>
</blockquote></td>
<td><blockquote>
<p>9-001</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>fruits</p>
</blockquote></td>
<td><blockquote>
<p>4.8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ADVANCE LIQUID 16 CAL/OZ</p>
</blockquote></td>
<td><blockquote>
<p>IF-017</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>floz.</p>
</blockquote></td>
<td><blockquote>
<p>30.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALBA 77 CHOCOLATE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>env.</p>
</blockquote></td>
<td><blockquote>
<p>21.2 FIT'N</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FROSTY, CHOCOLATE (ALBA) NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALBA HOT COCOA MIX</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>env.</p>
</blockquote></td>
<td>19.1 COCOA MIX,</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SUGAR-FREE (ALBA) NO</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALFALFA SPROUTS, RAW</p>
</blockquote></td>
<td><blockquote>
<p>11-001</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td><blockquote>
<p>33.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALLSPICE, GROUND</p>
</blockquote></td>
<td><blockquote>
<p>2-001</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>tsp.</p>
</blockquote></td>
<td><blockquote>
<p>1.9</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMOND BUTTER, W/SALT ADDED</p>
</blockquote></td>
<td><blockquote>
<p>12-605</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>tbsp.</p>
</blockquote></td>
<td><blockquote>
<p>16.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALMOND BUTTER, WO/SALT ADDED</p>
</blockquote></td>
<td><blockquote>
<p>12-105</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>tbsp.</p>
</blockquote></td>
<td><blockquote>
<p>16.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMOND PASTE</p>
</blockquote></td>
<td><blockquote>
<p>12-071</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALMONDS, DRIED</p>
</blockquote></td>
<td><blockquote>
<p>12-061</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMONDS, DRIED, BLANCHED</p>
</blockquote></td>
<td><blockquote>
<p>12-062</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALMONDS, DRY ROASTED, UNBLANCHED, W/SA</p>
</blockquote></td>
<td><blockquote>
<p>12-563</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMONDS,BLANCHED,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALMONDS,BLANCHED,SILVERED,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMONDS,CHEESE,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALMONDS,OIL ROASTED,SALTED,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMONDS,ONION GARLIC,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALMONDS,RAW,FISHER</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMONDS,SLICED,NATURAL,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALMONDS,SMOKEHOUSE,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALMONDS,WHOLE,NATURAL,BLUE DIAMOND</p>
</blockquote></td>
<td><blockquote>
<p>BC-025</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AMARANTH</p>
</blockquote></td>
<td><blockquote>
<p>20-001</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td><blockquote>
<p>196.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AMIN AID</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>ml.</p>
</blockquote></td>
<td>1.0 SUPPLEMENT</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AMIN AID PUDDING</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>servings</p>
</blockquote></td>
<td><blockquote>
<p>387.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANCHOVY, PICKLED</p>
</blockquote></td>
<td><blockquote>
<p>15-002</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>anchovies</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ANISE SEED</p>
</blockquote></td>
<td><blockquote>
<p>2-002</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>tsp.</p>
</blockquote></td>
<td><blockquote>
<p>2.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLE BROWN BETTY,CAMPBELL'S FRESH KITC</p>
</blockquote></td>
<td><blockquote>
<p>BC-004</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5-oz.</p>
</blockquote></td>
<td><blockquote>
<p>142.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APPLE BUTTER</p>
</blockquote></td>
<td><blockquote>
<p>19-294</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>tbsp.</p>
</blockquote></td>
<td><blockquote>
<p>17.6</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLE FRITTERS,FRZN,MRS. PAUL'S</p>
</blockquote></td>
<td><blockquote>
<p>BC-004</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2-fritters</p>
</blockquote></td>
<td><blockquote>
<p>113.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APPLE JUICE, CND, UNSW, W/VIT C</p>
</blockquote></td>
<td><blockquote>
<p>9-400</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>fl oz.</p>
</blockquote></td>
<td><blockquote>
<p>31.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLE JUICE, CND, UNSW, WO/VIT C</p>
</blockquote></td>
<td><blockquote>
<p>9-016</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>fl oz.</p>
</blockquote></td>
<td><blockquote>
<p>31.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APPLE JUICE, FRZ, UNSW, W/VIT C</p>
</blockquote></td>
<td><blockquote>
<p>9-411</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>fl oz.</p>
</blockquote></td>
<td><blockquote>
<p>29.9</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLE JUICE, FRZ, UNSW, WO/VIT C</p>
</blockquote></td>
<td><blockquote>
<p>9-018</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>fl oz.</p>
</blockquote></td>
<td><blockquote>
<p>29.9</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>APPLES, CND, SWEETENED</p>
</blockquote></th>
<th><blockquote>
<p>9-007</p>
</blockquote></th>
<th><blockquote>
<p>YES</p>
</blockquote></th>
<th><blockquote>
<p>cups</p>
</blockquote></th>
<th>204.0</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>APPLES, FRZ</p>
</blockquote></td>
<td><blockquote>
<p>9-014</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td>172.0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLES, RAW, PARED, BOILED</p>
</blockquote></td>
<td><blockquote>
<p>9-005</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td>172.0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APPLES, RAW, PARED, MICROWAVE</p>
</blockquote></td>
<td><blockquote>
<p>9-006</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td>170.0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLES, RAW, WO/SKIN</p>
</blockquote></td>
<td><blockquote>
<p>9-004</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>fruits</p>
</blockquote></td>
<td>128.0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APPLESAUCE, CND, SWEETENED, W/SALT</p>
</blockquote></td>
<td><blockquote>
<p>9-402</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td>256.0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLESAUCE, CND, SWEETENED, WO/SALT</p>
</blockquote></td>
<td><blockquote>
<p>9-020</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td>256.0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APPLESAUCE, CND, UNSW, W/VIT C</p>
</blockquote></td>
<td><blockquote>
<p>9-401</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td>244.0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLESAUCE, CND, UNSW, WO/VIT C</p>
</blockquote></td>
<td><blockquote>
<p>9-019</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>cups</p>
</blockquote></td>
<td>244.0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APRICOT NECTAR, CND, W/VIT C</p>
</blockquote></td>
<td><blockquote>
<p>9-403</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>fl oz.</p>
</blockquote></td>
<td><blockquote>
<p>31.4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APRICOTS, CANDIED</p>
</blockquote></td>
<td><blockquote>
<p>31-0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>oz.</p>
</blockquote></td>
<td><blockquote>
<p>28.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APRICOTS, CND, HEAVY SIRUP, W/SKIN</p>
</blockquote></td>
<td><blockquote>
<p>9-027</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>halves</p>
</blockquote></td>
<td>28.3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APRICOTS, RAW</p>
</blockquote></td>
<td><blockquote>
<p>9-021</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>fruits</p>
</blockquote></td>
<td>35.0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ARBY'S, BEEF &amp; CHEESE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ea.</p>
</blockquote></td>
<td><blockquote>
<p>168.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ARBY'S, CLUB SANDWICH</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ea.</p>
</blockquote></td>
<td><blockquote>
<p>252.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ARBY'S, HAM &amp; CHEESE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ea.</p>
</blockquote></td>
<td><blockquote>
<p>154.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ARBY'S, JUNIOR ROAST BEEF</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ea.</p>
</blockquote></td>
<td><blockquote>
<p>74.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ARBY'S, ROAST BEEF SAND</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ea.</p>
</blockquote></td>
<td><blockquote>
<p>140.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

### RE Recipe Analysis \[FHNU11\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Recipe Analysis option allows you to analyze the recipes by gram weight for all ingredients. You can also analyze recipes with the Analyze All Recipes (NA) option in Recipe Management (XR). The only basic requirement is gram weights for all ingredients. The gram is the basic unit underlying the USDA Nutrient Data Base. It is required because the variety of other possible units and the conversions necessary to use them make the computer program inefficient, even though it might be more user-friendly. The program calculates the recipe using the metric weights entered and displays the per serving analysis.

> The recipe can be stored in the FOOD NUTRIENTS file. The program automatically calculates the nutrient values per 100-gram portions as normally required by the option Enter/Edit Nutrients (NE). The recipe is recalled by name using either the Input Menu Data (MD) option or the Abbreviated Analysis (AA) option in the Energy/Nutrient Analysis (EA) menu.

> If there are changes to be made after the recipe is stored, use the Enter/Edit Nutrients (NE) option. The Site Manager can add the Recipe Analysis (RE) option to the menu for any non- manager.

> Using this option is similar to using Abbreviated Analysis (AA) with only minor additions.

> Title of Recipe: This is free text 3-60 characters in length.

> Number of Portions: This is a required field and must be a number, 1-1000. This is the number of portions the recipe yields.

> Do You Wish to Use Common Units Rather Than Grams?: This allows entry of ingredient quantities by common units without having to convert quantities to grams.

> Select Food Item: Enter a name from the FOOD NUTRIENTS file.

> Amount: Enter a number 1-99999 or a 0 to delete a Food Item. The number is the amount of the item needed in the units, which is either grams or common units.

> Final Ingredient List: Once all food items are entered, a list of Food Items displays with a line number to the left. You can edit the list at the "Do you wish to edit this list?" prompt. You can change amounts, delete items, or add items to the list, at the appropriate prompts.

> Do You Wish to Store This Recipe in the FOOD NUTRIENTS File?: Answering "YES" at this prompt stores the recipe permanently in the FOOD NUTRIENTS file. If this recipe is one that is often referred to, it should be stored. Answering "NO" or hitting \<RET\> results in the analysis not being stored, and the recipe would have to be re-entered if needed again.

#### Example

> Title of Recipe: Baked Potato

> Number of Portions: 1

> Do you wish to use common units rather than grams? YES// \<RET\>

> We will now build the ingredient list.

> Select Food Item: potato

1.  POTATO CHIPS
2.  POTATO CHIPS, WO/SALT ADDED
3.  POTATO CHIPS,BARBECUE,EAGLE THINS
4.  POTATO CHIPS,BARBECUE,PRINGLES,LIGHT
5.  POTATO CHIPS,CHEDDAR N' SOUR CREAM,PRINGLES
6.  POTATO CHIPS,DILL & SOUR CREAM,CAPE COD
7.  POTATO CHIPS,DILLS & SOUR CREAM,CAPE COD (NS)
8.  POTATO CHIPS,FRENCH ONION,RIPPLED,PRINGLES
9.  POTATO CHIPS,LIGHT PRINGLES
10. POTATO CHIPS,PLAIN,CAPE COD
11. POTATO CHIPS,PLAIN,CAPE COD,NO SALT
12. POTATO CHIPS,PLAIN,EAGLE
13. POTATO CHIPS,PLAIN,EAGLE,RIDGED
14. POTATO FLOUR
15. POTATO GRANULES, DRY FORM
16. POTATO PANCAKES, HOME-PREPARED
17. POTATO PATTIES,GOLDEN,FROZEN,ORE-LDA
18. POTATO PUFFS, FRZ, PREPARED

> Select Food Item \#, '^' to Quit,

> or 'RETURN' to continue list =\> \<RET\>

1.  POTATO SALAD
2.  POTATO SALAD,GERMAN STYLE,CND,JOAN OF ARC
3.  POTATO SALAD,HOME STYLE,CND,JOAN OF ARC
4.  POTATO SALAD,WENDY'S
5.  POTATO STICKS
6.  POTATO,BAKED W/BACON&CHEESE,WENDY'S
7.  POTATO,BAKED W/BROCCOLI & CHEESE,WENDY'S
8.  POTATO,BAKED W/BUTTER FLAVOR FROZEN,ORE-IDA
9.  POTATO,BAKED W/CHEDDAR CHEESE,FROZEN,ORE-LDA
10. POTATO,BAKED W/CHEESE TOPPING,FROZEN,PILLSBURY
11. POTATO,BAKED W/CHEESE,WENDY'S
12. POTATO,BAKED W/CHILI & CHEESE,WENDY'S
13. POTATO,BAKED W/SOUR CREAM & CHIVES,WENDY'S
14. POTATO,BAKED W/SOUR CREAM & CHIVES,FROZEN,PILLSBURY
15. POTATO,BAKED W/SOUR CREAM,FROZEN,ORE-LDA
16. POTATO,BAKED,WENDY'S
17. POTATO,CND,NEW,WHOLE,HUNT'S
18. POTATO,CRISPERS,FROZEN,ORE-LDA

> Select Food Item \#, '^' to Quit, or 'RETURN' to continue list =\> 15

> POTATO,BAKED W/SOUR CREAM,FROZEN,ORE-LDA

> Amount (potato at 142 gms) =\> 1 ... 142 grams Select Food Item: \<RET\>

> Here is the final ingredient list:

> 1 POTATO,BAKED W/SOUR CREAM,FROZEN,ORE-LDA 1 potat

> Do you wish to edit this list? NO// \<RET\>

> --- Analysis of Recipe Portion --- Baked Potato

> Calories (1) 209 K Vitamin A (0)

> Protein (1) 4.7 Gms Ascorbic Acid (1) 1.0 Mg

> Carbohydrate (1) 26.9 Gms Vitamin E (0)

> Fat (1) 8.9 Gms Riboflavin (1) 0.1 Mg

> Sodium (1) 445.0 Mg Thiamin (1) 0.1 Mg

> Potassium (1) 583.0 Mg Niacin (1) 2.4 Mg

> Calcium (1) 39.0 Mg Vitamin B6 (0)

> Phosphorus (0) Vitamin B12 (0)

> Iron (1) 1.9 Mg Vitamin K (0)

> Zinc (0) Folate (0)

> Magnesium (0) Pantothenic Ac (0)

> Manganese (0) Cholesterol (1) 0.0 Mg

> Copper (0) Linoleic Acid (0)

> Selenium (0) Linolenic Acid (0)

Monounsat. Fat (1) 4.4 Gms

Polyunsat. Fat (1) 2.3 Gms

Water (0) Saturated Fat (1) 1.8 Gms

> Ash (0) Tryptophan (0)

> Alcohol (0) Threonine (0)

> Caffeine (0) Isoleucine (0)

> Total Diet Fiber (0) Leucine (0)

> Total Tocopherol (0) Lysine (0)

> Capric Acid (0) Methionine (0)

> Lauric Acid (0) Cystine (0)

> Myristic Acid (0) Phenylalanine (0)

> Palmitic Acid (0) Tyrosine (0)

> Palmitoleic Acid (0) Valine (0)

> Stearic Acid (0) Arginine (0)

> Oleic Acid (0) Histidine (0)

> Arachidonic Acid (0) Alanine (0)

> Aspartic Acid (0)

> Glutamic Acid (0)

> Glycine (0)

> Proline (0)

> Serine (0)

> Grams/Portion: 142

> Do you wish to STORE this recipe in FOOD NUTRIENT File? y

> NAME: Baked Potato// \<RET\> COMMON UNITS: svg.// \<RET\> GRAMS/COMMON UNIT: 142// \<RET\>

> ORIGINAL NAME ON QUICK LIST?: \<RET\>

> ALTERNATE NAME: \<RET\>

> SOURCE OF DATA: \<RET\>

> Do you wish to analyze another Recipe? NO// \<RET\>

### RL List DRI Values \[FHNU9\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List DRI Values option prints the contents of the DRI VALUES file \#112.2 for reference. The list requires a 132-column printer.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><blockquote>
<p>DEVICE: (Printer name) DRI VALUES</p>
<p>10-Mar-05 7:47am Page 1</p>
<p>Protein Vitamin Vitamin Vitamin Thiamin Riboflavin Niacin Vitamin Folate Vitamin</p>
<p>Name Gm. A RE E Mg C Mg Mg Mg Mg B6 Mg Mcg B12 Mcg</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>--</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHILDREN 1-3 YR. 16.0</p>
</blockquote></td>
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>0.7</p>
</blockquote></td>
<td><blockquote>
<p>0.8</p>
</blockquote></td>
<td>9</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.0 50 0.7</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHILDREN 4-6 YR. 24.0</p>
</blockquote></td>
<td><blockquote>
<p>500</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>0.9</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.1 75 1.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHILDREN 7-10 YR. 28.0</p>
</blockquote></td>
<td><blockquote>
<p>700</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.4 100 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEMALES 11-14 YR. 46.0</p>
</blockquote></td>
<td><blockquote>
<p>800</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.4 150 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEMALES 15-18 YR. 44.0</p>
</blockquote></td>
<td><blockquote>
<p>800</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.5 180 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEMALES 19-24 YR. 46.0</p>
</blockquote></td>
<td><blockquote>
<p>800</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.6 180 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEMALES 25-50 YR. 50.0</p>
</blockquote></td>
<td><blockquote>
<p>800</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.6 180 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEMALES 51+ YR. 50.0</p>
</blockquote></td>
<td><blockquote>
<p>800</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.6 180 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INFANTS 0-1/2 YR. 13.0</p>
</blockquote></td>
<td><blockquote>
<p>375</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>0.3</p>
</blockquote></td>
<td><blockquote>
<p>0.4</p>
</blockquote></td>
<td>5</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.3 25 0.3</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INFANTS 1/2-1 YR. 14.0</p>
</blockquote></td>
<td><blockquote>
<p>375</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>0.4</p>
</blockquote></td>
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td>6</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.6 35 0.5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LACTATING 1ST. 6 MO. 65.0</p>
</blockquote></td>
<td><blockquote>
<p>1300</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>05</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>1.8</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.1 280 2.6</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LACTATING 2ND. 6 MO. 62.0</p>
</blockquote></td>
<td><blockquote>
<p>1200</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>03</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>1.7</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.1 260 2.6</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MALES 11-14 YR. 45.0</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>17</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.7 150 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MALES 15-18 YR. 59.0</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>1.8</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.0 200 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MALES 19-24 YR. 58.0</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>1.7</p>
</blockquote></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.0 200 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MALES 25-50 YR. 63.0</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>1.7</p>
</blockquote></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.0 200 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MALES 51+ YR. 63.0</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.0 200 2.0</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREGNANT FEMALES 60.0</p>
</blockquote></td>
<td><blockquote>
<p>800</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>70</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td>1.6</td>
<td>17</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.2 400 2.2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DRI VALUES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10-Mar-05 7:47am Page 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Calcium</td>
<td>Phosphorus</td>
<td>Magnesium</td>
<td>Iron</td>
<td><blockquote>
<p>Zinc</p>
</blockquote></td>
<td>Pantothenic</td>
<td>Copper</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Manganese Sodium Potassium</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Name Mg</p>
</blockquote></td>
<td>Mg</td>
<td>Mg</td>
<td>Mg</td>
<td><blockquote>
<p>Mg</p>
</blockquote></td>
<td>Acid Mg</td>
<td>Mg</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mg Mg Mg</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>--</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CHILDREN 1.25 CHILDREN</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>1-3 YR.</p>
<p>300</p>
<p>4-6 YR.</p>
</blockquote></th>
<th>1400</th>
<th><blockquote>
<p>800</p>
<p>800</p>
</blockquote></th>
<th><blockquote>
<p>800</p>
<p>800</p>
</blockquote></th>
<th><blockquote>
<p>80</p>
<p>120</p>
</blockquote></th>
<th><blockquote>
<p>10</p>
<p>10</p>
</blockquote></th>
<th><blockquote>
<p>10</p>
<p>10</p>
</blockquote></th>
<th><blockquote>
<p>3.0</p>
<p>3.5</p>
</blockquote></th>
<th><blockquote>
<p>0.85</p>
<p>1.25</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.75</p>
<p>CHILDREN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>300</p>
<p>7-10 YR.</p>
</blockquote></td>
<td>1400</td>
<td>800</td>
<td>800</td>
<td>170</td>
<td>10</td>
<td>10</td>
<td><blockquote>
<p>4.5</p>
</blockquote></td>
<td>1.50</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.50</p>
</blockquote></td>
<td>400</td>
<td></td>
<td>1600</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEMALES</p>
</blockquote></td>
<td>11-14</td>
<td><blockquote>
<p>YR.</p>
</blockquote></td>
<td></td>
<td>1200</td>
<td>1200</td>
<td>280</td>
<td>15</td>
<td>12</td>
<td><blockquote>
<p>5.5</p>
</blockquote></td>
<td>2.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.50</p>
</blockquote></td>
<td>500</td>
<td></td>
<td>2000</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEMALES</p>
</blockquote></td>
<td>15-18</td>
<td><blockquote>
<p>YR.</p>
</blockquote></td>
<td></td>
<td>1200</td>
<td>1200</td>
<td>300</td>
<td>15</td>
<td>12</td>
<td><blockquote>
<p>5.5</p>
</blockquote></td>
<td>2.25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.50</p>
</blockquote></td>
<td>500</td>
<td></td>
<td>2000</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEMALES</p>
</blockquote></td>
<td>19-24</td>
<td><blockquote>
<p>YR.</p>
</blockquote></td>
<td></td>
<td>1200</td>
<td>1200</td>
<td>280</td>
<td>15</td>
<td>12</td>
<td><blockquote>
<p>5.5</p>
</blockquote></td>
<td>2.25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.50</p>
</blockquote></td>
<td>500</td>
<td></td>
<td>2000</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEMALES</p>
</blockquote></td>
<td>25-50</td>
<td><blockquote>
<p>YR.</p>
</blockquote></td>
<td></td>
<td>800</td>
<td>800</td>
<td>280</td>
<td>15</td>
<td>12</td>
<td><blockquote>
<p>5.5</p>
</blockquote></td>
<td>2.25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.50</p>
</blockquote></td>
<td>500</td>
<td></td>
<td>2000</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEMALES 3.50</p>
</blockquote></td>
<td colspan="2"><p>51+ YR.</p>
<p>500</p></td>
<td>2000</td>
<td>800</td>
<td>800</td>
<td>280</td>
<td>10</td>
<td>12</td>
<td><blockquote>
<p>5.5</p>
</blockquote></td>
<td>2.25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>INFANTS</p>
</blockquote></td>
<td>0-1/2</td>
<td><blockquote>
<p>YR.</p>
</blockquote></td>
<td></td>
<td>400</td>
<td>300</td>
<td>40</td>
<td>6</td>
<td>5</td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td>0.50</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.45</p>
</blockquote></td>
<td>120</td>
<td></td>
<td>500</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INFANTS</p>
</blockquote></td>
<td>1/2-1</td>
<td><blockquote>
<p>YR.</p>
</blockquote></td>
<td></td>
<td>600</td>
<td>500</td>
<td>60</td>
<td>10</td>
<td>5</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
<td>0.65</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0.80</p>
</blockquote></td>
<td>200</td>
<td></td>
<td>700</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11"><blockquote>
<p>LACTATING 1ST. 6 MO. 1200 1200 355 15 19 5.5 2.25</p>
<p>3.50 500 2000</p>
<p>LACTATING 2ND. 6 MO. 1200 1200 340 15 16 5.5 2.25</p>
<p>3.50 500 2000</p>
<p>MALES 11-14 YR. 1200 1200 270 12 15 5.5 2.00</p>
<p>3.50 500 2000</p>
<p>MALES 15-18 YR. 1200 1200 400 12 15 5.5 2.25</p>
<p>3.50 500 2000</p>
<p>MALES 19-24 YR. 1200 1200 350 10 15 5.5 2.25</p>
<p>3.50 500 2000</p>
<p>MALES 25-50 YR. 800 800 350 10 15 5.5 2.25</p>
<p>3.50 500 2000</p>
<p>MALES 51+ YR. 800 800 350 10 15 5.5 2.25</p>
<p>3.50 500 2000</p>
<p>PREGNANT FEMALES 1200 1200 320 30 15 5.5</p>
<p>2.25 3.50 500 2000</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Limitations of the Files

> FOOD NUTRIENTS File: The Veterans Administration (VA) FOOD NUTRIENTS file is based on the Nutrient Data Base for Standard Reference, USDA, supplemented by items entered by Salt Lake City, Bay Pines, and Tampa VA Medical Centers. During development, the USDA data was edited for functionality within the VA. Individual items, such as eel, and groups of baby food items in the junior and toddler categories were eliminated because they are not usually eaten by VA patients. Other categories of foods were reduced for the convenience of the routine user. For example, the USDA list contains 51 margarines, identified by oil composition. Such a list is unwieldy and impractical for the routine user, so it was reduced to eight of varying, but common, oil content.

> Nutrient selection was based upon functionality and extent of available data. Fewer nutrients were reported in earlier editions of Handbook 8 than in later publications.

> Amino Acids and Fatty Acids: Much of the information is missing in the data sources and use is not routine among VA users. Of the fatty acids, linoleic and linolenic are used and reported in the output as 18:2 and 18:3, respectively. Values are also reported for mono-unsaturated, polyunsaturated, and saturated fats and cholesterol.

> Vitamins: Vitamin A is reported in retinol equivalents (REs) rather than International Units (IUs) or as beta-carotene.

> Vitamin D is not reported by USDA.

> Fiber: Fiber is expressed as total dietary fiber.

#### Macronutrients:

- KCAL - the field name is Food Energy.
- FAT - the field name is Lipids.

> RDA VALUES File: In order to provide a comparison to the Recommended Daily Allowances, the RDA VALUES file was developed using the Recommended Daily Allowances, 1980. Where possible, a single value was used. When a range of values was given, the mid-point was used as the single figure for comparison. For trace minerals and nutrients for which no RDA exists, the level defined as "estimated safe and adequate" was used. The file is alterable only by programmers. At this time, it does not make provision for a range of values.

## XM Consult Management \[FHORCX\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CE</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Consult Types [FHORC7]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CL</p>
</blockquote></td>
<td><blockquote>
<p>List Consult Types [FHORC8]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CR</p>
</blockquote></td>
<td><blockquote>
<p>Re-Assign Active Consults [FHOEC9]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CX</p>
</blockquote></td>
<td><blockquote>
<p>Consult Statistics [FHORC10]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Location Assignments [FHORC5]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WL</p>
</blockquote></td>
<td><blockquote>
<p>List Ward Assignments [FHORC6]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Consult Management allows you to edit data in the NUTRITION CONSULTS file, set the clinical staff member’s location assignments, and reassign active consults from one staff member to another.

### Managing Consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Most facilities use the Consult/Request Service Tracking package for consults from Physicians and treatment team members. The NUTRITION CONSULTS file is used internally in Nutrition and Food Service to communicate and document messages to clinical staff. For example, during tray delivery, the food service worker identifies a problem with a patient’s meal, which a dietitian needs to address, or a strange request comes to the diet communication office on the diet activity report.

> Clinical managers can use information generated by Consult Management (XM) to examine workload distribution, individual professional activity, and aggregate effort expended in specific types of activities.

> Diagram of the Relationship

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 20%" />
<col style="width: 22%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#) POINTER FIELD</p>
</blockquote></th>
<th><blockquote>
<p>POINTER TYPE</p>
</blockquote></th>
<th><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th><blockquote>
<p>FILE POINTED TO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p><strong>NUTRITION PERSON</strong> (#115.03) | | ADMIS:CONSULT:CONSULT* (N )-&gt; | 119.5 <strong>NUTRITION CONSULTS</strong></p>
<p>| USER TO BULLET* |-&gt; <strong>NEW PERSON</strong></p>
<p><strong>NUTRITION PERSON</strong> (#115.01) | | ADMISSION:LAST LABEL * (N )-&gt; | 119.6 <strong>NUTRITION LOCATION</strong> ADMISSION:NUTRITION LOCATION (N C )-&gt;| CLINICIAN |-&gt; <strong>NEW PERSON</strong> NUTRITION:NUTRITION WA* (N )-&gt; | TRAY SERVICE P* |-&gt; <strong>SERVICE POINT</strong></p>
<p>| CAFETERIA SERV* |-&gt; <strong>SERVICE POINT</strong></p>
<p>| COMMUNICATION * |-&gt; <strong>COMMUNICATION OFFICE</strong></p>
<p>| SUPP. FDG. SITE |-&gt; <strong>SUPPLEMENTAL F</strong>*</p>
<p>| DEFAULT ADMISS* |-&gt; <strong>DIETS</strong></p>
<p>| m BULK N:BULK N* |-&gt; <strong>SUPPLEMENTAL F*</strong></p>
<p>| m ROOM-B:ROOM-B* |-&gt; <strong>ROOM-BED</strong></p>
<p>| m ASSOCI:ASSOCI* |-&gt; <strong>LOCATION LOCATION</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

### CE Enter/Edit Consult Types \[FHORC7\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Consult Types option allows you to add or modify types of consults. The NUTRITION CONSULTS file \#119.5 contains all of the nutritional care activities a station tracks as a "consult." Each activity has a name, a brief name, the ability to question whether the activity is an initial or follow-up action, and a time unit for each type of activity (initial and follow-up).

> Nutrition and Food Service Consults Name: The name represents a word or phrase that enables the Location/medical personnel to easily make a request. It usually denotes activities frequently requested, such as diet instruction, Nutritional assessment, calorie count and patient visit. Although there is no limit to the number of consults that you enter in the file, practicality suggests that the number be not more than 10-12. The size of a CRT or computer screen makes user search of a longer list unwieldy. The program allows entry of additional comments or an explanation for any consult. Therefore, the description of the consult need not be detailed.

#### Examples

- Diet Instruction: Patient or Family
- Discharge Planning
- Food Preferences (Eating Problems)
- Nutrient Intake Study (Calorie Count)
- Nutritional Assessment (Consult)
- Nutritional Support Team
- Recommend Diet, Supplement or Tubefeeding
- Other

> Brief Name: This field represents a short name or abbreviation of not more than 10 characters. The brief name displays when the active consults is listed for each clinician.

> Sample brief names: "TEACH" for Diet Instruction and "NST" for Nutritional Support Team.

> Initial/Follow-up: The distinction between an initial and a follow-up consult may be significant for some categories of consults. For example, an initial diet instruction or assessment may take significantly longer than a follow-up. For some types of consults, the distinction may not be important. For example, recommending that a supplement take the same amount of time for every patient, regardless of the disease complexity.

> This field determines whether to indicate "Initial" or "Follow-up". If a "Y" (YES) is entered in this field for any consult, the program prompts with "Initial/Follow-up?:". Entering "I" results in treating the consult as an Initial, using that time unit in the statistics. An "F" treats the consult as a Follow-up, using the follow-up time unit. A "N" (NO) or a null (empty field), results in not presenting the question.

> Time Units for Initial and Follow-up Consult: TU stands for Time Units. The value of a TU is determined by each medical center. It can be a unit of time or a number representing a unit of time and degree of complexity. It may differ for each consult-type from station to station. For

> example, a TU is defined as 10 minutes. If the average initial diet instruction requires 40 minutes, the TU for an Initial Consult is 4. 40 minutes represents 4 TUs of 10 minutes each. A follow-up diet instruction may require an average of 20 minutes, or 2 TUs. Each consult-type has a field for "TU for Initial Consult" and "TU for Follow-up". For any consult-type with differing TUs for Initial and Follow-up, the "Ask Initial/Follow-up" field contains a "Y" (YES).

> The concept of time units is used as a powerful productivity tool for clinical managers and as a means of documenting professional time spent in various activities.

> User to Bulletin: A consult-type is directed to an individual team clinician or clinical specialist, such as Nutrition and Food Service Support Team or renal dietitian. The specified clinician receives a bulletin regardless of the originating Location.

> Inactive?: The only way to remove an entry from a selection, look-up list is to inactivate it by a "Y" in this field. Deletion of the entry causes "Undefined Errors" throughout other parts of the program. Once an entry is inactivated, you can no longer select it. To reactivate it requires VA FileMan access or intervention by the Site Manager.

### CL List Consult Types \[FHORC8\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Consult Types option prints a list of all entries in the NUTRITION CONSULTS file \#119.5.

> The list requires a 132-column printer.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE: (Printer name)</p>
<p>CONSULTATION TYPES</p>
<p>MAR 9,2005 15:50 PAGE 1 NAME</p>
<p>INACT BULLETIN</p>
</blockquote></th>
<th><blockquote>
<p>BRIEF NAME</p>
</blockquote></th>
<th><blockquote>
<p>ASK</p>
</blockquote></th>
<th>IN-TU</th>
<th>FU-TU</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>--</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACCESS CALORIE LEVEL-WT RED/DIAB DIETS</p>
</blockquote></td>
<td><blockquote>
<p>WT RED/DB</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>4.00</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ANOREXIA DISORDER TREATMENT</p>
</blockquote></td>
<td><blockquote>
<p>ANOREXIA</p>
</blockquote></td>
<td></td>
<td>1.00</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BULIMIA DISORDER TREATMENT</p>
</blockquote></td>
<td><blockquote>
<p>BULIMIA</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>1.50</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONSULT RENAL DIETITIAN</p>
</blockquote></td>
<td><blockquote>
<p>RENAL</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>1.00</td>
<td>1.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NFSDOCTOR<strong>,</strong>One</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DIET INSTRUCTION: PATIENT OR FAMILY</p>
</blockquote></td>
<td><blockquote>
<p>TEACH</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>1.00</td>
<td>1.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVALUATE FOR DINING ROOM</p>
</blockquote></td>
<td><blockquote>
<p>DR/EVAL</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>2.00</td>
<td>1.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FOOD PREFERENCES OR EATING PROBLEMS</p>
</blockquote></td>
<td><blockquote>
<p>FOOD PREF</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>1.00</td>
<td>1.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NFSPATIENT,ONE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NEW2</p>
</blockquote></td>
<td><blockquote>
<p>NEW</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>1.00</td>
<td>1.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DDD,DDD</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NEW3</p>
</blockquote></td>
<td><blockquote>
<p>NEW</p>
</blockquote></td>
<td></td>
<td>1.00</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NURSING HOME PLACEMENT/VNA REFERRAL</p>
</blockquote></td>
<td><blockquote>
<p>NHP?VNA</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>1.00</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NUTRIENT INTAKE STUDY (CAL COUNT)</p>
</blockquote></td>
<td><blockquote>
<p>CAL CNT</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>1.00</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUTRITIONAL ASSESSMENT OR CONSULT</p>
</blockquote></td>
<td><blockquote>
<p>CONSULT</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>5.00</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OTHER</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
</blockquote></td>
<td></td>
<td>2.00</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DDD,DDD</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RECOMMEND DIET, SUPPLEMENT OR TUBEFEEDING</p>
</blockquote></td>
<td><blockquote>
<p>RECOMMEND</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>1.00</td>
<td></td>
</tr>
</tbody>
</table>

### CR Re-Assign Active Consults \[FHORC9\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Re-Assign Active Consults option allows you to shift responsibility for all currently active consults to a new person. Consults ordered after this re-assignment go to the responsible clinician as assigned under Enter/Edit Location Assignments (WE) or Enter/Edit Consult Types (CE). It is a quick method to make temporary changes.

> To accommodate extended workload shifts or permanent changes in personnel, use the Enter/Edit Location Assignments (WE) option and change the clinician assigned to the Location in question.

> Current Clinician: This refers to the name of the Dietitian or Diet Technician, who is currently assigned the consults.

> New Clinician: This refers to the name of the Dietitian or Diet Technician, who is temporarily assigned the consults.

### CX Consult Statistics \[FHORC10\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Consult Statistics option generates a report showing workload distribution and professional activity. It is a management tool. The time period to view completed consults is designated with a choice of breakdown by clinician and a list of individual patient consults.

### WE Enter/Edit Location Assignments \[FHORC5\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Location Assignments option allows you to add or modify location assignments. To receive consults, a clinician is assigned to each Location. Each Location has one assigned clinician, either a dietitian or nutrition technician, but not both. All consults, originating on a Location, are assigned to the responsible clinician, and automatically transmitted by an electronic message. It is possible to direct certain consults, such as team consults, to a specific individual regardless of their point of origin through the Enter/Edit Consult Types (CE) option. All staff electronically assigned to a Location must also have access to VistA.

> Nutrition Location Name: This is the name of the assigned nutrition location. Location assignments are made only when there are corresponding Location entries in the NUTRITION LOCATION file \#119.6.

> Clinician: This refers to the name of the assigned Dietitian or Diet Technician to the Location. Clinicians must have access codes to VistA.

> Example

### WL List Location Assignments \[FHORC6\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Location Assignments option prints a list of each Location and its assigned clinician. Enter the name of a printer.

<table>
<colgroup>
<col style="width: 91%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE: (Printer name)</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>LOCATION ASSIGNMENTS APR 14,2005 13:01 PAGE NAME CLINICIAN</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>10E NFS,P1</p>
<p>12E NFS,P2</p>
<p>13E</p>
<p>14E</p>
<p>15E</p>
<p>1A NFS,P3</p>
<p>1B NFS,P4</p>
<p>3E NFS,P5</p>
<p>3W NFS,P6</p>
<p>4E NFS,P7</p>
<p>5E NFS,P8</p>
<p>5W NFS,P9</p>
<p>7E NFS,P10</p>
<p>8E NFS,P11</p>
<p>CCU</p>
<p>GOOD EATS LOCATION NFS,P12</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## XS Supplemental Feeding Management \[FHNOX\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BE</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Bulk Location Feedings [FHNO8]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Supplemental Feeding Menus [FHNO6]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td><blockquote>
<p>List Supplemental Feeding Menus [FHNO7]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Supplemental Feedings [FHNO4]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>List Supplemental Feedings [FHNO5]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Supplemental Feeding Management allows you to enter available supplemental feeding food items and pre-set supplemental feeding (SF) menus. The SF menus are used to standardize feedings for specific diet orders or diet patterns.

### Managing Supplemental Feeding

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once associated with a diet pattern, the SF menu automatically goes into effect during diet order entry. If the diet order changes, the SF menu automatically changes to the new menu or is deleted. Bulk Location feedings are also assigned through this program.

> There are steps necessary to build the data in the files for the Supplemental Feeding program. It also describes the option to enter, change, or delete Bulk Location Feedings (BE).

> Data in the NUTRITION LOCATION file \#119.6 and the SUPPLEMENTAL FEEDING SITE

> file \#119.74 is built using the Nutrition Facilities (DF) menu, before entering supplemental feedings.

#### Diagram of Relationships

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 1%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#) POINTER FIELD</p>
</blockquote></th>
<th><blockquote>
<p>POINTER TYPE</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p><strong>NUTRITION PERSON</strong> (#115.07) | | ADMIS:SUPPLEM:10AM FE* (N )-&gt; | 118 <strong>SUPPLEMENTAL FEEDINGS</strong> ADMIS:SUPPLEM:10AM FE* (N )-&gt; | CORRESPONDING * |-&gt; <strong>RECIPE</strong></p>
<p>ADMIS:SUPPLEM:10AM FE* (N )-&gt; | |</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>... -&gt;</p>
<p><strong>SUPPLEMENTAL FEEDING</strong> (#118.1)</p>
<p>10AM FEEDING #1 ...... (N )-&gt;</p>
</blockquote></td>
<td>|</td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td>|</td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>10AM FEEDING #2 ...... (N )-&gt;</p>
<p>10AM FEEDING #3 ...... (N )-&gt;</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
</tr>
</tbody>
</table>

- Determine who will enter supplemental feedings. Will it be dietitians, technicians, or diet office personnel? Write revised procedures if the policy will be different from the current system.
- Accomplish training of Nutrition and Food Service staff prior to implementation.
- Devise a back-up procedure and practice how it will be carried out should the computer actually go down. For example, establish a regular schedule for printing the Location list or an extra set of labels to file as back-up.
- Develop a time schedule for printing lists/reports.
- When Diet Order is not running but Supplemental Feedings is, a mechanism is needed to alert diet office personnel and food service workers that a feeding exists on patients who have been transferred or discharged. This is done by marking the diet card with an SF or by running the Diet Activity Report. It contains an SF indicator for discharged or transferred patients.
- The associated Supplemental Feeding Menu is similar to associated standing orders. The new admission receives the associated supplemental feeding menu if it exists in the pattern. Inpatients with existing supplemental feedings will not receive it. You need to cancel the existing order and reorder the diet.
- Each supplemental feeding order ordered through the Supplemental Feeding menu is considered an individual order and remains with the patient until cancelled through the Change Patient Supplemental Feeding (SF) option. On the tray ticket, an existing supplemental feeding menu is denoted by “SF” and an individual one is denoted by “SF(I)”. You can check whether a supplemental feeding is associated with a diet pattern through the Supplemental Feeding Inquiry (IN) and History of Supplemental Feeding (SH) options.
- Items for both individual and bulk feedings are included in the supplemental feeding formulary.
- Involve clinical Nutrition and Food Service staff in writing procedures and in formulary development.
- Determine the number of labels to be provided for supplemental feedings and how they will be used.
- Consider combining food items for one supplemental feeding. This may be helpful since labels are limited to three lines.

#### Example

> A sandwich may include condiments rather than listing them separately. The supplemental feeding could be "Sand/Mayo".

- In naming the supplemental feedings, remember that there are 30 characters. Extra spaces can be used for other notations (e.g., item/portion, item/condiment, item/utensil).
- Files created in the test account can be transferred into the "live" account. Check with the Site Manager.
- When changing a bulk nourishment, be aware that you can delete an existing entry following the // and enter the change.
- Diet orders and supplemental feeding orders are saved and can be retrieved in Patient Data Log (DM).

### BE Enter/Edit Bulk Location Feedings \[FHNO8\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Bulk Location Feedings option allows you to assign bulk food items to a specific Location There must be data in the SUPPLEMENTAL FEEDINGS and NUTRITION LOCATION files before you use this option to change bulk food items or their quantities. You can obtain a printout of bulk feedings using the Print Bulk Feedings/Cost Report (WP or BW) option to monitor quantities and costs for each delivery point.

> Nutrition Location Name: Enter Location name from the NUTRITION LOCATION file.

> Bulk Nourishment: Enter a Supplemental Feeding from the SUPPLEMENTAL FEEDINGS file.

> The default displays previously entered Bulk Nourishments, if any.

> Quantity: Enter a whole number, 1-99. The default displays previously entered quantities, if any.

### ME Enter/Edit Supplemental Feeding Menus \[FHNO6\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Supplemental Feeding Menus option allows you to add and modify supplemental feeding menus. The SUPPLEMENTAL FEEDING MENU file \#118.1 contains a list of diets which include standard associated feedings from the SUPPLEMENTAL FEEDINGS file \#118. The associated feedings for a diet form a supplemental feeding menu bearing the name of the diet.

#### Example

> An 1800 kcal diabetic diet may have the following standard associated feedings:

> This information is entered into the computer as follows:

> (\* Null means that nothing was entered into the computer for this time period, not even zero. A null is obtained by pressing the \<RET\> key.)

> In order to permit the ordering and frequent changing of feedings for patients on diets not normally receiving feedings (e.g., Regular), an "INDIVIDUALIZED" entry was created as part of this file. It permits a user to order feedings for any

> patient and to change those feedings at will. It is a non-removable part of this file. See the User Manual, Supplemental Feedings, for further explanation.

> Supplemental Feeding Menu Name: This entry is 3-27 characters in length. If the Supplemental Feeding is associated with a particular diet, then the Supplemental Feeding Menu should have the same name, or a name that is easily identifiable as being associated with that diet. As an example, the Supplemental Feeding Menu associated with the 1800 calorie ADA diet, could be 1800.

> Synonym: Each Supplemental Feedings Menu has a synonym associated with it to save typing time. This synonym may only be 3-10 characters in length.

#### Examples

- Diet Name Synonym
- Clear Liquid CLIQ
- 2400 Diabetic LS DIA2400LS
- Liquid Diabetic 1000 LIQ1000

> Dietary or Therapeutic: The Dietary (D) or Therapeutic (T) designation is an aid in nourishment cost analysis. This is a required field.

> Time Period: Each Supplemental Feeding Menu can contain up to four food items in each time period. Enter Supplemental Feedings from the SUPPLEMENTAL FEEDINGS file or press the

> \<RET\> key to bypass this time period.

> Quantity: These display after each time period field. Enter the desired quantity for the Supplemental Feeding item or \<RET\> to bypass the quantity field.

> Inactive: Answering "YES" at this prompt inactivates an item, rendering it unavailable for selection when entering patient food preferences. A "NO" designates that the item is available for selection. A \<RET\> keeps the existing response intact.

### ML List Supplemental Feeding Menus \[FHNO7\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Supplemental Feeding Menus option allows you to print the data in the SUPPLEMENTAL FEEDING MENU file. The output is used to monitor quantities of food items for each diet.

> The list requires a 132-column printer.

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 28%" />
<col style="width: 8%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEVICE: (Printer name) SUPPLEMENTAL FEEDING MEN</p>
<p>NAME SYNONYM</p>
<p>FEEDING 8PM FEEDING</p>
</blockquote></th>
<th><blockquote>
<p>INACT</p>
</blockquote></th>
<th><blockquote>
<p>D/T</p>
</blockquote></th>
<th><blockquote>
<p>MAR 9,2005 15:53 10AM FEEDING</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 2PM</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>--</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1000 CALORIE ADA DB1000 ADA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td><blockquote>
<p>1 BANANA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APPLESAUCE/SPOON 1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FRUIT,FRESH 1 CUSTARD/SP0</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>1 CEREAL I/BOWL/SPOON</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SANDWICH DB II</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1000 CALORIE ADA SODIUM DB 1000 LS</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td><blockquote>
<p>2 MILK,WHOLE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SANDWICH,LS I 1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>1 SHERBET/SPOON</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CUSTARD/SPOON 1 JUICE OF TH</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1100 CALORIE ADA DB1100 ADA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1100 CALORIE ADA SODIUM DB 1100 LS</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1200 CALORIE ADA DB1200 ADA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1400 CALORIE ADA DB1400 ADA</p>
<p>1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 CRAX, GRAHAM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1400 CALORIE ADA SODIUM DB 1400 LS</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 CRAX, GRAHAM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1500 CALORIE ADA DB1500 ADA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIET</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 MILK, SKIM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 CRAX, GRAHAM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

### SE Enter/Edit Supplemental Feedings \[FHNO4\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Supplemental Feedings option allows you to add and modify the standard acceptable food items provided as nourishments in the facility. The data in the SUPPLEMENTAL FEEDINGS file \#118 forms the foundation of the Supplemental Feedings Program. Supplemental feedings must be established first and any changes to it may alter the operation of the entire program.

> Use the List Supplemental Feedings (SL) option to obtain a printout of Supplemental Feedings.

> Supplemental Feedings Name: The complete name of each food item is 3-20 characters in length. There is no limit to the number of food items you can enter.

#### Examples

- MILK, WHOLE
- MILK, SKIM
- JUICE OF DAY
- PUNCH - 1/2 GAL

> Space on the label is limited. You can include standard portion units or container sizes in the 20- character name, or are defined by policy and "understood" by food preparation and service personnel.

#### Example

> The sample list contains "COT.CH/SPOON, EXCH". "COT.CH" is the abbreviation for "cottage cheese". "SPOON" is the accompanying utensil. "EXCH" is the portion unit; however, the size of the portion unit (1/2 c) is defined in policy, not on the label.

#### Example

> "Punch - 1/2 gal" may be a bulk Location nourishment.

> In order to handle the non-standard requests needed for patient care, a "\*\* SPECIAL ORDER

> \*\*" entry was created. It is an unalterable, non-removable part of the file.

> Certain items may be difficult to enter if other items containing the same first word already exist in the list. For example, if "sugar sub" is already on the list, it may be difficult to enter the shorter word, "sugar". If possible, this problem

> should be avoided by entering sugar first, then entering sugar sub. Another solution is to "force" the entry of sugar by enclosing it in quotes ("sugar").

> Synonym: This is an optional entry to assign a similar name when Supplemental Feedings are entered for patients. This is free text 3-30 characters in length.

> Label?: The default answer is "YES". Answer "NO", if you do not want a label. This is a

> required field and indicates whether a label prints for the supplemental feeding. The label

> information includes the patient name and last four digits of the Social Security Number, room number, the supplemental feeding, and the date and time. Label sizes are specified using the Modify Site Parameters (SP) option in the Nutrition Facilities (DF) program.

> Vehicle for Meds?: Answering "YES" at this prompt means the item is totaled and costed as a vehicle for medication. "NO" means it is totaled and costed as therapeutic. A \<RET\> keeps the existing response in place.

> Bulk Only?: Answering "YES" means the supplemental feeding can be selected only as a bulk nourishment and not be ordered for an individual patient. Entering "NO" means it may be ordered for an individual patient or for bulk delivery to a location. Press \<RET\> to keep the existing response in place.

> Corresponding Recipe: This field associates the supplemental feeding to the appropriate production recipe for costing purposes.

> Inactive: This field allows you to remove an item from the list by making it inactive. Answering "YES" inactivates the item. A "NO" indicates that the item is active, and therefore, available for selection. A \<RET\> keeps the existing response in place.

### SL List Supplemental Feedings \[FHNO5\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Supplemental Feedings option prints all the data entered in the SUPPLEMENTAL FEEDINGS file \#118 using the Enter/Edit Supplemental Feedings (SE) option. Unit costs and dates of last cost change are listed. File a printed copy, so output can compare cost changes from one date to another.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 31%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DEVICE: (Printer name)</p>
<p>SUPPLEMENTAL FEEDINGS MAR 10,2005 BULK</p>
<p>NAME LABEL ONLY</p>
<p>SYNONYM</p>
</blockquote></th>
<th colspan="2"><p>08:01 PAGE 1 MED</p>
<p>VEH INACT COST</p>
<blockquote>
<p>RECIPE</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p> SPECIAL ORDER </p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>0.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8PM-GR CRAX(30 EA)</p>
</blockquote></td>
<td>YES YES</td>
<td>NO</td>
<td colspan="2"><blockquote>
<p>1.50</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>GRAHAM CRAC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ERS BULK (30 PKG)</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>BULK GRAH CRAX</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8PM-MILK,IND(30EA)</p>
</blockquote></td>
<td>YES YES</td>
<td>NO</td>
<td colspan="2"><blockquote>
<p>3.87</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BULK 2% MIL</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BULK IND MILK</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BREAD, RYE, 1 SLICE</p>
</blockquote></td>
<td>NO NO</td>
<td>NO</td>
<td colspan="2"><blockquote>
<p>0.02</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>RYE BREAD -</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>RYE BREAD, ONE SLICE</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BREAD,RYE</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BREAD,WHITE,1 SLICE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
<td colspan="2"><blockquote>
<p>0.07</p>
<p>WHITE BREAD</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>WHITE BREAD - 1 SLICE</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>WHT BREAD - 1 SLICE</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>WHT BRD - 1 SL</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CEREAL,40% BRAN/SP</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
<td colspan="2"><blockquote>
<p>0.17</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>1ST: BRANFL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>40% BRANFLAKES/SP</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BRANFLAKES/SP</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>40% BRAN CEREAL/SP</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BRAN CEREAL/SP</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CEREAL,LS/BWL/SP</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
<td colspan="2"><blockquote>
<p>0.15</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>LS CORNFLA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LS CEREAL/SP</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>LOW NA CEREAL</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CEREAL,REG/SP</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td>NO</td>
<td colspan="2"><blockquote>
<p>0.14</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>DRY CEREAL,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>DRY CEREAL/SP</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>REG CEREAL/SP</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CHEESE,COTT,2OZ/SP</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>0.12</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>COTTAGE CHE</p>
</blockquote></td>
</tr>
</tbody>
</table>

# DF Dietetic Facilities \[FHPRG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CE</p>
</blockquote></th>
<th><blockquote>
<p>Enter/Edit Communication Offices [FHPRO9]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Production Facilities [FHPRO7]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Supplemental Fdg. Sites [FHPRO11]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Service Points [FHPRO8]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>List Production/Service/Communication Facilities [FHPRO10]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SP</p>
</blockquote></td>
<td><blockquote>
<p>Modify Site Parameters [FHSITE]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WE</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Nutrition Locations [FHPRO2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WL</p>
</blockquote></td>
<td><blockquote>
<p>List Nutrition Locations [FHPRO6]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Nutrition Facilities allows you to add new nutrition locations and edit existing nutrition locations. Manual processes for ordering individual special meals, recurring meals for VA patients, non-VA facility patients, and guest meals for outpatients are automated. There are options specialized for the type of meal requested and approved through an authorization process that notifies the requestor via an alert.

## Managing Dietetic Facilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can sort the data by multiple production facilities, service points, communication offices, supplemental feeding sites, and customized nutrition locations. Reports are generated specific to the production facility and service needs of each facility. Clinical location assignments and quality care monitors are defined for each nutrition location, which allows for monitoring specific to a patient population type. Once data is entered, clinicians generate daily patient- specific TICKLER file reminders for timely and appropriate initial and follow-up clinical care.

> Five files set the structure for the Food Management Program, Diet Order Entry Processing, Tray and Supplemental Feeding Delivery, Clinical Nutrition Location Assignments, and Clinical Tickler File. The Nutrition Facilities (DF) menu consists of five options you use to enter and edit these files and two list options to view the data. This menu also contains the option to edit site parameters.

> These files create the “Nutrition Geography” or the manner in which data is compiled for Nutrition reports. All Nutrition information is compiled according to Locations (as defined by MAS) and Delivery Points. There is a need for more data categorization. The five files in the Nutrition Facilities Program allow for multiple groupings of data, which more accurately reflect the total capabilities of the Nutrition Systems software.

> The Nutrition Location groupings of MAS Locations into a single Nutrition Location accommodate each of the various services provided by Nutrition and Food Service, such as: tray passing, clinical care, etc.

> Communication Office: Groupings of nutrition locations into communication office subgroups for optimal processing of diet order entry data.

> Supplemental Feeding Site: These are the groupings of nutrition locations into subgroups, which provide the best sequencing for processing and distributing supplemental feedings.

> Production Facility: These are the primary production areas, which prepare food for direct serving or distribution to other serving sites.

> Note: Most stations have only one Production Facility.

> Service Point: This is assembly/serving points, which are intermediate designations between the production facility and inpatients and/or outpatients.

## CE Enter/Edit Communication Offices \[FHPRO9\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Communication Offices option allows you to edit data in the COMMUNICATION OFFICE file \#119.73. You can use it to group Nutrition Locations in a format that is most advantageous to the people processing Diet Order Entry (DOE) data. All DOE activity is formatted by data in the DELIVERY POINT file. In some facilities this worked well, but at sites that created multiple Delivery Points for production and only had one or two Diet Offices for processing functions, the Delivery Point designations were cumbersome. This file allows for a distinct categorization of Locations for Diet Order processing separate from the Production Facilities category of Service Points.

> This option also contains all the site parameters, which are specific to Diet Order Entry: the diet order cut off times by meal, bagged meal requests, early/late tray times, and alarm window times. The data and functions for these parameters have not changed, but the location of the prompts have. By listing these parameters under communication offices, facilities may have greater flexibility in adjusting cut-off times for certain processing areas. For example, a Nursing Home Care Unit may not use the early/late tray options in the computer or may have different cut off times due to the type of patient service provided. Thus, the alarms for this Communication Office (NHCU) need not be set, and the cut-off times can be different than those used in the Main Hospital Communication Office.

> Many stations create only one Communication Office, however, multiple offices are possible. You may need more than one office for separate buildings, where diet activity and cards are maintained, for areas where DOE cut-off times vary, or within one diet office to divide the workload for multiple diet office personnel.

> Communication Offices Name: A communications office name is 3-30 characters long. If creating multiple offices, try to create each name with a different beginning letter to shorten data entry time to a single stroke.

> Production Facility[<sup>1</sup>](#_bookmark152): In order to print separately, use the Enter/Edit Communication Office option to establish a link for a specific Communication Office under a particular Production Facility. If this link is not established, a specific Communication Office is not selectable when entering a CENSUS during the Meal Production Reports option and is not be included or printed in a particular Production Facility.

> Note: The following field data is located in the COMMUNICATION OFFICE file.

> Begin Breakfast (Noon, Evening) Window: The next three fields define the latest time for which diet orders are accepted for each meal. The time entered is also associated with the designation B, N, and E, which may be used when entering diet orders.

> <sup>1</sup> Patch FH\*5.5\*3 January 2006 New prompt added to enter/edit a Production Facility.

#### Example

- At 3:00 AM, an NPO is entered for Mr. Jones at B. The screen displays effective at DATE and 06:20. NFSPatient’s NPO order displays on diet activity reports generated after 6:20 a.m.
- At 7:00 AM, a regular diet is entered for an NFSPatient effective NOW. The program beeps and displays:
1.  Select Time: (Late tray window times display, i.e., 1)..., 2)...)
2.  Enter YES and select a late tray time if multiple times are available, or if there is only one time available, DONE displays. NFSPatient’s diet order displays on the late tray list at the designated time.
3.  Enter NO and the regular diet order for NFSPatient goes into effect at 7:00 a.m. and displays on any diet activity reports generated after 7:00 AM, but does not display on the late tray list. Thus, NFSPatient does not receive a regular tray until the noon meal.

> Note: When an order is made by Location personnel using the meal designation B, N, or E, the time set (meal window time) in this field displays, such as the example “JUN 4, 1902-06:20”. Echoing back the diet activity cut off time, rather than the actual delivery time for the meal, such as 7:00 a.m., may be confusing. Training may be required to understand this.

4.  Enter times for each meal that represent the last time you accept diet orders for normal delivery. This is usually just prior to the start of trayline, which allows for a few minutes to begin processing of the diet activity report. You can change times at any time.

> Provide Bagged Meals?: This field allows the ordering of bagged meals for early or late trays. Enter YES for a prompt to enter a Y or N when ordering an early or late tray, to designate whether or not it is a bagged meal. Enter NO if you do not want the bagged meal prompt to display.

> Early Breakfast (Noon, Evening) Time 1 (2, 3): The program allows for the specification of up to three early and three late delivery times for each meal. Each meal must have at least one time entered. If multiple times exist, the choices are presented to the Location user. If only one time exists, the Location user is not given a choice. Each meal must have at least one time. The times designated display on the Early/Late Tray List (EL). You can change times at any time.

> <span id="_bookmark152" class="anchor"></span>Late Breakfast (Noon, Evening) Alarm Window: Alarm windows are periods of time during which a diet order cannot/will not be processed. Such windows typically are actual meal service periods. The beginning alarm time represents the "cut-off" time for accepting diet orders for normal tray delivery. It is synonymous with the Begin Breakfast (Noon, Evening) Window as entered previously.

> After this time, an order is accepted but the Location user is notified that the meal cannot be served at the normal time and is asked if a late tray is needed. The ending alarm time defines the end of this period of notification for late meal requests. The ending time should be a few minutes before the late meal assembly/delivery ends.

## FE Enter/Edit Production Facilities \[FHPRO7\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Production Facilities option allows you to edit the PRODUCTION FACILITY file \#119.71. A production facility is a primary production area, which prepares food for direct service at the same location or for distribution to other serving sites. An area of bulk food preparation, portioning and distribution usually denotes a Production Facility. Most stations have only one production facility, commonly referred to as Main Kitchen. Multi-division sites may have more than one production facility.

> Five former site parameters are now fields in the PRODUCTION FACILITY file. These five fields control the way in which menus and production reports are printed. If multiple Production Facilities are created, different data is entered for these fields for each facility. Examine the sample reports in the Production Reports chapter to determine which report format is desirable. You can change the format at any time.

> Production Facility Name: The Production Facility name may be 3-30 characters long. This name prints as an identifier on the census sheet for Meal Production Reports. If there is more than one Production Facility, make the names distinct from each other and readily recognizable for the facility.

> In order to print separately, use the Enter/Edit Communication Office option to establish a link for a specific Communication Office under a particular Production Facility. If this link is not established, a specific Communication Office is not selectable when entering a CENSUS during the Meal Production Reports option and is not be included or printed in a particular Production Facility.

> Note: The following field data is located under this option rather than the Modify Site Parameters option. Full explanations and samples of the reports affected by these site parameters are found in the Production Reports section of the *Nutrition and Food Service User Manual*.

> Full Names On Daily Menu?: This field allows you to choose the format for printing the daily menus. Full recipe names or numbers representing the recipe served to the regular diet can be printed under each production diet. If you choose numbering and a production diet cannot receive the regular recipe, the modified recipe name prints instead of the associated regular recipe number.

> Enter YES to print full recipe names under each production diet heading on the daily menu. Enter NO to print numbers and some recipe names under the Production Diet headings.

> The next four fields affect the way the Meal Production Reports print. Refer to the User Manual under the Production Reports section for an example of these reports.

> Separate Production Summary Pages?: The Production Summary (Refer to Meal Production Reports (MR) in the User Manual) for a meal may be printed as a single consolidated list of all recipes or as separate lists sorting the recipes by preparation area, i.e., Hot Prep, Cold Prep,

> Trayline, etc. A YES entry prints separate Production Summary pages for each designated preparation area. In order to use separate pages, each recipe must have a preparation area entered in the RECIPE file. A NO generates a single list Production Summary.

> Separate Recipe Preparation Pages?: The Recipe Summary (refer to Meal Production Reports (MR) in the User Manual) can also be printed as a single list or as separate lists for each preparation area. Enter YES for separate pages for each preparation area. Reports are only complete if a preparation area is entered for each recipe. Entering NO generates a single list.

> Print Meal Distribution?: The Meal Distribution Summary (refer to Meal Production Reports (MR) in the User Manual) breaks down the Production Summary quantities from servings to weight, volume, or individual measures. A YES in this field allows this report to print automatically every time a Production Summary is generated.

> Separate Storeroom Pages?: The Storeroom Requisition Summary (refer to Meal Production Reports (MR) in the User Manual) can also be printed as a single list or as separate pages for each storeroom location. Enter YES to fill in the storeroom location field for each ingredient in order for the listings to be complete.

## NE Enter/Edit Supplemental Fdg. Sites \[FHPRO11\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Supplemental Fdg. Sites option allows you to edit the SUPPLEMENTAL FEEDING SITE file \#119.74. Nutrition Locations are grouped into Supplemental Feeding (SF) sites, which are most advantageous for feeding, assembly and distribution according to the needs of the SF system rather than according to Delivery Points.

> Each SF site can set its own Supplemental Feeding Site parameters. Use this option to adjust the parameters for each designated SF area. The data and function of these parameters, Nourishment Labels Separate and Ingredients on Location Lists, have not changed. Only their location within the program was altered.

> Supplemental Feeding Site Name: The SF site name is up to 30 characters long.

> Short Name: Create a shortened name, 1-6 characters. This shortened name hastens data entry and displays on SF reports.

> Production Facility: This mandatory field requires entry of a Production Facility name from the PRODUCTION FACILITY file. The production area is responsible for preparing the food used as supplemental feedings distributed by this site. In future versions, this file pointer will be used along with the Projected Usage Option to generate ordering quantities for a designated time period. Currently, it has no specific function but must be entered.

> Separate Supp Feeding Labels?: A YES entered here generates a separate label for each supplemental feeding item ordered for a patient if the SF item has a YES in the “LABEL?” field within the SUPPLEMENTAL FEEDINGS file \#118. (See the option XS Supplemental Feeding Management.) Entering NO generates one label per patient, listing all supplemental feeding items.

#### Example

> If the Supplemental Feeding Label field is set at "YES" for separate labels, NFSPATIENT, ONE will have 2 Supplemental Feeding labels, one for Milk and one for 2 Graham Crax, and none for Apple Juice.

> IF the SF Label field is set at NO for separate labels, Mr. Bob will have one label listing Apple Juice, Milk, and 2 Graham Crax.

> Note: To separate labels for all items, you must enter YES in the Label field in the SUPPLEMENTAL FEEDINGS file and YES at this field.

> This parameter applies to only individual supplemental feedings. It does not affect Bulk Location Feedings. It also applies uniformly to all feeding times for this specific Supplemental Feeding Site. You can change this parameter at any time.

> Ingredients On Location Lists?: The choice is Y or N. Entering Yes will result in the printing of separate ingredient lists for 10:00 a.m., 2:00 p.m. and 8:00 p.m. at the end of each Location on the Location Supplemental Feeding List (WL). This parameter affects only the Locations associated with this SF Site. You can change this parameter at any time.

## SE Enter/Edit Service Points \[FHPRO8\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Service Points option allows you to edit the SERVICE POINT file \#119.72. Service Points are food assembly and distribution points between the Production Area and the patient. Each Service Point has only one service type associated with it: either trayline service or cafeteria service. This singular service type association is different from the previous definition of a Delivery Point in Version 4.01. Delivery Points could have had both trayline and cafeteria service associated with it. A Service Point can have only one associated service type. This change to Service Points was made to accommodate future Food Management enhancements.

> A Service Point may accommodate any number or combination of Nutrition Locations, outpatients, or staff. A Nutrition Location is assigned to more than one Service Point to accommodate tray and cafeteria patients. A small serving unit, which contains both a small cafeteria style operation and a small trayline operation, is designated as two separate Service Points or grouped into one cafeteria Service Point. The one Service Point is appropriate if the trays are assembled off the cafeteria line. The two Service Points are better if there are separate assembly lines for the cafeteria and trayline so the food is appropriately portioned.

> A Service Point of cafeteria is also created for outpatients and staff with no Nutrition Locations assigned. This type of service point only has “Other Meals” associated with it, instead of inpatient Locations.

> The previous service type of Dining Room (DR) is a designation made for congregate eating areas; however, it is a characteristic of a Location rather than a Delivery Point. A DR designation really deals with the manner of delivery rather than production requirements. This designation is appropriate for trays assembled and delivered to a dining room setting, and passed out to patients there, rather than in their rooms. Any Locations with Dining Room designations must have associated trayline service points. (refer to Enter/Edit Nutrition Locations for further explanation.)

> A maximum of seven Service Points is created. More than seven displaces spacing on some reports.

> Service Point Name: The Service Point Name is up to 30 characters. Select a unique name for each Service Point that is readily understood by the production and service staff.

> Short Name: For most reports, the short name of 1-6 characters is used for identification.

> Type: This field defines whether the Service Point is a trayline (T) or cafeteria (C). Enter only the T or C as necessary. Remember, a Service Point cannot be both T and C.

> Production Facility: This field indicates the Production Facility responsible for preparing the food served by this Service Point. A Service Point is assigned only one Production Facility. If a Service Point actually receives food from two Production Facilities, two distinct Service Points are created to accommodate this situation.

> Additional Meals Production Diet: This field is synonymous with the Other Meals Table created under the Production Management Program. At this prompt, a production diet is entered along with the number of meals wanted by day of week and specific meal, breakfast, noon or evening. There is no limit to the number of production diet that are selected. One to 1000 meals are entered for each day and meal time. Additional meals are entered for each Service Point to account for meals provided to outpatients, volunteers, O.D.s, etc. These meals are automatically added for this Service Point into the designated Production Diet total on the Forecasted and/or Actual Diet Census generated with the Meal Production Reports.

> Forecast % Production Diet: This field is synonymous with the Production Diet Percentages Table built under the Production Management Program. Data for this function is entered under either option. This allows for meals to be forecasted for this Service Point by Production Diet and day of the week. Once the Production Diet is entered, a number is entered for each day of the week, which reflects this Production Diet's percentage of the actual diet census for this service point. It is possible to enter up to 110 % to accommodate special needs.

## SL List Production/Service/Communications Facilities \[FHPRO10\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Production/Service/Communications facilities option generates a profile for each Production Facility, Service Point, Communication Office and Supplemental Feeding Site created. Each profile includes all data entered for each field of the respective file. These listings provide a quick reference for all data pertinent to each file.

> Associated Tray Lines:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 25%" />
<col style="width: 14%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HOSPITAL TL</p>
</blockquote></th>
<th></th>
<th></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Associated Cafeterias:</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CAFETERIA NUTRITION KITCHEN</p>
<p>VENDING MACHINE ROOM</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Associated Supplemental Fdg. Sites:</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SUPPLEMENTAL FEEDINGS</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>7-Apr-05 P R O D U C T I O N</p>
</blockquote></th>
<th>F A C I L I T Y</th>
<th><blockquote>
<p>Page 2</p>
</blockquote></th>
</tr>
<tr class="header">
<th>TRAY LINE</th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Full Names on Daily Menu: YES</p>
<p>Print Meal Distribution: YES Separate Production Summary Pages: NO Separate Recipe Preparation Pages: NO</p>
<p>Separate Storeroom Pages: YES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Associated Tray Lines:

> Associated Supplemental Fdg. Sites:

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 1%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 1%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MEAL</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>7-Apr-05 P R O</p>
</blockquote></th>
<th>D</th>
<th>U C T I O</th>
<th><blockquote>
<p>N</p>
</blockquote></th>
<th></th>
<th>F</th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>I</p>
</blockquote></th>
<th><blockquote>
<p>L</p>
</blockquote></th>
<th><blockquote>
<p>I</p>
</blockquote></th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th><blockquote>
<p>Y</p>
</blockquote></th>
<th><blockquote>
<p>Page</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th>MEAL</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Full Names on Daily Menu: Print Meal Distribution: Separate Production Summary Separate Recipe Preparation Separate Storeroom Pages:</p>
</blockquote></th>
<th></th>
<th>Pages: Pages:</th>
<th></th>
<th>YES YES YES YES YES</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Associated Cafeterias:

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 7%" />
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PARK BENCH</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th>7-Apr-05 P R O D U C T I O N F A C</th>
<th>I L I</th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th><blockquote>
<p>Y</p>
</blockquote></th>
<th><blockquote>
<p>Page</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
</tr>
<tr class="header">
<th>SOYLENT GREEN (RENEWABLE</th>
<th><blockquote>
<p>FOOD)</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>Full Names on Daily Menu: YES</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>Print Meal Distribution: YES</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>Separate Production Summary Pages: YES</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>Separate Recipe Preparation Pages: NO</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>Separate Storeroom Pages: YES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Associated Supplemental Fdg. Sites:

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 45%" />
<col style="width: 18%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TACOS ARE US 7-Apr-05</p>
</blockquote></th>
<th><blockquote>
<p>S E R V I C E P O I N T HOSPITAL TL</p>
</blockquote></th>
<th><blockquote>
<p>Page 6</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Type of Service: Short Name: Production Facility:</p>
</blockquote></th>
<th><blockquote>
<p>Tray Line MAIN KITCHEN</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Associated Nutrition Locations:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CLEAR LIQUID</p>
</blockquote></th>
<th>60.0</th>
<th>50.0</th>
<th><blockquote>
<p>70.0</p>
</blockquote></th>
<th><blockquote>
<p>88.0</p>
</blockquote></th>
<th>38.0</th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PUREED</p>
</blockquote></td>
<td>20.0</td>
<td>29.0</td>
<td><blockquote>
<p>88.0</p>
</blockquote></td>
<td><blockquote>
<p>03.0</p>
</blockquote></td>
<td>56.0</td>
<td><blockquote>
<p>11.0</p>
</blockquote></td>
<td>20.0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHOLESTEROL RESTRI</p>
</blockquote></td>
<td>30.0</td>
<td>50.0</td>
<td><blockquote>
<p>60.0</p>
</blockquote></td>
<td><blockquote>
<p>70.0</p>
</blockquote></td>
<td>71.0</td>
<td><blockquote>
<p>44.0</p>
</blockquote></td>
<td>55.0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Not Eating</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>45.0</p>
</blockquote></td>
<td>25.0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Total Sum</p>
</blockquote></td>
<td>110.0</td>
<td>129.0</td>
<td><blockquote>
<p>218.0</p>
</blockquote></td>
<td><blockquote>
<p>248.0</p>
</blockquote></td>
<td>165.0</td>
<td><blockquote>
<p>100.0</p>
</blockquote></td>
<td>100.0</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 28%" />
<col style="width: 29%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CHOLESTEROL RESTRICTED</p>
</blockquote></th>
<th><blockquote>
<p>Brk</p>
</blockquote></th>
<th>99</th>
<th>40</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Noon</p>
</blockquote></td>
<td>2 99</td>
<td>35</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Even</p>
</blockquote></td>
<td>10 50</td>
<td>50</td>
</tr>
</tbody>
</table>

> Associated Nutrition Locations:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 19%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Production Diet %:</p>
</blockquote></th>
<th><blockquote>
<p>Sun Mon</p>
</blockquote></th>
<th>Tue</th>
<th></th>
<th><blockquote>
<p>Wed</p>
</blockquote></th>
<th>Thu</th>
<th colspan="2"><blockquote>
<p>Fri Sat</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CALORIE CONTROLLED</p>
</blockquote></td>
<td><blockquote>
<p>12.0 12.0</p>
</blockquote></td>
<td>12.0</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Not Eating</p>
</blockquote></td>
<td><blockquote>
<p>88.0 88.0</p>
</blockquote></td>
<td>88.0</td>
<td></td>
<td><blockquote>
<p>100.0</p>
</blockquote></td>
<td>100.0</td>
<td colspan="2"><blockquote>
<p>100.0 100.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Total Sum</p>
</blockquote></td>
<td><blockquote>
<p>100.0 100.0</p>
</blockquote></td>
<td><blockquote>
<p>100.0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>100.0</p>
</blockquote></td>
<td>100.0</td>
<td colspan="2"><blockquote>
<p>100.0 100.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Additional Meals:</p>
</blockquote></td>
<td><blockquote>
<p>Meal</p>
</blockquote></td>
<td>Sun Mon</td>
<td></td>
<td><blockquote>
<p>Tue</p>
</blockquote></td>
<td>Wed Thu</td>
<td colspan="2"><blockquote>
<p>Fri Sat</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REGULAR</p>
</blockquote></td>
<td><blockquote>
<p>Brk</p>
</blockquote></td>
<td>10 15</td>
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>8 5</td>
<td colspan="2"><blockquote>
<p>7</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Noon</p>
</blockquote></td>
<td>10 15</td>
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>8 5</td>
<td colspan="2"><blockquote>
<p>7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Even</p>
</blockquote></td>
<td>10 15</td>
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>8 5</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7-Apr-05</p>
</blockquote></td>
<td><blockquote>
<p>S E R V I C E</p>
</blockquote></td>
<td><blockquote>
<p>P O I</p>
</blockquote></td>
<td>N</td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>Page 8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CAFETE</p>
</blockquote></td>
<td><blockquote>
<p>RIA</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Type of Service: Short Name: Production Facility:</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>Cafeteria CAFE</p>
<p>MAIN KITCHEN</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Associated Nutrition Locations:

> Associated Nutrition Locations:

<table style="width:100%;">
<colgroup>
<col style="width: 26%" />
<col style="width: 25%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 1%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>3W</p>
<p>7-Apr-05</p>
</blockquote></th>
<th><blockquote>
<p>S E R V I C E P VENDING MACHINE</p>
</blockquote></th>
<th><blockquote>
<p>O I N ROOM</p>
</blockquote></th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th>Page</th>
<th colspan="2"><blockquote>
<p>10</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Type of Service: Short Name: Production Facility:</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Cafeteria VEND</p>
<p>MAIN KITCHEN</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Associated Nutrition Locations:

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 1%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>10E</p>
<p>7-Apr-05</p>
</blockquote></th>
<th><blockquote>
<p>S E R V I C E MEAL CATERING</p>
</blockquote></th>
<th><blockquote>
<p>P O I SERVICE</p>
</blockquote></th>
<th><blockquote>
<p>N</p>
</blockquote></th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th>Page</th>
<th colspan="2"><blockquote>
<p>11</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Type of Service: Short Name: Production Facility:</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>Tray Line MEAL</p>
<p>TRAY LINE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Associated Nutrition Locations:

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="12"><blockquote>
<p>4E</p>
<p>5W</p>
<p>Production Diet %: GOURMET SPECIAL</p>
<p>Not Eating Total Sum</p>
<p>Additional Meals: GOURMET SPECIAL</p>
<p>7-Apr-05</p>
</blockquote></th>
<th></th>
<th>GOOD EATS LOCATION</th>
<th colspan="2"></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p>SICU</p>
</blockquote></th>
<th colspan="2"></th>
</tr>
<tr class="header">
<th>Sun Mon</th>
<th>Tue Wed Thu</th>
<th colspan="2"><blockquote>
<p>Fri Sat</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>70.0 80.0</th>
<th>80.0 80.0 80.0</th>
<th colspan="2"><blockquote>
<p>80.0 75.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th>30.0 20.0</th>
<th>20.0 20.0 20.0</th>
<th colspan="2"><blockquote>
<p>20.0 25.0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>100.0 100.0</th>
<th>100.0 100.0 100.0</th>
<th colspan="2"><blockquote>
<p>100.0 100.0</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Meal</p>
</blockquote></th>
<th>Sun Mon Tue Wed Thu</th>
<th colspan="2"><blockquote>
<p>Fri Sat</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Brk</p>
</blockquote></th>
<th>2 3 2 3 2</th>
<th colspan="2"><blockquote>
<p>3 2</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Noon</p>
</blockquote></th>
<th>2 3 2 3 2</th>
<th colspan="2"><blockquote>
<p>3 2</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Even</p>
</blockquote></th>
<th>2 3 2 3 2</th>
<th colspan="2"><blockquote>
<p>3 2</p>
</blockquote></th>
</tr>
<tr class="header">
<th>S E R V I C</th>
<th>E P O I N T</th>
<th colspan="2"><blockquote>
<p>Page 12</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>PARK</th>
<th>BENCH</th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Type of Service: Short Name: Production Facility:</p>
</blockquote></td>
<td><blockquote>
<p>Cafeteria PARK MEALS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Associated Nutrition Locations:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 1%" />
<col style="width: 45%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SICU</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Production Diet %:</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>Sun Mon Tue Wed Thu</td>
<td>Fri</td>
<td colspan="2"><blockquote>
<p>Sat</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MECHANICAL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>60.0 80.0 89.0 91.0 82.0</td>
<td>84.0</td>
<td colspan="2"><blockquote>
<p>65.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GOURMET SPECIAL</p>
<p>Not Eating</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>60.0 80.0 85.0 87.0 82.0</td>
<td>88.0</td>
<td colspan="2"><blockquote>
<p>62.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Total Sum</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>120.0 160.0 174.0 178.0 164.0</td>
<td>172.0</td>
<td colspan="2"><blockquote>
<p>127.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Additional Meals:</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>Meal Sun Mon Tue Wed Thu</td>
<td colspan="3"><blockquote>
<p>Fri Sat</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REGULAR</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>Brk 8 8 8 8 8</td>
<td colspan="3"><blockquote>
<p>6 6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>Noon 8 8 8 8 8</td>
<td colspan="3"><blockquote>
<p>6 6</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>Even 8 8 8 8 8</td>
<td colspan="3"><blockquote>
<p>6 6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GOURMET SPECIAL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>Brk 5 5 5 5 5</td>
<td colspan="3"><blockquote>
<p>3 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>Noon 5 5 5 5 5</td>
<td colspan="3"><blockquote>
<p>3 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>Even 5 5 5 5 5</td>
<td colspan="3"><blockquote>
<p>3 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7-Apr-05</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>M U N I C A T I O N O F F I C E</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Page 13</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>COMMUNICATION OFFICE</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Provide Bagged Meals:</p>
<p>Meal Time:</p>
</blockquote></td>
<td></td>
<td></td>
<td><p>YES</p>
<blockquote>
<p>Breakfast Noon</p>
<p>8:15A 12:00P</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Evening 6:00P</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Early Time 1: 6:30A 11:15A</p>
<p>Early Time 2:</p>
<p>Early Time 3:</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>5:30P</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Late Time 1: 10:00A 1:30P</p>
<p>Late Time 2: 2:30P</p>
<p>Late Time 3:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>7:00P</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Late Alarm Begin: 10:00A 11:00A Late Alarm End: 3:00P</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Associated Nutrition Locations:</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>10E 5E</p>
<p>1A 7E</p>
<p>1B GOOD SLEEPIN LOCATION</p>
<p>3E PSY1</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>7-Apr-05 C O M M U N I C A T I O N O F F I C E</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Page 14</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>NORTH POLE</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Provide Bagged Meals: YES</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Breakfast Noon</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Evening</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Meal Time: 5:00A 11:30A</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>4:45P</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Early Time 1: 5:00A 11:00A</p>
<p>Early Time 2: 5:30A 11:30A</p>
<p>Early Time 3: 6:00A 11:45A</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>4:00P</p>
<p>4:30P</p>
<p>5:00P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Late Time 1: 9:00A 1:00P</p>
<p>Late Time 2: 9:30A 1:30P</p>
<p>Late Time 3: 10:00A 2:00P</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>6:30P</p>
<p>7:00P</p>
<p>7:30P</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Late Alarm Begin: 8:45A 1:45P</p>
<p>Late Alarm End: 10:15A 2:30P</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>6:15P</p>
<p>7:15P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Associated Nutrition Locations:</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>12E 5W</p>
<p>3W GOOD EATS LOCATION</p>
<p>4E</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>7-Apr-05 C O M M U N I C A T I O N O F F I C E</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Page 15</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>SCOTTVILLE</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Provide Bagged Meals:</p>
<p>Meal Time: Early Time 1:</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>Breakfast</p>
<p>9:00A</p>
<p>8:00A</p>
</blockquote></td>
<td><blockquote>
<p>Noon 1:00P</p>
<p>11:00A</p>
</blockquote></td>
<td><blockquote>
<p>Evening 6:00P</p>
<p>5:00P</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 1%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Early Time 2:</p>
<p>Early Time 3:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>11:30A</th>
<th></th>
<th rowspan="13"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Late Time 1:</p>
<p>Late Time 2:</p>
<p>Late Time 3:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>10:00A</p>
<p>10:30A</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>1:30P</p>
<p>1:45P</p>
<p>2:00P</p>
</blockquote></th>
<th><blockquote>
<p>6:30P</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Late Alarm Begin: Late Alarm End:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>9:30A</p>
<p>9:35A</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>1:30P</p>
<p>1:35P</p>
</blockquote></th>
<th><blockquote>
<p>6:45P</p>
<p>6:50P</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="16"><blockquote>
<p>Associated Nutrition Locations:</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="16"><blockquote>
<p>SICU</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th>7-Apr-05 C</th>
<th>O</th>
<th><blockquote>
<p>M</p>
</blockquote></th>
<th>M</th>
<th><blockquote>
<p>U</p>
</blockquote></th>
<th><blockquote>
<p>N</p>
</blockquote></th>
<th><blockquote>
<p>I</p>
</blockquote></th>
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th><blockquote>
<p>I</p>
</blockquote></th>
<th><blockquote>
<p>O</p>
</blockquote></th>
<th><blockquote>
<p>N O F F</p>
</blockquote></th>
<th><blockquote>
<p>I</p>
</blockquote></th>
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>Page 16</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="16"><blockquote>
<p>ALLENDALE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th>Provide Bagged Meals:</th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th>NO</th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th></th>
<th rowspan="6"></th>
<th rowspan="6"></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>Breakfast</p>
</blockquote></th>
<th><blockquote>
<p>Noon</p>
</blockquote></th>
<th><blockquote>
<p>Evening</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Meal Time:</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>7:00A</p>
</blockquote></th>
<th>11:00A</th>
<th><blockquote>
<p>5:00A</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Early Time 1:</p>
<p>Early Time 2:</p>
<p>Early Time 3:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Late Time 1:</p>
<p>Late Time 2:</p>
<p>Late Time 3:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Late Alarm Begin: Late Alarm End:</p>
</blockquote></th>
<th></th>
<th><p>7:30A</p>
<p>11:30A</p></th>
<th><p>10:30A</p>
<p>10:25A</p></th>
<th><blockquote>
<p>4:00P</p>
<p>3:45P</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Associated Nutrition Locations:

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>7-Apr-05 S U P P L E M E N T A L F E E D I N G</p>
<p>SUPPLEMENTAL FEEDINGS</p>
</blockquote></th>
<th>S</th>
<th>I</th>
<th>T</th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>Page 17</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Short Name: S FDGS</p>
<p>Separate Labels: YES Items on Location Lists: NO</p>
<p>Production Facility: MAIN KITCHEN Associated Nutrition Locations:</p>
<p>1A 5E</p>
<p>1B PSY1</p>
<p>3E</p>
<p>7-Apr-05 S U P P L E M E N T A L F E E D I N G</p>
<p>SUPP SITE 1</p>
</blockquote></td>
<td>S</td>
<td>I</td>
<td>T</td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Page 18</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="6"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Short Name: SITE 1</p>
<p>Separate Labels: YES Items on Location Lists: YES</p>
<p>Production Facility: TRAY LINE Associated Nutrition Locations:</p>
<p>7E GOOD SLEEPIN LOCATION</p>
<p>7-Apr-05 S U P P L E M E N T A L F E E D I N G S I T E Page 19 SAMMY'S SOUP SALON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Short Name: SAM'S</p>
<p>Separate Labels: YES Items on Location Lists: YES</p>
<p>Production Facility: GRETTA'S GREASY GRITS Associated Nutrition Locations:</p>
<p>10E 4E</p>
<p>12E 5W</p>
<p>3W GOOD EATS LOCATION</p>
<p>7-Apr-05 S U P P L E M E N T A L F E E D I N G S I T E Page 20 TACOS ARE US</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Short Name:</p>
<p>Separate Labels: YES Items on Location Lists: YES</p>
<p>Production Facility: SOYLENT GREEN (RENEWABLE FOOD) Associated Nutrition Locations:</p>
<p>SICU</p>
</blockquote></td>
</tr>
</tbody>
</table>

## SP Modify Site Parameters \[FHSITE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Modify Site Parameters option allows you to modify site parameters. All data previously listed under this option was moved to the PRODUCTION FACILITY file. Each label printer used for Nutrition labels is entered. The device name is entered in the facility’s DEVICE file. The size of labels used on this device is also entered. Each device has one label size assigned. There are four sizes available.

> 1\. 3-1/2 x 15/16

> 2\. 4 x 1-7/16

> 3\. 2-5/8 x 1

> 4\. 4 x 1-1/3

> All label printers are entered in order to print labels within the Nutrition Program. There are 15 authorizer fields in the FH SITE PARAMETERS ( 119.9) file.[<sup>1</sup>](#_bookmark160)

> Select Dietetic Facilities Option: SP Modify Site Parameters

> Select LABEL PRINTERS: HPLASERJET\$PRT-BIG// LABEL PRINTERS: HPLASERJET\$PRT-BIG//

> SIZE OF LABELS: 2-5/8 x 1 (Laser labels - 30 labels per sheet)

> // ?

> Choose from:

1.  3-1/2 x 15/16 (Single strip labels)
2.  4 x 1-7/16 (Single strip labels)
3.  2-5/8 x 1 (Laser labels - 30 labels per sheet)
4.  4 x 1-1/3 (Laser labels - 14 labels per sheet) SIZE OF LABELS: 2-5/8 x 1 (Laser labels - 30 labels per sheet)

> // 2 4 x 1-7/16 (Single strip labels) Select LABEL PRINTERS: \<RET\>

> MULTIDIVISIONAL SITE?: NO// \<RET\>

> OUTPATIENT MEALS DIET1: OUTPATIENT REGULAR// \<RET\> OUTPATIENT MEALS DIET2: LOW CALORIE// \<RET\> OUTPATIENT MEALS DIET3: CARDIAC// \<RET\>

> OUTPATIENT MEALS DIET4: VEGETARIAN// \<RET\> OUTPATIENT MEALS DIET5: MECHANICAL// \<RET\> OUTPATIENT MEALS DIET6: LOW POTASSIUM// \<RET\> OUTPATIENT MEALS DIET7: LOW SODIUM// \<RET\> OUTPATIENT MEALS DIET8: 2GM SODIUM// \<RET\>

> OUTPATIENT MEALS DIET9: LOW PROTEIN// \<RET\>

> OUTPATIENT MEALS DIET10: ATKINS// \<RET\> OUTPATIENT MEALS DIET11: SOFT// \<RET\> OUTPATIENT MEALS DIET12: FULL LIQUID// \<RET\>

> OUTPATIENT MEALS DIET13: 18000FLRES2ND TEST// \<RET\> OUTPATIENT MEALS DIET14: CLEAR LIQUID// \<RET\> OUTPATIENT MEALS DIET15: LOW CHOL/FAT// \<RET\>

> <sup>1</sup> FH\*5.5\*5 May 2007 Ten Authorizer fields were added to the FH SITE PARAMETER file (#119.9), for a total of 15 fields.

> AUTHORIZOR 1: NFSClinician,One// \<RET\> AUTHORIZOR 2: NFSClinician,Two // \<RET\> AUTHORIZOR 3: NFSClinician,Three // \<RET\> AUTHORIZOR 4: NFSClinician,Four // \<RET\> AUTHORIZOR 5: NFSClinician,Five // \<RET\> AUTHORIZOR 6: NFSClinician,Six // \<RET\> AUTHORIZOR 7: NFSClinician,Seven // \<RET\> AUTHORIZOR 8: NFSClinician,Eight // \<RET\> AUTHORIZOR 9: NFSClinician,Nine // \<RET\> AUTHORIZOR 10: NFSClinician,Ten // \<RET\> AUTHORIZOR 11: NFSClinician,Eleven // \<RET\> AUTHORIZOR 12: NFSClinician,Twelve // \<RET\> AUTHORIZOR 13: NFSClinician,Thirteen// \<RET\> AUTHORIZOR 14: NFSClinician,Fourteen // \<RET\> AUTHORIZOR 15: NFSClinician,Fiveteen // \<RET\> EMPLOYEE CLASS: YES// \<RET\>

> PAID CLASS: YES// \<RET\>

> OOD CLASS: NO// \<RET\> VOLUNTEER CLASS: NO//\<RET\> GRATUITOUS CLASS: NO// \<RET\>

> EMPLOYEE BREAKFAST CHARGE: 2.79// \<RET\>

> EMPLOYEE NOON CHARGE: 0.00// \<RET\>

> EMPLOYEE EVENING CHARGE: 4.49// \<RET\>

> PAID BREAKFAST CHARGE: 3.29// \<RET\>

> PAID NOON CHARGE: 3.99// \<RET\> PAID EVENING CHARGE: 4.99// \<RET\> OOD BREAKFAST CHARGE: 2.29// \<RET\> OOD NOON CHARGE: 3.29// \<RET\>

> OOD EVENING MEAL: 3.99// \<RET\>

> VOLUNTEER BREAKFAST CHARGE: 1.99// \<RET\> VOLUNTEER NOON CHARGE: 1.99// \<RET\> VOLUNTEER EVENING CHARGE: 1.99// \<RET\>\<RET\>

> GRATUITOUS BREAKFAST CHARGE: 4.79// GRATUITOUS NOON CHARGE: 5.69// \<RET\>\<RET\>

> GRATUITOUS EVENING CHARGE: 6.99// \<RET\> WILL YOU USE TRAY TICKETS?: YES// \<RET\> HEADING ON BOTTOM OF TICKET?: YES// \<RET\>

## WE Enter/Edit Nutrition Locations \[FHPRO2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Enter/Edit Nutrition Locations option allows you to edit data in the NUTRITION LOCATION file (#119.72). This file uses the Medical Administrative Service's LOCATION file \#42, and allows stations to aggregate the MAS Locations into Nutrition Locations.

> The Enter/Edit Nutrition Locations \[FHPRO2\] option is used to set up Room-Beds for Outpatient Locations. Once Room-Beds are set up for outpatient locations, the Recurring, Special, and Guest meal order options are used to select a Room-Bed when ordering outpatient meals. The outpatient Room-Bed displays on Tray Tickets and Diet Cards, as well as in other reports and options.

> This aggregation accommodates the way in which Nutrition and Food Service wants to deliver services rather than the previous constraints of the MAS designations.

- A Nutrition Location is named as the MAS Location, or a new name familiar to Nutrition and Food Service, which includes one or more MAS Locations.
- Many site parameters that universally apply to all Locations and Delivery Points, are individually assigned to a Nutrition Location. This provides each station with greater flexibility in setting parameters for Diet Order Entry (DOE), such as default admission diets, no order labels, print order, and tray, cafeteria and dining room designations, as well as Clinical Location assignment and Tickler rules.
- At some facilities, two or more dietitians are assigned to specific sections of one MAS Location. This allows for each one to have a separate Nutrition Location from which consults and bulletins are automatically generated.
- The Clinician field is a multiple field, which allows you to assign multiple clinicians to each nutrition location. Each assigned clinician receives the consult, diet, and tubefeeding bulletins.

> You can change all parameters in the NUTRITION LOCATION file at any time. This file uses data from many other Nutrition Files: SERVICE POINT, COMMUNICATION OFFICE, SUPPLEMENTAL FEEDING SITE, DIETS, and other VistA files. Any changes to any of these files impact and automatically change the NUTRITION LOCATION file.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#)</p>
<p>POINTER FIELD</p>
</blockquote></th>
<th><p>POINTER</p>
<p>TYPE</p></th>
<th><blockquote>
<p>(#) FILE POINTER FIELD</p>
</blockquote></th>
<th>FILE POINTED TO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p><strong>NUTRITION PERSON</strong> (#115.01) | | ADMISSION: LAST LABEL * (N )-&gt; | 119.6 <strong>NUTRITION LOCATION</strong></p>
<p>ADMISSION:NUTRITION LOCATION (N C )-&gt;| CLINICIAN |-&gt; NEW PERSON NUTRITION:NUTRITION WA* (N )-&gt; | TRAY SERVICE P* |-&gt; <strong>SERVICE POINT</strong></p>
<p>| CAFETERIA SERV* |-&gt; <strong>SERVICE POINT</strong></p>
<p>| COMMUNICATION * |-&gt; <strong>COMMUNICATION *</strong></p>
<p>| SUPP. FDG. SITE |-&gt; <strong>SUPPLEMENTAL F*</strong></p>
<p>| DEFAULT ADMISS* |-&gt; <strong>DIETS</strong></p>
<p>| m BULK N:BULK N* |-&gt; <strong>SUPPLEMENTAL F*</strong></p>
<p><span id="_bookmark160" class="anchor"></span>| m ROOM-B:ROOM-B* |-&gt; ROOM-BED</p>
<p>| m ASSOCI:ASSOCI* |-&gt; LOCATION LOCATION</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The NUTRITION LOCATION file (#119.6) has fields for the maximum number of days for ordering outpatient meals ahead of time, the number of days to review the Outpatient Meals Print Meal Plan Expiration List, non-VA facility designation, and inpatient or outpatient location designation.. Do not delete entries in this file if they are no longer in use, just *inactivate* them.

> Note: When you select this option, a list of rooms/beds or MAS Locations may display with a statement that the rooms/beds are not assigned to a Nutrition Location. This helps during installation of the software or whenever MAS adds locations or rooms/beds. The message is a reminder that you must assign these areas to Nutrition Locations, in order to service patients admitted to these MAS designations.

> Nutrition Locations Name: Nutrition Locations may be named the same as MAS Locations or may be given a distinct Nutrition name. It may be 1-30 characters in length and may be changed at any time.

> Clinician(s):[<sup>1</sup>](#_bookmark161) This multiple field allows you to assign multiple clinicians to each nutrition location. All nutrition consults and/or mailman notifications for special diets and tubefeedings are routed electronically to each assigned clinician. The consult, diet, and tubefeeding bulletins can be sent to more than one dietitian on a unit.

> Room-Bed:[<sup>2</sup>](#_bookmark161) The Enter/Edit Nutrition Locations \[FHPRO2\] option must be used to set up Room-Beds for Outpatient Locations. Once Room-Beds are set up for outpatient locations, then the Recurring, Special, and Guest meal order options can be used to select a Room-Bed when ordering outpatient meals. The outpatient Room-Bed will then be displayed on Tray Tickets and Diet Cards as well as other reports and display options. All rooms and beds to be assigned to this Nutrition Location must be entered in this field. Only active beds as listed in File (#405.4) (MAS) can be entered.

> Caution: Rooms and beds may have identical names. Make sure the correct

> MAS-LOCATION-ROOM-BED is associated with the correct Nutrition Location.

> Associated MAS Location: This field represents the default MAS Location or Locations associated with this Nutrition Location. Any patient admitted without a room-bed designation to any MAS Location entered in this field is automatically assigned to this Nutrition Location.

> Also, for forecasting purposes in the Food Management Program, the census for this MAS Location is used in calculating the forecasted census for this Nutrition Location. This field allows for multiple entries, however, each entry must be an active Location within the MAS LOCATION file.

> <sup>1</sup> Patch FH\*5.5\*8 September 2007 Changed the Clinician field to Clinician(s) in the Enter/Edit Nutrition Locations option.

> <sup>2</sup> Patch FH\*5.5\*5 May 2007 Modified the Enter/Edit Nutrition Locations \[FHPRO2\] option to set up Room-Beds for Outpatient Locations, allowing the outpatient Room-Bed to display on Tray Tickets and Diet Cards, as well as in other reports and options.

> Tray Service Point: This field uses data from the SERVICE POINT file. Only a Service Point with a trayline designation is entered. It indicates that tray service is available to this Location and is provided by this Service Point. This field must have a designated trayline Service Point if Dining Room service is also to be provided to this location.

> Tray Forecast %: This field functions in the forecasting process of Food Production Management. Complete this field only if you are also assigning a Cafeteria Service Point to this Location and the facility uses the Forecasting Program. Enter a number 0-120, with no decimals. This figure indicates the percentage of patients from this Location who usually receive tray service. If no value is entered, 100% or all patients are tray service.

> Cafeteria Service Point: Only Cafeteria Service Point names from the SERVICE POINT file are entered in this field. An entry indicates cafeteria service is available to this location and is provided by this Service Point. If a name is entered, the Location user is asked at the time of Diet Order Entry whether the patient is to receive Tray Service (T) or is to go to a Cafeteria (C).

> Cafeteria Forecast %: This field should only be completed if the forecasting process is to be utilized in the Food Production Program. A figure between 0 and 120, no decimals, may be entered to reflect the usual percentage of the patients on this Location who would eat in the Cafeteria. If no figure is entered, 100% of the patients are eating in the Cafeteria.

> Note: If you enter a Tray Service Point and a Cafeteria Service Point, if you fail to enter any figures under the Forecast % fields, and you run the Forecast Census for Production, you end up with 200% of the census for this Location. The program assumes all patients are eating in both places.

> Dining Room Tray Service: A YES in this field allows for a congregate eating area designation (Dining Room) for this Location. A Tray Service Point is also entered for the location, as all Dining Room patients actually receive trays from a trayline. A YES entry results in a prompt to the Location user at time of diet order entry, as to whether the patient is a Tray (T) or Dining Room (D) patient. The diet card label also reflects a D designation for appropriate delivery to the Dining Room.

> Communication Office: Enter the name of the Communication Office from the COMMUNICATION OFFICE file, which is responsible for processing all Diet Order Entry (DOE) data for this Location at this prompt.

> Supplemental Feeding Site: At this field, select the Supplemental Feeding Site, which is responsible for preparing and distributing supplements for this Location.

> Print Order: The number entered in this field is used to sort the Locations for printing the various DOE reports: Diet Activity, Tubefeeding, Supplemental Feeding, NPO List, etc. A number between 1 and 99 may be entered, with 1 printing first and 99 last. This print order applies to this Location on all reports. Only one print order can be assigned to each Location.

> Default Admission Diet: This parameter is set for each Nutrition Location. It directly affects operations and depends upon the DOE and clinical policies. This field may be null, generating no diet order, or contain a diet from the DIETS file. If a diet is entered, the program automatically orders that diet for every new admission to this location as soon as the patient is admitted by MAS.

> The effect on operations may vary significantly. For example, it may cause a reduction in late supper trays because patients are served, because of an automatic diet order. On the other hand, it may generate additional trays for patients who have not yet reached the Location. In addition, it may also cause a problem on same-day surgery locations where patients are normally admitted NPO. Evaluate the use of this parameter carefully for each Nutrition Location. If you use this field for this Location, enter a diet name from the DIETS file.

> No Order Diet on Admission: This field controls the generation of a No Order label for all patients at time of admission to this Location. This field is functional only if No default admission diet is entered and if a YES is entered at this prompt. A label is generated when Diet Activity is run if no diet order is entered. A NO at this prompt simply prohibits the generation of a No Order label. Regardless of the data entered in this field, No Order displays on the Patient Profile and Location Diet Order for new admissions to this location without diet orders.

> Bulk Location Feeding: This prompt allows for the ordering of bulk Location feedings for this Nutrition Location. Only bulk feedings already created in the SUPPLEMENTAL FEEDINGS file is entered. Once the name is entered, a quantity prompt displays. Multiple entries are possible.

> Note: The next eight fields are clinical parameters that are part of the DIETITIAN TICKLER FILE. They allow each station to set the guidelines for the Tickler rules for each Nutrition Location. By setting the rules at the Location level, the clinical applications are more appropriate for the type of patients you review.

> \# Days to Review NPO: For this field, enter a number from 1 to 7 to represent the number of days following an NPO order that the patient's name will display on the CLINICAL TICKLER FILE for review. When setting the days, remember the first day of an NPO is whenever it goes into effect, that is, it could be at 12:01 a.m. or 11:58 p.m. In the first case, it represents a whole day. In the second example, the patient may only be NPO for the two minutes left in that day. Review the facility's practices for routine entering of NPOs and determine which timeframe, 1- 7 days, is best for triggering the NPO review.

> \# Days to Review Tubefeedings: Enter the number of days, from 1 to 30, which represents when the patient should display on the DIETITIAN TICKLER FILE for tubefeeding order review. This field is meant primarily to track stable, long term tube fed patients.

> <span id="_bookmark161" class="anchor"></span>New or acute tube fed patients, usually have frequent product, strength or volume changes. Each change triggers the clock to reset for this Tickler rule. Thus, patients with frequent changes usually do not display on a Tickler report. Clinicians are alerted via MailMan bulletins each time

> a tubefeeding changes for acute care patients. Thus, their care can be tracked through MailMan rather than the TICKLER FILE.

> \# Days to Review Supplemental Feedings: Enter the number of days after which you want to review a patient's supplemental feeding order. The patient's name displays on the DIETITIAN TICKLER FILE for supplemental review after the designated timeframe.

> \# Days for Status After Admission: Enter the number of days following admission after which a Nutritional Status should be entered into the computer. This alerts the clinician that a patient was admitted for the designated number of days and does not have a Nutritional Status entered into the computer.

> \# Days To Review Status I: Enter the number of days after a Status Level I is assigned for the clinician to review the patient's status on this Location. The TICKLER FILE displays notice of need to review patient at Status Level I. The clock is reset every time a new status is entered.

> \# Days To Review Status II: Enter the number of days after a Status Level II is entered for the clinician to review the patient's status on this Location. The TICKLER FILE displays notice of need to review patient at Status Level II. The clock is reset every time a new status is entered.

> \# Days To Review Status III: Enter the number of days after a Status Level III is entered for the clinician to review the patient's status on this Location. The TICKLER FILE displays notice of need to review patient at Status Level III. The clock is reset every time a new status is entered.

> \# Days To Review Status IV: Enter the number of days after a Status Level IV is entered for the clinician to review the patient's status on this Location. The TICKLER FILE displays notice of need to review patient at Status Level IV. The clock is reset every time a new status is entered.

#### Outpatient Locations

> Outpatient locations are also set up in the NUTRITION LOCATION file (#119.6) (formerly the DIETETIC WARD file).

> To set the outpatient locations, use the Enter/Edit Nutrition Locations option.

1.  Select Dietetics Management Option: Dietetic Facilities.

> CE Enter/Edit Communication Offices FE Enter/Edit Production Facilities NE Enter/Edit Supplemental Fdg. Sites SE Enter/Edit Service Points

> SL List Production/Service/Communication Facilities SP Modify Site Parameters

> WE Enter/Edit Nutrition Locations WL List Nutrition Locations

2.  Select Dietetic Facilities Option: Enter/Edit Nutrition Locations by entering WE.
3.  Select WARD or OUTPATIENT for the type of location to create.

> WARD or OUTPATIENT LOCATION:OUTPATIENT

4.  Enter the name of the Nutrition Location, a name to use for Nutrition and Food Service purposes.

> Select Dietetic Facilities Option: WE Enter/Edit Nutrition Locations Select WARD or OUTPATIENT Location: Outpatient Location Select NUTRITION LOCATION NAME: SBK TESTING LOCATION

> Are you adding ‘SBK TESTING LOCATION’ as A new NUTRITION LOCATION (the 34<sup>TH</sup>)? No//

5.  Enter YES.

> NUTRITION LOCATION NAME: SBK TESTING LOCATION Replace

6.  Optional: Enter an associated Hospital Location from file \#44. It is not required to link every Nutrition Location to an associated Hospital Location. However, for VA-inpatient and VA- outpatient locations, an associated Hospital Location is needed. You can associate multiple Hospital Locations with a Nutrition Location.

> ASSOCIATED HOSPITAL LOCATION:

7.  Enter YES.
8.  Enter the Tray Service Point. Type ?? to view a list of service points from which to choose. If this field is populated, the next field displays.

TRAY FORECAST %:

> TRAY FORECAST %. This is the percentage of patients on the ward typically receiving tray service.

9.  Enter the Cafeteria Service Point. Type ?? to view a list of service points from which to choose. If this field is populated, the next field displays.

> CAFETERIA FORECAST %:

10. Enter the Dining Room Tray Service. Enter YES or NO. Does the location use dining room tray service? If this field is set to YES, the next field displays.

DINING ROOM FORECAST %:

11. Enter the Communication Office: Enter the Communication Office to link this location to, or enter ?? to view a list of Communication Offices.
12. Enter the Max \# of Days.

> Note: This field is optional. If used, it sets to the maximum number of days ahead, to order a recurring meal plan. If this field is set to 365, when ordering a recurring meal, it cannot be ordered beyond one year from the ordering date. If the field is NULL, the default, 999 days is accepted. This field is checked when entering the FROM/TO dates in the Order/Edit Outpatient Meals option.

13. Enter the Number of Days for Review.

> Note: Use this field for the Outpatient Meals Print Meal Plan Expiration List option. Set it to the number of days used for review by the Max \# of Days option.

#### Example

> If this field is set to 7, when the Print Meal Plan Expiration List option is run, it checks for recurring meal plans that expire within the next 7 days.

14. Enter the Non-VA Facility. Choose from YES (Y) or NO (N).

> Note: This is an optional YES/NO field to use when setting up new outpatient locations. If the field is set to YES, the Order/Edit Recurring Meal option uses this flag to allow selection of up to 5 diets from any diet in the DIETS (#111) file. If the field is blank or set to NO, the Order/Edit option only allows selection of 1 diet from the 5 allowable diets set up in the site parameters.

15. Enter the Inpatient/Outpatient. Enter O for Outpatient Locations.
16. Enter the Print Order. Enter a numeric for the print order value.
17. Select Bulk Nourishments.

> TThe following fields are optional.

> \# DAYS TO REVIEW NPO: \# DAYS TO REVIEW TF:

> \# DAYS TO REVIEW SF:

> \# DAYS FOR STATUS AFTER ADMIT: \# DAYS TO REVIEW STATUS I:

> \# DAYS TO REVIEW STATUS II: \# DAYS TO REVIEW STATUS III: \# DAYS TO REVIEW STATUS IV: CAFETERIA ON TRAY TICKET: INACTIVE?:

## WL List Nutrition Locations \[FHPRO6\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Nutrition Locations option allows for the printing of all or individual Nutrition Location profiles. Each profile lists all the data associated with the designated location as entered in the previous option. All data is readily identified. The percentage entered under the Forecast % Field displays next to the Tray Assembly or Cafeteria designation in parenthesis.

> The Also Send Alert To column allows you to list the names of additional clinicians assigned to the Nutrition Location.[1](#_bookmark166)

> Select DEVICE: HOME// \<RET\> Enter printer device OR

> \<RET\>.

> NUTRITION LOCATION ASSIGNMENTS OCT 3,2006 10:41 PAGE 1 NAME CLINICIAN

ALSO SEND ALERTS TO

> 1AS NFSclinician,one

> 214-2 DOM NFSclinician,two

> 217-2 DOM NFSclinician,three

> 2AS NFSclinician,five

> 2ASM NFSclinician,six

> 3AS NFSclinician,seven

> 4AS NFSclinician,eight

> 5NM NFSclinician,five

> 5NP NFSclinician,seven

> 6AS NFSclinician,ten

> DIALYSIS NFSclinician,two DIGESTIVE HEALTH CLINIC NFSclinician,four DOM NFSclinician,three

> HEMATOLOGY NFSclinician,two

> HOPTEL MAXIMUM LENGTH NFSclinician,one

> MEALS ON WHEELS NFSclinician,C

> MICU NFSclinician,B

> NEW CLINIC NFSclinician,seven

> NHCU NFSclinician,four

> PROSTHETICS CLINIC NFSclinician,five

> RADIOLOGY NFSclinician,three

> SICU NFSclinician,eight

> SOLDIER'S HOME NFSclinician,ten

> NSFclinician,A NFSclinician,B

> NFSclinician,C

> NFSclinician,five

> <sup>1</sup> Patch FH\*5.5\*4 November 2006 Added the Also Send Alert To column to list the names of additional clinicians.

# OM Outpatient Meals \[FHMGROM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SM</p>
</blockquote></th>
<th><blockquote>
<p>Special Meals Menu… [FHOMSMGR]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>RM</p>
</blockquote></td>
<td><blockquote>
<p>Recurring Meals Menu… [FHOMRMGR]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td><blockquote>
<p>Guest Meals Menu… [FHOMGMGR]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The Outpatient Meals menus and options are accessible from the Dietetic Management Menu \[FHMGR\]. The processes are automated and replace the manual processes for ordering individual special meals, recurring meals for VA patients, non VA facility patients and guest meals for individuals for outpatient services.

### Implementation for Outpatient Meals[<sup>1</sup>](#_bookmark167)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Site Parameters

> Some site parameters need to be set up to allow Outpatient Meals to function properly. Outpatient locations need to be set up in the NUTRITION LOCATION file (#119.6) (formerly the Dietetic Ward file).

> Note: Type ?? in any field for more details or a list of available choices.

#### Example

> OUTPATIENT MEALS DIET1: ?? displays a list of all the available Diets from which to select.

> To set the system site parameters, use the *Modify Site Parameters* option.

1.  Select the Dietetics Management Option: System Management. DF Create Dietetic File entry for all Inpatients DL Update Patient Dietetic Location

> FP Check File Pointers

> PD Purge Dietetic Data

> RD Recode Diets for all Inpatients RI Check Integrity of Routines

> SP Modify Site Parameters

2.  Select the System Management Option: Modify Site Parameters by entering SP.
3.  Select a printer for printing labels.

> Select LABEL PRINTERS: HPLASERJET6-LABEL// LABEL PRINTERS: HPLASERJET6-LABEL//

> SIZE OF LABELS: 2-5/8 x 1 (Laser labels - 30 labels per sheet)//

4.  Indicate whether it is a multidivisional site. The default is NO.

> MULTIDIVISIONAL SITE?: NO//

5.  Enter a diet from the DIETS file (#111) for each of the fifteen fields that follow. You can enter up to 15 diets only; one in each field. Enter the diet name or enter ?? for a list of diets from which to choose. These are the only outpatient diets that are selectable for VA- outpatient locations with OUTPATIENT MEALS DIET1 as the default outpatient diet. Non- VA outpatient locations are able to order any diet from the DIETS file.

> <sup>1</sup> FH\*5.5\*2 January 2006 Added the Implementation for Outpatient Meals section to the ADPAC Guide.

- <span id="_bookmark166" class="anchor"></span>OUTPATIENT MEALS DIET1:
- OUTPATIENT MEALS DIET2:
- OUTPATIENT MEALS DIET3:
- OUTPATIENT MEALS DIET4:
- OUTPATIENT MEALS DIET5:
- Through Outpatient Meals Diet15
6.  Enter clinicians who can authorize special meals. You can enter up to 15; one user in each field. Enter a name or enter ?? for a list of names from the NEW PERSON file (#200).

> AUTHORIZER 1:

> AUTHORIZER 2:

> AUTHORIZER 3:

> AUTHORIZER 4:

> AUTHORIZER 5:

> AUTHORIZER 6:

> AUTHORIZER 7:

> AUTHORIZER 8:

> AUTHORIZER 9:

> AUTHORIZER 10:

> AUTHORIZER 11:

> AUTHORIZER 12:

> AUTHORIZER 13:

> AUTHORIZER 14:

> AUTHORIZER 15:

7.  Enter YES or NO at the class type field, if you serve these types of meals at your facility.

> EMPLOYEE CLASS:

> PAID CLASS:

> OOD CLASS:

> VOLUNTEER CLASS:

> GRATUITOUS CLASS:

8.  Enter a dollar amount for each class type of meals you serve at your facility. If you do not serve a particular type of meal, leave that charge-related field blank.

> EMPLOYEE BREAKFAST CHARGE:

> EMPLOYEE NOON CHARGE:

> EMPLOYEE EVENING CHARGE:

> PAID BREAKFAST CHARGE:

> PAID NOON CHARGE:

> PAID EVENING CHARGE:

> OOD BREAKFAST CHARGE:

> OOD NOON CHARGE:

> OOD EVENING MEAL:

> VOLUNTEER BREAKFAST CHARGE:

> VOLUNTEER NOON CHARGE:

> VOLUNTEER EVENING CHARGE:

> GRATUITOUS BREAKFAST CHARGE:

> GRATUITOUS NOON CHARGE:

> GRATUITOUS EVENING CHARGE:

9.  Enter YES or NO to indicate a tray ticket and if there is a heading on the bottom of the ticket. The default is YES.

> WILL YOU USE TRAY TICKETS?: YES// HEADING ON BOTTOM OF TICKET?: YES//

#### FH SITE PARAMETERS File (#119.9)

> Authorized Personnel: This field is a multiple and holds as many individuals a facility specifies to receive “Authorization Alerts” from unauthorized users, who request a special meal and need authorization.

> Guest Meal Classification: Sites can customize the parameters to include which type of guest meals they serve at their facility. For each class-type presented, set the field to YES or NO.

- Employee
- Paid
- OOD
- Volunteer
- Gratuitous

> Charge: A dollar amount is associated with each meal time for each Guest Meal Classification.

- Breakfast Charge
- Noon Charge
- Evening Charge

> Diet Selection (s): A site can designate up to 15 outpatient diets to be selectable for ordering outpatient meals.[<sup>1</sup>](#sm-special-meals-menu-fhomsmgr) These are the 15 most common outpatient meals served at the site, selected from the DIETS file (#111).

> The Outpatient Meals Diet1 field is the default outpatient meal diet. The fields Outpatient Meals Diet2 through Outpatient Meals Diet15 are deleted if the Outpatient Meals Diet1 field is deleted. You cannot enter data for the 2-15 Diet fields, if there is no data in the Outpatient Meals Diet1 field. Outpatient Meals Diets are edited in the FH SITE PARAMETERS file (#119.9).

- Outpatient Meals Diet1
- Outpatient Meals Diet2
- Outpatient Meals Diet3
- Outpatient Meals Diet4
- Outpatient Meals Diet5
- Through Outpatient Meals Diet15

> These 15 diets are the only diets selectable for VA outpatient nutrition locations; for Non-VA nutrition locations, select from any diet in the DIETS File.

> <span id="_bookmark167" class="anchor"></span><sup>1</sup> Patch FH\*5.5\*2 May 2007 Added ten Outpatient Meals Diets to select from the Diets file \#111.

#### NUTRITION PERSON File (#115)

> The NUTRITION PERSON file is a file that includes several fields, which assist in defining information to accommodate the outpatient meal menus, options and reports.

> The NUTRITION PERSON file (#115) contains the following sub-files.

- RECURRING MEALS
- SPECIAL MEALS
- GUEST MEALS

> The following fields are stored in the sub-fields:

- NUMBER
- DIET 1 – DIET 5
- MEAL
- BAGGED MEAL
- ADDITIONAL ORDERS
- TUBEFEEDING ORDERS

> Name: The field is a free text field and stores either "P" followed by a pointer value to File (#2) or "N" followed by a pointer value to File (#200).

#### Example

> The field stores P27 for IEN \#27 in File (#2) or this field stores N1866 for IEN \#1866 in File (#200).

> Patient: This field contains a pointer to the PATIENT file (#2), if the Nutrition Person is a patient.

> New Person: This field contains a pointer to the NEW PERSON file (#200), if the Nutrition Person is not a patient.

> Outpatient Location: This field is a pointer to the NUTRITION LOCATION file (# 119.6) to determine the person’s location.

## SM Special Meals Menu \[FHOMSMGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>RO</p>
</blockquote></th>
<th><blockquote>
<p>Request a Meal FHOMSR]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AM</p>
</blockquote></td>
<td><blockquote>
<p>Authorize a Meal [FHOMSA]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PM</p>
</blockquote></td>
<td><blockquote>
<p>Print Meal Voucher [FHOMSP]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>Cancel a Meal [FHOMSC]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS</p>
</blockquote></td>
<td><blockquote>
<p>Meal Status Report [FHOMSS]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Special Meals Menu allows access to all special meals options within the outpatient meals menu.

### RO Request a Meal \[FHOMSR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Request a Meal option allows you to prompt a patient’s name based on a search in the PATIENT file (#2). If you hold the necessary Security Key, the device prompt displays and a ticket prints with the defined default diet from the FH SITE PARAMETER file (#119.9). If you do not want the default diet, select a diet from a pull down list of diets specified in the FH SITE PARAMETER file (#119.9). If you do not hold the Security Key, the request is sent to a pre- defined list of people for approval. Once approved, an alert notifies you that a ticket is printed. When a special meal request is made, the system checks the meal window time for that selected meal, and if necessary, prompts for a late tray.

#### Example

> A breakfast meal is selected and it is within the breakfast meal window times, you are asked about ordering a late tray for that date. If it is past the breakfast window times, a message displays stating that the meal window time has passed.

> Special Meal Status: This field stores the status of the special meal request. The allowable statuses are Authorize, Deny, Cancel, and Pending.

> Special OE/RR: This field contains the number of the special meal.

> Date/Time Special Meal Ordered: This field stores the date/time the special meal was requested.

> Special Meal Location: This field stores the location for the special meal requested. This is a pointer to the NUTRITION LOCATION file (#119.6).

> Special Meal Diet: This field stores the diet for the special meal requested. This is a pointer to the DIETS file (#111).

> Special Meal Requestor: This field stores the name of the person who requested the special meal. This is a pointer to the NEW PERSON file (#200).

> Special Meal Authorizer: This field stores the name of the person who authorized the special meal. This is a pointer to the NEW PERSON file (#200).

## RM Recurring Meals Menu \[FHOMRMGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OD</p>
</blockquote></th>
<th><blockquote>
<p>Order/Edit Outpatient Meals [FHOMRO]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EL</p>
</blockquote></td>
<td><blockquote>
<p>Early/Late Tray [FHOMRE]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RO</p>
</blockquote></td>
<td><blockquote>
<p>Review Outpatient Meal [FHOMRR]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PP</p>
</blockquote></td>
<td><blockquote>
<p>Patient Profile [FHORD9]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>Cancel Outpatient Meal [FHOMRC]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AO</p>
</blockquote></td>
<td><blockquote>
<p>Additional Orders [FHOMRA]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TF</p>
</blockquote></td>
<td><blockquote>
<p>Tubefeeding [FHOMRT]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>Recurring Meal Plan Expiration List [FHOMRP]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RM</p>
</blockquote></td>
<td><blockquote>
<p>Recurring Meals List by Location [FHOMRL]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IP</p>
</blockquote></td>
<td><blockquote>
<p>Outpatient Isolation/Precaution [FHOMIP]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CA</p>
</blockquote></td>
<td><blockquote>
<p>Cancel Additional Order [FHOMRAC]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>Cancel Early/Late Tray [FHOMREC]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CT</p>
</blockquote></td>
<td><blockquote>
<p>Cancel Tubefeeding FHOMRTC]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Recurring Meal Menu allows access to all recurring meals options within the outpatient meals menu.

> Max \# of Days a Meal Plan can be Scheduled: This field is optional. If used, it sets the maximum number of days ahead a recurring meal plan can be ordered; that is, if this field is set to 365, when ordering a recurring meal, it cannot be ordered past one year from the ordering date. If the field is NULL, the default 999 days is accepted. This field checks the FROM/TO dates in the Order/Edit Outpatient Meals option.

> Number of Days for Review before Meal Plan Expires: This field is used for the Print Meal Plan Expiration option in the Recurring Meals Menu to list all patients whose meal plan is expiring within the predetermined number of days by each hospital facility.

> Recurring Meal Plan Expiration List: This report is generated by the clinic clerks for a list of patients for a specific location. Use the PT synonym to print a list of all patients whose meal plan is expiring within a specified number of days, as defined in the Nutrition Location file (#119.6).

> Non VA Facility: The field is set to ‘YES’ or ‘NO’ and is utilized if a facility is servicing Non- VA Facilities for meals. If the field is set to "Yes", the Order/Edit Outpatient Meals option uses this flag to allow selection of up to 5 diets from the DIETS file (#111). If the field is set to "NO", the Order/Edit Outpatient Meals option only allows the selection of one diet from the 5 allowable OUTPATIENT MEALS DIETS defined in the site parameters.

> Inpatient/Outpatient: This field is a set of codes ( I – Inpatient; O – Outpatient) that serve as a flag to identify, if a location is an inpatient or an outpatient location.

## GM Guest Meals Menu \[FHOMGMGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GM</p>
</blockquote></th>
<th><blockquote>
<p>Request a Meal FHOMSR]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>Print Guest Meal List [FHOMGP]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CA</p>
</blockquote></td>
<td><blockquote>
<p>Cancel a Guest Meal [FHOMGC]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Guest Meals Menu allows access to all guest meals options within the outpatient meals menu.

> Guest Meal Date/Time: This field stores the date/time that the guest meal was requested.

> Guest Meal Classification: This field stores the classification for the guest meal requested. There are five different classifications for guest meals: Employee, Gratuitous, OOD, Paid, and Volunteer.

> Guest Meal: This field stores the specific meal (breakfast, noon, or evening) for which the guest meal was requested.

> Guest Meals Report: This report summarizes by Date, Location, Classification, and Number of Meals served by Meal by Classification and cost for each.

# SM System Management \[FHSYSM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DF</p>
</blockquote></th>
<th><blockquote>
<p>Create Nutrition File entry for all Inpatients [FHX4]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DL</p>
</blockquote></td>
<td><blockquote>
<p>Update Patient Nutrition Location [FHX5]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FP</p>
</blockquote></td>
<td><blockquote>
<p>Check File Pointers [FHX3]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PD</p>
</blockquote></td>
<td><blockquote>
<p>Purge Nutrition Data [FHPURGE]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RD</p>
</blockquote></td>
<td><blockquote>
<p>Recode Diets for all Inpatients [FHX2]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RI</p>
</blockquote></td>
<td><blockquote>
<p>Check Integrity of Routines [FHX1]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SP</p>
</blockquote></td>
<td><blockquote>
<p>Modify Site Parameters (See Nutrition Facilities)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> System Management allows you to check file pointers and routine integrity, purge nutrition data, recode information, and modify site parameters.

## Managing the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are several activities which recur infrequently, but which the Nutrition ADP Coordinator is able to accomplish without disturbing the IRM staff. The System Management section contains a number of these activities. Use the options carefully because they sometimes alter the data for all patients, as well as take considerable ADP resources. Some of these options take 10-30 minutes to run to completion. Run these options during hours of light demand on the CPU.

> Two of the options, Check File Pointers (FP) and Check Integrity of Routines (RI), do not alter anything, but checks if the database and the routines (or programs) are intact. The other three options allow you to make changes to the database.

- Purge Nutrition Data (PD) eliminates data older than 400 days.
- Create Nutrition File entry for all Inpatients (DF) creates file entries when the link from MAS is down and patients are admitted without creating the required file entries.
- Recode Diets for all Inpatients (RD) is designed to recode all existing inpatients when changes are made to the PRODUCTION DIET file.

#### Running Routines

> DF Create Nutrition File entry for all Inpatients: Use when you cannot find some known inpatients in the Nutrition system.

> FP Check File Pointers: Use whenever you are experiencing undefined errors and especially if you cleaned up files by deleting entries.

> PD Purge Nutrition Data: You can run once a year to regain disk space by deleting very old data.

> RD Recode Diets for all Inpatients: Run whenever the production-diet tally order is modified or a new production diet is added, and you want the new method of tallying to be effective for existing inpatients.

> FI Check Integrity of Routines: Used by ADP staff to ascertain which routines are modified.

## DF Create Nutrition File entry for all Inpatients \[FHX4\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Create Nutrition File entry for all Inpatients option checks to see that all inpatients have a corresponding NUTRITION PERSON file entry and, if not, creates one. Any default admission diet is also ordered.

> Only run this option when you cannot select some known inpatients for Nutrition orders. Often the entries are created "on the fly" and the system discovers that some inpatients do not have file entries. Running this option is more efficient when a number of inpatients do not have file entries. The cause of this is usually the result of disabled links between the MAS database and the Nutrition database or intermittent functioning.

> Selecting the option performs the action. No additional input is required.

## DL Update Patient Nutrition Location \[FHX5\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Update Patient Nutrition Location option allows you to update the Nutrition locations for inpatients. This inserts the proper location into the NUTRITION PERSON file for the appropriate admission.

> Note: During installation, the Nutrition locations for inpatients are updated and this option updates them again.

## FP Check File Pointers \[FHX3\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Check File Pointers option is used to ensure that file entries are pointed to/used by other fields.

#### Example

> When the RECIPE file asks for equipment used in preparing a recipe, it does not store the name of the equipment. Rather, if the piece of equipment is the 11th entry in the EQUIPMENT file, the RECIPE file knows that EQUIPMENT \#11 is used. If you edited the EQUIPMENT file and removed item 11, the RECIPE file has no idea which piece of equipment was originally referred to. This can cause undefined errors and for this reason, entries are normally inactivated rather than deleted.

> This option checks whether or not an entry was deleted, but is still pointed to by other files.

> Verify Inpatient Data: You can select whether or not file pointers are checked for the entire NUTRITION PERSON file, only inpatients, or no patients at all. The NUTRITION PERSON file contains a number of pointers to diets, supplemental feedings, supplemental feeding menus, isolation types, etc. You should probably check only inpatients. All other files are checked completely.

> Type A, I, or N.

- A – all admitted to the hospital
- I – current inpatient only
- N – non-patient files only

> If any entries indicate something is missing, correct them by editing the file. In the example, the ingredient CAKE, COFFEE points to Vendor 3. There is no way of knowing who that was, because the entry in the FH VENDOR file (#113.2) is missing. Edit the Vendor field in the INGREDIENT file (# 113) by using the Enter/Edit Ingredients option in the Ingredient Management menu and enter an existing vendor.

> Note: The default name for Vendor is 3. When the vendor name is not found, its internal number is used. Ignore this and select a new vendor name.

## PD Purge Nutrition Data \[FHPURGE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Purge Nutrition Data option purges old Nutrition data. It completely deletes the data and does not archive it in any way. Once deleted, it is gone. As determined by Nutrition and Food Service officials in VA Central Office, delete data only if it is at least 400 days (about 13 months) since the discharge of the patient. You can retain data longer, but do not delete data that is more recent than 400 days, and do not delete data selectively through this option.

> Purge To: This field defaults back to the date 400 days ago. However, you can select an earlier date than this. The default date is 400 days prior to today. Accept the default date or enter a date prior to the default.

> Requested Start Time: This is the time to begin the purge process. The start time default is NOW, but you can enter a later time. The request to purge nutrition data is queued, because it is a time consuming process. Press \<RET\> to accept a start time of NOW or enter a date and time greater than NOW.

## RD Recode Diets for all Inpatients \[FHX2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Recode Diets for all Inpatients option allows you to specify the order in which to tally production diets. The PRODUCTION DIET file \#116.2 sets a tally order for production diets and creates combination production diets, which are groups of single production diets. The coding of the clinical diet order into the appropriate production diet occurs at the time of the order entry.

> Changing the tally order does not affect existing inpatient orders, but only orders entered from now on. In order to recode existing inpatient diet orders according to some new tally order, it is necessary to run this option. No input is required. Selecting the option causes a recode of all existing inpatient diet orders.

> Note: When you run this option, you may receive a message like:

> DOE,JOHN, Admission "#", Diet Order 2 not recoded

> If it is not a current admission, you can ignore it. If it is a current admission, you need to reorder the diet for the patient.

## RI Check Integrity of Routines \[FHX1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Check Integrity of Routines option verifies that the various Nutrition routines are not altered since distribution. It is important to recognize that official patches, as well as local modifications cause a routine to be flagged as altered. This is a means of learning whether official patches were installed or whether any modifications were made to the software.

> The output is a list of the routine names.

> In the example, any routine name followed by “off by nnnn” was modified.

# XF File Manager \[FHFILM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FD</p>
</blockquote></th>
<th><blockquote>
<p>File Dictionaries [FHFIL4]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IE</p>
</blockquote></td>
<td><blockquote>
<p>Inquire to Files [FHFIL3]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PE</p>
</blockquote></td>
<td><blockquote>
<p>Print File Entries [FHFIL1]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SE</p>
</blockquote></td>
<td><blockquote>
<p>Search File Entries FHFIL2]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> File Manager allows you to print entries in Nutrition and Food Service files, as well as file dictionaries.

> For more information, refer to the latest version of the *VA FileMan User Manual*.

## FD File Dictionaries \[FHFIL4\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The File Dictionaries option is used to look at the field definitions and help text:

- Date/Time: A date field with or without a time entry
- Number: A numeric value
- Set of Codes: A listing of the only choices available
- Free Text: A specified number of characters
- Word Processing: Usually an unlimited number of characters
- Computed: A value that is not stored by this file

> (e.g. Patient SSN or birth date is usually a computed field. It is stored in another file and is not subject to change.)

- Pointer: References/uses an entry from another file
- Variable Pointer: References/uses an entry from more than one file

> Select File Manager Option: File Dictionaries

> START WITH WHAT FILE: MENU CYCLE// recip

1.  RECIPE (507 entries)
2.  RECIPE CATEGORY (61 entries) CHOOSE 1-2: 1

> GO TO WHAT FILE: RECIPE// \<RET\>

> Select SUB-FILE: ?

> Answer with FIELD NUMBER, or LABEL

> Do you want the entire FIELD List? y (Yes) Choose from:

> 1 INGREDIENT

> 1.5 EMBEDDED RECIPE

> 5 EQUIPMENT

> 20 DIRECTIONS

> 103 DIABETIC EXCHANGE

> Select SUB-FILE: \<RET\>

> Select LISTING FORMAT: STANDARD// ?

> Answer with LISTING FORMAT NUMBER, or NAME Choose from:

1.  STANDARD
2.  BRIEF
3.  CUSTOM-TAILORED
4.  MODIFIED STANDARD
5.  TEMPLATES ONLY
6.  GLOBAL MAP
7.  CONDENSED

> Select LISTING FORMAT: STANDARD// 2 BRIEF ALPHABETICALLY BY LABEL? No// \<RET\> (No)

> DEVICE: \<RET\> HYPER SPACE RIGHT MARGIN: 80// \<RET\>

> BRIEF DATA DICTIONARY \#114 -- RECIPE FILE 05/9/05 PAGE 1 SITE: HISC UCI: DIE,PAY (VERSION 5.0)

> 7

> NAME 114,.01 FREE TEXT

> 0

> ANSWER MUST BE 3-30 CHARACTERS IN LENGTH

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 46%" />
<col style="width: 10%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>INGREDIENT</p>
<p>Multiple</p>
</blockquote></th>
<th></th>
<th></th>
<th>114,1 114.01 POINTER</th>
<th></th>
<th rowspan="22"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>INGREDIENT</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114.01,.01 POINTER</p>
<p>TO INGREDIENT FILE (#113)</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>QUANTITY</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114.01,1 NUMBER</p>
<p>Enter Quantity in proper units</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ASSOCIATED NUTRIENT</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114.01,2 POINTER</p>
<p>TO FOOD NUTRIENTS FILE (#112)</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NUTRIENT AMOUNT IN</p>
</blockquote></th>
<th>LBS.</th>
<th></th>
<th>114.01,3 NUMBER</th>
<th></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>Type a Number between 0 and 9999, 5 Decimal Digits</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>EMBEDDED RECIPE</p>
<p>Multiple</p>
</blockquote></th>
<th></th>
<th></th>
<th>114,1.5 114.03 POINTER</th>
<th></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>EMBEDDED RECIPE 114.03,.01 POINTER TO RECIPE FILE (#114)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>BRIEF DATA DICTIONARY #114 -- RECIPE FILE 05/9/05 PAGE 2 SITE: HISC UCI: DIE,PAY (VERSION 5.0)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>NO. OF PORTIONS 114.03,1 NUMBER</p>
<p>TYPE A NUMBER BETWEEN 0 AND 9999</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NUMBER OF PORTIONS</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114,2 NUMBER</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>Type a Number between 1 and 1000, 0 Decimal Digits</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PORTION SIZE</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114,3 FREE TEXT</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>ANSWER MUST BE A NUMBER FOLLOWED BY OZ, FLOZ OR EACH</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PREPARATION TIME</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114,4 FREE TEXT</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>ANSWER MUST BE 1-10 CHARACTERS IN LENGTH</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>EQUIPMENT</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114,5 114.05 POINTER</p>
<p>Multiple</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>EQUIPMENT</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114.05,.01 POINTER</p>
<p>TO EQUIPMENT FILE (#114.4)</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>SERVING UTENSIL 114,6 POINTER</p>
<p>TO SERVING UTENSIL FILE (#114.3)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>DEFAULT CATEGORY 114,7 POINTER</p>
<p>TO RECIPE CATEGORY FILE (#114.1)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>BRIEF DATA DICTIONARY #114 -- RECIPE FILE 05/9/05 PAGE 3 SITE: HISC UCI: DIE,PAY (VERSION 5.0)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SYNONYM</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>114,8 FREE TEXT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 64%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>ANSWER MUST BE 3-25 CHARACTERS IN LENGTH</p>
</blockquote></th>
<th rowspan="15"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p># DAYS PRE-PREP 114,9 NUMBER</p>
<p>TYPE A WHOLE NUMBER BETWEEN 0 AND 3</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>PRINT RECIPE 114,10 SET</p>
<p>'Y' FOR YES; 'N' FOR NO;</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>PRE-PREP STATE 114,11 SET</p>
<p>'M' FOR MIX;</p>
<p>'D' FOR DEHYDRATED; 'F' FOR FROZEN;</p>
<p>'C' FOR CANNED;</p>
<p>'X' FOR CONCENTRATED; 'S' FOR SCRATCH;</p>
<p>'I' FOR IND/R-T-S;</p>
<p>'P' FOR PARTIALLY PREP; 'R' FOR R-T-S;</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>PREPARATION AREA 114,12 POINTER</p>
<p>TO PREPARATION AREA FILE (#114.2)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>DIRECTIONS 114,20 114.02 WORD-PROCESSING</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>ANSWER MUST BE 1-80 CHARACTERS IN LENGTH</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>COST/PORTION 114,101 NUMBER</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Type a Number between .001 and 30, 3 Decimal Digits</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>ASSOCIATED NUTRIENT ANALYSIS 114,102 POINTER</p>
<p>TO FOOD NUTRIENTS FILE (#112)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>BRIEF DATA DICTIONARY #114 -- RECIPE FILE 05/9/05 PAGE 4 SITE: HISC UCI: DIE,PAY (VERSION 5.0)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>DIABETIC EXCHANGE</p>
<p>Multiple</p>
</blockquote></th>
<th><blockquote>
<p>114,103 114.0103 POINTER</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>DIABETIC EXCHANGE</p>
</blockquote></th>
<th><blockquote>
<p>114.0103,.01 POINTER</p>
<p>TO RECIPE CATEGORY FILE (#114.1)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>QUANTITY</p>
</blockquote></th>
<th><blockquote>
<p>114.0103,1 NUMBER</p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
<th><blockquote>
<p>Type a Number between 1 and 5, 0 Decimal Digits</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## IE Inquire to Files \[FHFIL3\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inquire to Files option provides a quick look at all the data for a specific entry in a file.

## PE Print File Entries \[FHFIL1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Print File Entries option allows you to select from a file, the fields by which to sort and print the data. For more information on using the print option, refer to the latest version of the *VA FileMan User Manual*.

> Select File Manager Option: Print File Entries

> OUTPUT FROM WHAT FILE: recipe

1.  RECIPE
2.  RECIPE CATEGORY CHOOSE 1-2: 1

> SORT BY: NAME// ??

> Choose from:

> .01 NAME

1.  INGREDIENT (multiple)

> 1.5 EMBEDDED RECIPE (multiple)

2.  NUMBER OF PORTIONS
3.  PORTION SIZE
4.  PREPARATION TIME
5.  EQUIPMENT (multiple)
6.  SERVING UTENSIL
7.  DEFAULT CATEGORY
8.  SYNONYM
9.  \# DAYS PRE-PREP
10. PRINT RECIPE
11. PRE-PREP STATE
12. PREPARATION AREA
101. COST/PORTION
102. ASSOCIATED NUTRIENT ANALYSIS
103. DIABETIC EXCHANGE (multiple)

> TYPE '-' IN FRONT OF NUMERIC-VALUED FIELD TO SORT FROM HI TO LO TYPE '+' IN FRONT OF FIELD NAME TO GET SUBTOTALS BY THAT FIELD,

> '#' TO PAGE-FEED ON EACH FIELD VALUE, '!' TO GET RANKING NUMBER, '@' TO SUPPRESS SUB-HEADER, '\]' TO FORCE SAVING SORT TEMPLATE

> TYPE ';TXT' AFTER FREE-TEXT FIELDS TO SORT NUMBERS AS TEXT

> TYPE \[TEMPLATE NAME\] IN BRACKETS TO SORT BY PREVIOUS SEARCH RESULTS

> SORT BY: NAME// \<RET\>

> START WITH NAME: FIRST// \<RET\>

> FIRST PRINT FIELD: ??

> Choose from:

> .01 NAME

1.  INGREDIENT (multiple)

> 1.5 EMBEDDED RECIPE (multiple)

2.  NUMBER OF PORTIONS
3.  PORTION SIZE
4.  PREPARATION TIME
5.  EQUIPMENT (multiple)
6.  SERVING UTENSIL
7.  DEFAULT CATEGORY
8.  SYNONYM
9.  \# DAYS PRE-PREP
10. PRINT RECIPE
11. PRE-PREP STATE
12. PREPARATION AREA

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 43%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>20 DIRECTIONS (word-processing)</p>
</blockquote>
<ol start="101" type="1">
<li><p>COST/PORTION</p></li>
<li><p>ASSOCIATED NUTRIENT ANALYSIS</p></li>
<li><p>DIABETIC EXCHANGE (multiple)</p></li>
</ol></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>TYPE '&amp;' IN FRONT OF FIELD NAME TO GET TOTAL FOR THAT FIELD,</p>
<p>'!' TO GET COUNT, '+' TO GET TOTAL &amp; COUNT, '#' TO GET MAX &amp; MIN, ']' TO FORCE SAVING PRINT TEMPLATE</p>
<p>TYPE '[TEMPLATE NAME]' IN BRACKETS TO USE AN EXISTING PRINT TEMPLATE YOU CAN FOLLOW FIELD NAME WITH ';' AND FORMAT SPECIFICATION(S)</p>
<p>FIRST PRINT FIELD: <strong>1</strong> INGREDIENT (multiple) FIRST PRINT INGREDIENT SUB-FIELD: <strong>?</strong></p>
<p>Answer with INGREDIENT SUB-FIELD NUMBER, or LABEL</p>
<p>Choose from:</p>
<p>.01 INGREDIENT</p>
</blockquote>
<ol type="1">
<li><p>QUANTITY</p></li>
<li><p>ASSOCIATED NUTRIENT</p></li>
<li><p>NUTRIENT AMOUNT IN LBS.</p></li>
</ol></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>TYPE '&amp;' IN FRONT OF FIELD NAME TO GET TOTAL FOR THAT FIELD,</p>
<p>'!' TO GET COUNT, '+' TO GET TOTAL &amp; COUNT, '#' TO GET MAX &amp; MIN, ']' TO FORCE SAVING PRINT TEMPLATE</p>
<p>TYPE '[TEMPLATE NAME]' IN BRACKETS TO USE AN EXISTING PRINT TEMPLATE YOU CAN FOLLOW FIELD NAME WITH ';' AND FORMAT SPECIFICATION(S)</p>
<p>FIRST PRINT INGREDIENT SUB-FIELD: <strong>.01</strong> INGREDIENT THEN PRINT INGREDIENT SUB-FIELD: <strong>&lt;RET&gt;</strong></p>
<p>THEN PRINT FIELD: <strong>dir</strong>ECTIONS (word-processing) THEN PRINT FIELD: <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>* Heading (S/C): RECIPE LIST// <strong>&lt;RET&gt;</strong></p>
<p>DEVICE: <strong>&lt;RET&gt;</strong> HYPER SPACE RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>RECIPE LIST MAY 9,2005 10:29 PAGE 1 INGREDIENT DIRECTIONS</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NAME: APPLE JUICE, 4OZ IND JUICE, APPLE, FROZEN, UNSW, IND</p>
</blockquote></th>
<th><blockquote>
<p>PLACE 4-OZ THAWED CONTAINER OF JUICE ON TRAY.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NAME: APPLE JUICE, 6OZ IND JUICE, APPLE, CND, UNSW, IND</p>
<p>NAME: APPLE JUICE, BULK JUICE, APPLE, CND</p>
</blockquote></th>
<th><blockquote>
<p>PLACE ON CAN ON TRAY.</p>
<p>PORTION INTO 4-OZ SERVING.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NAME: APPLE PIE PIE, APPLE, FZN</p>
<p>NAME: APPLESAUCE APPLESAUCE, CND, SWEETENED</p>
</blockquote></th>
<th><blockquote>
<p>CUT PIE IN EIGHTHS.</p>
<p>1) PORTION INTO SERVING DISHES. COVER AND CHILL TO SERVE.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## SE Search File Entries \[FHFIL2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Search File Entries option provides a way to select file entries that meet a predetermined set of criteria. You need to identify the file, describe the search criteria, specify the combinations of logic for the search, and specify the fields to print. The example contains a search for all recipes that do not contain directions.

> Example

<table>
<colgroup>
<col style="width: 78%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>START WITH NAME: FIRST// <strong>&lt;RET&gt;</strong></p>
<p>FIRST PRINT FIELD: <strong>name</strong></p>
<p>THEN PRINT FIELD: <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>*</p>
<p>Heading (S/C): RECIPE SEARCH// <strong>&lt;RET&gt;</strong></p>
<p>DEVICE: <strong>&lt;RET&gt;</strong> HYPER SPACE RIGHT MARGIN: 80// <strong>&lt;RET&gt;</strong></p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>RECIPE SEARCH MAY 9,2005 10:44</p>
<p>NAME</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>AGAIN</p>
<p>APPLE JELLY DIET, IND APPLE JELLY, IND APRICOT DIET JELLY, IND</p>
<p>ASSORTED DIET JELLY, IND BAKED APPLES</p>
<p>BANANA IND</p>
<p>BLACKBERRY DIET JELLY, IND BLACKBERRY JAM, IND BLACKBERRY JELLY, IND</p>
<p>BLUE 2 CONDIMENT PK</p>
<p>BLUE CHEESE DRESSING, IND BLUE CONDIMENT PK</p>
<p>BUTTER PAT CATSUP, DIET IND</p>
<p>CHEERIOS CEREAL, IND</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Acronym</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ADP</p>
</blockquote></td>
<td><blockquote>
<p>Automated Data Processing or Automated Data Processing Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADTS</p>
</blockquote></td>
<td><blockquote>
<p>MAS software: Admissions, Discharge, Transfer, Scheduling Nutrition's software requires that ADTS be running effectively.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AMIS</p>
</blockquote></td>
<td><blockquote>
<p>Automated Management Information System - a VA wide centralized database</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CAHG</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Ad Hoc Group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCOW</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Context Object Workgroup</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRT</p>
</blockquote></td>
<td><blockquote>
<p>Cathode Ray Tube; refers to the terminal screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPU</p>
</blockquote></td>
<td><blockquote>
<p>Central Processing Unit; a major unit of the computer containing the arithmetic unit, main memory, and control unit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HL7</p>
</blockquote></td>
<td><blockquote>
<p>Health Level 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HSD&amp;D</p>
</blockquote></td>
<td><blockquote>
<p>Health System Design and Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IMG</p>
</blockquote></td>
<td><blockquote>
<p>Information Management Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IRM</p>
</blockquote></td>
<td><blockquote>
<p>Information Resource Management</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ISC</p>
</blockquote></td>
<td><blockquote>
<p>Information Systems Center; ISCs are software development centers for VA software applications</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LAYGO</p>
</blockquote></td>
<td><blockquote>
<p>Learn as the user go; allows all users to add to the existing files</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAS</p>
</blockquote></td>
<td><blockquote>
<p>Medical Administration Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MIRMO</p>
</blockquote></td>
<td><blockquote>
<p>Medical Information Research Management Office at VACO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NNAB</p>
</blockquote></td>
<td><blockquote>
<p>National Nutrition Advisory Board</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ODD</p>
</blockquote></td>
<td><blockquote>
<p>Officer of the Day</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OINT</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information National Training and Education Office</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PCE</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Encounter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information Management Systems</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PMO</p>
</blockquote></td>
<td><blockquote>
<p>Project Management Office</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SI</p>
</blockquote></th>
<th><blockquote>
<p>System Implementation</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Veteran Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VACO</p>
</blockquote></td>
<td><blockquote>
<p>VA Central Office, Washington DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VAMC</p>
</blockquote></td>
<td><blockquote>
<p>VA Medical Center</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VDT</p>
</blockquote></td>
<td><blockquote>
<p>Video display terminal; same as terminal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WOC</p>
</blockquote></td>
<td><blockquote>
<p>Without Compensation</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Terms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An individual's code used to gain entry to the computer system
> A person in the Information Resource Management service who answers questions
> A person selected in each medical center's services who has the responsibility for the implementation/coordination of the ADP activities
> A copy of a file or information kept as a reference in case the original file is destroyed or unavailable
> Methods of accomplishing work, if the computer is not functioning. The smallest unit of storage in the computer
> The Nutrition Service quarterly computer newsletter An error in a program or a system
> The smallest addressable unit of storage of data; eight bits
> A letter, digit, space, or other symbol used as part of the representation of data
> A system of symbols and rules for use in representing information, or a series of letters used as part of a security code system, for gaining access to the computer system
> A request entered on a terminal to have a function performed; e.g., a printer command
> An electronic device for performing high speed arithmetic and logical operation
> A system composed of a computer, peripheral equipment, such as disks, printers, and terminals, and the software necessary to make them operate together
> Symbols or commands common to VA software
> A hardware or software failure that leads to an abnormal cessation of processing
> A highlighted mark displaying on the CRT; a bright square or underscore character that indicates where the next entry on the keyboard is recorded on the CRT
> Characters arranged together in specific patterns, to which meaning is assigned; information
> A large file of organized data that users draw upon as a common pool of information
> A collection of information about the contents of each file, which includes such information as data type, minimum and maximum length of the entry, and other files and pointers. Also called DD.
> An answer or response entered automatically into the computer program if no response is provided; is usually shown before the slashes, e.g., Name: Gingerale//
> To remove data from the system
> In Nutrition Software programs, refers to the selection of the terminal display or the printer for receiving the output; may refer to any hardware
> A platter, similar to a phonograph record, coated with a magnetic surface on which data is stored
> A small disk
> A collection of descriptions or procedures, which provide information about a program, so that it can be used properly and maintained
> To generate a printout of a file from main memory at a given point in time
> To correct, rearrange, and validate input data. To modify the form of output information by inserting blank spaces, special characters where needed, etc.
> A general term to describe the transmission of messages by the use of computing systems and telecommunications facilities
> Key on the keyboard used at the end of a data entry or command to indicate that you finished the entry. Same as the return key on some terminals
> In a record, a specific area used for a particular category of data A collection of related records, treated as a unit
> A database management system developed by the Veterans Administration. Also referred to as VA FileMan
> A variable used in a program to indicate whether a condition has or has not occurred
> Global Variable - refers to variables that are permanently stored on disk.
> Printed copy of data stored in the computer
> The physical equipment that makes up a computer system
> Enter ?, ??, or ??? and an explanation or choices shows on the screen Data that is submitted to the computer for processing
> A shared boundary between two devices, systems, or programs
> The person at each VA Medical Center who is responsible for all IRM functions
> A collection of specific tasks constituting a unit of work for a computer
> A departure from sequence in executing instructions in a computer
> The set of utilities, which perform the tasks of the VA computer system, including Menu Manager, Task Manager, Device Handler, the security system and specialized routines
> A device with an arrangement of keys like those on a typewriter; often includes a second set of numbers similar to a calculator pad
> 1024 bytes; refers to computer storage capacity
> Use of the programs with real persons as opposed to the test account
> A variable that exists only in memory and is lost when exiting the program
> The process of exiting from the computer system The process of entering the computer system
> An electronic mail program that enables users to send memos, letters, messages, documents from one computer terminal to another
> A large computer capable of supporting many peripheral devices and users
> One million bytes; or 1000 kilobytes A device for storage of data
> A list of choices presented by the software that represent a decision point in the running of the program
> Contraction of modulator-demodulator, a device that transmits signals over a communications line
> Massachusetts General Hospital Utility Multi-Programming System; a high level (source) computer language especially convenient for manipulating textual data
> The absence of information
> List/menu of choices of available programs; a single choice in the list Information that comes from the computer after processing
> A code used for gaining access to the computer system; may be referred to as access and verify codes
> The modification of a program in an expedient way
> An address that specifies a storage location where data can be stored or retrieved
> A connection between CPU and another device, by means of which data can enter or leave the computer
> A device to produce permanent (hard copy) computer output
> A message on the display terminal requiring input from the user
> A logically arranged set of instructions defining the operations to be performed by the computer
> Positioning behind other work; used in directing output work to a printer
> The process of accessing information previously stored by the computer
> Same as a program
> Process of exiting the computer system Process of entering the computer system
> A setting in a program that is decided upon and then left for the use of the program
> A formula developed to determine the equipment and CPU needs of a service
> A set of computer programs associated with the operation of a data processing system
> To retain data for future use
> A device used by a person to send data and to receive data from the computer
> An account in which the software is run before it is used live; is used to set up files, training, and practice
> Persons who use the computer system
> Same as Nutrition and Food Service User Manual, if referring to Nutrition and Food Service programs
> A program that performs many tasks of the computer system; Kernel in VistA is the utility that provides data processing support for the software programs
> Series of letters; part of the security code used for accessing the computer
> Various releases or editions of the Nutrition and Food Service software programs; new versions have a higher number and replace earlier ones
> The use of computers to create, view, edit, store, retrieve, and print text material
