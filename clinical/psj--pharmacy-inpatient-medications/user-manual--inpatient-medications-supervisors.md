---
title: Inpatient Medications Supervisor's User Manual (PSJ*5.0*447)
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: null
app_code: PSJ
app_name: 'Pharmacy: Inpatient Medications'
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5.0
patch_id: PSJ*5.0*447
group_key: PSJ:PSJ:5.0
file_numbers:
- '3'
- '6'
- '42'
- '50'
- '50.2'
- '50.4'
- '50.68'
- '50.8'
- '51'
- '51.1'
- '51.2'
- '52.6'
- '52.7'
- '53.45'
- '53.46'
- '57.5'
- '57.7'
- '59.5'
- '59.6'
- '59.7'
- '100'
- '900903'
security_keys:
- GMRA VERIFIER
- PROVIDER
- PSJ PADE ADV
- PSJ PHARM TECH
- PSJ RNURSE
- PSJ RPHARM
- PSJI MGR
- PSJI PURGE
- PSJU MGR
- PSJU PL
menu_options: 1
description: The Inpatient Medications package provides a method of management, dispensing, and administration of inpatient drugs within the hospital. Inpatient Medications combines clinical and patient information that allows each medical center to enter orders for patients, dispense medications by means of Pic
audience: End users (clinical / administrative, per package)
keywords: []
page_count: 0
word_count: 33840
section_count: 26
table_count: 4
figure_count: 7
appendix_count: 1
has_toc: false
is_stub: false
pub_date: December 1997
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/PSJ_5_0_p447_SUPR_UM.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/PSJ_5_0_p447_SUPR_UM.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=88
audit_applied: '2026-05-31'
master_source: Inpatient Medications Supervisor's User Manual (PSJ*5.0*447)
master_pub_date: December 1997
consolidated_from: 2 versions
prior_versions:
- Inpatient Medications Version 5 Supervisor's User Manual (Updated PSJ*5*423)
consolidated_title: inpatient medications supervisor's user manual
---

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/001.png)INPATIENT MEDICATIONSSUPERVISOR'S USER MANUAL

December 1997

<span id="Title_Page" class="anchor"></span>(Revised August 2025)

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Orientation](#orientation)
- [Supervisor's Menu](#supervisors-menu)
  - [Administering Teams](#administering-teams)
  - [Clinic Definition](#clinic-definition)
    - [Pre-Exchange Printer for Clinic Orders](#pre-exchange-printer-for-clinic-orders)
  - [Clinic Groups](#clinic-groups)
  - [MANagement Reports Menu](#management-reports-menu)
    - [AMIS (Cost per Ward)](#amis-cost-per-ward)
    - [Drug (Cost and/or Amount)](#drug-cost-andor-amount)
    - [Patients on Specific Drug(s)](#patients-on-specific-drugs)
    - [PRovider (Cost per)](#provider-cost-per)
    - [Service (Total Cost per)](#service-total-cost-per)
    - [Total Cost to Date (Current Patients)](#total-cost-to-date-current-patients)
  - [Non-Standard Schedule Report](#non-standard-schedule-report)
  - [Non-Standard Schedule Search](#non-standard-schedule-search)
  - [Order Set Enter/Edit](#order-set-enteredit)
  - [PARameters Edit Menu](#parameters-edit-menu)
    - [AUto-Discontinue Set-Up](#auto-discontinue-set-up)
    - [Inpatient User Parameters Edit](#inpatient-user-parameters-edit)
    - [Inpatient Ward Parameters Edit](#inpatient-ward-parameters-edit)
    - [Systems Parameters Edit](#systems-parameters-edit)
  - [PATient Order Purge – Temporarily Unavailable](#patient-order-purge-temporarily-unavailable)
  - [PIck List Menu](#pick-list-menu)
    - [DElete a Pick List](#delete-a-pick-list)
    - [PIck List Auto Purge Set/Reset](#pick-list-auto-purge-setreset)
    - [PUrge Pick Lists](#purge-pick-lists)
  - [Ward Groups](#ward-groups)
- [SUPervisor's Menu (IV)](#supervisors-menu-iv)
  - [AUto-Discontinue Set-Up](#auto-discontinue-set-up-1)
  - [CAtegory File (IV)](#category-file-iv)
  - [COmpile IV Statistics (IV)](#compile-iv-statistics-iv)
  - [Management Reports (IV)](#management-reports-iv)
    - [ACtive Order Report by Ward/Drug (IV)](#active-order-report-by-warddrug-iv)
    - [AMIS (IV)](#amis-iv)
    - [Drug Cost Report (132 COLUMNS) (IV)](#drug-cost-report-132-columns-iv)
    - [Patient Cost Report (132 COLUMNS) (IV)](#patient-cost-report-132-columns-iv)
    - [Patients on Specific Drug(s)](#patients-on-specific-drugs-1)
    - [PROvider Drug Cost Report (132 COLUMNS) (IV)](#provider-drug-cost-report-132-columns-iv)
    - [Ward/Drug Usage Report (132 COLUMNS) (IV)](#warddrug-usage-report-132-columns-iv)
  - [PUrge Data (IV) – Temporarily Unavailable](#purge-data-iv-temporarily-unavailable)
    - [Delete Orders (IV) – Temporarily Unavailable](#delete-orders-iv-temporarily-unavailable)
    - [Purge Expired Orders (IV) – Temporarily Unavailable](#purge-expired-orders-iv-temporarily-unavailable)
  - [Recompile Stats File (IV)](#recompile-stats-file-iv)
  - [SIte Parameter (IV)](#site-parameter-iv)
- [Order Checks](#order-checks)
  - [Allergy Order Checks](#allergy-order-checks)
  - [CPRS Order Checks](#cprs-order-checks)
  - [Clinical Reminder Order Checks](#clinical-reminder-order-checks)
  - [Enhanced Order Checks](#enhanced-order-checks)
    - [Duplicate Therapy Order Checks](#duplicate-therapy-order-checks)
    - [Drug/Drug Interaction Order Checks](#drugdrug-interaction-order-checks)
    - [Dosing Order Checks](#dosing-order-checks)
    - [Pharmacogenomic Order Checks](#pharmacogenomic-order-checks)
    - [Clinic Orders](#clinic-orders)
    - [Dosing Order Checks](#dosing-order-checks-1)
    - [Order Check Data Caching](#order-check-data-caching)
    - [Display of Provider Overrides and Pharmacist Interventions](#display-of-provider-overrides-and-pharmacist-interventions)
- [Check Drug Interactions](#check-drug-interactions)
- [Check Pharmacogenomic Interactions](#check-pharmacogenomic-interactions)
- [Pharmacy Interface Automation](#pharmacy-interface-automation)
  - [Displaying PADE Balances](#displaying-pade-balances)
  - [Reports](#reports)
- [Error Messages](#error-messages)
  - [Error Information](#error-information)
- [Glossary](#glossary)
- [Index](#index)
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2025</td>
<td>Title, <a href="#order-checks">60</a>, <a href="#Order_Level_Errors">61</a>, <a href="#allergy-order-checks">62</a>, <a href="#cprs-order-checks">63</a>, <a href="#clinical-reminder-order-checks">65</a>, <a href="#enhanced-order-checks">67</a>, <a href="#drugdrug-interaction-order-checks">69</a>, <a href="#dosing-order-checks">71</a>, <a href="#pharmacogenomic-order-checks">72</a>, <a href="#error-messages">88</a>, <a href="#Gene">96</a>, <a href="#PGx_Definition">99</a></td>
<td>PSJ*5*447</td>
<td><ul>
<li><p>Deleted Section 4.8 Dosing Order Checks</p></li>
<li><p>Added Section 5 <a href="#order-checks">Order Checks</a></p></li>
<li><p>Added <a href="#Order_Level_Errors">Order Level Errors</a> to Display of Order Checks</p></li>
<li><p>Updated Section 5.1 <a href="#allergy-order-checks">Allergy Order Checks</a></p></li>
<li><p>Updated Section 5.2 <a href="#cprs-order-checks">CPRS Order Checks</a></p></li>
<li><p>Updated Section 5.3 <a href="#clinical-reminder-order-checks">Clinical Reminder Order Checks</a></p></li>
<li><p>Updated Section 5.4 <a href="#enhanced-order-checks">Enhanced Order Checks</a></p></li>
<li><p>Updated Section 5.4.1 <a href="#duplicate-therapy-order-checks">Duplicate Therapy Order Checks</a></p></li>
<li><p>Updated Section 5.4.2 <a href="#drugdrug-interaction-order-checks">Drug/Drug Interaction Order Checks</a></p></li>
<li><p>Updated Section 5.4.3 <a href="#dosing-order-checks">Dosing Order Checks</a></p></li>
<li><p>Updated Section 5.4.4 <a href="#pharmacogenomic-order-checks">Pharmacogenomic Order Checks</a></p></li>
<li><p>Updated Section 9 <a href="#error-messages">Error Message</a></p></li>
<li><p>Added <a href="#Gene">Gene</a> definition to Glossary</p></li>
<li><p>Added <a href="#Genotype">Genotype</a> definition to Glossary</p></li>
<li><p>Added <a href="#PGx_Definition">Pharmacogenomic</a> definition to Glossary</p></li>
<li><p>Added <a href="#Phenotype">Phenotype</a> definition to Glossary</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul></td>
</tr>
<tr class="even">
<td>05/2025</td>
<td>Title, 69, 70</td>
<td>PSJ*5*423</td>
<td><ul>
<li><p>Updated <u>Error Information</u> with new <u>System</u> and <u>Drug</u> error messages</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>03/2025</td>
<td><p><a href="#opioid_2">6</a></p>
<p><a href="#opioid_3">73</a></p></td>
<td>PSJ*5*445</td>
<td><ul>
<li><p>Added <a href="#opioid_2">Opioid Treatment Clinic</a> to Clinic Definition</p></li>
<li><p>Modified Clinic Definition File Glossary entry to include <a href="#opioid_3">Opioid Treatment Clinic</a></p></li>
</ul></td>
</tr>
<tr class="even">
<td>03/2023</td>
<td>Title, i, 58, 73</td>
<td>PSJ*5*407</td>
<td><ul>
<li><p>Added Coverage Times <strong><u>Note</u></strong> in the Site Parameter (IV) section</p></li>
<li><p>Added Coverage Times <strong><u>Note</u></strong> in the Glossary section</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>09/2020</td>
<td><p><a href="#P6">6</a></p>
<p><a href="#P66">66</a></p>
<p><a href="#CM_New_Clinic_Medication">70</a>, <a href="#Glossary_CM_New_Clinic_Medication_Entry">73</a></p>
<p>Global</p></td>
<td>PSJ*5*319</td>
<td><p>Added <a href="#P6">CLINIC APPT DATE RANGE MIN</a>, and <a href="#CLINIC_APPT_DATE_RANGE_MAX">CLINIC APPT DATE RANGE MAX</a> to Clinic Definitions</p>
<p>Added <a href="#CM_New_Clinic_Medication_Entry_Example">CM New Clinic Medication Entry</a> to Order Entry examples. Also added Note describing the CM New Clinic Medication action below the example</p>
<p>Glossary: Under <a href="#CM_New_Clinic_Medication"><strong>Patient/Order Action Prompts</strong></a>, added CM New Clinic Medication Entry. Also added <a href="#Glossary_CM_New_Clinic_Medication_Entry">a definition of CM New Clinic Medication Entry</a>.</p>
<p>Updated Title Page, Footer, and Revision History</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/2020</td>
<td>Title, i, 18, all</td>
<td>PSJ*5*394</td>
<td><ul>
<li><p>Added <strong>Note:</strong> <strong>Note:</strong> <strong><u>Note:</u></strong></p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td><span id="Revision_History" class="anchor"></span>09/2018</td>
<td><p><a href="#Title_Page">Title Page</a>, <a href="#Revision_History">Revision History</a>, and <a href="\l">i</a></p>
<p><a href="#Inpatient_Order_Entry">65</a></p>
<p><a href="#Orphan_Bullet">3</a>, <a href="#Orphan_Paragraph_Title">43</a>, and <a href="#EX_PSJI_AOR">45</a></p></td>
<td>PSJ*5*373</td>
<td><p>Updated Title Page, Footer, and Revision History</p>
<p>Corrected date so year is displayed with four digits for Inpatient Order Entry.</p>
<p>Orphan bullet and example titles.</p></td>
</tr>
<tr class="even">
<td>02/2018</td>
<td><p>58</p>
<p>64</p>
<p>69</p></td>
<td>PSJ*5*256</td>
<td><p>Updated Section 4.8 Dosing Order Checks</p>
<p>Updated Section 6.1 Displaying PADE Balances - Updated Patient Header Info Display</p>
<p>Updated Error Message Table – Added System Level Error</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>10/2016</td>
<td><p>i-vi</p>
<p>65</p>
<p>65</p>
<p>67</p></td>
<td>PSJ*5*317</td>
<td><p>Updated Revision History and Table of Contents</p>
<p>Added section 6: Pharmacy Interface Automation</p>
<p>Added 6.1 Displaying PADE Balances</p>
<p>Added 6.2 Reports</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/2016</td>
<td><p>45-46</p>
<p>50-51</p></td>
<td>PSS*1*189</td>
<td><p>Added example 3 and 4 to 4.4.1 PSJI AOR showing inactivation date for IV Additives and Solutions</p>
<p>Added Example 2 and 3 to 4.4.4 PSJI Patient Cost showing inactivation date for IV Additives and Solutions</p>
<p>Updated Revision History and Table of Contents</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/2014</td>
<td><p>All</p>
<p>i, v-vi</p>
<p>1</p>
<p>57</p>
<p>63-64</p>
<p>6-7</p>
<p>68, 70, 73</p>
<p>79-80</p></td>
<td><p>PSJ*5*252,</p>
<p>PSJ*5*257</p></td>
<td><p>Renumber all pages</p>
<p>Updated Revision History &amp; Table of Contents</p>
<p>Added to the Related Manuals</p>
<p>Add section 4.8 Dosing Order Checks</p>
<p>Remove &amp; update content</p>
<p>Added IMO DC/EXPIRED DAY LIMIT bullet and note, and also updated screen capture</p>
<p>Updated Glossary</p>
<p>Update Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2013</td>
<td>i-iii, v-vi, 6a-6f, 61, 71-72</td>
<td>PSJ*5*279</td>
<td><p>Added Missing Dose Printer and Pre-Exchange Report Device to section 3.2., Clinic Definition.</p>
<p>Added section 3.2.1., Pre-Exchange Printer for Clinic Orders.</p>
<p>Updated Glossary and Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>01/2013</td>
<td><p><a href="\l">i</a>, iv</p>
<p>58</p>
<p>60-62</p></td>
<td><p>PSJ*5*260,</p>
<p>PSJ*5*268</p></td>
<td><p>Updated Revision History</p>
<p>New Hidden Action for DA, OCI, &amp; CK</p>
<p>Added BSA, CrCL, &amp; DATUP to Glossary</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>4/2011</td>
<td><p>i</p>
<p>iii-iv</p>
<p>5</p>
<p>6</p>
<p>6b</p>
<p>7</p>
<p>10</p>
<p>12-13</p>
<p>13</p>
<p>14</p>
<p>15</p>
<p>16a-b</p>
<p>17</p>
<p>20</p>
<p>22-23</p>
<p>24</p>
<p>26-29</p>
<p>29</p>
<p>30-30b</p>
<p>31</p>
<p>34</p>
<p>35</p>
<p>38</p>
<p>38-38b</p>
<p>40</p>
<p>41</p>
<p>54</p>
<p>55</p>
<p>56a-d</p>
<p>56e-f</p>
<p>57-70</p>
<p>71-72</p></td>
<td>PSJ*5*181</td>
<td><p>Updated Revision History</p>
<p>Updated Table of Contents</p>
<p>Updated Example: Supervisor's Menu &amp; update the Administering Team file</p>
<p>Updated Example: Administering Teams</p>
<p>Updated Example: Clinic Groups and Updated Example: Management Reports Menu</p>
<p>Updated Example2: AMIS Report with No Data</p>
<p>New example 2: Drug (Cost and/or Amount) Report with No Data</p>
<p>New Example: Provider (Cost per) Report</p>
<p>New Example: Service (Total Cost per) Report</p>
<p>New Example: Total Cost to Date (Current Patients) Report</p>
<p>New Example: Non-Standard Schedule Search</p>
<p>Updated Example: Order Set Enter/Edit</p>
<p>New Example: Parameters Edit Menu</p>
<p>New Example: Auto-Discontinue Set-Up</p>
<p>New Example: Inpatient User Parameters Edit</p>
<p>Added New Inpatient Ward Parameters Edit - HOURS OF RECENTLY DC/EXPIRED</p>
<p>New Example: Inpatient Ward Parameters Edit</p>
<p>Added New Systems Parameters Edit - HOURS OF RECENTLY DC/EXPIRED</p>
<p>New Example: Systems Parameters Edit</p>
<p>New Example: Pick List Menu</p>
<p>New Example: Ward Groups</p>
<p>New Example: Supervisor's Menu (IV)</p>
<p>New Example: Auto-Discontinue Set-Up (continued)</p>
<p>New Example: Category File (IV)</p>
<p>New Example: Management Reports (IV)</p>
<p>New Example: Active Order Report by Ward/Drug (IV)</p>
<p>New Example: Recompile Stats File (IV)</p>
<p>New Example: Site Parameter (IV) (continued)</p>
<p>CPRS Order checks: How they work</p>
<p>Error Messages</p>
<p>Glossary</p>
<p>Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/10</td>
<td>i-ii, 10-11, 47-48</td>
<td>PSJ*5*214</td>
<td><p>Revised description of <em>Patients on Specific Drug(s)</em> option in Sections 3.4.3 and 4.4.5.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/07</td>
<td>1, 69-70</td>
<td>PSJ*5*120</td>
<td><p>Removed revised dates for Inpatient Medications manuals.</p>
<p>Modified Glossary to revise definition of Stop Date/Time. <mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>5/06</td>
<td><p>25a-25b, 27-28</p>
<p>29-30</p>
<p>73-74</p></td>
<td>PSJ*5*154</td>
<td><p>Added the INPATIENT WARD PARAMETER, PRIORITIES FOR NOTIFICATION to section 3.8.3 description and example.</p>
<p>Added the PHARMACY SYSTEM PARAMETERS, PRIORITIES FOR PENDING NOTIFY, and PRIORITIES FOR ACTIVE NOTIFY to section 3.9.4 description and example.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>03/05</td>
<td><p>iii,</p>
<p>1,</p>
<p>5a-5b,</p>
<p>6, 8, 10, 12, 13, 15, 17, 20, 23, 27, 31-33</p>
<p>29-30,</p>
<p>61-70,</p>
<p>71-74</p></td>
<td>PSJ*5*112</td>
<td><p>Updated Table of Contents with new Section 3.2, Clinic Definition; renumbered all following sections in Section 3. (p. iii)</p>
<p>In Section 1, Introduction, updated revision dates. (p. 1)</p>
<p>Added new Section 3.2 for the Clinic Definition [PSJ CD] option; renumbered all following sections numbers in Section 3. (p. 5a-5b, 6, 8, 10, 12, 13, 15, 17, 20, 23, 27, 31‑33)</p>
<p>Added heading above and &lt;Enter&gt; symbols in Clinic Groups screen shot. (p. 6)</p>
<p>In Section 3.8, PARameters Edit Menu, changed Clinic Stop Dates to Clinic Definition on screen shot. (p. 17)</p>
<p>In Section 3.8.4., removed AUTO-DC IMO ORDERS field from bulleted list and Systems Parameters Edit screen shot; added Note about the new location of field. (p.29-30)</p>
<p>In Section 5, Glossary, added definition for CLINIC DEFINITION File and reflowed text to next page. (p. 61‑70)</p>
<p>Updated Index to include CLINIC DEFINITION File and Option, Auto-Discontinue IMO Orders, and Inpatient Medications for Outpatients; reflowed text to remaining pages. (p. 71-74)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>01/05</td>
<td>All</td>
<td>PSJ*5*111</td>
<td><p>Reissued entire document to include updates for Inpatient Medication Orders for Outpatients and Non-Standard Schedules.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>
*(This page included for two-sided copying.)*Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications package provides a method of management, dispensing, and administration of inpatient drugs within the hospital. Inpatient Medications combines clinical and patient information that allows each medical center to enter orders for patients, dispense medications by means of Pick Lists, print labels, create Medication Administration Records (MARs), and create Management Reports. Inpatient Medications also interacts with the Computerized Patient Record System (CPRS) and the Bar Code Medication Administration (BCMA) packages to provide more comprehensive patient care.

This user manual is written for the Pharmacy Supervisor or the Automated Data Processing Application Coordinator (ADPAC). The main texts of the manual provide information to setup various function requirements needed for the basic running of the Unit Dose Medications and IV Medications modules. It also outlines options available under the Management Reports menu and Pick List actions.

The Inpatient Medications documentation is comprised of several manuals. These manuals are written as modular components and can be distributed independently and are listed below.

Nurse's User Manual V. 5.0

Pharmacist's User Manual V. 5.0

Supervisor's User Manual V. 5.0

Technical Manual/Security Guide V. 5.0

Release Notes

Release Notes (IMO – Phase I & II/ IMR – Phase II)

Pharmacy Ordering Enhancements (POE) Phase 2 Release Notes V. 1.0

Pharmacy Ordering Enhancements (POE) Phase 2 Installation Guide V. 1.0

Dosing Order Check User Manual

VistA to MOCHA Interface Document

  
*(This page included for two-sided copying.)*

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *Inpatient Order Entry* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

> Example: "Select DRUG:" indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

> Example: Printing a MAR report by ward group G, by ward W, or by patient P.

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.

> Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

- Text depicted with a black background, displayed in a screen capture, designates blinking text on the screen.

> Example:

> \(9\) Admin Times: 01-09-15-20

> \*(10) Provider: PSJPHARMACIST,ONE

- ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/002.png)Note: Indicates especially important or helpful information.
- ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/003.png) Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.

Example: ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/004.png) All options under the *PIck List Menu* are locked with the PSJU PL key.

- Some of the menu options have several letters that are capitalized. By entering in the letters and pressing \<Enter\>, the user can go directly to that menu option (the letters do not have to be entered as capital letters).

Example: From the *Unit Dose Medications Option*: the user can enter INQ and proceed directly into the *INQuiries Menu* option.

<span id="Orphan_Bullet" class="anchor"></span>

- ?, ??, ??? One, two or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.
- ^ Caret (up arrow or a circumflex) and pressing \<Enter\> can be used to exit the current option.

# Supervisor's Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU FILE\]

The *Supervisor's Menu* option allows the user (coordinator) to edit the various files and perform certain functions needed for the basic running of the Inpatient Medications package.

Example: Supervisor's Menu

Select Supervisor's Menu Option: ?

Administering Teams

Clinic Groups

MANagement Reports Menu ...

Non-Standard Schedule Report

Non-Standard Schedule Search

Order Set Enter/Edit

PARameters Edit Menu ...

PATient Order Purge

\*\*\> Out of order: TEMPORARILY UNAVAILABLE

PIck List Menu ...

Ward Groups

Select Supervisor's Menu Option:

## Administering Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU AT\]

The *Administering Teams* option allows the supervisor to add and edit the names and room-bed numbers associated with the administering teams (carts) on each ward. Since a number of teams might be required to administer medications to one ward, depending on the size of the ward and the shift, this option provides a way of defining these teams. The Medication Administering Team file (#57.7) contains this information.

It would be helpful to have lists of all wards and associated beds from Medical Administration Service (MAS). These lists will allow the user to easily breakdown wards by room-bed numbers for team assignment.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/005.png)Note: The user will not be able to enter a room-bed number into more than one team.

Example: Administering Teams

Select Supervisor's Menu Option: Administering Teams

Select WARD: 1

1 1 GEN MED

2 1 MIKE'S IP WARD \*\*\* INACTIVE \*\*\*

CHOOSE 1-2: 1 GEN MED

Select TEAM: GENERAL MED TWO// \<Enter\>

TEAM: GENERAL MED TWO// \<Enter\> Select ROOM-BED: B-5// B-4

ROOM-BED: B-4// \<Enter\>

Select ROOM-BED: \<Enter\>

Select TEAM: \<Enter\>

Select WARD:

## Clinic Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ CD\]

This *Clinic Definition* option allows sites to define the behavior of Inpatient Medications for Outpatients (IMO) orders on a clinic-by-clinic basis. Users can define the following parameters, by clinic:

- NUMBER OF DAYS UNTIL STOP: The number of days to be used to calculate the stop date for orders placed in the specified clinic.
- AUTO-DC IMO ORDERS: Whether to auto-dc IMO orders upon patient movement, such as admission, discharge, ward transfer, and treating specialty change.
- SEND TO BCMA?: Whether to transmit IMO orders to BCMA.
- MISSING DOSE PRINTER: This printer is used to print Missing Dose Requests for this clinic, if defined, or will use the BCMA Site Parameters value for Clinic Missing Dose Request Printer. If that field is blank, it will use the BCMA Site Parameters value for Inpatient Missing Dose Request Printer.
- PRE-EXCHANGE REPORT DEVICE: This device will be used as the default device for the Pre-Exchange report for this clinic.
- IMO DC/EXPIRED DAY LIMIT: Enter number of days that DC/Expired clinic orders will be included in the enhanced order checks for drug interaction and therapeutic duplications. If this field is left blank, a default value of 30 days will be used. Otherwise, sites can define this field to be a number from 1–120 to represent the number of days that DC/EXPIRED IMO orders should be included in Order Checks.

> If an Inpatient Medications for Outpatients (IMO) order is created in CPRS for a clinic that is not defined in the CLINIC DEFINITION (#53.46) file, a message is sent to the PSJ CLINIC DEFINITION mail group indicating the order will not display in BCMA unless the clinic is defined in the CLINIC DEFINITION (#53.46) file, and the SEND TO BCMA? (#3) field is set to YES.

- <span id="P6" class="anchor"></span>CLINIC APPT DATE RANGE MIN: The number of days to search for past appointments when entering a clinic order. If not specified, the default period of 90 days (3 months) will be used. Appointments will display with dates between CLINIC APPT DATE RANGE MIN and CLINIC APPT DATE RANGE MAX.
- <span id="CLINIC_APPT_DATE_RANGE_MAX" class="anchor"></span>CLINIC APPT DATE RANGE MAX: The number of days to search for future appointments when entering a clinic order. If not specified, the default period of 365 days (1 year) will be used. Appointments will display with dates between CLINIC APPT DATE RANGE MIN and CLINIC APPT DATE RANGE MAX.
- <span id="opioid_2" class="anchor"></span>OPIOID TREATMENT CLINIC?: This field determines if the clinic should be identified as an Opioid Treatment Program Clinic. Allows YES, NO, or null answer. The initial default is null, which is equivalent to a NO answer.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/006.png)Note: For detailed descriptions of the above parameters, please see "Fields from the CLINIC DEFINITION File (#53.46)" in the Inpatient Medications V. 5.0. Technical Manual/Security Guide.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/007.png)Note: The *Clinic Stop Dates* \[PSJ CSD\] option has been removed, and the *Clinic Definition* \[PSJ CD\] option has been added under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/008.png)Note: The AUTO-DC IMO ORDERS field is only used if the auto-dc parameters in Inpatient Medications are controlling the movement actions. Otherwise, this field would be ignored.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/009.png)Note: The IMO DC/EXPIRED DAY LIMIT field is used to define the number of days expired and discontinued clinic orders are displayed for drug interaction and therapeutic duplications.

Example: Clinic Definition

Select OPTION NAME: PSJ CD Clinic Definition

Clinic Definition

Select CLINIC: CLINIC (45)

...OK? Yes// \<Enter\>

NUMBER OF DAYS UNTIL STOP: 10// \<Enter\>

AUTO-DC IMO ORDERS: YES// \<Enter\>

SEND TO BCMA?: NO// \<Enter\>MISSING DOSE PRINTER:PRE-EXCHANGE REPORT DEVICE:

IMO DC/EXPIRED DAY LIMIT: 30 \<Enter\>

### Pre-Exchange Printer for Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A modified version of the pre-exchange report is available allowing the user to print pre-exchange reports to devices associated with each clinic.

If any Inpatient orders were processed/verified with clinic orders, you will be prompted for the Ward Pre-Exchange Report device prior to receiving a prompt for any clinic location Pre-Exchange Report device.

You will be prompted separately, (and a different report will print), for all orders for each different clinic for which you have edited orders.

If you have defined a default report device at the *Clinic Definition* \[PSJ CD\] option, press Enter to accept the default and print the Pre-Exchange Units Report.

- The use of the existing next pick list / cart exchange process for clinic orders is not supported.
- An additional prompt is added to the *Clinic Definition* \[PSJ CD\] option when entering the clinic default printer device for a clinic defined in the CLINIC DEFINITION (#53.46) file.

Example: Pre-Exchange Printer Prompt

Select OPTION NAME: CLINIC DEFINITION  PSJ CD     Clinic Definition

Select CLINIC: CLINIC (60)

         ...OK? Yes//   (Yes)

NUMBER OF DAYS UNTIL STOP: 7

AUTO-DC IMO ORDERS: NO//

SEND TO BCMA?: YES// Y  YES

MISSING DOSE PRINTER:

PRE-EXCHANGE REPORT DEVICE: L9150\$PRT

- The last inpatient location is no longer used in determining the default pre-exchange printer.
- If no default device is defined in the CLINIC DEFINITION (#53.46) file, "Home" defaults as the pre-exchange printer.

Example: Select HOME as Default Printer

Select DEVICE for PRE-EXCHANGE UNITS Report: HOME//      Right Margin: 80//

- The user may select the default device when printing the Pre-Exchange report, upon finishing new orders.

Example: Selecting Default Printer upon Finishing New Order

Select DEVICE for PRE-EXCHANGE UNITS Report for CLINIC (60): PRINTER2// \<return\>   Right Margin: 80//

Keep PRINTER2 as the PRE-EXCHANGE REPORT DEVICE for CLINIC (60)this session? Y

Pre-Exchange Units Report

The Pre-Exchange Units Report for non-inpatients displays the Clinic name in the header and detail rather than Ward.

If any Inpatient orders were processed/verified with clinic orders, you will be prompted for the Ward Pre-Exchange Report device prior to receiving a prompt for any clinic location Pre-Exchange Report device.

You will be prompted separately, (and a different report will print), for all orders for each different clinic for which you have edited orders.

If you have defined a default report device at the *Clinic Definition* \[PSJ CD\] option, press Enter to accept the default and print the Pre-Exchange Units Report.

Viewing the Pre-Exchange Units report:

Use existing functionality to either enter a report device or '??' to display, and then select from a list, and then press Enter.

If a default report device has not been defined and you do not enter a Pre-Exchange Units Report device at the prompt, the report will print to the screen with the following information:

- Report Heading with Date and Time
- Clinic or Ward (with Room-Bed if a Ward), Patient, Order, Dispense Drug, U/D (Unit Dose), and Needs Headings

Example: Pre-Exchange Units Report

<u>For a Clinic:</u>

PRE-EXCHANGE UNITS REPORT - 12/09/12 19:38

Clinic Room-bed

Patient

Order

Dispense Drug U/D Needs

--------------------------------------------------------------------------------

BECKY'S CLINIC

BCMACOIM,FIFTEEN (9015)

ACETAMINOPHEN 10 MG PO Q4H

THIORIDAZINE 30MG/ML CONC. 1 1

DIGITOXIN 25MG PO Q4H

DIGITOXIN 0.1MG S.T. 1 4

FLUCYTOSINE 500 MG PO BID-AM

FLUCYTOSINE 500MG CAP 1 2

FUROSEMIDE 20 MG PO QID

FUROSEMIDE 20 MG 1 1

METOPROLOL 50 MG PO BID-NOON

METOPROLOL 50MG S.T. 1 2

<u>For a Ward:</u>

PRE-EXCHANGE UNITS REPORT - 12/09/12 19:34

Ward Room-bed

Patient

Order

Dispense Drug U/D Needs

--------------------------------------------------------------------------------

GEN MED B-3

BCMACOIM,FIFTEEN (9015)

DIGITOXIN 25MG PO Q4H

DIGITOXIN 0.1MG S.T. 1 4

FUROSEMIDE 20 MG PO QID

FUROSEMIDE 20 MG 1 1

METOPROLOL 50 MG PO BID-NOON

METOPROLOL 50MG S.T. 1 2

## Clinic Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU ECG\]

The *Clinic Groups* option is used to group clinics into entities for sorting and reporting functions. The primary purpose of Clinic Groups is for use with Inpatient Medications for Outpatients functionality.

Example: Clinic Groups

Select Supervisor's Menu Option: Clinic Groups

Select CLINIC GROUP NAME: SHOT CLINIC GROUP

Are you adding 'SHOT CLINIC GROUP' as a new CLINIC GROUP (the 1ST)? No// Y

(Yes)

NAME: SHOT CLINIC GROUP// \<Enter\>

Select CLINIC: CLINIC

1 CLINIC (45)

2 CLINIC (PAT)

3 CLINIC PATTERN

4 CLINIC PATTERN (MAIN)

5 CLINIC PATTERN 45

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 CLINIC (45)

Are you adding 'CLINIC (45)' as a new CLINIC (the 1ST for this CLINIC GROUP)?

No// Y (Yes)

Select CLINIC: \<Enter\>

Select CLINIC GROUP NAME: SHOT CLINIC GROUP

NAME: SHOT CLINIC GROUP// \<Enter\>

Select CLINIC: CLINIC (45)// \<Enter\>

Select CLINIC GROUP NAME:

## MANagement Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU MNGMT REPORTS\]

The *MANagement Reports Menu* option is used to print various reports using data generated by the Unit Dose software module. There are six reports that can be printed using this option. All of the reports are printed in an 80-column format. It is advisable to queue these reports whenever possible.

Example: Management Reports Menu

Select Supervisor's Menu Option: MANagement Reports Menu

AMIS (Cost per Ward)

Drug (Cost and/or Amount)

PSD Patients on Specific Drug(s)

PRovider (Cost per)

Service (Total Cost per)

Total Cost to Date (Current Patients)

Select MANagement Reports Menu Option:

### AMIS (Cost per Ward)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### \[PSJU AMIS\]

The *AMIS (Cost per Ward)* option will produce an Automated Management Information System (AMIS) report to show the dispensing cost of the pharmacy by ward. Only those wards with a dispensing amount or cost are shown.

The user can enter the start and stop dates of the time span covered by this AMIS report. The start and stop dates can be the same, thus producing a one-day report. The stop date cannot come before the start date.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/010.png)Note: If there are any pick lists that need to be filed away for this report to be accurate, there will be a warning on the screen, after the user enters the dates, listing the pick lists.

Example 1: AMIS Report

Select MANagement Reports Menu Option: AMIS (Cost per Ward)

Enter START DATE: T-3 (FEB 05, 2001)

Enter STOP DATE: T (FEB 08, 2001)

\*\*\* WARNING \*\*\*

PICK LISTS need to be filed away for the following ward groups, or this AMIS

report will not be accurate for the date range asked for.

WEST WING

SOUTH WING

Select PRINT DEVICE: 0;80;999 NT/Cache virtual TELNET terminal

UNIT DOSE AMIS REPORT 02/08/01 22:10

FROM 02/05/01 THROUGH 02/08/01

TOTAL UNITS TOTAL AVERAGE COST

WARD DISPENSED COST PER UNIT

--------------------------------------------------------------------------------

1 EAST 16 0.63 0.04

================================================================================

TOTALS =\> 16 0.63 0.04

Example 2: AMIS Report with No Data

UNIT DOSE AMIS REPORT 02/08/01 22:10

FROM 02/05/01 THROUGH 02/08/01

TOTAL UNITS TOTAL AVERAGE COST

WARD DISPENSED COST PER UNIT

--------------------------------------------------------------------------------

\*\*\* NO AMIS DATA FOUND \*\*\*

AMIS (Cost per Ward)

Drug (Cost and/or Amount)

PSD Patients on Specific Drug(s)

PRovider (Cost per)

Service (Total Cost per)

Total Cost to Date (Current Patients)

Select MANagement Reports Menu Option:

### Drug (Cost and/or Amount)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### \[PSJU DCT\]

The *Drug (Cost and/or Amount)* option creates a report that calculates the total cost for all or selected drugs dispensed over a specific time frame of at least one calendar day. The information from this report can be sorted alphabetically by drug name, by descending order of total cost, or by descending order of total amount dispensed. The information for the report can be limited by a minimum total cost and a minimum amount dispensed.

The start and stop dates are required to run this report. The start and stop dates can be the same, thus producing a one-day report. Non-formulary items will be designated on the report by two asterisks (\*\*) preceding the dispense drugs.

The user will also encounter the following prompts:

- "Select by Ward? (Y/N): NO//"

> A YES answer will include dispensing amounts and cost by ward.

- "Select drugs by DISPENSE DRUG, ORDERABLE ITEM, or VA CLASS:"

> The user will enter the category, (D) Dispense Drug, (O) Orderable Item, or (V) VA Class, to indicate how the report will be sorted.

- "Select \<PREVIOUSLY SELECTED SORT CATEGORY\> drug: ALL//"

> The user can enter A (or press \<Enter\>) to show all drugs on this report. An S can be entered to specify which drugs to show on this report. If an S is entered, the user will not be prompted for lower limits for cost or dispensed units.

- "Sort drugs by \<PREVIOUSLY SELECTED SORT CATEGORY\>, COST, or AMOUNT DISPENSED:"

> What is shown here as \<PREVIOUSLY SELECTED SORT CATEGORY\> will show on the screen as DISPENSED DRUG, ORDERABLE ITEM, or VA CLASS, depending on the selected answer to the earlier prompt in this list. Enter D, O, or V to have this report print the drugs in alphabetical order of the Dispensed Drug name, Orderable Item name, or VA Class. Enter C to have this report print the drugs in descending order of Total Cost; or enter A to have this report print the drugs in descending order of the Amount Dispensed (in units).

- "Print all drugs costing at least?"

Enter a number, representing a dollar amount, to be the lower limit for this report. This number can be zero (0) to include all drugs with a positive cost. A null response will include all drugs.

- "Print all drugs with a dispensing amount of at least?"

> Enter a number to be the lower dispensing limit (inclusive) for this report. This number can be zero (0) to include all drugs with a positive dispensing amount. A null response will include all drugs.

Example 1: Drug (Cost and/or Amount) Report

Select MANagement Reports Menu Option: Drug (Cost and/or Amount)

Enter START DATE: T-3 (FEB 05, 2001)

Enter STOP DATE: T (FEB 08, 2001)

Select by Ward? (Y/N):? NO// \<Enter\>

Select drugs by DISPENSE DRUG, ORDERABLE ITEM, or VA CLASS: DISPENSE DRUG

Select Dispensed Drug: ALL// \<Enter\>

Sort drugs by DISPENSED DRUG, COST, or AMOUNT DISPENSED: ?

Enter a code from the list.

Select one of the following:

1 DISPENSED DRUG

2 COST

3 AMOUNT DISPENSED

Sort drugs by DISPENSED DRUG, COST, or AMOUNT DISPENSED: 1 DISPENSED DRUG

Print all drugs costing at least? ?

Enter a number (dollar amount) to be the lower limit for this report. This

number may be zero (0) to include all drugs with a positive cost. A NULL

response will include all drugs. Enter an '^' to terminate this report.

Print all drugs costing at least? .5

Print all drugs with a dispensing amount of at least? ?

Enter a number to be the lower dispensing limit (inclusive) for this report.

This number may be zero (0) to include all drugs with a positive dispensing

amount. A NULL response will include all drugs. Enter an '^' to

terminate this report.

Print all drugs with a dispensing amount of at least? 0

Select PRINT DEVICE: 0;80;99 NT/Cache virtual TELNET terminal

UNIT DOSE DRUG COST REPORT 02/08/01 22:22

FROM 01/30/01 THROUGH 02/08/01

TOTAL UNITS TOTAL

DISPENSED DRUG DISPENSED COST

--------------------------------------------------------------------------------

\*\*CEFACLOR 250MG CAPS 3.000 3.2550

\*\*HALCINONIDE 0.1% CREAM 30GM 3.000 45.9300

\*\*MASOPROCOL 10% CREAM 30GM 1.000 20.0600

\*\*NITROFURANTOIN 50MG 1.000 0.3150

POTASSIUM CHLORIDE 10 mEq U/D TABLET 3.000 0.0360

\*\*RESERPINE 0.25MG 10.000 0.3500

TEMAZEPAM 15MG U/D 6.000 0.2820

---------------------------

Total: 27.000 70.2280

Example 2: Drug (Cost and/or Amount) Report with No Data

UNIT DOSE DRUG COST REPORT 02/08/01 22:19

FROM 02/05/01 THROUGH 02/08/01

TOTAL UNITS TOTAL

DISPENSED DRUG DISPENSED COST

--------------------------------------------------------------------------------

\*\*\* NO DRUG COST DATA FOUND \*\*\*

AMIS (Cost per Ward)

Drug (Cost and/or Amount)

PSD Patients on Specific Drug(s)

PRovider (Cost per)

Service (Total Cost per)

Total Cost to Date (Current Patients)

Select MANagement Reports Menu Option:

### Patients on Specific Drug(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ PDV\]

The *Patients on Specific Drug(s)* option creates a report that lists patients on specific Orderable Item(s), Dispense Drug(s), or Veterans Affairs (VA) class(es) of drugs. When more than one of these drugs is chosen, the user will have the option to only display patients with orders containing ALL of the selected drugs or classes. The default behavior will be to display patients with orders for ANY of the selected drugs or classes.

The user will be prompted for the start and stop dates. Orders that are active between these two dates will be listed on the report. The user then has the choice to see only IV orders, Unit Dose orders, or both types of orders. These orders may be sorted by patient name or by the start date of the orders. The user will choose to sort by Orderable Items, Dispense Drug, or VA class of drugs and then choose one or multiple drugs or classes. If a single drug or class is chosen, the orders for that drug or class will be listed. If multiple matches for drugs or classes are designated, the report will only include patients for whom orders are found meeting the designated number of matches to drugs or classes. By using the "Select number of matches" prompt, the user may select how many of the items entered must be on the patient's record in order for the patient to be displayed in the report.

For example: Patient A has an order for ACETAMINOPHEN TAB, patient B has an order for ASPIRIN TAB, and patient C has orders for both. If the user chooses two Orderable Items (ACETAMINOPHEN TAB and ASPIRIN TAB), and enters '1' (default) on the number of matches screen, the orders of all three patients will print. If the user chooses two Orderable Items and enters '2' on the number of matches screen, only patient C's orders will print.

Selecting a parent VA class will function as if the user had selected all of its children classes manually. Users will also be able to select one or more divisions and/or wards, which will limit the results to print only patients from the locations entered. When selecting all divisions and all wards, an additional prompt is shown to allow selection of one pharmacy ward group for selected locations.

Example: Patients on Specific Drug(s) Report

Select MANagement Reports Menu Option: Patients on Specific Drug(s)

Enter start date: T-9 (JAN 30, 2001)

Enter stop date: T (FEB 08, 2001)

List IV orders, Unit Dose orders, or All orders: ALL// \<Enter\>

Do you wish to sort by (P)atient or (S)tart Date: Patient// \<Enter\>

List by (O)rderable Item, (D)ispense Drug, or (V)A Class of Drugs: Orderable Item

Select PHARMACY ORDERABLE ITEM NAME: WARFARIN TAB

Dispense Drugs for WARFARIN are:

WARFARIN 10MG U/D

WARFARIN 5MG U/D

WARFARIN 2.5MG U/D

WARFARIN 2MG U/D

WARFARIN 5MG

WARFARIN 7.5MG U/D

WARFARIN 2.5MG

WARFARIN 2MG

WARFARIN 7.5MG

WARFARIN 10MG

Select PHARMACY ORDERABLE ITEM NAME: \<Enter\>

Select number of matches: 1// \<Enter\>

Select division: ALL// \<Enter\>

Select ward: ALL// \<Enter\>

You may optionally select a ward group...

Select a Ward Group: \<Enter\>

Select PRINT DEVICE: NT/Cache virtual TELNET terminal

...this may take a few minutes...

...you really should QUEUE this report, if possible...

Press RETURN to continue "^" to exit: \<Enter\>

02/08/01 PAGE: 1

LISTING OF PATIENTS WITH ORDERS CONTAINING ORDERABLE ITEM(S):

WARFARIN

FROM 01/30/01 00:01 TO 02/08/01 24:00

--------------------------------------------------------------------------------

Start Stop

Patient Order Date Date

--------------------------------------------------------------------------------

PSJPATIENT,ONE WARFARIN TAB 01/30 01/31

000-00-0001 Give: 5MG PO QPM PRN

1 EAST

WARFARIN TAB 01/30 01/31

Give: 5MG PO QPM PRN

### PRovider (Cost per)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU PRVR\]

The *PRovider (Cost per)* option will create a report to print the cost of all drugs dispensed within a user-specified length of time, grouped together by provider. The user will be prompted to enter the start and stop dates for this Provider report. The report will show a sub-total for each provider and the total cost for all providers at the end of the report. A report can be printed for one or more specific providers or for all providers. Also, the user can select to start a new page for each provider.

Example: Provider (Cost per) Report

Select MANagement Reports Menu Option: PRovider (Cost per)

Enter START DATE: T-9 (JAN 30, 2001)

Enter STOP DATE: T (FEB 08, 2001)

Show ALL or SELECTED providers? ALL// \<Enter\> (ALL)

Do you want to start a new page for each provider? No// \<Enter\> (No)

Select PRINT DEVICE: 0;80;999 NT/Cache virtual TELNET terminal

02/08/01 22:30 UNIT DOSE COST PER PROVIDER REPORT Page: 1

FROM 01/30/01 TO 02/08/01

PROVIDER TOTAL UNITS TOTAL

DRUG DISPENSED COST

--------------------------------------------------------------------------------

PSJPHARMACIST,ONE

\*\* HALCINONIDE 0.1% CREAM 30GM 3 45.93

POTASSIUM CHLORIDE 10 mEq U/D TABLET 2 0.02

--------- ------------

----- AVG. COST/UNIT: 9.19 5 45.95

PSJPROVIDER,ONE

\*\* CEFACLOR 250MG CAPS 3 3.26

\*\* MASOPROCOL 10% CREAM 30GM 1 20.06

\*\* NITROFURANTOIN 50MG 1 0.32

POTASSIUM CHLORIDE 10 mEq U/D TABLET 1 0.01

\*\* RESERPINE 0.25MG 10 0.35

TEMAZEPAM 15MG U/D 6 0.28

--------- ------------

----- AVG. COST/UNIT: 1.10 22 24.27

================================================================================

TOTALS =\> AVG. COST/UNIT: 2.60 27 70.23

\*\*\* DONE \*\*\*

AMIS (Cost per Ward)

Drug (Cost and/or Amount)

PSD Patients on Specific Drug(s)

PRovider (Cost per)

Service (Total Cost per)

Total Cost to Date (Current Patients)

Select MANagement Reports Menu Option:

### Service (Total Cost per)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU SCT\]

The *Service (Total Cost per)* option creates a report of the total cost of dispensed medications forward services (medicine, surgery, etc.) over a user-specified time frame. The report provides the total number of units dispensed, the total cost of those units dispensed, and the average cost of each unit dispensed on a service-by-service basis.

############################### 

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/011.png)Note: The software looks in the Ward Location file (#42) to determine which service a ward is assigned. If a ward has Unit Dose cost and/or amount but is not assigned to a service, that ward will print at the end of the report.

Example: Service (Total Cost per) Report

Select MANagement Reports Menu Option: SERvice (Total Cost per)

Enter START DATE: T-9 (JAN 30, 2001)

Enter STOP DATE: T (FEB 08, 2001)

Select PRINT DEVICE: 0;80;999 NT/Cache virtual TELNET terminal

UNIT DOSE COST PER SERVICE REPORT 02/08/01 22:31

FROM 01/30/01 THROUGH 02/08/01

TOTAL UNITS TOTAL AVERAGE COST

SERVICE DISPENSED COST PER UNIT

--------------------------------------------------------------------------------

INTERMEDIATE MED 22 24.27 1.10

MEDICINE 5 45.95 9.19

\*\*\* A SERVICE COULD NOT BE FOUND FOR THE FOLLOWING WARD(S) \*\*\*

999Z 26 6.11 0.24

================================================================================

TOTALS =\> 27 70.23 2.60

### Total Cost to Date (Current Patients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU TCTD\]

The *Total Cost to Date (Current Patients)* option creates a report of the total cost of the Unit Dose dispensed items for patients that are currently admitted at the medical center. The user can generate this report by ward groups, wards, or individual patients. If the user chooses to print this report for individual patients, then an unlimited number of patients can be selected.

Example: Total Cost to Date (Current Patients) Report

Select MANagement Reports Menu Option: TOtal Cost to Date (Current Patients)

Select by WARD GROUP (G), WARD (W), or PATIENT (P): PATIENT

Select PATIENT: PSJPATIENT,ONE 000-00-0001 08/18/20 1 EAST

Select another PATIENT: \<Enter\>

Select PRINT DEVICE: 0;80;999 NT/Cache virtual TELNET terminal

TOTAL COST TO DATE REPORT 02/08/01 22:32

(BY PATIENT)

Patient Admitting Date

Admitting Diagnosis

Drug Dispensed Cost

--------------------------------------------------------------------------------

PSJPATIENT,ONE (0001) 11/07/00 11:25

TEST

AMPICILLIN 500MG CAP 15 10.97

\*\* CEFACLOR 250MG CAPS 3 3.26

\*\* DANOCRINE 200MG 35 52.33

\*\* NITROFURANTOIN 50MG 1 0.32

\*\* RESERPINE 0.25MG 10 0.35

TEMAZEPAM 15MG U/D 6 0.28

\*\* THEOPHYLLINE 100MG 1 0.17

THEOPHYLLINE 400MG/DEXTROSE 5% 4 13.14

WARFARIN 2.5MG U/D 1 0.00

--------- ------------

----- AVG. COST/UNIT: 1.06 76 80.81

================================================================================

TOTALS =\> AVG. COST/UNIT: 1.06 76 80.81

AMIS (Cost per Ward)

Drug (Cost and/or Amount)

PSD Patients on Specific Drug(s)

PRovider (Cost per)

Service (Total Cost per)

Total Cost to Date (Current Patients)

Select MANagement Reports Menu Option:

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/012.png)Note: The Medication Status Check option which is located in the PSO Supervisor

menu will search for inpatient medication and  IV orders as well as outpatient orders. 

This option searches for discontinued and expired medication orders, which are still

active in the ORDERS (#100) file.

For more information, see Chapter 27 in the Outpatient Pharmacy (PSO) Manager's

User Manual.

## Non-Standard Schedule Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSJU NSS REPORT\]

The *Non-Standard Schedule Report* option allows the user to list out the non-standard schedules identified by running the *Non-Standard Schedule Search.*

## Non-Standard Schedule Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSJU NSS SEARCH\]

The *Non-Standard Schedule Search* option allows users to identify non-standard schedules that are currently in use. This option will search through Order Sets, Quick Codes, the ADMINISTRATION SCHEDULE file, the PHARMACY ORDERABLE ITEM file, and all orders for the timeframe specified by the user. The person running the option will receive a series of email messages identifying the non-standard schedules. The email message subjects will be: ADMIN SCHEDULES, ADMIN SCHEDULES NOT IN 51.1, NON-STANDARD SCHEDULES IN QUICK CODES, NON-STANDARD SCHEDULES IN ORDER SETS, and NON-STANDARD SCHEDULES IN ORDERABLE ITEMS. The search routine can be run multiple times. This can be used to help show the progress being made in correcting issues. In addition, the report will show active orders in the search period. Please note: the default schedules in the PHARMACY ORDERABLE ITEM file are for both inpatient and outpatient orders.

Example: Non-Standard Schedule Search

Select Supervisor's Menu Option: ?

Administering Teams

Clinic Groups

MANagement Reports Menu ...

Non-Standard Schedule Report

Non-Standard Schedule Search

Order Set Enter/Edit

PARameters Edit Menu ...

PATient Order Purge

\*\*\> Out of order: TEMPORARILY UNAVAILABLE

PIck List Menu ...

Ward Groups

Select Supervisor's Menu Option: Non-Standard Schedule Search

NUMBER OF DAYS: 365// \<Enter\>

Requested Start Time: NOW// \<Enter\> (FEB 24, 2010@14:20:08)

The check of Pharmacy orders is queued

(to start NOW).

YOU WILL RECEIVE A MAILMAN MESSAGE WHEN TASK \#1285255 HAS COMPLETED.

## Order Set Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSJU OSE\]

The *Order Set Enter/Edit* option allows the supervisor to create and edit order sets. An order set is a group of any number of pre-written orders. The maximum number of orders is unlimited.

Order sets are used to expedite order entry for drugs that are dispensed to all patients in certain medical practices or procedures. Order sets are designed for use when a recognized pattern for the administration of drugs can be identified. For example:

- A pre-operative series of drugs administered to all patients that are to undergo a certain surgical procedure
- A certain series of drugs to be dispensed to all patients prior to undergoing a particular radiographic procedure
- A certain group of drugs prescribed by a physician for all patients that are treated for a certain medical ailment or emergency

The rapid entering of this repetitive information using order sets will expedite the whole order entry process. Experienced users might want to set up their more common orders as individual order sets to expedite the order entry process.

Once the orders have been entered through an order set, they are treated as individual orders and can only be acted upon as such.

| ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/013.png) | Note: The VA FileMan convention of enclosing the duplicate entry name in double quotes can be used to enter the same Orderable Item more than once. An example would be to add ACETAMINOPHEN to an order set already containing that drug. |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Order Set Enter/Edit

Select Supervisor's Menu Option: Order Set Enter/Edit

Select ORDER SET: ASPIRIN

Are you adding 'ASPIRIN' as a new UNIT DOSE ORDER SET (the 6TH)? No// Y (Yes)

NAME: ASPIRIN// \<Enter\>

Select ORDERABLE ITEM: AS

1 ASCORBIC ACID TAB 03-25-1996

2 ASCORBIC ACID/FERROUS SULFATE/FOLIC ACID TAB,SA

3 ASPIRIN SUPP,RTL

4 ASPIRIN TAB

5 ASPIRIN TAB,CHEWABLE

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 4 ASPIRIN TAB

Are you adding 'ASPIRIN' as a new ORDERABLE ITEM? No// Y (Yes)

DOSAGE ORDERED: 325MG

DAY (nD) OR DOSE (nL) LIMIT: ?

Answer must be a number followed by a 'D" (for DAY LIMIT), or a number

followed by an 'L' (for DOSE LIMIT).

DAY (nD) OR DOSE (nL) LIMIT: 7D

START DAY AND TIME: ?

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses CURRENT YEAR. Two digit year

assumes no more than 20 years in the future, or 80 years in the past.

If only the time is entered, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.

You may enter a time, such as NOON, MIDNIGHT or NOW.

You may enter NOW+3' (for current date and time Plus 3 minutes

\*Note--the Apostrophe following the number of minutes)

Time is REQUIRED in this response.

Enter the day and time after the order is selected that this order should

start.

START DAY AND TIME: \<Enter\>

MED ROUTE: PO ORAL \<Enter\> PO

SCHEDULE TYPE: C CONTINUOUS

SCHEDULE: QID

1 QID 01-09-15-20

2 QID PC FAR 09-13-17-21

CHOOSE 1-2: 1 01-09-15-20

SPECIAL INSTRUCTIONS: TESTING

Select DISPENSE DRUG: ASPIRIN 325MG U/D CN103

Are you adding 'ASPIRIN 325MG U/D' as a new DISPENSE DRUG (the 1ST for this

ORDERABLE ITEM)? No// Y (Yes)

UNITS PER DOSE: 2

Select DISPENSE DRUG: \<Enter\>

Select ORDERABLE ITEM: \<Enter\>

Select ORDER SET:

## PARameters Edit Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ PARAM EDIT MENU\]

The *PARameters Edit Menu* option is used to edit various parameters within the Unit Dose software module.

Example: Parameters Edit Menu

Select PARameters Edit Menu Option: ?

AUto-Discontinue Set-Up

IUP Inpatient User Parameters Edit

IWP Inpatient Ward Parameters Edit

Clinic Definition

Systems Parameters Edit

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select PARameters Edit Menu Option:

### AUto-Discontinue Set-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ AC SET-UP\]

The *AUto-Discontinue Set-Up* option allows the site to determine if a patient's Inpatient Medications (Unit Dose and IV) orders are to be automatically d/c'd (discontinued) or held when the patient is transferred between wards, between services or to authorized absence.

The decision to discontinue Inpatient Medications orders is determined by the site, on a ward-by-ward and/or service-by-service basis. While this process will entail extra set up on the site's part initially, it will allow the site almost complete control of the auto-discontinue process.

The set up for this process involves three main steps:

1.  <u>Auto-Discontinue for all wards:</u> If the site wants to have Inpatient Medications orders discontinued on all or most ward transfers, the supervisor can have the module automatically set up all wards as 'from' and 'to' wards, saving some time. When this option is chosen, wards currently marked as inactive will also be included. The user can still delete, edit, or add 'from' and 'to' wards at any time. See step 2C for further information.
2.  <u>Ward transfers:</u> The supervisor will select a 'from' ward. This is a ward from which a patient may be transferred. For each 'from' ward, the user can:
1.  Select an 'On Pass' action. This is the action the Inpatient Medications package will take on a patient's orders whenever the patient is transferred from the selected 'from' ward to authorized absence less than 96 hours (known as 'On Pass'). The possible actions are:
- Discontinue the orders
- Place the orders on hold
- Take no action
2.  Select an 'Authorized Absence' action. This is the action the Inpatient Medications package will take on a patient's orders whenever the patient is transferred from the selected 'from' ward to authorized absence <u>greater than</u> 96 hours. The possible actions are:
- Discontinue the orders
- Place the orders on hold
- Take no action
3.  Select an 'Unauthorized Absence' action. This is the action the Inpatient Medications package will take on a patient's orders whenever the patient is transferred from the selected 'from' ward to unauthorized absence <u>greater than</u> 96 hours. The possible actions are:
- Discontinue the orders
- Place the orders on hold
- Take no action
4.  Select the 'To' wards. Whenever a patient is transferred from the selected 'from' ward to any of the selected 'to' wards, the patient's IV and Unit Dose orders will be discontinued. For example, if 1 North is selected as a 'from' ward and 1 South is selected as a 'to' ward, any time a patient is transferred FROM 1 North TO 1 South, the patient's Inpatient Medications orders will be discontinued.

> This process is one way only. For example, if the site also wants orders to be discontinued whenever a patient is transferred FROM 1 South TO 1 NORTH, the user will have to enter 1 South as a 'from' ward and then enter 1 North as one of its 'to' wards.

3.  <u>Service transfers</u>: The supervisor will select a 'from' service. This is a service from which a patient may be transferred. For each 'from' service, the user can select the 'to' services. Whenever a patient is transferred from the selected 'from' service to any of the selected 'to' services, the patient's IV and Unit Dose orders will be discontinued. For example, if Medicine is selected as a 'from' service and SURGERY is selected as a 'to' service, any time a patient is transferred FROM MEDICINE TO SURGERY, the patient's Inpatient Medications orders will be discontinued.

> This process is also one way only. For example, if the site also wants orders to be discontinued whenever a patient is transferred FROM SURGERY TO MEDICINE, the user will have to enter SURGERY as a 'from' service and then enter Medicine as one of its 'to' services.

> If all of the wards are set for auto d/c, it is not necessary to enter services.

> If there is a specific ward or service for which the site does not want Inpatient Medications orders d/c'd, then the supervisor only needs to delete the 'to' ward or service.

> Inpatient Medications orders are always automatically d/c'd whenever the patient is admitted, discharged, or transferred to unauthorized absence.

| ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/014.png) | Note: Pending orders that are auto discontinued will UU<u>NEVER</u>UU be re-instated. |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|

| ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/015.png) | Note: When the Patient Information Management System (PIMS) deletes a patient movement, the medication orders that were discontinued due to the movement are automatically reinstated. There are checks included to prevent the reinstatement of an order if a new duplicate order has been added. |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> A mail message is sent to the PSJ-ORDERS-REINSTATED mail group when the medication orders are automatically reinstated due to the deletion of a patient movement. This message contains the patient's name, last four digits of the patient's social security number, current ward location, reason the orders were reinstated, and a list of the orders that were reinstated. The orders will be listed in the mail message in the same format as a patient profile. This notification also includes any orders that could not be reinstated due to duplicates existing on the system.

Example: Auto-Discontinue Set-Up

Select PARameters Edit Menu Option: AUto-Discontinue Set-Up

Do you want the instructions for auto-discontinue set-up? Yes// N (No)

Do you want the package to set-up all of your wards for auto-discontinue? No// \<Enter\> (No)

(Action on WARD transfer)

Select FROM WARD: 1 EAST// \<Enter\>

FROM WARD: 1 EAST//

'ON PASS' ACTION: DISCONTINUE ORDERS// \<Enter\>

ACTION ON AUTHORIZED ABSENCE: DISCONTINUE ORDERS // \<Enter\>

ACTION ON UNAUTHORIZED ABSENCE: DISCONTINUE ORDERS // \<Enter\>

Select TO WARD: 2 EAST// \<Enter\>

Select FROM WARD: \<Enter\>

(Action on SERVICE transfer)

Select FROM SERVICE: PSYCHIATRY// \<Enter\>

FROM SERVICE: PSYCHIATRY// \<Enter\>

Select TO SERVICE: NHCU// \<Enter\>

Select FROM SERVICE: \<Enter\>

AUto-Discontinue Set-Up

IUP Inpatient User Parameters Edit

IWP Inpatient Ward Parameters Edit

Clinic Definition

Systems Parameters Edit

Select PARameters Edit Menu Option:

### Inpatient User Parameters Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ SEUP\]

The *Inpatient User Parameters Edit* option allows the supervisor to edit Inpatient User parameters that cannot be edited by the user, pharmacist, nurse, etc. The supervisor can allow auto-verification for individual nurses and pharmacists, choose the users that can select Dispense Drugs (instead of just Orderable Items), choose which pharmacy technicians or ward clerks can renew, hold or discontinue orders, and select the order entry process for each user (regular, abbreviated, or ward).

The prompts that appear for each user are dependent on which of the following security keys the user holds:

> PSJ RPHARM identifies the user as a pharmacist

> PSJ RNURSE identifies the user as a nurse

> PSJ PHARM TECH identifies the user as a pharmacy technician using the Unit Dose Medications module

> PSJI PHARM TECH identifies the user as a pharmacy technician using the IV module

Users who do not hold any of these keys are seen as ward clerks. If a user is assigned more than one of these keys, the pharmacist key supersedes the other keys; the nurse key supersedes the pharmacy technician key.

A user's status as a provider does not affect this option. The prompts shown for a provider will be based on which of the above security keys he/she holds. For example, if a provider is also a nurse, the prompts that appear will be those for a nurse.

<u>All Users</u>

The supervisor will see the "ORDER ENTRY PROCESS:" prompt for all users. This is the type of order entry process to be used by this user. Selections available are Regular, Abbreviated, or Ward order entry.

- UU<u>Regular</u> order entry is the full set of prompts for the entry of an order, after which the user is shown a full view of the order and is allowed to take immediate action on the order.
- UU<u>Abbreviated</u> order entry gives the user fewer prompts for the entry of an order, after which the user is shown a full view of the order and is allowed to take immediate action on the order.
- UU<u>Ward</u> order entry gives the user the same prompts as the Abbreviated order entry.

If no entry is made here, it will be interpreted as Regular order entry.

<u>Pharmacist</u>

In addition to the "ORDER ENTRY PROCESS:" prompt, the supervisor will see the following prompt for pharmacists:

- "ALLOW AUTO-VERIFY FOR USER:"

> If this parameter is YES, when the user enters an order, the order is automatically entered as ACTIVE.

<u>Nurse</u>

Since the nurse is not automatically given authority to select the strength and dose form of the medication to be dispensed, the supervisor will see the following prompt, for nurses, in addition to the "ORDER ENTRY PROCESS:" and "ALLOW AUTO-VERIFY FOR USER:" prompts given for pharmacists:

- "MAY SELECT DISPENSE DRUGS:"

> If this is set to YES, the user can select the Dispense Drug for an order. If this is set to NO (or not set), the user can only select the Orderable Item*.*<u>Pharmacy Technician or Ward Clerk</u>

The PSJ PHARM TECH key does not affect the prompts of this option. The supervisor will see the same prompts for a pharmacy technician as for a ward clerk. Since the pharmacy technician and ward clerk are not given authority to verify orders, the supervisor will not see the "ALLOW AUTO-VERIFY FOR USER:" prompt. The following three prompts will be shown in addition to "MAY SELECT DISPENSE DRUGS:" and "ORDER ENTRY PROCESS:". These prompts strictly apply to Unit Dose orders.

- "ALLOW USER TO RENEW ORDERS:"

> If this is set to YES, the user can actually renew orders. If this is set to NO (or not set), the user can only mark orders to be renewed by someone else.

- "ALLOW USER TO HOLD ORDERS:"

> If this is set to YES, the user can actually hold/un-hold orders. If this is set to NO (or not set), the user can only mark orders for hold/un-hold.

- "ALLOW USER TO D/C ORDERS:"

> If this is set to YES, the user can actually discontinue orders. If this is set to NO (or not set), the user can only mark orders to be discontinued by someone else.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/016.png)Note: Any changes made in the *Inpatient User Parameters Edit* option will not take effect for the corresponding users until those users completely exit and re-enter the system.

Example: Inpatient User Parameters Edit

Select PARameters Edit Menu Option: IUP Inpatient User Parameters Edit

Select INPATIENT USER: PSJPHARMACIST,ONE

This user is a PHARMACIST and a PROVIDER.

ALLOW AUTO-VERIFY FOR USER: NO// ?

Answer 'YES' if verification can be automatic when this user enters

orders.

Choose from:

1 YES

0 NO

ALLOW AUTO-VERIFY FOR USER: NO// \<Enter\>

ORDER ENTRY PROCESS: REGULAR// ?

Enter the type of Unit Dose order entry to be used by this user.

Choose from:

0 REGULAR

1 ABBREVIATED

2 WARD

ORDER ENTRY PROCESS: REGULAR// \<Enter\>

Select INPATIENT USER: \<Enter\>

PLEASE NOTE: Any changes made will not take effect for the corresponding users

until those users completely exit and re-enter the system.

AUto-Discontinue Set-Up

IUP Inpatient User Parameters Edit

IWP Inpatient Ward Parameters Edit

Clinic Definition

Systems Parameters Edit

Select PARameters Edit Menu Option:

### Inpatient Ward Parameters Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ IWP EDIT\]

The *Inpatient Ward Parameters Edit* option allows the supervisor to edit the Inpatient Ward parameters. These parameters determine how the Inpatient Medications package will act, depending on the ward where the patient resides. The supervisor will encounter the following prompts in this option:

- "DAYS UNTIL STOP DATE/TIME:"

Enter the number of days (1-100) that an order will last.

- "DAYS UNTIL STOP FOR ONE-TIME:"

> Enter the number of days a one-time order should last. The number can be from 1-100, however; it cannot exceed the number of days that standard orders last (DAYS UNTIL STOP DATE/TIME).

- "SAME STOP DATE ON ALL ORDERS:"

> Answer YES (or 1) if all of a patient's orders are to stop on the same date/time.

- "TIME OF DAY THAT ORDERS STOP:"

> Enter the time of day that orders stop for this ward (military time).

- "DEFAULT START DATE CALCULATION:"

> Enter any of the following codes to select the default start time for orders. When there is no entry for this prompt, NOW will be assumed.

1.  Use CLOSEST ADMIN TIME as Default
2.  Use NEXT ADMIN TIME as Default
3.  Use NOW as Default
- "START TIME FOR 24 HOUR MAR:"

> Enter the time of day (0001-2400) that the 24-Hour MAR is to start. Please use military time with leading and trailing zeros.

- HOURS OF RECENTLY DC/EXPIRED: 31//

> This parameter allows the site to specify the time frame for recently discontinued/expired orders to display on the patient profiles. The value defined in this field will take precedence over the Inpatient System parameter.

- "LABEL FOR WARD STAFF:"

> Enter any of the following codes to select when labels will print for ward staff:

1.  No Labels
2.  First Label On Order Entry/Edit
3.  Label On Entry/Edit and Verification
4.  First Label On Nurse Verification

> If a 0 is entered, labels will only be printed at the end of order entry. No label record will be created, so the user will not be able to print or reprint labels later.

- "WARD LABEL PRINTER POINTER:"

> Enter the device to which labels created by ward staff will be printed. If no device is entered, labels will not print automatically, but as long as a label record is created (see previous prompt) labels can be manually printed using the *Label Print/Reprint* option.

- "LABEL FOR PHARMACY POINTER:"

> Enter any of the following codes to select when labels will print for pharmacy staff:

> 0 No Labels  
> 1 First Label On Order Entry/Edit  
> 2 Label On Entry/Edit and Verification  
> 3 First Label On Pharmacist Verification

> If a 0 is entered, labels will only be printed at the end of order entry. No label record will be created, so the user will not be able to print or reprint labels later.

- "PHARMACY LABEL PRINTER:"

> Enter the device to which labels created by pharmacy staff will be printed. If no device is entered, labels will not print automatically, but as long as a label record is created (see previous prompt) labels can be manually printed using the *Label Print/Reprint* option.

- "LABEL ON AUTO-DISCONTINUE:"

> Answer YES to have labels created when this ward's patients' orders are auto discontinued.

- "MAR HEADER LABELS:"

> Enter YES if MAR header labels should be generated for this ward.

- "DAYS NEW LABELS LAST:"

> Any new labels older than the number of days specified here will automatically be purged. Enter a whole number between 0 and 35.

- "MAR ORDER SELECTION DEFAULT:"

> Enter the number corresponding to the type of orders to be included on MARs and the Medications Due Worksheet printed for this ward.

> 1 All Medications  
> 2 Non-IV Medications only  
> 3 IV Piggybacks

5.  LVPs
6.  TPNs
7.  Chemotherapy Medications (IV)

> Multiple order types (except 1) may be selected using the hyphen (-) or the comma (,). Example: 2-4 or 2,3,4

- "PRINT PENDING ORDERS ON MAR:"

> Enter YES to include the pending orders that were acknowledged by a nurse on the MARs and the Medication Due Worksheet.

- " 'SELF MED' IN ORDER ENTRY:"

> Answer YES to have the prompts for patient self-medication included in the order entry process.

- "PRE-EXCHANGE REPORT DEVICE:"

> Enter a device on which the Pre-Exchange Report may be printed. Answer with DEVICE NAME, or LOCAL SYNONYM, or \$I, or VOLUME SET(CPU), or SIGN-ON/SYSTEM DEVICE, or FORM CURRENTLY MOUNTED.

- "STAT NOW MAIL GROUP:"

> Enter the name of the mail group to be used for sending STAT/NOW active order notifications.

- "PRIORITIES FOR NOTIFICATION:"

> Select the priorities / schedules for notifications to be sent to the mail group defined in the "STAT NOW MAIL GROUP" parameter above.

> If this parameter is empty / not defined, the priority set in the PRIORITIES FOR PENDING NOTIFY parameter via the SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option will be used (if defined).

> If the PRIORITIES FOR PENDING NOTIFY and PRIORITIES FOR ACTIVE NOTIFY parameters of the SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option, and the PRIORITIES FOR NOTIFICATION parameter of the INPATIENT WARD PARAMETERS EDIT \[PSJ IWP EDIT\] option are all empty / not defined then notifications will be sent for priorities of STAT and ASAP, and schedules of NOW and STAT.

Example: Inpatient Ward Parameters Edit

Select PARameters Edit Menu Option: IWP Inpatient Ward Parameters Edit

Select WARD: 2 NORTH

DAYS UNTIL STOP DATE/TIME: 8// ?

Enter the number (1-100) of days that an order will last.

DAYS UNTIL STOP DATE/TIME: 8// \<Enter\>

DAYS UNTIL STOP FOR ONE-TIME: ?

Enter the number of days a one-time order should last. The number can be

from 1-100, however, it cannot exceed the number of days that standard

orders last (DAYS UNTIL STOP DATE/TIME).

DAYS UNTIL STOP FOR ONE-TIME: \<Enter\>

SAME STOP DATE ON ALL ORDERS: YES// ?

Answer 'YES' (or '1') if all of a patient's orders are to stop on the same

date/time.

Choose from:

1 YES

0 NO

SAME STOP DATE ON ALL ORDERS: YES// \<Enter\>

TIME OF DAY THAT ORDERS STOP: 2400// ?

Enter the time of day that orders stop for this ward (military time).

ENTER A NUMBER BETWEEN 0001 AND 2400. THE ZEROS ARE NEEDED.

TIME OF DAY THAT ORDERS STOP: 2400// \<Enter\>

DEFAULT START DATE CALCULATION: USE NEXT ADMIN TIME AS DEFAULT // ?

Enter "0" to use the closest admin time, "1" to use the next admin time,

or "2" to use "now" as the default start time for orders.

Choose from:

0 USE CLOSEST ADMIN TIME AS DEFAULT

1 USE NEXT ADMIN TIME AS DEFAULT

2 USE NOW AS DEFAULT

DEFAULT START DATE CALCULATION: USE NEXT ADMIN TIME AS DEFAULT // \<Enter\>

START TIME FOR 24 HOUR MAR: ?

Enter the time of day (0001-2400) that the 24 MAR is to start.

PLEASE USE MILITARY TIME WITH LEADING AND TRAILING ZEROS.

START TIME FOR 24 HOUR MAR: \<Enter\>

HOURS OF RECENTLY DC/EXPIRED: ?

Enter a number between 1 and 120. Any orders discontinued/expired within

the hours specified here will be displayed on the patient profile.

HOURS OF RECENTLY DC/EXPIRED: 24

LABEL FOR WARD STAFF: ?

Choose from:

0 NO LABELS

1 FIRST LABEL ON ORDER ENTRY/EDIT

2 LABEL ON ENTRY/EDIT AND VERIFICATION

3 FIRST LABEL ON NURSE VERIFICATION

LABEL FOR WARD: \<Enter\>

WARD LABEL PRINTER POINTER: \<Enter\>

LABEL FOR PHARMACY: ?

Choose from:

0 NO LABELS

1 FIRST LABEL ON ORDER ENTRY/EDIT

2 LABEL ON ENTRY/EDIT AND VERIFICATION

3 FIRST LABEL ON PHARMACIST VERIFICATION

LABEL FOR PHARMACY: \<Enter\>

PHARMACY LABEL PRINTER POINTER: \<Enter\>

LABEL ON AUTO-DISCONTINUE: ?

Answer 'YES' to have labels created when this ward's patients' orders are

auto-discontinued.

Choose from:

1 YES

0 NO

LABEL ON AUTO-DISCONTINUE: \<Enter\>

MAR HEADER LABELS: ?

Enter "YES" if MAR header labels should be generated for this ward.

Choose from:

1 YES

MAR ORDER SELECTION DEFAULT: ?

Answer must be 1-10 characters in length.

Enter the number corresponding to the type of orders to be included on

MARs printed for this ward. Multiple types (except 1) may be selected

using "-" or "," as delimiters.

Choose from:

1 - All Medications

2 - Non-IV Medications only

3 - IV Piggybacks

4 - LVPs

5 - TPNs

6 - Chemotherapy Medications (IV)

MAR ORDER SELECTION DEFAULT: 1 1 - All Medications

PRINT PENDING ORDERS ON MAR: ?

'SELF MED' IN ORDER ENTRY: ?

Answer 'YES' to have the prompts for patient self-medication included in

the order entry process.

Choose from:

1 YES

0 NO

'SELF MED' IN ORDER ENTRY: \<Enter\>

PRE-EXCHANGE REPORT DEVICE: ?

Enter a device on which the Pre-Exchange Report may be printed.

Answer with DEVICE NAME, or LOCATION OF TERMINAL, or LOCAL SYNONYM, or

\$I, or VOLUME SET(CPU), or DEFAULT SUBTYPE, or

FORM CURRENTLY MOUNTED, or \*PHYSICAL AREA

Do you want the entire DEVICE List?

PRE-EXCHANGE REPORT DEVICE:

STAT NOW MAIL GROUP: \<Enter\>

PRIORITIES FOR NOTIFICATION: ?

Choose from:

S STAT

SA STAT/ASAP

SAN STAT/ASAP/NOW

A ASAP

AN ASAP/NOW

N NOW

SN STAT/NOW

PRIORITIES FOR NOTIFICATION: \<Enter\>

Select WARD: \<Enter\>

AUto-Discontinue Set-Up

IUP Inpatient User Parameters Edit

IWP Inpatient Ward Parameters Edit

Clinic Definition

Systems Parameters Edit

Select PARameters Edit Menu Option:

### Systems Parameters Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ SYS EDIT\]

The PHARMACY SYSTEM file allows a hospital to tailor various aspects of the Unit Dose Medications module that affect the entire medical center. Currently the following fields can be edited by using the *Systems Parameters Edit* option.

- "NON-FORMULARY MESSAGE:"

> This is a message that will be shown to non-pharmacist users when ordering a non-formulary drug for a patient (a drug that is not currently stocked by the pharmacy). This is typically a warning and/or a procedure the non-pharmacist users must follow before the pharmacy will dispense the non-formulary drug. The message will show exactly as entered here.

- "EDIT Option:"

This field is used to edit the non-formulary message displayed above.

- "PRINT 6 BLOCKS FOR THE PRN MAR:"

> This field is used to indicate if 4 or 6 blocks are to be used for ONE-TIME/PRN orders on the 7/14 DAY MAR ONE-TIME/PRN SHEET. The 7/14 DAY MAR ONE-TIME/PRN SHEET will print 4 blocks if this field is UU<u>not</u>UU set to YES.

- "PRINT DIET ABBR LABEL ON MAR:"

> If this field contains a 1 or YES, the Dietetics Abbreviated Label will be printed on the MAR.

- "MAR SORT:"

> This parameter allows the sorting of the MAR by the order's schedule type or alphabetically by the medication names.

CHOOSE FROM:

> 0 Sort by order's Schedule Type and then by Medication Names

> 1 Sort by order's Medication Names

- "ATC SORT PARAMETER:"

> This parameter allows sending of the Pick List to the ATC machine by ATC mnemonic within Patient (as in Inpatient Medications versions up to 4.0), or else by admin time within patient.

CHOOSE FROM:

> 0 ATC MNEMONIC

> 1 ADMIN TIME

- "CALC UNITS NEEDED PRN ORDERS:"

This parameter controls whether or not the Units Needed will be calculated for the orders with PRN in the schedule field on the Pick List.

- "DAYS UNTIL STOP FOR ONE-TIME:"

This parameter indicates the number of days a one-time order should last if there is no ward parameter defined. This number can be between 1 and 30.

- "ROUND ATC PICK LIST UNITS:"

> This parameter allows the site to decide whether or not fractional units per dose will be rounded to the next whole number before the pick list is sent to the ATC.

- HOURS OF RECENTLY DC/EXPIRED: 1//

> This parameter allows the site to specify the time frame for recently discontinued/expired orders to display on the patient profiles.

- "EXPIRED IV TIME LIMIT:"

> Type the Number of Hours between 0 and 24 that continuous IV orders may be renewed after expiring.

- "PRIORITIES FOR PENDING NOTIFY:"

> Select the priorities / schedules for notifications to be sent to the PSJ STAT NOW PENDING ORDER mail group.

> If the PRIORITIES FOR PENDING NOTIFY and PRIORITIES FOR ACTIVE NOTIFY parameters of the SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option, and the PRIORITIES FOR NOTIFICATION parameter of the INPATIENT WARD PARAMETERS EDIT \[PSJ IWP EDIT\] option are all empty / not defined then notifications will be sent for priorities of STAT and ASAP, and schedules of NOW and STAT.

- "PRIORITIES FOR ACTIVE NOTIFY:"

> Select the priorities / schedules for notifications to be sent to the PSJ STAT NOW ACTIVE ORDER mail group.

> If this parameter is empty / not defined, the priority set in the PRIORITIES FOR PENDING NOTIFY parameter via the SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option will be used (if defined).

> If the PRIORITIES FOR PENDING NOTIFY and PRIORITIES FOR ACTIVE NOTIFY parameters of the SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option, and the PRIORITIES FOR NOTIFICATION parameter of the INPATIENT WARD PARAMETERS EDIT \[PSJ IWP EDIT\] option are all empty / not defined then notifications will be sent for priorities of STAT and ASAP, and schedules of NOW and STAT.

| ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/017.png) | Note: The "AUTO-DC IMO ORDERS:" field has been moved from the PHARMACY SYSTEM file to the CLINIC DEFINITION file. To access this field, use the *Clinic Definition* \[PSJ CD\] option under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option. |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Systems Parameters Edit

Select PARameters Edit Menu Option: SYStems Parameters Edit

NON-FORMULARY MESSAGE:

1\>This is the Non formulary message!!!

EDIT Option: ?

Choose, by first letter, a Word Processing Command

or type a Line Number to edit that line.

EDIT Option: ^

PRINT 6 BLOCKS FOR THE PRN MAR: ?

Enter 1 to allow 6 blocks to be printed for the ONE-TIME/PRN orders on the

7/14 DAY MAR ONE-TIME/PRN SHEET.

Choose from:

1 YES

PRINT 6 BLOCKS FOR THE PRN MAR: \<Enter\>

PRINT DIET ABBR LABEL ON MAR: ?

Enter 1 or Yes, the Dietetics Abbreviated Label will print on the MAR

Choose from:

1 YES

PRINT DIET ABBR LABEL ON MAR: \<Enter\>

MAR SORT: Sort by order's Medication Names.// ?

Choose from:

0 Sort by order's Schedule Type and then Medication Names.

1 Sort by order's Medication Names.

MAR SORT: Sort by order's Medication Names.// \<Enter\>

ATC SORT PARAMETER: ATC MNEMONIC// ?

Enter '0' to send Pick List to ATC by drug, '1' for admin time.

Choose from:

0 ATC MNEMONIC

1 ADMIN TIME

ATC SORT PARAMETER: ATC MNEMONIC// \<Enter\>

CALC UNITS NEEDED PRN ORDERS: YES// ?

Enter a 1 if you would like to have the UNITS NEEDED calculated for PRN

orders on the Pick List.

Choose from:

1 YES

CALC UNITS NEEDED PRN ORDERS: YES// \<Enter\>

DAYS UNTIL STOP FOR ONE-TIME: ?

Type a Number between 1 and 30, indicating the number of days a one-time

order should last if there is no ward parameter defined.

DAYS UNTIL STOP FOR ONE-TIME: \<Enter\>

ROUND ATC PICK LIST UNITS: YES// ?

The purpose of this field is to allow rounding of fractional doses to be

sent by the pick list to the ATC.

ROUND ATC PICK LIST UNITS: \<Enter\>

HOURS OF RECENTLY DC/EXPIRED: ?

Enter a number between 1 and 120. Any orders discontinued/expired within

the hours specified here will be displayed on the patient profile.

HOURS OF RECENTLY DC/EXPIRED: \<Enter\>

EXPIRED IV TIME LIMIT: ?

Type the Number of Hours between 0 and 24 that continuous IV orders may be

renewed after expiring

EXPIRED IV TIME LIMIT: \<Enter\>

PRIORITIES FOR PENDING NOTIFY: ?

Choose from:

S STAT

SA STAT/ASAP

SAN STAT/ASAP/NOW

A ASAP

AN ASAP/NOW

N NOW

SN STAT/NOW

PRIORITIES FOR ACTIVE NOTIFY: ?

Choose from:

S STAT

SA STAT/ASAP

SAN STAT/ASAP/NOW

A ASAP

AN ASAP/NOW

N NOW

SN STAT/NOW

PRIORITIES FOR ACTIVE NOTIFY: \<Enter\>

AUto-Discontinue Set-Up

IUP Inpatient User Parameters Edit

IWP Inpatient Ward Parameters Edit

Clinic Definition

Systems Parameters Edit

Select PARameters Edit Menu Option:

## PATient Order Purge – Temporarily Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU PO PURGE\]

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/018.png)Note: The *PATient Order Purge* option is "UU<u>Out of Order</u>UU" and UU<u>TEMPORARILY UNAVAILABLE</u>UU.

The *PATient Order Purge* option will start a background job to delete all orders for patients that have been discharged before or on the user-specified date. This option does not affect orders for currently admitted patients.

Patient order purge looks at the earliest start date of the last Pick List that has not been filed away and allows the user to purge orders three days before that start date.

This option is UU<u>very</u> CPU-intensive and should be queued to run at a time of day when the fewest users are on the system, such as on a weekend. The supervisor should only purge <u>several months</u> of data at one time.

## PIck List Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU PL MENU\]

The *PIck List Menu* option is used to control deletion of a pick list, auto purging parameters, and the physical purging of pick lists.

Example: Pick List Menu

Select Supervisor's Menu Option: ?

Administering Teams

Clinic Groups

MANagement Reports Menu ...

Non-Standard Schedule Report

Non-Standard Schedule Search

Order Set Enter/Edit

PARameters Edit Menu ...

PATient Order Purge

\*\*\> Out of order: TEMPORARILY UNAVAILABLE

PIck List Menu ...

Ward Groups

Select Supervisor's Menu Option: PIck List Menu

Delete a Pick List

PIck List Auto Purge Set/Reset

PUrge Pick Lists

### DElete a Pick List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU PLDEL\]

The *DElete a Pick List* option is used to delete the most recent pick list that has been run, but not filed away, for a ward group.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/019.png)Note: If the user deleting the pick list is not the user who created it, a MailMan message is sent to all users with the PSJU MGR key.

Example: Delete a Pick List

Select PIck List Menu Option: DElete a Pick List

Select WARD GROUP NAME: ?

Answer with WARD GROUP NAME

Choose from:

SOUTH WING

PHARMACY HOME

WEST WING

PHARMACY FIDO

Select WARD GROUP NAME: SOUTH WING

PHARMACY HOME

The last Pick List was last run for SOUTH WING

by PSJPHARMACIST,ONE on 02/05/01 13:42

Pick List number 76, for 02/03/01 13:21 through 02/04/01 13:20.

DO YOU WANT TO DELETE THIS PICK LIST? Y (Yes)

...a few moments, please......DONE!

### PIck List Auto Purge Set/Reset

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU PLAPS\]

The *PIck List Auto Purge Set/Reset* option allows the user (coordinator/supervisor) to start and stop the daily automatic deletions of pick lists that have been filed away. The user may specify the number of days (1-90) the pick lists remain on the system. When the supervisor wants the system to stop automatically deleting pick lists, the entry for this option can be deleted.

Example: Pick List Auto Purge Set/Reset

Select PIck List Menu Option: PIck List Auto Purge Set/Reset

DAYS 'FILED AWAY' PICK LISTS SHOULD LAST 1// ?

If a number is found in this field by the daily background job, the job will

completely delete all PICK LISTS that have been FILED AWAY and have been around

longer than the number of days specified in this field. Entering a number into

this field will effectively start the AUTO PURGE. DELETING this field will

effectively STOP the AUTO PURGE.

ENTER THE NUMBER (1-90) OF DAYS THAT PICK LISTS THAT ARE FILED AWAY MAY STAY

IN THE COMPUTER.

DAYS 'FILED AWAY' PICK LISTS SHOULD LAST 1// \<Enter\>

### PUrge Pick Lists 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU PLPRG\]

With the *PUrge Pick Lists* option, the user (coordinator/supervisor) can manually delete or purge all pick lists that are filed away and have a start date earlier than the date entered in this option.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/020.png)Note: Purging pick lists will not purge the statistics extracted from them when they are filed. That data is stored elsewhere when the pick lists are filed.

Example: Purge Pick Lists

Select PIck List Menu Option: PUrge Pick Lists

\*\* AUTO PURGE SET TO 1 DAYS, AS OF 02/22/98 14:43 \*\*

Enter PURGE STOP DATE: ?

If a date is entered here, all of the FILED AWAY PICK LISTS that started

before the entered date will be deleted.

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer assumes a date in the PAST.

If only the time is entered, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.

You may enter a time, such as NOON, MIDNIGHT or NOW.

You may enter NOW+3' (for current date and time Plus 3 minutes

\*Note--the Apostrophe following the number of minutes)

Enter PURGE STOP DATE: T-90 (NOV 10, 2000)

Pick list purge queued!

## Ward Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJU EWG\]

The Unit Dose Medications module makes use of wards as defined in the Ward Location file. The module allows the supervisor to group the wards (Ward Group) together in various orders to facilitate the preparation of reports and other functions. The *Pick List* option requires the use of Ward Groups. The *Ward Groups* option allows the package coordinator to name the Ward Groups, and enter or edit data in the Ward Group file. The name given to each Ward Group is an arbitrary choice that can be from 1 to 20 characters long.

When each Ward Group is created, the user will be prompted to assign a type to the Ward Group. The type is required, and cannot be edited, once chosen. (The Ward Group would have to be deleted if the type was no longer valid.) Pharmacy and MAS are the two types of Ward Group choices.

Pharmacy (type) Ward Groups are the only Ward Groups that can be selected by the *Pick List* options. Because of dose tracking and accountability, the same ward is not allowed in more than one Pharmacy type Ward Group. MAS (type) Ward Groups can be comprised of any wards grouped in any manner desired. Both MAS and Pharmacy type Ward Groups can be selected for the various other reports and functions.

Any number of wards can be entered into a Ward Group. A Ward Group need only have one ward in it.

Example: Ward Groups

Select Supervisor's Menu Option: WArd Groups

Select WARD GROUP NAME: ?

Answer with WARD GROUP NAME

Choose from:

NORTH WING

PHARMACY HOME

SOUTH WING

PHARMACY HOME

WEST WING

PHARMACY HOME

You may enter a new WARD GROUP, if you wish

Answer must be 1-20 characters in length.

Select WARD GROUP NAME: SOUTH WING

PHARMACY HOME

NAME: SOUTH WING// \<Enter\>

Select WARD: 2 EAST// \<Enter\>

LENGTH OF PICK LIST (in hours): 24// \<Enter\>

PICK LIST - OMIT WARD SORT: YES (DO NOT SORT BY WARD) // \<Enter\>

PICK LIST - OMIT ROOM-BED SORT: \<Enter\>

PICK LIST - ROOM/BED SORT: \<Enter\>

PICK LIST - FORM FEED/PATIENT: \<Enter\>

PICK LIST - FORM FEED/WARD: \<Enter\>

PICK LIST - LINES ON FORM FEED: \<Enter\>

PRINT NON-ACTIVE ORDERS FIRST: \<Enter\>

BAXTER ATC DEVICE: HOME// \<Enter\>

USE OLD ATC INTERFACE: \<Enter\>Select WARD GROUP NAME:

*(This page included for two-sided copying.)*

# SUPervisor's Menu (IV) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI SUPERVISOR\]

The *SUPervisor's Menu (IV)* option contains options only available to the applications coordinator. These include setting up site parameters, generating the IV AMIS report, and cost/usage reports.

Example: Supervisor's Menu (IV)

Select SUPervisor's Menu (IV) Option: ?

AUto-Discontinue Set-Up

CAtegory File (IV)

COmpile IV Statistics (IV)

Management Reports (IV) ...

Recompile Stats File (IV)

SIte Parameters (IV)

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select SUPervisor's Menu (IV) Option:

## AUto-Discontinue Set-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ AC SET-UP\]

The *AUto-Discontinue Set-Up* option allows the site to determine if a patient's Inpatient Medications (Unit Dose and IV) orders are to be automatically discontinued (d/c'd) or held when the patient is transferred between wards, between services, or to authorized absence.

The decision to discontinue Inpatient Medications orders is determined by the site, on a ward-by-ward, and/or service-by-service basis. While this process will entail extra set up on the site's part initially, it will allow the site almost complete control of the auto-discontinue process.

The set up for this process involves three main steps:

1.  UU<u>Auto-Discontinue for all wards:</u>UU If the site wants to have Inpatient Medications orders discontinued on all or most ward transfers, the supervisor can have the module automatically set up all wards as 'from' and 'to' wards, saving some time. When this option is chosen, wards currently marked as inactive will also be included. The user can still delete, edit, or add 'from' and 'to' wards at any time. See step 2C for further information.
2.  UU<u>Ward transfers:</u>UU The supervisor will select a 'from' ward. This is a ward from which a patient may be transferred. For each 'from' ward, the user can:
1.  Select an 'On Pass' action. This is the action the Inpatient Medications package will take on a patient's orders whenever the patient is transferred from the selected 'from' ward to authorized absence <u>less than</u> 96 hours (known as 'On Pass'). The possible actions are:
- Discontinue the orders
- Place the orders on hold
- Take no action
2.  Select an 'Authorized Absence' action. This is the action the Inpatient Medications package will take on a patient's orders whenever the patient is transferred from the selected 'from' ward to authorized absence <u>greater than</u> 96 hours. The possible actions are:
- Discontinue the orders
- Place the orders on hold
- Take no action
3.  Select an 'Unauthorized Absence' action. This is the action the Inpatient Medications package will take on a patient's orders whenever the patient is transferred from the selected 'from' ward to unauthorized absence <u>g</u>U<u>reater than</u> 96 hours. The possible actions are:
- Discontinue the orders
- Place the orders on hold
- Take no action
4.  Select the 'To' wards. Whenever a patient is transferred from the selected 'from' ward to any of the selected 'to' wards, the patient's IV and Unit Dose orders will be discontinued. For example, if 1 North is selected as a 'from' ward and 1 South is selected as a 'to' ward, any time a patient is transferred FROM 1 North TO 1 South, the patient's Inpatient Medications orders will be discontinued.

> This process is one way only. For example, if the site also wants orders to be discontinued whenever a patient is transferred FROM 1 South TO 1 NORTH, the user will have to enter 1 South as a 'from' ward and then enter 1 North as one of its 'to' wards.

3.  U<u>Service transfers:</u>UU The supervisor will select a 'from' service. This is a service from which a patient may be transferred. For each 'from' service, the user can select the 'to' services. Whenever a patient is transferred from the selected 'from' service to any of the selected 'to' services, the patient's IV and Unit Dose orders will be discontinued. For example, if Medicine is selected as a 'from' service and SURGERY is selected as a 'to' service, any time a patient is transferred FROM MEDICINE TO SURGERY, the patient's Inpatient Medications orders will be discontinued.

> This process is also one way only. For example, if the site also wants orders to be discontinued whenever a patient is transferred FROM SURGERY TO MEDICINE, the user will have to enter SURGERY as a 'from' service and then enter Medicine as one of its 'to' services.

> If all of the wards are set for auto d/c, it is not necessary to enter services.

> If there is a specific ward or service for which the site does not want Inpatient Medications orders d/c'd, then the supervisor only needs to delete the 'to' ward or service.

> Inpatient Medications orders are always automatically d/c'd whenever the patient is admitted, discharged, or transferred to unauthorized absence.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/021.png) Note: Pending orders that are auto discontinued will UU<u>NEVER</u>UU be re-instated.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/022.png) Note: When the Patient Information Management System (PIMS) deletes a patient movement, the medication orders that were discontinued due to the movement are automatically reinstated. There are checks included to prevent the reinstatement of an order if a new duplicate order has been added. For IVs, when the order to be reinstated has any additives the same as a new order, it will not be reinstated.

A mail message is sent to the PSJ-ORDERS-REINSTATED mail group when the medication orders are automatically reinstated due to the deletion of a patient movement. This message contains the patient's name, last four digits of the patient's social security number, current ward location, reason the orders were reinstated, and a list of the orders that were reinstated. The orders will be listed in the mail message in the same format as a patient profile. This notification also includes any orders that could not be reinstated due to duplicates existing on the system.

Example: Auto-Discontinue Set-Up

Select SUPervisor's Menu (IV) Option: AUto-Discontinue Set-Up

Do you want the instructions for auto-discontinue set-up? Yes// N (No)

Do you want the package to set-up all of your wards for auto-discontinue? No// \<Enter\> (No)

(Action on WARD transfer)

Select FROM WARD: 1 EAST// \<Enter\>

FROM WARD: 1 EAST//

'ON PASS' ACTION: DISCONTINUE ORDERS// \<Enter\>

ACTION ON AUTHORIZED ABSENCE: DISCONTINUE ORDERS // \<Enter\>

ACTION ON UNAUTHORIZED ABSENCE: DISCONTINUE ORDERS // \<Enter\>

Select TO WARD: 2 EAST// \<Enter\>

Select FROM WARD: \<Enter\>

(Action on SERVICE transfer)

Select FROM SERVICE: PSYCHIATRY// \<Enter\>

FROM SERVICE: PSYCHIATRY// \<Enter\>

Select TO SERVICE: NHCU// \<Enter\>

Select FROM SERVICE: \<Enter\>

AUto-Discontinue Set-Up

CAtegory File (IV)

COmpile IV Statistics (IV)

Management Reports (IV) ...

Recompile Stats File (IV)

SIte Parameters (IV)

Select SUPervisor's Menu (IV) Option

## CAtegory File (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### \[PSJI IVCATEGORY\]

############################### 

############################### The *CAtegory File (IV)* option allows the supervisor to group drugs into categories. Within this file, the user can create a new drug category, add drugs to an existing drug category, or delete drugs from previously defined categories. Once a drug category is created, provider cost reports, ward/drug usage cost reports, and drug cost reports can be run for that drug category.

############################### 

############################### The advantage of this file is that the user can create custom-tailored reports. Examples of customized reports are drug utilization sets, restricted drugs by provider, reports by IV type, or any grouping of drugs that have something in common.

############################### 

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><p id="note-called-out-with-pencil-icon" class="heading unnumbered">![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/023.png)</p></th>
<th><p id="note-the-last-drug-entered-into-a-category-will-always-be-the-default-drug-at-the-select-iv-drug-prompt-when-re-entering-the-category.-to-get-a-list-of-drugs-in-a-category-type-a-question-mark-at-the-select-iv-drug-prompt." class="heading unnumbered">Note: The last drug entered into a category will always be the default drug at the "Select IV DRUG:" prompt when re-entering the category. To get a list of drugs in a category, type a question mark (?) at the "Select IV DRUG:" prompt.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

############################### 

Example: Category File (IV)

Select SUPervisor's Menu (IV) Option: CAtegory File (IV)

Select IV CATEGORY NAME: ?

Answer with IV CATEGORY NAME:

TEST

You may enter a new IV CATEGORY, if you wish

Answer must be 1-40 characters in length.

Select IV CATEGORY NAME: \<Enter\> TEST

NAME: TEST// \<Enter\>

Select IV DRUG: D10W// \<Enter\>

IV DRUG: D10W// \<Enter\>

GENERIC DRUG: DEXTROSE 10% 1000ML // (No Editing)

Select IV DRUG: \<Enter\>

AUto-Discontinue Set-Up

CAtegory File (IV)

COmpile IV Statistics (IV)

Management Reports (IV) ...

PUrge Data (IV) ...

\*\*\> Out of order: TEMPORARILY UNAVAILABLE

Recompile Stats File (IV)

SIte Parameters (IV)

Select SUPervisor's Menu (IV) Option:

############################### 

############################### To delete a drug from a category, the user must choose the drug by typing in the drug name at the "Select IV DRUG:" prompt. The next prompt asks if the system has selected the correct drug (answer \<Enter\> for Yes if correct). At the following "Select IV DRUG:" prompt, the drug appears as the default drug. To delete the drug from the category, type an "at" symbol (@) at the prompt.

############################### 

Example: Delete a Drug from a Category

Select SUPervisor's Menu (IV) Option: CAtegory File (IV

Select IV CATEGORY NAME: DEX

NAME: DEX// \<Enter\>

Select IV DRUG: D5%// ?

Answer with IV DRUG

Choose from:

D10W DEXTROSE 10% 1000ML

D5% DEXTROSE 5% 1000ML

You may enter a new IV DRUG, if you wish

Enter one of the following:

A.EntryName to select a IV ADDITIVES

S.EntryName to select a IV SOLUTIONS

To see the entries in any particular file type \<Prefix.?\>

Select IV DRUG: D5%// D10

Searching for a IV ADDITIVES, (pointed-to by IV DRUG)

Searching for a IV SOLUTIONS, (pointed-to by IV DRUG)

D10W D10W TEST PRINT NAME 2 1000 ML

...OK? Yes// \<Enter\> (Yes) DEXTROSE 10% 1000ML

IV DRUG: D10W// @

SURE YOU WANT TO DELETE THE ENTIRE IV DRUG? Yes

Select IV DRUG:

## COmpile IV Statistics (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI COMPILE STATS\]

Statistical data is stored in a holding area each time a label is printed. The *IV Background job* option and the *COmpile IV Statistics (IV)* option both merge the information into the IV STATS file and delete any data which is older than the age specified in the site parameter, DAYS TO RETAIN IV STATS. This will be a number between 100 and 2000 days. If no entry is made for this parameter, this number will default to 100 days. This option is a menu option that allows the job to be started manually in cases where the data must be compiled before the automatic background job *IV Background job* runs that night.

It is suggested that the *IV Background job* option be set up to run nightly to ensure that the IV STATS file is kept up to date. The reports that capture data from the IV STATS file do not include any information waiting to be merged from the holding area. Contact the Information Resources Management Service (IRMS) Chief or Site Manager to have this task scheduled.

<u>Problem with IV STATS File</u>UU

When labels are printed or returns are entered for an IV order, a transaction entry is added to the IV Stats file. These entries are later compiled either manually using the *Compile IV Statistics (IV)* option on the *Supervisor's menu (IV)*, or by the *IV Background job* that should be scheduled to run each night. When these entries are compiled, all additives in the order are counted as usage for each label printed or returned, regardless of whether the additive was included on the label or in the returned bottle.

<span id="Orphan_Paragraph_Title" class="anchor"></span>

Example: Hyperal Order

SODIUM CHLORIDE 40 MEQ 1,2

POTASSIUM CHLORIDE 30 MEQ 3

K PHOS 10 MM 3

MVI CONC 5 ML

D 50 W 500 ML

125 ml/hr

When a single label is printed for this order and counted as usage, Potassium Chloride and K Phos will be counted in the IV Stats file, even though these additives were not printed on the label as they were to be included only in bottle 3.

## Management Reports (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### \[PSJI MANAGEMENT REPORTS\]

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/024.png) Users must hold the PSJI MGR key for access to this option.

The *Management Reports (IV)* option allows the user to print reports from data compiled by the IV module. Those reports requiring 132-column paper are so noted in the menu options. If no paper width is indicted, standard 80-column width is assumed.

Example: Management Reports (IV)

Select Management Reports (IV) Option: ?

ACtive Order Report by Ward/Drug (IV)

AMIS (IV)

Drug Cost Report (132 COLUMNS) (IV)

PCR Patient Cost Report (132 COLUMNS) (IV)

PSD Patients on Specific Drug(s)

PRovider Drug Cost Report(132 COLUMNS) (IV)

Ward/Drug Usage Report (132 COLUMNS) (IV)

Select Management Reports (IV) Option:

### ACtive Order Report by Ward/Drug (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI AOR\]

The *ACtive Order Report by Ward/Drug (IV)* option allows the user to capture all active orders that exist for a specific ward, broken down by drug. At the "Select Ward:" prompt, a specific ward, Outpatient IVs (by entering ^OUTPATIENT) or all wards (by entering ^ALL) can be selected. At the "Select DRUG:" prompt, the user can select a specific drug, or all drugs (by entering ^ALL).

Select Management Reports (IV) Option: ACtive Order Report by Ward/Drug (IV)

Select Ward (or enter ^ALL or ^OUTPATIENT): ?

This active order report will list all active orders within the

ward that you specify. You may select a specific ward. You may

also select Outpatient orders by entering ^OUTPATIENT or you may

select all wards by entering ^ALL.

Select Ward (or enter ^ALL or ^OUTPATIENT): ^ALL

Select DRUG (or enter ^ALL): ?

This active order report will list all active orders containing

the specified drug. You may pick a single drug or you may select

all drugs by entering ^ALL.

Select DRUG (or enter ^ALL): ^ALL

DEVICE: NT TELNET TERMINAL// 0;80;9999 NT/Cache virtual TELNET terminal

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

Active Order Report by Ward/Drug For: ALL WARDS, ALL DRUGS

Printed by: PSJPHARMACIST,ONE on FEB 8,2001@22:55:37 PAGE: 1

IV ROOM/WARD/NAME/ORDER STOP DATE PROVIDER

================================================================================

IV ROOM: BIRMINGHAM ISC

WARD: 1 EAST

PSJPATIENT,ONE 0001

\[342\] P FEB 16,2001@16:54 PSJPROVIDER,ONE

ATROPINE 1 MG

0.9% NACL 500 ML

INFUSE OVER 10 MIN.

QID 01-09-15-20

Cumulative doses: 0

\[343\] A FEB 11,2001@16:54 PSJPROVIDER,ONE

AMPICILLIN 100 GM

0.9% NACL 500 ML

100 ml/hr

Cumulative doses: 0

ACtive Order Report by Ward/Drug (IV)

AMIS (IV)

Drug Cost Report (132 COLUMNS) (IV)

PCR Patient Cost Report (132 COLUMNS) (IV)

PSD Patients on Specific Drug(s)

PRovider Drug Cost Report (132 COLUMNS) (IV)

Ward/Drug Usage Report (132 COLUMNS) (IV)

Select Management Reports (IV) Option:

<span id="EX_PSJI_AOR" class="anchor"></span>Example: IV Additives

Select OPTION NAME: ACTIVE ORDER REPORT BY WARD/DR PSJI AOR ACtive Order Re

port by Ward/Drug (IV)

ACtive Order Report by Ward/Drug (IV)

Select IV ROOM NAME: XXXXXX IV ROOM

You are signed on under the XXXXXX IV ROOM IV ROOM

Current IV LABEL device is: FTA

Current IV REPORT device is: FTA

Select Ward (or enter ^ALL or ^OUTPATIENT): ^ALL

Select DRUG (or enter ^ALL): PIP

1 PIPERACILLIN/TAZOBACTAM 12-03-15 Additive Strength: 3.375 GM

2 PIPERACILLIN/TAZOBACTAM Additive Strength: 2.25 GM

3 PIPERACILLIN/TAZOBACTAM Additive Strength: 4.5 GM

> **NOTE:** Additive \#1 has an "inactivation date" of 12-03-15

Example: IV Solutions

Select OPTION NAME: PSJI AOR ACtive Order Report by Ward/Drug (IV)

ACtive Order Report by Ward/Drug (IV)

Select Ward (or enter ^ALL or ^OUTPATIENT): ^ALL

Select DRUG (or enter ^ALL): DEXTROSE 5% / NACL ??

1 DEXTROSE 5% / NACL 0.2% 1000 ML

2 DEXTROSE 5% / NACL 0.33% 1000 ML

3 DEXTROSE 5% / NACL 0.45% 1000 ML 12-03-15

4 DEXTROSE 5% / NACL 0.9% 1000 ML

CHOOSE 1-4:

> **NOTE:** Solution \#3 has an "inactivation date" of 12-03-15

### AMIS (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI AMIS\]

The *AMIS (IV)* option allows the user to run a report that captures the IV workload of the pharmacy by ward. Only those wards with a dispensing amount will be included. The user will be prompted to select a start date and a stop date to set the time span for which the costs will be calculated.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/025.png)Note: Canceled, recycled or destroyed IV bags are not subtracted out of the total bag count on the AMIS report.

Example: AMIS (IV) Report

Select Management Reports (IV) Option: AMIS (IV)

The IV BACKGROUND JOB \[PSJI BACKGROUND JOB\] that compiles IV cost data

was last successfully run on: FEB 8,2001@22:52:18

The oldest cost data for room: BIRMINGHAM ISC goes back to: JUN 29,1999

Enter Start Date: T-1000 (MAY 15, 1998)

Enter End Date: T (FEB 08, 2001)

DEVICE: NT TELNET TERMINAL// 0;80;999 NT/Cache virtual TELNET terminal

IV AMIS REPORT Page No. 1

FROM MAY 15,1998 THROUGH FEB 8,2001 FEB 8,2001

TOTAL AVERAGE

TYPE DISPENSED (BAGS) COST

================================================================================

IV ROOM BIRMINGHAM ISC

1 EAST

Piggyback 96 5.4882

Admixture 3 1.1089

Hyperal 0 0.0000

Syringe 0 0.0000

Chemotherapy 1 0.4670

\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTAL FOR WARD 100 5.3066

2 EAST

Piggyback 79 1.2436

Admixture 4 0.9830

Hyperal 0 0.0000

Syringe 0 0.0000

Chemotherapy 0 0.0000

\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTAL FOR WARD 83 1.2311

================

\*TOTAL FOR IV ROOM: BIRMINGHAM ISC 6.5377

\*Piggyback 175 3.5721

\*Admixture 7 1.0370

\*Hyperal 0 0.0000

\*Syringe 0 0.0000

\*Chemotherapy 1 0.4670

FINISHED PRINTING ON: FEB 8,2001@23:07:41

### Drug Cost Report (132 COLUMNS) (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI DRUG COST REPORT\]

The *Drug Cost Report (132 COLUMNS) (IV)* option allows the user to capture the total dispensing cost for an IV drug. The system will give the date of the oldest cost data on file for the IV room selected and proceed to prompt the user for more information. The user is asked to select a start date and a stop date to set the time span for which the costs will be calculated. Once a stop date is entered and the selection of the type of cost report (regular or condensed), the system will prompt for a drug name. The user can select a specific drug, all drugs (by entering ^ALL), all non-formulary drugs (by entering ^NON), a category of drugs (by entering ^CAT), a VA drug class (by entering ^VADC), or an IV type, such as piggyback or syringe (by entering ^TYPE). The user can request a high/low drug cost report (by entering ^HIGH). The user will be prompted whether to include patient data. When a regular (non-condensed) report has been selected, the system will prompt whether the report should include ward data.

The Drug Cost Report includes bag and cost summaries at the end of the report, as well as the grand total costs for dispensed, destroyed, recycled, and canceled IV bags. Total drug units and total drug costs are listed for each drug in the report.

The following formulas are used to calculate the results in the Bag and Cost Summaries:

UU<u>Bag Summary</u>

- % Destroyed = (Grand Total Destroyed/Grand Total Bags Dispensed) \* 100%
- % Recycled = (Grand Total Recycled/Grand Total Bags Dispensed) \* 100%
- % Canceled = (Grand Total Canceled/Grand Total Bags Dispensed) \* 100%

UU<u>Cost Summary</u>

- % Destroyed = (Grand Total Destroyed/Grand Total Bags Dispensed) \* 100%
- % Recycled = (Grand Total Recycled/Grand Total Bags Dispensed) \* 100%
- % Canceled = (Grand Total Canceled/Grand Total Bags Dispensed) \* 100%

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/026.png)Note: Grand Total Column for bags is not shown in the drug cost report. All summaries are in relation to Dispensed Bags and Dispensed Cost.

<u>Additional Computations in Drug Cost Report</u>

This report breaks down each drug by ward. The Total Drug Units for each drug is calculated using the following formulas:

- Total Drug Units = Total Drug Units Dispensed – Total Drug Units Recycled – Total Drug units Canceled
- Total Drug Cost = Total Drug Cost Dispensed – Total Drug Cost Recycled – Total Drug Cost Canceled
- Total Bags for Drug = Total Bags Dispensed – Total Bags Recycled – Total Bags Canceled
- Total Drug Cost = Total Drug Units \* Drug Cost per Unit
- Grand Total Cost = Grand Total Cost Dispensed – Grand Total Cost Recycled – Grand Total Cost Canceled

Example: Drug Cost Report (IV)

Select Management Reports (IV) Option: Drug Cost Report (132 COLUMNS) (IV)

The IV BACKGROUND JOB \[PSJI BACKGROUND JOB\] that compiles IV cost data

was last successfully run on: FEB 8,2001@22:52:18

\*\*WARNING\*\* that was \<5\> days ago. PLEASE contact your site manager.

Cost data is probably not accurate because of this.

The oldest cost data for room: BIRMINGHAM ISC goes back to: JUN 29,1999

Enter Start Date: 6/29/00 (JUN 29, 2000)

Enter End Date: T (FEB 13, 2001)

Select one of the following:

C Condensed

R Regular

(R)egular or (C)ondensed: Regular// \<Enter\>

Select IV room: ^ALL// BIRMINGHAM ISC

Select DRUG:

or ^ALL (All drugs):

or ^NON (Non-formulary drugs):

or ^CAT (Category of drugs):

or ^VADC (VA drug class):

or ^HIGH (H/L cost):

or ^TYPE (IV type):^TYPE

Select IV TYPE: ADMIXTURE

DEVICE: NT TELNET TERMINAL// 0;132;999 NT/Cache virtual TELNET terminal

IV DRUG COST REPORT (REGULAR) FOR: PAGE:1

JUN 29,2000 THROUGH FEB 13,2001

IV ROOM: BIRMINGHAM ISC

IV TYPE: ADMIXTURE

PRINTED BY: PSJPHARMACIST,ONE ON FEB 13, 2001@09:41:51

UNITS

IV ROOM/DRUG/WARD DISPENSED (DESTROYED) RECYCLED CANCELLED COST

=================================================================================================

IV ROOM: BIRMINGHAM ISC

AMPHOTERICIN B 1 BAGS 0 BAGS 0 BAGS 0 BAGS 1 BAGS

WARD: 1 EAST 1.00 MG 0.00 0.00 0.00 \$ 0.31

========== ========== ========== ========== ============

TOTAL DRUG UNITS: 1.00 MG 0.00 0.00 0.00 1.00

========== ========== ========== ========== ============

TOTAL DRUG COST: \$ 0.31 \$ 0.00 \$ 0.00 \$ 0.00 \$ 0.31

D5-0.45% NACL 500 ML 1 BAGS 0 BAGS 0 BAGS 0 BAGS 1 BAGS

WARD: 1 EAST 500.00 ML 0.00 0.00 0.00 \$ 0.25

========== ========== ========== ========== ============

TOTAL DRUG UNITS: 500.00 ML 0.00 0.00 0.00 500.00

========== ========== ========== ========== ============

TOTAL DRUG COST: \$ 0.25 \$ 0.00 \$ 0.00 \$ 0.00 \$ 0.25

========== ========== ========== ========== ============

========== ========== ========== ========== ============

GRAND TOTAL COST: \$ 0.56 \$ 0.00 \$ 0.00 \$ 0.00 \$ 0.56

IV DRUG COST REPORT (REGULAR) FOR: PAGE:2

JUN 29,2000 THROUGH FEB 13,2001

IV ROOM: BIRMINGHAM ISC

IV TYPE: ADMIXTURE

PRINTED BY: PSJPHARMACIST,ONE ON FEB 13, 2001@09:41:51

=================================================================================================

BAG SUMMARY:

DESTROYED = 0.00 % OF DISPENSED BAGS

RECYCLED = 0.00 % OF DISPENSED BAGS

CANCELLED = 0.00 % OF DISPENSED BAGS

COST SUMMARY:

DESTROYED = 0.00 % OF DISPENSED COST

RECYCLED = 0.00 % OF DISPENSED COST

CANCELLED = 0.00 % OF DISPENSED COST

FINISHED PRINTING ON: FEB 13,2001@09:41:51

### Patient Cost Report (132 COLUMNS) (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI PATIENT COST\]

The *Patient Cost Report (132 COLUMNS) (IV)* option allows the user to capture the total IV dispensing cost for a patient. The system will prompt the user to select a start date and a stop date that will set the time span for which the costs will be calculated.

Example 1: Patient Cost Report (IV)

Select Management Reports (IV) Option: Patient Cost Report (132 COLUMNS) (IV)

The IV BACKGROUND JOB \[PSJI BACKGROUND JOB\] that compiles IV cost data

was last successfully run on: FEB 8,2001@22:52:18

The oldest cost data for room: BIRMINGHAM ISC goes back to: JUN 29,1999

Enter Start Date: T-1000 (MAY 15, 1998)

Enter End Date: T (FEB 08, 2001)

Select PATIENT: PSJPATIENT,ONE 000000001 1 EAST

DEVICE: NT TELNET TERMINAL// 0;132;999 NT/Cache virtual TELNET terminal

FEB 8,2001

PATIENT COST REPORT FOR: PAGE 1

PSJPATIENT,ONE PID: 000-00-0001

MAY 15,1998 THROUGH FEB 8,2001

WARD: 1 EAST

DOB: AUG 18,1920 SEX: MALE

Weight (kg): NF

DX: TEST

DRUG NAME DISPENSED (DESTROYED) RECYCLED CANCELLED DRUG COST

=================================================================================================

0.9% NACL 500 ML 1000.00 ML 0.00 0.00 0.00 \$ 468.0000

0.9% NaCl 250 ML 2750.00 ML 0.00 0.00 0.00 \$ 4.9500

AMPICILLIN 31.00 GM 0.00 0.00 0.00 \$ 15.8100

CIMETIDINE 300MG PREMIX 1.00 UNITS 0.00 0.00 0.00 \$ 0.0000

D5-0.2% NaCl 1000 ML 4000.00 ML 0.00 0.00 0.00 \$ 2.0800

D5-0.45% NaCl 1000 ML 1000.00 ML 0.00 0.00 0.00 \$ 1.2100

MORPHINE SULFATE 1.00 MG 0.00 0.00 0.00 \$ 0.4500

MULTIVITAMINS 10.00 ML 0.00 10.00 0.00 \$ 0.0000

PRIMAXIN 5.00 MG 0.00 0.00 0.00 \$ 0.1450

THEOPHYLLINE 200MG PREMIX 2.00 UNITS 0.00 0.00 0.00 \$ 2.5560

==========

GRAND TOTAL: \$ 495.2010

FINISHED PRINTING ON: FEB 8,2001@23:10:03

Example 2: Patient Cost Report (IV) Additives

Select OPTION NAME: PSJI DRUG COST REPORT Drug Cost Report (132 COLUMNS) (IV)

Drug Cost Report (132 COLUMNS) (IV)

The IV BACKGROUND JOB \[PSJI BACKGROUND JOB\] that compiles IV cost data

was last successfully run on: MAY 25,1999@11:42:02

\*\*WARNING\*\* that was \<6036\> days ago. PLEASE contact your site manager.

Cost data is probably not accurate because of this.

The oldest cost data for room: TST ISC ROOM goes back to: MAR 5,2002

The oldest cost data for room: XXXXXX IV ROOM goes back to: ??

Enter Start Date: T-500 (JUL 21, 2014)

Enter End Date: T (DEC 03, 2015)

Select one of the following:

C Condensed

R Regular

(R)egular or (C)ondensed: Regular//

Select IV room: ^ALL//

Select DRUG:

or ^ALL (All drugs):

or ^NON (Non-formulary drugs):

or ^CAT (Category of drugs):

or ^VADC (VA drug class):

or ^HIGH (H/L cost):

or ^TYPE (IV type):PIP

1 PIPERACILLIN/TAZOBACTAM 12-03-15 Additive Strength: 3.375 GM

2 PIPERACILLIN/TAZOBACTAM Additive Strength: 2.25 GM

3 PIPERACILLIN/TAZOBACTAM Additive Strength: 4.5 GM

> **NOTE:** Additive \#1 has an "inactivation date" of 12-03-15

Example 3: Patient Cost Report (IV) Solutions

Select OPTION NAME: PSJI DRUG COST REPORT Drug Cost Report (132 COLUMNS) (IV)

Drug Cost Report (132 COLUMNS) (IV)

The IV BACKGROUND JOB \[PSJI BACKGROUND JOB\] that compiles IV cost data

was last successfully run on: MAY 25,1999@11:42:02

\*\*WARNING\*\* that was \<6036\> days ago. PLEASE contact your site manager.

Cost data is probably not accurate because of this.

The oldest cost data for room: TST ISC ROOM goes back to: MAR 5,2002

The oldest cost data for room: XXXXXX IV ROOM goes back to: ??

Enter Start Date: T-500 (JUL 21, 2014)

Enter End Date: T (DEC 03, 2015)

Select one of the following:

C Condensed

R Regular

(R)egular or (C)ondensed: Regular//

Select IV room: ^ALL//

Select DRUG:

or ^ALL (All drugs):

or ^NON (Non-formulary drugs):

or ^CAT (Category of drugs):

or ^VADC (VA drug class):

or ^HIGH (H/L cost):

or ^TYPE (IV type):DEXTROSE 5% / NACL ??

1 DEXTROSE 5% / NACL 0.2% 1000 ML

2 DEXTROSE 5% / NACL 0.33% 1000 ML

3 DEXTROSE 5% / NACL 0.45% 1000 ML 12-03-15

4 DEXTROSE 5% / NACL 0.9% 1000 ML

CHOOSE 1-4:

> **NOTE:** Solution \#3 has an "inactivation date" of 12-03-15

### Patients on Specific Drug(s) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ PDV\]

The *Patients on Specific Drug(s)* option creates a report that lists patients on specific Orderable Item(s), Dispense Drug(s), or VA class(es) of drugs. When more than one of these drugs is chosen, the user will have the option to only display patients with orders containing ALL of the selected drugs or classes. The default behavior will be to display patients with orders for ANY for the selected drugs or classes.

The user will be prompted for the start and stop dates. Orders that are active between these two dates will be listed on the report. The user then has the choice to see only IV orders, Unit Dose orders, or both types of orders. These orders may be sorted by patient name or by the start date of the orders. The user will choose to sort by Orderable Items, Dispense Drug, or VA class of drugs, and then choose one or multiple drugs or classes. If a single drug or class is chosen, the orders for that drug or class will be listed. If multiple drugs or classes are chosen, the patient must have an order for each of the drugs or classes for the patient and their orders to print. By using the "Select number of matches" prompt, the user may select how many of the items entered must be on the patient's record in order for the patient to be displayed in the report.

For example: Patient A has an order for ACETAMINOPHEN TAB, patient B has an order for ASPIRIN TAB, and patient C has orders for both. If the user chooses two Orderable Items (ACETAMINOPHEN TAB and ASPIRIN TAB) and enters '1' (default) on the number of matches screen, the orders of all three patients will print. If the user chooses two Orderable Items and enters '2' on the number of matches screen, only patient C's orders will print.

Selecting a parent VA class will function as if the user had selected all of its children classes manually. Users will also be able to select one or more divisions and/or wards, which will limit the results to print only patients from the locations entered. When selecting all divisions and all wards, an additional prompt is shown to allow selection of one pharmacy ward group for selected locations.

Example: Patients on Specific Drug(s) Report

Select Management Reports (IV) Option: Patients on Specific Drug(s)

Enter start date: T-9 (JAN 30, 2001)

Enter stop date: T (FEB 08, 2001)

List IV orders, Unit Dose orders, or All orders: ALL// \<Enter\>

Do you wish to sort by (P)atient or (S)tart Date: Patient// \<Enter\>

List by (O)rderable Item, (D)ispense Drug, or (V)A Class of Drugs: Orderable Item

Select PHARMACY ORDERABLE ITEM NAME: WARFARIN TAB

Dispense Drugs for WARFARIN are:

WARFARIN 10MG U/D

WARFARIN 5MG U/D

WARFARIN 2.5MG U/D

WARFARIN 2MG U/D

WARFARIN 5MG

WARFARIN 7.5MG U/D

WARFARIN 2.5MG

WARFARIN 2MG

WARFARIN 7.5MG

WARFARIN 10MG

Select PHARMACY ORDERABLE ITEM NAME: \<Enter\>

Select number of matches: 1// \<Enter\>

Select division: ALL// \<Enter\>

Select ward: ALL// \<Enter\>

You may optionally select a ward group...

Select a Ward Group: \<Enter\>

Select PRINT DEVICE: NT/Cache virtual TELNET terminal

...this may take a few minutes...

...you really should QUEUE this report, if possible...

Press RETURN to continue "^" to exit: \<Enter\>

02/08/01 PAGE: 1

LISTING OF PATIENTS WITH ORDERS CONTAINING ORDERABLE ITEM(S):

WARFARIN

FROM 01/30/01 00:01 TO 02/08/01 24:00

--------------------------------------------------------------------------------

Start Stop

Patient Order Date Date

--------------------------------------------------------------------------------

PSJPATIENT,ONE WARFARIN TAB 01/30 01/31

000-00-0001 Give: 5MG PO QPM PRN

1 EAST

WARFARIN TAB 01/30 01/31

Give: 5MG PO QPM PRN

### PROvider Drug Cost Report (132 COLUMNS) (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI PROVIDER REPORT\]

The *PROvider Drug Cost Report (132 COLUMNS) (IV)* option allows the user to capture the total IV dispensing cost for a provider. The system will prompt for a start date and a stop date for which the costs will be calculated. A specific provider can be selected or the system will capture data for all providers. The user may select one drug, ^ALL for all drugs, ^NON for non-formulary drugs only, ^CAT for category of drugs, or ^VADC for a VA drug class. A regular or condensed version of this report may be generated. The condensed version is listed in an 80-column format and includes IV room, provider name, and the total dispensing cost for the provider.

Example: Provider Drug Cost Report (IV)

Select Management Reports (IV) Option: PRovider Drug Cost Report (132 COLUMNS) (IV)

The IV BACKGROUND JOB \[PSJI BACKGROUND JOB\] that compiles IV cost data

was last successfully run on: FEB 8,2001@22:52:18

The oldest cost data for room: BIRMINGHAM ISC goes back to: JUN 29,1999

Enter Start Date: T-1000 (MAY 15, 1998)

Enter End Date: T (FEB 08, 2001)

Select one of the following:

C Condensed

R Regular

(R)egular or (C)ondensed: Regular// \<Enter\>

Select IV room: ^ALL// \<Enter\>

Select PROVIDER (or enter ^ALL): ^ALL

Select DRUG:

or ^ALL (All drugs):

or ^NON (Non-formulary drugs):

or ^CAT (Category of drugs):

or ^VADC (VA drug class):^ALL

DEVICE: NT TELNET TERMINAL// 0;132;99 NT/Cache virtual TELNET terminal

PROVIDER DRUG COST REPORT (REGULAR): PAGE:1

MAY 15,1998 THROUGH FEB 8,2001

ALL PROVIDERS

ALL DRUGS

ALL IV ROOMS

PROVIDER DISPENSED DESTROYED RECYCLED CANCELLED COST

================================================================================================

IV ROOM: BIRMINGHAM ISC

PROVIDER: PSJPHARMACIST,ONE

0.9% NACL 100 ML 300.00 ML 0.00 0.00 0.00 \$ 2.43

0.9% NACL 50 ML 400.00 ML 0.00 500.00 0.00 \$ -1.56

0.9% NACL 500 ML 1000.00 ML 0.00 0.00 0.00 \$ 468.00

0.9% NaCl 250 ML 40000.00 ML 0.00 0.00 0.00 \$ 72.00

AMPICILLIN 71.31 GM 0.00 0.00 0.00 \$ 36.37

CALCIUM GLUCONATE 10% 1.80 ML 0.00 0.00 0.00 \$ 0.09

CIMETIDINE 300MG PREMIX 7.00 UNITS 0.00 0.00 0.00 \$ 0.00

D10W 1000 ML D10W TEST 3000.00 ML 0.00 0.00 0.00 \$ 2.10

D5-0.45% NACL 500 ML 1000.00 ML 0.00 0.00 0.00 \$ 0.50

D5-0.45% NaCl 1000 ML 1000.00 ML 0.00 0.00 0.00 \$ 1.21

D5W 1000 ML D5W TEST 1000.00 ML 0.00 1000.00 0.00 \$ 0.00

DEXTROSE 20% 1666 ML 3332.00 ML 0.00 0.00 0.00 \$ 33.32

DEXTROSE 5% 25OML BAG 0.98 UNITS 0.00 0.00 0.00 \$ 0.96

HUMAN INSULIN REG 0.90 UNITS 0.00 0.00 0.00 \$ 0.00

MANNITOL 20% 8.50 ML 0.00 0.00 0.00 \$ 0.12

MULTIVITAMINS 10.00 ML 0.00 30.00 0.00 \$ -3.18

POTASSIUM CHLORIDE 4.37 MEQ 0.00 0.00 0.00 \$ 0.04

PRIMAXIN 5.00 MG 0.00 0.00 0.00 \$ 0.15

THEOPHYLLINE 200MG PREMIX 1.34 UNITS 0.00 0.00 0.00 \$ 1.71

--------

TOTAL FOR PROVIDER: PSJPHARMACIST,ONE \$ 614.27

PROVIDER: PSJPROVIDER,ONE

AMPHOTERICIN B 1.00 MG 0.00 0.00 0.00 \$ 0.31

AMPICILLIN 2.00 GM 0.00 0.00 0.00 \$ 1.02

D5-0.2% NaCl 1000 ML 4000.00 ML 0.00 0.00 0.00 \$ 2.08

D5-0.45% NACL 500 ML 500.00 ML 0.00 0.00 0.00 \$ 0.25

MORPHINE SULFATE 1.00 MG 0.00 0.00 0.00 \$ 0.45

THEOPHYLLINE 200MG PREMIX 1.00 UNITS 0.00 0.00 0.00 \$ 1.28

--------

TOTAL FOR PROVIDER: PSJPROVIDER,ONE \$ 5.39

GRAND TOTAL: ========

\$ 619.66

FINISHED PRINTING ON: FEB 8,2001@23:14:36

### Ward/Drug Usage Report (132 COLUMNS) (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI WARD/DRUG USAGE REPORT\]

The *Ward/Drug Usage Report (132 COLUMNS) (IV)* option allows the user to capture the total IV dispensing cost for a drug, broken down by ward. The system will prompt the user to select a start date and a stop date for which the costs will be calculated. The user may select a specific drug, ^ALL to capture data for all drugs, ^NON to capture data for all non-formulary drugs, ^CAT to capture data for a category of drugs, or ^VADC to capture data for a specific VA drug class. At the "Select WARD:" prompt, the user may enter the name of a specific ward, enter ^ALL for all wards, or enter ^OUTPATIENT for the outpatient orders only.

Example: Ward/Drug Usage Report (IV)

Select Management Reports (IV) Option: WArd/Drug Usage Report (132 COLUMNS) (IV)

The IV BACKGROUND JOB \[PSJI BACKGROUND JOB\] that compiles IV cost data

was last successfully run on: FEB 8,2001@22:52:18

The oldest cost data for room: BIRMINGHAM ISC goes back to: JUN 29,1999

Enter Start Date: T-1000 (MAY 15, 1998)

Enter End Date: T (FEB 08, 2001)

Select IV room: ^ALL// ^ALL

Select DRUG:

or ^ALL (All drugs):

or ^NON (Non-formulary drugs):

or ^CAT (Category of drugs):

or ^VADC (VA drug class):^ALL

Select WARD

or enter ^ALL (all wards)

or enter ^OUTPATIENT (outpatient ward): ^ALL

DEVICE: NT TELNET TERMINAL// 0;132;99 NT/Cache virtual TELNET terminal

WARD/DRUG USAGE REPORT PAGE: 1

JAN 30,2001 THROUGH FEB 8,2001

ALL WARDS

ALL DRUGS

ALL IV ROOMS

DRUG NAME DISPENSED (DESTROYED) RECYCLED CANCELLED DRUG COST

=================================================================================================

IV ROOM: BIRMINGHAM ISC

2 EAST

0.9% NACL 100 ML 300.00 ML 0.00 0.00 0.00 \$ 2.43

0.9% NACL 50 ML 400.00 ML 0.00 500.00 0.00 \$ -1.56

0.9% NaCl 250 ML 16750.00 ML 0.00 0.00 0.00 \$ 30.15

AMPICILLIN 42.22 GM 0.00 0.00 0.00 \$ 21.53

CALCIUM GLUCONATE 10% 1.46 ML 0.00 0.00 0.00 \$ 0.07

CIMETIDINE 300MG PREMIX 7.00 UNITS 0.00 0.00 0.00 \$ 0.00

D10W 1000 ML D10W TEST 3000.00 ML 0.00 0.00 0.00 \$ 2.10

D5-0.45% NACL 500 ML 1000.00 ML 0.00 0.00 0.00 \$ 0.50

D5-0.45% NaCl 1000 ML 1000.00 ML 0.00 0.00 0.00 \$ 1.21

D5W 1000 ML D5W TEST 1000.00 ML 0.00 1000.00 0.00 \$ 0.00

DEXTROSE 20% 1666 ML 3332.00 ML 0.00 0.00 0.00 \$ 33.32

DEXTROSE 5% 25OML BAG 0.98 UNITS 0.00 0.00 0.00 \$ 0.96

HUMAN INSULIN REG 0.90 UNITS 0.00 0.00 0.00 \$ 0.00

MULTIVITAMINS 10.00 ML 0.00 30.00 0.00 \$ -3.18

POTASSIUM CHLORIDE 3.35 MEQ 0.00 0.00 0.00 \$ 0.03

PRIMAXIN 5.00 MG 0.00 0.00 0.00 \$ 0.15

THEOPHYLLINE 200MG PREMIX 1.00 UNITS 0.00 0.00 0.00 \$ 1.28

-------------

TOTAL FOR WARD: 2 EAST \$ 89.00

1 EAST

0.9% NACL 500 ML 1000.00 ML 0.00 0.00 0.00 \$ 468.00

0.9% NaCl 250 ML 23250.00 ML 0.00 0.00 0.00 \$ 41.85

AMPHOTERICIN B 1.00 MG 0.00 0.00 0.00 \$ 0.31

AMPICILLIN 31.09 GM 0.00 0.00 0.00 \$ 15.86

CALCIUM GLUCONATE 10% 0.34 ML 0.00 0.00 0.00 \$ 0.02

D5-0.2% NaCl 1000 ML 4000.00 ML 0.00 0.00 0.00 \$ 2.08

D5-0.45% NACL 500 ML 500.00 ML 0.00 0.00 0.00 \$ 0.25

MANNITOL 20% 8.50 ML 0.00 0.00 0.00 \$ 0.12

MORPHINE SULFATE 1.00 MG 0.00 0.00 0.00 \$ 0.45

POTASSIUM CHLORIDE 1.02 MEQ 0.00 0.00 0.00 \$ 0.01

THEOPHYLLINE 200MG PREMIX 1.34 UNITS 0.00 0.00 0.00 \$ 1.71

-------------

TOTAL FOR WARD: 1 EAST \$ 530.66

=============

GRAND TOTAL: \$ 619.66

FINISHED PRINTING ON: FEB 8,2001@23:06:04

## PUrge Data (IV) – Temporarily Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI PURGE\]

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/027.png)Note: The *PUrge Data (IV)* option is "UU<u>Out of Order</u>UU" and UU<u>TEMPORARILY UNAVAILABLE</u>UU.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/028.png) Users must hold the PSJI PURGE key for access to this option.

The *PUrge Data (IV)* option allows the supervisor to purge orders using one of two sub-options shown below.

### Delete Orders (IV) – Temporarily Unavailable 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI DELETE ORDER\]

The *Delete Orders (IV)* option allows the deletion of IV orders for a specific patient. This option should only be used if an order has been entered for the wrong patient. The deletion of IV orders will only take place if there were no labels printed for that order!

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/029.png)Note: Notice that the number shown on the patient profile under the \# symbol is only a reference number. That number is NOT the internal order number of the order. The reference numbers will always be from one (1) to the number of orders that have been entered for that patient. The internal order numbers may be quite large, since each order in the system has a unique internal order number. The internal order number is only displayed on the order view of the order.

### Purge Expired Orders (IV) – Temporarily Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI PURGE ORDERS\]

The *Purge Expired Orders (IV)* option will allow the user to purge all Expired and Discontinued IV orders that have been inactive for at least 30 days. Any orders that are purged from the database cannot be retrieved. The user is required to enter a date. All IV orders, which have been discontinued before that date entered, will be deleted. Orders that have an expiration date after the date entered will remain on file. Orders that have been inactivated less than 30 days cannot be purged.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/030.png)Note: Large volumes of orders are entered (and expire) in the IV module. Therefore, this option should be run at least once a month. This will speed up module operation because obsolete orders will not have to be compiled.

## Recompile Stats File (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI RECOMPILE\]

The *Recompile Stats File (IV)* option allows the user to change the costs in the IV STATS file dispensed in the past. The AVERAGE DRUG COST PER UNIT field in the IV ADDITIVES or IV SOLUTIONS file must have been edited (by using the *Drug Enter/Edit* option in the *Pharmacy Data Management (PDM) Menu*) for the new cost to appear. The user must enter a start date (date that the changed cost went into effect) and an ending date (last date the changed cost should be in effect). A specific drug can be chosen to update or several drug names, separated by a comma (,), can be entered. After the dates and drug(s) have been entered, the recompilation of the IV STATS file runs as a background job.

Example: Recompile Stats File (IV)

Select SUPervisor's Menu (IV) Option: Recompile Stats File (IV)

The oldest cost data for room: TST ISC ROOM goes back to: ??

The oldest cost data for room: XXXXXX IV ROOM goes back to: ??

Enter Start Date: T-1000 (JUN 01, 2007)

Enter End Date: T (FEB 25, 2010)

Enter Name of Drug to be recompiled

(if multiple names, separate by ","): ?

This option will allow costs to be changed in the statistics file.

The Average Drug Cost Per Unit field in the Additive or Solution file

must first have been edited for the new cost to appear.

A single drug or multiple drugs (separated by , ) may be selected.

After drugs have been selected, the editing of the statistics file

runs as a background job.

Enter Name of Drug to be recompiled

(if multiple names, separate by ","): \<Enter\>

Enter Name of Drug to be recompiled

(if multiple names, separate by ","): CEFAZOLIN

CEFAZOLIN

1 CEFAZOLIN (Additive)

2 CEFAZOLIN (KEFZOL) (Additive)

3 CEFAZOLIN 2GM RTU IN D5W 100ML (Additive)

4 CEFAZOLIN 500MG (Additive)

CHOOSE 1-4: 1 CEFAZOLIN (Additive)

CEFAZOLIN in the Additive File

Queued

Enter Name of Drug to be recompiled

(if multiple names, separate by ","): \<Enter\>

AUto-Discontinue Set-Up

CAtegory File (IV)

COmpile IV Statistics (IV)

Management Reports (IV) ...

PUrge Data (IV) ...

\*\*\> Out of order: TEMPORARILY UNAVAILABLE

Recompile Stats File (IV)

SIte Parameters (IV)

Select SUPervisor's Menu (IV) Option:

## SIte Parameter (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJI SITE PARAMETERS\]

The *SIte Parameter (IV)* option allows the application coordinator to define the characteristics of the IV room and satellites to the module. Manufacturing and delivery times, label size, and same day expiration are identified. This information is stored in the IV ROOM file. The user must define at least one IV room in order for the IV module to function correctly. The definition of the IV room can be altered at any time.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/031.png)Note: If all coverage times are not populated for the user selected IV Room, then IV order entry may be blocked and this warning message will be displayed, "The \[name of file 59.5 entry\] IV ROOM can be updated using option 'Site Parameters (IV)' by a holder of the PSJI MGR VistA Security Key. Contact the Pharmacy Informaticist to update the IV Room parameters."

Example: Site Parameter (IV)

Select SUPervisor's Menu (IV) Option: SIte Parameters (IV)

Select IV ROOM NAME: ?

You may enter a new IV ROOM, if you wish

Answer must be 1-30 characters in length, identifying an IV

distribution area. Each satellite (area) must be named separately.

Select IV ROOM NAME: BIRMINGHAM ISC

NAME: BIRMINGHAM ISC// \<Enter\>

LENGTH OF LABEL: 18// ?

Type a whole number between 12 and 66.

LENGTH OF LABEL: 18// \<Enter\>

WIDTH OF LABEL: 30// ?

Enter a number between 10 and 100 of maximum characters that may print on

a single line of your labels.

WIDTH OF LABEL: 30// \<Enter\>

LINE FEEDS BETWEEN LABELS: 2// ?

Type a whole number between 0 and 6.

LINE FEEDS BETWEEN LABELS: 2// \<Enter\>

END OF LABEL TEXT: Fld by: \_\_\_\_ Chkd by: \_\_\_\_ Replace ?

Answer must be 1-245 characters in length.

END OF LABEL TEXT: Fld by: \_\_\_\_ Chkd by: \_\_\_\_ Replace

HEADER LABEL: YES// ?

Choose from:

0 NO

1 YES

HEADER LABEL: YES// \<Enter\>

SHOW BED LOCATION ON LABEL: YES// \<Enter\>

USE SUSPENSE FUNCTIONS: YES// \<Enter\>

DOSE DUE LINE: BOTH IVPB'S AND LVP'S// ?

Choose from:

0 NO DOSE DUE LINE

1 IVPB'S ONLY

2 LVP'S ONLY

3 BOTH IVPB'S AND LVP'S

DOSE DUE LINE: BOTH IVPB'S AND LVP'S// \<Enter\>

LVP'S GOOD FOR HOW MANY DAYS: 14// ?

Type a Number between 1 and 31, 2 Decimal Digits

LVP'S GOOD FOR HOW MANY DAYS: 14// \<Enter\>

HYPERAL GOOD FOR HOW MANY DAYS: 7// \<Enter\>

PB'S GOOD FOR HOW MANY DAYS: 7// \<Enter\>

SYRN'S GOOD FOR HOW MANY DAYS: 7// \<Enter\>

CHEMO'S GOOD FOR HOW MANY DAYS: 10// \<Enter\>

STOP TIME FOR ORDER: 1654// ?

Type a whole number between 0001 and 2400.

STOP TIME FOR ORDER: 1654// \<Enter\>

EXPIRE ALL ORDERS ON SAME DAY: NO// ?

Choose from:

0 NO

1 YES

EXPIRE ALL ORDERS ON SAME DAY: NO// \<Enter\>

ACTIVITY RULER: YES// ?

Choose from:

0 NO

1 YES

ACTIVITY RULER: YES// \<Enter\>

TOTAL VOL. ON HYPERAL LABELS: YES// ?

Choose from:

0 NO

1 YES

TOTAL VOL. ON HYPERAL LABELS: YES// \<Enter\>

Select START OF COVERAGE: 1000// ?

Answer with START OF COVERAGE

Choose from:

1 0901 S covering from 0901 to 2100

2 0001 P covering from 2400

3 1200 H covering from 1200 to 1159

4 0001 A covering from 0001-2400

6 1100 A covering from 1100 to 1059

7 1000 C covering from 1000 to 2400

You may enter a new START OF COVERAGE, if you wish

Answer must be in military time (i.e., 4 NUMBERS)!

Select START OF COVERAGE: 1000// \<Enter\>

START OF COVERAGE: 1000// \<Enter\>

END OF COVERAGE: 2400// \<Enter\>

TYPE: CHEMOTHERAPY// \<Enter\>

MANUFACTURING TIME: 1000// \<Enter\>

DESCRIPTION: 1000 to 2400// \<Enter\>

Select START OF COVERAGE: \<Enter\>

Select DELIVERY TIME: 2200// \<Enter\>

LABEL DEVICE: LAT TERM// \<Enter\>

REPORT DEVICE: LAT TERM// \<Enter\>

INACTIVATION DATE: \<Enter\>

DAYS TO RETAIN IV STATS: 189// \<Enter\>

You are signed on under the BIRMINGHAM ISC IV ROOM

AUto-Discontinue Set-Up

CAtegory File (IV)

COmpile IV Statistics (IV)

Management Reports (IV) ...

PUrge Data (IV) ...

\*\*\> Out of order: TEMPORARILY UNAVAILABLE

Recompile Stats File (IV)

SIte Parameters (IV)

Select SUPervisor's Menu (IV) Option:

# Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Order checks (allergy/adverse drug reactions, drug-drug interactions, duplicate therapy, pharmacogenomic, dosing, dangerous medications for patient over 64 years of age, Glucophage lab results, aminoglycosides ordered, and Clinical Reminder) are performed when a new medication order is placed through Inpatient Medications or when various actions are taken on medication orders through the Inpatient Medications application. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/032.png)Note: The check for remote data availability is performed when entering a patient's chart, rather than on each order.

The following actions will initiate an order check:

- Action taken through Inpatient Medications to enter a medication order will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through Inpatient Medications to finish a medication order placed through CPRS will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through IV Menu to finish a medication order placed through CPRS will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through Inpatient Medications to renew a medication order will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.
- Action taken through IV Menu to renew a medication order will initiate order checks (allergy, drug-drug interaction, and duplicate therapy) against existing medication orders.

> Action taken through IV Menu to copy a medication order, thereby creating a new order.

The following are the different items used for the order checks:

- Checks each Dispense Drug within the Unit Dose order for allergy/adverse drug reactions.
- Checks each Dispense Drug within the Unit Dose order against existing orders for drug-drug interaction,, and duplicate therapy.
- Checks each additive within an IV order for drug-drug interaction, and duplicate therapy against solutions or other additives within the order.
- Checks each IV order solution for allergy/adverse reactions.
- Checks each IV order solution for drug-drug interaction against other solutions or additives within the order if they are defined as a PreMix.
- Checks each IV order additive for allergy/adverse reaction.
- Checks each IV order additive for drug-drug interaction, and duplicate therapy against existing orders for the patient.
- Checks each IV order solution for drug-drug interaction against existing orders for the patient.

Order Checks will be displayed/processed in the following order:

- System Errors
- Allergy/ADR (local & remote)
- CPRS checks generated backdoor (Aminoglycoside Ordered, Dangerous Meds for Patients \>64, and Glucophage Lab Results)
- Clinical Reminder
- Drug Level Errors
- Inpatient Critical Drug Interaction
- Local & Remote Outpatient Critical Drug Interactions
- Inpatient Significant Drug Interactions
- Local & Remote Outpatient Significant Drug Interactions
- Duplicate Therapy – Inpatient, Local & Remote Outpatient
- Pharmacogenomic (PGx) Order Checks
- <span id="Order_Level_Errors" class="anchor"></span>Order Level Errors
- Dosing Order Checks

These checks will be performed at the Dispense Drug level. Order checks for IV orders will use Dispense Drugs linked to each additive/solution in the IV order. If the order is entered in CPRS with only the Orderable Item, the Dispense Drug will need to be specified when processing the order in Backdoor Pharmacy, and the order check will then use the Dispense Drug.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/033.png) Note: All pending, non-verified, active and renewed Inpatient and Clinic orders, active Outpatient orders and active Non-Veterans Affairs (VA) Meds documented in CPRS will be included in the check. In addition, with the release of OR\*3\*238, order checks will be available using data from the Health Data Repository Historical (HDR-Hx) and the Health Data Repository Interim Messaging Solution (HDR-IMS). This will contain both Outpatient orders from other VAMCs as well as from Department of Defense (DoD) facilities, if available. Any remote Outpatient order that has been expired for 30 days or less will be included in the list of medications to be checked.

Override capabilities are provided based on the severity of the order check, if appropriate. In VistA for example, only critical drug interactions and high PGx checks require an intervention. In CPRS, override requirements are determined by the clinical danger level. For significant interactions or moderate PGx order checks, interventions or overrides are optional.

There is a slight difference in the display of local Outpatient orders compared with remote Outpatient orders. For example, in the Remote Outpatient Duplicate Therapy Order Display example, notice the name of the remote location has been added and the number of refills is not available.

Below are examples of the two displays:

Example: Local Outpatient Duplicate Therapy Order Display

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es) as SIMVASTATIN 20MG

TAB:

Local Rx \#501820A (ACTIVE) for SIMVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Processing Status: Not released locally (Window)

Class(es) Involved in Therapeutic Duplication(s): HMGCo-A Reductase

Inhibitors

Example: Remote Outpatient Duplicate Therapy Order Display

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es) as SIMVASTATIN 20MG

TAB:

LOCATION: REMOTE VA MEDICAL CENTER

Remote Rx \#5769 (ACTIVE) for SIMVASTATIN 10MG TAB

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Last Filled On: 7/25/25

Class(es) Involved in Therapeutic Duplication(s): HMGCo-A Reductase

Inhibitors

## Allergy Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications (Unit Dose and IV) order entry processes check for allergy/Adverse Drug Reactions (ADRs) early in the order entry process. Enterprise-wide Allergy assessments and records are available through HDR and are queried each time a patient's medication profile is accessed. A patient's record may also be marked as 'No Known Allergies'.

Allergies/Adverse Drug Reactions (ADR) may be entered through CPRS or VistA. Site parameters allow the package to be set to auto-verify new patient allergies or require verification by pharmacy staff or others with the GMRA VERIFIER key.

In Backdoor Pharmacy, Allergy order checks appear prior to Clinical Reminder Order Checks.

The following changes have been made to the existing allergy order checks:

In Backdoor Pharmacy, the system will require the pharmacist to complete an Intervention if the severity value equals 'Severe' before allowing the pharmacist to continue with the order.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/034.png)Note: The intervention functionality will be similar to the Critical Drug-Drug Interactions in backdoor pharmacy today.

2\. For orders with Severity of Mild, Moderate, or Not Entered, the system will

continue the same as it does today with the option that allows the pharmacist to enter an intervention at their discretion.

3\. All allergies are captured and stored with the order, regardless of whether or not

an intervention was entered.

4\. Remote/HDR allergy Signs/Symptoms are now displayed when doing Allergy/ADR Order Checks.

5\. Modified Allergy/ADR Order Check to display actual Station Name in lieu of Local or Remote terminology.

6\. For a Severe Allergy the user is required to enter an intervention and their electronic signature.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/035.png) Note: In order to enter the Severity for an allergy in the Allergy Package it must be entered as (O)bserved and not (H)istorical Allerge/Adverse.

Please see Appendix A for steps to enter and allergy or adverse drug reaction or refer to the Adverse Reaction Tracking User Manual or Adverse Reaction Tracking Technical Manual for more information.

## CPRS Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In CPRS, Order Checks occur by evaluating a requested order against existing patient data. Most order checks are processed via the CPRS Expert System. A few are processed within the Pharmacy, Allergy Tracking System, and Order Entry packages. Order Checks are a real-time process that occurs during the ordering session and is driven by responses entered by the ordering provider. Order Check messages are displayed interactively in the ordering session.

Order Checks review existing data and current events to produce a relevant message, which is presented to patient caregivers. Order Checks use the CPRS Expert System (OCX namespace), to define logical expressions for this evaluation and message creation. In addition to the expert system Order Checks have some hard-coded algorithms. For example, the drug-drug interaction order check is made via an entry point in the pharmacy package whereas Renal Functions for Patients Over 65 is defined as a rule in the CPRS Expert System.

Three CPRS Order Checks that are normally performed in CPRS are now performed through Pharmacy backdoor options. They are: Aminoglycoside Ordered, Dangerous Meds for Patients \>64, and Glucophage – Lab Results.

The new order checks were added to both Outpatient Pharmacy and Inpatient Medications (IV and UD modules) applications. The order check warnings displayed are informational only and no user action/intervention is required.

These checks will always be performed through backdoor pharmacy options if set up correctly through CPRS. It does not matter at what level (i.e. user, system) they are enabled or disabled through CPRS.

For example, for the 'Aminoglycoside Ordered' order check, if the medication belongs to the Aminoglycoside VA Drug Class, the software will calculate a creatinine clearance value if a serum creatinine is available using a modified Cockcroft-Gault formula. The creatinine clearance will be displayed along with the latest values for BUN and serum Creatinine. If no creatinine clearance can be calculated, the message will let the user know that that information is not available. This order check will be done in Outpatient Pharmacy, Inpatient Medications (IV and Unit Dose modules).

Figure 104: CPRS Order Check: Aminoglycoside Ordered

> Trigger: Ordering session completion.

> Mechanism: For each medication order placed during this ordering session, the CPRS Expert System requests the pharmacy package to determine if the medication belongs to the VA Drug Class 'Aminoglycosides'. If so, the patient's most recent BUN results are used to calculate the creatinine clearance then OERR is notified and the warning message is displayed.

> \[Note: The creatinine clearance value displayed in some order check messages is an estimate based on adjusted body weight if patient height is \> 60 inches. Approved by the CPRS Clinical Workgroup 8/11/04, it is based on a modified Cockcroft-Gault formula and was installed with patch OR\*3\*221.

> For more information: <http://www.ascp.com/public/pubs/tcp/1999/jan/cockcroft.shtml>

> CrCl (male) = (140 - age) x (adj body weight\* in kg)

> --------------------------------------

> (serum creatinine) x 72

> \* If patient height is not greater than 60 inches, actual body weight is used.

> CrCl (female) = 0.85 x CrCl (male)

> To calculate adjusted body weight, the following equations are used:

> Ideal body weight (IBW) = 50 kg x (for men) or 45 kg x (for women) + 2.3 x (height in inches - 60)

> Adjusted body weight (Adj. BW) if the ratio of actual BW/IBW \> 1.3 = (0.3 x (Actual BW - IBW)) + IBW

> Adjusted body weight if the ratio of actual BW/IBW is not \> 1.3 = IBW or Actual BW (whichever is less)\]

> Message: Aminoglycoside - est. CrCl: \<value calculated from most recent serum creatinine\>. (CREAT: \<result\> BUN: \<result\>).

> Danger Lvl: This order check is exported with a High clinical danger level.

Figure 105: CPRS Order Check: Dangerous Meds for Patients \>64

> DANGEROUS MEDS FOR PT \> 64 – Yes

> This is based on the BEERS list. This order check only checks for three drugs: Amitriptyline, Chlorpropamide and Dipyridamole. The workgroup felt that the list of drugs should be expanded. A request can be sent to CPRS for this.

> Trigger: Acceptance of pharmacy orderable items amitriptyline, chlorpropamide or dipyridamole.

> Mechanism: The CPRS Expert System determines if the patient is greater than 64 years old. It then checks the orderable item of the medication ordered to determine if it is mapped as a local term to the national term DANGEROUS MEDS FOR PTS \> 64.

> Message: If the orderable item text contains AMITRIPTYLINE this message is displayed:

> Patient is \<age\>. Amitriptyline can cause cognitive impairment and loss of balance in older patients. Consider other antidepressant medications on formulary.

> If the orderable item text contains CHLORPROPAMIDE this message is displayed:

> Patient is \<age\>. Older patients may experience hypoglycemia with Chlorpropamide due do its long duration and variable renal secretion. They may also be at increased risk for Chlorpropamide-induced SIADH.

> If the orderable item text contains DIPYRIDAMOLE this message is displayed:

> Patient is \<age\>. Older patients can experience adverse reactions at high doses of Dipyridamole (e.g., headache, dizziness, syncope, GI intolerance.) There is also questionable efficacy at lower doses.

> Danger Lvl: This order check is exported with a High clinical danger level.

Figure 106: CPRS Order Check: Glucophage Lab Results

> Trigger: Selection of a Pharmacy orderable item.

> Mechanism: The CPRS Expert System checks the pharmacy orderable item's local text (from the Dispense Drug file \[#50\]) to determine if it contains "glucophage" or "metformin". The expert system next searches for a serum creatinine result within the past x number of days as determined by parameter ORK GLUCOPHAGE CREATININE. If the patient's creatinine result was greater than 1.5 or does not exist, OE/RR is notified and the warning message is displayed.

> Message: Metformin– no serum creatinine within past \<x\> days. else:

> Metformin – Creatinine results: \<creatinine greater than 1.5 w/in past \<x\> days\>

> Danger Lvl: This order check is exported with a High clinical danger level

## Clinical Reminder Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Clinical Reminder Order Checks (CROCs) functionality. Order Checks now include the ability to view Clinical Reminders and will display prior to the Enhanced Drug-Drug interactions). Reminders are used to aid clinicians in performing tasks to fulfill Clinical Practice Guidelines and periodic procedures or education as needed for patients.

For an IV order, if there are multiple drugs that are involved in a CROC, one will have to log an intervention for each drug.

Only the CPRS orderable item and drug level CROCs are displayed through the Pharmacy Backdoor.

Example: Clinical Reminder Order Check with severity of Medium

Now processing Clinical Reminder Order Checks. Please wait ...

\*\*\* Clinical Reminder Order Check \| Severity: MEDIUM \*\*\*

Potentially Teratogenic Medication (FDA Category D or C)

Concern has been raised about use of this medication during pregnancy.

1\) Pregnancy status should be determined. Discuss use of this medication on the

context of risks to the mother and child of untreated disease. Potential

benefits may warrant use of the drug in pregnant women despite risks.

2\) The patient must be provided contraceptive counseling on potential risk vs.

benefit of taking this medication if she were to become pregnant.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The 'Teratogenic Medications' Order Check will display for female patients

between the ages of 12 and 50, except those with a known exclusion criterion

(e.g., hysterectomy), or those with a documented IUD placement that is more

recent than a documented IUD removal.

----------------------------------------------------------------------------

Do you want to Intervene? N// NO

> **NOTE:** Clinical Reminder Order Checks will have a severity of low, medium, or high. For a Clinical Reminder Order Check with a low or medium severity, the entry of an intervention is optional. For a Clinical Reminder Order Check with a high severity, the user <u>must</u> enter an intervention before continuing.

Example: Clinical Reminder Order Check with severity of High.

Now processing Clinical Reminder Order Checks. Please wait ...

============================================================================

\*\*\* Clinical Reminder Order Check \| Severity: HIGH \*\*\*

Patient is greater than 64yo and on Statins

This alert will display for patients greater than 64yo and who are taking a

STATIN drug.

----------------------------------------------------------------------------

Do you want to Continue? Y// ES

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

For LOVASTATIN 40MG TAB

PROVIDER: INPATIENT

1 INPATIENT-MEDS,NURSE NURSE

2 INPATIENT-MEDS,PHARMACIST PI

3 INPATIENT-MEDS,PROVIDER PROV

CHOOSE 1-3: 3 INPATIENT-MEDS,PROVIDER PROV

RECOMMENDATION: CHANGE DRUG

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

## Enhanced Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medication Order Check Healthcare Application (MOCHA) v1.0, implemented enhanced order checking functionality using HealtheVet (HEV) compatible architecture and First Databank (FDB) MedKnowledge Framework Application Program Interfaces (APIs), and database for Drug Interaction and Duplicate Therapy order checks.

MOCHA v3.0 implemented pharmacogenomic (PGx) order checks, providing additional guidance for selecting suitable drug therapies based on genomic factors and indicators. This assists clinicians in delivering safe and effective treatment options tailored to individual patients. 

### Duplicate Therapy Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient orders are checked for therapeutic duplication with drugs within similar therapeutic classes. If orders share similar classes with the order being processed, they will be included in the list within the therapeutic duplication warning. If 2 orders are entered for the same drug, such as one scheduled and one PRN order, they are checked and displayed as a Duplicate Therapy warning.

The user will have the opportunity to discontinue duplicate therapy order(s) after the duplicate therapy warning is displayed as long as at least one of the orders listed is an inpatient order and that order is not being worked on (i.e., copy action taken).

Each First Databank therapeutic class is assigned a duplication allowance value. The duplication allowance value indicates how many duplications (drug pairs) are considered appropriate before a warning is generated. If the number of duplicate therapy drug pairs exceeds the duplication allowance value, a warning is displayed. In the example below, if the patient is already receiving orders containing a Dispense Drug in the same class as one of the Dispense Drugs in the new order, the orders containing the drug in that class are displayed. Inpatient duplicate orders of this kind are displayed in a numbered list. The user is first asked whether to continue the current order. If the user selects to continue the order, then the user is prompted with which, if any, numbered Inpatient duplicate orders to discontinue. The user may enter a range of numbers from the numbered list of duplicate orders or bypass the prompt by selecting \<Enter\> and continue with the order. Entry of orders with duplicate drugs of the same class will be allowed.

Table: Duplication Allowance

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/036.png)

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/037.png)Note: Inpatient Medications order checks display orders with the same drug

as Duplicate Therapy instead of Duplicate Drug.

Therapeutic Duplication - IV and Unit Dose clinic order therapeutic duplications display in the same format as drug interactions. See examples below:

Example: Unit Dose Duplicate Therapy Order Check:

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es) as POTASSIUM CHLORIDE

10MEQ TAB :

POTASSIUM (K) LIQUID,ORAL ? \*\*\*\*\* \*\*\*\*\* P

Give: 40MEQ/15ML PO BID

Local Rx \#100002933 (SUSPENDED) for POTASSIUM CHLORIDE 10MEQ TAB

SIG: TAKE ONE TABLET BY BY MOUTH TWICE A DAY

Processing Status: Not released locally (Mail)

Class(es) Involved in Therapeutic Duplication(s): Potassium

Example: IV Duplicate Therapy Order Check:

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

CEFAZOLIN 1 GM

Clinic Order: CEFAZOLIN 2 GM (PENDING)

Solution(s): 5% DEXTROSE 50 ML

Order Date: NOV 20, 2012@11:01

Start Date: \*\*\*\*\*\*\*\*

Stop Date: \*\*\*\*\*\*\*\*

Clinic Order: CEFAZOLIN SOD 1GM INJ (EXPIRED)

Solution(s): 5% DEXTROSE 50 ML

Start Date: OCT 24, 2012@16:44

Stop Date: OCT 25, 2012@24:00

Class(es) Involved in Therapeutic Duplication(s): Beta-Lactams,

Cephalosporins, Cephalosporins - 1st Generation

### Drug/Drug Interaction Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Drug Interaction Order Checks are performed when new orders are processed and compare prospective drug to the existing profile drugs. For Drug Interaction Order Checks, local outpatient orders include all active, non-verified, pending and Non-VA medication orders. Remote outpatient orders include all active orders. For Duplicate Therapy Order Checks, local outpatient orders include all active, expired (Exp Date + 120), discontinued (Cancel Date + Days Supply +7), non-verified, pending and Non-VA Medication orders. Remote outpatient orders include all active, expired (Exp Date +30) and discontinued (Cancel Date +30).

Inpatient medication orders include all active, non-verified, pending orders for both IV and Unit Dose modules.

Clinic Orders participate in both Drug Interaction Order Checks and Duplicate Therapy Order Checks for Inpatient and Outpatient medication orders.

For Significant Drug Interaction Order Checks, a pharmacy intervention is optional. Critical Drug Interaction Order Checks require a pharmacy intervention during processing. See examples below:

Example: Critical Drug Interaction – Pharmacy Intervention required

================================================================================

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with WARFARIN 2MG TABS:

CIPROFLOXACIN TAB C 08/13 08/18 A

Give: 500MG PO BID

Concurrent use of quinolones may be associated with an increase in

hypoprothrombinemic effects of anticoagulants, which may result in an

increased risk of bleeding.

================================================================================

Display Professional Interaction Monograph(s)? NO//

Do you want to Continue with WARFARIN 2MG TABS? NO// YES

Now creating Pharmacy Intervention

PROVIDER: PSJPROVIDER, ONE

RECOMMENDATION: ORDER LAB TEST

Example: Significant Drug Interaction

Now Processing Enhanced Order Checks! Please wait...

================================================================================

This patient is receiving the following order(s) that have a SIGNFICANT Drug Interaction

with ASPIRIN 325MG TAB:

WARFARIN TAB C 08/15 08/30 A

Give: 2.5MG PO QPM

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

For Drug Interaction Order Checks, a profession interaction monograph is available to display during order processing through backdoor pharmacy. See example below:

Example: Significant Drug Interaction for Unit Dose Order – Display Monograph

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

================================================================================

This patient is receiving the following order(s) that have a SIGNFICANT Drug Interaction

with ASPIRIN 325MG TAB:

WARFARIN TAB C 08/15 08/30 A

Give: 2.5MG PO QPM

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

================================================================================

Display Professional Interaction Monograph? No// Y es

Device: Home// \<Home would print to screen, or a specific device could be specified\>

Professional Monograph

Drug Interaction with WARFARIN AND ASPIRIN

This information is generalized and not intended as specific medical advice. Consult your healthcare professional before taking or discontinuing any drug or commencing any course of treatment.

MONOGRAPH TITLE: Anticoagulants/Salicylates

SEVERITY LEVEL: 2-Severe Interaction: Action is required to reduce the risk of severe adverse interaction.

MECHANISM OF ACTION: Multiple processes are involved: 1) Salicylate doses greater than 3 gm daily decrease plasma prothrombin levels. 2) Salicylates may also displace anticoagulants from plasma protein binding sites. 3) Salicylates impair platelet function, resulting in prolonged bleeding time. 4) Salicylates may cause gastrointestinal bleeding due to irritation.

CLINICAL EFFECTS: The concurrent use of anticoagulants and salicylates may result in increased INR values and increase the risk of bleeding.

PREDISPOSING FACTORS: None determined.

PATIENT MANAGEMENT: Avoid concomitant administration of these drugs. If salicylate use is necessary, monitor prothrombin time, bleeding time or INR values closely. When possible, the administration of a non-aspirin salicylate would be preferable.

DISCUSSION: This interaction has been reported between aspirin and warfarin and between aspirin and dicumarol. Diflunisal, sodium salicylate, and topical methyl salicylate have been shown to interact with anticoagulants as well. Based on the proposed mechanisms, other salicylates would be expected to interact with anticoagulants as well. The time of highest risk for a coumarin-type drug interaction is when the precipitant drug is initiated, altered, or discontinued.

REFERENCES:

1.Quick AJ, Clesceri L. Influence of acetylsalicylic acid and salicylamide on the coagulation of blood. J Pharmacol Exp Ther 1960;128:95-8.

2.Watson RM, Pierson RN, Jr. Effect of anticoagulant therapy upon aspirin-induced gastrointestinal bleeding. Circulation 1961 Sep;24:613-6.

3.Barrow MV, Quick DT, Cunningham RW. Salicylate hypoprothrombinemia in rheumatoid arthritis with liver disease. Report of two cases. Arch Intern Med 1967 Nov;120(5):620-4.

4.Weiss HJ, Aledort LM, Kochwa S. The effect of salicylates on the hemostatic properties of platelets in man. J Clin Invest 1968 Sep; 47(9):2169-80.

5.Udall JA. Drug interference with warfarin therapy. Clin Med 1970 Aug; 77:20-5.

6.Fausa O. Salicylate-induced hypoprothrombinemia. A report of four cases. Acta Med Scand 1970 Nov;188(5):403-8.

7.Zucker MB, Peterson J. Effect of acetylsalicylic acid, other nonsteroidal anti-inflammatory agents, and dipyridamole on human blood platelets. J Lab Clin Med 1970 Jul;76(1):66-75.

8.O'Reilly RA, Sahud MA, Aggeler PM. Impact of aspirin and chlorthalidone on the pharmacodynamics of oral anticoagulant drugs in man. Ann N Y Acad Sci 1971 Jul 6;179:173-86.

9.Dale J, Myhre E, Loew D. Bleeding during acetylsalicylic acid and anticoagulant therapy in patients with reduced platelet reactivity after aortic valve replacement. Am Heart J 1980 Jun;99(6):746-52.

10.Donaldson DR, Sreeharan N, Crow MJ, Rajah SM. Assessment of the interaction of warfarin with aspirin and dipyridamole. Thromb Haemost 1982 Feb 26;47(1):77.

11.Chesebro JH, Fuster V, Elveback LR, McGoon DC, Pluth JR, Puga FJ, Wallace RB, Danielson GK, Orszulak TA, Piehler JM, Schaff HV. Trial of combined warfarin plus dipyridamole or aspirin therapy in prosthetic heart valve replacement: danger of aspirin compared with dipyridamole. Am J Cardiol 1983 May 15;51(9):1537-41.

12.Chow WH, Cheung KL, Ling HM, See T. Potentiation of warfarin anticoagulation by topical methylsalicylate ointment. J R Soc Med 1989 Aug;82(8):501-2.

13.Meade TW, Roderick PJ, Brennan PJ, Wilkes HC, Kelleher CC. Extra-cranial bleeding and other symptoms due to low dose aspirin and low intensity oral anticoagulation. Thromb Haemost 1992 Jul 6;68(1):1-6.

Copyright \<2010\> First DataBank, Inc.

### Dosing Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v2.0 implemented the first increment of dosage checks and introduced the Maximum Single Dose Check for simple and complex orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.1b implemented the second increment of dosage checks and introduced the Max Daily Dose Check for simple orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.0 and MOCHA v2.1b use the same interface to First Databank (FDB) as MOCHA v1.0. See example below:

Example: Dosing order checks – Frequency, Max Single & Max Daily Dose warnings

Max Daily Dose Check could not be performed for Drug: SIMVASTATIN 10MG

TAB

Reason(s): Invalid or Undefined Frequency

SIMVASTATIN 10MG TAB: Single dose of 160 milligrams exceeds the maximum

single dose of 80 milligrams.

General dosing range for SIMVASTATIN 10MG TAB (ORAL): 5 milligram/day to

40 milligram/day. Maximum daily dose is 80 milligram/day.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/038.png) Please refer to the Dosing Order Checks User Manual for a detailed description of dosing order checks.

### Pharmacogenomic Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v3.0 implemented Pharmacogenomic (PGx) Order Checks, providing additional guidance for selecting suitable drug therapies based on genomic factors and indicators. This assists clinicians in delivering safe and effective treatment options tailored to individual patients

In order to perform the Pharmacogenomic Order Checks, the system first retrieves the patient's pharmacogenomic lab results which are stored in the HDR, regardless of where they were drawn. Results are retrieved at the time the order is accepted in CPRS or being processed in VistA. If the HDR server or the MOCHA server are not able to connect, a corresponding message will be displayed to the user.

Pharmacogenomic order checks levels of severity:

- High order checks require an override by the provider and an intervention by the pharmacist
- Medium order check overrides or interventions are optional.
- Screen Message displays when additional information or testing needs to be provided to perform a PGx order check. This can occur when the PGx order check cannot be completed due to uninterpretable gene or phenotype results, even though the vendor database contains genomic findings and PGx guidance exists for the prospective drug.

At the time of entering or processing the order, the user can display 'Additional Information' to see the order check content as well as the sources and references returned from the vendor.

Only VA Products that are marked as PGx Eligible in the National Drug File are eligible for PGx Order checks.

PGx order checks are not rechecked when the order is edited, unless the dispense drug field or dosage related fields are edited.

An email notification to the PBM PGx CDS group is sent when an HDR-retrieved gene or phenotype cannot be mapped to the FDB gene database. The Pharmacogenomic Email Log (File \#51.29) will store the pertinent information. If an order is entered or processed for that specific patient with the same unresolved gene or unresolved or null phenotype greater than 7 days from the last email, another email and log will be sent.

Suppression of Pharmacogenomic Order Checks may occur at the following 2 levels:

- Profile suppression occurs if the ingredient for the prospective order is set to PGx Eligible and PGx Suppress, the severity of the PGx order check is Medium (Informational), the patient has an active local or remote inpatient order (Unit Dose, Clinic Meds, IV or Clinic Infusion) for a drug with the same ingredient as the prospective drug. NOTE: Non-VA medications are NOT included for suppression logic.
- Severity and PGx Action Category Suppression occurs if the severity of the order check is Medium (Informational) and the PGx Action Category is one of the following:
  - 9 – No therapy adjustment needed
  - 14 – No therapy recommendation
  - 2 – Await genotype test result
  - 4 – Consider genotype test or prescribe alternative
  - 13 – Consider genotype test
  - 5 – Order genotype test or prescribe alternative
- ![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/039.png) Please refer to the MOCHA FAQs for more detailed information.

Pharmacogenomic HIGH Order Check:

GENOMIC FINDING: CYP2D6 poor metabolizer

IMPACTED MEDICATION: AMITRIPTYLINE 100MG

ACTION: For conditions requiring higher starting doses (e.g., 25 mg/day or

higher) such as depression, consider alternate drug with less dependence on

CYP2D6 metabolism (e.g., citalopram, sertraline). If amitriptyline use is

warranted, consider a 50% reduction of the standard starting dose and use

therapeutic drug monitoring to guide subsequent dose adjustment.

MONITORING: If using amitriptyline, monitor for symptom improvement as well as

adverse reactions (e.g., anticholinergic, central nervous system, and cardiac

effects).

For more details on VA National Pharmacogenomics Program go to:

[<https://bit.ly/VA-PGx>](https://bit.ly/VA-PGx)

Display Additional Information on Pharmacogenomic Order Check(s)? NO// YES

DEVICE: HOME// Linux Telnet /SSh

Pharmacogenomics Detailed Information

GENOMIC FINDING: CYP2D6 poor metabolizer

IMPACTED MEDICATION: AMITRIPTYLINE 100MG

SEVERITY LEVEL: HIGH

EVIDENCE RATINGS:

SOURCE: Clinical Pharmacogenetics Implementation Consortium (CPIC)

(1,2)

RATING: Strong

SOURCE: Dutch Pharmacogenetics Working Group (DPWG) (3)

RATING: 3, A

ACTION:

For conditions requiring higher starting doses (e.g., 25 mg/day or higher)

such as depression, consider alternate drug with less dependence on CYP2D6

metabolism (e.g., citalopram, sertraline). If amitriptyline use is

warranted, consider a 50% reduction of the standard starting dose and use

therapeutic drug monitoring to guide subsequent dose adjustment.

Type \<Enter\> to continue or '^' to exit:

RATIONALE:

Greatly reduced amitriptyline metabolism results in higher concentrations of

active drug and increased risk of adverse reactions.

MONITORING:

If using amitriptyline, monitor for symptom improvement as well as adverse

reactions (e.g., anticholinergic, central nervous system, and cardiac

effects).

CITATIONS:

\(1\) Hicks JK, Sangkuhl K, Swen JJ, et al. Clinical Pharmacogenetics

Implementation Consortium Guideline (CPIC) for CYP2D6 and CYP2C19 Genotypes

and Dosing of Tricyclic Antidepressants: 2016 update. Clinical Pharmacology

and Therapeutics. 2017 Jul 01; 102 (1): 37-44. Available from

[<https://cpicpgx.org/content/guideline/publication/TCA/2016/TCA_2016.pdf>](https://cpicpgx.org/content/guideline/publication/TCA/2016/TCA_2016.pdf)

\(2\) Clinical Pharmacogenetics Implementation Consortium (CPIC). CPIC Guideline

for Tricyclic Antidepressants and CYP2D6 and CYP2C19. Available from

[<https://cpicpgx.org/guidelines/guideline-for-tricyclic-antidepressants-and-cyp2d>](https://cpicpgx.org/guidelines/guideline-for-tricyclic-antidepressants-and-cyp2d)

6-and-cyp2c19/

\(3\) Dutch Pharmacogenetics Working Group. Pharmacogenomics guidelines.

Type \<Enter\> to continue or '^' to exit:

Available from

[<https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf>](https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf)

First Databank database updated on 07/02/2025.

Do you want to Continue with AMITRIPTYLINE 100MG? NO// Y

Example: PGx MEDIUM Order Check, no intervention required

Pharmacogenomic MEDIUM Order Check:

GENOMIC FINDING: CYP2D6 intermediate metabolizer

IMPACTED MEDICATION: TRAMADOL HCL 100MG TAB

ACTION: Initiate therapy with usual recommended starting dose. If there is

poor therapeutic response, consider alternative analgesic such as morphine or

a nonopioid. Codeine and hydrocodone are also affected by CYP2D6 polymorphisms

and may not be suitable alternatives.

MONITORING: Monitor for analgesic response.

For more details on VA National Pharmacogenomics Program go to:

https://bit.ly/VA-PGx

Display Additional Information on Pharmacogenomic Order Check(s)? NO//

Do you want to Intervene with TRAMADOL HCL 100MG TAB ? NO//

Press Return to continue...

### Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinic orders are created via CPRS generally using the Meds Inpatient tab or the IV Fluids tab. Drug orders that have a clinic and an appointment date and time are considered clinic orders. The clinic must be defined with 'ADMINISTER INPATIENT MEDS?' prompt answered YES under the SETUP A CLINIC \[SDBUILD\] option in the Scheduling package. Defining the clinic in this manner ensures that an appointment date and time are defined. Orders placed via backdoor inpatient medications are not considered clinic orders.

Patch PSJ\*5\*319 added functionality to allow users to create clinic orders in backdoor. Users can select the action, CM New Clinic Medication Entry, available on the ListMan Inpatient order entry screen to create a new clinic order.

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Next Screen// CM New Clinic Medication Entry

Visit Location: GENERAL MEDICINE

Date/Time of Visit: NOW// (AUG 10, 2020@13:57)

Select DRUG:

MOCHA v1.0 Enhancements 1 added drug interaction and therapeutic duplication order checks for clinic orders to Outpatient Pharmacy. Previously Inpatient Medications package performed order checks on active, pending and non-verified clinic orders. With the MOCHA v1.0 Enhancements 1, Inpatient medications will perform enhanced order checks for recently discontinued and expired inpatient medications clinic orders.

MOCHA v3.0 Enhancements added Pharmacogenomic (PGx) Order Checks. Clinic Orders are included in PGx Order Checks and suppression evaluations.

For both packages, the system will display clinic orders in a standard format to differentiate them from Inpatient Medications and Outpatient Pharmacy order checks.

Example: Unit Dose Drug Interaction Clinic Order Check

Now Processing Enhanced Order Checks!  Please wait...

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with CIMETIDINE 300 MG:

      Clinic Order: PHENYTOIN 100MG CAP (DISCONTINUED)

          Schedule: Q8H

           Dosage: 100MG

        Start Date: FEB 27, 2012@13:00

         Stop Date: FEB 28, 2012@15:22:27

Concurrent use of cimetidine or ranitidine may result in elevated levels

of and toxicity from the hydantoin.Neutropenia and thrombocytopenia have

been reported with concurrent cimetidine and phenytoin. 

Example: IV Clinic Drug Interaction Order Check

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with WARFARIN 2MG TAB:

      Clinic Order: POTASSIUM CHLORIDE 20 MEQ (ACTIVE)

Other Additive(s): MAGNESIUM SULFATE 1 GM (1), CALCIUM GLUCONATE 1 GM (2),

                    HEPARIN 1000 UNITS, CIMETIDINE 300 MG

       Solution(s): DEXTROSE 20% 500 ML 125 ml/hr

                    AMINO ACID SOLUTION 8.5% 500 ML 125 ml/hr

        Start Date: APR 05, 2012@15:00

         Stop Date: APR 27, 2012@24:00

The pharmacologic effects of warfarin may be increased resulting in severe

bleeding.

Based on the number of days defined in the IMO DC/EXPIRED DAY LIMIT field (#6) in CLINIC DEFINITION file (#53.46), the enhanced order checks process will only include discontinued and expired orders with a stop date that falls within the range defined for drug interactions and/or duplicate therapy checks. The following are the scenarios that drive which dates will be displayed for the clinic order:

- If there are start/stop dates defined, they are displayed.
- If there are no stop/start dates defined, the 'requested start/stop dates' will be displayed with the word "Requested" prior to the start/stop date header.
- If there are no requested start/stop dates defined, the order date will be displayed and the start/stop date headers will be displayed with "\*\*\*\*\*\*\*\*" for the date.
- If there is either a requested start date or a requested stop date, the available date will be displayed and "\*\*\*\*\*\*\*\*" will be displayed for the undefined date.

Therapeutic Duplication - IV and Unit Dose clinic order therapeutic duplications display in the same format as drug interactions.

Figure 102: Unit Dose Duplicate Therapy Clinic Order Check example

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

POTASSIUM CHLORIDE 30 MEQ

Clinic Order: POTASSIUM CHLORIDE 10MEQ TAB (PENDING)

Schedule: BID

Dosage: 20MEQ

Requested Start Date: 11/20/2012@17:00

Stop Date: \*\*\*\*\*\*\*\*

Class(es) Involved in Therapeutic Duplication(s): Potassium

Figure 103: IV Duplicate Therapy Clinic Order Check example

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

CEFAZOLIN 1 GM

Clinic Order: CEFAZOLIN 2 GM (PENDING)

Solution(s): 5% DEXTROSE 50 ML

Order Date: 11/20/12@11:01

Start Date: \*\*\*\*\*\*\*\*

Stop Date: \*\*\*\*\*\*\*\*

Clinic Order: CEFAZOLIN SOD 1GM INJ (EXPIRED)

Solution(s): 5% DEXTROSE 50 ML

Start Date: 10/24/2012@16:44

Stop Date: 10/25/2012@24:00

Class(es) Involved in Therapeutic Duplication(s): Beta-Lactams,

Cephalosporins, Cephalosporins - 1st Generation

> .

### Dosing Order Checks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v2.0 implemented the first increment of dosage checks and introduced the Maximum Single Dose Check for simple and complex orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.1b implemented the second increment of dosage checks and introduced the Max Daily Dose Check for simple orders for both Outpatient Pharmacy and Inpatient Medications applications. MOCHA v2.0 and MOCHA v2.1b use the same interface to First Databank (FDB) as MOCHA v1.0.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/040.png)Note: Please refer to the Dosing Order Checks User Manual for a detailed description of dosing order checks.

### Order Check Data Caching

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data caching was recently added to improve the speed of order checks. Before data caching, order checks could be slow because each order check retrieved data from the other VISTA packages—even if the order checks used the same data. With data caching, the first order check in an ordering session retrieves data from other VISTA packages, uses the data to evaluate whether it should display a warning, and then stores the retrieved data in the ^XTMP("OCXCACHE" global for five minutes. The order checks that occur in the next five minutes can use the cached data, if it is the appropriate data, instead of retrieving data from the other packages. After five minutes, the cached data expires, and order checks must retrieve new data from the VISTA packages.

For example, before data caching was implemented, if an order check took 3 seconds to retrieve data from other VISTA packages, and there were 12 order checks, clinicians might wait 36 seconds to sign orders. With data caching, the first order check might take 3 seconds to retrieve the data, but subsequent order checks could use the cache and might take only .03 seconds each. That would be 3.33 seconds compared to 36 seconds. The numbers in this example are for illustration only and do not reflect real system speed. However, data caching should speed up order checks.

To avoid using all available disk space for storing data from order checks, there are several ways to clear the ^XTMP("OCXCACHE" global. ORMTIME removes data from the global when it runs. The suggested frequency for running ORMTIME is every 30 minutes, but not every site runs it that frequently. Kernel clean up utilities also remove data from the cache when they run, which is usually every 24 hours. If needed, users that have access to the programmer's prompt can manually clear the cache from that prompt by using PURGE^OCXCACHE.

### Display of Provider Overrides and Pharmacist Interventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Inpatient Medications, the first time a field preceded by an asterisk (\*) is selected for editing and when renewing an order, if Current Pharmacist Interventions exist for the order, entering Y (Yes) at the prompt, "Order Check Overrides/Interventions exist for this order. Display? (Y/N)? Y//," will display the following information when the fields are populated with data:

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Heading: Current Pharmacist Interventions for this order</p></li>
</ul></th>
<th><ul>
<li><blockquote>
<p>Recommendation Accepted</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Intervention Date/Time</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Agree With Provider</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Provider</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Rx #</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Pharmacist</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Division</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Drug,</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Financial Cost</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Instituted By</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Other For Intervention</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Intervention</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Reason For Intervention</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Other For Recommendation</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Action Taken</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Originating Package</p></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Clinical Impact</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>Was Provider Contacted</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Financial Impact</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>Provider Contacted</p>
</blockquote></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

============================================================================

\*\* Current Provider Overrides for this order \*\*

============================================================================

Overriding Provider: PSJPROVIDER,ONE (PROVIDER)

Override Entered By: PSJPROVIDER,ONE (PROVIDER)

Date/Time Entered: 7/12/11 09:13

Override Reason: Testing 9 OTHER

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN NA

(GOLDEN STATE) 2MG TAB \[ACTIVE\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN(GOLDEN

ST) 0.5MG(1/2X1MG) TAB \[UNRELEASED\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

Press RETURN to Continue or '^' to Exit :

============================================================================

\*\* Current Pharmacist Interventions for this order \*\*

============================================================================

Intervention Date: 7/12/11 09:14

Provider: PSJPROVIDER,ONE Pharmacist: PSJPHARMACIST,ONE

Drug: METRONIDAZOLE 250MG TAB Instituted By: PHARMACY

Intervention: CRITICAL DRUG INTERACTION

Recommendation: OTHER Originating Package: INPATIENT

Other For Recommendation:

INTERVENTION FOR CRITICAL DRUG-DRUG

Press RETURN to Continue or '^' to Exit :

If Historical Overrides/Interventions exist for an order, entering Y (Yes) at the prompt: "View Historical Overrides/Interventions for this order (Y/N)? Y//," displays the Historical Pharmacist Intervention information:

============================================================================

\*\* Historical Pharmacist Interventions for this order \*\*

============================================================================

Intervention Date: 07/12/11 09:14

Provider: PSJPROVIDER,ONE Pharmacist: PSJPHARMACIST,ONE

Drug: METRONIDAZOLE 250MG TAB Instituted By: PHARMACY

Intervention: CRITICAL DRUG INTERACTION

Recommendation: OTHER Originating Package: INPATIENT

Other For Recommendation:

Testing 9 OTHER

Press RETURN to Continue or '^' to Exit :

============================================================================

\*\* Historical Provider Overrides for this order \*\*

============================================================================

Overriding Provider: PSJPROVIDER,ONE (PROVIDER)

Override Entered By: PSJPROVIDER,ONE (PROVIDER)

Date/Time Entered: 07/12/11 09:13

Override Reason: Testing 9 OTHER

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN NA

(GOLDEN STATE) 2MG TAB \[ACTIVE\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

CRITICAL drug-drug interaction: METRONIDAZOLE 250MG TAB and WARFARIN(GOLDEN

ST) 0.5MG(1/2X1MG) TAB \[UNRELEASED\] - Concurrent use of anticoagulants with

metronidazole or tinidazole may result in reduced prothrombin activity and/or

increased risk of bleeding. - Monograph Available

Intervention TIME displays to the right of the date (e.g., 07/12/11 09:14. Current Pharmacist Intervention fields and labels also display, when the fields are populated.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/041.png)Note: In Inpatient Medications, if no Current Pharmacist Interventions exist when editing a field preceded by an asterisk (\*),the following displays:

============================================================================

\*\* Current Pharmacist Interventions for this order \*\*

============================================================================

No Pharmacist Interventions to display

# Check Drug Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSJ CHECK DRUG INTERACTION\]

The Check Drug Interaction option allows a user to check for a drug interaction and Therapeutic Duplications between two or more drugs. This option is located on the Unit Dose Medications \[PSJU MGR\] Menu, and the IV \[PSJI MGR\] Menu.

Figure 107: Example: Checking for Drug Interactions

Select IV Menu Option: Check Drug Interaction

Drug 1: CIMETIDINE 300MG TAB GA301

...OK? Yes// (Yes)

Drug 2: WARFARIN 5MG TAB

Lookup: GENERIC NAME

WARFARIN 5MG TAB BL110

...OK? Yes// (Yes)

Drug 3:

Now Processing Enhanced Order Checks! Please wait...

\*\*\* DRUG INTERACTION(S) \*\*\*

============================================================

\*\*\*Critical\*\*\* with WARFARIN 5MG TAB and

CIMETIDINE 300MG TAB

CLINICAL EFFECTS: The pharmacologic effects of warfarin may be

increased resulting in severe bleeding.

============================================================

Press Return to Continue...:

Display Professional Interaction monograph? N// YES

DEVICE: HOME// SSH VIRTUAL TERMINAL Right Margin: 80//

------------------------------------------------------------

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

This information is generalized and not intended as specific medical

advice. Consult your healthcare professional before taking or

discontinuing any drug or commencing any course of treatment.

MONOGRAPH TITLE: Anticoagulants/Cimetidine

SEVERITY LEVEL: 2-Severe Interaction: Action is required to reduce

the risk of severe adverse interaction.

MECHANISM OF ACTION: Inhibition of warfarin hepatic metabolism. The

effect appears to be greater on the less active R-warfarin than on the

S-warfarin.

CLINICAL EFFECTS: The pharmacologic effects of warfarin may be

increased resulting in severe bleeding.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

PREDISPOSING FACTORS: None determined.

PATIENT MANAGEMENT: Coadministration of cimetidine and warfarin

should be avoided. If they are administered concurrently, monitor

anticoagulant activity and adjust the dose of warfarin indicated. The

H-2 antagonists famotidine and nizatidine are unlikely to interact

with warfarin.The time of highest risk for a coumarin-type drug

interaction is when the precipitant drug is initiated or discontinued.

Contact the prescriber before initiating, altering the dose or

discontinuing either drug.

DISCUSSION: The majority of drug interaction reports involving H-2

antagonists and warfarin have occurred with cimetidine. Reports of a

possibly significant interaction between ranitidine and warfarin have

been equivocal. Famotidine and nizatidine do not appear to affect

prothrombin time.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

REFERENCES:

1.Silver BA, Bell WR. Cimetidine potentiation of the

hypoprothrombinemic effect of warfarin. Ann Intern Med 1979

Mar;90(3):348-9.

2.Wallin BA, Jacknowitz A, Raich PC. Cimetidine and effect of

warfarin. Ann Intern Med 1979 Jun;90(6):993.

3.Serlin MJ, Sibeon RG, Breckenridge AM. Lack of effect of ranitidine

on warfarin action. Br J Clin Pharmacol 1981 Dec;12(6):791-4.

4.Kerley B, Ali M. Cimetidine potentiation of warfarin action. Can Med

Assoc J 1982 Jan 15;126(2):116.

5.Desmond PV, Mashford ML, Harman PJ, Morphett BJ, Breen KJ, Wang YM.

Decreased oral warfarin clearance after ranitidine and cimetidine.

Clin Pharmacol Ther 1984 Mar;35(3):338-41.

6.Toon S, Hopkins KJ, Garstang FM, Rowland M. Comparative effects of

ranitidine and cimetidine on the pharmacokinetics and pharmacodynamics

of warfarin in man. Eur J Clin Pharmacol 1987;32(2):165-72.

Press Return to Continue or "^" to Exit:

Professional Monograph

Drug Interaction with WARFARIN 5MG TAB and CIMETIDINE 300MG TAB

7.Cournot A, Berlin I, Sallord JC, Singlas E. Lack of interaction

between nizatidine and warfarin during chronic administration. J Clin

Pharmacol 1988 Dec;28(12):1120-2.

8.Hussey EK, Dukes GE. Do all histamine2-antagonists cause a warfarin

drug interaction?. DICP 1989 Sep;23(9):675-9.

9.Hunt BA, Sax MJ, Chretien SD, Gray DR, Frank WO, Lalonde RL.

Stereoselective alterations in the pharmacokinetics of warfarin

enantiomers with two cimetidine dose regimens. Pharmacotherapy 1989;

9(3):184.

10.Baciewicz AM, Morgan PJ. Ranitidine-warfarin interaction. Ann

Intern Med 1990 Jan 1;112(1):76-7.

Copyright 2012 First DataBank, Inc.

------------------------------------------------------------

Enter RETURN to continue or '^' to exit:

Display Professional Interaction monograph? N// O

# Check Pharmacogenomic Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS CHECK PGX INTERACTION\]

The Check Pharmacogenomic Interaction option allows users to check for pharmacogenomic interactions by patient or by drug and between pharmacogenomic genes and drugs. The user can review combinations of prospective drug(s), gene(s), and phenotype(s), to view the PGx order checks returned from the vendor. PGx order checks can be returned with a 'High' or 'Medium' severity. These 'High' and 'Medium' PGx order checks come with the option to view "Additional Information', which in addition to data already seen will contain Evidence Ratings and Citations. Another type of PGx order check that users will see is a 'Screen' message. A 'Screen' message suggests that the PGx order check cannot be completed due to uninterpretable gene or phenotype results, even though the vendor database contains genomic findings and PGx guidance exists for the prospective drug.

Figure 108: Example: Check PGx Interaction (same for IV \[PSJI MGR\] Menu)

Select OPTION NAME: CHECK PHARMACOGENOMIC INTERACTION PSS CHECK PGX INTERACTION

> Check Pharmacogenomic Interaction

> PHARMACOGENOMIC (PGx) TEST OPTION

> Do you want to use a specific patient? Y// NO

> Drug selection \*\*\*Only PGx-eligible drugs are available for selection\*\*\*

> Do you want to see the PGx eligible drugs? N// YES

> ABACAVIR SULFATE 300MG TAB

> ACETAMINOPHEN AND CODEINE 30MG

> ALLOPURINOL 100MG S.T.

> ALLOPURINOL 300MG S.T.

> ALLOPURINOL 300MG, 30'S

> ALLOPURINOL NA 500MG/VIL INJ

> AMIKACIN SULFATE 1GM INJ.

> AMIKACIN SULFATE 500MG INJ

> AMITRIPTYLINE 100MG

> AMITRIPTYLINE 10MG TAB

> AMITRIPTYLINE 25MG

> Press Return to continue, '^' to exit list: ^

> Select DRUG: ABACAVIR SULFATE 300MG TAB AM800

> VA PRODUCT: ABACAVIR SO4 300MG TAB

> GCNSEQNO: 40964

> Select Another DRUG:

> Drugs Selected:

> ABACAVIR SULFATE 300MG TAB

> Press Return to continue:

> Select Gene: HLA-B 57:01

> Select Another Gene:

> Genes Selected:

> HLA-B 57:01

> Press Return to continue:

> Genotype selection for HLA-B 57:01 (optional):

> Enter HLA-B 57:01 Activity Score:

> Phenotype selection for HLA-B 57:01

> 1\) HIGH RISK

> 2\) INDETERMINANT ACTIVITY

> 3\) LOW RISK

> Select HLA-B 57:01 Phenotype: (1-3): 1 HIGH RISK

> Gene: HLA-B 57:01

> Genotype:

> Activity Score:

> Phenotype: HIGH RISK

> Inputs:

> Drug: ABACAVIR SULFATE 300MG TAB

> VA Product: ABACAVIR SO4 300MG TAB

> GCNSEQNO: 40964

> Gene: HLA-B 57:01

> Genotype:

> Activity Score:

> Phenotype: HIGH RISK

> Pharmacogenomic HIGH Order Check:

> GENOMIC FINDING: HLA-B \*57:01 positive

> IMPACTED MEDICATION: ABACAVIR SULFATE 300MG TAB

> ACTION: Avoid abacavir use and choose alternative antiretroviral. Alternative

> nucelos(t)ide reverse transcriptase inhibitors (NRTIs) include tenofovir

> disoproxil fumarate, tenofovir alafenamide, lamivudine and emtricitabine.

> RATIONALE: HLA-B\*57:01 carriers are at high risk for severe hypersensitivity

> reaction.

> MONITORING: Abacavir is contraindicated in patients who have the HLA-B\*57:01

> allele.

> For more details on VA National Pharmacogenomics Program go to:

> https://bit.ly/VA-PGx

> Display Additional Information on Pharmacogenomic Order Check(s)? NO// YES

> DEVICE: HOME// Linux Telnet /SSh

> Pharmacogenomics Detailed Information

> GENOMIC FINDING: HLA-B \*57:01 positive

> IMPACTED MEDICATION: ABACAVIR SULFATE 300MG TAB

> SEVERITY LEVEL: HIGH

> EVIDENCE RATINGS:

> SOURCE: Clinical Pharmacogenetics Implementation Consortium (CPIC)

> (1,2)

> RATING: Strong

> SOURCE: Dutch Pharmacogenetics Working Group (DPWG) (3)

> RATING: 4, E

> SOURCE: FDA Table of Pharmacogenetic Associations (4)

> RATING: Therapeutic management recommendation

> SOURCE: Manufacturer prescribing information (5)

> RATING: not applicable

> ACTION:

> Avoid abacavir use and choose alternative antiretroviral. Alternative

> nucelos(t)ide reverse transcriptase inhibitors (NRTIs) include tenofovir

> disoproxil fumarate, tenofovir alafenamide, lamivudine and emtricitabine.

> RATIONALE:

> HLA-B\*57:01 carriers are at high risk for severe hypersensitivity reaction.

> MONITORING:

> Abacavir is contraindicated in patients who have the HLA-B\*57:01 allele.

> CITATIONS:

> \(1\) Martin MA, Klein TE, Dong BJ, et al. Clinical Pharmacogenetics

> Implementation Consortium Guidelines for HLA-B Genotype and Abacavir Dosing.

> Clinical Pharmacology and Therapeutics. 2012 Apr; 91 (4): 734-738. Available

> from

> https://cpicpgx.org/content/guideline/publication/abacavir/2012/22378157.pdf

> \(2\) Clinical Pharmacogenetics Implementation Consortium (CPIC). CPIC Guideline

> for Abacavir and HLA-B. Available from

> https://cpicpgx.org/guidelines/guideline-for-abacavir-and-hla-b/

> \(3\) Dutch Pharmacogenetics Working Group. Pharmacogenomics guidelines.

> Available from

> https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf

> \(4\) FDA Table of Pharmacogenetic Associations. Available from

> https://www.fda.gov/medical-devices/precision-medicine/table-pharmacogenetic-ass

> ociations

> \(5\) Ziagen \[package insert\]. Research Triangle Park, NC. ViiV HealthCare. 2020

> Nov. Available from

> https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/020977s035,020978s038l

> bl.pdf

> First Databank database updated on 07/02/2025.

# Pharmacy Interface Automation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pharmacy Interface Automation is a vital enhancement to the medication transaction functions of the Pharmacy Automated Dispensing Equipment (PADE.) It allows pharmacists to access dispensing equipment remotely; keep a perpetual inventory of all medication received, dispensed, and wasted; alert the pharmacy of medication removed from the devices without orders; and establishes monitors for potentially inappropriate electronic pharmacy transactions.

This menu has the following options:

SA     PADE Send Area Setup

   SS     PADE System Setup

   IN     PADE Inbound Inventory Setup

   RP     PADE Reports

SC     PADE Send Surgery Cases

SO     PADE Send Patient Orders

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/042.png) The Send Area Setup, System Setup and Inbound Inventory Setup are only available to those users who hold the PSJ PADE MGR or PSJ PADE ADV key.

## Displaying PADE Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA Pharmacy Inpatient Order Entry (IOE) screen, if DISPLAY PADE BALANCES is set to Yes, and the drug is in PADE, then IOE will display the number of drugs in PADE while the order is being finished.

The following is an example of IOE where an active PADE exists,  the DISPLAY PADE BALANCES IN IOE is set to YES, and the drug selected is kept in PADE:

<u>Inpatient Order Entry         Dec 23, 2015@15:30:01        Page:    1 of    1</u>

PIAPATIENT,ONE                    Ward: GENERAL

   PID: 666-34-5107           Room-Bed: GENSUR-1    Ht(cm): 200.66 (11/17/15)

   DOB: 01/01/61 (54)                               Wt(kg): 94.55 (11/17/15)

   Sex: MALE                                    Admitted: 07/01/15

Dx: CHEST PAIN Last transferred: \*\*\*\*\*\*\*\*

CrCL: 43.7(est.) (CREAT: 1.5mg/dL 4/19/17) BSA (m2): 1.85

<u>                                                                              </u>

 - - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - -

   1    BACLOFEN TAB                             C  12/18<span id="Inpatient_Order_Entry" class="anchor"></span>/2015  12/29/2015 A  WP 

          Give: 40MG PO Q2H                                                     

          Enter ?? for more actions                                            

PI  Patient Information                 NO  New Order Entry

PU  Patient Record Update               <span id="CM_New_Clinic_Medication_Entry_Example" class="anchor"></span>CM New Clinic Medication Entry

SO  Select Order

Select Action: Quit// NO

Select DRUG: RANITIDINE![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/043.png)

No Enhanced Order Checks can be performed.

   Reason(s): The connection to the vendor database has been disabled.

![](inpatient-medications-supervisor-s-user-manual-psj-5-0-447/044.png)Note: A new action, <span id="P66" class="anchor"></span>CM New Clinic Medication Entry, has been added to the Inpatient order entry screen and is selectable by users for entering Clinic Medication orders.

For more details on the PADE Main Menu Options and the Inpatient Order Entry Profile, refer to the following sections of the [Inpatient Medications Pharmacist's User Manual](http://www.va.gov/vdl/application.asp?appid=88):

- Section 4.1.9 - PADE Main Menu Options
- Section 4.1.4.5 Inpatient Order Entry profile -'PD' flag example.               

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supervisors can view reports of electronic pharmacy transactions from PADE so that they can monitor and investigate pharmacy transactions.

From the PADE Main Menu, supervisors can select RP for PADE Reports, which will give them the option of running and viewing PADE On-Hand Amounts and PADE Transaction Reports.

> **NOTE:** the supervisor will need the PSJ PADE MGR Security Key to access the PADE Reports menu option.

Example: RP – PADE Reports Menu Option

Select OPTION NAME: PADE MAIN MENU  PSJ PADE MAIN MENU     PADE Main Menu

   SA     PADE Send Area Setup

   SS     PADE System Setup

   IN     PADE Inventory Setup ...

   RP     PADE Reports ...

   SC     PADE Send Surgery Cases

You've got PRIORITY mail!

Select PADE Main Menu \<TEST ACCOUNT\> Option: RP  PADE Reports

   IN     PADE On-Hand Amounts

   TR     PADE Transaction Report

For more details on the PADE Main Setup Options, refer to the Inpatient Medications Pharmacy Interface Automation (PIA) Startup and Troubleshooting Guide (updated for PSJ\*5\*432).

# Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Error Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The text in the error message and reason column will be displayed to the user. The type of error is displayed in Column 1.

There are three levels of error messages:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>System</strong></th>
<th>When such an error occurs, no Drug Interaction, Duplicate Therapy, Dosing, or Pharmacogenomic order checks will be performed. Other order checks that do not use the COTS database (FDB) will still be performed such as allergy/ADRs, duplicate drug (for outpatient only) and new CPRS order checks, etc.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Drug</strong></td>
<td><p>The second error level is for the drug and no Drug Interaction, Duplicate Therapy, Dosing, or Pharmacogenomic order checks will be performed for a specific drug. Drug level errors can occur for the prospective drug (drug being processed) or the profile drug. If a drug level error occurs on the prospective drug, no profile drug errors will be displayed. The only exception to this is when you are processing an IV order with multiple prospective drugs (i.e. multiple IV Additives). Profile drug level errors will only be shown once per patient session.</p>
<p>There are two reasons that a drug level error is generated; the drug is not matched to NDF or the drug is matched to NDF, but the VA Product to which it is matched does not have a GCNSEQNO assigned or the GCNSEQNO assigned does not match up to the GCNSEQNO in the COTS database. The latter (GCNSENO mismatch) is rare.</p></td>
</tr>
<tr class="even">
<td><strong>Order</strong></td>
<td>The third error level is for the order. Order level errors will only occur with dosing order checks. Please see the <em><a href="http://vaww.oed.portal.va.gov/projects/pre/PRE_TW/MOCHA%20v2x%20PDFs/Assignments%20and%20Schedule/Kiley&#39;s%20Assignments/Dosing%20Order%20Check%20User%20Manual.doc">Dosing Order Check User Manual</a></em> for more information.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Level</strong></th>
<th><strong>Error Message</strong></th>
<th><strong>Reason</strong></th>
<th><strong>Why message is being displayed</strong></th>
</tr>
<tr class="odd">
<th>System</th>
<th>No Enhanced Order Checks can be performed.</th>
<th>Vendor Database cannot be reached.</th>
<th>The connectivity to the vendor database has gone down. A MailMan message is sent to the G. PSS ORDER CHECKS mail group when the link goes down and when it comes back up.</th>
</tr>
<tr class="header">
<th>System</th>
<th><p>Please perform a manual PGx Order check by using the Check Pharmacogenomic</p>
<p>Interaction option for Drug: &lt;drug&gt;</p></th>
<th>Lab Data could not be retrieved at this time.</th>
<th>The Health Data Repository (HDR) could not be reached to retrieve the patient's pharmacogenomic lab data.</th>
</tr>
<tr class="odd">
<th>System</th>
<th>No Enhanced Order Checks can be performed.</th>
<th>The connection to the vendor database has been disabled.</th>
<th>A user has executed the Enable/Disable Vendor Database Link [PSS ENABLE/DISABLE DB LINK] option and disabled the interface. This will disable drug interactions, duplicate therapy, pharmacogenomic and dosing order checks.</th>
</tr>
<tr class="header">
<th>System</th>
<th>No Enhanced Order Checks can be performed</th>
<th>Vendor database updates are being processed</th>
<th>The vendor database (custom and standard data) is being updated using the DATUP (Data Update) process.</th>
</tr>
<tr class="odd">
<th>System</th>
<th>No Enhanced Order Checks can be performed</th>
<th>An unexpected error has occurred</th>
<th>There is a system network problem and the vendor database cannot be reached or a software interface issue.</th>
</tr>
<tr class="header">
<th>System</th>
<th>No Dosing Order Checks can be performed</th>
<th>Dosing Order Checks are disabled</th>
<th>A user has executed the <em>Enable/Disable Dosing Order Checks</em> [PSS Dosing Order Checks] option.</th>
</tr>
<tr class="odd">
<th>System</th>
<th>Recommended frequency of &lt;DRUG NAME&gt;: Unable to convert units: &lt;DOSE UNIT&gt; to &lt;DOSE UNIT&gt;. A frequency check was not performed because the ordered dose of &lt;DOSE UNIT&gt; is not convertible to the dose screening unit of measure of &lt;DOSE UNIT&gt;.</th>
<th></th>
<th>VA customization may exist in which the Dose Units were customized but the patient age is not within bounds of the customized age bands. VA NDF team to refer to PECS to introduce and/or update VA customizations for the patient ages.</th>
</tr>
<tr class="header">
<th>Drug</th>
<th>Enhanced Order Checks cannot be performed for Local or Local Outpatient Drug: &lt;DRUG NAME&gt;</th>
<th>Drug not matched to NDF</th>
<th>The local drug being ordered/ or on profile has not been matched to NDF. Matching the drug to a VA Product will eliminate this message.</th>
</tr>
<tr class="odd">
<th>Drug</th>
<th><p>Order Checks could not be done for Remote Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions and Duplicate Therapy.</p>
<p>Remote order indicator.</p>
<p>Order Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy, Appropriate Dosing and Pharmacogenomics.</p></th>
<th></th>
<th><p>If this error message is displayed, it means that the VA product that the local or remote drug being ordered/or on the local or remote profile does not have a GCNSEQNO or in rare cases, the GCNSEQNO assigned to the VA Product does not match up with a GCNSEQNO in the vendor database.</p>
<p>If the VA Product the Dispense Drug is matched to does not have a GCNSEQNO and is PGx eligible, Pharmacogenomics will be added to the error message.</p></th>
</tr>
<tr class="header">
<th>Drug</th>
<th>Enhanced Order Checks cannot be performed for Orderable Item: &lt;OI NAME&gt;</th>
<th>No active Dispense Drug found</th>
<th>Highly unlikely that this error would be seen. At the time the order check was being performed the orderable item did not have an active dispense drug associated.</th>
</tr>
<tr class="odd">
<th>Drug</th>
<th>&lt;DRUG NAME&gt; is contraindicated for this patient. Do NOT prescribe/administer this drug by the CONTRAINDICATED &lt;DRUG ROUTE&gt;.</th>
<th>Contraindication</th>
<th>The chosen route is contraindicated and should not be selected.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action Prompts</strong></th>
<th>There are three types of Inpatient Medications "Action" prompts that occur during order entry: ListMan, Patient/Order, and Hidden action prompts.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ListMan Action Prompts</strong></td>
<td><blockquote>
<p>+ Next Screen</p>
<p>- Previous Screen</p>
<p>UP Up a Line</p>
<p>DN Down a Line</p>
<p>&gt; Shift View to Right</p>
<p>&lt; Shift View to Left</p>
<p>FS First screen</p>
<p>LS Last Screen</p>
<p>GO Go to Page</p>
<p>RD Re Display Screen</p>
<p>PS Print Screen</p>
<p>PT Print List</p>
<p>SL Search List</p>
<p>Q Quit</p>
<p>ADPL Auto Display (on/off)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Patient/Order Action Prompts</strong></td>
<td><blockquote>
<p>PU Patient Record Updates</p>
<p>DA Detailed Allergy/ADR List</p>
<p>VP View Profile</p>
<p>NO New Orders Entry</p>
<p><span id="CM_New_Clinic_Medication" class="anchor"></span>CM New Clinic Medication Entry</p>
<p>IN Intervention Menu</p>
<p>PI Patient Information</p>
<p>SO Select Order</p>
<p>DC Discontinue</p>
<p>ED Edit</p>
<p>FL Flag</p>
<p>VF Verify</p>
<p>HD Hold</p>
<p>RN Renew</p>
<p>AL Activity Logs</p>
<p>OC On Call</p>
<p>NL Print New IV Labels</p>
<p>RL Reprint IV Labels</p>
<p>RC Recycled IV</p>
<p>DT Destroyed IV</p>
<p>CA Cancelled IV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Hidden Action Prompts</strong></td>
<td><blockquote>
<p>LBL Label Patient/Report</p>
<p>JP Jump to a Patient</p>
<p>OTH Other Pharmacy Options</p>
<p>MAR MAR Menu</p>
<p>DC Speed Discontinue</p>
<p>RN Speed Renew</p>
<p>SF Speed Finish</p>
<p>SV Speed Verify</p>
<p>CO Copy</p>
<p>N Mark Not to be Given</p>
<p>I Mark Incomplete</p>
<p>DIN Drug Restr/Guide</p>
<p>DA Display Drug Allergies</p>
<p>OCI Overrides/Interventions Options</p>
<p>CK Check Drug Interaction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Active Order</strong></td>
<td>Any order which has not expired or been discontinued. Active orders also include any orders that are on hold or on call.</td>
</tr>
<tr class="odd">
<td><strong>Activity Reason Log</strong></td>
<td>The complete list of all activity related to a patient order. The log contains the action taken, the date of the action, and the user who took the action.</td>
</tr>
<tr class="even">
<td><strong>Activity Ruler</strong></td>
<td>The activity ruler provides a visual representation of the relationship between manufacturing times, doses due, and order start times. The intent is to provide the on-the-floor user with a means of tracking activity in the IV room and determining when to call for doses before the normal delivery. The activity ruler can be enabled or disabled under the <em>SIte Parameters (IV)</em> option.</td>
</tr>
<tr class="odd">
<td><strong>Additive</strong></td>
<td>A drug that is added to an IV solution for the purpose of parenteral administration. An additive can be an electrolyte, a vitamin or other nutrient, or an antibiotic. Only an electrolyte or multivitamin type additives can be entered as IV fluid additives in CPRS.</td>
</tr>
<tr class="even">
<td><strong>ADMINISTRATION SCHEDULE File</strong></td>
<td>File #51.1. This file contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule type (e.g., QID, Q4H, PRN). The administration time entered is in military time, with each time separated from the next by a dash, and times listed in ascending order.</td>
</tr>
<tr class="odd">
<td><strong>Administering Teams</strong></td>
<td>Nursing teams used in the administration of medication to the patients. There can be a number of teams assigned to take care of one ward, with specific rooms and beds assigned to each team.</td>
</tr>
<tr class="even">
<td><strong>Admixture</strong></td>
<td>An admixture is a type of intravenously administered medication comprised of any number of additives (including zero) in one solution. It is given at a specified flow rate; when one bottle or bag is empty, another is hung.</td>
</tr>
<tr class="odd">
<td><strong>APSP INTERVENTION File</strong></td>
<td>File #9009032.4. This file is used to enter pharmacy interventions. Interventions in this file are records of occurrences where the pharmacist had to take some sort of action involving a particular prescription or order. A record would record the provider involved, why an intervention was necessary, what action was taken by the pharmacists, etc.</td>
</tr>
<tr class="even">
<td><strong>Average Unit Drug Cost</strong></td>
<td>The total drug cost divided by the total number of units of measurement.</td>
</tr>
<tr class="odd">
<td><strong>BCMA</strong></td>
<td>A <strong>V</strong><em>IST</em><strong>A</strong> computer software package named Bar Code Medication Administration. This package validates medications against active orders prior to being administered to the patient.</td>
</tr>
<tr class="even">
<td><strong>BSA</strong></td>
<td><p>Body Surface Area. The Dubois formula is used to calculate the Body Surface Area using the following formula:</p>
<p>BSA (m²) = 0.20247 x Height (m)<sup>0.725</sup> x Weight (kg)<sup>0.425</sup></p>
<p>The equation is performed using the most recent patient height and weight values that are entered into the vitals package.</p>
<p>The calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy</strong></td>
<td>Chemotherapy is the treatment or prevention of cancer with chemical agents. The chemotherapy IV type administration can be a syringe, admixture, or a piggyback. Once the subtype (syringe, piggyback, etc.) is selected, the order entry follows the same procedure as the type that corresponds to the selected subtype (e.g., piggyback type of chemotherapy follows the same entry procedure as regular piggyback IV).</td>
</tr>
<tr class="even">
<td><strong>Chemotherapy: "Admixture"</strong>;</td>
<td>The Chemotherapy "Admixture" IV type follows the same order entry procedure as the regular admixture IV type. This type is in use when the level of toxicity of the chemotherapy drug is high and is to be administered continuously over an extended period of time (e.g., hours or days).</td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy "Piggyback"</strong></td>
<td>The Chemotherapy "Piggyback" IV type follows the same order entry procedure as the regular piggyback IV type. This type of chemotherapy is in use when the chemotherapy drug does not have time constraints on how fast it must be infused into the patient. These types are normally administered over a 30 - 60 minute interval.</td>
</tr>
<tr class="even">
<td><strong>Chemotherapy "Syringe"</strong></td>
<td>The Chemotherapy "Syringe" IV type follows the same order entry procedure as the regular syringe IV type. Its administration may be continuous or intermittent. The pharmacist selects this type when the level of toxicity of the chemotherapy drug is low and needs to be infused directly into the patient within a short time interval (usually 1-2 minutes).</td>
</tr>
<tr class="odd">
<td><strong>Clinic Group</strong></td>
<td>A clinic group is a combination of outpatient clinics that have been defined as a group within Inpatient Medications to facilitate processing of orders.</td>
</tr>
<tr class="even">
<td><strong>CLINIC DEFINITION File</strong></td>
<td>File #53.46. This file is used in conjunction with Inpatient Medications for Outpatients (IMO) to give the user the ability to define, by clinic, default stop dates, whether to auto-dc IMO orders, define the number of days to display discontinued and expired clinic orders, and the option to set a clinic as an <span id="opioid_3" class="anchor"></span>Opioid Treatment Clinic.</td>
</tr>
<tr class="odd">
<td><span id="Glossary_CM_New_Clinic_Medication_Entry" class="anchor"></span><strong>CM New Clinic Medication Entry</strong></td>
<td>This is an action in backdoor Inpatient order entry that allows users to enter clinic orders.</td>
</tr>
<tr class="even">
<td><strong>Continuous Syringe</strong></td>
<td>A syringe type of IV that is administered continuously to the patient, similar to a hyperal IV type. This type of syringe is commonly used on outpatients and administered automatically by an infusion pump.</td>
</tr>
<tr class="odd">
<td><strong>Coverage Times</strong></td>
<td><p>The start and end of coverage period designates administration times covered by a manufacturing run. There must be a coverage period for all IV types: admixtures and primaries, piggybacks, hyperals, syringes, and chemotherapy. For one type, admixtures for example, the user might define two coverage periods; one from 1200 to 0259 and another from 0300 to 1159 (this would mean that the user has two manufacturing times for admixtures).</p>
<p><strong>Note:</strong> If any of the five Coverage Times are not present in file 59.5 (IV Room) the following warning message will be displayed, "The [name of file 59.5 entry] IV ROOM can be updated using option 'Site Parameters (IV)' by a holder of the PSJI MGR VistA Security Key. Contact the Pharmacy Informaticist to update the IV Room parameters."</p></td>
</tr>
<tr class="even">
<td><strong>CPRS</strong></td>
<td>A <strong>V</strong><em>IST</em><strong>A</strong> computer software package called Computerized Patient Record Systems. CPRS is an application in <strong>V</strong><em>IST</em><strong>A</strong> that allows the user to enter all necessary orders for a patient in different packages from a single application. All pending orders that appear in the Unit Dose and IV modules are initially entered through the CPRS package.</td>
</tr>
<tr class="odd">
<td><strong>CrCL</strong></td>
<td><p>Creatinine Clearance. The CrCL value which displays in the pharmacy header is identical to the CrCL value calculated in CPRS. The formula approved by the CPRS Clinical Workgroup is the following:</p>
<p>Modified Cockcroft-Gault equation using Adjusted Body Weight in kg (if ht &gt; 60in)</p>
<p>This calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="even">
<td><strong>Cumulative Doses</strong></td>
<td>The number of IV doses actually administered, which equals the total number of bags dispensed less any recycled, destroyed, or canceled bags.</td>
</tr>
<tr class="odd">
<td><strong>DATUP</strong></td>
<td>Data Update (DATUP). Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out VA custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the production and pre-production centralized MOCHA databases at Austin and Philadelphia.</td>
</tr>
<tr class="even">
<td><strong>Default Answer</strong></td>
<td>The most common answer, predefined by the system to save time and keystrokes for the user. The default answer appears before the two slash marks (//) and can be selected by the user by pressing &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="odd">
<td><strong>Dispense Drug</strong></td>
<td>The Dispense Drug is pulled from the DRUG file (#50) and usually has the strength attached to it (e.g., Acetaminophen 325 mg). Usually, the name alone without a strength attached is the Orderable Item name.</td>
</tr>
<tr class="even">
<td><strong>Delivery Times</strong></td>
<td>The time(s) when IV orders are delivered to the wards.</td>
</tr>
<tr class="odd">
<td><strong>Dosage Ordered</strong></td>
<td>After the user has selected the drug during order entry, the dosage ordered prompt is displayed.</td>
</tr>
<tr class="even">
<td><strong>DRUG ELECTROLYTES File</strong></td>
<td>File #50.4. This file contains the names of anions/cations, and their concentration units.</td>
</tr>
<tr class="odd">
<td><strong>DRUG File</strong></td>
<td>File #50. This file holds the information related to each drug that can be used to fill a prescription.</td>
</tr>
<tr class="even">
<td><strong>Electrolyte</strong></td>
<td>An additive that disassociates into ions (charged particles) when placed in solution.</td>
</tr>
<tr class="odd">
<td><strong>Enhanced Order Checks</strong></td>
<td>Drug–Drug Interaction, Duplicate Therapy, Pharmacogenomic, and Dosing order checks that are executed utilizing FDB's MedKnowledge Framework APIs and database</td>
</tr>
<tr class="even">
<td><strong>Entry By</strong></td>
<td>The name of the user who entered the Unit Dose or IV order into the computer.</td>
</tr>
<tr class="odd">
<td><strong>FDB</strong></td>
<td>First DataBank</td>
</tr>
<tr class="even">
<td><span id="Gene" class="anchor"></span><strong>Gene</strong></td>
<td>A gene is a section of an individual's DNA that provides instructions for making proteins, including those that affect how the body processes medications.</td>
</tr>
<tr class="odd">
<td><span id="Genotype" class="anchor"></span><strong>Genotype</strong></td>
<td>A genotype is a combination of alleles (version of a gene) which can influence how an individual processes medications.</td>
</tr>
<tr class="even">
<td><strong>Hospital Supplied Self Med</strong></td>
<td>Self medication, which is to be supplied by the Medical Center's pharmacy. Hospital supplied self med is only prompted for if the user answers Yes to the SELF MED: prompt during order entry.</td>
</tr>
<tr class="odd">
<td><strong>Hyperalimentation (Hyperal)</strong></td>
<td>Long term feeding of a protein-carbohydrate solution. Electrolytes, fats, trace elements, and vitamins can be added. Since this solution generally provides all necessary nutrients, it is commonly referred to as Total Parenteral Nutrition (TPN). A hyperal is composed of many additives in two or more solutions. When the labels print, they show the individual electrolytes in the hyperal order.</td>
</tr>
<tr class="even">
<td><strong>Infusion Rate INPATIENT USER</strong></td>
<td>The designated rate of flow of IV fluids into the patient.File #53.45. This file is used to tailor various aspects</td>
</tr>
<tr class="odd">
<td><strong>PARAMETERS File</strong></td>
<td>of the Inpatient Medications package with regards to specific users. This file also contains fields that are used as temporary storage of data during order entry/edit.</td>
</tr>
<tr class="even">
<td><strong>INPATIENT WARD PARAMETERS File</strong></td>
<td>File #59.6. This file is used to tailor various aspects of the Inpatient Medications package with regards to specific wards.</td>
</tr>
<tr class="odd">
<td><strong>Intermittent Syringe</strong></td>
<td>A syringe type of IV that is administered periodically to the patient according to an administration schedule.</td>
</tr>
<tr class="even">
<td><strong>Internal Order Number</strong></td>
<td>The number on the top left corner of the label of an IV bag in brackets ([ ]). This number can be used to speed up the entry of returns and destroyed IV bags.</td>
</tr>
<tr class="odd">
<td><strong>IV ADDITIVES File</strong></td>
<td>File #52.6. This file contains drugs that are used as additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.</td>
</tr>
<tr class="even">
<td><strong>IV CATEGORY File</strong></td>
<td>File #50.2. This file allows the user to create categories of drugs in order to run "tailor-made" IV cost reports for specific user-defined categories of drugs. The user can group drugs into categories.</td>
</tr>
<tr class="odd">
<td><strong>IV Duration</strong></td>
<td>The duration of an order may be entered in CPRS at the IV DURATION OR TOTAL VOLUME field in the IV Fluids order dialog. The duration may be specified in terms of volume (liters or milliliters), or time (hours or days). Inpatient Medications uses this value to calculate a default stop date/time for the order at the time the order is finished.</td>
</tr>
<tr class="even">
<td><strong>IV Label Action</strong></td>
<td><p>A prompt, requesting action on an IV label, in the form of "Action ( )", where the valid codes are shown in the parentheses. The following codes are valid:</p>
<blockquote>
<p>P – Print a specified number of labels now.</p>
<p>B – Bypass any more actions.</p>
<p>S – Suspend a specified number of labels for the IV room to print on demand.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>IV Room Name</strong></td>
<td>The name identifying an IV distribution area.</td>
</tr>
<tr class="even">
<td><strong>IV SOLUTIONS File</strong></td>
<td>File #52.7. This file contains drugs that are used as primary solutions in the IV room. The solution must already exist in the Drug file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.</td>
</tr>
<tr class="odd">
<td><strong>IV STATS File</strong></td>
<td>File #50.8. This file contains information concerning the IV workload of the pharmacy. This file is updated each time the <em>COmpile IV Statistics</em> option is run and the data stored is used as the basis for the AMIS (IV) report.</td>
</tr>
<tr class="even">
<td><strong>Label Device</strong></td>
<td>The device, identified by the user, on which computer-generated labels will be printed.</td>
</tr>
<tr class="odd">
<td><strong>Local Possible Dosages</strong></td>
<td>Free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.</td>
</tr>
<tr class="even">
<td><strong>LVP</strong></td>
<td>Large Volume Parenteral (LVP — Admixture. A solution intended for continuous parenteral infusion, administered as a vehicle for additive (s) or for the pharmacological effect of the solution itself. It is comprised of any number of additives, including zero, in one solution. An LVP runs continuously, with another bag hung when one bottle or bag is empty.</td>
</tr>
<tr class="odd">
<td><strong>Manufacturing Times</strong></td>
<td>The time(s) that designate(s) the general time when the manufacturing list will be run and IV orders prepared. This field in the <em>SIte Parameters (IV)</em> option (IV Room file (#59.5)) is for documentation only and does not affect IV processing.</td>
</tr>
<tr class="even">
<td><strong>MEDICATION ADMINISTERING TEAM File</strong></td>
<td>File #57.7. This file contains wards, the teams used in the administration of medication to that ward, and the rooms/beds assigned to that team.</td>
</tr>
<tr class="odd">
<td><strong>MEDICATION INSTRUCTION File</strong></td>
<td>File #51. This file is used by Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion, and intended use.</td>
</tr>
<tr class="even">
<td><strong>MEDICATION ROUTES File</strong></td>
<td>File #51.2. This file contains medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.</td>
</tr>
<tr class="odd">
<td><strong>Medication Routes/ Abbreviations</strong></td>
<td>Route by which medication is administered (e.g., oral). The Medication Routes file (#51.2) contains the routes and abbreviations, which are selected by each VAMC. The abbreviation cannot be longer than five characters to fit on labels and the MAR. The user can add new routes and abbreviations as appropriate.</td>
</tr>
<tr class="even">
<td><strong>Non-Formulary Drugs</strong></td>
<td>The medications that are defined as commercially available drug products not included in the VA National Formulary.</td>
</tr>
<tr class="odd">
<td><strong>Non-Verified Orders</strong></td>
<td>Any order that has been entered in the Unit Dose or IV module that has not been verified (made active) by a nurse and/or pharmacist. Ward staff may not verify a non-verified order.</td>
</tr>
<tr class="even">
<td><strong>Orderable Item</strong></td>
<td>An Orderable Item name has no strength attached to it (e.g., Acetaminophen). The name with a strength attached to it is the Dispense Drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="odd">
<td><strong>Order Check</strong></td>
<td>Order checks (drug-allergy/ADR interactions, drug-drug interactions, duplicate drug, and duplicate therapy, PGx, and dosing) are performed when a new medication order is placed through either the CPRS or Inpatient Medications applications. They are also performed when medication orders are renewed, when Orderable Items are edited, or during the finishing process in Inpatient Medications. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error.</td>
</tr>
<tr class="even">
<td><strong>Order Sets</strong></td>
<td>An Order Set is a set of N pre-written orders. (N indicates the number of orders in an Order Set is variable.) Order Sets are used to expedite order entry for drugs that are dispensed to all patients in certain medical practices and procedures.</td>
</tr>
<tr class="odd">
<td><strong>Order View</strong></td>
<td>Computer option that allows the user to view detailed information related to one specific order of a patient. The order view provides basic patient information and identification of the order variables.</td>
</tr>
<tr class="even">
<td><strong>Parenteral</strong></td>
<td>Introduced by means other than by way of the digestive track.</td>
</tr>
<tr class="odd">
<td><strong>Patient Profile</strong></td>
<td>A listing of a patient's active and non-active Unit Dose and IV orders. The patient profile also includes basic patient information, including the patient's name, social security number, date of birth, diagnosis, ward location, date of admission, reactions, and any pertinent remarks.</td>
</tr>
<tr class="even">
<td><strong>PECS</strong></td>
<td>Pharmacy Enterprise Customization System. A Graphical User Interface (GUI) web-based application used to research, update, maintain, and report VA customizations of the commercial-off-the-shelf (COTS) vendor database used to perform Pharmacy order checks such as drug-drug interactions, duplicate therapy, dosing, and pharmacogenomics.</td>
</tr>
<tr class="odd">
<td><strong>Pending Order</strong></td>
<td>A pending order is one that has been entered by a provider through CPRS without Pharmacy or Nursing finishing the order. Once Pharmacy or Nursing has finished and verified the order, it will become active.</td>
</tr>
<tr class="even">
<td><span id="PGx_Definition" class="anchor"></span><strong>Pharmacogenomics (PGx)</strong></td>
<td>Pharmacogenomics (PGx) is the application of genetic information to predict how a person will respond to medications. It uses genetic data to guide drug selection and dosing, helping ensure treatments are both safe and effective.</td>
</tr>
<tr class="odd">
<td><strong>PHARMACY SYSTEM File</strong></td>
<td>File #59.7. This file contains data that pertains to the entire Pharmacy system of a medical center, and not to any one site or division.</td>
</tr>
<tr class="even">
<td><strong>Piggyback</strong></td>
<td>Small volume parenteral solution for intermittent infusion. A piggyback is comprised of any number of additives, including zero, and one solution; the mixture is made in a small bag. The piggyback is given on a schedule (e.g., Q6H). Once the medication flows in, the piggyback is removed; another is not hung until the administration schedule calls for it.</td>
</tr>
<tr class="odd">
<td><span id="Phenotype" class="anchor"></span><strong>Phenotype</strong></td>
<td>A phenotype is the observable result of an individual's genes; in pharmacogenomics, it refers to how a person will respond to medications. It uses genetic data to guide drug selection and dosing, helping ensure treatments are both safe and effective.</td>
</tr>
<tr class="even">
<td><strong>Possible Dosages</strong></td>
<td>Dosages that have a numeric dosage and numeric dispense units per dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to the VA PRODUCT file (#50.68). The VA PRODUCT file (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.</td>
</tr>
<tr class="odd">
<td><strong>Pre-Exchange Units</strong></td>
<td>The number of actual units required for this order until the next cart exchange.</td>
</tr>
<tr class="even">
<td><strong>Primary Solution</strong></td>
<td>A solution, usually an LVP, administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. Infusion is generally continuous. An LVP or piggyback has only one solution (primary solution). A hyperal can have one or more solutions.</td>
</tr>
<tr class="odd">
<td><strong>Print Name</strong></td>
<td>Drug generic name as it is to appear on pertinent IV output, such as labels and reports. Volume or Strength is not part of the print name.</td>
</tr>
<tr class="even">
<td><strong>Print Name{2}</strong></td>
<td>Field used to record the additives contained in a commercially purchased premixed solution.</td>
</tr>
<tr class="odd">
<td><strong>Profile</strong></td>
<td>The patient profile shows a patient's orders. The Long profile includes all the patient's orders, sorted by status: active, non-verified, pending, and non-active. The Short profile will exclude the patient's discontinued and expired orders.</td>
</tr>
<tr class="even">
<td><strong>Prompt</strong></td>
<td>A point at which the system questions the user and waits for a response.</td>
</tr>
<tr class="odd">
<td><strong>Provider</strong></td>
<td>Another term for the physician involved in the prescription of an IV or Unit Dose order for a patient.</td>
</tr>
<tr class="even">
<td><strong>PSJI MGR</strong></td>
<td>The name of the <em>key</em> that allows access to the supervisor functions necessary to run the IV medications software. Usually given to the Inpatient package coordinator.</td>
</tr>
<tr class="odd">
<td><strong>PSJI PHARM TECH</strong></td>
<td>The name of the <em>key</em> that must be assigned to pharmacy technicians using the IV module. This key allows the technician to finish IV orders, but not verify them.</td>
</tr>
<tr class="even">
<td><strong>PSJI PURGE</strong></td>
<td>The <em>key</em> that must be assigned to individuals allowed to purge expired IV orders. This person will most likely be the IV application coordinator.</td>
</tr>
<tr class="odd">
<td><strong>PSJI RNFINISH</strong></td>
<td>The name of the <em>key</em> that is given to a user to allow the finishing of IV orders. This user must also be a holder of the PSJ RNURSE key.</td>
</tr>
<tr class="even">
<td><strong>PSJI USR1</strong></td>
<td>The <em>primary menu option</em> that may be assigned to nurses.</td>
</tr>
<tr class="odd">
<td><strong>PSJI USR2</strong></td>
<td>The <em>primary menu option</em> that may be assigned to technicians.</td>
</tr>
<tr class="even">
<td><strong>PSJU MGR</strong></td>
<td>The name of the <em>primary menu</em> and of the <em>key</em> that must be assigned to the pharmacy package coordinators and supervisors using the Unit Dose Medications module.</td>
</tr>
<tr class="odd">
<td><strong>PSJU PL</strong></td>
<td>The name of the <em>key</em> that must be assigned to anyone using the <em>Pick List Menu</em> options.</td>
</tr>
<tr class="even">
<td><strong>PSJ PHARM TECH</strong></td>
<td>The name of the <em>key</em> that must be assigned to pharmacy technicians using the Unit Dose Medications module.</td>
</tr>
<tr class="odd">
<td><strong>PSJ RNFINISH</strong></td>
<td>The name of the <em>key</em> that is given to a user to allow the finishing of a Unit Dose order. This user must also be a holder of the PSJ RNURSE key.</td>
</tr>
<tr class="even">
<td><strong>PSJ RNURSE</strong></td>
<td>The name of the <em>key</em> that must be assigned to nurses using the Unit Dose Medications module.</td>
</tr>
<tr class="odd">
<td><strong>PSJ RPHARM</strong></td>
<td>The name of the <em>key</em> that must be assigned to a pharmacist to use the Unit Dose Medications module. If the package coordinator is also a pharmacist he/she must also be given this key.</td>
</tr>
<tr class="even">
<td><strong>Quick Code</strong></td>
<td>An abbreviated form of the drug generic name (from one to ten characters) for IV orders. One of the three drug fields on which lookup is done to locate a drug. Print name and synonym are the other two. Use of quick codes will speed up order entry, etc.</td>
</tr>
<tr class="odd">
<td><strong>Report Device</strong></td>
<td>The device, identified by the user, on which computer-generated reports selected by the user will be printed.</td>
</tr>
<tr class="even">
<td><strong>Schedule</strong></td>
<td>The frequency of administration of a medication (e.g., QID, QDAILY, QAM, STAT, Q4H).</td>
</tr>
<tr class="odd">
<td><strong>Schedule Type</strong></td>
<td>Codes include: <strong>O</strong> - one time (i.e., STAT - only once), <strong>P</strong> - PRN (as needed; no set administration times). <strong>C</strong>- continuous (given continuously for the life of the order; usually with set administration times). <strong>R</strong> - fill on request (used for items that are not automatically put in the cart - but are filled on the nurse's request. These can be multidose items (e.g., eye wash, kept for use by one patient and is filled on request when the supply is exhausted)). And <strong>OC</strong> - on call (one time with no specific time to be given, i.e., 1/2 hour before surgery).</td>
</tr>
<tr class="even">
<td><strong>Self Med</strong></td>
<td>Medication that is to be administered by the patient to himself.</td>
</tr>
<tr class="odd">
<td><strong>Standard Schedule</strong></td>
<td>Standard medication administration schedules stored in the Administration Schedule file (#51.1).</td>
</tr>
<tr class="even">
<td><strong>Start Date/Time</strong></td>
<td>The date and time an order is to begin.</td>
</tr>
<tr class="odd">
<td><strong>Status</strong></td>
<td><strong>A</strong> - active, <strong>E</strong> - expired, <strong>R</strong> - renewed (or reinstated), <strong>D</strong> - discontinued, <strong>H</strong> - on hold, <strong>I</strong> - incomplete, or <strong>N</strong> - non-verified, <strong>U</strong> – unreleased, <strong>P</strong> – pending, <strong>O</strong> – on call, <strong>DE</strong> – discontinued edit, <strong>RE</strong> – reinstated, <strong>DR</strong> – discontinued renewal.</td>
</tr>
<tr class="even">
<td><strong>Stop Date/Time</strong></td>
<td>The date and time an order is to expire. The system calculates the default Stop Date/Time for order administration based on the STOP TIME FOR ORDER site parameter. The default date shown is the least of (1) the &lt;IV TYPE&gt; GOOD FOR HOW MANY DAYS site parameter (where &lt;IV TYPE&gt; is LVPs, PBs, etc.), (2) the NUMBER OF DAYS FOR IV ORDER field (found in the IV Additives file) for all additives in this order, (3) the DAY (nD) or DOSE (nL) LIMIT field (found in the PHARMACY ORDERABLE ITEM file) for the orderable item associated with this order or (4) the duration received from CPRS (if applicable). The Site Manager or Application Coordinator can change any field except duration.</td>
</tr>
<tr class="odd">
<td><strong>Stop Order Notices</strong></td>
<td>A list of patient medications that are about to expire and may require action.</td>
</tr>
<tr class="even">
<td><strong>Syringe</strong></td>
<td>Type of IV that uses a syringe rather than a bottle or bag. The method of infusion for a syringe-type IV may be continuous or intermittent.</td>
</tr>
<tr class="odd">
<td><strong>Syringe Size</strong></td>
<td>The syringe size is the capacity or volume of a particular syringe. The size of a syringe is usually measured in number of cubic centimeters (ccs).</td>
</tr>
<tr class="even">
<td><strong>TPN</strong></td>
<td>Total Parenteral Nutrition. The intravenous administration of the total nutrient requirements of the patient. The term TPN is also used to mean the solution compounded to provide those requirements.</td>
</tr>
<tr class="odd">
<td><strong>Units per Dose</strong></td>
<td>The number of Units (tablets, capsules, etc.) to be dispensed as a Dose for an order. Fractional numbers will be accepted.</td>
</tr>
<tr class="even">
<td><strong>VA Drug Class Code</strong></td>
<td>A drug classification system used by VA that separates drugs into different categories based upon their characteristics. IV cost reports can be run for VA Drug Class Codes.</td>
</tr>
<tr class="odd">
<td><strong>VDL</strong></td>
<td>Virtual Due List. This is a Graphical User Interface (GUI) application used by the nurses when administering medications.</td>
</tr>
<tr class="even">
<td><strong>Ward Group</strong></td>
<td>A ward group indicates inpatient nursing units (wards) that have been defined as a group within Inpatient Medications to facilitate processing of orders.</td>
</tr>
<tr class="odd">
<td><strong>WARD GROUP File</strong></td>
<td>File #57.5. This file contains the name of the ward group and the wards included in that group. The grouping is necessary for the pick list to be run for specific carts and ward groups.</td>
</tr>
<tr class="even">
<td><strong>Ward Group Name</strong></td>
<td>A field in the WARD GROUP File (#57.5) used to assign an arbitrary name to a group of wards for the pick list and medication cart.</td>
</tr>
<tr class="odd">
<td><strong>WARD LOCATION File</strong></td>
<td>File #42. This file contains all of the facility ward locations and their related data, i.e., Operating beds, Bedsection, etc. The wards are created/edited using the <em>Ward Definition</em> option of the ADT module.</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Abbreviated Order Entry, 24
Active Order Report by Ward/Drug (IV), 44
Additive, 43
Administering Teams, 5
Administering Teams Example, 5
AMIS (Cost per Ward), 10
AMIS (Cost per Ward) Report Example, 11
AMIS (Cost per Ward) Report with No Data Example, 11
AMIS (IV), 46
AMIS (IV) Report Example, 46
Asterisk, 12
ATC Machine, 31
Authorized Absence, 22, 40
Auto-Discontinue, 21, 22, 23, 27, 39, 40, 41
Auto-Discontinue IMO Orders, 6, 7, 33
Auto-Discontinue Set-Up, 21, 39
Auto-Discontinue Set-Up Example, 23, 41
B
BCMA, 1, 72
C
Category, 12, 42, 47, 53, 55
Category File (IV), 42
Category File (IV) Example, 42
CLINIC DEFINITION File, 33, 73
Clinic Definition Option, 6, 33
Clinic Group, 73
Clinic Groups, 5, 6, 9
Compile IV Statistics (IV), 43
CPRS, 1, 71, 73, 77
CPRS Order checks: How they work, 61
D
Default Start Date Calculation, 26
Delete A Drug From A Category Example, 42
Delete a Pick List, 35
Delete a Pick List Example, 35
Delete Orders (IV), 56
Detailed Allergy/ADR List, 70
Dispense Drug, 12, 14, 23, 25, 51, 52, 74, 77
Dosing Order Checks, 60
Drug (Cost and/or Amount), 11
Drug (Cost and/or Amount) Report Example, 12
Drug (Cost and/or Amount) Report with No Data Example, 13
Drug Cost Report (IV), 47
Drug Cost Report (IV) Example, 48
E
Enhanced Order Checks, 74
Error Information, 68
Error Messages, 68
Expired IV Time Limit, 32, 33
I
Inpatient Medications for Outpatients (IMO), 6, 9
Inpatient User Parameters Edit, 23
Inpatient User Parameters Edit Example, 25
Inpatient Ward Parameters Edit, 26
Inpatient Ward Parameters Edit Example, 29
Intervention Menu, 70
Introduction, 1
IRMS, 43
IV Additives File, 43, 57
IV Bags, 46, 47, 75
IV Duration, 75
IV Room, 47, 53, 58, 71, 75, 76
IV Solutions File, 43, 57
IV Stats File, 43, 44, 57
IV Type, 42, 47, 72, 73
M
Management Reports (IV), 44
Management Reports (IV) Example, 44
Management Reports Menu, 10
Management Reports Menu Example, 7, 8, 10
MAR, 1, 3, 27, 28, 29, 30, 31, 77
MAS Type Ward Group, 37
Medication Administering Team File, ii, 5
N
Non-Formulary Drugs, 31, 47, 53, 55
Non-Standard Schedule, 5, 18
O
OCXCACHE, 61
On Pass, 21, 39
Order check
data caching, 61
OCXCACHE, 61
XTMP, 61
Order Check, 77
Order Check Data Caching, 61
Order Set, 19, 20
Order Set Enter/Edit, 19
Order Set Enter/Edit Example, 20
Orderable Item, 12, 14, 20, 23, 25, 51, 52, 74, 77
Orientation, 3
P
Parameters Edit Menu, 21
Parameters Edit Menu Example, 21
Patient Cost Report (IV), 49
Patient Cost Report (IV) Example, 50, 51
Patient Information, 70
Patient Order Purge, 34
Patients on Specific Drug(s), 14, 51
Patients on Specific Drug(s) Report Example, 14, 52
PDM, 57
Pharmacy Type Ward Group, 37
Pick List, 1, 11, 31, 32, 34, 35, 36, 37, 79, 81
Pick List Auto Purge Set/Reset, 35
Pick List Auto Purge Set/Reset Example, 35
Pick List Menu, 34
Pick List Menu Example, 34
Piggyback, 47, 72, 73, 78
PIMS, 23, 41
Priorities For Active Notify, 32, 34
Priorities For Notification, 28, 30
Priorities For Pending Notify, 32, 33
Provider, 15, 24, 42, 53, 72, 77
Provider (Cost Per), 15
Provider (Cost per) Report Example, 15
Provider Drug Cost Report (IV), 53
Provider Drug Cost Report (IV) Example, 53
PSJ PHARM TECH Key, 24, 25
PSJ RNURSE Key, 24
PSJ RPHARM Key, 24
PSJI BACKGROUND Option, 43
PSJI MGR Key, 44
PSJI PHARM TECH Key, 24, 78
PSJI PURGE Key, 56
PSJI RNFINISH Key, 79
PSJ-ORDERS-REINSTATED Mail Group, 23, 41
PSJU MGR Key, 35
PSJU PL Key, 3
Purge Data (IV), 56
Purge Expired Orders (IV), 57
Purge Pick Lists, 36
Purge Pick Lists Example, 36
R
Recompile Stats File (IV), 57
Regular Order Entry, 24
Revision History, i
S
Select Order, 70
Service (Total Cost Per), 16
Service (Total Cost per) Report Example, 17
Service Transfer, 22, 40
Site Parameter (IV), 58
Site Parameter (IV) Example, 58
Speed Actions
Speed Discontinue, 71
Speed Finish, 71
Speed Renew, 71
Speed Verify, 71
STAT NOW Mail Group, 28
Stop Date/Time, 26
Supervisor's Menu, 5
Supervisor's Menu (IV), 39
Supervisor's Menu (IV) Example, 39
Supervisor's Menu Example, 5
Syringe, 47, 72, 73, 75, 80
Systems Parameters Edit, 31
T
Table of Contents, vi
Total Cost to Date (Current Patients), 17
Total Cost to Date (Current Patients) Report Example, 17
U
Unauthorized Absence, 22, 40
V
VA Class, 12, 14, 51, 52
VA Drug Class, 47, 53, 55
VDL, 80
View Profile, 70
V*IST*A, 73
W
Ward Clerk, 23, 24
Ward Group, 80
Ward Group File, 36
Ward Groups, 36
Ward Groups Example, 37
Ward Location File, 17, 36
Ward Order Entry, 24
Ward Staff, 27
<u>Ward Transfer</u>, 21, 39
Ward/Drug Usage Report (IV), 55
Ward/Drug Usage Report (IV) Example, 55
X
XTMP, 61


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Inpatient Medications Version 5 Supervisor's User Manual (Updated PSJ*5*423)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In CPRS, Order Checks occur by evaluating a requested order against existing patient data. Most order checks are processed via the CPRS Expert System. A few are processed within the Pharmacy, Allergy Tracking System, and Order Entry packages. Order Checks are a real-time process that occurs during the ordering session and is driven by responses entered by the ordering provider. Order Check messages are displayed interactively in the ordering session.

Order Checks review existing data and current events to produce a relevant message, which is presented to patient caregivers. Order Checks use the CPRS Expert System (OCX namespace), to define logical expressions for this evaluation and message creation. In addition to the expert system Order Checks have some hard-coded algorithms. For example, the drug-drug interaction order check is made via an entry point in the pharmacy package whereas Renal Functions for Patients Over 65 is defined as a rule in the CPRS Expert System.
