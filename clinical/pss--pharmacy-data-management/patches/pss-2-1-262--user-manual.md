---
title: Dosing Order Check Version 2.1 User Manual (Updated P*1*262)
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: (Updated P*1*262)
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 2.1
patch_id: PSS*2.1*262
group_key: "PSS:PSS:2.1"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - order
  - dose
  - drug
  - dosing
  - checks
  - strong
  - check
  - unit
  - dosage
  - single
page_count: 0
word_count: 68223
section_count: 17
table_count: 10
figure_count: 0
appendix_count: 7
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/PSS_1_DOSING_ORD_CK_p262_UM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/PSS_1_DOSING_ORD_CK_p262_UM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/001.png)

Dosing Order Check

User Manual

Version 2.1March 2014

<span id="TitlePage" class="anchor"></span>(Revised August 2025)

Product Development

######### Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 20%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2025</td>
<td>Title Page, <a href="#introduction">4</a>, <a href="#enhanced-order-checks-dosing-order-checks-and-pharmacogenomic-order-checks-process">8</a>, <a href="#display-sequence-for-order-checks">9</a>, <a href="#PGX_eligible">15</a>, <a href="#_Pharmacogenomic_Order_Check">83</a> <a href="#appendix-a-error-messages">195</a>, <a href="#Enhanced_Order">219</a>, <a href="#Pharamacogenomics">221</a></td>
<td>PSS*1*262</td>
<td><ul>
<li><p><u>Updated Section 1 Introduction for</u> <a href="#MOCHA_v_3_0">(MOCHA) v3.0 Enhancements</a></p></li>
<li><p><u>Updated Section 2</u> <a href="#enhanced-order-checks-dosing-order-checks-and-pharmacogenomic-order-checks-process">Enhanced Order Checks, Dosing Order Checks, and Pharmacogenomic Order Checks Process</a></p></li>
<li><p><u>Updated Section 2.2 Display Sequence for Order Checks to add</u> <a href="#PGX_High_Order">Pharmacogenomic High Order Checks</a> <u>and</u> <a href="#PGX_Medium_Order">Pharmacogenomic Medium Order Checks</a></p></li>
<li><p><u>Updated Section 2.5.2 Drug to add</u> <a href="#PGX_eligible">Pharmacogenomic Message Display</a></p></li>
<li><p><u>Added Section 2.8</u> <a href="#_Pharmacogenomic_Order_Check">Pharmacogenomic Order Check</a></p></li>
<li><p><u>Updated Appendix A –</u> <a href="#appendix-a-error-messages">Error Message</a></p></li>
<li><p><u>Added</u> <a href="#Gene">Gene</a><u>,</u> <a href="#Genotype">Genotype</a><u>,</u> <a href="#Pharamacogenomics">Pharmacogenomics</a><u>, and</u> <a href="#Phenotype">Phenotype</a> <u>to Glossary.</u></p></li>
<li><p><u>Updated Title Page with revision month/year, Revision History, Table of Contents</u></p></li>
</ul></td>
</tr>
<tr class="even">
<td>05/2025</td>
<td>2-4, 12, 15, 17-20, 24, 26, 27, 31, 33, 36, 39, 44, 46, 47, 49, 50, 54, 55, 58-63, 65, 67-70, 76-101, 105, 108, 112-116, 118-183, 187, 189, 192, 193, 198-210, 220, 221</td>
<td><p>PSS*1*254</p>
<p>PSJ*5*423</p>
<p>PSO*7*779</p></td>
<td><ul>
<li><p><u>Updated Title Page with revision month/year, Revision History, Table of Contents</u></p></li>
<li><p><u>Updated Section <strong>1</strong> <strong>Introduction</strong> for <strong>PSS*1*254</strong></u> <u>and <strong>PSJ*5*423</strong></u></p></li>
<li><p><u>Updated Section <strong>2.5.1</strong> <strong>Patient Parameters</strong> for ‘Body surface area required’ to ‘Body surface area is required’ and ‘Weight required’ to ‘Weight is required’ in VistA screenshots</u></p></li>
<li><p><u>Updated Section <strong>2.5.3</strong> <strong>Dosage Ordered</strong> for the <strong>FDB Dose Unit</strong></u></p></li>
<li><p><u>Updated Section <strong>2.5.3.2</strong> <strong>Local Possible Dosage for Single Ingredient Product</strong> for</u></p></li>
<li><p><u><strong>Example 2: Local Possible Dosage Selected for Single Ingredient Product</strong> and text describing Example 2Updated Section <strong>2.5.3.3</strong> <strong>Local Possible Dosage for Multi-Ingredient Product</strong> for</u></p></li>
<li><p><u><strong>Example 3: Local Possible Dosage Selected for Multi-Ingredient Product</strong> and text describing Example 3Updated Section <strong>2.5.3.4</strong> <strong>Local Possible Dosage with different Dose Units</strong> for <strong>Example 4: Local Possible Dosage(s) with Different Dose Units Defined for Same Drug</strong> and text describing Example 4</u></p></li>
<li><p><u>Updated Section <strong>2.5.5</strong> <strong>Dose Route (FDB)</strong> example for FDB Med Route to say ‘OPHTHALMIC (EYE)’ and the table for the STANDARD ROUTE and FDB DOSE ROUTE</u></p></li>
<li><p><u>Updated Section <strong>2.5.3.7</strong> <strong>IV Orders</strong> for</u></p></li>
<li><p><u><strong>Table 1: Examples of Single Dose Amount and Dose Unit derived from IV Additive</strong>Updated Section <strong>2.5.3.7.2</strong> <strong>IV Solution (PreMix) – Infusion Rate</strong> for the <strong>FDB Dose Unit</strong></u></p></li>
<li><p><u>Updated Section <strong>2.5.3.7.5</strong> <strong>Single Dose Adjustments</strong> for the VistA display screenshots</u></p></li>
<li><p><u>Updated Section <strong>2.5.7.1</strong> <strong>Fields Used to Determine Frequency</strong> for the</u> <u><strong>v4. updates</strong>, added <strong>Table of valid FREQUENCY (IN MINUTES)</strong></u>, <u><strong>Frequency Example 2: Every 5 Minutes for 3 Doses</strong> for ‘X#D’ to ‘#XD’ and <strong>Frequency Example 3: Schedule to Represent Two Different Frequency Values</strong> for ‘X#W’ to ‘#XW’</u></p></li>
<li><p><u>Updated Section <strong>2.6.1.2</strong> <strong>Dose Route</strong> for</u> <u>‘CONTINUOUS INFUSION’ to ‘CONTINUOUS IV INFUSION’</u></p></li>
<li><p><u>Updated Section <strong>2.6.1.3</strong> <strong>Low and High Dose/Max Daily Dose</strong> for updated display of the message</u></p></li>
<li><p><u>Updated Section <strong>2.6.1.4</strong> <strong>When is General Dosing Information Displayed?</strong> for display of the messages</u></p></li>
<li><p><u>Updated Section <strong>2.7</strong> <strong>Frequency Message</strong> for FDB generated frequency messages and removed the customization and updated</u></p></li>
<li></li>
<li><p><u><strong>Frequency Diagram 6: High Dose Warnings and Frequency Message</strong>, <strong>Frequency Diagram 7: Frequency Message with Error Message and GDI Message</strong>, <strong>Frequency Diagram 8: Frequency Message Only</strong>, and added</u> <u><strong>Frequency Diagram 9: Frequency Screening Not Performed with description</strong>Updated Section <strong>3.1.1 New Simple Medication Order</strong> for the message display in the <strong>Entering a new simple outpatient medication order screenshot</strong>Updated Section <strong>3.1.2</strong> <strong>New Complex Medication Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Entering a new complex Outpatient Medication order screenshotUpdated Section 3.1.3 Finishing a Pending Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Finishing a Pending Order screenshot</strong>Updated Section <strong>3.1.4</strong> <strong>Editing an Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Editing an Order</strong> screenshotUpdated Section <strong>3.1.5</strong> <strong>Renewing an Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Renewing an Order</strong> screenshotUpdated Section <strong>3.1.6</strong> <strong>Copying an Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Copying an Order</strong> screenshotUpdated Section <strong>3.1.8.1</strong> <strong>DC Action on Discontinued Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>DC Action on Discontinued Order</strong> screenshotUpdated Section <strong>3.1.8.2</strong> <strong>Discontinue Prescription(s) Option</strong> for the message display in the</u></p></li>
<li><p><u><strong>Discontinue Prescription(s) Option</strong> screenshotUpdated Section <strong>3.1.9</strong> <strong>Technician Entered Order</strong> for the message display in <strong>the</strong></u></p></li>
<li><p><u><strong>Technician Entered Order</strong> screenshotUpdated Section <strong>3.1.10.1</strong> <strong>Patient Prescription Processing</strong> for the message display in the</u></p></li>
<li><p><u><strong>Verifying order using Patient Prescription Processing option</strong> screenshotUpdated Section <strong>3.1.10.2</strong> <strong>Process Order Checks</strong> for the message display in the</u></p></li>
<li><p><u><strong>Verifying order using Process Order Checks option</strong> screenshotUpdated Section <strong>3.1.10.4</strong> <strong>Rx Verification by Clerk</strong> for the message display in the</u></p></li>
<li><p><u><strong>Verifying order using Rx Verification by Clerk option</strong> screenshotUpdated Section <strong>3.1.11.1</strong> <strong>High Single Dose and Schedule Excluded from Daily Dose Check</strong> for the message display in <strong>the</strong></u></p></li>
<li><p><u><strong>High Single Dose and Schedule Excluded from Daily Dose Check</strong> screenshotUpdated Section <strong>3.1.11.2</strong> <strong>Maximum Single Dose Order Check could not be Performed and Schedule Excluded from Daily Dose Order Check</strong> for the message display in the</u></p></li>
<li><p><u><strong>Maximum Single Dose Order Check could not be performed and Schedule Excluded from Daily Dose Order Check</strong> screenshotUpdated Section <strong>3.1.12.1</strong> <strong>High Dose Warnings</strong> for the message display in the</u></p></li>
<li><p><u><strong>High Dose Warnings</strong> screenshotUpdated Section <strong>3.1.12.2</strong> <strong>General Dosing Information Message</strong> for the message display in the</u></p></li>
<li><p><u><strong>General Dosing Information Message</strong> screenshotUpdated Section <strong>3.1.12.3</strong> <strong>Complex Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Complex Order</strong> screenshotUpdated Section <strong>3.1.13.1</strong> <strong>VistA Successfully Performs Max Daily Dose Order Check</strong> for the message display in the</u></p></li>
<li><p><u><strong>VistA successfully performs Max Daily Dose Order Check</strong> screenshotUpdated Section <strong>3.1.13.2</strong> <strong>VistA Cannot Perform Max Daily Dose Order Check – Not Correctable</strong> for the message display in the</u></p></li>
<li><p><u><strong>VistA cannot perform Max Daily Dose Order Check – Not Correctable</strong> screenshotUpdated Section <strong>3.1.13.3</strong> <strong>VistA Cannot Perform Max Daily Dose Order Check – Correctable</strong> for the message display in the <strong>Example 1: VistA cannot perform Max Daily Dose Order Check - Correctable</strong> and</u></p></li>
<li><p><u><strong>Example 2: VistA cannot perform Max Daily Dose Order Check - Corrected</strong> screenshotsUpdated Section <strong>3.2.1.1</strong> <strong>New Unit Dose Order</strong> for the message display in the <strong>New Unit Dose Order via backdoor pharmacy</strong> screenshot</u></p></li>
<li><p><u>Updated Section <strong>3.2.1.2</strong> <strong>New Unit Dose Order Using an Order Set</strong> for the message display in the</u></p></li>
</ul>
<ul>
<li><p><u><strong>New Unit Dose Order via pharmacy backdoor options using Order Set</strong> screenshotUpdated Section <strong>3.2.1.3</strong> Finishing a Complex Inpatient Medication Order for the message display in the</u></p></li>
</ul>
<ul>
<li><p><u><strong>Finishing Pending Complex Inpatient Medication order</strong> screenshotUpdated Section <strong>3.2.1.4</strong> <strong>Renewing an Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Renewing Unit Dose Order</strong> screenshotUpdated Section <strong>3.2.1.5</strong> <strong>Edit of an Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Editing Dosage Ordered –Creating New Unit Dose order</strong> screenshotUpdated Section <strong>3.2.1.6</strong> <strong>Copy a Unit Dose Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Copy a Unit Dose Order</strong> screenshotUpdated Section <strong>3.2.1.7</strong> <strong>Renew a Unit Dose Order - Free Text Dosage Error</strong> for the message display in the</u></p></li>
<li><p><u><strong>Renew a Unit Dose Order - Free Text Dosage Error</strong> screenshotUpdated Section <strong>3.2.1.8</strong> <strong>Verifying a non-verified Unit Dose Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Verifying a non-verified Unit Dose Order</strong> screenshotUpdated Section <strong>3.2.1.9</strong> <strong>Editing and then Verifying a Non-Verified Unit Dose Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Non-verified Unit Dose Order Edited and then Verified through pharmacy backdoor options</strong> screenshotUpdated Section <strong>3.2.1.10.1</strong> <strong>High Single Dose and Schedule Excluded from Daily Dose Order Check</strong> for the message display in the</u></p></li>
<li><p><u><strong>High Single Dose and Schedule Excluded from Daily Dose Order Check</strong> screenshotUpdated Section <strong>3.2.1.10.2</strong> <strong>Maximum Single Dose Order Check could not be Performed and Schedule Excluded from Daily Dose Order Check</strong> for the message display in the</u></p></li>
<li><p><u><strong>Maximum Single Dose Order check could not be performed and Schedule Excluded from Daily Dose Order Check</strong> screenshotUpdated Section <strong>3.2.1.11.1</strong> <strong>High Dose Warnings</strong> for the message display in the</u></p></li>
<li><p><u><strong>High Dose Warnings</strong> screenshotUpdated Section <strong>3.2.1.11.2</strong> <strong>General Dosing Information Message</strong> for the message display in the</u></p></li>
<li><p><u><strong>General Dosing Information Message</strong> screenshotUpdated Section <strong>3.2.1.12.1</strong> <strong>VistA Successfully Performs Max Daily Dose Order Check</strong> for the message display in the</u></p></li>
<li><p><u><strong>VistA Successfully Performs Max Daily Dose Order Check</strong> screenshotUpdated Section <strong>3.2.1.12.2</strong> <strong>VistA Cannot Perform Max Daily Dose Order Check – Not Correctable</strong> for the message display in the</u></p></li>
<li><p><u><strong>VistA Cannot Perform Max Daily Dose Order Check – Not Correctable and Example 2: VistA Cannot Perform Max Daily Dose Order Check – Corrected</strong> screenshotsUpdated Section <strong>3.2.1.12.3</strong> <strong>VistA Cannot Perform Max Daily Dose Order Check – Correctable</strong> for the message display in the <strong>Example 1: VistA Cannot Perform Max Daily Dose Order Check – Correctable</strong> and</u></p></li>
<li><p><u><strong>Example 2: VistA Cannot Perform Max Daily Dose Order Check – Corrected</strong> screenshotsUpdated Section <strong>3.2.2.1</strong> <strong>New IV Order</strong> for the message display in the</u></p></li>
</ul>
<blockquote>
<p><u><strong>New Order Entry through pharmacy backdoor options</strong> screenshotUpdated Section <strong>3.2.2.2</strong> <strong>Finishing an IV Order</strong> for the message display in the <strong>Finishing IV order with multiple prospective drugs</strong> screenshot</u></p>
</blockquote>
<ul>
<li><p><u>Updated Section <strong>3.2.2.3</strong> <strong>Editing an Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Editing infusion rate for an IV Solution marked as PreMix</strong> screenshotUpdated Section <strong>3.2.2.4</strong> <strong>Renewing of an Order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Renewing IV Order with a free text infusion rate</strong> screenshotUpdated Section <strong>3.2.2.5</strong> <strong>Copy an IV Order</strong> for the message display in the <strong>Copy an IV Order</strong> screenshot</u></p></li>
<li><p><u>Updated Section <strong>3.2.2.6</strong> <strong>Adjusting Single Dose Amount</strong> for the message display in the <strong>Adjusted Single Dose Amount for IV Order</strong> screenshot</u></p></li>
<li><p><u>Updated Section <strong>3.2.2.7</strong> <strong>Verifying a non-verified IV order for</strong> the message display in the</u></p></li>
<li><p><u><strong>Verifying a non-verified IV order</strong> screenshotUpdated Section <strong>3.2.2.8</strong> <strong>Editing and then Verifying a non-verified IV order</strong> for the message display in the</u></p></li>
<li><p><u><strong>Editing and then Verifying a non-verified IV order</strong> screenshotUpdated <strong>Example 2: Local Possible Dosage Selected for Single Ingredient Product</strong> and text describing Example 2</u></p></li>
<li><p><u>Updated <strong>Example 3: Local Possible Dosage Selected for Multi-Ingredient Product</strong> and text describing Example 3</u></p></li>
<li><p><u>Updated <strong>Example 4: Local Possible Dosage(s) with Different Dose Units Defined for Same Drug</strong> and text describing Example 4</u></p></li>
<li><p><u>Updated <strong>Example 6: Free Text Dosage for Logic 1 Check 1</strong> and text describing Example 6</u></p></li>
<li><p><u>Updated <strong>Example 7: Free Text Dosage for Logic 1 Check 2</strong> and text describing Example 7</u></p></li>
<li><p><u>Updated <strong>Example 8: Free Text Dosage fails Logic 1 Check 2</strong> and text describing Example 8</u></p></li>
<li><p><u>Updated <strong>Example 9: Free Text Dosage for Logic 2 Check 1</strong> and text describing Example 9</u></p></li>
<li><p><u>Updated <strong>Example 10: Free Text Dosage for Logic 2 Check 2</strong> and text describing Example 10</u></p></li>
<li><p><u>Updated <strong>Example 11: Free Text Dosage for Logic 2 Check 4</strong> and text describing Example 11</u></p></li>
<li><p><u>Updated <strong>Example 12: Free Text Dosage for Logic 1 and Logic 2 Combination</strong> and text describing Example 12</u></p></li>
<li><p><u>Updated <strong>Example 15: Free Text Dosage Range with two Dose Units</strong> and text describing Example 15</u></p></li>
<li><p><u>Updated <strong>Example 17: Evaluate Free Text Portion preceding Informational Data in Parenthesis (Step 2 in Diagram 11)</strong> and text describing Example 17</u></p></li>
<li><p><u>Updated <strong>Example 19: Free Text Dosage - Dose Units Match Active Ingredient Dose Units for Multi-Ingredient Product</strong> and text describing Example 19</u></p></li>
<li><p><u>Updated</u></p></li>
<li><p><u><strong>IV Diagram 2: Step 2 – Query Made To FDB Database</strong>Updated</u></p></li>
<li><p><u><strong>IV Diagram 3: Comparison Between Query Results and IV Order Route</strong>Updated</u></p></li>
<li><p><u><strong>IV Diagram 4: Continuous IV Order with One IV Additive and One IV Solution (not a PreMix)</strong>Updated Section <strong>4.2</strong> <strong>Drug Level Errors</strong> for FDB v4.5</u></p></li>
<li><p><u>Updated Section <strong>4.3</strong> <strong>Order Level Errors</strong> for FDB v4.5</u></p></li>
<li><p><u>Updated Section <strong>5</strong> <strong>Appendix A – Error Messages</strong> for FDB v4.5</u></p></li>
<li><p><u>Updated Section <strong>6</strong> <strong>Appendix B – Standard Medication Routes</strong></u></p></li>
<li><p><u>Updated Section <strong>7</strong> <strong>Appendix C – DOSE UNITS File with FDB Mapping</strong></u></p></li>
<li><p><u>Updated Section <strong>8</strong> <strong>Appendix D – Dose Unit Conversion File (#51.25)</strong></u></p></li>
<li><p><u>Updated Index page</u></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>09/2018</td>
<td><a href="#TitlePage">Title Page</a> <u><br />
<br />
</u><a href="#Page_128">128</a><u>,</u> <a href="#Page_130">130-148</a><u>,</u> <a href="#Page_149">149-150</a><u>,</u> <a href="#Page_149">152-154</a><u>,</u> <a href="#Page_157">157-162</a><u>,</u> <a href="#Page_164">164-174</a><u>, and</u> <a href="#Page_177">177-184</a></td>
<td>PSJ*5*373</td>
<td>Updated Title Page with revision month/year<br />
<br />
Corrected date so year is displayed with four digits for Start and Stop Dates.</td>
</tr>
<tr class="even">
<td>06/2018</td>
<td><a href="#Appendix_C">Appendix C</a></td>
<td>PSS*1*224</td>
<td>PUMP(S) entry added to DOSE UNIT File (#51.24)</td>
</tr>
<tr class="odd">
<td>02/2018</td>
<td><p>Title Page</p>
<p>vii-ix</p>
<p>2</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8-9</p>
<p>9</p>
<p>9-13, 20-21, 23-26, 28-39, 51-53, 59-63, 72</p>
<p>63-72</p>
<p>72-76</p>
<p>77-113</p>
<p>126-152</p>
<p>162-184</p>
<p>114-115</p>
<p>115-120</p>
<p>120-125</p>
<p>152-155</p>
<p>155-159</p>
<p>159-162</p>
<p>186-192</p>
<p>193-196</p>
<p>198-199</p>
<p>200-204</p>
<p>205-208</p>
<p>209-211</p>
<p>214-15</p></td>
<td><p>MOCHA v2.1b: PSJ*5*256, PSO*7*402, PSS*1*178</p>
<p>PSS*1*206, PSJ*5*347, and PSO*7*500</p></td>
<td><p>Updated revision month/year</p>
<p>Updated Table of Contents</p>
<p>Introduction section – new functionality listed</p>
<p>Updated text for Basic Flow of Order Check Diagram</p>
<p>Updated text for Section 2.1 – Dosing Order Check Exclusion</p>
<p>Updated text and table for Section 2.2 – Display Sequence for Order Checks</p>
<p>Updated Section 2.3 – text and table for Order Check Triggers</p>
<p>Updated text for Section 2.4 – FDB Dosing Record Information</p>
<p>Updated text for Section 2.5 – Data Requirements for Dosing Order Checks for Max Daily Dose Order Check</p>
<p>Added Frequency Section updated Section 2.5.7</p>
<p>Added Sections: 2.6 Custom Messages; 2.6.1 General Dosing Information Message; 2.6.2 Max Daily Dose Order Check Not Done – Frequency Failure and 2.6.3 Customized Frequency Message</p>
<p>Updated Order Entry Section (outputs and text) for new Max Daily Dose Order Check; BSA and CrCl header displays; Available Dosage List displays for OP; and Schedule displays for OP.</p>
<p>Outpatient</p>
<p>Inpatient Medications – Unit Dose</p>
<p>Inpatient Medications – IV</p>
<p>Added OP order entry sections:</p>
<p>Section 3.1.11 – Schedule Exclusions</p>
<p>Section 3.1.12 – Per Orifice Note</p>
<p>Section 3.1.13 – Max Daily Dose Order Check – Frequency Failure</p>
<p>Added IPM (Unit Dose) order entry sections:</p>
<p>Section 3.2.1.10 – Schedule Exclusions</p>
<p>Section 3.2.1.11 – Per Orifice Note</p>
<p>Section 3.2.1.12 – Max Daily Dose Order Check – Frequency Failure</p>
<p>Updated Section 4 – Error Handling</p>
<p>Updated Appendix A – Error Message content</p>
<p>Updated Appendix B – date and content</p>
<p>Updated Appendix C – date and content</p>
<p>Updated Appendix D – data and content</p>
<p>Added Appendix E, F, G – Frequency diagrams for Inpatient Medications and Outpatient Pharmacy order schedules</p>
<p>Updated Glossary content</p></td>
</tr>
<tr class="even">
<td>05/2017</td>
<td><a href="#v">v</a>, <a href="#v">vi</a>, <a href="#introduction">1</a>, <a href="#Page_2">2</a>, <a href="#Page_4">4</a>, <a href="#Page_8">8</a>, <a href="#local-possible-dosage-for-single-ingredient-product">14</a>, <a href="#Page_25">25</a>, <a href="#free-text-dosage-dispense-drug-assigned-to-order">27</a>, <a href="#free-text-dosage-dispense-drug-assigned-to-order">28</a>, <a href="#Page_34">34</a>, <a href="#free-text-dosage-logic-1-and-logic-2-combination">35</a>, <a href="#Page_36">36</a>, <a href="#free-text-dosage-range-enhancements">39</a>, <a href="#Page_40">40</a>, <a href="#Page_41">41</a>, <a href="#Page_43">43</a>, <a href="#Page_44">44</a>, <a href="#Page_45">45</a>, <a href="#Page_46">46</a>, <a href="#Page_47">47</a>, <a href="#Page_48">48</a>, <a href="#iv-additive-strength-and-drug-unit">49</a>, <a href="#Page_66">66</a>, <a href="#Page_68">68</a>, <a href="#Page_72">72</a>, <a href="#Page_75">75</a>, <a href="#reinstate-an-order">78</a>, <a href="#Page_79">79</a>, <a href="#Page_80">80</a>, <a href="#Page_81">81</a>, <a href="#Page_83">83</a>, <a href="#Page_84">84</a>, <a href="#Page_89">89</a>, <a href="#Page_91">91</a>, <a href="#Page_94">94</a>, <a href="#Page_98">98</a>, <a href="#Page_101">101</a>, <a href="#Page_103">103</a>, <a href="#Page_103">104</a>, <a href="#Page_103">106</a>, <a href="#Page_109"><span>108</span></a>, <a href="#Page_109">109</a>, <a href="#Page_112">112</a>, <a href="#high-single-dose-and-schedule-excluded-from-daily-dose-check">115</a>, <a href="#Page_117">117</a>, <a href="#Page_118">118</a>, <a href="#Page_120">120</a>, <a href="#Page_123">123</a>, <a href="#Page_125">125</a>, <a href="#Page_127">127</a>, <a href="#Page_128">128</a>, <a href="#Page_129">129</a>, <a href="#Page_131">131</a>,<a href="#Page_135">135</a> , <a href="#Page_137">137</a>, <a href="#Page_139">139</a>, <a href="#Page_141">141</a>, <a href="#Page_142">142</a>, <a href="#error-handling">143</a>, <a href="#Page_145">145</a>, <a href="#Page_146">146</a>, <a href="#max-daily-dose-order-check-frequency-failure-1">159</a>, <a href="#appendix-d-dose-unit-conversion-file-51.25">161</a>, <a href="#Page_163">163</a>, <a href="#Page_166">166</a>, <a href="#Page_167">167</a>, <a href="#Page_168">168</a>, <a href="#Page_169">169</a>, <a href="#Page_173">172</a></td>
<td>PSS*1*201</td>
<td><p>Updated Table of Contents</p>
<p>Introduction section – new functionality listed</p>
<p>Added Release Notes for patch PSS*1*201 to Related Manual section</p>
<p>Added CROCs to Display Sequence for Order Checks</p>
<p>Fixed Dosage Ordered table format</p>
<p>Updated text describing Diagram 2</p>
<p>Diagram 3 updated</p>
<p>Updated text describing Diagram 3</p>
<p>Example 11 and accompanying text deleted</p>
<p>Updated text describing Diagram 7</p>
<p>Reference Example 12 changed to Example 11</p>
<p>Updated text describing Diagram 8</p>
<p>Reference Example 13 changed to Example 12</p>
<p>Diagram 10 updated</p>
<p>Updated text describing Diagram 10</p>
<p>Reference Example 14 changed to Example 13</p>
<p>Added section 2.5.3.6.6 (Free Text Dosage Range Enhancements), Examples 14 and 15</p>
<p>Added section 2.5.3.6.7 (Informational Data in Parenthesis as part of Dosage Ordered), Diagram 11, Examples 16a-16c</p>
<p>Added section 2.5.3.6.8 (Free Text Logic for Multi Ingredient where dose unit derived from Free Text Dosage matches active ingredient dose unit), Example 17</p>
<p>Section 3 – Order Entry Display updates</p>
<p>Appendix B – Updated date</p>
<p>Appendix C – Updated date and contents</p>
<p>Appendix D – Added contents of Dose Unit Conversion File (#51.25)</p>
<p>Glossary – Added Dose Unit Conversion File definition</p>
<p>Update Revision History</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/2014</td>
<td>All Pages</td>
<td>MOCHA 2.0: PSJ*5*252, PSJ*5*257, PSO*7*372, PSO*7*416, PSS*1*160, PSS*1*173</td>
<td><p>New document</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

Preface

This user manual describes the functional characteristics of Dosing Order Checks. It is intended for pharmacists and technicians who are familiar with the functioning of Outpatient Pharmacy, Inpatient Medications, Pharmacy Data Management (PDM), and Computerized Patient Record System (CPRS) in a Veterans Affairs Medical Center (VAMC).

<span id="v" class="anchor"></span>Table of Contents

Examples

Diagrams

IV Examples

IV Diagrams

Frequency Diagrams

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Documentation Collections](#documentation-collections)
  - [Getting Help](#getting-help)
  - [Related Manuals](#related-manuals)
- [Enhanced Order Checks, Dosing Order Checks, and Pharmacogenomic Order Checks Process](#enhanced-order-checks-dosing-order-checks-and-pharmacogenomic-order-checks-process)
  - [Dosing Order Checks Exclusions](#dosing-order-checks-exclusions)
  - [Display Sequence for Order Checks](#display-sequence-for-order-checks)
  - [Order Check Triggers](#order-check-triggers)
  - [FDB Dosing Record Information](#fdb-dosing-record-information)
  - [Data Required for Dosing Order Checks](#data-required-for-dosing-order-checks)
    - [Patient Parameters](#patient-parameters)
    - [Drug](#drug)
    - [Dosage Ordered](#dosage-ordered)
    - [Dose Rate Unit](#dose-rate-unit)
    - [Dose Route (FDB)](#dose-route-fdb)
    - [Dose Type](#dose-type)
    - [Frequency](#frequency)
    - [Duration](#duration)
    - [Duration Rate Unit](#duration-rate-unit)
  - [Custom Messages](#custom-messages)
    - [General Dosing Information Message](#general-dosing-information-message)
  - [Frequency Message](#frequency-message)
  - [Pharmacogenomic Order Check](#pharmacogenomic-order-check)
- [Order Entry](#order-entry)
  - [Outpatient Pharmacy](#outpatient-pharmacy)
    - [New Simple Medication Order](#new-simple-medication-order)
    - [New Complex Medication Order](#new-complex-medication-order)
    - [Finishing a Pending Order](#finishing-a-pending-order)
    - [Editing an Order](#editing-an-order)
    - [Renewing an Order](#renewing-an-order)
    - [Copying an Order](#copying-an-order)
    - [Discontinuing an Active Order](#discontinuing-an-active-order)
    - [Reinstate an Order](#reinstate-an-order)
    - [Technician Entered Order](#technician-entered-order)
    - [Verification of an Order](#verification-of-an-order)
    - [Schedule Exclusions](#schedule-exclusions)
    - [Per Orifice Note](#per-orifice-note)
    - [Max Daily Dose Order Check – Frequency Failure](#max-daily-dose-order-check-frequency-failure)
  - [Inpatient Medications](#inpatient-medications)
    - [Unit Dose Module](#unit-dose-module)
    - [IV Module](#iv-module)
- [# Error Handling](#error-handling)
  - [System Level Errors](#system-level-errors)
  - [Drug Level Errors](#drug-level-errors)
  - [Order Level Errors](#order-level-errors)
    - [Warning Messages](#warning-messages)
- [Appendix A – Error Messages](#appendix-a-error-messages)
- [Appendix B – Standard Medication Routes](#appendix-b-standard-medication-routes)
- [Appendix C – DOSE UNITS File with FDB Mapping](#appendix-c-dose-units-file-with-fdb-mapping)
- [Appendix D – Dose Unit Conversion File (#51.25)](#appendix-d-dose-unit-conversion-file-5125)
- [Appendix E – Inpatient Order Frequency Logic](#appendix-e-inpatient-order-frequency-logic)
- [Appendix F – Outpatient Order Frequency Logic for One-Time, On Call, and DOW Schedules](#appendix-f-outpatient-order-frequency-logic-for-one-time-on-call-and-dow-schedules)
- [Appendix G – Outpatient Order Frequency Logic for Continuous and PRN Schedules](#appendix-g-outpatient-order-frequency-logic-for-continuous-and-prn-schedules)
- [Glossary](#glossary)
- [Index](#index)
Medication Order Check Healthcare Application (MOCHA) v2.0 implemented the first increment of Dosing Order Checks and introduced the Maximum Single Dose Order check for simple and complex orders for Outpatient Pharmacy, Inpatient Medications applications, and Computerized Patient Record System (CPRS). MOCHA v2.0 uses the same interface to First Databank (FDB) as MOCHA v1.0.
- Provides error messages with reasons at the order level when a Maximum Single Dose Order Check cannot be performed for pharmacy users
- Provides a generic error message at the order level when a Maximum Single Dose Order Check cannot be performed for CPRS users
- Adds a check during installation to see if Pre-Release setup work – mapping of Local Medication Routes and population of Numeric Dose and Dose Unit fields for Local Possible Dosages has been completed
- Adds new fields to the ADMINISTRATION SCHEDULE file (#51.1) to support the ability to exclude a schedule from all Dosing Order Checks or just from a Daily Dose Order Check
- Modifies the *Standard Schedule Edit* \[PSS SCHEDULE EDIT\] option to allow editing of the new dosing exclusion fields
- Modifies the *Administration Schedule File Report* \[PSS SCHEDULE REPORT\] option to display data entered in the new dosing exclusion fields
- Applies the ‘all Dosage Checks exclusion’ for a schedule when processing outpatient and inpatient medication orders
- Creates a new Pharmacy Data Management (PDM) option called *Lookup Dosing Check Info for Drug* \[PSS DRUG DOSING LOOKUP\] so a user can view all data that can affect Dosing Order Checks for a drug
- Adds new entries to the VistA DOSE UNITS file (#51.24)
- Creates and auto enables new DOSING_INFO web service
- Provides option to enable/disable Dosing Order Checks called *Enable/Disable Dosing Order Checks* \[PSS DOSING ORDER CHECKS\]
- Provides notification via email when Dosing Order Checks enabled/disabled
- Provides audit trail for enabling/disabling of Dosing Order Checks
- Provides option to identify drug names with trailing spaces called *Drug Names with Trailing Spaces* \[PSS TRAILING SPACES REPORT\]
- Modifies *Check Vendor Database Link* \[PSS CHECK VENDOR DATABASE LINK\] option to show Domain Name Service name for the MOCHA server when displaying the connection status
- Provides a new field in the CLINIC DEFINITION file (#53.46) to allow the entry of the number of days that discontinued/expired IMO orders will be included in Enhanced Order Checks (Drug Interactions and Therapeutic Duplications)
Patch PSS\*1\*201 (MOCHA v2.1a) provides the following functionality:
- Modify entries to the DOSE UNITS file (#51.24)
- Create a new file called DOSE UNIT CONVERSION (#51.25)
- Enhance free text dosage logic for dosing ranges and for multi-ingredient drugs
- Enhance free text logic to screen out information data placed in parenthesis which is found in the dosage ordered field for an order
<span id="Page_2" class="anchor"></span>Medication Order Check Healthcare Application (MOCHA) v2.1b implemented the Max Daily Dose (MDD) Order Check for simple orders for Outpatient Pharmacy, Inpatient Medications applications, and Computerized Patient Record System (CPRS). MOCHA v2.1b use the same interface to First Databank (FDB) as MOCHA v1.0 and v2.0.
MOCHA v2.1b will provide the following enhancements:
- Implement Dose Range Checking with a Max Daily Dose limit for simple medication orders entered through Outpatient Pharmacy, Inpatient Medications applications and CPRS
- Display a generic error message when the Max Daily Dose Order Check cannot be performed in CPRS
- Display an error message when the Max Daily Dose Order Check cannot be performed in CPRS with a detailed reason when height and/or weight is required, but does not exist in the Vitals application for the patient
- Display an error message when the Max Daily Dose Order Check cannot be performed in Pharmacy with a detailed reason
- Correct identified daily dose errors due to frequency failure
- Resolve miscellaneous frequency issues with incorporation of new dosing check frequency fields
- Apply Daily Dose Check exclusion for schedule to medication orders entered through Outpatient Pharmacy, Inpatient Medications, and CPRS
- Apply advisory note to high dose warnings and General Dosing Guidelines for medication administered through eye, ear, or nose
- Create a customized frequency message
- Create a general dosing information message
- Create a Max Daily Dose Warning message for the calculated Daily Dose
- Add FDB data elements from Dosing Order Check call to VistA side of interface
- Display one warning if Maximum Single Dose and Max Daily Dose Order Check warning texts are identical
- Adjustment to the Daily Dose if a Single Dose Adjustment is made for an IV order when performing Dosing Order Checks.
- Modify entries to the DOSE UNITS file (#51.24)
- Modify entries to the DOSE UNIT CONVERSION file (#51.25)
- Update Check PEPS Services Setup \[PSS CHECK PEPS SERVICES SETUP\] option to perform the Max Daily Dose Order Check instead of the Daily Dose Range Order Check
FDB MedKnowledge Framework v4.5 project updated MOCHA Drug Interactions, Duplicate Therapy, and Dosing in their release. Patch PSS\*1\*254 provided the following enhancements:
- Modifies hardcoded OTIC and OPTHALMIC routes to OTIC (EAR) and OPHTHALMIC (EYE)
- Modifies Check Vendor Database Link to display properly for the Database Version and Build Version fields
- Modifies Check PEPS Services Setup option for a Drug-Drug Interaction check to display significant interaction for drug that previously had a critical interaction
- Modify and add entries to the DOSE UNITS file (#51.24)
- Modify entries to the DOSE UNIT CONVERSION file (#51.25)
- Modify and add entries to the STANDARD MEDICATION ROUTES file (#51.23)
- Modifies Option PSS DRUG DOSING LOOKUP option intlDoseRouteDescription updated to DoseRouteDescription and updated the FDB Dose Units format from X per Y per Z to X/Y/Z format
- Enabled Message Suppression for messages which provide no additional information
- Update server and port for MOCHA and PPS-N webservices
- Update messaging “Weight required.” to “Weight is required.”
- Update messaging “Body surface area required.” to “Body surface area is required.”
- Display the top level text from the MOCHA return message if nothing exists in the Single Dose Message and the Max Daily Dose Message
- Continuous route requests updated to send the appropriate duration rate
- Modifies formatting of the Dosing Check Frequency field in File \#51 and File \#51.1.
- Modifies DOSE UNITS file (#51.24) for the NAME (#.01), SYNONYM (#01), and FIRST DATABANK DOSE UNIT (#1) fields. Field lengths were increased from 30 to 40 to support MICROGRAM DIETARY FOLATE EQUIVALENT.
- An update has been made for IV routes that results in a dose rate in the order checks of units/hour. This was done to match 3.3 functionality
- Modifies PEPS Services Setup option for a Dosing Order Check. FDB v3.3 frequency ‘Q4H’ was hardcoded to ‘Q4H’. FDB v4.5 the value is set to be ‘6’
- Display Age Exclusion and Contraindicated dosing messages in CPRS
- Modifies the message to say "Dosing Checks could not be performed for Drug:" in cases where there is no detail message text back from MOCHA
- Orders with a bad route will display a more meaningful message
- FDB v3.3 returned custom frequency messages created in VistA. FDB v4.5 returns standard frequency messages
- Custom Frequency messages and General Dosing messages both print on PSO LM BACKDOOR ORDERS when FIRST DATABANK messages are returned during New Order entry
- Adjusted the logic for displaying the General Dosing message
- Added support for annual dosing frequency Q12L and Q52W for MEDICATION INSTRUCTION File (#51) field DOSING CHECK FREQUENCY (#32) and ADMINISTRATION SCHEDULE File (#51.1) field DOSING CHECK FREQUENCY (#11)
- In the DOSE UNITS File (#51.24), New Type Cross Reference FDBNAME was added for the NAME (#.01) field to support the longer field length.
- In the DOSE UNITS File (#51.24), New Type Cross Reference FDBUNIT was added for the FIRST DATABANK DOSE UNIT (#1) field to support the longer field length.
- In the DOSE UNITS File (#51.24), New Type Cross Reference FDBSYN was added to the SYNONYM (#.01) field of the SYNONYM subfile (#51.242) to support the longer field length.
- The length of the FIRST DATABANK MED ROUTE (#1) field in the STANDARD MEDICATION ROUTES file (#51.23) was increased from 30 to 40.
- Implemented new type cross reference FDBMRT for the FIRST DATABANK MED ROUTE field in the STANDARD MEDICATION ROUTES file (#51.23) to support the longer field length
- Implemented new type cross reference FDBMRT for the NAME field of the MEDICATION ROUTES file (#51.2) to support the longer entries in the STANDARD MEDICATION ROUTES file (#51.23).
Patch PSJ\*5\*423 provided the following enhancements:
- Suppress display of the Single Dose messaging for Continuous Routes. 
- Inpatient orders with Drug-Drug Interaction checks that returned only a significant interaction displayed two lines of ===. This has been updated to display only one === line. 
- FDB 4.5 returns routes in mixed case. FDB 3.3 returned them in all capital letters. 
- The following new values have been added to the continuous routes:
  - CONTINUOUS ADDUCTOR CANAL BLOCK
  - CONTINUOUS EPIDURAL
  - CONTINUOUS INFRACLAVICULAR
  - CONTINUOUS INHALATION
  - CONTINUOUS INTERSCALENE
  - CONTINUOUS INTRA-CATHETER INFUSION
  - CONTINUOUS INTRAPERITONEAL INFUSION
  - CONTINUOUS INTRA-UMBILICAL VEIN INFUSION
- The following continuous routes values are being updated:
  - CONTINUOUS INFUSION to CONTINUOUS IV INFUSION
  - CONT INTRAARTER INF to CONTINUOUS INTRA-ARTERIAL INFUSION
  - CONTINUOUS INFILTRAT to CONTINUOUS INFILTRATION
  - CONT CAUDAL INFUSION to CONTINUOUS CAUDAL INFUSION
  - CONT INTRAOSSEOUS to CONTINUOUS INTRAOSSEOUS INFUSION
  - CONT INTRATHECAL INF to CONTINUOUS INTRATHECAL INFUSION
  - CONT NEBULIZATION to CONTINUOUS NEBULIZATION
  - CONT SUBCUTAN INFUSI to CONTINUOUS SUBCUTANEOUS INFUSION
<span id="MOCHA_v_3_0" class="anchor"></span>Medication Order Check Healthcare Application (MOCHA) v3.0 implemented Pharmacogenomic Order Checks for Outpatient Pharmacy, Inpatient Medications applications, and Computerized Patient Record System (CPRS). MOCHA v3.0 uses the same interface to First Databank (FDB) as MOCHA v1.0, v2.0 and v2.1b.
MOCHA v3.0 provided the following enhancements:
- Implement PGx order checks, high and medium severity, for PGx eligible medication orders entered in Outpatient Pharmacy, Inpatient Medications, and CPRS applications.
- Make ‘Additional Information’ (like a monograph) available to CPRS and Pharmacy users for all high and medium severity PGx order checks. 
- Retrieve patient genomic lab data from the Health Data Repository (HDR) to be used for the PGx order checks. 
- Provide a ‘Screen’ message to CPRS/Pharmacy users that when appropriate will suggest that additional information or testing needs to be provided for the drug being entered to do a PGx order check. 
- Apply suppression rules to the PGx Order checks to ensure a PGx order check is displayed only when necessary. 
- Provide error/exception messages when a PGx order check cannot be performed for whatever reason. 
- Create a new Pharmacy option called ‘Check Pharmacogenomic Interaction’ \[PSS CHECK PGX INTERACTION\] that allows a user to enter drug(s), gene(s), phenotype(s), and genotype(s) and see the PGx Order checks returned from the vendor for the data entered. The option can also be run by patient, where the patient’s genomic lab results and PGx eligible drug(s) from his/her current profile are used to retrieve PGx order checks. 
- Require a CPRS override reason for PGx order checks with a high severity. 
- Require a Pharmacy intervention for PGx order checks with a high severity. 
- Store PGx order check information in the ORDER CHECK INSTANCES (#100.05) File for PGx order checks seen in CPRS. 
- Store PGx order check information in the CANCELLED ORDERS AND ORDER CHECKS (#100.3) File when a CPRS user exits during the entry of a new order without completing the order. 
- Restructure some of the Pharmacy Data Management menus to group like options together for a  more logical display. 
- Send an Email to a Pharmacy Benefits Management (PBM) mail group when genomic data is retrieved from the HDR for a PGx order check and the gene or phenotype cannot be resolved to an acceptable term that the vendor is expecting. PBM will investigate accordingly. 

## Documentation Collections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Dosing Order Checks User Manual includes documentation conventions, also known as notations, which are used consistently throughout this manual. Each convention is outlined below.

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Convention</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Menu option text is italicized.</td>
<td>There are eight options on the <em>Archiving</em> menu.</td>
</tr>
<tr class="even">
<td>Screen prompts are denoted with quotation marks around them.</td>
<td>The “Dosage:” prompt displays next.</td>
</tr>
<tr class="odd">
<td>Responses in bold face indicate user input.</td>
<td>Select Orders by number: (1-6): <strong>5</strong></td>
</tr>
<tr class="even">
<td><p><strong>&lt;Enter&gt;</strong> indicates that the Enter key (or Return key on some keyboards) must be pressed.</p>
<p><strong>&lt;Tab&gt;</strong> indicates that the Tab key must be pressed.</p></td>
<td><p>Type <strong>Y</strong> for Yes or <strong>N</strong> for No and press <strong>&lt;Enter&gt;</strong>.</p>
<p>Press <strong>&lt;Tab&gt;</strong> to move the cursor to the next field.</p></td>
</tr>
<tr class="odd">
<td>![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/002.png)Indicates especially important or helpful information.</td>
<td>![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/003.png)Up to four of the last LAB results can be displayed in the message.</td>
</tr>
<tr class="even">
<td>![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/004.png)Indicates that options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.</td>
<td>![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/005.png)This option requires the security key PSOLOCKCLOZ.</td>
</tr>
</tbody>
</table>

## Getting Help 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One, two or three question marks (?, ??, ???) can be entered at any of the prompts for online help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals are located on the VistA Documentation Library (VDL) at: <http://www.va.gov/vdl>.

Main Package Documentation:

- *Outpatient Pharmacy V. 7.0 Release Notes*
- *Outpatient Pharmacy V. 7.0 Manager’s User Manual*
- *Outpatient Pharmacy V. 7.0 Pharmacist’s User Manual*
- *Outpatient Pharmacy V. 7.0 Technician’s User Manual*
- *Outpatient Pharmacy V. 7.0 User Manual – Supplemental*
- *Outpatient Pharmacy V. 7.0 Technical Manual/Security Guide*
- *Dosing Order Check User Manual*
- <span id="Page_4" class="anchor"></span>*VistA to MOCHA Interface Document*
- *Inpatient Medications V. 5.0 Nurse’s User Manual*
- *Inpatient Medications V. 5.0 Pharmacist’s User Manual*
- *Inpatient Medications V. 5.0 Supervisor’s User Manual*
- *Inpatient Medications V. 5.0 Technical Manual/Security Guide*
- *Pharmacy Data Management V.1.0 User Manual*
- *Pharmacy Data Management V. 1.0 Technical Manual/Security Guide*
- *Pharmacy Data Management V. 1.0 Release Notes (PSS\*1\*201)*
- *MOCHA V. 2.0 Installation Guide*
- *MOCHA V. 2.0 Release Notes*
- *MOCHA V. 2.0 FAQ Document*
- *PREM\*4\*2 MOCHA Server Version Release Notes*
- *PREM\*4\*2 MOCHA Server Installation Guide*
- *PREM\*4\*2 MOCHA Server Deployment, Installation, Back-out, and Rollback Guide*
- *PREM\*4\*2 MOCHA Server Productions Operations Manua*Additional Documentation:

Additional documentation related to specific projects is also located on the VDL. For example, there may be several different Release Notes documents, which apply to specific projects. Also, there may be several sets of “Change Page” documents, which apply to changes made only for a specific package patch.

# Enhanced Order Checks, Dosing Order Checks, and Pharmacogenomic Order Checks Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/006.png)

This diagram depicts the basic flow of order check data for Drug Interactions and Duplicate Therapy Order Checks as introduced with MOCHA v1.0 with the Maximum Single Dose Order Check and the Max Daily Dose Order Check for simple orders.

When a VistA application, such as Outpatient Pharmacy or Inpatient Medications requests an order check, the data required to perform the check will be sent from VistA to FDB using the Health*<u>e</u>*Vet Web Services Client (HWSC) in the form of an extensible mark-up language (XML) message. The MOCHA services will receive and validate the format of the request. Provided the format is correct, the MOCHA services will triage the request, interacting with FDB’s MedKnowledge Framework (formerly Drug Information Framework) to perform the requested check, and return the results. For Pharmacogenomics, if the medication being ordered is PGx Eligible in the VA Product file, the PGx lab values are retrieved from HDR where they are stored at an enterprise level. They will then be part of the data that is sent from VistA to FDB to perform the order check.

The way Remote Data Interoperability (RDI) works has not changed. For Duplicate Therapy and Drug Interaction Order Checks, the remote information is bundled with local information for the patient as the order check request. With the implementation of MOCHA v1.0, another step was added in the process. Instead of the order checks (i.e., Drug Interactions, Duplicate Therapy) being performed all within VistA, now the order checks are performed by FDB’s MedKnowledge Framework. For PGx, suppression rules will use FDB data and the patient’s local medication profile to determine if the order check should be suppressed.

## Dosing Order Checks Exclusions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Dosing Order Checks will be performed on supply items. A supply item is identified by either a VA Drug Class code that begins with an ‘XA’ or contains an ‘S’ in the DEA, SPECIAL HDLG field in the DRUG file .

A dosage form is excluded from Dosing Order Checks if the EXCLUDE FROM DOSAGE CHECKS field in the DOSAGE FORM file is set to ‘Yes’. If the drug ordered is associated with a dosage form (i.e., cream, ointment) that is excluded from Dosing Order Checks and the value in the OVERRIDE DF DOSE CHK EXCLUSION field in the VA PRODUCT file is blank or set to ‘No’ for the VA Product the drug is matched to, no Dosing Order Checks will be performed. If the drug ordered is associated with a dosage form that is NOT excluded from Dosing Order Checks and the value in the OVERRIDE DF DOSE CHK EXCLUSION field in the VA PRODUCT file is set to ‘Yes’ for the VA Product that the drug is matched to, no Dosing Order Checks will be performed. An example of such a drug would be a Placebo Tab.

The table below shows all the different combinations of values for the EXCLUDE FROM DOSAGE CHECK field in the DOSAGE FORM file and the OVERRIDE DF DOSE CHK EXCLUSION field in the VA PRODUCT file and whether or not those combinations result in Dosing Order Checks being performed.

| Dosage Form Field – Exclude from Dosage Checks | VA Product Field – OVERRIDE DF DOSE CHK EXCLUSION | Dosing Order Checks Performed? (Y/N) |
|----------------------------------------------------|-------------------------------------------------------|------------------------------------------|
| Yes                                                | No                                                    | No                                       |
| Yes                                                | Yes                                                   | Yes                                      |
| No                                                 | No                                                    | Yes                                      |
| No                                                 | Yes                                                   | No                                       |

No Dosing Order Checks will be performed for a simple medication order contains a schedule that has been excluded from all Dosing Order Checks. No message will be displayed to the user informing them that no Dosing Order Checks will be performed.

No Maximum Single Dose Order Check will be performed for an individual dosing sequence within a complex order that contains a schedule which has been excluded from all Dosing Order Checks. No message will be displayed to the user informing them that a Maximum Single Dose Order Check will not be performed. Max Daily Dose Order Checks for complex orders will be implemented in a future version of MOCHA.

No Max Daily Dose Order Check will be performed for a simple medication order that contains a schedule which has been excluded from the Daily Dose Order Check. No message will be displayed to the user informing them that a Max Daily Dose Order Check will not be performed.

Non-VA medication orders are excluded from Dosing Order Checks. A majority of Non-VA medication orders will have incomplete dosing information. This dosing information is needed to perform Dosing Order Checks. Had non-VA medication orders been included in Dosing Order Checks, in most cases this would have resulted in an error message being displayed to the user stating that Dosing Order Checks could not be performed.

## Display Sequence for Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Order checks are displayed in the same sequence for both Outpatient Pharmacy and Inpatient Medications applications. There may be some order checks displayed in one application and not the other, but for those order checks shared between both applications, the order sequence is the same. The table below lists the order check and error display sequence for both applications.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Outpatient Pharmacy</strong></th>
<th><strong>Inpatient Medications</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>System Errors</td>
<td>System Errors</td>
</tr>
<tr class="even">
<td>Duplicate Drug</td>
<td></td>
</tr>
<tr class="odd">
<td>Clozapine</td>
<td></td>
</tr>
<tr class="even">
<td><p>Allergy/ADR (local and remote) or</p>
<p>Non-Assessment</p></td>
<td><p>Allergy/ADR (local and remote)</p>
<p>Non-Assessment</p></td>
</tr>
<tr class="odd">
<td>CPRS Order Checks (i.e., Aminoglycoside Ordered; Dangerous Meds for Patients&gt;64; Glucophage Lab Results)</td>
<td>CPRS Order Checks (i.e., Aminoglycoside Ordered; Dangerous Meds for Patients&gt;64; Glucophage Lab Results)</td>
</tr>
<tr class="even">
<td>Clinical Reminder Order Checks (CROCs)</td>
<td>Clinical Reminder Order Checks (CROCs)</td>
</tr>
<tr class="odd">
<td>Drug Level Errors</td>
<td>Drug Level Errors</td>
</tr>
<tr class="even">
<td>Local and Remote Critical Drug Interactions</td>
<td>Inpatient, Local and Remote Outpatient Critical Drug Interactions</td>
</tr>
<tr class="odd">
<td>Local and Remote Significant Drug Interactions</td>
<td>Inpatient, Local and Remote Outpatient Significant Drug Interactions</td>
</tr>
<tr class="even">
<td>Local and Remote Duplicate Therapy</td>
<td>Inpatient, Local and Remote Outpatient Duplicate Therapy</td>
</tr>
<tr class="odd">
<td><span id="PGX_High_Order" class="anchor"></span>Pharmacogenomic High Order Checks</td>
<td>Pharmacogenomic High Order Checks</td>
</tr>
<tr class="even">
<td><span id="PGX_Medium_Order" class="anchor"></span>Pharmacogenomic Medium Order Checks</td>
<td>Pharmacogenomic Medium Order Checks</td>
</tr>
<tr class="odd">
<td>Order Level Errors</td>
<td>Order Level Errors</td>
</tr>
<tr class="even">
<td>Dosing Order Checks</td>
<td>Dosing Order Checks</td>
</tr>
</tbody>
</table>

For Drug Interaction Order Checks, local outpatient orders include all active, non-verified, pending and Non-VA medication orders. Remote outpatient orders include all active orders. For Duplicate Therapy Order Checks, local outpatient orders include all active, expired (Exp Date + 120), discontinued (Cancel Date + Days Supply +7), non-verified, pending and Non-VA Medication orders. Remote outpatient orders include all active, expired (Exp Date +30) and discontinued (Cancel Date +30).

Inpatient medication orders include all active, non-verified, pending orders for both IV and Unit Dose modules.

Clinic Orders participate in both Drug Interaction Order Checks and Duplicate Therapy Order Checks for Inpatient and Outpatient medication orders.

## Order Check Triggers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the order entry actions that will trigger order checks to be performed through the pharmacy backdoor options for both Outpatient Pharmacy and Inpatient Medications - IV and Unit Dose modules.

| Order Action                                       | Outpatient                                                                                      | Inpatient                                                                                                   | Medications                                                                                                     |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|                                                        | Pharmacy                                                                                        | Unit Dose                                                                                                   | IV                                                                                                              |
| New Order                                              | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/007.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/008.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/009.png)                 |
| New Order using Order Sets                             |                                                                                                     | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/010.png)             |                                                                                                                     |
| Finish                                                 | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/011.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/012.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/013.png)                 |
| Renew                                                  | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/014.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/015.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/016.png)                 |
| Copy                                                   | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/017.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/018.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/019.png)                 |
| Reinstate DC                                           | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/020.png) |                                                                                                                 |                                                                                                                     |
| Verify                                                 | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/021.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/022.png)<sup>4</sup> | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/023.png)<sup>4</sup>     |
| Edit Orderable Item                                    | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/024.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/025.png)             |                                                                                                                     |
| Edit Dispense Drug                                     | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/026.png) |                                                                                                                 |                                                                                                                     |
| Edit Dispense Units Per Dose/Units Per Dose            | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/027.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/028.png)             |                                                                                                                     |
| Edit IV Additive field (Additive, Strength, or Bottle) |                                                                                                     |                                                                                                                 | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/029.png)                 |
| Edit IV Solution field (Solution or Volume)            |                                                                                                     |                                                                                                                 | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/030.png)<sup>3</sup> |
| Edit Dosage/Dosage Ordered                             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/031.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/032.png)             |                                                                                                                     |
| <span id="Page_8" class="anchor"></span>Edit Route     | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/033.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/034.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/035.png)<sup>5</sup>     |
| Edit Schedule                                          | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/036.png) | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/037.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/038.png)<sup>1, 5</sup>  |
| Edit Infusion Rate                                     |                                                                                                     |                                                                                                                 | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/039.png)<sup>2, 5</sup>  |
| Edit Provider                                          |                                                                                                     | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/040.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/041.png)<sup>5</sup>     |
| Edit Start Date/Time                                   |                                                                                                     | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/042.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/043.png)<sup>5</sup>     |
| Edit Stop Date/Time                                    |                                                                                                     | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/044.png)             | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/045.png)<sup>5</sup>     |
| Edit Conjunction (complex order)                       | ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/046.png) |                                                                                                                 |                                                                                                                     |

> <sup>1</sup> Intermittent type IV orders only

> <sup>2</sup> Continuous type IV orders only

> <sup>3</sup> If Volume is edited, IV Solution must not be marked as PreMix and not Intermittent type IV order

> <sup>4</sup> The VERIFY action must be the only action taken within the order session that triggers the Order Checks

> <sup>5</sup> Dosing Order Checks performed only

If a new order is created due to an order entry action taken, all order checks will be performed for the drug ordered. Dosing Order Checks will be performed and displayed last.

When editing the schedule for an IV order, only intermittent IV orders will generate Dosing Order Checks. The IV type must be a ‘Piggyback’, ‘Intermittent Syringe’, ‘Chemotherapy Piggyback’, or ‘Chemotherapy Intermittent Syringe’ for Dosing Order Checks to occur. Although the schedule does not affect the single dose amount, the business rule established is to execute both the Maximum Single Dose Order Check and the Max Daily Order Check when the schedule is edited.

When editing the infusion rate for an IV order, only continuous IV orders will generate Dosing Order Checks. The IV type must be an ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’ or ‘Chemotherapy Continuous Syringe’ for Dosing Order Checks to occur.

If the volume of an IV Solution is edited that is not marked as a PreMix within an IV order with an IV type of ‘Piggyback’, ‘Intermittent Syringe’, ‘Chemotherapy Piggyback’, or ‘Chemotherapy Intermittent Syringe’, no Dosing Order Checks will be performed. In all other cases, Dosing Order Checks will be executed.

The MOCHA 1 Enhancements 1 project (PSJ\*5.0\*260) made a change in the Inpatient Medications application to allow for the triggering of order checks to occur when the verification action was being taken on unit dose and IV orders. The only condition is that the verify action is the only action taken during the order session. For example, if auto verification was turned off and a user was finishing an order, order checks would only be displayed once during the finish action and not twice during finish and verification if both actions were taken during a single order session. If the same user within a separate order session, selected a non-verified order from the patient profile and then took the verify action without taken any other action on the order, order checks would be performed.

## FDB Dosing Record Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FDB Dosing Order Checks are unique by age, dose type (i.e., single dose, maintenance dose) and route. Dose types and routes will be discussed in more detail in the next section of this document. Gender does not come into play with Dosing Order Checks.

FDB has specific age group categories defined for their dosing records. The two categories that come into play for most of our medication orders are the ADULT and ELDERLY categories. The ADULT age category is defined as 18 years old up to but not including 65 years old. The ELDERLY age category is defined as 65 years old up to and including 110 years old.

Sometimes when Dosing Order Checks are performed, a message may be displayed that no dosing information is available for a specific drug. It could be the age of the patient is outside any of the age ranges defined for a drug’s dosing records. It may also be the combination of data sent in for the order check did not match a defined dosing record for that particular drug.

On other occasions you may see different maximum values in the warning message for different patients. Different values may be designated for different age ranges. For example, if you enter an order for a maintenance dose of 10mg for WARFARIN for a 70 year old patient, you will get a Maximum Single Dose warning. The limit for that age is 7.5mg. If you enter the same maintenance dose of 10mg for a 60 year old patient, you will not get an alert. The limit for the 60-year-old is 10mg.

The dose type may also come into play. A higher dose may be allowed for a one time (single dose). The maximum of 10mg can be given for a one time dose of WARFARIN for a 70-year-old, while a maximum of 15mg can be given for a one time dose for a 60 year old.

How frequently the drug is administered should also be considered. You may see that the maximum single dose amount is larger than the high dose displayed within a general dosage range and larger than the maximum daily dose for a drug. If the drug is administered less frequently, i.e., every 7 days versus once a day, the maximum single dose can be larger.

## Data Required for Dosing Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for Dosing Order Checks (Maximum Single Dose and Maximum Daily Dose) to be performed, the following information is required:

- Patient Parameters: (Age, Weight, and Body Surface Area \[BSA in m<sup>2</sup>\])
- Drug
- Single Dose Amount
- Dose Unit (FDB Equivalent)
- Dose Rate
- Dose Route (FDB Equivalent)
- Dose Type
- Frequency
- Duration
- Duration Rate

### Patient Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The three patient parameters that are required to perform Dosing Order Checks are:

- Age (in days)
- Weight (in Kg)
- Body Surface Area (BSA in m<sup>2</sup>)

The age of the patient is found in the PATIENT file. Should the age of the patient not be available, Dosing Order Checks will not be performed, and an error message will be displayed to the user as shown below.

Dosing Checks could not be performed for Drug: GABAPENTIN 600MG TAB

Reason(s): One or more required patient parameters unavailable: AGE

The Dubois formula is used to calculate the Body Surface Area (BSA). It is as follows:

BSA (m²) = 0.20247 x Height(m)<sup>0.725</sup> x Weight(kg)<sup>0.425</sup>

The most recent values for height and weight found in the GEN. MED. REC. – VITALS V. 5.0 application are used to calculate the BSA in m<sup>2</sup> for a patient. If a BSA or weight is required for a specific drug/age combination as determined by FDB in order to perform a Maximum Single Dose Order Check, Max Daily Dose Order Check, or both Dosing Order Checks, and no value is found, an error message as shown below will be displayed indicating which Dosing Order Check or both Dosing Order Checks could not be performed.

> Maximum Single Dose Check could not be performed for Drug: LOMUSTINE 100MG

> CAP

> Reason(s): Body surface area is required.

> Or

> Maximum Single Dose Check could not be performed for Drug: ENOXAPARIN

> 100MG/ML INJ

> Reason(s): Weight is required.

> Max Daily Dose Check could not be performed for Drug: METHOTREXATE 25MG/ML

> INJ

> Reason(s): Body surface area is required.

> Or

> Max Daily Dose Check could not be performed for Drug: DIPYRIDAMOLE

> 5MG/ML INJ

> Reason(s): Weight is required.

> Dosing Checks could not be performed for Drug: CARMUSTINE 100MG/VIAL INJ

> Reason(s): Body surface area is required.

> Or

> Dosing Checks could not be performed for Drug: ISONIAZID 100MG

> Reason(s): Weight is required.

### Drug

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to communicate with FDB, a VistA drug has to be mapped to an equivalent drug in the FDB database. The GCNSEQNO for the VA Product that the local dispense drug is matched to, is used to map a VistA drug to a drug in the FDB database. For IV orders, the dispense drug associated with the IV Additive or the IV Solution (marked as a PreMix) will be used to obtain the GCNSEQNO. If a dispense drug is not matched to NDF, a GCNSEQNO cannot be obtained and therefore Drug Interactions, Duplicate Therapy Dosing, or Pharmacogenomic Order Checks cannot be executed. In some instances, the drug may be matched to NDF, but the VA Product that it is matched to may not have a GCNSEQNO defined. These should be reported to the NDF National Manager for correction. Users can log a helpdesk ticket, or a mail message can be sent to the Outlook mail group <span class="mark">REDACTED</span>. If a local prospective or profile drug is not matched to NDF, the following error message will be displayed to the pharmacy user. The software, within this error message text, will distinguish an inpatient versus an outpatient medication order when processing inpatient medication orders. The inpatient order will have the text ‘Local Drug:’ displayed before the drug name, whereas the outpatient order will have the text ‘Local Outpatient Drug:’ displayed before the drug name.

> Not Matched to NDF

Enhanced Order Checks cannot be performed for Local Drug: EZOGABINE 200MG TAB

Reason(s): Drug not matched to NDF

> Or

> Not Matched to NDF

Enhanced Order Checks cannot be performed for Local Outpatient Drug: EZOGABINE 200MG TAB

Reason(s): Drug not matched to NDF

When an IV order is edited and only Dosing Order Checks are performed and the drug within the order is not matched to NDF, the message that the Pharmacy user will see is shown below.

> Not Matched to NDF for Dosing Order Checks when editing IV Order

Dosing Checks could not be performed for Drug: \<DRUG NAME\>

Reason(s): Drug not matched to NDF.

If the drug is matched to NDF, but the VA Product that it is matched to does not have a GCNSEQNO and the EXCLUDE DRG-DRG INTERACTION CK field for the VA Product is blank, the following error message will be displayed to the pharmacy user for a prospective drug.

No GCNSEQNO (prospective drug)

Order Checks could not be done for Drug: EZOGABINE 200MG TAB please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate Dosing.

The text referencing Dosing is removed for a profile drug.

No GCNSEQNO (profile drug)

Order Checks could not be done for Drug: EZOGABINE 200MG TAB please complete a manual check for Drug Interactions and Duplicate Therapy.

A remote order will have the text ‘Remote Drug:’ displayed before the drug name and will not have the text referencing Dosing.

> No GCNSEQNO (remote drug)

Order Checks could not be done for Remote Drug: EZOGABINE 200MG TAB please complete a manual check for Drug Interactions and Duplicate Therapy.

If the drug is <span id="PGX_eligible" class="anchor"></span>PGx eligible, Pharmacogenomic Order Checks will be added to the above messages. If the drug is not PGx eligible, no reference will be made to PGx.

If the EXCLUDE DRG-DRG INTERACTION CK field for the VA Product is set to ‘Yes’, no error message will be displayed. A generic message is displayed to the CPRS user when a drug is not matched to NDF or if no GCNSEQNO exists for the VA Product to which the drug is matched. The text referencing Dosing is removed for a profile drug. A remote order will have the text ‘Remote Drug:’ displayed before the drug name and will not have the text referencing Dosing.

No GCNSEQNO or drug not matched to NDF for a prospective drug

Order Checks could not be done for Drug: EZOGABINE 200MG TAB please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate Dosing.

No GCNSEQNO or drug not matched to NDF for a profile drug

Order Checks could not be done for Drug: EZOGABINE 200MG TAB please complete a manual check for Drug Interactions and Duplicate Therapy.

No GCNSEQNO or drug not matched to NDF for a remote profile drug

Order Checks could not be done for Remote Drug: EZOGABINE 200MG TAB please complete a manual check for Drug Interactions and Duplicate Therapy.

When an IV order is edited and only Dosing Order Checks are performed and a GCNSEQNO number cannot be obtained for the drug within the order, the message that the CPRS and Pharmacy user will see is shown below. The same message will be seen by CPRS users when the drug is not matched to NDF.

> No GCNSEQNO for Dosing Order Checks when editing IV Order

Dosing Checks could not be done for Drug: \<DRUG NAME\>, please complete a manual check for appropriate Dosing.

When Enhanced Order checks are performed against outpatient or unit dose profile drugs through pharmacy backdoor options, and a pending order is found on the profile for which an active dispense drug cannot be assigned, the pharmacy user will see the following error message.

Profile Pending Order without Active Dispense Drug (Pharmacy User)

Enhanced Order Checks cannot be performed for Orderable Item: \<OI NAME \>

Reason(s): No Dispense Drug found.

CPRS users will also see an error message, but a reason will not be displayed.

Profile Pending Order without Active Dispense Drug (CPRS User)

Order Checks could not be done for Drug: \<Drug Name\>, please complete a manual check for Drug Interactions and Duplicate Therapy.

If an order is entered through the IV Fluid dialog in CPRS for which an active IV Additive or IV Solution (marked as PreMix) cannot be found and Dosing Order Checks cannot be performed, the CPRS user will see the following message:

> Prospective drug – No Active IV Additive or IV Solution (marked as PreMix) Found

Dosing Checks could not be done for Drug: \<DRUG NAME\>, please complete a manual check for appropriate Dosing.

For this scenario, the IV Additive or IV Solution (marked as a PreMix) must be active when the order is entered. The inactivation must occur before the order is accepted to generate the error message.

### Dosage Ordered

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The dosage ordered provides the single dose amount and Dose Unit for most inpatient unit dose and outpatient medication orders. The single dose amount is the numeric representation of the dosage ordered. The Dose Unit is the unit that is associated with the numeric dosage ordered. An FDB Dose Unit equivalent must be determined. A lookup is done against the NAME, SYNONYM or FIRST DATABANK DOSE UNIT fields of the DOSE UNITS file. Each entry in the VistA DOSE UNITS file is mapped to a FDB Dose Unit.

| Dosage Ordered | Single Dose Amount | Dose Unit | FDB Dose Unit |
|--------------------|------------------------|---------------|-------------------|
| 325 MG             | 325                    | MG            | MILLIGRAMS        |
| 0.5 GM             | 0.5                    | GM            | GRAMS             |
| 1 TABLET           | 1                      | TABLET(S)     | TABLETS           |
| 20 MEQ             | 20                     | MEQ           | MILLIEQUIVALENTS  |
| 10 ML              | 10                     | ML            | MILLILITERS       |

The table above shows some examples of dosages ordered and how the single dose amount and Dose Unit would be derived.

In the sections that follow, examples of dosages ordered and how the single dose amount and Dose Unit are derived will be reviewed.

#### Possible Dosage Selection

<span id="_Toc206596776" class="anchor"></span>Example 1: Possible Dosage Selection

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/047.png)

Here is an example of an inpatient medication order where a Possible Dosage has been selected for the Orderable Item, ASPIRIN TAB. The dispense drug ASPIRIN 81MG TAB has been assigned to the order. If a Possible Dosage of ‘81MG’ is ordered, the software will use the unit identified in the DRUG file and do a lookup in the DOSE UNITS File on the NAME, SYNONYM, or FIRST DATABANK DOSE UNIT fields. Once a match is found, the software will take the corresponding FDB Dose Unit and send that to the interface. The Numeric Dose sent to the interface will be calculated by multiplying the Dispense Units per Dose by the Strength specified in the Drug File. The drug will be identified by the GCNSEQNO of the VA Product to which it is matched.

#### Local Possible Dosage for Single Ingredient Product

<span id="_Toc206596777" class="anchor"></span>Example 2: Local Possible Dosage Selected for Single Ingredient Product

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/048.png)

Here is an example of an outpatient medication order where a Local Possible Dosage has been selected for a single ingredient product. The software will identify the drug Timolol Maleate 0.5% Oph Soln with the FDB database by passing in the GCNSEQNO found for the VA product that the drug Timolol Maleate 0.5% Oph Soln is matched to. For the Local Possible Dosage of ‘2 DROPS’, the Dose Unit is mapped to the DROP(S) entry in the DOSE UNITS file and the corresponding Numeric Dose is set to ‘2’. The corresponding FDB Dose Unit ‘DROPS’ along with the Numeric Dose of ‘2’ will be sent to the interface.

#### Local Possible Dosage for Multi-Ingredient Product

<span id="_Toc206596778" class="anchor"></span>Example 3: Local Possible Dosage Selected for Multi-Ingredient Product

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/049.png)

Here is an example of an outpatient medication order where a Local Possible Dosage has been selected for a multiple ingredient product. For a combination product, Amlodipine Besylate 10mg/Benazepril 40mg cap, the GCNSEQNO that is sent to the interface identifies the drug and strength. So, when the software sends ‘2’ for the Numeric Dose and ‘CAPSULES’ for the Dose Unit to the interface, it is understood what ‘2 CAPSULE(S)’ represents.

#### Local Possible Dosage with different Dose Units

<span id="Example4" class="anchor"></span>Example 4: Local Possible Dosage(s) with Different Dose Units Defined for Same Drug

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/050.png)

Here is an example of a drug with two Local Possible Dosages defined. However, the Dose Unit that has been mapped to each of the Local Possible Dosages is not the same. In some cases, more than one Dose Unit can be specified for a Local Possible Dosage. Let’s look at the first Local Possible Dosage defined, ‘ONE TEASPOONFUL’. In this case the user could map the Dose Unit to the entry ‘TEASPOONFUL(S)’ or to the entry ‘MILLIGRAM(S)’ in the DOSE UNITS file.” Either would be acceptable, as long as the Numeric Dose is entered correctly for that Dose Unit. In the example above, the Dose Unit was mapped to the ‘MILLIGRAM(S)’ entry with a corresponding Numeric Dose of ‘160’. For the second Local Possible Dosage defined, ‘ONE TABLESPOONFUL’, the user could map the Dose Unit to the entry ‘TABLESPOONFUL(S)’ or to the entry ‘MILLIGRAM(S)’ in the DOSE UNITS file. In this case, the Dose Unit was mapped to the ‘TABLESPOONFUL(S)’ entry and assigned ‘1’ as the Numeric Dose. For the second Local Possible Dosage, since the Dose Unit was mapped to the ‘TABLESPOONFUL(S)’ entry, the GCNSEQNO will identify the drug and strength within the FDB database, in order to be able to evaluate the dosage prescribed. For the first Local Possible Dosage, since the Dose Unit was mapped to the ‘MILLIGRAM(S)’ entry, the GCNSEQNO is needed to identify the drug, but not the strength.

Whatever Dose Unit is selected for a Local Possible Dosage, should a warning message be returned indicating that the dose was too high after Dosing Order Checks are performed; the message will contain the Dose Unit sent into the interface. For example, if high doses of ACETAMINOPHEN (1440 MILLIGRAMS and 9 TABLESPOONFULS respectively) were sent into the interface, the following messages would have been returned and displayed to the clinician when two different Dose Units were defined:

For 1440 MILLIGRAMS, where 1440 was the single dose amount and MILLIGRAMS is the Dose Unit sent into the interface:

ACETAMINOPHEN ELIX 160MG/5ML 4OZ: Single dose of 1,440 milligrams exceeds

the maximum single dose of 1,000 milligrams.

For 9 TABLESPOONFULS, where 9 was the single dose amount and TABLESPOONFULS is the Dose Unit sent into the interface:

ACETAMINOPHEN ELIX 160MG/5ML 4OZ: Single dose of 9 tablespoonsful exceeds

the maximum single dose of 2.08333 tablespoonsful.

ACETAMINOPHEN ELIX 160MG/5ML 4OZ: Total dose of 9 tablespoonfuls/day

exceeds the maximum daily dose of 8.33333 tablespoonfuls/day.

The message using the ‘MILLIGRAMS’ Dose Unit may be more meaningful to the clinician versus the ‘TABLESPOONFULS’ Dose Unit. This should be kept in mind when defining the Dose Unit for Local Possible Dosages.

#### Strength Mismatch

<span id="_Toc206596780" class="anchor"></span>Example 5: Strength Mismatch (DRUG file vs. VA PRODUCT File)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/051.png)

Here is an example of an outpatient medication order where a Local Possible Dosage is ordered for a drug where a strength mismatch exists between the strength in the DRUG File and the strength of the VA Product the drug is matched to. Users need to be very careful when populating the Dose Unit and Numeric Dose fields for such a drug. The Numeric Dose should reflect the strength that is defined for the drug in the DRUG file. Although for the Local Possible Dosage of ‘TWO TEASPOONFULS’ the user can assign a Dose Unit of ‘TEASPOONFUL(S)’ or ‘MILLIGRAM(S)’, it is recommended that ‘MILLIGRAM(S)’ be selected with ‘240’ entered as the Numeric Dose in order to have the Dosing Order Check evaluated correctly. The reason for this is that the GCNSEQNO which is passed in for the VA Product that the dispense drug is matched to reflect a different strength. If the user had assigned ‘TEASPOONFUL(S)’ as the Dose Unit with a corresponding Numeric Dose of ‘2’, the GCNSEQNO passed into the interface would identify the drug and strength as ACETAMINOPHEN 160MG/5ML ELIXIR and evaluate ‘2 TEASPOONFULS’ as ‘320MG’ instead of ‘240MG’.

#### Free Text Dosages

This section will review the free text logic that the software has been used since MOCHA v2.1b to try to evaluate free text dosages.

#### Free Text Dosage – No Dispense Drug Assigned to Order

The logic used by the MOCHA v2.1b software to evaluate a free text dosage when no dispense drug is assigned to the order is described in this section. This can only occur with an order entered through CPRS because a medication order will always have a dispense drug when entered or processed through the pharmacy backdoor when Dosing Order Checks are performed. This free text logic can only be applied to a dosage ordered for a single ingredient drug. There also must be more than one dispense drug eligible for Dosing Order Checks that is associated with the Orderable Item being ordered. As a general rule, any order entered through CPRS for a multi-ingredient product with a free text dosage when a dispense drug is not assigned to the order and multiple dispense drugs are associated with the Orderable Item will not have any Dosing Order Checks performed successfully. If only one dispense drug exists for an Orderable Item and a user enters a free text dosage, CPRS WILL NOT automatically assign the one dispense drug to the order. Dosing Order Checks however will occur if that one dispense drug is eligible for Dosing Order Checks. This will be discussed in more detail further in the documentation.

If a CPRS order passes the initial set of criteria specified at the top of Diagram 1, the free text dosage is evaluated using a set of logic. The first check is labeled Logic 1 Check 1 in Diagram 1.

<span id="_Toc140565530" class="anchor"></span>Diagram 1: Free Text Dosage with No Dispense Drug - Logic 1 Check 1

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/052.png)

Logic 1 Check 1 expects the free text dosage to be in the format of ‘XY’ or ‘X\<space\>Y’ where ‘X’ represents a numeric value. The numeric value can have commas and decimals. The ‘Y’ represents the Dose Unit. No spaces or only one space is allowed between the ‘X’ and ‘Y’. The Dose Unit ‘Y’ must match the NAME, SYNONYM, or FIRST DATABANK DOSE UNIT of any entry in the DOSE UNITS file. If a match is found, the DOSE FORM INDICATOR field must be set to ‘No’ to indicate that the Dose Unit is of a metric type. If the free text dosage passes the criteria for Logic 1 Check 1, then Dosing Order Checks will be performed. If the free text dosage does not pass Logic 1 Check 1, the software moves on to check the free text dosage against the second set of logic when no dispense drug is assigned to a CPRS order.

<span id="_Toc206596781" class="anchor"></span>Example 6: Free Text Dosage for Logic 1 Check 1

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/053.png)

Here is an example of a free text dosage ordered for an inpatient medication order through CPRS. The Orderable Item selected was INSULIN HUMAN REGULAR INJ for 15UNITS SQ QAM. No dispense drug was assigned to the order. Looking at the Pharmacy Orderable Item, we see two eligible dispense drugs, INSULIN REG HUMAN 100U/ML INJ NOVOLIN R and INSULIN REG HUMAN 100U/ML INJ HUMULIN R are associated with the Orderable Item. The criteria used to determine eligibility of dispense drugs for Dosing Order Checks and how a dispense drug is selected to be used for Dosing Order Checks when no dispense drug has been assigned to the order by the application will be discussed later in this document.

In Example 6, the dispense drug selected to be used for the Dosing Order Check is INSULIN REG HUMAN 100U/ML INJ NOVOLIN R. It is matched to a VA Product with a GCNSEQNO of ‘001723’ which will identify the VistA drug in FDB. Regardless of the concentration of the injection selected for the dispense drug of the order, the dosage of 15UNITS reflects the exact dose that should be administered to the patient. 15UNITS fits our free text logic format of’ ‘XY’, where ‘X’ is a numeric and ‘Y’ is free text. ‘X’ represents ‘15’, the single dose amount and ‘Y’ represents ‘UNITS’, the Dose Unit. A lookup is done on the DOSE UNITS file to find a FDB equivalent which is UNITS. In this case, the Dose Unit that is sent into the interface for Dosing Order Checks must have the DOSE FORM INDICATOR field in the DOSE UNITS file set to ‘No’. A setting of ‘No’ indicates a metric type of unit. The entry UNIT(S) has a ‘No’ in the DOSE FORM INDICATOR field. ‘UNITS’ will be sent into the interface for the Dose Unit.

If the free text dosage ordered had been ‘0.15ML’ that has a unit of ‘ML’ which has a dose form indicator of ‘Yes’, the software would not have performed Dosing Order Checks because the Dose Unit is ambiguous and does not precisely reflect the dosage to be administered without knowing the strength of the drug. The logic cannot presume to know what strength of the drug (or in this case concentration) the provider had in mind when ordering the drug. The CPRS user would have been displayed an error message stating that the Dosing Order Checks could not be done.

Regardless of which dose had been ordered, the pharmacist when finishing the order would have had to associate the order with a dispense drug. In either case, Dosing Order Checks would have been performed.

<span id="_Toc140565531" class="anchor"></span>Diagram 2: Free Text Dosage with No Dispense Drug - Logic 1 Check 2

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/054.png)

The second check for the logic that the software uses to evaluate a free text dosage when no dispense drug is assigned to the order is illustrated in Diagram 2. As stated earlier, this logic can only be applied to an order entered through CPRS. A medication order entered or processed through pharmacy backdoor options will always have a dispense drug associated with the order when Dosing Order Checks are performed. This free text logic can only be applied to a dosage ordered for a single ingredient drug. There also must be more than one dispense drug eligible for Dosing Order Checks that is associated with the Orderable Item being ordered.

In Diagram 1 the CPRS order criteria was met, but the Logic 1 Check 1 was not met by the free text dosage, so the software moves on to execute Logic 1 Check 2 as shown in Diagram 2. The logic expects the free text dosage to be in the format of ‘X\<space\>Y’ where X represents a numeric value in the form of a pattern of predefined text. Examples are shown in the box outlined with broken lines. A whole number can be represented using a numeric value such as ‘2’ or text – ‘TWO’. Fractions can be represented by a combination of numbers and text or just text. Ranges between whole numbers can be represented by numbers, text, or a combination of numbers and text. Numbers within the range start with ‘1/4’ and go up to ‘10 1/2’. Whole numbers greater than ‘10’ within a range can only be represented by numbers. Numbers within the range do not have to be sequential (i.e., 1,2,3,4,5…), but Dosage 2 must be greater than Dosage 1.

The pattern of predefined text representing a number is followed by one space which is followed by a Dose Unit ‘Y’. The Dose Unit ‘Y’ must match the NAME, SYNONYM or FIRST DATABANK DOSE UNIT of any entry in the DOSE UNITS file. If a match is found, the DOSE FORM INDICATOR field must be set to ‘No’ to indicate that the Dose Unit is of a metric type. If the free text dosage passes Logic 1 Check 2 then Dosing Order Checks will be performed. If the free text dosage does not pass Logic 1 Check 2, Dosing Order Checks are not performed and a message stating that Dosing Order Checks could not be performed and that a manual check for appropriate dosing should be done is displayed.

<span id="_Toc206596782" class="anchor"></span>Example 7: Free Text Dosage for Logic 1 Check 2

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/055.png)

Example 7 illustrates a free text dosage ordered for an inpatient medication order through CPRS. The Orderable Item selected was LORAZEPAM TAB for 1-2 MG PO QHS PRN. No dispense drug was assigned to the order. Looking at the Pharmacy Orderable Item, we see two eligible dispense drugs, LORAZEPAM 2MG TAB and LORAZEPAM 1MG TAB are associated with the Orderable Item. The software determines the best drug for the Dosing Order Checks based on criteria. We will discuss the criteria later in the documentation. The best drug selected is LORAZEPAM 1MG TAB. This dispense drug is matched to a VA Product with a GCNSEQNO of ‘003758’ which will identify the VistA drug in FDB.

Example 7 illustrates how the software breaks down the free text dosage, ‘1-2 MG’. The logic states that a space separates the numeric representation from the Dose Unit. Therefore, ‘1-2’ represents the number and ‘MG’ represents the Dose Unit. Looking at the various patterns of predefined text we find the range ‘1-2’. The higher number will be sent into the interface for a range. In this case that is ‘2’. The software finds ‘MG’ in the DOSE UNITS file in the SYNONYM field for ‘MILLIGRAM(S)’. The dose form indicator is set to ‘No’. A setting of ‘No’ indicates a metric type of unit. ‘MILLIGRAMS’, the FDB Dose Unit equivalent is sent to the interface for the Dose Unit.

The free text dosage in Example 7 passes the Logic 1 Check 2 and Dosing Order Checks will be performed.

<span id="_Toc206596783" class="anchor"></span>Example 8: Free Text Dosage fails Logic 1 Check 2

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/056.png)Example 8 shows a free text dosage that fails for Logic 1 Check 2. A CPRS inpatient order was entered for LORAZEPAM TAB ONE TO TWO TABS PO QHS PRN. The free text dosage is ‘ONE TO TWO TABS’.

The logic states that a space separates the numeric representation from the Dose Unit. Therefore, ‘ONE TO TWO’ represents the number and ‘TABS’ represents the Dose Unit. Looking at the various patterns <span id="Page_25" class="anchor"></span>of predefined text (box with broken lines) we find the range ‘ONE TO TWO’. The higher number will be sent into the interface for a range. In this case that is ‘2’. The software finds ‘TABS’ in the DOSE UNITS file in the SYNONYM field for ‘TABLET(S)’. The dose form indicator is set to ‘Yes’. A setting of ‘Yes’ indicates a non-metric type of unit. Since the logic requires the Dose Unit to be of a metric type, the free text dosage fails, and no Dosing Order Checks are performed and a message stating that fact is displayed.

<span id="_Toc140565532" class="anchor"></span>Diagram 3: Free Text Dosage with No Dispense Drug RECAP (Logic 1 Checks 1-2)

![Diagram 3 recaps what needs to be in place for Dosing Order Checks to be performed when a free text dosage is entered through CPRS, no dispense drug is assigned to the order, and multiple dispense drugs are tied to the Orderable Item being ordered. The Orderable Item selected must represent a single ingredient. Dosing Order Checks will not be performed if a multi-ingredient is ordered. Second, the Dose Unit entered has to be metric (i.e., ‘MG’). Entry of dose form type units such as TABLET, CAPSULE will result in Dosing Order Checks not being performed.](dosing-order-check-version-2-1-user-manual-updated-p-1-262/057.png)

*Diagram 3 recaps what needs to be in place for Dosing Order Checks to be performed when a free text dosage is entered through CPRS, no dispense drug is assigned to the order, and multiple dispense drugs are tied to the Orderable Item being ordered. The Orderable Item selected must represent a single ingredient. Dosing Order Checks will not be performed if a multi-ingredient is ordered. Second, the Dose Unit entered has to be metric (i.e., ‘MG’). Entry of dose form type units such as TABLET, CAPSULE will result in Dosing Order Checks not being performed.*

The free text dosage must meet one of two formats. For format 1, the free text dosage must be in the format of ‘XY’ or ‘X\<space\>Y’ where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. For format 1, ‘X’ can only be a number. The numeric portion can only contain commas or decimals. For format 2, the free text dosage must be in the format of ‘X\<space\>Y’, where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. The numeric portion, ‘X’ must match a pattern of predefined text which can consist of whole numbers, fractions, or ranges. A whole number can be represented using a numeric value such as ‘2’ or text – ‘TWO’. Fractions can be represented by a combination of numbers and text or just text. Ranges between whole numbers can be represented by numbers, text, or a combination of numbers and text. Range numbers start with ‘1/4’ and end with ’10 1/2’. Whole numbers greater than ‘10’ within a range can only be represented by numbers. Numbers within the range do not have to be sequential (i.e., 1,2,3,4,5…), but Dosage 2 must be greater than Dosage 1.

#### Best Drug Match

One of the previous examples discussed the best drug match for Dosing Order Checks when a dispense drug is not assigned to an order when a free text dosage is selected. Criteria have been established to determine which dispense drugs are eligible for Dosing Order Checks. The first is that the dispense drug tied to the Orderable Item being ordered must be active. The second is that the dispense drug must not be exempt from Dosing Order Checks. The third is that the dispense drug must be matched to NDF and the VA Product match must have a valid GCNSEQNO. And lastly, the APPLICATION PACKAGES’ USE field values will be taken into consideration to match the CPRS order dialog once a list of equally eligible dispense drugs based on the criteria have been collected. For example, an eligible dispense drug marked for outpatient will be selected if the order is placed using the CPRS outpatient dialog. If there is more than one eligible dispense drug marked for Outpatient use on the list, a random selection is made by the software, If no eligible dispense drugs marked for outpatient use are available, then a random selection is made from the eligible drug list regardless of the APPLICATION PACKAGES’ USE.

#### Free Text Dosage – Dispense Drug Assigned to Order

<span id="_Toc140565533" class="anchor"></span>Diagram 4: Free Text Dosage with Dispense Drug – Logic 2 Check 1

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/058.png)

The sections that follow will discuss the free text logic (LOGIC 2) when a dispense drug is assigned to an order. This could be a CPRS order when a Local Possible Dosage selection is made when ordering a single or multi-ingredient product or a Pharmacy backdoor order with a dispense drug for a single or multi-ingredient product that was assigned when entering a new order or when finishing a pending order from CPRS.

For Check 1, the software loops through all the Local Possible Dosages that are defined for the dispense drug assigned to the order looking for an exact match of the dosage ordered. If a match is found, the software looks to see that a Numeric Dose and Dose Unit are defined. If yes, those values are used for Dosing Order Checks. If no match is found, the software goes on to execute the next check.

<span id="_Toc206596784" class="anchor"></span>Example 9: Free Text Dosage for Logic 2 Check 1

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/059.png)

In Example 9, an outpatient medication order is entered through CPRS for CARBAMIDE PEROXIDE 5-10 DROPS IN LEFT EAR BID. When the pharmacist selects the order to finish, the software automatically assigns CARBAMIDE PEROXIDE 6.5% OTIC SOLN as the dispense drug for the order. CARBAMIDE PEROXIDE 6.5% OTIC SOLN is marked for Outpatient and Unit Dose package use. As stated earlier, the first check in the free text logic (LOGIC 2) when a dispense drug is assigned to the order is to loop through all the Local Possible Dosages defined for the dispense drug assigned to the order. In this case, the only Local Possible Dosage defined for CARBAMIDE PEROXIDE 6.5% OTIC SOLN is 5-10 DROPS, and it is an exact match for the free text dosage that was entered through CPRS for the outpatient order. The Local Possible Dosage is marked for Inpatient use. A Numeric Dose of ‘10’ and Dose Unit of ‘DROP(S)’ are defined for the Local Possible Dosage. The ‘10’ will be sent into the interface for the single dose amount and the FDB equivalent ‘DROPS’ will be sent into the interface for the Dose Unit to perform Dosing Order Checks. The GCNSEQNO of ‘8120’ will be sent into the interface to identify the drug.

<span id="_Toc140565534" class="anchor"></span>Diagram 5: Free Text Dosage with Dispense Drug – Logic 2 Check 2

![Diagram 5 illustrates the second check for the free text logic when a dispense drug is assigned to the order. The software does the second check when the first check has failed. If the software does not find a Numeric Dose and Dose Unit defined for the Local Possible Dosage match, the Pre-Release Logic (PSS\*1\*129) is used to define those fields for Dosing Order Checks. If the Pre-Release Logic fails to define those fields, the software moves on to execute the third check.](dosing-order-check-version-2-1-user-manual-updated-p-1-262/060.png)

*Diagram 5 illustrates the second check for the free text logic when a dispense drug is assigned to the order. The software does the second check when the first check has failed. If the software does not find a Numeric Dose and Dose Unit defined for the Local Possible Dosage match, the Pre-Release Logic (PSS\*1\*129) is used to define those fields for Dosing Order Checks. If the Pre-Release Logic fails to define those fields, the software moves on to execute the third check.*

<span id="Example10" class="anchor"></span>Example 10: Free Text Dosage for Logic 2 Check 2

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/061.png)

Example 10 illustrates the second check in the free text logic when a dispense drug is assigned to the order. The inpatient order is for ALBUTEROL 90MCG/IPRAPTROPIUM BR 18MCG/SPRAY INHALER for 1-2 PUFFS QID. The dosage ordered is 1-2 PUFFS. The software loops through the Local Possible Dosages for the dispense drug to find a match for 1-2 PUFFS. The drug has three Local Possible Dosages defined, but none have the Dose Unit or Numeric Dose defined. The software uses the Pre-Release Logic to try to define the fields. In this example, the software was able to define the Numeric Dose as‘2’ and the Dose Unit as ‘INHALATION(S)’ using condition set \#4 in the Pre-Release Logic in the bottom box with broken lines in Example 10. The Numeric Dose of ‘2’ is sent into the interface for the single dose amount and the FDB equivalent ‘INHALATIONS for the Dose Unit of ‘INHALATIONS’ is sent into the interface for the Dose Unit. The GCNSEQNO of ‘29123’ is sent into the interface to identify the drug. Dosing Order Checks can be performed using those values.

<span id="_Toc140565535" class="anchor"></span>Diagram 6: Free Text Dosage for Logic 2 Check 3

![Diagram 6 illustrates the third check in the free text logic when a dispense drug is associated with an order. This is similar to Check 1 of the free text logic (Logic 1) when no dispense drug is associated with the order. The logic looks for the free text dosage being in the format of ‘XY’ or ‘X\<space\>Y’ where X represents a numeric value. The numeric value can have commas and decimals. The ‘Y’ represents the Dose Unit. No spaces or only one space is allowed between the ‘X’ and ‘Y’. The Dose Unit ’Y’ must match the NAME, SYNONYM or FIRST DATABANK DOSE UNIT of any entry in the DOSE UNITS file. The difference here is that the dose form indicator does not come into play. It can be set to ‘Yes’ or ‘No’. It does not matter. As with the other free text dosage logic checks, if the free text dosage passes Check 3, then Dosing Order Checks will be performed. If the free text dosage does not pass the Logic 2 Check 3, the software moves on to the fourth and last check of the free text logic when a dispense drug is assigned to a medication order.](dosing-order-check-version-2-1-user-manual-updated-p-1-262/062.png)

*Diagram 6 illustrates the third check in the free text logic when a dispense drug is associated with an order. This is similar to Check 1 of the free text logic (Logic 1) when no dispense drug is associated with the order. The logic looks for the free text dosage being in the format of ‘XY’ or ‘X\<space\>Y’ where X represents a numeric value. The numeric value can have commas and decimals. The ‘Y’ represents the Dose Unit. No spaces or only one space is allowed between the ‘X’ and ‘Y’. The Dose Unit ’Y’ must match the NAME, SYNONYM or FIRST DATABANK DOSE UNIT of any entry in the DOSE UNITS file. The difference here is that the dose form indicator does not come into play. It can be set to ‘Yes’ or ‘No’. It does not matter. As with the other free text dosage logic checks, if the free text dosage passes Check 3, then Dosing Order Checks will be performed. If the free text dosage does not pass the Logic 2 Check 3, the software moves on to the fourth and last check of the free text logic when a dispense drug is assigned to a medication order.*

<span id="_Toc140565536" class="anchor"></span>Diagram 7: Free Text Dosage for Logic 2 Check 4

![Diagram 7 illustrates the fourth and final check in the free text logic when a dispense drug is associated with an order. This is similar to Check 2 of the free text logic (Logic 1) when no dispense drug is associated with the order.](dosing-order-check-version-2-1-user-manual-updated-p-1-262/063.png)

*Diagram 7 illustrates the fourth and final check in the free text logic when a dispense drug is associated with an order. This is similar to Check 2 of the free text logic (Logic 1) when no dispense drug is associated with the order.*

The logic looks for the free text dosage being in the format of ‘X\<space\>Y’ where ‘X’ represents a numeric value in the form of a pattern of predefined text. Examples are shown in the box outlined with broken lines on the bottom left of the diagram. A whole number can be represented using a numeric value such as ‘2’ or text – ‘TWO’. Fractions can be represented by a combination of numbers and text or just text. Ranges between whole numbers can be represented by numbers, text, or a combination of numbers and text. Numbers in the range start with ‘1/4’ and continue up to and including ’10 1/2’. Whole numbers greater than ‘10’ within a range can only be represented by numbers. Numbers within the range do not have to be sequential (i.e., 1,2,3,4,5…), but Dosage 2 must be greater than Dosage 1.

The pattern of predefined text representing a number is followed by one space which is followed by a Dose Unit ‘Y’. The Dose Unit ‘Y’ must match the NAME, SYNONYM or FIRST DATABANK DOSE UNIT of any entry in the DOSE UNITS file the difference in this check is that if a match is found, it does not matter what the dose form indicator is set to. The software does not take it into consideration. If the free text dosage passes the check, Dosing Order Checks will be performed. If the free text dosage does not pass Check 4, Dosing Order Checks are not performed and a message stating that Dosing Order Checks could not be performed and a manual check for appropriate dosing should be done is displayed.

<span id="_Toc206596786" class="anchor"></span>Example 11: Free Text Dosage for Logic 2 Check 4

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/064.png)

Example 11 shows an outpatient medication order for AMIODARONE ½ TABLET PO TID.

Evaluating the free text dosage, ‘1/2 TABLET’, the logic states that the free text dosage can contain a pattern of predefined text which represents a number followed by one space which is followed by the Dose Unit. The software would determine ‘1/2’ to be the numeric portion and will find ‘1/2’ in the pattern of predefined text in the box at the bottom left in Example 11. The software finds ‘TABLET’ in the DOSE UNITS file in the SYNONYM field for the entry ‘TABLET(S)’. For this check, it does not matter what the dose form indicator is set to since a dispense drug is assigned to the order and we have a strength. The free text dosage passes the logic and Dosing Order Checks will be performed.

<span id="_Toc140565537" class="anchor"></span>Diagram 8: <span id="Page_34" class="anchor"></span>Free Text Dosage with Dispense Drug RECAP (Logic 2 Checks 1-4)

![Diagram 8 recaps what needs to be in place for Dosing Order Checks to be performed when a free text dosage is entered through either CPRS or Pharmacy backdoor options; a dispense drug is assigned to the order; and more than one dispense drug is tied to the Orderable Item being ordered. In this case, the Orderable Item can either represent a single ingredient or multi-ingredient.](dosing-order-check-version-2-1-user-manual-updated-p-1-262/065.png)

*Diagram 8 recaps what needs to be in place for Dosing Order Checks to be performed when a free text dosage is entered through either CPRS or Pharmacy backdoor options; a dispense drug is assigned to the order; and more than one dispense drug is tied to the Orderable Item being ordered. In this case, the Orderable Item can either represent a single ingredient or multi-ingredient.*

Since a dispense drug is assigned to the order, the software can look through all the Local Possible Dosages that are defined for the dispense drug to find a match for the free text dosage entered. If a match is found, the software looks to see if a Numeric Dose and Dose Unit fields have been populated to use for Dosing Order Checks. If the Numeric Dose and Dose Unit fields are not populated, the Pre-Release Logic is used to define those fields for Dosing Order Checks.

Since we have a dispense drug assigned to the order, the Dose Unit does not have to be a metric type. It can be either a metric or dose form type. The Dose Unit just has to be found in the DOSE UNITS file so that a FDB equivalent can be determined.

The free text dosage must meet the same two formats that must be used when a dispense drug is not assigned to the order. For format 1, the free text dosage must be in the format of ‘XY’ or ‘X\<space\>Y’ where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. For format 1, ‘X’ can only be a number. The numeric portion can only contain commas or decimals. For format 2, the free text dosage must be in the format of ‘X\<space\>Y’, where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. The numeric portion, ‘X’ must match a pattern of predefined text which can consist of whole numbers, fractions, or ranges. A whole number can be represented using a numeric value such as ‘2’ or text – ‘TWO’. Fractions can be represented by a combination of numbers and text or just text. Ranges between whole numbers can be represented by numbers, text, or a combination of numbers and text. Numbers for the ranges can start with ‘1/4’ and go up to and including ’10 1/2’. Whole numbers greater than ‘10’ within a range can only be represented by numbers. Numbers within the range do not have to be sequential (i.e., 1,2,3,4,5… ), but Dosage 2 must be greater than Dosage 1.

#### Free Text Dosage – Logic 1 and Logic 2 Combination

<span id="_Toc140565538" class="anchor"></span>Diagram 9: Free Text Dosage without Dispense Drug for Logic 1 and Logic 2 Combination

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/066.png)

The third free text dosage scenario is somewhat of a combination of the Logic 1 and Logic 2 scenarios that were reviewed. The order criterion is similar to Logic 1 where we have an order with no dispensed drug assigned. This can only occur with a CPRS order. The drug ordered can be either a single or multi-ingredient. There is only one eligible dispense drug tied to the Orderable Item being ordered for Dosing Order Checks. And of course, a free text dosage is entered. If the order meets the criteria, the software executes free text Logic 2, Checks 1 through 4. If any of the checks are met, the Dosing Order Checks will be performed. If not, the CPRS user will be informed that Dosing Order Checks will not be performed and to do a manual check.

What should be noted is that although a dispense drug is not assigned to the CPRS order when only one eligible dispense drug is tied to the Orderable Item, the software uses that dispense drug to perform Dosing Order Checks.

<span id="Example12" class="anchor"></span>Example 12: <span id="Page_36" class="anchor"></span>Free Text Dosage for Logic 1 and Logic 2 Combination

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/067.png)Example 12 illustrates an order that would have failed the free text logic when no dispense drug is assigned to the order. It is not only a multi-ingredient, but the Dose Unit is a non-metric type (dose form indicator is set to Yes). An outpatient order was entered for ACETAMINOPHEN/CODEINE TAB 2 TABLETS PO Q4H as needed for pain. Only one dispense drug is eligible and tied to the Orderable Item.

Since this order meets the criteria, and the only dispense drug tied to the Orderable Item is eligible for Dosing Order Checks, the dispense drug will be used to perform Dosing Order Checks. The free text dosage of ‘2 TABLETS’ will be evaluated using one of the four Checks in Logic 2. In this case, the free text dosage passes Check 3 and Dosing Order Checks will be performed.

<span id="_Toc140565539" class="anchor"></span>Diagram 10: Free Text Dosage without Dispense Drug for Logic 1 & Logic 2 Combination RECAP

![Diagram 10 recaps what needs to be in place for Dosing Order Checks to be performed when a free text dosage is entered through either CPRS or Pharmacy backdoor options; no dispense drug is assigned to the order; and only one dispense drug is tied to the Orderable Item being ordered. Because there is a 1:1 relationship between the dispense drug and the Orderable Item, the dispense drug will be used for Dosing Order Checks. It will not be automatically assigned to the order, however.](dosing-order-check-version-2-1-user-manual-updated-p-1-262/068.png)

*Diagram 10 recaps what needs to be in place for Dosing Order Checks to be performed when a free text dosage is entered through either CPRS or Pharmacy backdoor options; no dispense drug is assigned to the order; and only one dispense drug is tied to the Orderable Item being ordered. Because there is a 1:1 relationship between the dispense drug and the Orderable Item, the dispense drug will be used for Dosing Order Checks. It will not be automatically assigned to the order, however.*

The rules to derive a Numeric Dose and Dose Unit from the free text dosage will be the same as if a free text dosage was entered for an order where a dispense drug is assigned.

The software will first look through all the Local Possible Dosages that are defined for the dispense drug to find a match for the free text dosage entered. If a match is found, the software looks to see if a Numeric Dose and Dose Unit have been populated to use for the Dosing Order Checks. If the Numeric Dose and Dose Unit fields are not populated, the Pre-Release Logic is used to define those fields for Dosing Order Checks.

The Dose Unit can be either a metric or dose form type. The Dose Unit just has to be found in the DOSE UNITS file so that a FDB equivalent can be determined.

The free text dosage must meet the same two formats that we have already discussed. For format 1, the free text dosage must be in the format of ‘XY’ or ‘X\<space\>Y’ where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. For format 1, ‘X’ can only be a number. The numeric portion can only contain commas or decimals. For format 2, the free text dosage must be in the format of ‘X\<space\>Y’, where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. The numeric portion, ‘X’ must match a pattern of predefined text which can consist of whole numbers, fractions, or ranges. A whole number can be represented using a numeric value such as ‘2’ or text – ‘TWO’. Fractions can be represented by a combination of numbers and text or just text. Ranges between whole numbers can be represented by numbers, text, or a combination of numbers and text. Numbers within the range start at ‘1/4’ and go up to and including ’10 1/2’. Whole numbers greater than ‘10’ within a range can only be represented by numbers. Numbers within the range do not have to be sequential (i.e., 1,2,3,4,5…), but Dosage 2 must be greater than Dosage 1.

#### Dosage Text in Provider Comments

<span id="_Toc206596788" class="anchor"></span>Example 13: Dosage Entered in Provider Comment Field

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/069.png)

As a general rule, if dosages are entered in comment fields, as in Example 13, Dosing Order Checks will not be performed. The user will see a message displayed that Dosing Order Checks could not be performed and to do a manual check for appropriate dosing.

If a free text dosage cannot be evaluated, a message will be displayed to both the Pharmacy and CPRS user. For the pharmacy user the message will read: ‘Dosing Checks could not be performed for Drug: \<DRUG NAME\> Reason(s): Free Text Dosage could not be evaluated.’

For the CPRS user the message will read: ‘Dosing Checks could not be done for Drug: \<DRUG NAME\>, please complete a manual check for appropriate Dosing.’ This is a generic message with no specific reason.

#### Free Text Dosage Range Enhancements

Patch PSS\*1\*201 provides enhanced free text logic for dosage ranges. MOCHA v2.0 free text logic rules will still apply unless otherwise specified.

For documentation purposes, a free text dosage range will be represented by 3 sections:

DOSAGE 1 + DELIMITER + DOSAGE 2

DOSAGE 1 is represented by ‘X’ or ‘XY’ or ‘X\<space\>Y’; where ‘X’ represents a number and ‘Y’ represents the Dose Unit. DOSAGE 2 is represented by ‘XY’ or ‘X\<space\>Y’; where ‘X’ represents a number and ‘Y’ represents the Dose Unit. The number, represented by ‘X’ can contain commas and decimals. Numbers represented by ‘X’ in DOSAGE 1 and DOSAGE 2 do not have to be sequential, but DOSAGE 2 must be greater than DOSAGE 1. The higher number, represented by ‘X’ in DOSAGE 2, identified within the range will be sent in for the Dosing Order Checks.

‘Y’ which represents the Dose Unit must match the NAME, SYNONYM or FIRST DATABANK DOSE UNIT of any entry in the DOSE UNITS file (#51.24). If only one Dose Unit is identified for a free text dosage range, that Dose Unit will be sent in for the Dosing Order Checks. If two Dose Units have been identified for a free text dosage range, but the Dose Units are not resolved (same IEN in DOSE UNITS file) to be the same, Dosing Order Checks will not be performed.

The following DELIMITERS are allowed with the free text dosage range:

- Dash represented by ‘-’
- ‘TO’ represented by all lowercase, all uppercase, or a combination of lowercase/uppercase characters
- ‘OR’ represented by all lowercase, all uppercase, or a combination of lowercase/uppercase characters

One space is allowed before and/or after the DELIMITER.

<span id="_Toc206596789" class="anchor"></span>Example 14: <span id="Page_40" class="anchor"></span>Free Text Dosage Range with one Dose Unit

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/070.png)

Example 14 displays an inpatient pending order for ACETAMINOPHEN 325MG TAB 325-650MG PO Q6H PRN.

The logic states that the free text dosage range is represented by 3 sections, Dosage 1, Dosage 2 and a Delimiter between Dosage 1 and Dosage 2. Dosage 1 can be in the format ‘X’, ‘XY’ or ‘X\<space\>Y’ and Dosage 2 can be in the format ‘XY’ or ‘X\<space\>Y’; where ‘X’ represents a number and ‘Y’ represents the Dose Unit. No spaces or only one space is allowed between ‘X’ and ‘Y’. Dosage 1 and Dosage 2 do not have to be sequential (i.e., 1,2,3,4,5…), but Dosage 2 must be greater than Dosage 1. A Delimiter of a dash (-), the text ‘TO’ or ‘OR’ represented by lowercase or uppercase characters is allowed. One space is allowed before and/or after the Delimiter.

In the dosage ordered of ‘325-650MG’, Dosage 1 is represented by only a number, ‘325’; which is an acceptable format of ‘X’. A dash (-) represents the Delimiter. Dosage 2 is represented by ‘650MG’; where ‘650’ is the numeric value of ‘X’ and ‘MG’ represents the Dose Unit ‘Y’. No spaces between the Delimiter and Dosage 1 and Dosage 2 are acceptable. The software does find ‘MG’ in the DOSE UNITS file in the SYNONYM field for the MILLIGRAM(S) entry. Since only one Dose Unit is identified within the free text dosage range, ‘MILLIGRAMS’ will be sent in for the Dosing Order Checks. The greater numeric value of ‘650’ representing Dosage 2 will be sent in for the Dosing Order Checks.

In Example 14, the order had a dispense drug, Acetaminophen 325mg tab, assigned. The Dosing Order Check would still have been performed if the order had not been assigned a dispense drug, as long as the dose form indicator for the Dose Unit within the free text dosage range is set to ‘No’. In this example, the dose form indicator for ‘MILLIGRAMS’ is set to ‘No’. Had the Dose Unit’s dose form indicator been set to ‘Yes’ such as it is for ‘TABS’, the Dosing Order Check would only have been performed if a dispense drug was assigned to the order when processing orders through backdoor Pharmacy options or if entering the order through CPRS and the orderable item being entered was associated with only one dispense drug.

<span id="_Toc206596790" class="anchor"></span>Example 15: <span id="Page_41" class="anchor"></span>Free Text Dosage Range with two Dose Units

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/071.png)

Example 15 displays an outpatient pending order for DIPHENHYDRAMINE 25MG CAP 1 CAP OR 2 CAPS PO Q6H PRN.

In the dosage ordered of ‘1 CAP OR 2 CAPS’, Dosage 1 is represented by ‘1 CAP’ in the format ‘X\<space\>Y’; where ‘1’ is the numeric value of ‘X’ and ‘CAP’ represents the Dose Unit ‘Y’. ‘OR’ represents the Delimiter. Dosage 2 is represented by ‘2 CAPS’ in the format ‘X\<space\>Y’; where ‘2’ is the numeric value of ‘X’ and ‘CAPS’ represents the Dose Unit ‘Y’. One space between the Delimiter and Dosage 1 and Dosage 2 are acceptable. In this example, we have two Dose Units, ‘CAP’ and ‘CAPS’ that have been identified for the free text dosage range. The software finds ‘CAP’ and ‘CAPS’ in the DOSE UNITS file in the SYNONYM field for the same CAPSULE(S) entry. Since both Dose Units resolve to the same IEN in the DOSE UNITS file, ‘CAPSULES’ will be sent in for the Dosing Order Checks. The greater numeric value of ‘2’ representing Dosage 2 will be sent in for the Dosing Order Checks.

In Example 15, the order had a dispense drug, Diphenhydramine 25mg Cap, assigned when the pending order was finished, so even though the dose form indicator for the Dose Unit of ‘CAP’ and ‘CAPS’ was set to ‘Yes’, Dosing Order Checks were performed. Dosing Order Checks were not performed when this same order was initially entered through CPRS, because the dose form indicator of the Dose Units, ‘CAP’ and ‘CAPS’ was set to ‘Yes’ and more than one dispense drug was associated with the Orderable Item.

#### Informational Data in Parenthesis as part of Dosage Ordered

Many times when a dosage is ordered for a medication, clarifying information is placed in parenthesis next to the actual dose (i.e. 1 PATCH (0.2MG/24HR)). Patch PSS\*1\*201 makes software modifications to the free text logic to now evaluate this type of free text dosage.

In Diagram 11, using the existing MOCHA v2.0 free text logic, in step 1, the software first evaluates the free text entry as a whole with or without parenthesis. If a single dose amount and Dose Unit can be derived from the free text entry as a whole, Dosing Order Checks will be performed. If a single dose amount and Dose Unit cannot be determined from the free text entry as a whole, the free text portion preceding the informational data within parenthesis is evaluated as shown in step 2. If the software can derive a single dose amount and Dose Unit from the free text portion preceding the informational data within parenthesis, Dosing Order Checks will be performed. If a single dose amount and dose unit from the free text portion preceding the information data within the parenthesis, cannot be determined, the software next evaluates the free text portion within the parenthesis as shown in step 3. If the software can derive a single dose amount and Dose Unit from the free text portion within the parenthesis, Dosing Order Checks will be performed. If a single dose amount and dose unit from the free text portion within the parenthesis cannot be determined, Dosing Order Checks will not be performed, and an error message will be displayed to the user indicating that the Dosing Check could not be performed.

<span id="_Toc140565540" class="anchor"></span>Diagram 11: Free Text Logic for Informational Data in Parenthesis as part of Dosage Ordered

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/072.png)

Let us take a look at one example of a free text dosage that includes clarifying information in parenthesis.

Examples 16 – 18, will illustrate steps 1-3 in Diagram 11. We will look at an order that was entered through CPRS with a free text dosage that has clarifying information in parenthesis and where no dispense drug was assigned to the order. There is only one dispense drug tied to the Orderable Item being ordered. Because there is a 1:1 relationship between the dispense drug and the Orderable Item, the dispense drug will be used for the Dosing Order Checks.

<span id="Page_43" class="anchor"></span>In Example 16, using existing MOCHA v2.0 rules to derive a Numeric Dose and Dose Unit from the free text dosage will be the same as if a free text dosage was entered for an order where a dispense drug is assigned. The software will first evaluate the free text dosage as a whole. The order that was entered was for NIFEDIPINE 90MG SA TAB with a free text dosage of ‘ONE TABLET (90MG)’.

<span id="_Toc206596791" class="anchor"></span>Example 16: Evaluate Free Text Dosage as a Whole (Step 1 in Diagram 11)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/073.png)The software will first look through all the Local Possible Dosages that are defined for the dispense drug to find a match for the free text dosage entered. The only Local Possible Dosage defined for NIFEDIPINE 90MG SA TAB is ‘ONE TABLET’ and is not a match for ‘ONE TABLET (90MG)’. The free text dosage meets the format ‘X\<space\>Y’ where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. For the free text dosage, ‘ONE TABLET (90MG)’, ‘ONE’ represents the numeric portion; a pattern of predefined text representing the numeric value of ‘1’. ‘TABLET (90MG)’ represents ‘Y’, the Dose Unit. ‘TABLET (90MG) is not found in the DOSE UNITS file. Although a Numeric Dose can be determined, a Dose Unit cannot, so the software moves on to step 2; evaluating the free text portion preceding the informational data in parenthesis as illustrated in Example 17.

<span id="Page_44" class="anchor"></span>Example 17: Evaluate Free Text Portion preceding Informational Data in Parenthesis (Step 2 in Diagram 11)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/074.png)In Example 17, ‘ONE TABLET’ is the free text portion preceding the informational data in parenthesis.

Using existing MOCHA v2.0 logic as in step 1, for step 2, the software will first look through all the Local Possible Dosages that are defined for the dispense drug, NIFEDIPINE 90MG SA TAB, to find a match for the free text dosage entered. For the free text portion of ‘ONE TABLET’ a match is found. The Numeric Dose and Dose Unit have been populated. The Numeric Dose is set to ‘1’ and the Dose Unit is set to the ‘TABLET(S)’ entry. The FDB Dose Unit of ‘TABLETS’ and the Numeric Dose of ‘1’ will be sent into the interface for the Dosing Order Checks.

Had there not been a Local Possible Dosage defined, a successful Dosing Order Check would still have been possible. The free text portion of ‘ONE TABLET’ meets the format ‘X\<space\>Y’ where ‘X’ represents the Numeric Dose and ‘Y’ represents the Dose Unit. For the free text portion, ‘ONE TABLET’, ‘ONE’ represents the numeric portion; a pattern of predefined text representing the numeric value of ‘1’. ‘TABLET’ represents ‘Y’, the Dose Unit. ‘TABLET’ is found in the SYNONYM field of the DOSE UNITS file. Both a Numeric Dose and Dose Unit can be determined, resulting in a successful Dosing Order Check. In step 2, more than one check in the current MOCHA v2.0 free text logic allowed for the determination of a Numeric Dose and Dose Unit.

Although there is no need to continue to step 3 as illustrated in Diagram 11, let us evaluate the free text portion within the parenthesis to see what the results would have been. In Example 18, the free text portion ‘90MG’ within parenthesis is evaluated.

<span id="Page_45" class="anchor"></span>Example 18: Evaluate Free Text Portion in Parenthesis (Step 3 in Diagram 11)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/075.png)

Had the software not been able to determine a Numeric Dose and Dose Unit in step 2 of Diagram 11, the software would have moved on to step 3 to evaluate the free text portion within the parenthesis. As in steps 1 and 2, the software will first look through all the Local Possible Dosages that are defined for the dispense drug to find a match for the free text dosage entered. A match is not found for the free text portion of ‘90MG’. The free text portion ‘90MG’ meets the format of ‘XY’; where ‘X’ represents the Numeric Dose and can only be a number. ‘Y’ represents the Dose Unit. The Dose Unit can be either a metric or dose form type. The Dose Unit just has to be found in the DOSE UNITS file so that a FDB equivalent can be determined. In Example 18, ‘90’ represents the Numeric Dose and ‘MG’ is found in the SYNONYM field for the ‘MILLIGRAM(S)’ entry. The free text portion within the parenthesis would have also resulted in successful Dosing Order Checks.

#### Free Text Logic for Multi-Ingredient where dose unit derived from Free Text Dosage matches active ingredient dose unit

Combination Insulin Products have active ingredients that are assigned the same dose units as the combination product when the product is ordered. MOCHA v2.0 did not perform Dosing Order Checks on a combination product for which a free text dosage was ordered if no dispense drug was assigned to the order and multiple dispense drugs were associated with the Orderable Item. With Patch PSS\*1\*201, the software will allow Dosing Order Checks to occur if the dose unit derived from the Free Text Dosage matches the drug units assigned to the active ingredients and is not a dose form type.

<span id="Page_46" class="anchor"></span>In Example 19, an order is entered through CPRS for a multi-ingredient product, INSULIIN HUMULIN 70/30 INJ 15 UNITS SQ QAM. The Orderable Item is associated with two dispense drugs; so no dispense drug is assigned to the order. The free text dosage ordered, ‘15 UNITS’ contains the Dose Unit of ‘UNITS’ which has a dose form indicator of ‘No’. The best match, dispense drug INSULIN HUMULIN 70/30 (NPH/REG) INJ LILY has two active ingredients. Both active ingredients have ‘UNIT/ML’ for their units. The software recognizes what is in front of the ‘/’ as the Dose Unit which is ‘UNIT’. Both ‘UNIT’ and ‘UNITS’ are both synonyms for the UNIT(S) entry in the Dose Units file (#51.24). Since the units assigned to the active ingredients of the product ordered match the Dose Units within the dosage ordered, Dosing Order Checks will be performed.

<span id="Example19" class="anchor"></span>Example 19: Free Text Dosage - Dose Units Match Active Ingredient Dose Units for Multi-Ingredient Product

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/076.png)

#### IV Orders

<span id="Page_47" class="anchor"></span>IV orders are a bit more complicated, and the derivation of the single dose amount and Dose Unit is based on various business rules. The single dose amount and Dose Unit can be derived from an IV Solution volume, an IV Additive strength/unit, infusion rate, or calculated via a formula. Some examples are shown in Tables 1 and 2.

Table 1: Examples of Single Dose Amount and Dose Unit derived from IV AdditiveIV Additives<u>Strength</u><u>Drug Unit</u><u>Single Dose</u> <u>FDB Dose</u><u>Amount</u> <u>Unit</u>

20 MEQ 20 MILLIEQUIVALENTS

0.5 GM 0.5 GRAMS

2 MU 2 MILLION UNITS

30 IU 30 UNITS

Table 2: Examples of Single Dose Amount and Dose Unit derived from IV SolutionIV Solution marked as PreMix<u>IV Type</u> <u>Volume</u> <u>Infusion Rate</u> <u>Drug Unit</u> <u>Single Dose</u> <u>FDB Dose </u><u>Amount</u> <u>Unit</u>

Piggyback 20 ML 20 MILLILITERS

Admixture 125ML/HR ML 125 MILLILITERS

Table 1 displays some examples of IV orders where the single dose amount and Dose Unit are derived from the strength and unit of the IV Additive. The single dose amount is derived from the strength of the IV Additive. A lookup is done in the VistA DOSE UNITS file using the drug unit for the IV Additive to find the FDB Dose Unit equivalent.

In Table 2, there are two IV orders with just an IV Solution that is marked as a PreMix. In the first example, the IV type, of the order is Piggyback. It is an intermittent order. In this case, the volume of the IV Solution is used to derive the single dose amount and Dose Unit. The single dose amount will be ’20’ and the FDB Dose Unit equivalent for ‘ML’; which is ‘MILLILITERS’ will be sent into the interface for the Dose Unit.

In the second example, we have another IV order with only an IV Solution that is marked as a PreMix. The IV type of the order is Admixture. It is a continuous order. In this case, the infusion rate of the order is used to derive the single dose amount and Dose Unit. The single dose amount will be ‘125’ and the FDB Dose Unit equivalent for ‘ML’; which is ‘MILLILITERS’ will be sent into the interface for the Dose Unit.

In some cases, a formula will be used to calculate the single dose amount for an IV order. The IV order must be continuous and only have one IV Additive and one IV Solution that is not marked as a PreMix. The software will check FDB dosing records for the dispense drug associated with the IV Additive to see whether or not it can be administered via a continuous FDB dose route. Continuous FDB routes will be discussed later on in the documentation in more detail. If the answer is ‘No’, the IV Additive strength and drug unit are used to calculate the single dose amount and Dose Unit. If the answer is ‘Yes’, then the formula is used to calculate the single dose amount. The IV Additive drug unit will be used to derive the Dose Unit. The formula used is as follows:

<span id="Page_48" class="anchor"></span>Single Dose Amount/Dose Rate = (IV Additive Strength & Unit/ Volume of the IV Solution) \* Infusion rate (ML/HR)

Let us look at a continuous IV order for Heparin 25,000 units in D5W 250ml to run 10ml/hr. Heparin can be administered via a continuous FDB dose route. The formula is used to calculate the single dose amount. We take the 25,000 units and divide by 250ml and multiply by 10ml/hr for a result of 1000 units/hr. The single dose amount is ‘1000’, the FDB Dose Unit equivalent is ‘UNITS’ and the dose rate which we have not yet discussed is ‘HOUR’.

Examples of IV orders and the business rules that are applied to determine the single dose amount and Dose Unit will be reviewed in the sections that follow.

#### IV Additive Strength and Drug Unit

<span id="_Toc133325849" class="anchor"></span>IV Example 1: Intermittent IV Type Order – One IV Additive/One IV Solution (not PreMix)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/077.png)

IV Example 1 shows an intermittent IV order with an IV type of Piggyback with one IV Additive (CEFAZOLIN) and one IV Solution (5% DEXTROSE) that is not a PreMix. In this case, the single dose amount and Dose Unit are derived from the IV Additive strength/unit. The single dose amount will equal the strength ‘2’ and the drug unit of the IV Additive ‘GM’ will be looked up in the DOSE UNITS file to find the FDB Dose Unit equivalent which is ‘GRAMS’. The GCNSEQNO of ‘9065’ is identified by looking at the VA Product for the dispense drug that is associated with the IV Additive.

#### IV Solution (PreMix) – Infusion Rate

<span id="_Toc133325850" class="anchor"></span>IV Example 2: Continuous IV Type with only an IV Solution (PreMix)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/078.png)

IV Example 2 shows a continuous IV order with an IV type of Admixture with only an IV Solution (HEPARIN 25,000 UNITS/0.45% NACL) that is marked as a PreMix. In this example, the infusion rate is used to determine the single dose amount and Dose Unit. The ‘10’ will be sent in for the single dose amount and the FDB equivalent of ‘ML’ which is ‘MILLILITERS’ will be sent into the interface for the Dose Unit. The GCNSEQNO of ‘60440’ is identified by looking at the VA Product for the dispense drug that is associated with the IV Solution.

Entry through backdoor pharmacy options require that the infusion rate be entered in the format of ‘ML/HR’, however the provider through CPRS may enter infusion rates in other formats and the order may be finished through pharmacy in those formats. Let us take a look at some free text infusion rate formats that the software will recognize and for which Dosing Order Checks will be performed.

If the infusion rate is in the format of ‘XML/HR’ or XML/HR@N’, where ‘X’ represents a numeric value and the single dose amount; and ‘N’ represents a numeric value for the number of IV labels to be generated. The FDB equivalent of ‘ML’ which is ‘MILLILITERS’ will be sent to the interface for the Dose Unit. ‘HOUR’ will be sent for the Dose Rate Unit/Duration Rate. This format applies to IV orders that may be entered through CPRS or Pharmacy backdoor options.

Examples that meet this format are shown in Table 3.

Table 3: Infusion Rate Examples for ‘XML/HR’ or ‘XML/HR@N’ formats

> <u>Infusion Rate</u> <u>Single Dose Amount</u> <u>Drug Unit</u> <u>FDB Dose Unit</u>

125ML/HR 125 ML MILLILITERS

100ML/HR@1 100 ML MILLILITERS

167ML/HR@0 167 ML MILLILITERS

The single dose amount will be derived from the numeric portion of the infusion rate and the FDB equivalent of the drug unit ‘ML’ which is ‘MILLILITERS’ will be sent to the interface for the Dose Unit. ‘HR’ represents the Dose Rate/Duration Rate and will be sent into the interface as ‘HOUR’.

Let us take a look at another infusion rate format that specifies a patient parameter. If we look at format ‘XY/P/R@N’ or ‘X\<space\>Y/P/R@N’; where ‘X’ represents the Numeric Dose; ‘Y’ represents the Dose Unit; ‘P’ represents a patient parameter; and ‘N’ represents a numeric value for the number of IV labels to be generated. The software will only consider two values for ‘P’ and they are ‘KG’ or ‘M<sup>2</sup>’. The software will multiply the parameter value for the patient by the Numeric Dose to calculate the single dose amount to send into the interface.

‘R’ represents the Dose Rate/Duration Rate. Acceptable values for ‘R’ are ‘MIN’ or ‘MINUTE’; ‘HR’ or ‘HOUR’; and ‘DAY’. The software will send in a Dose Rate/Duration Rate equal to ‘MINUTE’, ‘HOUR’ or ‘DAY’ respectively.

This format only applies to orders entered through CPRS and two examples are shown below in Table 4.

Table 4: Infusion Rate Examples for ‘XY/P/R@N’ or ‘X\<sp\>Y/P/R@N’ formats

> <u>Infusion Rate</u> <u>Single Dose Amount</u> <u>Drug Unit</u><u>FDB Dose Unit</u>

50MCG/KG/MIN@0 50 \* Patient’s weight in KG MCG MICROGRAMS

1.5MG/M<sup>2</sup>/DAY@1 1.5 \* Patient’s BSA in M<sup>2</sup> MG MILLIGRAMS

Evaluating the first Infusion Rate of ‘50MCG/KG/MIN@0’listed in Table 4, the Numeric Dose is ’50’; the drug unit is ‘MCG’; the patient parameter is ‘KG’ and the Dose Rate Unit/Duration Rate is ‘MIN’. The single dose amount will be calculated by looking up the patient’s latest weight in ‘KG’ and multiplying by ‘50’. If the patient was 70KG, the single dose amount would be calculated to be ‘3500’. The software does a lookup into the DOSE UNITS file for the drug unit of ‘MCG’ to find the FDB equivalent of ‘MICROGRAMS’ to send into the interface. ‘MINUTE’ will be sent into the interface for our Dose Rate/Duration Rate.

Evaluating the second Infusion Rate of ‘1.5MG/M<sup>2</sup>/DAY@1’ listed in Table 4, the Numeric Dose is ‘1.5’; the drug unit is ‘MG’; the patient parameter is ‘M<sup>2</sup>’; and the Dose Rate/Duration Rate is ‘DAY’. The single dose amount will be calculated by looking up the patient’s latest weight and height and using the DUBOIS formula to calculate the Body Surface Area (BSA). If the patient had a BSA of ‘1.5’, the single dose amount would be calculated to be ‘2.25’. The software does a lookup into the DOSE UNITS file for the drug unit of ‘MG’ to find the FDB equivalent of ‘MILLIGRAMS’ to send into the interface. ‘DAY’ will be sent into the interface for the Dose Rate/Duration Rate.

This infusion rate format will not be recognized if a new order is placed through backdoor pharmacy options. A message will be displayed to the pharmacy user that Dosing Order Checks could not be performed because the free text infusion rate could not be evaluated.

Let’s take a look at another infusion rate format of ‘XY/R@N’ or ‘X\<space\>Y/R@N’. The ‘X’ represents the Numeric Dose or single dose amount; the ‘Y’ represents a free text value which in this case is the Dose Unit; the ‘R’ represents the Dose Rate/Duration Rate, and the ‘N’ represents a numeric value for the number of IV labels to be generated. This format only applies to orders entered through CPRS.

If the values for ‘R’ are ‘MIN’ or ‘MINUTE’; ‘HR’ or ’HOUR’; and ‘DAY’, the software shall set the Dose Rate/Duration Rate equal to ‘MINUTE’, ‘HOUR’ or ‘DAY’ respectively.

This infusion rate format will not be recognized if a new order is placed through backdoor pharmacy options. A message will be displayed to the pharmacy user that Dosing Order Checks could not be performed because the free text infusion rate could not be evaluated.

Table 5: Infusion Rate Examples for ‘XY/R@N’ or ‘X\<SP\>Y/R@N’ formats

> <u>Infusion Rate</u> <u>Single Dose Amount</u> <u>Drug Unit</u> <u>FDB Dose Unit</u>

8MG/HR@1 8 MG MILLIGRAMS

1000UNITS/HR@0 1000 UNITS UNITS

Evaluating the first Infusion Rate listed in Table 5, the Numeric Dose or single dose amount is ‘8’, the drug unit is ‘MG’, and the Dose Rate Unit/Duration Rate is ‘HR’. The software does a lookup into the DOSE UNITS file for the drug unit of ‘MG’ to find the FDB equivalent of ‘MILLIGRAMS’ to send into the interface. ‘HOUR’ will be sent into the interface for our Dose Rate/Duration Rate.

Evaluating the second Infusion Rate listed in Table 5, the Numeric Dose or single dose amount is ‘1000’, the drug unit is ‘UNITS’ and the Dose Rate/Duration Rate is ‘HR’. The software does a lookup into the DOSE UNITS file for the drug unit of ‘UNITS’ to find the FDB equivalent of ‘UNITS’ to send into the interface. ‘HOUR’ will be sent into the interface for the Dose Rate/Duration Rate.

Additional text can now be entered in the infusion rate field; TITRATE AT and START AT when entering a continuous IV order through CPRS. Acceptable formats would be ‘TITRATE AT 10u/kg/min@0’ or ‘START AT 10ml/hr@0’.

If the format cannot be interpreted for the free text infusion entered, a message will be displayed to the pharmacy user informing them that Dosing Order Checks could not be performed and the reason why.

Maximum Single Dose Check could not be performed for Drug: DOBUTAMINE 1000MG IN D5W 250 ML

Reason(s): Free Text Infusion Rate could not be evaluated.

#### IV Solution (PreMix) – Volume

<span id="_Toc133325851" class="anchor"></span>IV Example 3: Intermittent Order with only IV Solution (PreMix)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/079.png)

IV Example 3 is an intermittent IV order with an IV type of Piggyback with only an IV Solution (CEFAZOLIN 2GM IN D5W) that is marked as a PreMix. In this example, the volume of the IV Solution will be used to determine the single dose amount and the Dose Unit. The ‘100’ will be the single dose amount and the FDB equivalent of ‘ML’ which is ‘MILLILITERS’ will be sent into the interface for the Dose Unit. The GCNSEQNO of ‘9059’ is identified by looking at the VA Product for the dispense drug that is associated with the IV Solution.

#### Calculated Formula - Single Dose & Dose Unit

<span id="_Toc133325861" class="anchor"></span>IV Diagram 1: Step 1 - Does IV Order Meet Criteria?

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/080.png)

The IV order in IV Diagram 1 is a continuous IV order with an IV type of Admixture with one IV Additive (HEPARIN) and one IV Solution (5% DEXTROSE) not marked as a PreMix. The dispense drug associated with the HEPARIN IV Additive is HEPARIN 10,000 units/ml 5ml vial. The VA Drug Class is BL110. For this type of order before Dosing Order Checks can be performed, it needs to be determined how the single dose amount and Dose Unit will be derived. They can either be derived from the strength and unit of the IV Additive or from the following formula which has already been discussed:

(IV Additive Strength & Unit/Volume of IV Solution) \* Infusion rate (ML/HR) = Dose/Dose Rate

In Step 1 it needs to be determined if the order meets certain criteria. For all continuous IV orders entered through CPRS or pharmacy IV orders that have an IV Type of ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’ or ‘Chemotherapy Continuous Syringe’ that have one IV Additive and one IV Solution not marked as a PreMix and the Dispense Drug associated with the IV Additive does not have a VA Drug Class code that contains a ‘VT’, the software will send an inquiry over to the FDB database to determine if the drug can be administered via a ‘CONTINUOUS’ FDB Dose route. If the IV order does not meet the criteria, the single dose amount and Dose Unit are derived using the IV Additive strength and drug unit. If the IV order meets the criteria, as it does in this case, the inquiry to the FDB database is performed as illustrated in Step 2 of IV Diagram 2.

<span id="_Toc133325862" class="anchor"></span>IV Diagram 2: Step 2 – Query Made To FDB Database

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/081.png)

A list of FDB continuous Dose Routes is shown at the top of IV Diagram 1. The IV order and drug met the criteria in IV Diagram 1 and an inquiry is made to the FDB database in STEP 2 on IV Diagram 2 to retrieve a list of FDB Dose Routes found in dosing records for the dispense drug associated with the IV Additive.

The second box in the diagram displays the query results for HEPARIN 10,000 units/ml 5ml vial. The FDB dose routes that are returned are continuous IV infusion, continuous intra-arterial infusion, intra-arterial, intravenous, intravesical, and subcutaneous. The ‘continuous IV infusion’ route is listed as one of the continuous FDB Dose Routes in the box at the top of the diagram. Since there is one continuous FDB Dose Route returned Step 3 is executed in IV Diagram 3.

Had no continuous FDB Dose Routes been returned, the IV Additive strength and drug unit would have been used to derive the single dose amount and Dose Unit for the Dosing Order Checks.

<span id="_Toc133325863" class="anchor"></span>IV Diagram 3: Comparison Between Query Results and IV Order Route

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/082.png)If the drug can be administered via a ‘CONTINUOUS’ FDB Dose route, the software checks the list of continuous FDB Dose routes that are returned for the drug and compares them against the list of continuous FDB dose routes and their associated Standard Medication Routes shown in the IV Diagram 3. If the Local Medication Route found in the IV order is mapped to any of those Standard Medication Route(s), then the single dose amount and Dose Unit will be derived using the formula shown in IV Diagram 3. If no matches are found, the single dose amount and the Dose Unit will be derived using the IV Additive strength and unit.

In this case the Local Medication Route was ‘IV’ and it was mapped to a Standard Medication Route of ‘INTRAVENOUS’. The Standard Medication Route ‘INTRAVENOUS’ maps to the continuous FDB Dose route of ‘continuous IV infusion’. The continuous FDB Dose Route returned for the drug was ‘continuous IV infusion’. We have a match. The formula will be used to derive the single dose amount and Dose Unit.

<span id="_Toc133325864" class="anchor"></span>IV Diagram 4: Continuous IV Order with One IV Additive and One IV Solution (not a PreMix)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/083.png)

IV Diagram 4 shows a continuous IV order with an IV type of ‘Admixture’ that has one IV Additive (HEPARIN 25,000units) and one IV Solution that is not marked as a PreMix (D5W 250ml) to run at 10ml/hr. The Local Medication Route of ‘INTRAVENOUS’ assigned to the order is mapped to the Standard Medication Route of ‘INTRAVENOUS’. For this order a determination has to be made as to how the single dose amount and Dose Unit will be derived; using the IV Additive Strength or Drug Unit or using the formula. The order meets the criteria for making an inquiry to the FDB database to see if the drug associated with the IV Additive can be administered via a continuous FDB route.

In this case, the list of FDB dose routes that are returned for the dispense drug HEPARIN 10,000 UNT/ML 5ML VI which is associated with the IV Additive HEPARIN are: ‘continuous IV infusion’, ‘continuous intra-arterial infusion’, ‘intra-arterial’, ‘intravenous’, ‘intravesical’, and ‘subcutaneous’. The continuous FDB Dose route ‘continuous IV infusion’ is associated with the Standard Medication Route of ‘INTRAVENOUS’. The Local Medication Route, ‘INTRAVENOUS’ within the order, is mapped to the Standard Medication Route of ‘INTRAVENOUS’. Since there is a match, the single dose amount and Dose Unit will be derived using the formula.

For the Dosing Order Checks, the GCNSEQNO of ‘6544’ is identified by looking at the VA Product for the dispense drug that is associated with the IV Additive.

Using the formula:

(IV Additive Strength & Unit/Volume of IV Solution) \* Infusion rate (ML/HR) = Dose/Dose Rate

The calculation would be:

25,000 UNITS / 250 ML \* 10ML/HR = 1000 UNITS/HOUR

The single dose amount is calculated to be ‘1000’, the Dose Unit is the FDB equivalent of ‘UNITS’ which is ‘UNITS’ and the Dose Rate (which we have not yet discussed) is ‘HOUR’.

#### Single Dose Adjustments

In certain situations, IV Orders meeting specific criteria (i.e., having a frequency that requires rounding or if an IV bag infuses longer than the order duration), may require single dose adjustments. Let us look at some examples of IV orders that would require single dose adjustments when Dosing Order Checks are performed.

IV Example 5: IV Admixture of Folic Acid 1000mg (all bags) in 0.9% Sodium Chloride 1000ml to run 100ml/hr. Order to start 5/11@1500 and to end 5/11@2400.

IV Example 5 shows a continuous IV order with one IV Additive (FOLIC ACID) and IV Solution (0.9% SODIUM CHLORIDE) not marked as a PreMix with an order duration of 9 hours. One IV bag of fluids will run 10 hours (1000ML/100ML/HR). The dispense drug (FOLIC ACID 5MG/ML INJ) that is associated with the IV Additive has a VA Drug Class code of VT102. This IV order does not meet the criteria for querying the FDB database to see whether or not the drug is administered via a continuous FDB Dose Route. Normally in this situation, if the single bag of the IV order was able to complete before the order ended, we would have calculated the single dose amount from the IV Additive strength which would have been ‘1000’ and determined the FDB Dose Unit equivalent from looking up the drug unit ‘MG’ in the DOSE UNITS file. However, in this example, a single bag of the IV order will not complete before the order ends, so the single dose amount is adjusted to 900mg; the amount that will infuse over 10 hours.

As a general rule, if an IV order is processed through pharmacy backdoor options and meets the following criteria, the software will adjust the single dose amount sent into the interface of the IV Additive using the formula,

Adjusted Single Dose Amount (SDA) = (SDA/Volume of IV Solution) \* Infusion Rate (ML/HR) \* Duration of order (in hours)’:

- IV Order has an IV type of ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’, or ‘Chemotherapy Continuous Syringe’
- The IV Additive is NOT administered via a continuous FDB Dose Route
- Additive is to be administered in all IV bags
- Order duration is less than 24 hours
- Volume of solution (equivalent to ‘1’ bag dispensed) will not finish infusing over order duration

In IV Example 5, the dose of 900mg exceeds both the maximum single dose and maximum daily dose amounts and the user will see the warning messages displayed below. The user will also see a message preceding the warning. This message will inform the user that the single dose amount has been adjusted and the amount of fluid that will be administered over the duration of the order.

PLEASE NOTE: The single dose of the IV Additive has been adjusted to

reflect the amount of drug infused over the duration of the order or 24

hours; whichever is less (900 ML over 9 hours).

FOLIC ACID 1000 MG: Single dose of 900 milligrams exceeds the maximum

single dose of 5 milligrams.

FOLIC ACID 1000 MG: Total dose of 900 milligrams/day exceeds the maximum

daily dose of 5 milligrams/day.

IV Example 6: An IV Admixture of Folic Acid 1000mg in 0.9% Sodium Chloride 1000ml IV to infuse 62ml/hr.

IV Example 6 shows a continuous IV order with one IV Additive (FOLIC ACID) and IV Solution (0.9% SODIUM CHLORIDE) not marked as a PreMix. One IV bag of fluids will infuse over 16.12 hours (1000ML / 62ML/HR). The frequency is rounded to ‘16’ because the result is not a whole number. The dispense drug (FOLIC ACID 5MG/ML INJ) that is associated with the IV Additive has a VA Drug Class code of ‘VT102’. This IV order does not meet the criteria for querying the FDB database to see whether or not the drug is administered via a continuous FDB Dose route. Normally in this situation, if the frequency of administration of one IV fluid bag resulted in a whole number, we would have calculated the single dose amount from the IV Additive strength which would have been ‘1000’. However, in this example, the single dose amount is adjusted to 992mg; the amount that will infuse over 16 hours.

As a general rule, if an IV order is processed through pharmacy backdoor options and meets the following criteria, the software will adjust the single dose amount sent into the interface of the IV Additive using the formula,

‘Adjusted Single Dose Amount (SDA) = (SDA/Volume of IV Solution) \* Infusion Rate (ml/hr) \* Frequency value<sup>1</sup>’:

- Order has a IV type of ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’, or ‘Chemotherapy Continuous Syringe’
- The IV Additive is NOT administered via a continuous FDB Dose Route
- IV Solution Volume/Infusion Rate does not result in a whole number
- IV Additive is to be administered in all bags
- Order duration is greater or equal to 24 hours

<sup>1</sup>If the rounded frequency value of the IV order is less than 24, as in this case, the rounded frequency value will be used in the calculation. If the rounded frequency value of the IV order is equal to or greater than 24, the frequency value of ‘24’ shall be used in the calculation. The calculation would be:

(1000MG/1000ML) \* 62ML/HR \* 16 HR = 992MG

If Dosing Check warnings are generated, a message preceding the warning will be displayed to the user stating how much IV fluid volume was infused over the duration of the order. See example below.

PLEASE NOTE: The single dose of the IV Additive has been adjusted to

reflect the amount of drug infused over the nearest whole number of

hours (992 ML over 16 hours).

FOLIC ACID 1000 MG: Single dose of 992 milligrams exceeds the maximum

single dose of 5 milligrams.

FOLIC ACID 1000 MG: Total dose of 1,488 milligrams/day exceeds the

maximum daily dose of 5 milligrams/day.

Recommended frequency of FOLIC ACID 1000 MG: Frequency of 1.5

administrations per day exceeds the high frequency of 1 administration

per day.

### Dose Rate Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The value of the Dose Rate Unit will be determined by the software. It must be in terms of a ‘DAY’, ‘HOUR’ or ‘MINUTE’.

In almost all cases, for unit dose, outpatient and intermittent IV orders, the Dose Rate Unit will be set to ‘DAY’. Only continuous IV orders will use ‘HOUR’ or ‘MINUTE and only if the drug can be given via a continuous FDB Dose Route.

If the dose rate unit is undefined or invalid, an order level error message will be displayed to the user.

Dosing Checks could not be performed for Drug: HEPARIN 25000 UNITS/0.45% NACL 250 ML

Reason(s): Invalid or Undefined Dose Rate

### Dose Route (FDB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Dose Route represents the Local Medication Route specified within the order. The FDB dose route that the Local Medication Route is mapped to via the Standard Medication Route will be passed to the interface. Pharmacy Data Management (PDM) options have been provided for sites to map each Local Medication Route that is marked for ‘All Packages’ to an active Standard Medication Route. Reports have also been provided to review the mappings. See examples in the table below:

<u>Local Med Route</u> à mapped to <u>Standard Med Route</u> à mapped to <u>FDB Dose Route</u>

G TUBE ORAL ORAL

NASAL NASAL INTRANASAL

HHN NEBULIZATION NEBULIZATION

Example:

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/084.png)

The software will look at the Local Medication Route that is in the medication order and find the Standard Medication Route that it is mapped to. It will then look in the STANDARD MEDICATION ROUTES File to locate the equivalent FDB Dose Route to send to the interface.

If the Local Medication Route is not mapped, a Maximum Single Dose Order Check will not be performed. The user entering the order will be informed that the Maximum Single Dose Order Check was not performed, and the reason why as displayed below.

Dosing Checks could not be performed for Drug: GABAPENTIN 600MG TAB

Reason(s): Invalid or Undefined Dose Route

If a Local Medication Route cannot be mapped because a corresponding Standard Medication Route is not available, visit [New Term Rapid Turnaround (NTRT)](http://vista.med.va.gov/ntrt/) to request a new Standard Medication Route or change an existing one.

In some cases, a medication route may be selected for a drug order for which a vendor dosing record could not be found. In such a case, a DoseRouteDescription is NOT returned from FDB for a dosing check and an error/exception message is returned for either a Maximum Single Dose Order Check or for both Maximum Single Dose and Max Daily Dose Order Checks. The FDB route associated with the standard medication route that the local medication route in the order is mapped to will be inserted (CAPITALIZED) in the error/exception message text for display in Inpatient Medications, Outpatient Pharmacy applications and CPRS. This was done to indicate that the order route was responsible for the dosing check not to be performed. See examples below with inserted text bolded.

Backdoor Pharmacy

Maximum Single Dose Check could not be performed for Drug: KETOROLAC 10MG TAB

Reason(s) for INTRAMUSCULAR route: No dosing information specific to maximum single dose

is available from the database.

OR

Maximum Single Dose Check could not be performed for Drug: KETOROLAC 10MG TAB

Reason(s) for INTRAMUSCULAR route: No dosing information specific to maximum single dose

is available from the database.

Max Daily Dose Check could not be performed for Drug: KETOROLAC 10MG TAB

Reason(s) for INTRAMUSCULAR route: Unavailable

OR

Dosing Checks could not be performed for EPOETIN ALFA,RECOMBINANT 10000UNT/ML INJ

Reason(s) for ORAL route: FDB dosing information is not available for this drug.

CPRS

Dosing Checks could not be done for Drug: KETOROLAC 10MG TAB for INTRAMUSCULAR route, please complete a manual check for appropriate Dosing.

OR

Maximum Single Dose Check could not be done for Drug: KETOROLAC 10MG TAB for INTRAMUSCULAR route, please complete a manual check for appropriate Dosing.

There are two instances when the software automatically assigns a continuous FDB Dose Route when performing Dosing Order Checks. The first is when we have a continuous IV order with an IV type of either ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’, or ‘Chemotherapy Continuous Syringe’ and only one IV Solution marked as a PreMix is defined within the order.

The second is when we have a continuous IV order with an IV type of either ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’, or ‘Chemotherapy Continuous Syringe’ and one IV Additive and one IV Solution not marked as a PreMix is defined within the order. The dispense drug associated with the IV Additive does NOT have a VA Drug Class code assigned that starts with a ‘VT’ and can possibly be administered via a continuous FDB Dose Route.

If any IV order meets the second set of criteria above, the software queries the FDB database to get a list of all FDB Dose Routes for the dispense drug associated with the IV Additive. The software also checks whether the Local Medication Route specified for the IV order is mapped to one of the Standard Medication Routes in the table below. If yes, and the corresponding continuous FDB Dose Route in the table below is returned in the list of all FDB Dose Routes for the dispense drug associated with the IV Additive, the continuous FDB dose route associated with the Standard Medication Route will be sent into the interface for the Dosing Order Checks. The software makes this determination in the background; pharmacy users do not have to make any adjustments to their Local Medication Route mapping.

<u>STANDARD ROUTE</u><u>FDB DOSE ROUTE</u>

INTRA-ARTERIAL CONTINUOUS INTRA-ARTERIAL INFUSION

INTRATHECAL CONTINUOUS INTRATHECAL INFUSION

NEBULIZATION CONTINUOUS NEBULIZATION

SUBCUTANEOUS CONTINUOUS SUBCUTANEOUS INFUSION

EPIDURAL CONTINUOUS EPIDURAL

INTRAVENOUS CONTINUOUS IV INFUSION

INTRAOSSEOUS CONTINUOUS INTRAOSSEOUS INFUSION

INTRACAUDAL CONTINUOUS CAUDAL INFUSION

INFILTRATION CONTINUOUS INFILTRATION

ADDUCTOR CANAL BLOCK CONTINUOUS ADDUCTOR CANAL BLOCK

INFRACLAVICULAR CONTINUOUS INFRACLAVICULAR

INHALATION CONTINUOUS INHALATION

INTERSCALENE CONTINUOUS INTERSCALENE

INTRA-CATHETER INFUSION CONTINUOUS INTRA-CATHETER INFUSION

INTRAPERITONEAL INFUSION CONTINUOUS INTRAPERITONEAL INFUSION

INTRA-UMBILICAL VEIN INFUSION CONTINUOUS INTRA-UMBILICAL VEIN INFUSION

### Dose Type 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Dose Type is required for Dosing Order Checks to be performed. For all medication orders within VistA only two dose types will be used; Single Dose or Maintenance.

If the schedule type within a Unit Dose order is designated as one time or on call or a schedule within any type of medication order is designated as one time or on call, a Dose Type of ‘Single Dose’ will be sent into the interface.

All IV Orders assigned a continuous FDB Dose Route will be assigned a dose type of ‘Maintenance’.

For all other orders, a Dose Type of Maintenance will be sent into the interface. The software makes this determination in the background.

If a Dose Type is undefined or invalid; an error message will be generated and displayed to the user.

Dosing Checks could not be performed for Drug: GABAPENTIN 600MG TAB

Reason(s): Invalid or Undefined Dose Type

### Frequency 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The frequency represents the number of administrations per day. A frequency is needed to perform a Max Daily Dose Order Check. The single dose amount is multiplied by the frequency to provide the daily dose of a drug. The daily dose of the drug is then compared again the vendor max daily dose value for the drug. If the daily dose exceeds the max daily dose, a high dose warning is displayed to the user.

#### Fields Used to Determine Frequency

The frequency is derived from the VistA schedule associated with the order. For an outpatient medication order, the user can select from the ADMINISTRATION SCHEDULE file (#51.1), the MEDICATION INSTRUCTION file (#51) or can enter a free text value. For an inpatient medication order, the user can only select from the ADMINISTRATION SCHEDULE file (#51.1).

The following fields and in the order listed are used to lookup the schedule from a medication order.

- NAME field (#.01) in the ADMINISTRATION SCHEDULE file (#51.1)
- OLD SCHEDULE NAME(S) field (#13) multiple in the ADMINISTRATION SCHEDULE file (#51.1)
- NAME field (#.01) in the MEDICATION INSTRUCTION file (#51)
- SYNONYM field (#.5) in the MEDICATION INSTRUCTION file (#51)
- OLD MED INSTRUCTION NAME(S) field (#33) multiple in the MEDICATION INSTRUCTION file (#51)

  There are a couple of fields in both the Administration Schedule file and the Medication Instruction file that can be used to derive a frequency from a schedule/medication instruction within an order in the sequence listed below.

ADMINISTRATION SCHEDULE File (#51.1)

- DOSING CHECK FREQUENCY field (#11)
- DRUG(S) FOR DOSING CHK FREQ field (#11.1) – multiple
- FREQUENCY (IN MINUTES) field (#2)

MEDICATION INSTRUCTION File (#51)

- DOSING CHECK FREQUENCY field (#32)
- DRUG(S) FOR DOSING CHK FREQ field (#32.1) – multiple
- FREQUENCY (IN MINUTES) field (#31)

The DOSING CHECK FREQUENCY and DRUG(S) FOR DOSING CHK FREQ fields are only used for Dosing Order Checks, specifically the Max Daily Dose Order Check. These fields should be defined in those situations when the FREQUENCY (IN MINUTES) field does not adequately represent the number of administrations of a drug per a 24-hour period or does not allow for a successful Max Daily Dose Order Check to be performed.

FDB v4.5 Upgrade updated the logic used by the FREQUENCY (IN MINUTES) and the DOSING CHECK FREQUENCY fields. The DOSING CHECK FREQUENCY fields are now subject to additional formatting logic.

> Q#H \[every \# hour(s), values supported for '#': 1-12, 14-24, 30, 36, 48, 60, 72 and 96

> Q#D \[every \# day(s), values supported for '#': 1-10, 14, 21, 28, 30, 56 and 90

> Q#W \[every \# week(s), values supported for '#': 1-6, 8-10, 12, 16, 24 and 52

> Q#L \[every \# month(s), values supported for '#': 1-4, 6 and 12

> \#XD \[times per day, values supported for '#': 1-99

> \#XW \[times per week, values supported for '#': 1-6

The FREQUENCY (IN MINUTES) field generally converts to a whole number or a valid DOSING CHECK FREQUENCY value with limited exceptions. The FREQUENCY (IN MINUTES) values that are able to be converted are indicated in the Dosing Checks column in the following table. Example: FREQUENCY (IN MINUTES) 60 equals 24. If the FREQUENCY (IN MINUTES) cannot be converted, populating the DOSING CHECK FREQUENCY field is recommended to enable order checks to occur.

Table of valid FREQUENCY (IN MINUTES)

| FREQUENCY (IN MINUTES) | Frequency used in Dosing Checks |
|----------------------------|-------------------------------------|
| 60                         | 24                                  |
| 120                        | 12                                  |
| 180                        | 8                                   |
| 240                        | 6                                   |
| 300                        | Q5H                                 |
| 360                        | 4                                   |
| 420                        | Q7H                                 |
| 480                        | 3                                   |
| 540                        | Q9H                                 |
| 600                        | Q10H                                |
| 660                        | Q11H                                |
| 720                        | 2                                   |
| 840                        | Q14H                                |
| 900                        | Q15H                                |
| 960                        | Q16H                                |
| 1020                       | Q17H                                |
| 1080                       | Q18H                                |
| 1140                       | Q19H                                |
| 1200                       | Q20H                                |
| 1260                       | Q21H                                |
| 1320                       | Q22H                                |
| 1380                       | Q23H                                |
| 1440                       | 1                                   |
| 1800                       | Q30H                                |
| 2160                       | Q36H                                |
| 2880                       | Q2D                                 |
| 3600                       | Q60H                                |
| 4320                       | Q3D                                 |
| 5760                       | Q4D                                 |
| 7200                       | Q5D                                 |
| 8640                       | Q6D                                 |
| 10080                      | Q1W                                 |
| 11520                      | Q8D                                 |
| 12960                      | Q9D                                 |
| 14400                      | Q10D                                |
| 20160                      | Q2W                                 |
| 30240                      | Q3W                                 |
| 40320                      | Q4W                                 |
| 43200                      | Q1L                                 |
| 50400                      | Q5W                                 |
| 60480                      | Q6W                                 |
| 80640                      | Q8W                                 |
| 86400                      | Q2L                                 |
| 90720                      | Q9W                                 |
| 100800                     | Q10W                                |
| 120960                     | Q12W                                |
| 129600                     | Q3L                                 |
| 161280                     | Q16W                                |
| 172800                     | Q4L                                 |
| 241920                     | Q24W                                |
| 259200                     | Q6L                                 |
| 518400                     | Q12L                                |
| 524160                     | Q52W                                |
| 525600                     | Q12L                                |

Let us look at a couple of examples.

Frequency Example 1: Frequency Value is less than ‘1’

A drug is administered every 72 hours or every 3 days. Before MOCHA v2.1a was released, the only field available to define a frequency was the FREQUENCY (IN MINUTES) field. A user would enter the value ‘4320’. The frequency is computed by dividing the ‘4320’ into ‘1440’. The result is ‘0.33’. The frequency value sent into the interface for the Max Daily Dose Order Check can only be a whole number. Since the FREQUENCY (IN MINUTES) field was the only field available to define frequency, the Max Daily Dose Order Check could not be performed. The new DOSING CHECK FREQUENCY field allows a numeric frequency value to be represented by a free text format. A schedule or medication instruction of every 72 hours or every 3 days can be represented by the free text formats, ‘Q3D’ or ‘Q72H’. The free text formats can be sent into the interface for the Dosing Order Check so that the Max Daily Dose Order Check is successful.

Frequency Example 2: Every 5 Minutes for 3 Doses

The FREQUENCY (IN MINUTES) field only allows one to enter a value based on a 24 hour period. If a value of ‘5’ minutes is entered, the frequency is determined by computing ‘1440/5’. The resultant value of ‘288’ administrations per 24 hours is a big difference from the desired ‘3’ administrations per 24 hours. One of the free text formats that is allowed for the DOSING CHECK FREQUENCY field is ‘#XD’ which allows one to enter a numeric value for ‘#’ to convey the number of administrations per day. The numeric value must be a whole number. In this case, we can set the DOSING CHECK FREQUENCY field to ‘3XD’ which would represent ‘3’ administrations as the frequency for the Max Daily Dose Order Check instead of ‘288’.

If the DOSING CHECK FREQUENCY field is used to convey a dose limit, there is no need to place a dose limit on the order in order for the Max Daily Dose Order Check to be performed accurately. If a dose limit is placed on the order and the DOSING CHECK FREQUENCY field has a value for the ‘#XD’ format, the value in the DOSING CHECK FREQUENCY file will be used for the frequency to perform the Max Daily Dose Order Check.

Frequency Example 3: Schedule to Represent Two Different Frequency Values

This is not a scenario that you will see that often, but in some cases a schedule may be used for two different inpatient medication orders with different drugs that convey different frequency values. Let us look as such a schedule. One order is for WARFARIN 5MG PO MO-WE-FR@17 and the other order is for EPOETIN 10,000 units SQ MO-WE-FR@17. For both orders the schedule is the same. We want the frequency value to be ‘1’ for Warfarin and the frequency value to represent three times per week for the Epoetin. In the Administration Schedule file, the MO-WE-FR@17 is setup as displayed below.

NAME: MO-WE-FR@17 STANDARD ADMINISTRATION TIMES: 17

PACKAGE PREFIX: PSJ TYPE OF SCHEDULE: DAY OF THE WEEK

OUTPATIENT EXPANSION: MONDAY, WEDNESDAY AND FRIDAY AT 5PM

DOSING CHECK FREQUENCY: 3XW

DRUG(S) FOR DOSING CHK FREQ: EPOETIN ALPHA 40,000 U/ML INJ

DRUG(S) FOR DOSING CHK FREQ: EPOETIN ALPHA 10,000 U/ML INJ

The entry has the standard administration times of ‘17’ defined. The dosing check frequency is set to ‘3XW’. This free text format allows one to specify how many times per week a drug in administered. If the schedule within the order has a schedule type of Day of the Week (DOW) the FREQUENCY (IN MINUTES) field will not have a value. Two drugs are defined for the DRUG(S) FOR DOSING CHK FREQ field; Epoetin Alpha 40,000 u/ml Inj and Epoetin Alpha 10,000 u/ml Inj. It is important that all dispense drugs tied to the same Orderable Item are defined for this field so that the Max Daily Dose Order Check is successfully performed through CPRS. In this case only 2 dispensed drugs are assigned to the Orderable Item, and both are defined for the DRUG(S) FOR DOSING CHK FREQ field.

For a Day of the Week schedule found in the Administration Schedule file for an inpatient medication order, the DOSING CHECK FREQUENCY field is first checked for a value. If no value is found, the number of administration times defined in the order is used to define the frequency. If there is a value found in the DOSING CHECK FREQUENCY field, the DRUG(S) FOR DOSING CHK FREQ field is checked. If there are dispense drugs defined, a check is made to see if the drug in the order matches one of the dispense drugs defined. If it does, the value in the DOSING CHECK FREQUENCY field is used to derive the frequency. If no dispense drugs are defined, the frequency is set to the number of administration times defined in the order.

The warfarin 5mg order does not match either of the two EPOETIN dispense drugs defined in the DRUG(S) FOR DOSING CHK FREQ field, so the value in the DOSING CHECK FREQUENCY field is not used for the frequency. The frequency is set to the number of administration times in the order. There is one administration time defined for the inpatient medication order because there was one administration time defined for the schedule. The frequency value will be set to ‘1’ for the Max Daily Dose Order Check.

For the EPOETIN 10,000 u/ml Inj order, since the drug in the order matches one of the drugs defined in the DRUG(S) FOR DOSING CHK FREQ field, the frequency will be set to the value in the DOSING CHECK FREQUENCY field which is ‘3XW’ and represents ‘three times per week’ to be used for the Max Daily Dose Order Check.

Since the schedule was defined appropriately, the frequency for each order was assigned correctly and the Max Daily Dose Order Check will be successfully performed for both inpatient medication orders.

#### Frequency Check Logic for Inpatient Medication Orders

A diagram depicting the logic of how a frequency is derived for an Inpatient Medication Order is shown in Appendix E. In this section we will take a look at each type of schedule and see how the frequency is derived.

#### One-Time or On Call Schedules

As shown in the Frequency Diagram 1 below, if the schedule type for a schedule within an order is set to ONE-TIME or ON CALL, the frequency will be set to ‘1’ for an Inpatient Medication order.

<span id="_Toc197085150" class="anchor"></span>Frequency Diagram 1: One-Time, On Call, and DOW Schedules

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/085.png)

#### Day of the Week (DOW) Schedules

If a schedule within an inpatient medication order (unit dose or intermittent IV order) is not found in the Administration Schedule file, but is identified as a DOW (based on format), the frequency will be set to the number of administration times defined in the order as shown in Frequency Diagram 1.

If the schedule type is found in the Administration Schedule file and the schedule type is set to ‘Day of the Week’, as shown in Frequency Diagram 1, the software first checks to see if there is a value in the DOSING CHECK FREQUENCY field. If no value is found, the frequency is set to the number of administration times defined in the order. If a value is found, a check is made to see if any dispense drugs are defined in the DRUG(S) FOR DOSING CHK FREQ field. If no drugs are defined, the frequency is set to the value in the DOSING CHECK FREQUENCY field. If there are dispense drugs defined, and one of the drugs matches the drug in the order with that schedule, the frequency is set to the value in the DOSING CHECK FREQUENCY field. If no matches are made, the frequency is set to the number of administration times defined in the order.

#### Continuous and PRN Schedules

Looking at Frequency Diagram 2, for a schedule found in the Administration Schedule file with a schedule type of ‘Continuous’, the software first checks the DOSING CHECK FREQUENCY field for a value. If no value is found, a check is made to see if a value exists in the FREQUENCY (IN MINUTES) field. If a value is found in the DOSING CHECK FREQUENCY field, the DRUG(S) FOR DOSING CHK FREQ field is checked to see if any dispense drugs have been defined. If no dispense drugs have been defined, the frequency is set to the value in the DOSING CHECK FREQUENCY field. If dispense drugs have been defined and one matches the drug in the inpatient medication order, the frequency will be set to the value in the DOSING CHECK FREQUENCY field. If none of the dispense drugs defined match the drug in the inpatient medication order the software checks if a value exists in the FREQUENCY (IN MINUTES) field.

If no value is found in the FREQUENCY (IN MINUTES) field, the Max Daily Dose Order Check cannot be performed successfully. If there is a value found, a calculation is done by dividing the value in the FREQUENCY (IN MINUTES) field into ‘1440’ to derive the frequency. If the result is a whole number, the frequency value will be set to that value. If the result is not a whole number, the software will attempt to express the numeric value using free text formats such as ‘QXH’ or ‘QOD’. If not successful, the Max Daily Dose Order check will not be performed. If successful, that free text format will be set to the frequency.

For schedules with a schedule type of ‘PRN’, the logic that occurs to derive a frequency is the same as a schedule with a schedule type of ‘Continuous’. However, PRN schedules do not have a value in the FREQUENCY (IN MINUTES) field. So if there is no value defined in the DOSING CHECK FREQUENCY, the software will check the FREQUENCY (IN MINUTES) field, which for PRN schedule will not have a value. According to Frequency Diagram 2, if no value is found in the FREQUENCY (IN MINUTES) field, a frequency cannot be derived and the Max Daily Dose Order Check cannot be performed. What is not depicted in the diagram is that for a PRN schedule if a frequency cannot be determined, the software will strip the ‘\<space\> PRN’ from the schedule name with a schedule type of ‘PRN’ and run the ‘NEW’ schedule name through the frequency logic in Frequency Diagram 2. If a frequency can be determined, that frequency will be used for the Max Daily Dose Order Check.

<span id="_Toc197085151" class="anchor"></span>Frequency Diagram 2: Continuous and PRN Schedules

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/086.png)

#### Miscellaneous Business Rules on Frequency Determination

Let us visit some other business rules that determine/alter the frequency that is derived from an Inpatient Medication order.

For continuous IV orders where a ‘continuous FDB dose route’ (i.e., Continuous IV Infusion) is sent in for Dosing Order Checks, the frequency will always be set to 1. In all other cases for continuous IV orders, the infusion rate is used to determine how many IV bags will be administered over a 24 hour period. The frequency will be set to the number of IV bags. If an IV additive is administered in less than ‘All’ bags, such as ‘1 bag/day’, the frequency will set to the number of IV bags the IV Additive will be placed in.

For a very specific scenario through the pharmacy backdoor, if the following criteria are met, the frequency will be rounded and expressed in a ‘Q#H’ format:

- Has IV type of ‘Admixture’, ‘Hyperal’, or ‘Chemotherapy Admixture’
- The IV Additive is NOT administered via a ‘CONTINUOUS’ FDB Dose Route
- IV Solution volume/Infusion Rate does not result in a whole number
- IV Additive is NOT placed in all IV bags
- Number of IV bags specified for IV Additive is greater than the number of IV bags to be administered in a 24-hour period for the IV Order.

If a limit is placed on an inpatient order that affects how much drug is given for a 24 order period, the frequency will be adjusted for the Max Daily Dose Order Checks. Some examples follow.

Frequency Example 4: Ibuprofen 600mg Q4H for 12 hours

For a unit dose order, if the duration of the order is less than 24 hours (1 day), the frequency will be determined by how many doses are ordered. Only 3 doses of Ibuprofen 600mg will be administered in 24 hours. The frequency will be set to ‘3’ and NOT ‘6’.

Frequency Example 5: Intermittent IV - Gentamicin 100mg in 5% Dextrose 100ml Q6H with a duration limit of 2 doses.

For an IV intermittent fluid order entered through CPRS, even though the schedule for the order is Q6H which equates to a frequency of ‘4’, a duration limit for 2 doses was indicated. The frequency will be set to ‘2’ and not ‘4’.

Frequency Example 6: Continuous IV - Folate 500mg in 0.9% Sodium Chloride 500ml to infuse 125ml/hr with volume limit of 500ml.

For this continuous IV order through CPRS, even though the infusion rate is 125ml/hr which would equate to 6 of the 500ml IV bags infusing over a 24-hour period, the frequency in this case would be set to ‘1’ and not ‘6’.

#### Frequency Check Logic for Outpatient Medication Orders

Diagrams depicting the logic of how a frequency is derived for an outpatient medication order are show in Appendix F and Appendix G. In this section we will take a look at each type of schedule and see how the frequency is derived.

#### One-Time or On Call Schedules

As shown in the Frequency Diagram 3 below, if the schedule type for a schedule within an order is set to ONE-TIME or ON CALL, the frequency will be set to ‘1’ for an Outpatient medication order.

<span id="_Toc197085152" class="anchor"></span>Frequency Diagram 3: One-Time, On Call, and DOW not in Administration Schedule File

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/087.png)

#### Day of the Week (DOW) not in Administration Schedule File

Looking at Frequency Diagram 3, if a schedule within an outpatient medication order is not found in the Administration Schedule file, but is identified as a DOW (contains a ‘@’) the value after the ‘@’ is evaluated. If no value is found after the ‘@’ sign, the frequency is set to ‘1’. If there are administration times defined after the ‘@’ sign, the frequency is set to the number of administration times. If there is text defined after the ‘@’ sign, the text will be run through the frequency logic as if it were a schedule starting with the Administration Schedule file, then the Medication Instruction file and then treated as Free Text.

#### Schedule Type = Day of the Week (DOW)

As shown in Frequency Diagram 4, if the schedule within an outpatient medication order is found in the Administration Schedule file, and the schedule type is set to ‘Day of the Week’, the DOSING CHECK FREQUENCY field is checked for a value. If no value exists, and administration times exist for the schedule, the frequency will be set to the number of administration times defined for the schedule. If no administration times are defined for the schedule, the FREQUENCY (IN MINUTES) field is checked for a value.

If there was a value in the DOSING CHECK FREQUENCY field, a check is made to see if any drugs have been defined for the DRUG(S) FOR DOSING CHK FREQ field. If none have been assigned, the frequency is set to the value in the DOSING CHECK FREQUENCY field for all orders that have that schedule. If drugs have been defined for the DRUG(S) FOR DOSING CHK FREQ field, a check is made as to whether they match the drug in the order. If one of the drugs defined match the drug in the order, the frequency is set to the value in the DOSING CHECK FREQUENCY field. If none of the drug(s) defined match the drug in the order, the FREQUENCY (IN MINUTES) field is checked for a value.

<span id="_Toc197085153" class="anchor"></span>Frequency Diagram 4: DOW Schedule Found in Administration Schedule File

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/088.png)

If a value exists in the FREQUENCY (IN MINUTES) field, a calculation is made by dividing ‘1440’ by the FREQUENCY (IN MINUTES) value. If the result is a whole number, the frequency is set to the result. If the result is not a whole number, the software checks if the value can be expressed as the free text format of ‘QOD’ or ‘Q#H’, where ‘#’ represents a whole number. If the resultant value cannot be expressed as the free text formats of ‘QOD’ or ‘Q#H’, an error message is displayed indicating that the Max Daily Dose Order Check could not be performed. If the resultant value can be expressed as one of the free text formats, the frequency is set to that free text format. If no FREQUENCY (IN MINUTES) value exists, the software will see if the schedule can be found in the MEDICATION INSTRUCTION FILE.

If the schedule is found in the MEDICATION INSTRUCTION file, the logic to derive a frequency is similar to a schedule found in the Administration Schedule file. The only difference is that if the frequency is not set to an existing DOSING CHECK FREQUENCY field value or the DOSING CHECK FREQUENCY field value does not exist, the next check is whether a value in the FREQUENCY (IN MINUTES) field exists instead of looking for administration times. Administration times cannot be defined for a medication instruction.

#### Continuous and PRN Schedules

As depicted in Frequency Diagram 5, for a schedule type of continuous or PRN in an outpatient medication order, the frequency logic is the same. Regardless of whether the schedule is found in the Administration Schedule file or the Medication Instruction File, the first check is whether a value is found in the DOSING CHECK FREQUENCY field. If a value is not found in the DOSING CHECK FREQUENCY field, the software checks the FREQUENCY (IN MINUTES) field. If a value is found in the DOSING CHECK FREQUENCY field, the next field checked is the DRUG(S) FOR DOSING CHK FREQ field. If no dispense drugs are defined, the frequency is set to the value in the DOSING CHECK <span id="Page_72" class="anchor"></span>FREQUENCY field for all outpatient medication orders that have that schedule or medication instruction. If dispense drugs are defined and one matches the drug in the outpatient medication order, the frequency is set to the value in the DOSING CHECK FREQUENCY field. If no drug matches a check is made to see if a value is in the FREQUENCY (IN MINUTES) field. If a value is found a calculation is performed. The value in the FREQUENCY (IN MINUTES) is divided into ‘1440’. If the result is a whole number, the frequency is set to that whole number. If the result is not a whole number, the software checks if the value can be expressed as the free text format of ‘QOD’ or “QXH’. If it can, the free text format is set as the frequency. If not, an error message is displayed to the user indicating that the Max Daily Dose Order Check could not be performed. If there was no value in the FREQUENCY (IN MINUTES) field, the schedule is treated as free text. Again the software checks if the value can be expressed as the free text format of ‘QOD’ or “QXH’. If so, the free text format is set as the frequency. If not, an error message is displayed to the user indicating that the Max Daily Dose Order Check could not be performed.

<span id="_Toc197085154" class="anchor"></span>Frequency Diagram 5: Continuous and PRN Schedule Frequency Logic

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/089.png)

As stated above, for schedules with a schedule type of ‘PRN’, the logic that occurs to derive a frequency is the same as a schedule with a schedule type of ‘Continuous’. However, PRN schedules do not have a value in the FREQUENCY (IN MINUTES) field. So if there is no value defined in the DOSING CHECK FREQUENCY, the software will check the FREQUENCY (IN MINUTES) field, which for PRN schedule will not have a value. According to Frequency Diagram 5, if no value is found in the FREQUENCY (IN MINUTES) field, a frequency cannot be derived and the Max Daily Dose Order Check cannot be performed. What is not depicted in the diagram is that for a PRN schedule if a frequency cannot be determine, the software will strip the ‘\<space\> PRN’ from the schedule name with a schedule type of ‘PRN’ and run the ‘NEW’ schedule name through the frequency logic in Frequency Diagram 5. If a frequency can be determined, that frequency will be used for the Max Daily Dose Order Check.

#### Miscellaneous Business Rules for Frequency Determination

Let us visit some business rules that determine/alter the frequency that is derived from an Outpatient Medication order.

If a limit is placed on an outpatient order that affects how much drug is given for a 24 order period, the frequency will be adjusted for the Max Daily Dose Order Checks. Some examples follow.

Frequency Example 7: Ibuprofen 600mg Q4H for 12 hours

For an outpatient order, if the duration of the order is specified as 12 hours, the frequency will be determined by how many doses are ordered. Only 3 doses of Ibuprofen 600mg will be administered in 12 hours. The frequency will be set to ‘3’ and NOT ‘6’.

If the schedule entered for an order cannot be found as a whole in either the ADMINISTRATION SCHEDULE (#51.1) file or the MEDICATION INSTRUCTION (#51) file, the schedule will be broken down using a \<space\> as a delimiter and each word looked up in the ADMINISTRATION SCHEDULE (#51.1) file and if not found then looked up in the MEDICATION INSTRUCTION (#51) file. The following rules will be used to derive the frequency:

- If only one frequency value is found for any of the words in either file, that frequency value will be used.
- If multiple frequency values are found, but the values are the same, that value will be used for the frequency.
- If multiple frequency values are found, but the values are not the same, none of the values will be used and an error displayed to the user that the Max Daily Dose Order Check could not be performed.
- Only schedules marked as Pharmacy use will be used to determine the frequency value.
- If more than one schedule is found and at least one of the schedules is marked as ONE-TIME or ON CALL, the frequency will be set to ‘1’ and only a Maximum Single Dose Order Check will be performed.
- If more than one schedule is found and at least one of the schedules is marked as DAY OF THE WEEK, and no value is found in the DOSING CHECK FREQUENCY field, the day of the week logic shall be used to determine the frequency value.

### Duration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The duration is a numeric representation in terms of a specific duration rate (i.e. HOUR, DAY, etc.) that a dosing regimen is administered. For Dosing Order Checks, dosing periods greater than one (1) day are not being evaluated. For Dosing Order Checks, the duration of ‘1’ is always sent into the interface.

### Duration Rate Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The duration rate unit will always have the same value as the dose rate unit. Please see 2.5.4 Dose Rate Unit for specifics.

## Custom Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### General Dosing Information Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under certain conditions when Dosing Order Checks are performed, a general dosing information message will be displayed to the user that provides a normal dosing range (high and low values) for the drug and route prescribed. In addition to a normal dosing range, a max daily dose for the drug is also provided if available. Whenever possible, the normal dosing range and max daily dose values will be represented in the dose units that were derived from the dosage ordered. If a Local Possible Dosage is selected during order entry for a medication order, and that Local Possible Dosage has a defined numeric dose and dose unit, the dose unit that is mapped to the Local Possible Dosage shall be used for the General Dosing Information message.

The general dosing information message will be composed from the following information:

- Drug Name
- Dose Route
- Low Dose
- High Dose
- Max Daily Dose

#### Drug Name

The Drug Name in the General Dosing Information (GDI) message will be represented by the following formats in CPRS:

- The Dispense Drug Name for an Outpatient or Inpatient Medications (UD) order if a Dispense Drug is assigned to the order.
- The Dispense Drug Name for an Outpatient or Inpatient Medications (UD) order if there is only one Dispense Drug assigned to the Orderable Item.
- The Orderable Item Name and Dosage Form for an Outpatient or Inpatient Medications (UD) order if a Dispense Drug is NOT assigned to the order and there is more than one Dispense Drug assigned to the Orderable Item.
- The Orderable Item Name, Dosage Form, Strength, and Drug Unit for an IV Additive within an IV Fluid order.
- The Orderable Item Name, Dosage Form, and Volume for an IV Solution (Premix) within an IV Fluid order.

The Drug Name in the General Dosing Information (GDI) message will be represented by the following formats in Pharmacy backdoor options:

- The Dispense Drug Name for an Outpatient medication order.
- The Dispense Drug Name for a Unit Dose (UD) order with a single Dispense Drug.
- The Orderable Item Name and Dosage Form for a Unit Dose (UD) order with multiple Dispense Drugs.
- The IV Additive Print Name, Strength, and Drug Unit for an IV Additive within an IV order.
- The IV Solution Print Name (1) and Volume for an IV Solution (Premix) within an IV order.

#### Dose Route

In some cases, a dosing record not specific to any route or dose type may be used for the Dosing Order Check when no route specific dosing records exist. In other cases, no dosing records at all can be found in the vendor database. When either situation occurs, a general dosing information message will not be displayed to the user. No high dose warnings will be displayed that result from the use of a dosing record not specific to any route or dose type for the Dosing Order Check.

If the Dose Route sent into the interface is a FDB Continuous Route, the FDB Continuous Route will be displayed in the general dosing information message. For more detailed information on FDB Continuous Routes please refer to section 2.6.5 Dose Route (FDB) of this manual.

General dosing range for HEPARIN 20000 UNITS \*PREMIXED\* 500 ML

(CONTINUOUS IV INFUSION): 0.3 milliliter/kilogram/hour to 0.45

milliliter/kilogram/hour. Maximum dose rate is 0.6125

milliliter/kilogram/hour.

OR

General dosing range for CEFAZOLIN 100 GM (CONTINUOUS IV INFUSION):

1.875 milligram/kilogram/hour to 4.167 milligram/kilogram/hour. Maximum

dose rate is 666.67 milligram/hour.

#### Low and High Dose/Max Daily Dose

If the low and high dose values returned from the vendor database are the same, the dosing information message will display the maximum single dose and maximum daily dose value.

CLOPIDOGREL 75MG TAB: Single dose of 750 milligrams exceeds the maximum  
single dose of 75 milligrams.  

 

CLOPIDOGREL 75MG TAB: Total dose of 1,500 milligrams/day exceeds the  
maximum daily dose of 75 milligrams/day.

For each drug, two values the low and high dose are returned based on the dose unit defined in the vendor dosing record. The DOSE FORM INDICATOR field (#3) in the DOSE UNITS file (#51.24) is used to determine which values will be displayed in the general dosing information message for not only the low and high dose values, but also the max daily dose.

#### When is General Dosing Information Displayed?

A general dosing information message will be displayed when the following conditions are met:

- Max Daily Dose Order Check cannot be performed.

Max Daily Dose Check could not be performed for Drug: GABAPENTIN

(GRALISE) 600MG SA TAB

     Reason(s): Invalid or Undefined Frequency

General dosing range for GABAPENTIN (GRALISE) 600MG SA TAB (ORAL): 300

milligram/day to 1800 milligram/day. Maximum daily dose is 1800

milligram/day. 

- Both Maximum Single Dose and Max Daily Dose Order Checks cannot be performed.

Dosing Checks could not be performed for Drug: GABAPENTIN (GRALISE)

600MG SA TAB

     Reason(s): Free Text Dosage could not be evaluated

General dosing range for GABAPENTIN (GRALISE) 600MG SA TAB (ORAL): 300

milligram/day to 1800 milligram/day. Maximum daily dose is 1800

milligram/day. 

- Maximum Single Dose Order Check results in a high dose warning for a simple medication order <u>and</u> the schedule within the order is excluded from the Max Daily Dose Order Check.

HALOPERIDOL 10MG S.T.: Single dose of 60 milligrams exceeds the maximum

single dose of 40 milligrams.

General dosing range for HALOPERIDOL 10MG S.T. (ORAL): 0.25

milligram/day to 100 milligram/day. Maximum daily dose is 100

milligram/day.

- Maximum Single Dose Order Check for a simple medication order cannot be performed <u>and</u> the schedule within the order is excluded from the Max Daily Dose Order Check.

Maximum Single Dose Check could not be performed for Drug: GENTAMICIN

40MG/ML 20ML M.D.V.

Reason(s): Weight is required.

General dosing range for GENTAMICIN 40MG/ML 20ML M.D.V. (INTRAMUSCULAR):

1.5 milligram/kilogram/day to 7 milligram/kilogram/day. Maximum daily

dose is 7 milligram/kilogram/day.

A general dosing information message will NOT be displayed under the following conditions:

- If a schedule from the ADMINISTRATION SCHEDULE file (#51.1) is selected for a medication order and the type of schedule is designated as ONE-TIME OR ON CALL, the dose type will be set to ‘Single Dose’.
- Dosing Order Check results in a FDB message that is returned with a severity of ‘Not Screened’ or ‘Warning’.
- A DoseRouteDescription is not returned from the Dosing Order Check.
- When a free text dosage is entered through CPRS for a multi-ingredient product where the derived dose unit is a dose form type for which a dispense drug cannot be determined; more than one dispense drug is associated with the orderable item; and none of the dosing order check exclusion criteria apply.

## Frequency Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to FDB v4.5 Upgrade, a VistA created frequency message was displayed. After the implementation of FDB v4.5 Upgrade now displays the FDB generated frequency messages. Some examples are shown below:

Recommended frequency of ZZMETFORMIN 500MG: Frequency of 12 administrations

per day exceeds the frequency range of 1 to 2 administrations per day.

Recommended frequency of NITROGLYCERIN PATCHES 0.1MG/HR: Frequency of 2

administrations per day exceeds the high frequency of 1 administration per day. 

Recommended frequency of RISPERIDONE 25MG/VIL INJ,SUSP,SA: Frequency of

every 21 days is below the low frequency of every 14 days. 

Recommended frequency of RISPERIDONE 25MG/VIL INJ,SUSP,SA: Frequency of 12

administrations per day exceeds the high frequency of every 14 days

Recommended frequency of AMIODARONE 200MG TAB: Frequency of every 21 days

is below the frequency range of 3 administrations per day to 2 times every

7 days. 

Recommended frequency of AMIODARONE 200MG TAB: Frequency of 12

administrations per day exceeds the frequency range of 3 administrations

per day to 2 times every 7 days.

The frequency message can be displayed as the lone dosing message. You can also see it displayed with high dose warnings or ‘cannot be performed’ messages. Let us look at a couple of examples.

<span id="_Toc180596932" class="anchor"></span>Frequency Diagram 6: High Dose Warnings and Frequency Message

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/090.png)

Frequency Diagram 6 is an example of the frequency message being displayed with two high dose warnings. No general dosing information message is displayed because this scenario does not meet the four scenarios for the General dosing information message display.

<span id="_Toc180596933" class="anchor"></span>Frequency Diagram 7: Frequency Message with Error Message and GDI Message

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/091.png)

In Frequency Diagram 7, the drug’s frequency low and high values are less than 1 and the order frequency is greater than 1. VistA could not perform the Max Daily Dose (MDD) Order Check (OC) because a weight was required and one was not documented for the patient. A ‘could not be performed’ message is displayed with the reason. A general dosing information message is also displayed.

<span id="_Toc180596934" class="anchor"></span>Frequency Diagram 8: Frequency Message Only

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/092.png)

In Frequency Diagram 8, the only order check messaging is for the recommended frequency. The vendor performs both the Maximum Single Dose Order Check and the Max Daily Dose Order Check and VistA displays the result which in this case is nothing because both dosing checks passed.

Frequency Diagram 9: Frequency Screening Not Performed

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/093.png)

In Frequency Diagram 9, VistA could not perform the Max Daily Dose (MDD) Order Check (OC) because the Single Dose exceeds the Maximum Single Dose Order Check. VistA displays the error message and reason. The recommended frequency screening was not performed because the prescribed dose can only be screened with a frequency of once. When the low frequency and high frequency both equal one, the daily frequency of one is expected.

## Pharmacogenomic Order Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v3.0 implemented Pharmacogenomic (PGx) Order Checks, providing additional guidance for selecting suitable drug therapies based on genomic factors and indicators. This assists clinicians in delivering safe and effective treatment options tailored to individual patients

To perform the Pharmacogenomic Order Checks, the system first retrieves the patient’s pharmacogenomic lab results which are stored in HDR, regardless of where they were drawn. Results are retrieved at the time the order is accepted in CPRS or being processed in VistA. If the HDR server or the MOCHA server are not able to connect, a corresponding message will be displayed to the user.

Pharmacogenomic order checks levels of severity:

- High order checks require an override by the provider and an intervention by the pharmacist
- Medium order check overrides or interventions are optional.
- Screen Message displays when additional information or testing needs to be provided to perform a PGx order check. This can occur when the PGx order check cannot be completed due to uninterpretable gene or phenotype results, even though the vendor database contains genomic findings and PGx guidance exists for the prospective drug.

At the time of entering or processing the order, the user can display ‘Additional Information’ for the ‘High’ and ‘Medium” PGx order checks to see the order check content as well as the sources and references returned from the vendor.

Only VA Products that are marked as PGx Eligible in the National Drug File are eligible for PGx Order checks.

PGx order checks are not rechecked when the order is edited, unless the dispense drug field is edited.

An email notification to the PBM PGx CDS group is sent when an HDR-retrieved gene or phenotype cannot be mapped to the FDB gene database. The Pharmacogenomic Email Log (File \#51.29) will store the pertinent information. If an order is entered or processed for that specific patient with the same unresolved gene or unresolved or null phenotype greater than 7 days from the last email, another email and log will be sent.

Suppression of Pharmacogenomic Order Checks may occur at the following 2 levels:

- Profile suppression occurs if the ingredient for the prospective order is set to PGx Eligible and PGx Suppress, the severity of the PGx order check is Medium (Informational), and the patient has an active local orders in the following conditions:
  - Inpatient Order being placed: Active inpatient profile order (Unit Dose, Clinic Meds, IV or Clinic Infusion) or outpatient profile order (with the following statuses: active, hold, provider hold, suspended, active/parked or expired within the last 90 days) for a drug with the same ingredient as the prospective drug. NOTE: Non-VA medications and remote profile orders are NOT included for suppression logic.
  - Outpatient Order being placed: Active outpatient profile order with one of the following statuses: active, hold, provider hold, suspended, active/parked, or expired (within the last 90 days) for a drug with the same ingredient as the prospective drug. NOTE: Non-VA medications, inpatient profile orders and remote profile orders are NOT included for suppression logic.
- Severity and PGx Action Category Suppression occurs if the severity of the order check is Medium (Informational) and the PGx Action Category is one of the following:
  - 9 – No therapy adjustment needed
  - 14 – No therapy recommendation
  - 2 – Await genotype test result
  - 4 – Consider genotype test or prescribe alternative
  - 13 – Consider genotype test
  - 5 – Order genotype test or prescribe alternative
- ![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/094.png) Please refer to the MOCHA FAQs for more detailed information.

<span id="_Toc206596795" class="anchor"></span>Example 20: PGx HIGH Order Check, intervention required

> Pharmacogenomic HIGH Order Check:

> GENOMIC FINDING: CYP2D6 poor metabolizer

> IMPACTED MEDICATION: AMITRIPTYLINE 100MG

> ACTION: For conditions requiring higher starting doses (e.g., 25 mg/day or

> higher) such as depression, consider alternate drug with less dependence on

> CYP2D6 metabolism (e.g., citalopram, sertraline). If amitriptyline use is

> warranted, consider a 50% reduction of the standard starting dose and use

> therapeutic drug monitoring to guide subsequent dose adjustment.

> MONITORING: If using amitriptyline, monitor for symptom improvement as well as

> adverse reactions (e.g., anticholinergic, central nervous system, and cardiac

> effects).

> For more details on VA National Pharmacogenomics Program go to:

> [[<u>https://bit.ly/VA-PGx</u>](https://bit.ly/VA-PGx)](https://bit.ly/VA-PGx)

> Display Additional Information on Pharmacogenomic Order Check(s)? NO// YES

> DEVICE: HOME// Linux Telnet /SSh

> Pharmacogenomics Detailed Information

> GENOMIC FINDING: CYP2D6 poor metabolizer

> IMPACTED MEDICATION: AMITRIPTYLINE 100MG

> SEVERITY LEVEL: HIGH

> EVIDENCE RATINGS:

> SOURCE: Clinical Pharmacogenetics Implementation Consortium (CPIC)

> (1,2)

> RATING: Strong

> SOURCE: Dutch Pharmacogenetics Working Group (DPWG) (3)

> RATING: 3, A

> ACTION:

> For conditions requiring higher starting doses (e.g., 25 mg/day or higher)

> such as depression, consider alternate drug with less dependence on CYP2D6

> metabolism (e.g., citalopram, sertraline). If amitriptyline use is

> warranted, consider a 50% reduction of the standard starting dose and use

> therapeutic drug monitoring to guide subsequent dose adjustment.

> Type \<Enter\> to continue or '^' to exit:

> RATIONALE:

> Greatly reduced amitriptyline metabolism results in higher concentrations of

> active drug and increased risk of adverse reactions.

> MONITORING:

> If using amitriptyline, monitor for symptom improvement as well as adverse

> reactions (e.g., anticholinergic, central nervous system, and cardiac

> effects).

> CITATIONS:

> \(1\) Hicks JK, Sangkuhl K, Swen JJ, et al. Clinical Pharmacogenetics

> Implementation Consortium Guideline (CPIC) for CYP2D6 and CYP2C19 Genotypes

> and Dosing of Tricyclic Antidepressants: 2016 update. Clinical Pharmacology

> and Therapeutics. 2017 Jul 01; 102 (1): 37-44. Available from

> [[<u>https://cpicpgx.org/content/guideline/publication/TCA/2016/TCA_2016.pdf</u>](https://cpicpgx.org/content/guideline/publication/TCA/2016/TCA_2016.pdf)](https://cpicpgx.org/content/guideline/publication/TCA/2016/TCA_2016.pdf)

> \(2\) Clinical Pharmacogenetics Implementation Consortium (CPIC). CPIC Guideline

> for Tricyclic Antidepressants and CYP2D6 and CYP2C19. Available from

> [[<u>https://cpicpgx.org/guidelines/guideline-for-tricyclic-antidepressants-and-cyp2d</u>](https://cpicpgx.org/guidelines/guideline-for-tricyclic-antidepressants-and-cyp2d)](https://cpicpgx.org/guidelines/guideline-for-tricyclic-antidepressants-and-cyp2d)

> 6-and-cyp2c19/

> \(3\) Dutch Pharmacogenetics Working Group. Pharmacogenomics guidelines.

> Type \<Enter\> to continue or '^' to exit:

> Available from

> [[<u>https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf</u>](https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf)](https://www.knmp.nl/downloads/farmacogenetica-engels-recommendation-tekst.pdf)

> First Databank database updated on 07/02/2025.

> Do you want to Continue with AMITRIPTYLINE 100MG? NO// Y

<span id="_Toc206596796" class="anchor"></span>Example 21: PGx MEDIUM Order Check, no intervention required

> Pharmacogenomic MEDIUM Order Check:

> GENOMIC FINDING: CYP2D6 intermediate metabolizer

> IMPACTED MEDICATION: TRAMADOL HCL 100MG TAB

> ACTION: Initiate therapy with usual recommended starting dose. If there is

> poor therapeutic response, consider alternative analgesic such as morphine or

> a nonopioid. Codeine and hydrocodone are also affected by CYP2D6 polymorphisms

> and may not be suitable alternatives.

> MONITORING: Monitor for analgesic response.

> For more details on VA National Pharmacogenomics Program go to:

> https://bit.ly/VA-PGx

> Display Additional Information on Pharmacogenomic Order Check(s)? NO//

> Do you want to Intervene with TRAMADOL HCL 100MG TAB ? NO//

> Press Return to continue...

# Order Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v2.0 implemented a Maximum Single Dose Order Check for simple and complex medication orders. MOCHA v2.1b implemented the Max Daily Dose Order Check for simple medication orders only. During order entry both Dosing Order Checks will be performed for simple orders, while only the Maximum Single Dose Order Check will be performed for complex orders with other existing order checks when the pharmacy user takes various order entry actions.

### New Simple Medication Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the example below, a new simple outpatient medication order is entered through the pharmacy backdoor and generates a Maximum Single Dose Order Check warning.

Entering a new simple outpatient medication order

Medication Profile Sep 30, 2011@09:39:39 Page: 1 of 1

\<A\>

Ht(cm): 165.10 (04/19/2017)

DOB: MAY 1,1955 (56) Wt(kg): 77.27 (04/19/2017)

SEX: MALE CrCL: 33.2(est.) (CREAT: 1.5mg/dL 4/19/17) BSA (m2): 1.85

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

This patient has no prescriptions

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// NO New Order

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 60

RX PATIENT STATUS: OPT NSC//

DRUG: GABA

Lookup: GENERIC NAME

GABAPENTIN 600MG TAB CN900

...OK? Yes// (Yes)

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

VERB: TAKE

There are 2 Available Dosage(s):

1\. 600MG

2\. 1200MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2400MG 2400MG

You entered 2400MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 4// 4

Dosage Ordered: 2400MG

NOUN: TABLETS

ROUTE: ORAL// ORAL

Schedule: TID (THREE TIMES A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Press Return to continue,'^' to exit:

GABAPENTIN 600MG TAB: Single dose of 2,400 milligrams exceeds the maximum

single dose of 1,200 milligrams.

GABAPENTIN 600MG TAB: Total dose of 9,600 milligrams/day exceeds the

maximum daily dose of 3,600 milligrams/day.

Recommended frequency of GABAPENTIN 600MG TAB: Frequency of 4

administrations per day exceeds the frequency range of 1 to 3

administrations per day.

After the pharmacy user bypasses the conjunction prompt, Dosing Order Checks will be performed. If the dosage ordered exceeds the FDB recommended maximum single dose and/or maximum daily dose, warning message(s) will be displayed to the user for the appropriate Dosing Order Check. The warning message(s) will be indented, and the drug name will precede the message(s).

Do you want to Continue? Y// ES

Do you want to Process or Cancel medication?

GABAPENTIN 600MG TAB: P// CANCEL MEDICATION

RX DELETED

Another New Order for ? YES//

\*\*\*\*\*\*\*\*\*\*\*OR\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

GABAPENTIN 600MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for GABAPENTIN 600MG TAB

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

.

.

. \*\*\*\*\*\*\*\*\*\*\*OR\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

.

.

Do you want to Continue? Y// N NO

RX DELETED

Another New Order for ? YES//

If a Maximum Single Dose Order Check and/or Max Daily Dose Order Check warning is displayed, the user will be prompted with ‘Do you want to Continue?’ If the user accepts the default of ‘Yes’, the program will prompt the user if they wish to Process or Cancel the medication order. If the user decides to ‘Cancel’ the medication order, the order is deleted. If the user takes the default to ‘Process’, the program proceeds with the intervention dialog. A user will always be required to log an intervention if the dosage has been exceeded. The intervention type is set to ‘MAX SINGLE DOSE’ if only a Maximum Single Dose Order Check warning is displayed. The intervention type is set to ‘MAX DAILY DOSE’ if only a Max Daily Dose warning is displayed. If both a Maximum Single Dose Order Check and Max Daily Dose warning are displayed, the intervention type is set to ‘MAX SINGLE DOSE & MAX DAILY DOSE’.

If a user does not hold the ‘PSORPH’ key, he/she will not be asked to enter an intervention. The program will just continue on with the order entry dialog.

If an error message is displayed because the Maximum Single Dose Order Check, Max Daily Dose or both Dosing Order Checks could not be performed, the user will not be asked to enter an intervention to continue.

If the schedule within the order has been marked to be excluded from all Dosing Order Checks, no Dosing Order Checks will be performed. If the schedule within the order has been marked to be excluded from the Daily Dose Check, no Max Daily Dose Order Check will be performed although the Maximum Single Dose Order Check will be done. In either case, no message will be displayed to the user informing them that both Dosing Order Checks, or just the Max Daily Dose Order Check were not performed.

If the user responds ‘No’ to the ‘Do you want to Continue?’ prompt, the order will be deleted.

### New Complex Medication Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the example below, a new complex outpatient medication order with four dosing sequences is entered. Three of the dosing sequences will generate a Maximum Single Dose Order Check warning. A Max Daily Dose will not be performed on any of the dosing sequences within the complex order. A future version of MOCHA will implement the Max Daily Dose Order Check for complex orders.

Entering a new complex Outpatient Medication order

Another New Order for ? YES//

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 60

RX PATIENT STATUS: OPT NSC//

DRUG: HALOPERIDOL

Lookup: GENERIC NAME

1 HALOPERIDOL 10MG S.T. CN709

2 HALOPERIDOL 1MG S.T. CN709

3 HALOPERIDOL 20MG TAB CN709

4 HALOPERIDOL 2MG S.T. CN709

5 HALOPERIDOL 5MG S.T. CN709

Press \<RETURN\> to see more, '^' to exit this list, '^^' to exit all lists, OR

CHOOSE 1-5: 3 HALOPERIDOL 20MG TAB CN709

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

VERB: TAKE

There is 1 Available Dosage(s):

1\. 20MG

Select from list of Available Dosages (1-1), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 40MG 40MG

You entered 40MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 2// 2

Dosage Ordered: 40MG

NOUN: TABLETS

ROUTE: ORAL// ORAL

Schedule: QAM

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QAM QAM EVERY MORNING

...OK? Yes// (Yes)

(EVERY MORNING)

<span id="Page_66" class="anchor"></span>LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION: AND

VERB: TAKE

There is 1 Available Dosage(s):

1\. 20MG

Select from list of Available Dosages (1-1), Enter Free Text Dose

or Enter a Question Mark (?) to view list: xxx xxx

You entered xxx is this correct? Yes// YES

VERB: TAKE

Schedule: QNOON

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

Now searching MEDICATION INSTRUCTION (#51) file...

Free text 'QNOON' entered for schedule (QNOON)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION: a AND

Maximum Single Dose Check could not be performed for Drug: HALOPERIDOL

20MG TAB

Reason(s): Free Text Dosage could not be evaluated

VERB: TAKE

There is 1 Available Dosage(s):

1\. 20MG

Select from list of Available Dosages (1-1), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 60MG 60MG

You entered 60MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 3// 3

Dosage Ordered: 60MG

NOUN: TABLETS

Schedule: QPM

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QPM QPM EVERY EVENING

...OK? Yes// (Yes)

(EVERY EVENING)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION: AND

Press Return to continue,'^' to exit:

HALOPERIDOL 20MG TAB: Single dose of 60 milligrams exceeds the maximum

single dose of 40 milligrams.

Do you want to Continue? Y// ES

VERB: TAKE

There is 1 Available Dosage(s):

1\. 20MG

Select from list of Available Dosages (1-1), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 80MG 80MG

You entered 80MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 4// 4

Dosage Ordered: 80MG

NOUN: TABLETS

Schedule: QHS

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QHS QHS AT BEDTIME

...OK? Yes// (Yes)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Press Return to continue,'^' to exit:

HALOPERIDOL 20MG TAB: Single dose of 80 milligrams exceeds the maximum

single dose of 40 milligrams.

After the pharmacy user bypasses the conjunction prompt, a Maximum Single Dose Order Check will be performed as we saw with a simple order in the previous example. For complex orders, a Maximum Single Dose Order Check will be performed on each individual dosing sequence.

If a Maximum Single Dose Order Check warning is displayed, the user will be prompted with ‘Do you want to Continue?’ This prompt will be displayed for every dosing sequence that generates a Maximum Single Dose Order Check warning. If the user takes the default of ‘Yes’ and a value has been entered for the conjunction, the program will continue with entry of the next dosing sequence.

If an error message is displayed because the Maximum Single Dose Order Check could not be performed, the user will not be prompted with ‘Do you want to Continue?’ for that specific dosing sequence.

If the user responds ‘No’ to any of the ‘Do you want to Continue?’ prompts for any of the dosing sequences that generated a dosage warning while entering the complex order, the order will be deleted at that point.

No Maximum Single Dose Order Check will be performed for a dosing sequence within a complex outpatient medication order that contains a schedule that has been excluded from all Dosing Order Checks. No message will be displayed to the user informing them that a Maximum Single Dose Order Check will not be performed for that dosing sequence.

DOSING CHECK SUMMARY:

DOSE SEQ 2:

Maximum Single Dose Check could not be performed for Drug: HALOPERIDOL

20MG TAB

Reason(s): Free Text Dosage could not be evaluated

DOSE SEQ 3:

HALOPERIDOL 20MG TAB: Single dose of 60 milligrams exceeds the maximum

single dose of 40 milligrams.

DOSE SEQ 4:

HALOPERIDOL 20MG TAB: Single dose of 80 milligrams exceeds the maximum

single dose of 40 milligrams.

Press Return to continue,'^' to exit:

Do you want to Continue? Y// ES

Do you want to Process or Cancel medication?

HALOPERIDOL 20MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Press Return to continue,'^' to exit:

Now creating Pharmacy Intervention

<span id="Page_68" class="anchor"></span>for HALOPERIDOL 20MG TAB

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

PATIENT INSTRUCTIONS:

For a complex order, if the number of dosing sequences is greater than three (3), a summary of error messages, and/or warning messages will be redisplayed after the last dosing sequence has been entered. Each error message/warning will be preceded by a dosing sequence indicator to remind the user entering the order for which dosing sequence the error or warning occurred.

Once all dosing sequences have been entered for the complex order, and assuming the user takes the default of ‘Yes’ for all dosing sequences that may have generated a Maximum Single Dose warning, the program will proceed with the intervention dialog after the last dosing sequence has been entered and any warnings, error messages or dosing summary is displayed.

If the user chooses to ‘Cancel’ the order instead of processing the medication order, the medication order will be deleted.

A pharmacist will always be asked to log an intervention if at least one of the dosing sequences within the complex order has generated a Maximum Single Dose Order Check warning for a dose that has exceeded the recommended dose in the FDB database. Only one pharmacy intervention will be required to be logged if multiple Maximum Single Dose warnings are displayed. The intervention type shall be set to ‘MAX SINGLE DOSE’.

As with a simple order, if a user does not hold the ‘PSORPH’ key, he/she will not be asked to enter an intervention. The program will just continue on with the order entry dialog.

### Finishing a Pending Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example below illustrates finishing a pending outpatient order that was entered through CPRS that will generate several different order checks including a Maximum Single Dose warning.

Finishing a Pending Order

Medication Profile Sep 30, 2011@12:21:58 Page: 1 of 1

\<A\>

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 100002147 GABAPENTIN 600MG TAB 360 A 09-30 09-30 5 30

2 100002148 WARFARIN 10MG TAB 30 A 09-30 09-30 5 30

------------------------------------PENDING-------------------------------------

3 ASPIRIN 325MG TAB QTY: 100 ISDT: 09-30 REF: 1

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//3

Pending OP Orders (ROUTINE) Sep 30, 2011@12:22:33 Page: 1 of 3

\<A\>

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

CPRS Order Checks:

Duplicate Therapy: Order(s) exist for {WARFARIN 10MG TAB \[ACTIVE\]} in the

same therapeutic categor(ies): Antiplatelet and Antithrombotic Drugs

Overriding Provider: PROVIDER,ONE

Overriding Reason: TESTING

ASPIRIN 325MG TAB: Single dose of 3,250 milligrams exceeds the maximum

single dose of 2,000 milligrams.

Overriding Provider: PROVIDER,ONE

Overriding Reason: TESTING

ASPIRIN 325MG TAB: Total dose of 19,500 milligrams/day exceeds the maximum

daily dose of 8,000 milligrams/day.

Overriding Provider: PROVIDER,ONE

Overriding Reason: TESTING

SIGNIFICANT drug-drug interaction: ASPIRIN TAB and WARFARIN 10MG TAB

\[ACTIVE\] - The concurrent use of anticoagulants and salicylates may result

in increased INR values and increase the risk of bleeding. - Monograph

\+ Enter ?? for more actions

BY Bypass DC Discontinue FL Flag/Unflag

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

-------------------------------------------------------------------------------

\*\*\*Significant\*\*\* Drug Interaction with Prospective Drug:

ASPIRIN 325MG TAB and

Local RX#: 100002148

Drug: WARFARIN 10MG TAB (Active)

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Processing Status: Not released locally (Window)

Last Filled On: 09/30/11

\*\*\* Refer to MONOGRAPH for SIGNIFICANT INTERACTION CLINICAL EFFECTS

Display Interaction Monograph? No// NO

Do you want to Intervene? Y// NO

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* ASPIRIN 325MG TAB with

Local RX#: 100002148

Drug: WARFARIN 10MG TAB (Active)

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

QTY: 30 Days Supply: 30

Processing Status: Not released locally (Window)

Last Filled On: 09/30/11

Class(es) Involved in Therapeutic Duplication(s): Antiplatelet and

Antithrombotic Drugs, Antiplatelet and Antithrombotic Drugs (Selected

Group 2)

===============================================================================

Press Return to continue:

Discontinue Rx \#100002148 WARFARIN 10MG TAB Y/N ? <u>NO</u>

===============================================================================

ASPIRIN 325MG TAB: Single dose of 3,250 milligrams exceeds the maximum

single dose of 2,000 milligrams.

ASPIRIN 325MG TAB: Total dose of 19,500 milligrams/day exceeds the maximum

daily dose of 8,000 milligrams/day.

Do you want to Continue? Y// ES

Do you want to Process or Cancel medication?

ASPIRIN 325MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for ASPIRIN 325MG TAB

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

Rx \# 100002149 09/30/11

\#100

TAKE TEN TABLETS BY MOUTH EVERY 4 HOURS

ASPIRIN 325MG TAB

PROVIDER,ONE PHARMACIST,ONE

\# of Refills: 1

SC Percent: 60%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? NO//

Upon selection of the pending order for Aspirin 325mg Tab to finish, the Dosing Order Checks displayed to the provider during order entry via CPRS have been added to the ‘CPRS Order Checks’ section of the screen. When the user selects to finish the order, several order checks are generated; a Drug Interaction, Duplicate Therapy and Dosing Order Checks. We see that the Drug Interaction between Aspirin and Warfarin was displayed first, followed by the Duplicate Therapy Order Check between Aspirin and Warfarin and lastly the Maximum Single Dose Order Check warning and the Max Daily Dose Order Check warning.

Dosing Order Checks will be performed with all other order checks when the user takes the following actions on an outpatient medication order:

- Finish
- Renew
- Copy
- Reinstate
- Verify (PSORPH key holders only)

Dosing Order Checks will be the last order checks displayed to the user.

If the user responds ‘No’ to the ‘Do you want to Continue?’ prompt after the Maximum Single Dose Order Check warning is displayed, the user will be returned to the order screen where the action was initiated. In this case the user is returned to the Pending order screen as shown below.

If the user takes the default of Yes when finishing a simple order, a pharmacist will be forced to log an intervention.

### Editing an Order 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example illustrates editing of a dosage for an order which results in a number of order checks being generated.

Editing an Order

OP Medications (ACTIVE) Sep 30, 2011@13:21:06 Page: 1 of 2

\<A\>

PID: Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 55696

\(1\) \*Orderable Item: WARFARIN TAB (2) Drug: WARFARIN 10MG TAB

\(3\) \*Dosage: 10 (MG)

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL (BY MOUTH)

\*Schedule: QPM

(4)Pat Instructions:

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

\+ Enter ?? for more actions

DC Discontinue PR Partial RL Release

ED Edit RF Refill RN Renew

Select Action: Next Screen// 3

VERB: TAKE

There is 1 Available Dosage(s):

1\. 10MG

Select from list of Available Dosages (1-1), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 10MG// 40 40MG

You entered 40MG is this correct? Yes// YES

VERB: TAKE// TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 4// 4

Dosage Ordered: 40MG

NOUN: TABLETS// TABLETS

ROUTE: ORAL (BY MOUTH)// ORAL (BY MOUTH)

Schedule: QNOON// QPM

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QPM QPM EVERY EVENING

...OK? Yes// (Yes)

(EVERY EVENING)

LIMITED DURATION (IN MONTHS, WEEKS, DAYS, HOURS OR MINUTES):

CONJUNCTION:

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press return to continue:

-------------------------------------------------------------------------------

\*\*\*Significant\*\*\* Drug Interaction with Prospective Drug:

WARFARIN 10MG TAB and

Local RX#: 100002151

Drug: ASPIRIN BUFFERED 325MG TAB (Non-Verified)

SIG: TAKE TEN TABLETS BY MOUTH EVERY 4 HOURS

Processing Status: Not released locally (Window)

Last Filled On: 09/30/11

\*\*\* Refer to MONOGRAPH for SIGNIFICANT INTERACTION CLINICAL EFFECTS

Display Interaction Monograph? No// NO

Do you want to Intervene? Y// NO

===============================================================================

\*\*\* THERAPEUTIC DUPLICATION(S) \*\*\* WARFARIN 10MG TAB with

Local RX#: 100002150

Drug: ASPIRIN 325MG TAB (Discontinued)

SIG: TAKE 3000MG BY MOUTH EVERY 4 HOURS

QTY: 100 Days Supply: 30

Processing Status: Not released locally (Window)

Last Filled On: 09/30/11

-------------------------------------------------------------------------------

Local RX#: 100002151

Drug: ASPIRIN BUFFERED 325MG TAB (Non-Verified)

SIG: TAKE TEN TABLETS BY MOUTH EVERY 4 HOURS

QTY: 1800 Days Supply: 30

Processing Status: Not released locally (Window)

Last Filled On: 09/30/11

Class(es) Involved in Therapeutic Duplication(s): Antiplatelet and

Antithrombotic Drugs, Antiplatelet and Antithrombotic Drugs (Selected Group 2

===============================================================================

Press Return to continue:

Discontinue Rx \#100002151 ASPIRIN BUFFERED 325MG TAB Y/N ? NO

===============================================================================

New OP Order (ROUTINE) Sep 30, 2011@13:19:27 Page: 1 of 2

\<A\>

PID: Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

Orderable Item: WARFARIN TAB

\(1\) Drug: WARFARIN 10MG TAB

\(2\) Patient Status: OPT NSC

\(3\) Issue Date: SEP 30,2011 (4) Fill Date: SEP 30,2011

\(5\) Dosage Ordered: 40 (MG)

Verb: TAKE

Dispense Units: 4

Noun: TABLETS

Route: ORAL (BY MOUTH)

Schedule: QPM

(6)Pat Instruction:

SIG: TAKE FOUR TABLETS BY MOUTH EVERY EVENING

\(7\) Days Supply: 30 (8) QTY ( ): 30

\(9\) \# of Refills: 5 (10) Routing: WINDOW

\+ This change will create a new prescription!

AC Accept ED Edit

Select Action: Next Screen// AC Accept

WARFARIN 10MG TAB: Single dose of 40 milligrams exceeds the maximum single

dose of 20 milligrams.

WARFARIN 10MG TAB: Total dose of 40 milligrams/day exceeds the maximum

daily dose of 20 milligrams/day.

Do you want to Continue? Y//

Do you want to Process or Cancel medication?

WARFARIN 10MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for WARFARIN 10MG TAB

PROVIDER:

Dosing Order Checks will be performed when the following fields are edited in an order:

- Orderable Item
- Dispense Drug
- Dosage Ordered
- Dispense Units per Dose
- Route
- Schedule
- Conjunction (if complex order)

Dosing Order Checks will be performed after the user accepts a simple medication order after all edits have been made. If there are any other order checks generated such as Drug Interactions or Duplicate Therapy, they will be displayed before the user accepts the order.

If editing a complex order, all error messages and/or Maximum Single Dose Order Check warnings will be displayed all at one time after all changes are made and the user accepts the order.

### Renewing an Order 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example illustrates renewing an outpatient medication order for a drug that requires a patient weight in order to perform the Maximum Single Dose Order Check. An error message is generated.

Renewing an Order

OP Medications (ACTIVE)       May 26, 2022@09:15:48          Page:    1 of    3

XXXXXXXXX,XXXXXXXX

  PID: XXX-XX-XXXX                                 Ht(cm): 172.72 (03/11/2022)

  DOB: JAN 1,1950 (72)                             Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)  

  SEX: MALE                           

  CrCL: \<Not Found\> (CREAT: Not Found)           BSA (m2): \_\_\_\_\_\_\_

                                                                                

                Rx \#: BUSO\$                                                     

 (#) \*Orderable Item: BUSULFAN TAB                                             

 (#)            Drug: BUSULFAN 2MG TAB                                         

 (2)             NDC: 00081-0713-25                                             

 (3)         \*Dosage: 2 (MG)                                                   

                Verb: TAKE                                                     

      Dispense Units: 1                                                         

                Noun: TABLET                                                   

              \*Route: ORAL (BY MOUTH)                                          

           \*Schedule: BID-NOON                                                  

 (4)Pat Instructions:                                                          

                 SIG: TAKE ONE TABLET BY MOUTH BID-NOON                     
+         Enter ?? for more actions                                            

DC   Discontinue          PR   Partial              RL   Release

ED   Edit                 RF   Refill               RN   Renew

Select Action: Next Screen// RN   Renew 

FILL DATE:  (MAY 26, 2022-MAY 27, 2023): TODAY//   (MAY 26, 2022)

MAIL/WINDOW: WINDOW// WINDOW

Nature of Order: WRITTEN//        W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No//   NO

Now Renewing Rx \# BUSO   Drug: BUSULFAN 2MG TAB

--------------------------------------------------------------------------------

                            \*\*\*\*\* WARNING \*\*\*\*\*

     BUSULFAN is hazardous to handle and dispose. Please notify

     pharmacy staff and counsel patient to take the appropriate handling and

     disposal precautions.

--------------------------------------------------------------------------------

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please wait...

   Dosing Checks could not be performed for Drug: BUSULFAN 2MG TAB

     Reason(s): Weight is required. 

   General dosing range for BUSULFAN 2MG TAB (oral): 0.26 milligram/day to

   4 milligram/kilogram/day. Maximum daily dose is 4

   milligram/kilogram/day. 

<span id="Page_75" class="anchor"></span>In the previous example, the patient does not have a height or weight defined. During the renewal process, an order level error message is generated telling the user that both Dosing Order Checks could not be performed because a weight is required. In addition to the error message, a general dosing information message is displayed for the drug which includes the drug’s normal dosage range and the max daily dose in milligrams per kilogram per day. After the error message and general dosing information for the drug are displayed, the order dialog continues on. The user is not asked if they wish to continue as they would be if a warning was displayed. The user is not required to enter an intervention.

### Copying an Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example illustrates copying an outpatient medication order. The Local Medication Route in the order is mapped to a Standard Medication Route that is not associated with an FDB Dose Route assigned to the drug being acted upon.

Copying an Order

Another New Order for ? YES//

Eligibility: SC LESS THAN 50% SC%: 30

RX PATIENT STATUS: SC//

DRUG: CAPSA

Lookup: GENERIC NAME

CAPSAICIN 0.025% PATCH DE650

...OK? Yes// (Yes)

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

VERB: APPLY

There are 2 Available Dosage(s):

1\. 1 PATCH

2\. 2 PATCHES

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2 2 PATCHES

You entered 2 PATCHES is this correct? Yes// YES

VERB: APPLY

ROUTE: TOPICAL//TRANSDERMAL

Schedule: QPM// QDAILY

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QDAILY QDAILY EVERY DAY

...OK? Yes// (Yes)

(EVERY DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Press Return to continue,'^' to exit:

Dosing Checks could not be performed for Drug: CAPSAICIN 0.025% PATCH

Reason(s) for TRANSDERMAL route: No dosing information is available from

the database.

PATIENT INSTRUCTIONS: //

The Local Medication Route of ‘TRANSDERMAL’ is mapped to the Standard Medication Route of ‘TRANSDERMAL’. The Standard Medication Route of ‘TRANSDERAML’ is mapped to a FDB Dose Route of ‘TRANSDERMAL’. The reason the error message is generated is because there are no FDB dosing records for CAPSAICIN 0.025% PATCH with a ‘TRANSDERMAL’ dose route.

If a different Local Medication Route of ‘TOPICAL’ which is mapped to the Standard Medication Route of ‘TOPICAL’ is assigned to this drug order for which FDB dosing records exist, a Dosing Order Checks will be performed. The Standard Medication Route of ‘TOPICAL’ is mapped to a FDB Dose Route of ‘TOPICAL’ and FDB dosing records exist for this drug under that dose route.

Another New Order for ? YES//

Eligibility: SC LESS THAN 50% SC%: 30

RX PATIENT STATUS: SC//

DRUG: CAPSA

Lookup: GENERIC NAME

CAPSAICIN 0.025% PATCH DE650

...OK? Yes// (Yes)

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

VERB: APPLY

There are 3 Available Dosage(s):

1\. 1 PATCH

2\. 2 PATCHES

3\. 5 PATCHES

Select from list of Available Dosages (1-3), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 3 5 PATCHES

You entered 5 PATCHES is this correct? Yes// YES

VERB: APPLY

ROUTE: TRANSDERMAL// TOPICAL

Schedule: QPM// QDAILY

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

QDAILY QDAILY EVERY DAY

...OK? Yes// (Yes)

(EVERY DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Press Return to continue '^' to exit:

CAPSAICIN 0.025% PATCH: Single dose of 5 patches exceeds the maximum single

dose of 1 patch.

CAPSAICIN 0.025% PATCH: Total dose of 5 patches/day exceeds the maximum

daily dose of 4 patches/day.

Do you want to Continue? Y// NO

RX DELETED

The previous example illustrates the need for a new PDM option brought in with MOCHA v2.0 called *Lookup Dosing Check Info for Drug* \[PSS DRUG DOSING LOOKUP\]. This new option displays dosing information for a drug that may affect whether Dosing Order Checks will be performed or can be performed. One piece of information provided is the FDB Dose Routes used for the drug selected. In this case, had we looked up the drug CAPSAICIN 0.025% PATCH it would have displayed that the FDB Dose Route used is ‘TOPICAL’.

### Discontinuing an Active Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Order checks including Dosing Order Checks are not performed when discontinuing an active order.

### Reinstate an Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following two examples illustrate reinstating an order. This can be done in two ways, using the DC action within the Patient Prescription Processing option on a discontinued order or by using the Discontinue Prescription(s) option.

#### DC Action on Discontinued Order

The following example, as explained in Section 3.1.8, is shown below.

DC Action on Discontinued Order

OP Medications (DISCONTINUED) Dec 18, 2012@13:46:19 Page: 1 of 2

PID: Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 10,1944 (68) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

Rx \#: 3363

\(1\) \*Orderable Item: DIGOXIN TAB

\(2\) Drug: DIGOXIN 0.25MG

\(3\) \*Dosage: 0.75 (MG)

Verb: TAKE

Dispense Units: 3

Noun: TABLETS

\*Route: ORAL

\*Schedule: QAM

(4)Pat Instructions:

SIG: TAKE THREE TABLETS BY MOUTH EVERY MORNING

\+ Enter ?? for more actions

DC Discontinue PR (Partial) RL Release

ED Edit RF (Refill) RN Renew

Select Action: Next Screen// DC Discontinue

Are you sure you want to Reinstate? NO// YES

Comments: DISCONTINUED IN ERROR

Nature of Order: SERVICE CORRECTION// S

================================================================================

3363 DIGOXIN 0.25MG TAB

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

DIGOXIN 0.25MG: Single dose of 0.75 milligrams exceeds the maximum single

dose of 0.5 milligrams.

DIGOXIN 0.25MG: Total dose of 0.75 milligrams/day exceeds the maximum daily

dose of 0.5 milligrams/day.

Do you want to Continue? Y//

Do you want to Process or Cancel medication?

DIGOXIN 0.25MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

<span id="Page_79" class="anchor"></span>Now creating Pharmacy Intervention

for DIGOXIN 0.25MG TAB

PROVIDER: PROVIDER, ONE PROVIDER,ONE OP

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

Prescription \#3363 REINSTATED!

Prescription \#3363:

Filled: DEC 18, 2012 Printed: Released:

Either print the label using the reprint option

or check later to see if the label has been printed.

Press Return to continue...:

Medication Profile Dec 18, 2012@13:47:58 Page: 1 of 1

PID: Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 10,1944 (68) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 3363 DIGOXIN 0.25MG TAB 270 A 12-18 12-18 3 90

2 3361 FOLIC ACID 1MG TAB 90 A 12-18 12-18 3 90

----------------------------------DISCONTINUED----------------------------------

3 3362 GABAPENTIN 600MG TAB 1080 DC 12-18 12-18 3 90

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

#### Discontinue Prescription(s) Option

The following example, as explained in Section 3.1.8, is shown below.

Discontinue Prescription(s) Option

Select Rx (Prescriptions) \<TEST ACCOUNT\> Option: discontinue Prescription(s)

Discontinue/Reinstate by Rx# or patient name: (R/P): r RX NUMBER

Discontinue/Reinstate Prescription(s)#: 3363 DIGOXIN 0.25MG TAB

RX: 3363 PATIENT:

STATUS: Discontinued

DRUG: DIGOXIN 0.25MG TAB

QTY: 270 90 DAY SUPPLY

SIG: TAKE THREE TABLETS BY MOUTH EVERY MORNING

<span id="Page_80" class="anchor"></span> LATEST: 12/18/2012 \# OF REFILLS: 3 REMAINING: 3

ISSUED: 12/18/12 PROVIDER:

LOGGED: 12/18/12 CLINIC: NOT ON FILE

EXPIRES: 12/19/13 DIVISION: HINES (499)

CAP: SAFETY ROUTING: WINDOW

ENTRY BY: PROVIDER,ONE VERIFIED BY:

FILLED: 12/18/12 PHARMACIST: LOT \#:

DISPENSED: 12/18/12 RELEASED:

ACTIVITY LOG:

\# DATE REASON RX REF INITIATOR OF ACTIVITY

===============================================================================

1 12/18/12 DISCONTINUED ORIGINAL RPH, ONE

COMMENTS: demonstration

ACTIVITY LOG:

\# DATE REASON RX REF INITIATOR OF ACTIVITY

===============================================================================

2 12/18/12 REINSTATE ORIGINAL PROVIDER,ONE

COMMENTS: DISCONTINUED IN ERROR

3 12/18/12 DISCONTINUED ORIGINAL RPH,ONE

COMMENTS: error

Are you sure you want to Reinstate? NO// y YES

Comments: discontinued in error

Nature of Order: SERVICE CORRECTION// S

================================================================================

3363 DIGOXIN 0.25MG TAB

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

DIGOXIN 0.25MG: Single dose of 0.75 milligrams exceeds the maximum single

dose of 0.5 milligrams.

DIGOXIN 0.25MG: Total dose of 0.75 milligrams/day exceeds the maximum daily

dose of 0.5 milligrams/day.

Do you want to Continue? Y//

Do you want to Process or Cancel medication?

DIGOXIN 0.25MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for DIGOXIN 0.25MG TAB

PROVIDER: provider,one PROVIDER,ONE OP

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

<span id="Page_81" class="anchor"></span>intervention or for more options.

Would you like to edit this intervention ? N// O

Prescription \#3363 REINSTATED!

Prescription \#3363:

Filled: DEC 18, 2012 Printed: Released:

Either print the label using the reprint option

or check later to see if the label has been printed.

Press Return to continue...:

### Technician Entered Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example below illustrates the verification changes to incorporate Dosing Order Checks. In this example a medication order is entered by a non-pharmacist (not holding the PSORPH key) with the outpatient site parameter set to ‘Yes’ for VERIFICATION.

Technician Entered Order

Medication Profile Sep 30, 2011@13:49:10 Page: 1 of 1

\<A\>

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 12147 GABAPENTIN 600MG TAB 360 A 09-30 09-30 5 30

2 12148 WARFARIN 10MG TAB 30 A 09-30 09-30 5 30

----------------------------------DISCONTINUED----------------------------------

3 12150 ASPIRIN 325MG TAB 100 DC 09-30 09-30 1 30

----------------------------------NON-VERIFIED----------------------------------

4 12151 ASPIRIN BUFFERED 325MG TAB 1800 N 09-30 09-30 5 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// NO New Order

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 60

RX PATIENT STATUS: OPT NSC//

DRUG: CIMETIDINE

Lookup: GENERIC NAME

1 CIMETIDINE 150MG/ML 8ML INJ GA301

2 CIMETIDINE 200MG TAB GA301

3 CIMETIDINE 300MG TAB GA301

4 CIMETIDINE 300MG/5ML SOL (OZ) GA301

CHOOSE 1-4: 3 CIMETIDINE 300MG TAB GA301

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press return to continue:

-------------------------------------------------------------------------------

\*\*\*Critical\*\*\* Drug Interaction with Prospective Drug:

CIMETIDINE 300MG TAB and

Local RX#: 100002148

Drug: WARFARIN 10MG TAB (Active)

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Processing Status: Not released locally (Window)

Last Filled On: 09/30/11

The pharmacologic effects of warfarin may be increased resulting in severe

bleeding.

Display Interaction Monograph? No// NO

VERB: TAKE

There are 2 Available Dosage(s):

1\. 300MG

2\. 600MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1200MG 1200MG

You entered 1200MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 4// 4

Dosage Ordered: 1200MG

NOUN: TABLETS

ROUTE: ORAL (BY MOUTH)// ORAL (BY MOUTH)

Schedule: Q6H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

1 Q6H Q6H EVERY 6 HOURS

2 Q6H PRN Q6H

3 Q6H-MID-PRN Q6H

CHOOSE 1-3: 1 Q6H Q6H EVERY 6 HOURS (EVERY 6 HOURS)

LIMITED DURATION (IN DAYS, HOURS, OR MINUTES):

CONJUNCTION:

Press Return to continue,'^' to exit:

CIMETIDINE 300MG TAB: Single dose of 1,200 milligrams exceeds the maximum

single dose of 800 milligrams.

CIMETIDINE 300MG TAB: Total dose of 4,800 milligrams/day exceeds the

maximum daily dose of 1,600 milligrams/day.

PATIENT INSTRUCTIONS:

(TAKE FOUR TABLETS BY MOUTH EVERY 6 HOURS)

DAYS SUPPLY: (1-90): 30//

QTY ( TAB ) : 480// 480 Greater Than Current Inventory! Below Reorder Level.

COPIES: 1// 1

\# OF REFILLS: (0-5): 5//

PROVIDER: RESIDENT,NEW

CLINIC:

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

REMARKS:

<span id="Page_83" class="anchor"></span>ISSUE DATE: TODAY// (SEP 30, 2011)

FILL DATE: (9/30/2011 - 9/30/2012): TODAY// (SEP 30, 2011)

Nature of Order: WRITTEN// W

Rx \# 100002152 09/30/11

\#480

TAKE FOUR TABLETS BY MOUTH EVERY 6 HOURS

CIMETIDINE 300MG TAB

RESIDENT,NEW PSOTECH,ONE

\# of Refills: 5

SC Percent: 60%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? NO

Is this correct? YES//

Another New Order for ? YES// N

When the VERIFICATION outpatient site parameter is set to ‘Yes’, Dosing Order Check warnings will be displayed to a user who does not hold the PSORPH key when entering a new outpatient medication order through the pharmacy backdoor or when finishing a pending order.

When the VERIFICATION outpatient site parameter is set to ‘No’, Dosing Order Check warnings will be displayed to a user who does not hold the PSORPH key when entering a new outpatient medication order through the pharmacy backdoor. In this instance, the user will not be allowed to finish a pending order.

A user who does not hold the PSORPH key, regardless of how the VERIFICATION outpatient site parameter is set to, will not be prompted to take any intervention action on a Dosing Order Check warning.

If the VERIFICATION outpatient site parameter is set to ‘Yes’, a prescription (Rx) warning label is generated to inform the pharmacist that a critical Drug Interaction and/or a Dosing Order Check warnings have occurred for an outpatient medication order entered by a user who does not hold the PSORPH key. The bottle label will not be printed.

Changes have been made in MOCHA v2.1b to the warning label(s) shown below to incorporate notification that a Dosing Check warnings have also occurred.

Critical Drug Interaction and Dosing Order Checks

Rx# 12152 has caused a DRUG-DRUG INTERACTION with the following prescription(s):

12148 CRITICAL INTERACTION WARFARIN 10MG TAB

DOSAGE EXCEEDS MAX SINGLE DOSE AND/OR MAX DAILY DOSE This prescription was entered by: PSOTECH,ONE

This prescription requires intervention by a pharmacist

SEPT 30,2011 Fill 1 of 5

TAKE FOUR TABLETS BY MOUTH EVERY 6 HOURS

Qty: 480 PSOTECH,ONE

Tech\_\_\_\_\_\_\_\_\_\_RPh\_\_\_\_\_\_\_\_\_\_

CIMETIDINE 300MG TAB

Routing: WINDOW

Days supply: 90 Cap: SAFETY

Isd: SEPT 30,2011 Exp: SEPT 30,2012

Stat SC Clinic: UNKNOWN

Dosing Order Checks Only

DOSAGE EXCEEDS MAX SINGLE DOSE AND/OR MAX DAILY DOSE This prescription was entered by: PSOTECH,ONE

This prescription requires intervention by a pharmacist

<span id="Page_84" class="anchor"></span>SEPT 30,2011 Fill 1 of 5

TAKE ONE CAPSULE BY MOUTH EVERY 8 HOURS

Qty: 270 PSOTECH, ONE

Tech\_\_\_\_\_\_\_\_\_\_RPh\_\_\_\_\_\_\_\_\_\_

INDINAVIR 400MG CAP

Routing: WINDOW

Days supply: 90 Cap: SAFETY

Isd: SEPT 30,2011 Exp: SEPT 30,2012

Last Fill: N/A

Pat. Stat SC Clinic: UNKNOWN

If the VERIFICATION outpatient site parameter is set to ‘No’ and there are Drug Interactions and/or Dosing Order Check warnings for the outpatient medication order, both the warning label and the bottle label will print.

All order checks that are normally displayed during order entry will be executed for the order being processed and in the same sequence. Edits to any of the following fields will result in Dosing Order Checks being executed again:

- Orderable Item
- Dispense Drug
- Dosage
- Dispense Units per Dose
- Route
- Conjunction (complex order)

The status of the order will remain non-verified until all Drug Interactions and Dosing Order Checks have been processed for an order.

### Verification of an Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will illustrate various options that can be used to verify an outpatient medication order.

#### Patient Prescription Processing

In the example below, a pharmacist will verify the order from the example above using the Patient Prescription Processing option. The order has a critical Drug Interaction and Dosing Order Checks to process.

Verifying order using Patient Prescription Processing option

Medication Profile Sep 30, 2011@14:07:51 Page: 1 of 1

\<A\>

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 12147 GABAPENTIN 600MG TAB 360 A 09-30 09-30 5 30

2 12148 WARFARIN 10MG TAB 30 A 09-30 09-30 5 30

----------------------------------DISCONTINUED----------------------------------

3 12150 ASPIRIN 325MG TAB 100 DC 09-30 09-30 1 30

----------------------------------NON-VERIFIED----------------------------------

4 12151 ASPIRIN BUFFERED 325MG TAB 1800 N 09-30 09-30 5 30

5 12152 CIMETIDINE 300MG TAB 480 N 09-30 09-30 5 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// 5

OP Medications (NON-VERIFIED) Sep 30, 2011@14:06:35 Page: 1 of 2

\<A\>

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

Rx \#: 12152

\(1\) \*Orderable Item: CIMETIDINE TAB

\(2\) Drug: CIMETIDINE 300MG TAB

\(3\) \*Dosage: 1200 (MG)

Verb: TAKE

Dispense Units: 4

Noun: TABLETS

\*Route: ORAL (BY MOUTH)

\*Schedule: Q6H

(4)Pat Instructions:

SIG: TAKE FOUR TABLETS BY MOUTH EVERY 6 HOURS

\(5\) Patient Status: OPT NSC

\(6\) Issue Date: 09/30/11 (7) Fill Date: 09/30/11

Last Fill Date: 09/30/11 (Window)

\+ Enter ?? for more actions

DC Discontinue PR (Partial) RL (Release)

ED Edit RF (Refill) RN (Renew)

Select Action: Next Screen// VF VF

ID#: RX: 12152

RX: 12152 PATIENT:

STATUS: Non-Verified

DRUG: CIMETIDINE 300MG TAB

QTY: 480 30 DAY SUPPLY

SIG: TAKE FOUR TABLETS BY MOUTH EVERY 6 HOURS

LATEST: 09/30/2011 \# OF REFILLS: 5 REMAINING: 5

ISSUED: 09/30/11 PROVIDER:

LOGGED: 09/30/11 CLINIC: NOT ON FILE

EXPIRES: 09/30/12 DIVISION: ALBANY (500)

CAP: SAFETY ROUTING: WINDOW

ENTRY BY: PSOTECH,ONE VERIFIED BY:

LABEL LOG:

\# DATE RX REF PRINTED BY

===============================================================================

1 09/30/11 ORIGINAL PSOTECH, ONE

COMMENTS: From RX number 12152 Drug-Drug interaction

EDIT: (Y/N/P): N// O

Press return to continue:

RX#: 12152

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

--------------------------------------------------------------------------------

-------------------------------------ACTIVE-------------------------------------

1 12147 GABAPENTIN 600MG TAB 360 A 09-30 09-30 5 30

2 12148 WARFARIN 10MG TAB 30 A 09-30 09-30 5 30

----------------------------------DISCONTINUED----------------------------------

3 12150 ASPIRIN 325MG TAB 100 DC 09-30 09-30 1 30

----------------------------------NON-VERIFIED----------------------------------

4 12151 ASPIRIN BUFFERED 325MG TAB 1800 N 09-30 09-30 5 30

5 12152 CIMETIDINE 300MG TAB 480 N 09-30 09-30 5 30

Press Return to continue:

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

-------------------------------------------------------------------------------

\*\*\*Critical\*\*\* Drug Interaction with Prospective Drug:

CIMETIDINE 300MG TAB and

Local RX#: 12148

Drug: WARFARIN 10MG TAB (Active)

SIG: TAKE ONE TABLET BY MOUTH EVERY EVENING

Processing Status: Not released locally (Window)

Last Filled On: 09/30/11

The pharmacologic effects of warfarin may be increased resulting in severe

bleeding.

Display Interaction Monograph? No// NO

Do you want to Continue? Y// ES

Do you want to Process or Cancel medication?

Rx \#100002152 Drug: CIMETIDINE 300MG TAB: PROCESS//

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for CIMETIDINE 300MG TAB

PROVIDER: RESIDENT,NEW

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

Press return to continue:

CIMETIDINE 300MG TAB: Single dose of 1,200 milligrams exceeds the maximum

single dose of 800 milligrams.

CIMETIDINE 300MG TAB: Total dose of 4,800 milligrams/day exceeds the

maximum daily dose of 1,600 milligrams/day.

Do you want to Continue? Y// ES

Do you want to Process or Cancel medication?

CIMETIDINE 300MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for CIMETIDINE 300MG TAB

PROVIDER: RESIDENT,NEW

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

VERIFY FOR ? (Y/N/Delete/Quit): Y// ES

Medication Profile Sep 30, 2011@14:13:34 Page: 1 of 1

\<A\>

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 1,1955 (56) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 12152 CIMETIDINE 300MG TAB 480 A 09-30 09-30 5 30

2 12147 GABAPENTIN 600MG TAB 360 A 09-30 09-30 5 30

3 12148 WARFARIN 10MG TAB 30 A 09-30 09-30 5 30

----------------------------------DISCONTINUED----------------------------------

4 12150 ASPIRIN 325MG TAB 100 DC 09-30 09-30 1 30

----------------------------------NON-VERIFIED----------------------------------

5 12151 ASPIRIN BUFFERED 325MG TAB 1800 N 09-30 09-30 5 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

#### Process Order Checks

The following example illustrates a pharmacist verifying an outpatient medication order using the *Process Order Check* \[PSO ORDER CHECKS VERIFY\] option for the drug Erythromycin which has several Drug Interactions and Dosing Order Check warnings.

Verifying order using Process Order Checks option

Select Outpatient Pharmacy Manager Option: PROCESS Order Checks

Select RX with Order Checks: 3334 ERYTHROMYCIN 250MG CAP

RX: 3334

RX: 3334

STATUS: Non-Verified

DRUG: ERYTHROMYCIN 250MG CAP

QTY: 800 10 DAY SUPPLY

SIG: TAKE 20 CAPSULES BY MOUTH FOUR TIMES A DAY

LATEST: 08/09/2012 \# OF REFILLS: 3 REMAINING: 3

ISSUED: 08/09/12 PROVIDER:

LOGGED: 08/09/12 CLINIC: NOT ON FILE

EXPIRES: 08/10/13 DIVISION: HINES (499)

CAP: SAFETY ROUTING: WINDOW

ENTRY BY: PSTECH,ONE VERIFIED BY:

FILLED: 08/09/12 PHARMACIST: LOT \#:

DISPENSED: 08/09/12 RELEASED:

LABEL LOG:

\# DATE RX REF PRINTED BY

===============================================================================

1 08/09/12 ORIGINAL PSTECH,ONE

COMMENTS: From RX number 3334 Drug-Drug interaction

EDIT: (Y/N/P): N// O

RX#: 3334

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

--------------------------------------------------------------------------------

-------------------------------------ACTIVE-------------------------------------

1 3326 CIMETIDINE 300MG TAB 90 A 08-09 08-09 3 90

2 3333 FOLIC ACID 1MG TAB 9000 A 08-09 08-09 3 90

3 3335 KETOCONAZOLE 200MG TAB 2700 A 08-09 08-09 3 90

4 3329 THEOPHYLLINE/ 200MG S.A. TAB 120 A 08-09 08-09 3 30

----------------------------------DISCONTINUED----------------------------------

5 3327 THEOPHYLLINE 300MG S.A. TAB 180 DF 08-09 08-09 3 90

----------------------------------NON-VERIFIED----------------------------------

6 3334 ERYTHROMYCIN 250MG CAP 800 N 08-09 08-09 3 10

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

-------------------------------------------------------------------------------

\*\*\*Critical\*\*\* Drug Interaction with Prospective Drug:

ERYTHROMYCIN 250MG CAP and

<span id="Page_89" class="anchor"></span> Local RX#: 3329

Drug: THEOPHYLLINE/ 200MG S.A. TAB (Active)

SIG: TAKE TWO TABLETS BY MOUTH TWICE A DAY

Processing Status: Released locally on 8/9/12@12:05:08 (Window)

Last Filled On: 08/09/12

The concurrent administration of xanthine derivatives and some macrolides

may result in elevated levels and increased clinical and adverse effects of

the xanthine derivatives. The serum levels of erythromycin may be

decreased.

Display Interaction Monograph? No// NO

-------------------------------------------------------------------------------

\*\*\*Significant\*\*\* Drug Interaction with Prospective Drug:

ERYTHROMYCIN 250MG CAP and

Local RX#: 3335

Drug: KETOCONAZOLE 200MG TAB (Active)

SIG: TAKE SEVEN AND ONE-HALF TABLETS BY MOUTH THREE

TIMES A DAY

Processing Status: Not released locally (Window)

Last Filled On: 08/09/12

\*\*\* Refer to MONOGRAPH for SIGNIFICANT INTERACTION CLINICAL EFFECTS

Display Interaction Monograph? No// NO

Do you want to Continue? Y// ES

Do you want to Process or Cancel medication?

Rx \#3334 Drug: ERYTHROMYCIN 250MG CAP: PROCESS//

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for ERYTHROMYCIN 250MG CAP

PROVIDER: PROVIDER,ONE

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

Intervention or for more options.

Would you like to edit this intervention ? N// O

ERYTHROMYCIN 250MG TAB: Single dose of 5,000 milligrams exceeds the maximum

single dose of 1,000 milligrams.

ERYTHROMYCIN 250MG TAB: Total dose of 20,000 milligrams/day exceeds the

maximum daily dose of 4,000 milligrams/day.

Do you want to Continue? Y//

Do you want to Process or Cancel medication?

ERYTHROMYCIN 250MG CAP: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for ERYTHROMYCIN 250MG CAP

PROVIDER: PROVIDER,ONE

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

RX#: 3334

ERYTHROMYCIN 250MG CAP

VERIFY FOR ? (Y/N/Delete/Quit): Y// ES

Label Printer: Rx Label DEVICE

LABEL: QUEUE/CHANGE PRINTER/HOLD/SUSPEND or '^' to bypass Q// UEUE

LABEL(S) QUEUED TO PRINT

Select RX with Order Checks:

#### List of Non-Verified Scripts

The following example displays the *List of Non-Verified Scripts* \[PSO VRPT\] option. The option provides a list of outpatient medication orders that have a status of non-verified sorted by patient or clerk. The prescription number, date issued, drug and the Internal Entry Number (IEN) of the person who entered the order are displayed. A ‘#’ in front of the drug name indicates that the non-verified order has a critical Drug Interaction and/or Dosing Order Checks that require processing.

List of Non-Verified Scripts option

Select Verification Option: LIST Non-Verified Scripts

Sort By Patient or Clerk: P// ATIENT

DEVICE: HOME// Local SSH Device Right Margin: 80//

NON-VERIFIED PRESCRIPTIONS

AS OF AUG 9,2012@13:08:12

SORTED BY PATIENT

(# indicates Order Check)

Patient name Page: 1

Rx \# Issued Drug Entry By

------------------------------------------------------------------------------

PSOPATIENT,NINETEEN

3332 08/09/12 \#KETOCONAZOLE 200MG TAB 222222317

3333 08/09/12 \#FOLIC ACID 1MG TAB 222222317

3334 08/09/12 \#ERYTHROMYCIN 250MG CAP 222222317

#### Rx Verification by Clerk

The example below illustrates a pharmacist verifying an order using the *Rx Verification by Clerk* \[PSO VR\] option. All non-verified outpatient orders entered by a clerk are presented for processing.

Verifying order using Rx Verification by Clerk option

Select Verification Option: RX Verification by Clerk

Enter Clerk Name: PSTECH,ONE OPT

RX: 3332 PATIENT:

STATUS: Non-Verified

DRUG: KETOCONAZOLE 200MG TAB

QTY: 2700 90 DAY SUPPLY

SIG: TAKE TEN TABLETS BY MOUTH THREE TIMES A DAY

<span id="Page_91" class="anchor"></span> LATEST: 08/09/2012 \# OF REFILLS: 3 REMAINING: 3

ISSUED: 08/09/12 PROVIDER:

LOGGED: 08/09/12 CLINIC: NOT ON FILE

EXPIRES: 08/10/13 DIVISION: HINES (499)

CAP: SAFETY ROUTING: WINDOW

ENTRY BY: PSTECH,ONE VERIFIED BY:

LABEL LOG:

\# DATE RX REF PRINTED BY

===============================================================================

1 08/09/12 ORIGINAL PSTECH,ONE

COMMENTS: From RX number 3332 Drug-Drug interaction

EDIT: (Y/N/P): N// YES

OP Medications (NON-VERIFIED) Aug 09, 2012@13:15:19 Page: 1 of 2

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 19,1920 (92) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

Rx \#: 3332

\(1\) \*Orderable Item: KETOCONAZOLE TAB

\(2\) Drug: KETOCONAZOLE 200MG TAB

\(3\) \*Dosage: 2000 (MG)

Verb: TAKE

Dispense Units: 10

Noun: TABLETS

\*Route: ORAL

\*Schedule: TID

(4)Pat Instructions:

SIG: TAKE TEN TABLETS BY MOUTH THREE TIMES A DAY

\(5\) Patient Status: SC

\(6\) Issue Date: 08/09/12 (7) Fill Date: 08/09/12

Last Fill Date: 08/09/12 (Window)

\+ Enter ?? for more actions

DC (Discontinue) PR (Partial) RL (Release)

ED Edit RF (Refill) RN (Renew)

Select Action: Next Screen// 3

There are 2 Available Dosage(s):

1\. 200MG

2\. 400MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2000MG//1500MG 1500MG

You entered 1500MG is this correct? Yes// YES

VERB: TAKE// TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 7.5// 7.5

Dosage Ordered: 1500MG

NOUN: TABLETS// TABLETS

ROUTE: ORAL// ORAL

Schedule: TID// (THREE TIMES A DAY)

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

TID TID THREE TIMES A DAY

...OK? Yes// (Yes)

(THREE TIMES A DAY)

LIMITED DURATION (IN MONTHS, WEEKS, DAYS, HOURS OR MINUTES):

CONJUNCTION:

Press return to continue:

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

-------------------------------------------------------------------------------

\*\*\*Critical\*\*\* Drug Interaction with Prospective Drug:

KETOCONAZOLE 200MG TAB and

Local RX#: 3328

Drug: WARFARIN 5MG TAB (Active)

SIG: TAKE ONE TABLET BY MOUTH ON MONDAY,WEDNESDAY AND

FRIDAY EXCEPT TAKE TWO TABLETS ON TUESDAYS AND

THURSDAYS

Processing Status: Released locally on 8/9/12@12:05:08 (Mail)

Last Filled On: 08/09/12

The anticoagulant effect of warfarin may be increased.

Display Interaction Monograph? No// NO

-------------------------------------------------------------------------------

\*\*\*Significant\*\*\* Drug Interaction with Prospective Drug:

KETOCONAZOLE 200MG TAB and

Local RX#: 3326

Drug: CIMETIDINE 300MG TAB (Active)

SIG: TAKE ONE TABLET BY MOUTH AT BEDTIME

Processing Status: Released locally on 8/9/12@12:05:08 (Window)

Last Filled On: 08/09/12

\*\*\* Refer to MONOGRAPH for SIGNIFICANT INTERACTION CLINICAL EFFECTS

Display Interaction Monograph? No// NO

-------------------------------------------------------------------------------

\*\*\*Significant\*\*\* Drug Interaction with Prospective Drug:

KETOCONAZOLE 200MG TAB and

Local RX#: 3334

Drug: ERYTHROMYCIN 250MG CAP (Non-Verified)

SIG: TAKE 20 CAPSULES BY MOUTH FOUR TIMES A DAY

Processing Status: Not released locally (Window)

Last Filled On: 08/09/12

\*\*\* Refer to MONOGRAPH for SIGNIFICANT INTERACTION CLINICAL EFFECTS

Display Interaction Monograph? No// NO

Do you want to Continue? Y// ES

Do you want to Process medication

KETOCONAZOLE 200MG TAB: P// ROCESS

Enter your Current Signature Code: SIGNATURE VERIFIED

Remote data not available - Only local order checks processed.

Press return to continue:

Now creating Pharmacy Intervention

for KETOCONAZOLE 200MG TAB

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

New OP Order (ROUTINE) Aug 09, 2012@13:17:37 Page: 1 of 2

Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 19,1920 (92) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

Orderable Item: KETOCONAZOLE TAB

\(1\) Drug: KETOCONAZOLE 200MG TAB

\(2\) Patient Status: SC

\(3\) Issue Date: AUG 9,2012 (4) Fill Date: AUG 9,2012

\(5\) Dosage Ordered: 1500 (MG)

Verb: TAKE

Dispense Units: 7.5

Noun: TABLETS

Route: ORAL

Schedule: TID

(6)Pat Instruction:

SIG: TAKE SEVEN AND ONE-HALF TABLETS BY MOUTH THREE TIMES

A DAY

\(7\) Days Supply: 90 (8) QTY ( ): 2700

\+ This change will create a new prescription!

AC Accept ED Edit

Select Action: Next Screen// AC Accept

KETOCONAZOLE 200MG TAB : Single dose of 1,500 milligrams exceeds the

maximum single dose of 600 milligrams.

KETOCONAZOLE 200MG TAB : Total dose of 4,500 milligrams/day exceeds the

maximum daily dose of 1,200 milligrams/day.

Do you want to Continue? Y//

Do you want to Process or Cancel medication?

KETOCONAZOLE 200MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for KETOCONAZOLE 200MG TAB

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

<span id="Page_94" class="anchor"></span>Nature of Order: SERVICE CORRECTION// S

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 3335 08/09/12

\#2700

TAKE SEVEN AND ONE-HALF TABLETS BY MOUTH THREE TIMES A DAY

KETOCONAZOLE 200MG TAB

PROVIDER,ONE RPH,ONE

\# of Refills: 3

SC Percent: %

Disabilities: NONE STATED

Was treatment for a Service Connected condition? NO//

Is this correct? YES// ...

Label Printer: NULL DEVICE

LABEL: QUEUE/CHANGE PRINTER/HOLD/SUSPEND or '^' to bypass Q// UEUE

LABEL(S) QUEUED TO PRINT

PROFILES MUST BE SENT TO PRINTER !!

Select PROFILE DEVICE: HOME// NULL NULL DEVICE NULL DEVICE

PROFILE IS QUEUED TO PRINT

PROFILE(S) QUEUED to PRINT

NAME SSN ID ORDER

Please advise the patient that the above ID \# and/or ORDER Letter

will be displayed with his/her name on the Bingo Display

Select Verification Option: RX Verification by Clerk

Enter Clerk Name: PSTECH,ONE OPT

RX: 3333 PATIENT:

STATUS: Non-Verified

DRUG: FOLIC ACID 1MG TAB

QTY: 25 10 DAY SUPPLY

SIG: TAKE 25 TABLETS BY MOUTH EVERY MORNING

LATEST: 08/09/2012 \# OF REFILLS: 3 REMAINING: 3

ISSUED: 08/09/12 PROVIDER:

LOGGED: 08/09/12 CLINIC: NOT ON FILE

EXPIRES: 08/10/13 DIVISION: HINES (499)

CAP: SAFETY ROUTING: WINDOW

ENTRY BY: PSTECH,ONE VERIFIED BY:

LABEL LOG:

\# DATE RX REF PRINTED BY

===============================================================================

1 08/09/12 ORIGINAL PSTECH,ONE

COMMENTS: From RX number 3333 Drug-Drug interaction

EDIT: (Y/N/P): N// O

ID#: RX#: 3333

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

--------------------------------------------------------------------------------

-------------------------------------ACTIVE-------------------------------------

3326 CIMETIDINE 300MG TAB 90 A 08-09 08-09 3 90

3335 KETOCONAZOLE 200MG TAB 2700 A 08-09 08-09 3 90

3329 THEOPHYLLINE/ 200MG S.A. TAB 120 A 08-09 08-09 3 30

3328 WARFARIN 5MG TAB 210 A 08-09 08-09 0 30

----------------------------------DISCONTINUED----------------------------------

3327 THEOPHYLLINE 300MG S.A. TAB 180 DF 08-09 08-09 3 90

----------------------------------NON-VERIFIED----------------------------------

3334 ERYTHROMYCIN 250MG CAP 800 N 08-09 08-09 3 10

3333 FOLIC ACID 1MG TAB 250 N 08-09 08-09 3 90

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

FOLIC ACID 1MG S.T.: Single dose of 25 milligrams exceeds the maximum

single dose of 20 milligrams.

FOLIC ACID 1MG S.T.: Total dose of 25 milligrams/day exceeds the maximum

daily dose of 20 milligrams/day.

Do you want to Continue? Y//

Do you want to Process or Cancel medication?

FOLIC ACID 1MG TAB: P// ROCESS MEDICATION

Enter your Current Signature Code: SIGNATURE VERIFIED

Now creating Pharmacy Intervention

for FOLIC ACID 1MG TAB

PROVIDER: PROVIDER,ONE

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// O

ID#: RX#: 3333

FOLIC ACID 1MG TAB

VERIFY FOR ? (Y/N/Delete/Quit): Y// ??

Enter Y (or return) to verify this prescription

N to leave this prescription non-verified and to end this session of verification

D to delete this prescription

Select one of the following:

Y YES

N NO

D DELETE

Q QUIT

VERIFY FOR ? (Y/N/Delete/Quit): Y// ES

### Schedule Exclusions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A schedule can be excluded from all Dosing Checks or just the Daily Dose Check. If such a schedule is used within an outpatient medication order, depending on which exclusion is applied, all Dosing Checks or just the Daily Dose Order Check will not be performed.

#### High Single Dose and Schedule Excluded from Daily Dose Check

In this example, a high single dose is entered for an order via an edit. The schedule within the order has been excluded from the Daily Dose Order Check. Upon acceptance of the order, a high dose warning for the single dose will be displayed with the general dosing information message. No message will be displayed to the user indicating that the Daily Dose Order Check was not performed.

High Single Dose and Schedule Excluded from Daily Dose Check

New OP Order (ROUTINE) Apr 21, 2025@19:56:17 Page: 1 of 2

PID: Ht(cm): 172.72 (03/11/2022)

DOB: JAN 1,1947 (78) Wt(kg): 112.00 (03/23/2025)

SEX: MALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.24

Orderable Item: HALOPERIDOL TAB

\(1\) Drug: HALOPERIDOL 20MG TAB

\(2\) Patient Status: SC

\(3\) Issue Date: APR 21,2025 (4) Fill Date: APR 21,2025

\(5\) Dosage Ordered: 100 (MG)

Verb: TAKE

Dispense Units: 5

Noun: TABLETS

Route: ORAL (BY MOUTH)

Schedule: QID

(6)Pat Instruction:

Indications: TESTING

SIG: TAKE FIVE TABLETS BY BY MOUTH FOUR TIMES A DAY

\+ This change will create a new prescription!

AC Accept ED Edit

Select Action: Next Screen// AC Accept

HALOPERIDOL 20MG TAB: Single dose of 100 milligrams exceeds the maximum

single dose of 40 milligrams.

General dosing range for HALOPERIDOL 20MG TAB (ORAL): 0.25 milligram/day

to 100 milligram/day. Maximum daily dose is 100 milligram/day.

Do you want to Continue? Y//

  

#### Maximum Single Dose Order Check could not be Performed and Schedule Excluded from Daily Dose Order Check

In this example, a free text dosage range which cannot be evaluated is entered for an order via an edit and the schedule has been excluded from the Daily Dose Order Check. Upon acceptance of the order, a message that the Maximum Single Dose Order Check could not be performed is displayed with the general dosing information message. No message will be displayed to the user indicating that the Daily Dose Order Check was not performed.

Maximum Single Dose Order Check could not be performed and Schedule Excluded from Daily Dose Order Check

<u>New OP Order (ROUTINE) Jun 07, 2017@12:44:50 Page: 1 of 2</u>

\<A\>

Ht(cm): 182.88 (11/14/1993)

DOB: JAN 1,1940 (77) Wt(kg): 90.91 (11/14/1993)

Orderable Item: HALOPERIDOL TAB

\(1\) Drug: HALOPERIDOL 20MG TAB

\(2\) Patient Status: SC

\(3\) Issue Date: JUN 7,2017 (4) Fill Date: JUN 7,2017

Verb: TAKE

\(5\) Dosage Ordered: 20-40MMGS

Route: ORAL

Schedule: TID

(6)Pat Instruction:

SIG: TAKE 20-40MMGS TABLET(S) BY MOUTH THREE TIMES A DAY

\(7\) Days Supply: 90 (8) QTY ( ): 540

\(9\) \# of Refills: 3 (10) Routing: WINDOW

\(11\) Clinic:

\(12\) Provider: PROVIDER,ONE (13) Copies: 1

\+ This change will create a new prescription!

AC Accept ED Edit

Select Action: Next Screen// ac Accept

Maximum Single Dose Check could not be performed for Drug: HALOPERIDOL

20MG TAB

Reason(s): Free Text Dosage could not be evaluated

General dosing range for HALOPERIDOL 20MG TAB (ORAL): 0.25 milligram/day

to 100 milligram/day. Maximum daily dose is 100 milligram/day.

Nature of Order: SERVICE CORRECTION//

.

.

.

#### Schedule Excluded from All Dosing Order Checks

In this example, a high single dose and a schedule that would normally result in a high single dose warning and a high daily dose warning is entered for an order via an edit. Upon acceptance of the order, nothing is displayed to the user. The schedule in the order was excluded from all Dosing Checks. No Maximum Single Dose Order Check or Max Daily Dose Order Check is performed. No message will be displayed to the user indicating that no Dosing Checks were performed.

Schedule Excluded from All Daily Dose Check

<u>New OP Order (ROUTINE) Jun 07, 2017@12:52:55 Page: 1 of 2</u>

\<A\>

PID: Ht(cm): 182.88 (11/14/1993)

DOB: JAN 1,1940 (77) Wt(kg): 90.91 (11/14/1993)

Orderable Item: HALOPERIDOL TAB

\(1\) Drug: HALOPERIDOL 20MG TAB

\(2\) Patient Status: SC

\(3\) Issue Date: JUN 7,2017 (4) Fill Date: JUN 7,2017

\(5\) Dosage Ordered: 60 (MG)

Verb: TAKE

Dispense Units: 3

Noun: TABLETS

Route: ORAL

Schedule: TID

(6)Pat Instruction:

SIG: TAKE THREE TABLETS BY MOUTH THREE TIMES A DAY

\(7\) Days Supply: 90 (8) QTY ( ): 810

\(9\) \# of Refills: 3 (10) Routing: WINDOW

\+ This change will create a new prescription!

AC Accept ED Edit

Select Action: Next Screen// AC Accept

Nature of Order: SERVICE CORRECTION// S

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 3641 06/07/17

PSOPATIENT,FIFTEEN \#810

TAKE THREE TABLETS BY MOUTH THREE TIMES A DAY

HALOPERIDOL 20MG TAB

PROVIDER,ONE PHARMACIST,ONE

\# of Refills: 3

SC Percent: 40%

Disabilities: NONE STATED

Was treatment for a Service Connected condition? NO//

Is this correct? YES// ...

### Per Orifice Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a high dose warning or general dosing information message is displayed to the user it will be prefaced with a note informing the user that the dosing information is per orifice. This will be done for drugs administered by the eye, ear, or nose. The mapping of the local medication route within the order to the standard medication routes of ‘NASAL’, ‘OPHTHALMIC’ and ‘OTIC’ will identify whether or not the drug is administered by the eye, ear, or nose.

#### High Dose Warnings

In this example, a new outpatient medication order is entered which results in a max single dose warning and a max daily dose warning. The high dose warnings are prefaced with the text ‘Dosing Information provided is PER NOSTRIL:’ and it is only displayed once.

High Dose Warnings

Select Action: Quit// NO New Order

Eligibility: SC LESS THAN 50% SC%: 40

RX PATIENT STATUS: SC//

DRUG: CROMOL

Lookup: GENERIC NAME

CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML NT900

...OK? Yes// (Yes)

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

VERB: INSTILL

There are NO Available Dosage(s):

Please Enter a Free Text Dose: 5 SPRAYS 5 SPRAYS

You entered 5 SPRAYS is this correct? Yes// YES

VERB: INSTILL

ROUTE: PO// NASA

1 NASAL NA

2 NASAL NASAL

CHOOSE 1-2: 2 NASAL NASAL

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

BID BID TWICE A DAY

...OK? Yes// (Yes)

(TWICE A DAY)

LIMITED DURATION (IN DAYS, HOURS, OR MINUTES):

CONJUNCTION:

Dosing Information provided is PER NOSTRIL:

CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML: Single dose of 5 sprays exceeds the

maximum single dose of 1 spray.

CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML: Total dose of 10 sprays/day exceeds

the maximum daily dose of 6 sprays/day.

Do you want to Continue? Y//

.

.

.

#### General Dosing Information Message

In this example, a schedule is entered for an outpatient medication order that does not have a frequency defined. After the Dosing Order Checks are performed, a message that the Max Daily Dose Order Check could not be performed is displayed with the general dosing information message. The General Dosing Information message is prefaced with the text ‘Dosing Information provided is PER EAR:’

General Dosing Information Message

DRUG:    ACETIC ACID 2% OTIC SOL 15 ML          OT109          

         ...OK? Yes//   (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

There are 2 Available Dosage(s):

       1. 1 DROP
       2. 2 DROP

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 5 DROPS 5 DROPS

You entered 5 DROPS is this correct? Yes//   YES

VERB: INSTILL

ROUTE: //OTIC        OTIC 

Schedule: FREQTEST

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

  FREQTEST  FREQTEST 

         ...OK? Yes//   (Yes)

(FREQTEST)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

   Max Daily Dose Check could not be performed for Drug: ACETIC ACID 2%

   OTIC SOL 15 ML

     Reason(s): Invalid or Undefined Frequency

Dosing Information provided is PER EAR:    General dosing range for ACETIC ACID

2% OTIC SOL 15 ML  (OTIC (EAR)): 12

   drop/day to 30 drop/day. Maximum daily dose is 30 drop/day.

PATIENT INSTRUCTIONS: //

.

.

.

#### Complex Order

In this example, an outpatient complex order is entered for a medication that is administered through the eye that has 5 dosing sequences. When each dosing sequence is entered that exceeds the maximum single dose, a high dose warning is displayed prefaced by the text ‘Dosing Information provided is PER EYE:’

Once the final dosing sequence has been entered, a dosing check summary is displayed because the order had more than 3 dosing sequences. The text ‘Dosing Information provided is PER EYE:’ is displayed before the first dosing sequence listed below the Dosing Check Summary header. If the dosing check summary information could not have been displayed on one page, the per orifice note text would have been repeated on each additional page for high dose warnings and general dosing information messages.

Complex Order

DRUG:    PREDNISOLONE 1% OPTH SOL 5ML         OP300          

         ...OK? Yes//   (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

There are 2 Available Dosage(s):

       1. 1 DROP
       2. 2 DROP(S)

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 6 DROPS 6 DROPS

You entered 6 DROPS is this correct? Yes//   YES

VERB: INSTILL

ROUTE: //OU  BOTH EYES      OU  IN BOTH EYES

Schedule: QD

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

     1   QD    QD  EVERY DAY

     2   QD    QD 

     3   QD  HS    QD 

     4   QDAY    QD 

     5   QDAY    QD 

CHOOSE 1-5: 1  QD  QD  EVERY DAY (EVERY DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): 6D (DAYS)

CONJUNCTION: THEN

Dosing Information provided is PER EYE:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 6 drops exceeds the maximum

   single dose of 2 drops.

Do you want to Continue? Y// ES

There are 2 Available Dosage(s):

       1. 1 DROP
       2. 2 DROP(S)

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 5 DROPS 5 DROPS

You entered 5 DROPS is this correct? Yes//   YES

VERB: INSTILL

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

  BID  BID  TWICE A DAY

         ...OK? Yes//   (Yes)

(TWICE A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): 4D (DAYS)

CONJUNCTION: THEN

Dosing Information provided is PER EYE:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 5 drops exceeds the maximum

   single dose of 2 drops.

Do you want to Continue? Y// ES

There are 2 Available Dosage(s):

       1. 1 DROP
       2. 2 DROP(S)

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 4 DROPS 4 DROPS

You entered 4 DROPS is this correct? Yes//   YES

VERB: INSTILL

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

  BID  BID  TWICE A DAY

         ...OK? Yes//   (Yes)

(TWICE A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): 3D (DAYS)

CONJUNCTION: THEN

Dosing Information provided is PER EYE:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 4 drops exceeds the maximum

   single dose of 2 drops.

Do you want to Continue? Y// ES

There are 2 Available Dosage(s):

       1. 1 DROP
       2. 2 DROP(S)

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 3 DROPS 3 DROPS

You entered 3 DROPS is this correct? Yes//   YES

VERB: INSTILL

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

  BID  BID  TWICE A DAY

         ...OK? Yes//   (Yes)

(TWICE A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): 12D (DAYS)

CONJUNCTION: THEN

Dosing Information provided is PER EYE:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 3 drops exceeds the maximum

   single dose of 2 drops.

Do you want to Continue? Y// ES

There are 2 Available Dosage(s):

       1. 1 DROP
       2. 2 DROP(S)

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2 DROPS 2 DROPS

You entered 2 DROPS is this correct? Yes//   YES

VERB: INSTILL

Schedule: BID

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

  BID  BID  TWICE A DAY

         ...OK? Yes//   (Yes)

(TWICE A DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES): 7D (DAYS)

CONJUNCTION:

   DOSING CHECK SUMMARY:

   Dosing Information provided is PER EYE:

   DOSE SEQ 1:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 6 drops exceeds the maximum

   single dose of 2 drops.

   DOSE SEQ 2:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 5 drops exceeds the maximum

   single dose of 2 drops.

   DOSE SEQ 3:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 4 drops exceeds the maximum

   single dose of 2 drops.

   DOSE SEQ 4:

   PREDNISOLONE 1% OPTH SOL 5ML: Single dose of 3 drops exceeds the maximum

   single dose of 2 drops.

Press Return to continue,'^' to exit:

Do you want to Continue? Y//

### Max Daily Dose Order Check – Frequency Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA performs the Max Daily Dose Order Check when the FDB MedKnowledge Framework logic does not due to a frequency failure. Below are two examples of when VistA performs the Max Daily Dose Order Check.

#### VistA Successfully Performs Max Daily Dose Order Check

In this example, an order for Metformin 6000mg Q48H is entered. If a frequency message is displayed that indicates VistA performed the Max Daily Dose Order Check, which in this case resulted in a high dose warning. A high dose warning is displayed for the Maximum Single Dose Order Check which was performed by the vendor.

VistA successfully performs Max Daily Dose Order Check

DRUG:    METFORMIN 500MG         HS502          

         ...OK? Yes//   (Yes)

Now doing allergy checks. Please wait...

\*\*\*Metformin Lab Results\*\*\*

  Metformin - no serum creatinine within past 120 days.

Now processing Clinical Reminder Order Checks. Please wait ...

============================================================

\*\*\* Clinical Reminder Order Check \| Severity: MEDIUM \*\*\*

CR3286 CROC - METFORMIN DRUG SEVERITY MEDIUM (RULE DISP NAME)

\*\*\* FIRST LINE OF ORDER CHECK TEXT \*\*\* ORDER CHECK LINE 02 ORDER CHECK LINE 03

ORDER CHECK LINE 04 ORDER CHECK LINE 05 ORDER CHECK LINE 06 ORDER CHECK LINE 07

ORDER CHECK LINE 08 ORDER CHECK LINE 09 \*\*\* LAST LINE OF ORDER CHECK TEXT \*\*\*

------------------------------------------------------------

Press Return to Continue...:

Do you want to Intervene? N// O

Now Processing Enhanced Order Checks! Please wait...

There are 2 Available Dosage(s):

       1. 500MG
       2. 1000MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 6000MG 6000MG

You entered 6000MG is this correct? Yes//   YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 12// 12

Dosage Ordered: 6000MG

NOUN: TABLETS

ROUTE: //ORAL (BY MOUTH)          PO  BY MOUTH

Schedule: Q48H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

  Q48H  Q48H 

         ...OK? Yes//   (Yes)

(Q48H)

LIMITED DURATION (IN DAYS, HOURS, OR MINUTES):

CONJUNCTION:

   METFORMIN 500MG: Single dose of 6,000 milligrams exceeds the maximum single

   dose of 2,000 milligrams.

   METFORMIN 500MG: Average daily dose of 3,000 milligrams/day exceeds the

   maximum daily dose of 2,000 milligrams/day.

   Recommended frequency of METFORMIN 500MG: Frequency of every 2 days is

   below the frequency range of 1 to 2 administrations per day.

Do you want to Continue? Y//

#### VistA Cannot Perform Max Daily Dose Order Check – Not Correctable

In this example, an order for Enoxaparin 60MG/0.6ML INJ - One Vial SQ Q48H is entered. The presence of the frequency message indicates that VistA performed the Max Daily Dose Order Check. An error message is displayed for both the Maximum Single Dose Order Check and the Max Daily Dose Order Check. A general dosing information message is also provided because both Dosing Checks could not be performed.

The Maximum Single Dose Order Check tells us that there is a problem with the dose unit of ‘VIAL’ that was sent in for the Dosing Order Checks. Using the PDM *Lookup Dosing Check Info for Drug* option, we find out that acceptable units are ‘milligrams’ or ‘milliliters’. VistA cannot perform the Max Daily Dose Order Check because the daily dose cannot be evaluated against the max daily dose value returned because the units returned for the max daily dose are in milliliters. VistA in turn displays the original reason returned by the vendor as to why the Max Daily Dose could not be performed and that was because the frequency check failed.

VistA cannot perform Max Daily Dose Order Check – Not Correctable

Select Action: Next Screen// NO New Order

Eligibility: SERVICE CONNECTED 50% to 100% SC%: 100

RX PATIENT STATUS: SC//

DRUG: ENOXAP

Lookup: GENERIC NAME

ENOXAPARIN 60MG/0.6ML INJ BL110

...OK? Yes// (Yes)

Now doing remote order checks. Please wait...

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

VERB: INJECT

There are NO Available Dosage(s).

Please Enter a Free Text Dose: ONE VIAL ONE VIAL

You entered ONE VIAL is this correct? Yes// YES

VERB: INJECT

ROUTE: PO// SQ SUBCUTANEOUS SQ

Schedule: Q48H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

Q48H Q48H

...OK? Yes// (Yes)

(Q48H)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Maximum Single Dose Check could not be performed for Drug: ENOXAPARIN

60MG/0.6ML INJ

Reason(s): Unable to convert units : 'vial' to 'milliliter'.

Max Daily Dose Check could not be performed for Drug: ENOXAPARIN 60MG/0.6ML

INJ

Reason(s): Unable to convert units : 'vial/day' to 'milliliter/day'.

General dosing range for ENOXAPARIN 60MG/0.6ML INJ (SUBCUTANEOUS): 0.2

milliliter/day to 0.02 milliliter/kilogram/day. Maximum daily dose is

0.02 milliliter/kilogram/day.

Recommended frequency of ENOXAPARIN 60MG/0.6ML INJ: Unable to convert units

: 'vial' to 'milliliter'. A frequency check was not performed because the

ordered dose of 1 vial is not convertible to the dose screening unit of

measure of milliliter.

PATIENT INSTRUCTIONS:

.

.

.

#### VistA Cannot Perform Max Daily Dose Order Check – Correctable

In Example 1, an order for Enoxaparin 100MG/ML INJ – 100mg SQ Q48H is entered. The presence of the frequency message indicates that VistA performed the Max Daily Dose Order Check. A message is displayed for the Maximum Single Dose Order Check indicating that a weight is missing for the patient.

Example 1: VistA cannot perform Max Daily Dose Order Check - Correctable

Select Action: Quit// NO New Order

Eligibility:

RX PATIENT STATUS: OTHER FEDERAL//

DRUG: ENOX

Lookup: GENERIC NAME

ENOXAPARIN 100MG/ML INJ BL110

...OK? Yes// (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

There are 4 Available Dosage(s):

1\. 90 MILLIGRAMS (0.9ML)

2\. 100 MILLIGRAMS (1.0ML)

3\. 85 MILLIGRAMS (0.85ML)

4\. 95 MILLIGRAMS (0.95ML)

Select from list of Available Dosages (1-4), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2 100 MILLIGRAMS (1.0ML)

You entered 100 MILLIGRAMS (1.0ML) is this correct? Yes// YES

VERB: INJECT

ROUTE: //SQ SUBCUTANEOUS SQ

Schedule: Q48H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

Q48H Q48H

...OK? Yes// (Yes)

(Q48H)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Dosing Checks could not be performed for Drug: ENOXAPARIN 100MG/ML INJ

Reason(s): Weight is required.

General dosing range for ENOXAPARIN 100MG/ML INJ (SUBCUTANEOUS): 20

milligram/day to 2 milligram/kilogram/day. Maximum daily dose is 2

milligram/kilogram/day.

Recommended frequency of ENOXAPARIN 100MG/ML INJ: Frequency of every 2 days

is below the frequency range of 1 to 2 administrations per day.

Do you want to Continue? Y//

In Example 2, once a weight is entered for the patient, the same order is entered again and the results are different. A high dose warning for the Maximum Single Dose Order Check is displayed with a frequency message. The presence of the frequency message indicates that VistA performed the Max Daily Dose Order Check. The absence of messages specific to the Max Daily Dose Order Check indicates that the daily dose did not exceed the max daily dose value. In other words the daily dose for the order passed.

Example 2: VistA cannot perform Max Daily Dose Order Check - Corrected

Select Action: Quit// NO New Order

Eligibility:

RX PATIENT STATUS: OTHER FEDERAL//

DRUG: ENOXA

Lookup: GENERIC NAME

ENOXAPARIN 100MG/ML INJ BL110

...OK? Yes// (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

There are 4 Available Dosage(s):

1\. 90 MILLIGRAMS (0.9ML)

2\. 100 MILLIGRAMS (1.0ML)

3\. 85 MILLIGRAMS (0.85ML)

4\. 95 MILLIGRAMS (0.95ML)

Select from list of Available Dosages (1-4), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2 100 MILLIGRAMS (1.0ML)

You entered 100 MILLIGRAMS (1.0ML) is this correct? Yes// YES

VERB: INJECT

ROUTE: //SQ SUBCUTANEOUS SQ

Schedule: Q48H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

Q48H Q48H

...OK? Yes// (Yes)

(Q48H)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

ENOXAPARIN 100MG/ML INJ: Single dose of 100 milligrams exceeds the maximum

single dose of 1.5 milligrams/kilogram (75.15682 milligrams).

Recommended frequency of ENOXAPARIN 100MG/ML INJ: Frequency of every 2 days

is below the frequency range of 1 to 2 administrations per day.

Do you want to Continue? Y//

## Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of MOCHA v2.0, a Maximum Single Dose Order Check was introduced. MOCHA v2.1b implemented the Max Daily Dose Order Check for simple medication orders. During order entry both Dosing Order Checks will be performed for simple orders, while only the Maximum Single Dose Order Check will be performed for complex orders with other existing order checks when the pharmacy user takes various order entry actions as specified below:

- Entering a new IV or Unit Dose medication order
- Finishing a pending IV or Unit Dose medication order
- Renewing an IV or Unit Dose order
- Creating a new Unit Dose order when editing the orderable item (to a new orderable item)
- When editing the IV Additive fields (changing existing additive or adding new additive) for an IV order
- When editing the IV Solution fields (changing existing solution or adding a new solution) for an IV order - This applies only to IV Solutions marked as a PreMix.
- Entering a new Unit Dose medication order using order sets
- Copying an IV or Unit Dose medication order, thereby creating a new order.
- Editing the following for a Unit Dose order:
- Dosage Ordered
- Units per Dose (for Dispense Drug)
- Med Route
- Schedule
- Provider
- Start Date/Time
- Stop Date/Time
- Editing the following for an IV order
- Infusion rate (only applies to IV types of ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’ or ‘Chemotherapy Continuous Syringe’)
- Schedule (only applies to IV types of ‘Piggyback’, ‘Intermittent Syringe’, ‘Chemotherapy Piggyback’, or ‘Chemotherapy Intermittent Syringe’)
- Med Route
- Volume (does not apply to orders with IV types of ‘Piggyback’, ‘Intermittent Syringe’, ‘Chemotherapy Piggyback’, or ‘Chemotherapy Intermittent Syringe’ with IV Solution not marked as PreMix)
- Provider
- Start Date/Time
- Stop Date/Time

For all with the exception of Volume, only Dosing Order Checks will be performed.

- Verifying a non-verified IV or Unit Dose order (only if separate process from an action that would also trigger any other Order Checks)

Dosage checks are the last order check that is performed.

### Unit Dose Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Unit Dose Order

In the example below, a new unit dose order is entered through the pharmacy backdoor and generates both a Maximum Single Dose Order Check warning and Max Daily Dose Order Check.

New Unit Dose Order via backdoor pharmacy

PU Patient Record Update NO New Order Entry

Select Action: Quit// NO New Order Entry

Select DRUG: SIMVASTATIN

Lookup: GENERIC NAME

1 SIMVASTATIN 20MG TAB CV350

2 SIMVASTATIN 80MG TAB CV350

CHOOSE 1-2: 2 SIMVASTATIN 80MG TAB CV350

Restriction/Guideline(s) exist. Display? : (N/O): No// NO

<span id="Page_98" class="anchor"></span>

Enter RETURN to continue or '^' to exit:

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

Available Dosage(s)

1\. 80MG

2\. 160MG

Select from list of Available Dosages or Enter Free Text Dose: 120MG

You entered 120MG is this correct? Yes// YES

UNITS PER DOSE: 1// 1.5 1.5

MED ROUTE: ORAL// PO

1 ORAL PO

2 ORAL ORAL

CHOOSE 1-2: 1 ORAL PO

SCHEDULE: BID// QPM 2100

SCHEDULE TYPE: CONTINUOUS// CONTINUOUS

ADMIN TIMES: 2100//

SPECIAL INSTRUCTIONS:

<span id="Page_128" class="anchor"></span>START DATE/TIME: NOV 3,2011@10:48// NOV 3,2011@10:48

STOP DATE/TIME: NOV 17,2011@10:48// NOV 17,2011@10:48

Expected First Dose: NOV 3,2011@21:00

PROVIDER: PROVIDER,ONE//

NON-VERIFIED UNIT DOSE Nov 03, 2011@10:49:03 Page: 1 of 2

Ward: 5NM

PID: Room-Bed: Ht(cm): 170.00 (05/10/10)

DOB: 01/02/47 (64) Wt(kg): 90.00 (05/10/10)

(1)Orderable Item: SIMVASTATIN TAB \<DIN\>

Instructions:

(2)Dosage Ordered: 120MG

Duration: (3)Start: 11/03/2011 10:48

\(4\) Med Route: ORAL

\(5\) Stop: 11/17/2011 10:48

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: QPM

\(9\) Admin Times: 2100

\(10\) Provider: PROVIDER,ONE

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

SIMVASTATIN 80MG TAB 1.5

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

SIMVASTATIN 80MG TAB: Single dose of 120 milligrams exceeds the maximum

single dose of 80 milligrams.

SIMVASTATIN 80MG TAB: Total dose of 120 milligrams/day exceeds the

maximum daily dose of 80 milligrams/day.

Do you want to Continue? NO//

No order created.

Select DRUG:

.

.

.

\*\*\*\*\*OR\*\*\*\*\*\*\*\*\*

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For SIMVASTATIN 80MG TAB

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// O

NATURE OF ORDER: WRITTEN// W

...transcribing this non-verified order....

When entering a new Unit Dose order through the pharmacy backdoor, Dosing Order Checks will be performed after the user accepts the order. If the dosage ordered exceeds the FDB recommended maximum single dose or maximum daily dose, a warning message will be displayed to the user. The warning message will be indented and the drug name will precede the warning message.

If a Maximum Single Dose Order Check and/or Max Daily Dose Order Check warning is displayed, the user will be prompted with ‘Do you want to Continue?’ If the user accepts the default of ‘No’, the software will take them back to the ‘Select DRUG:’ prompt. If the user responds ‘Yes’, the program will proceed with the intervention dialog.

If the schedule within the order has been marked to be excluded from all Dosing Order Checks, no Dosing Order Checks will be performed. In this case, no message will be displayed to the user informing them of this. If the schedule within the order has been marked to be excluded from the Daily Dose Order Check, no Max Daily Dose Order Checks will be performed. No message will be displayed to the user informing them of this. In this case, the Maximum Single Dose Order Check will be performed.

If either Dosing Order Check cannot be performed, an error message is displayed. The user will not be asked to enter an intervention to continue.

#### New Unit Dose Order Using an Order Set

In the following example, new unit dose orders are being entered via pharmacy options using an order set.

New Unit Dose Order via pharmacy backdoor options using Order Set

Select Action: View Profile// NO New Order Entry

Select DRUG: S.DT DEMO (ORDER SET)

NATURE OF ORDER: WRITTEN// W

...entering INDOMETHACIN.....

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

NON-VERIFIED UNIT DOSE Mar 21, 2008@09:35:40 Page: 1 of 2

Ward: 3AS A

Room-Bed: Ht(cm): 187.96 (07/05/94)

DOB: 01/01/45 (63) Wt(kg): 77.27 (07/05/94)

(1)Orderable Item: INDOMETHACIN CAP,ORAL

Instructions:

(2)Dosage Ordered: 25MG

<span id="Page_130" class="anchor"></span> Duration: (3)Start: 03/21/2008 08:00

\(4\) Med Route: ORAL

\(5\) Stop: 06/19/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: TID

\(9\) Admin Times: 08-12-16

\(10\) Provider: PSJPROVIDER,ONE \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDOMETHACIN 25MG CAP 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// VF Verify

...a few moments, please.....

...entering FAMOTIDINE.....

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now processing Enhanced Order Checks. Please wait ...

NON-VERIFIED UNIT DOSE Mar 21, 2008@09:30:36 Page: 1 of 2

Ward: 3AS A

Room-Bed: Ht(cm): 187.96 (07/05/94)

DOB: 01/01/45 (63) Wt(kg): 77.27 (07/05/94)

(1)Orderable Item: FAMOTIDINE TAB \<DIN\>

Instructions:

(2)Dosage Ordered: 20MG

Duration: (3)Start: 03/21/2008 09:00

\(4\) Med Route: ORAL

\(5\) Stop: 06/19/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: BID

<span id="Page_101" class="anchor"></span> (9) Admin Times: 09-17

\(10\) Provider: PSJPROVIDER,ONE \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

FAMOTIDINE 20MG TAB 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// VF Verify

...a few moments, please.....

Pre-Exchange DOSES:

ORDER VERIFIED.

Enter RETURN to continue or '^' to exit:

...entering CLOPIDOGREL.....

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

CLOPIDOGREL 75MG TAB: Single dose of 150 milligrams exceeds the maximum

single dose of 75 milligrams.

CLOPIDOGREL 75MG TAB: Total dose of 300 milligrams/day exceeds the

maximum daily dose of 75 milligrams/day.

Recommended frequency of CLOPIDOGREL 75MG TAB: Frequency of 2

administrations per day exceeds the high frequency of 1 administration

per day.

Do you want to Continue? N// n NO

Select DRUG: .

.

Or

Do you want to Continue? N// YES

Now creating Pharmacy Intervention

for CLOPIDOGREL 75MG TAB

PROVIDER: PSJPROVIDER, ONE

RECOMMENDATION: NO CHANGE

See ‘Pharmacy Intervention Menu’ if you want to delete this intervention or for more options.

Would you like to edit this intervention? N// O

(1)Orderable Item: CLOPIDOGREL TAB

Instructions:

(2)Dosage Ordered: 150MG

Duration: (3)Start: 03/21/2008 09:00

\(4\) Med Route: ORAL

\(5\) Stop: 06/19/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: BID

\(9\) Admin Times: 09-17

\(10\) Provider: PSJPROVIDER,ONE \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

CLOPIDOGREL 75MG TAB 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen//

When entering new Unit Dose orders via a pharmacy order set through pharmacy options, Dosing Order Checks will be performed after any Duplicate Therapy order checks are displayed. Dosing Order Checks will be performed for each drug within the order set one by one.

If the user responds ‘No’ to the ‘Do you want to Continue?’ prompt, the program will take them back to the ‘Select Drug:’ prompt when the drug being entered is the last one in the order set to be processed. If not the last drug to be processed within the order set, the program will delete the drug and go on to the next drug within the order set.

#### Finishing a Complex Inpatient Medication Order

In the following example, a complex inpatient medication order has been entered through CPRS and finished in Pharmacy. Only a Maximum Single Dose Order Check will be performed on the complex order as a whole through CPRS. All orders within the complex order are released as separate orders to Inpatient Medications. When finishing the pending complex order through Inpatient Medications, each order is treated as a simple order and therefore both a Maximum Single Dose Order Check and Max Daily Dose Order Check are performed in MOCHA v2.1b.

Finishing Pending Complex Inpatient Medication order

Inpatient Order Entry Oct 23, 2024@15:50:39 Page: 1 of 1

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): 162.56 (10/23/24)

DOB: 10/23/70 (54) Att: INPATIENT-MEDS,PROVIDERWt(kg): 85.00 (10/23/24)

Sex: MALE TrSp: MEDICAL OBSERVATI Admitted: 10/23/24

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.90

\- - - - - - - - - - - - - P E N D I N G C O M P L E X - - - - - - - - - - - -

1 WARFARIN TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 30MG PO QD

WARFARIN TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 40MG PO QD

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// 1

PENDING UNIT DOSE (ROUTINE) Oct 23, 2024@15:51:08 Page: 1 of 3

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): 162.56 (10/23/24)

DOB: 10/23/70 (54) Att: INPATIENT-MEDS,PROVIDERWt(kg): 85.00 (10/23/24)

\*(1)Orderable Item: WARFARIN TAB \<DIN\>

Instructions: 30MG

\*(2)Dosage Ordered: 30MG

Duration: 3 days (3)Start: 10/24/2024 10:00

\*(4) Med Route: ORAL (BY MOUTH) Calc Start: 10/23/2024 15:41

\(5\) Stop: 10/27/2024 10:00

\(6\) Schedule Type: CONTINUOUS Calc Stop: 11/07/2024 10:00

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider: INPATIENT-MEDS,PROVIDER

\(11\) Special Instructions:

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

\+ INVALID DISPENSE DRUG

BY Bypass FL Flag

DC Discontinue FN Finish

Select Item(s): Next Screen// FN Finish

PLEASE NOTE: This order must have at least one DISPENSE DRUG before it can be

finished.

CHOOSE FROM:

1\. WARFARIN 10MG TAB

2\. WARFARIN SODIUM 5MG S.T.

3\. WARFARIN 2MG TABS

Select DISPENSE DRUG(S) for this order: 1

WARFARIN 10MG TAB

UNITS PER DOSE: 1// 3

--------------------------------------------------------------------------------

\*\*\*\*\* WARNING \*\*\*\*\*

WARFARIN is hazardous to handle and dispose. Please take the

appropriate handling and disposal precautions.

--------------------------------------------------------------------------------

Press Return to continue:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

WARFARIN 10MG TAB: Single dose of 30 milligrams exceeds the maximum

single dose of 20 milligrams.

WARFARIN 10MG TAB: Total dose of 30 milligrams/day exceeds the maximum

daily dose of 20 milligrams/day.

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For WARFARIN 10MG TAB

PROVIDER: INPATIENT-MEDS,PROVIDER PROV

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N//

NON-VERIFIED UNIT DOSE Oct 23, 2024@15:53:21 Page: 1 of 3

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): 162.56 (10/23/24)

DOB: 10/23/70 (54) Att: INPATIENT-MEDS,PROVIDERWt(kg): 85.00 (10/23/24)

\*(1)Orderable Item: WARFARIN TAB \<DIN\>

Instructions: 30MG

\*(2)Dosage Ordered: 30MG

Duration: 3 days (3)Start: 10/24/2024 10:00

\*(4) Med Route: ORAL (BY MOUTH) Calc Start: 10/23/2024 15:41

\(5\) Stop: 10/27/2024 10:00

\(6\) Schedule Type: CONTINUOUS Calc Stop: 11/07/2024 10:00

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider: INPATIENT-MEDS,PROVIDER

\(11\) Special Instructions:

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

WARFARIN 10MG TAB 3

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

...accepting order........

PENDING UNIT DOSE (ROUTINE) Oct 23, 2024@15:54:01 Page: 1 of 3

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): 162.56 (10/23/24)

DOB: 10/23/70 (54) Att: INPATIENT-MEDS,PROVIDERWt(kg): 85.00 (10/23/24)

\*(1)Orderable Item: WARFARIN TAB \<DIN\>

Instructions: 40MG

\*(2)Dosage Ordered: 40MG

Duration: 5 days (3)Start: 10/27/2024 10:00

\*(4) Med Route: ORAL (BY MOUTH) Calc Start: 10/23/2024 15:41

\(5\) Stop: 11/01/2024 10:00

\(6\) Schedule Type: CONTINUOUS Calc Stop: 11/10/2024 10:00

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider: INPATIENT-MEDS,PROVIDER

\(11\) Special Instructions:

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

\+ INVALID DISPENSE DRUG

BY Bypass FL Flag

DC Discontinue FN Finish

Select Item(s): Next Screen// FN Finish

PLEASE NOTE: This order must have at least one DISPENSE DRUG before it can be

finished.

CHOOSE FROM:

1\. WARFARIN 10MG TAB

2\. WARFARIN SODIUM 5MG S.T.

3\. WARFARIN 2MG TABS

Select DISPENSE DRUG(S) for this order: 1

WARFARIN 10MG TAB

UNITS PER DOSE: 1// 4

--------------------------------------------------------------------------------

\*\*\*\*\* WARNING \*\*\*\*\*

WARFARIN is hazardous to handle and dispose. Please take the

appropriate handling and disposal precautions.

--------------------------------------------------------------------------------

Press Return to continue:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

WARFARIN 10MG TAB: Single dose of 40 milligrams exceeds the maximum

single dose of 20 milligrams.

WARFARIN 10MG TAB: Total dose of 40 milligrams/day exceeds the maximum

daily dose of 20 milligrams/day.

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For WARFARIN 10MG TAB

PROVIDER: INPATIENT-MEDS,PROVIDER PROV

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N//

NON-VERIFIED UNIT DOSE Oct 23, 2024@15:59:39 Page: 1 of 3

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): 162.56 (10/23/24)

DOB: 10/23/70 (54) Att: INPATIENT-MEDS,PROVIDERWt(kg): 85.00 (10/23/24)

\*(1)Orderable Item: WARFARIN TAB \<DIN\>

Instructions: 40MG

\*(2)Dosage Ordered: 40MG

Duration: 5 days (3)Start: 10/27/2024 10:00

\*(4) Med Route: ORAL (BY MOUTH) Calc Start: 10/23/2024 15:41

\(5\) Stop: 11/01/2024 10:00

\(6\) Schedule Type: CONTINUOUS Calc Stop: 11/10/2024 10:00

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider: INPATIENT-MEDS,PROVIDER

\(11\) Special Instructions:

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

WARFARIN 10MG TAB 4

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

...accepting order........

Inpatient Order Entry Oct 23, 2024@16:00 Page: 1 of 1

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): 162.56 (10/23/24)

DOB: 10/23/70 (54) Att: INPATIENT-MEDS,PROVIDERWt(kg): 85.00 (10/23/24)

Sex: MALE TrSp: MEDICAL OBSERVATI Admitted: 10/23/24

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 1.90

\- - - - - - - - - - N O N - V E R I F I E D C O M P L E X - - - - - - - - - -

1 WARFARIN TAB C 10/24/2024 10/27/2024 N

Give: 30MG PO QD

WARFARIN TAB C 10/27/2024 11/01/2024 N

Give: 40MG PO QD

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Quit//

<span id="Page_103" class="anchor"></span>A pharmacy intervention shall be required to be logged if the user wishes to continue with the order if any Dosing Order Check warnings were generated. The intervention type shall be set to ‘MAX SINGLE DOSE' if only a Maximum Single Dose Order Check warning was displayed. The intervention type will be set to ‘MAX DAILY DOSE’ if only a Max Daily Dose Order Check warning was displayed. If both Maximum Single Dose and Max Daily Dose Order Check warnings were displayed, the intervention type will be set to ‘MAX SINGLE DOSE & MAX DAILY DOSE’.

#### Renewing an Order

The following example illustrates renewing an inpatient medication order that was entered through CPRS.

Renewing Unit Dose Order

<span id="Page_108" class="anchor"></span>ACTIVE UNIT DOSE Nov 21, 2011@13:38:39 Page: 1 of 2

Ward: 3AS A

PID: Room-Bed: 300-3 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 05/30/40 (71) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: FAMOTIDINE TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 80MG

Duration: \*(3)Start: 11/21/2011 17:00

\*(4) Med Route: ORAL Renewed: 11/21/2011 13:38

\*(5) Stop: 02/01/2012 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: BID

\(9\) Admin Times: 09-17

\*(10) Provider: PROVIDER,ONE \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

FAMOTIDINE 20MG TAB 4

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// rn Renew

RENEW THIS ORDER? YES//

STOP DATE/TIME: FEB 1,2012@24:00// FEB 1,2012@24:00

Expected First Dose: NOV 21,2011@17:00

PROVIDER: PROVIDER,ONE// AA3333333 123

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

================================================================================

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es) as FAMOTIDINE 20MG

TAB:

FAMOTIDINE TAB C 11/03 02/01 A

<span id="Page_109" class="anchor"></span>Give: 20MG PO BID

Pending Outpatient Drug for SUCRALFATE 1GM TAB

SIG: TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY

Class(es) Involved in Therapeutic Duplication(s): Peptic Ulcer Agents,

Histamine-2 Receptor Antagonists (H2 Antagonists)

================================================================================

Do you wish to continue with the current order? YES//

Press Return to continue...

FAMOTIDINE TAB C 11/03 02/01 A

Give: 20MG PO BID

Do you want to discontinue the above order? No// (No)

FAMOTIDINE 20MG TAB: Single dose of 80 milligrams exceeds the maximum

single dose of 40 milligrams.

FAMOTIDINE 20MG TAB: Total dose of 160 milligrams/day exceeds the

maximum daily dose of 80 milligrams/day.

Do you want to Continue? NO// n NO

No changes made to this order.

Enter RETURN to continue or '^' to exit:

FL Flag VF (Verify)

ACTIVE UNIT DOSE Nov 21, 2011@13:40:16 Page: 1 of 2

Ward: 3AS A

PID: Room-Bed: 300-3 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 05/30/40 (71) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: FAMOTIDINE TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 80MG

Duration: \*(3)Start: 11/21/2011 17:00

\*(4) Med Route: ORAL Renewed: 11/21/2011 13:38

\*(5) Stop: 02/01/2012 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: BID

\(9\) Admin Times: 09-17

\*(10) Provider: PROVIDER,ONE \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

FAMOTIDINE 20MG TAB 4

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen//

If Dosing Order Check warnings are generated and the user responds ‘No’ to the ‘Do you want to Continue?’ prompt for the following pharmacy order entry processes, the software shall take them back to the point where they initiated the action for the following processes as in the example above.

- Finishing a pending Unit Dose medication order
- Renewing a Unit Dose order
- Creating a new Unit Dose order when editing the orderable item (to a new orderable item) through pharmacy options
- Entering a new Unit Dose medication order through pharmacy options using order sets
- Copying a Unit Dose medication order, thereby creating a new order
- Editing the following for a Unit Dose order:
- Dosage Ordered
- Units per Dose (for Dispense Drug)
- Med Route
- Schedule
- Provider
- Start Date/Time
- Stop Date/Time

Dosage checks will be the last order checks performed as documented in the order check display sequence Section 3.1.3 of this documentation.

#### Edit of an Order

In the following example, the Dosage Ordered is edited and thereby creates a new unit dose order.

Editing Dosage Ordered –Creating New Unit Dose order

ACTIVE UNIT DOSE Apr 21, 2008@14:37:23 Page: 1 of 2

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

--------------------------------------------------------------------------------------

\*(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

\*(2)Dosage Ordered: 400MG

Duration: \*(3)Start: 04/21/2008 14:00

\*(4) Med Route: ORAL

\*(5) Stop: 04/28/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q8H

\(9\) Admin Times: 0600-1400-2200

\*(10) Provider: PSJPROVIDER,TWO \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR 400MG CAP 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// ED Edit

Select FIELDS TO EDIT: 2

Available Dosage(s)

1\. 400MG

2\. 800MG

Select from list of Available Dosages or Enter Free Text Dose: 400MG// 1600

You entered 1600MG is this correct? Yes// YES

> **WARNING:** Dosage Ordered and Dispense Units do not match.

Please verify Dosage.

Enter RETURN to continue or '^' to exit:

ED Edit AC ACCEPT

NON-VERIFIED UNIT DOSE Apr 21, 2008@14:39:38 Page: 1 of 2

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

\*(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

\*(2)Dosage Ordered: 1600MG

Duration: \*(3)Start: 04/21/2008 14:00

\*(4) Med Route: ORAL

\*(5) Stop: 04/28/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q8H

\(9\) Admin Times: 0600-1400-2200

\*(10) Provider: PSJPROVIDER,TWO

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR 400MG CAP 1

\+ This change will cause a new order to be created.

Select Item(s): Next Screen// ED Edit

Select FIELDS TO EDIT: 12

Select DISPENSE DRUG: INDINAVIR 400MG CAP//

UNITS PER DOSE: 1// 4

INACTIVE DATE:

Select DISPENSE DRUG:

NON-VERIFIED UNIT DOSE Apr 21, 2008@14:40:29 Page: 1 of 2

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

\*(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

\*(2)Dosage Ordered: 1600MG

Duration: \*(3)Start: 04/21/2008 14:00

\*(4) Med Route: ORAL

\*(5) Stop: 04/28/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q8H

\(9\) Admin Times: 0600-1400-2200

\*(10) Provider: PSJPROVIDER,TWO

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR 400MG CAP 4

\+ This change will cause a new order to be created.

ED Edit AC ACCEPT

<span id="Page_112" class="anchor"></span>Select Item(s): Next Screen// AC ACCEPT

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

INDINAVIR 400MG CAP: Single dose of 1,600 milligrams exceeds the maximum

single dose of 1,200 milligrams.

INDINAVIR 400MG CAP: Total dose of 4,800 milligrams/day exceeds the maximum

daily dose of 3,000 milligrams/day.

Do you want to Continue? N// n NO

No changes made to this order.

Press Return to continue...:

ACTIVE UNIT DOSE Apr 21, 2008@14:37:23 Page: 1 of 2

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

\*(1)Orderable Item: INDINAVIR CAP,ORAL \<OCI\>

Instructions:

\*(2)Dosage Ordered: 400MG

Duration: \*(3)Start: 04/21/2008 14:00

\*(4) Med Route: ORAL

\*(5) Stop: 04/28/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q8H

\(9\) Admin Times: 0600-1400-2200

\*(10) Provider: PSJPROVIDER,TWO \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR 400MG CAP 1

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

.

.

OR

Do you want to Continue? N// ES

Now creating Pharmacy Intervention

for INDINAVIR 400MG CAP

PROVIDER: OPPROVIDER, ONE

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// NO

NATURE OF ORDER: SERVICE CORRECTION// S

...discontinuing original order...

...creating new order...(you will now work on this new order).

FL Flag VF Verify

NON-VERIFIED UNIT DOSE Apr 21, 2008@14:40:54 Page: 1 of 2

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

\*(1)Orderable Item: INDINAVIR CAP,ORAL

Instructions:

\*(2)Dosage Ordered: 1200MG

Duration: \*(3)Start: 04/21/2008 14:00

\*(4) Med Route: ORAL

\*(5) Stop: 04/28/2008 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q8H

\(9\) Admin Times: 0600-1400-2200

\*(10) Provider: PSJPROVIDER,TWO

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

INDINAVIR 400MG CAP 3

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen//

Shown in this previous example, when editing orders, the Dosing Order Checks will be performed after all edits are complete and the user accepts the order.

#### Copy a Unit Dose Order

In the following example, a copy of a unit dose order is performed.

Copy a Unit Dose Order

ACTIVE UNIT DOSE Aug 17, 2012@15:27:26 Page: 1 of 2

Ward: 7AS

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 06/09/25 (87) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: GABAPENTIN TAB

Instructions:

\*(2)Dosage Ordered: 2400MG

Duration: \*(3)Start: 08/15/2012 07:56

\*(4) Med Route: ORAL

\*(5) Stop: 11/23/2012 11:59

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: TID

\(9\) Admin Times: 09-13-17

\*(10) Provider: PROVIDER,ONE \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

GABAPENTIN 600MG TAB 4

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// co CO

Do you want to copy this order? No//Y (Yes)

..copying….

ACTIVE UNIT DOSE Aug 17, 2012@15:28:07 Page: 1 of 2

Ward: 7AS

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 06/09/25 (87) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

(1)Orderable Item: GABAPENTIN TAB

Instructions:

(2)Dosage Ordered: 2400MG

Duration: (3)Start: 08/17/2012 15:28

\(4\) Med Route: ORAL

\(5\) Stop: 11/25/2012 11:59

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: TID

\(9\) Admin Times: 09-13-17

\(10\) Provider: PROVIDER,ONE \[w\]

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

GABAPENTIN 600MG TAB 4

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// ac ACCEPT

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

GABAPENTIN 600MG TAB: Single dose of 2,400 milligrams exceeds the maximum

single dose of 1,200 milligrams.

GABAPENTIN 600MG TAB: Total dose of 7,200 milligrams/day exceeds the

maximum daily dose of 3,600 milligrams/day.

Do you want to Continue? Y//

Now creating Pharmacy Intervention

For GABAPENTIN 600MG TAB

PROVIDER: PROVIDER,ONE OP

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// O

NATURE OF ORDER: WRITTEN// W

...transcribing this active order.....

Pre-Exchange DOSES:

#### Renew a Unit Dose Order - Free Text Dosage Error

In the example below, a free text dosage has been entered that the software cannot interpret. It is a Local Possible Dosage for which the Numeric Dose and Dose Unit are not defined.

Renew a Unit Dose Order - Free Text Dosage Error

ACTIVE UNIT DOSE Nov 03, 2011@15:31:46 Page: 1 of 2

Ward: 3AS A

PID: Room-Bed: 300-3 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 05/30/40 (71) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: ALBUTEROL SOLN,INHL

Instructions:

\*(2)Dosage Ordered: 1 DOCDOSE

Duration: \*(3)Start: 10/21/2024 14:24

\*(4) Med Route: INHALATION

\*(5) Stop: 11/04/2024 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: Q4H

\(9\) Admin Times: 01-05-09-13-17-21

\*(10) Provider: TESTDEMO,THREE \[s\]

\(11\) Special Instructions:

\(14\) Indication:

\(12\) Dispense Drug U/D Inactive Date

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// RN Renew

RENEW THIS ORDER? YES//

STOP DATE/TIME: NOV 4,2024@24:00// NOV 4,2024@24:00

Expected First Dose: OCT 21,2024@17:00

PROVIDER: TESTDEMO,THREE//

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Dosing Checks could not be performed for Drug: ALBUTEROL 0.083% INHL

SOLN

Reason(s): Free Text Dosage could not be evaluated

General dosing range for ALBUTEROL 0.083% INHL SOLN (INHALATION): 3

milliliter/day to 24 milliliter/day. Maximum daily dose is 216

milliliter/day.

Press Return to continue...

NATURE OF ORDER: WRITTEN// W

Pre-Exchange DOSES:

...updating order.....DONE!

In this example, an error message stating that the free text dosage cannot be evaluated is displayed to the Pharmacy user because the dosage ordered of ‘1 DOCDOSE’ does not have a Numeric Dose and Dose Unit defined for the Local Possible Dosage selected. Dosing Order Checks cannot be performed. A general dosing information message that lists the normal dosage range and the maximum daily dose for the drug is also displayed. The user is not asked if they want to continue nor prompted to enter a pharmacy intervention.

#### Verifying a non-verified Unit Dose Order

In the following example, a pharmacist has selected a non-verified unit dose order and taken the VERIFY action. Upon taking the action, order checks will be processed. In this example a Maximum Single Dose Order Check warning and a Max Daily Dose Order Check warning are displayed. Had the VERIFY action been taken with any other action that triggers order checks, order checks would have only been displayed once.

Verifying a non-verified Unit Dose Order

<u>Inpatient Order Entry Oct 21, 2024@15:50:32 Page: 1 of 1</u>

Ward: 3 NORTH A

PID: Room-Bed: 1-3 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 06/14/51 (61) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 08/19/97

Dx: TESTING ALERT Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

1 ISONIAZID TAB C 08/24/2023 09/07/2023 N

Give: 100MG PO TID

2 WARFARIN TAB C 10/21/2024 11/04/2024 N

Give: 40MG PO QD

\- - - - - - - - - - - - - - - - - CLINIC (45) - - - - - - - - - - - - - - - - -

3 ISONIAZID TAB C 08/24/2023 09/07/2023 N

Give: 100MG PO QD

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// 2

<u>NON-VERIFIED UNIT DOSE Oct 21, 2024@15:51:47 Page: 1 of 2</u>

Ward: 3 NORTH A

PID: Room-Bed: 1-3 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 06/14/51 (61) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: WARFARIN TAB \<DIN\>

Instructions:

\*(2)Dosage Ordered: 40MG

Duration: (3)Start: 10/21/2024 15:10

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 11/04/2024 15:10

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider: TESTDEMO,THREE \[s\]

\(11\) Special Instructions:

\(14\) Indication:

\(12\) Dispense Drug U/D Inactive Date

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// VF Verify

--------------------------------------------------------------------------------

\*\*\*\*\* WARNING \*\*\*\*\*

WARFARIN is hazardous to handle and dispose. Please take the

appropriate handling and disposal precautions.

--------------------------------------------------------------------------------

Press Return to continue:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

WARFARIN 10MG TAB: Single dose of 40 milligrams exceeds the maximum

single dose of 20 milligrams.

WARFARIN 10MG TAB: Total dose of 40 milligrams/day exceeds the maximum

daily dose of 20 milligrams/day.

Do you want to Continue? NO//

<span id="Page_117" class="anchor"></span>

<u>NON-VERIFIED UNIT DOSE Oct 21, 2024@15:52:59 Page: 1 of 2</u>

Ward: 3 NORTH A

PID: Room-Bed: 1-3 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 06/14/51 (61) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: WARFARIN TAB

Instructions:

\*(2)Dosage Ordered: 40MG

Duration: (3)Start: 10/21/2024 15:10

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 11/04/2024 15:10

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider: TESTDEMO,THREE \[s\]

\(11\) Special Instructions:

\(14\) Indication:

\(12\) Dispense Drug U/D Inactive Date

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen//

#### Editing and then Verifying a Non-Verified Unit Dose Order

In the following example, a non-verified unit dose order is edited and then verified through pharmacy backdoor options within a single order session. Only Dosing Order Checks are generated when the Units per Dose field for the dispense drug Warfarin 10mg tab is edited from 4 to 5. Upon verification, enhanced order checks are processed and a drug interaction between Amiodarone and Warfarin is displayed for processing. Dosing Order Checks are not displayed again. In this case, since Dosing Order Checks were triggered during the Edit action, the same order check will not be displayed again during the Verify action.

<span id="Page_118" class="anchor"></span>Non-verified Unit Dose Order Edited and then Verified through pharmacy backdoor options

Inpatient Order Entry Apr 30, 2025@22:26:10 Page: 1 of 1

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/01/61 (64) Att: Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE TrSp: MEDICAL OBSERVATI Admitted: 04/29/25

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 AMIODARONE TAB C 04/29/2025 05/13/2025 A

Give: 200MG PO TID

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

2 WARFARIN TAB C 04/30/2025 05/14/2025 N

Give: 40MG PO QD

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Quit// 2

NON-VERIFIED UNIT DOSE Apr 30, 2025@22:26:43 Page: 1 of 2

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/01/61 (64) Att: Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: WARFARIN TAB \<OCI\>\<DIN\>

Instructions:

\*(2)Dosage Ordered: 40MG

Duration: (3)Start: 04/30/2025 22:26

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 05/14/2025 22:26

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider:

\(11\) Special Instructions:

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen//

Scrolled down to show the Dispensing Information.

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

WARFARIN 10MG TAB 4

(7)Self Med: NO

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// 12

Select DISPENSE DRUG: WARFARIN 10MG TAB//

DISPENSE DRUG: WARFARIN 10MG TAB//

UNITS PER DOSE: 4// 5

Select DISPENSE DRUG:

> **WARNING:** Dosage Ordered and Dispense Units do not match.

Please verify Dosage.

Type \<Enter\> to continue or '^' to exit:

NON-VERIFIED UNIT DOSE Apr 30, 2025@22:27:57 Page: 1 of 2

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/01/61 (64) Att: Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: WARFARIN TAB \<OCI\>\<DIN\>

Instructions:

\*(2)Dosage Ordered: 40MG

Duration: (3)Start: 04/30/2025 22:26

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 05/14/2025 22:26

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider:

\(11\) Special Instructions:

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

WARFARIN 10MG TAB 5

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

WARFARIN 10MG TAB: Single dose of 40 milligrams exceeds the maximum

single dose of 20 milligrams.

WARFARIN 10MG TAB: Total dose of 40 milligrams/day exceeds the maximum

daily dose of 20 milligrams/day.

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For WARFARIN 10MG TAB

PROVIDER:

RECOMMENDATION: 9 OTHER

OTHER FOR RECOMMENDATION:

Edit? NO//

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

...updating order......

...updating OE/RR...

NON-VERIFIED UNIT DOSE Apr 30, 2025@22:28:54 Page: 1 of 2

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/01/61 (64) Att: Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\+

\*(4) Med Route: ORAL (BY MOUTH)

\(5\) Stop: 05/14/2025 22:26

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QD

\(9\) Admin Times: 1000

\*(10) Provider:

\(11\) Special Instructions:

\(14\) Indication: TESTING

\(12\) Dispense Drug U/D Inactive Date

WARFARIN 10MG TAB 5

(7)Self Med: NO

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD (Hold) RN (Renew)

FL Flag VF Verify

Select Item(s): Next Screen// VF Verify

--------------------------------------------------------------------------------

\*\*\*\*\* WARNING \*\*\*\*\*

WARFARIN is hazardous to handle and dispose. Please take the

appropriate handling and disposal precautions.

--------------------------------------------------------------------------------

Press Return to continue:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

================================================================================

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with WARFARIN 10MG TAB:

AMIODARONE TAB C 04/29 05/13 A

Give: 200MG PO TID

The concurrent administration of amiodarone and a coumarin anticoagulant

may result in an increase in the clinical effects of the anticoagulant and

an increased risk of bleeding.(1-23) It may take several weeks of

concurrent therapy before the full effects of this interaction are noted.

The effect of amiodarone on anticoagulant levels may continue for several

months after amiodarone is discontinued.

================================================================================

Display Professional Interaction Monograph(s)? NO//

Do you want to Continue with WARFARIN 10MG TAB? NO// YES

Now creating Pharmacy Intervention

For WARFARIN 10MG TAB

PROVIDER:

RECOMMENDATION: 9 OTHER

OTHER FOR RECOMMENDATION:

Edit? NO//

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

> **WARNING:** Dosage Ordered and Dispense Units do not match.

Please verify Dosage.

Would you like to continue verifying the order? No// YES

...a few moments, please.....

Pre-Exchange DOSES:

ORDER VERIFIED.

Type \<Enter\> to continue or '^' to exit:

Inpatient Order Entry Apr 30, 2025@22:31:25 Page: 1 of 1

Ward: OBSERVATION

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/01/61 (64) Att: Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE TrSp: MEDICAL OBSERVATI Admitted: 04/29/25

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 AMIODARONE TAB C 04/29/2025 05/13/2025 A

Give: 200MG PO TID

2 WARFARIN TAB C 04/30/2025 05/14/2025 A

Give: 40MG PO QD

Enter ?? for more actions

PI Patient Information NO New Order Entry

PU Patient Record Update CM New Clinic Medication Entry

SO Select Order

Select Action: Quit//<span id="Page_149" class="anchor"></span>

#### Schedule Exclusions

A schedule can be excluded from all Dosing Checks or just the Daily Dose Check. If such a schedule is used within an inpatient unit dose order, depending on which exclusion is applied, all Dosing Checks or just the Daily Dose Order Check will not be performed.

#### High Single Dose and Schedule Excluded from Daily Dose Order Check

In this example, a high single dose is entered for a unit dose order via an edit and the schedule has been excluded from the Daily Dose Order Check. Upon acceptance of the order and after all the order checks are performed, a high dose warning for the single dose will be displayed with the general dosing information message. No message will be displayed to the user indicating that the Daily Dose Order Check was not performed.

High Single Dose and Schedule Excluded from Daily Dose Order Check

<u>ACTIVE UNIT DOSE Jun 07, 2017@13:24:07 Page: 1 of 2</u>

Ward: GASTRO A

PID: Room-Bed: 600-A Ht(cm): 182.88 (11/14/93)

DOB: 01/01/40 (77) Wt(kg): 90.72 (11/14/93)

\*(1)Orderable Item: HALOPERIDOL TAB

Instructions:

\*(2)Dosage Ordered: 60MG

Duration: \*(3)Start: 06/07/2017 13:24

\*(4) Med Route: ORAL

\*(5) Stop: 07/07/2017 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: TID

\(9\) Admin Times: 09-13-17

\*(10) Provider: PROVIDER,ONE

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

HALOPERIDOL 20MG TAB 3

\+ This change will cause a new order to be created.

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

HALOPERIDOL 10MG S.T.: Single dose of 60 milligrams exceeds the maximum

single dose of 40 milligrams.

General dosing range for HALOPERIDOL 10MG S.T. (ORAL): 0.25

milligram/day to 100 milligram/day. Maximum daily dose is 100

milligram/day.

Do you want to Continue? NO//

.

.

.

#### Maximum Single Dose Order Check could not be Performed and Schedule Excluded from Daily Dose Order Check

In this example, a free text dosage range which cannot be evaluated is entered for a unit dose order via an edit and the schedule has been excluded from the Daily Dose Order Check. Upon acceptance of the order, after all order checks have been performed, a message that the Maximum Single Dose Order Check could not be performed is displayed with the general dosing information message. No message will be displayed to the user indicating that the Daily Dose Order Check was not performed.

Maximum Single Dose Order check could not be performed and Schedule Excluded from Daily Dose Order Check

<u>ACTIVE UNIT DOSE Jun 07, 2017@13:35 Page: 1 of 2</u>

Ward: GASTRO A

PID: Room-Bed: 600-A Ht(cm): 182.88 (11/14/93)

DOB: 01/01/40 (77) Wt(kg): 90.72 (11/14/93)

\*(1)Orderable Item: HALOPERIDOL TAB

Instructions:

\*(2)Dosage Ordered: 20-40MMG

Duration: \*(3)Start: 06/07/2017 13:35

\*(4) Med Route: ORAL

\*(5) Stop: 07/07/2017 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: TID

\(9\) Admin Times: 09-13-17

\*(10) Provider: PROVIDER,ONE

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

HALOPERIDOL 20MG TAB 3

\+ This change will cause a new order to be created.

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

Maximum Single Dose Check could not be performed for Drug: HALOPERIDOL

20MG TAB

Reason(s): Free Text Dosage could not be evaluated

General dosing range for HALOPERIDOL 20MG TAB (ORAL): 0.25 milligram/day

to 100 milligram/day. Maximum daily dose is 100 milligram/day.

Press Return to continue...

#### Schedule Excluded from All Dosing Order Checks

In this example, a high single dose and a schedule that would normally result in a high single dose warning and a high daily dose warning is entered for a unit dose order via an edit. Upon acceptance of the order, and all other order checks are performed, no dosing messages are displayed to the user. The schedule in the order was excluded from all Dosing Checks. No Maximum Single Dose Order Check or Max Daily Dose Order Check is performed. No message will be displayed to the user indicating that no Dosing Checks were performed.

Schedule Excluded from All Dosing Order Checks

<u>ACTIVE UNIT DOSE Jun 07, 2017@13:43:07 Page: 1 of 2</u>

Ward: GASTRO A

PID: Room-Bed: 600-A Ht(cm): 182.88 (11/14/93)

DOB: 01/01/40 (77) Wt(kg): 90.72 (11/14/93)

\*(1)Orderable Item: HALOPERIDOL TAB

Instructions:

\*(2)Dosage Ordered: 60MG

Duration: \*(3)Start: 06/07/2017 13:43

\*(4) Med Route: ORAL

\*(5) Stop: 07/07/2017 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: TID

\(9\) Admin Times: 09-13-17

\*(10) Provider: PROVIDER,ONE

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

HALOPERIDOL 20MG TAB 3

\+ This change will cause a new order to be created.

ED Edit AC ACCEPT

Select Item(s): Next Screen// ac ACCEPT

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Enhanced Order Checks cannot be performed for Local Drug: ALBUTEROL INHALER

17GM

Reason(s): Drug not matched to NDF

Press Return to continue...

NATURE OF ORDER: SERVICE CORRECTION// S

...discontinuing original order...

...creating new order.....

Pre-Exchange DOSES:

.

.

.

#### Per Orifice Note

When a high dose warning or general dosing information message is displayed to the user it will be prefaced with a note informing the user that the dosing information is per orifice. This will be done for drugs administered by the eye, ear, or nose. The mapping of the local medication route within the order to the standard medication routes of ‘NASAL’, ‘OPHTHALMIC’, and ‘OTIC’ will identify whether or not the drug is administered by the eye, ear or nose.

#### High Dose Warnings

In this example, a new unit dose order is entered which results in a maximum single dose warning and a max daily dose warning. The high dose warnings are prefaced with the text ‘Dosing Information provided is PER NOSTRIL:’ and it is only displayed once.

High Dose Warnings

Select Action: Next Screen// NO New Order Entry

Select DRUG: CROMOL

Lookup: GENERIC NAME

CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML NT900

...OK? Yes// (Yes)

Remote data not available - Only local order checks processed.

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Enhanced Order Checks cannot be performed for Local Drug: ALBUTEROL INHALER

17GM

Reason(s): Drug not matched to NDF

Press Return to continue...

======================================================================

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es) as CROMOLYN 40MG/ML

(4%) NASAL SPRAY 26ML:

Local Rx \#3642 (ACTIVE) for CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML

SIG: INSTILL 5 SPRAYS NASAL TWICE A DAY

Processing Status: Not released locally (Window)

Class(es) Involved in Therapeutic Duplication(s): Nasal Mast Cell

Stabilizers

======================================================================

Press Return to continue...

DOSAGE ORDERED: 5 SPRAYS

You entered 5 SPRAYS is this correct? Yes// YES

UNITS PER DOSE: 1//

MED ROUTE: ORAL// NASAL

1 NASAL NA

2 NASAL NASAL

CHOOSE 1-2: 2 NASAL NASAL

SCHEDULE: BID

1 BID 09-17

2 BIDAC 07-16

3 BIDTST

CHOOSE 1-3: 1 BID 09-17

SCHEDULE TYPE: CONTINUOUS// CONTINUOUS

ADMIN TIMES: 09-17//

SPECIAL INSTRUCTIONS:

1\>

START DATE/TIME: JUN 7,2017@15:56// JUN 7,2017@15:56

STOP DATE/TIME: JUL 7,2017@24:00// JUL 7,2017@24:00

Expected First Dose: JUN 7,2017@17:00

<u>ACTIVE UNIT DOSE Jun 07, 2017@15:56:32 Page: 1 of 2</u>

Ward: GASTRO A

PID: Room-Bed: 600-A Ht(cm): 182.88 (11/14/93)

DOB: 01/01/40 (77) Wt(kg): 90.72 (11/14/93)

(1)Orderable Item: CROMOLYN SOLN,NASAL

Instructions:

(2)Dosage Ordered: 5 SPRAYS

<span id="Page_157" class="anchor"></span> Duration: (3)Start: 06/07/2017 15:56

\(4\) Med Route: NASAL

\(5\) Stop: 07/07/2017 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: BID

\(9\) Admin Times: 09-17

\(10\) Provider: PROVIDER,ONE

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML 1

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

Dosing Information provided is PER NOSTRIL:

CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML: Single dose of 5 sprays exceeds the

maximum single dose of 1 spray.

CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML: Total dose of 10 sprays/day exceeds

the maximum daily dose of 6 sprays/day.

Do you want to Continue? NO//

.

.

.

#### General Dosing Information Message

In this example, a schedule is entered for a unit dose order that does not have a frequency defined. After the Dosing Order Checks are performed, a message that the Max Daily Dose Order Check could not be performed is displayed with the general dosing information message. The General Dosing Information message is prefaced with the text ‘Dosing Information provided is PER EAR:’ If the dosing check information could not have been displayed on one page, the per orifice note text would have been repeated on each additional page for high dose warnings and general dosing information messages.

General Dosing Information Message

DRUG:    ACETIC ACID 2% OTIC SOL 15 ML          OT109          

         ...OK? Yes//   (Yes)

Now doing allergy checks.  Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks!  Please wait...

There are 2 Available Dosage(s):

       1. 1 DROP
       2. 2 DROP

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 5 DROPS 5 DROPS

You entered 5 DROPS is this correct? Yes//   YES

VERB: INSTILL

ROUTE: //OTIC        OTIC 

Schedule: FREQTEST

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

  FREQTEST  FREQTEST 

         ...OK? Yes//   (Yes)

(FREQTEST)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

   Max Daily Dose Check could not be performed for Drug: ACETIC ACID 2%

   OTIC SOL 15 ML

     Reason(s): Invalid or Undefined Frequency

Dosing Information provided is PER EAR:    General dosing range for ACETIC ACID

2% OTIC SOL 15 ML  (OTIC (EAR)): 12

   drop/day to 30 drop/day. Maximum daily dose is 30 drop/day. 

PATIENT INSTRUCTIONS: //

#### Max Daily Dose Order Check – Frequency Failure

VistA performs the Max Daily Dose Order Check when the FDB MedKnowledge Framework logic does not due to a frequency failure. Below are two examples of when VistA performs the Max Daily Dose Order Check.

#### VistA Successfully Performs Max Daily Dose Order Check

In this example, a new unit dose order for Metformin 6000mg Q48H is entered. Upon acceptance, the Dosing Order Checks are performed. If a frequency message is displayed it indicates that VistA performed the Max Daily Dose Order Check. A high dose warning is displayed for the Maximum Single Dose Order Check which was performed by the vendor. The high dose warning displayed for the Max Daily Dose Order Check was performed by VistA.

VistA Successfully Performs Max Daily Dose Order Check

DRUG: METFORMIN 500MG HS502

...OK? Yes// (Yes)

Now doing allergy checks. Please wait...

\*\*\*Metformin Lab Results\*\*\*

Metformin - no serum creatinine within past 120 days.

Now processing Clinical Reminder Order Checks. Please wait ...

============================================================

\*\*\* Clinical Reminder Order Check \| Severity: MEDIUM \*\*\*

CR3286 CROC - METFORMIN DRUG SEVERITY MEDIUM (RULE DISP NAME)

\*\*\* FIRST LINE OF ORDER CHECK TEXT \*\*\* ORDER CHECK LINE 02 ORDER CHECK LINE 03

ORDER CHECK LINE 04 ORDER CHECK LINE 05 ORDER CHECK LINE 06 ORDER CHECK LINE 07

ORDER CHECK LINE 08 ORDER CHECK LINE 09 \*\*\* LAST LINE OF ORDER CHECK TEXT \*\*\*

------------------------------------------------------------

Press Return to Continue...:

Do you want to Intervene? N// O

Now Processing Enhanced Order Checks! Please wait...

There are 2 Available Dosage(s):

1\. 500MG

2\. 1000MG

Select from list of Available Dosages (1-2), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 6000MG 6000MG

You entered 6000MG is this correct? Yes// YES

VERB: TAKE

DISPENSE UNITS PER DOSE(TABLET(S)): 12// 12

Dosage Ordered: 6000MG

NOUN: TABLETS

ROUTE: //ORAL (BY MOUTH) PO BY MOUTH

Schedule: Q48H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

Q48H Q48H

...OK? Yes// (Yes)

(Q48H)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

METFORMIN 500MG: Single dose of 6,000 milligrams exceeds the maximum single

dose of 2,000 milligrams.

METFORMIN 500MG: Average daily dose of 3,000 milligrams/day exceeds the

maximum daily dose of 2,000 milligrams/day.

Recommended frequency of METFORMIN 500MG: Frequency of every 2 days is

below the frequency range of 1 to 2 administrations per day.

Do you want to Continue? Y//

.

<u>.</u>

#### VistA Cannot Perform Max Daily Dose Order Check – Not Correctable

In this example, a unit dose order for Enoxaparin 60MG/0.6ML INJ - One Vial SQ Q48H is entered. The presence of the frequency message indicates that VistA performed the Max Daily Dose Order Check. An error message is displayed for both the Maximum Single Dose Order Check and the Max Daily Dose Order Check. A general dosing information message is also provided because both Dosing Checks could not be performed.

The Maximum Single Dose Order Check tells us that there is a problem with the dose unit of ‘VIAL’ that was sent in for the Dosing Order Checks. Using the PDM *Lookup Dosing Check Info for Drug* option, we find out that acceptable units are ‘milligrams’ or ‘milliliters’. VistA cannot perform the Max Daily Dose Order Check because the daily dose cannot be evaluated against the max daily dose value returned because the units returned for the max daily dose are in milliliters. VistA in turn displays the original reason returned by the vendor as to why the Max Daily Dose could not be performed and that was because the frequency check failed.

VistA Cannot Perform Max Daily Dose Order Check – Not Correctable

<u>ACTIVE UNIT DOSE Jun 08, 2017@13:51:29 Page: 1 of 2</u>

Ward: GASTRO A

PID: Room-Bed: 600-A Ht(cm): 182.88 (11/14/93)

DOB: 01/01/40 (77) Wt(kg): 90.72 (11/14/93)

(1)Orderable Item: ENOXAPARIN INJ \<DIN\>

Instructions:

(2)Dosage Ordered: ONE VIAL

Duration: (3)Start: 06/08/2017 13:51

\(4\) Med Route: SUBCUTANEOUS

\(5\) Stop: 07/08/2017 24:00

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: Q48H

\(9\) Admin Times: 09

\(10\) Provider: PROVIDER,ONE

\(11\) Special Instructions:

<u>(12) Dispense Drug U/D Inactive Date</u>

ENOXAPARIN 60MG/0.6ML INJ 1

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

Maximum Single Dose Check could not be performed for Drug: ENOXAPARIN

60MG/0.6ML INJ

Reason(s): Unable to convert units : 'vial' to 'milliliter'.

Max Daily Dose Check could not be performed for Drug: ENOXAPARIN 60MG/0.6ML

INJ

Reason(s): Unable to convert units : 'vial/day' to 'milliliter/day'.

General dosing range for ENOXAPARIN 60MG/0.6ML INJ (SUBCUTANEOUS): 0.2

milliliter/day to 0.02 milliliter/kilogram/day. Maximum daily dose is

0.02 milliliter/kilogram/day.

Recommended frequency of ENOXAPARIN 60MG/0.6ML INJ: Unable to convert units

: 'vial' to 'milliliter'. A frequency check was not performed because the

ordered dose of 1 vial is not convertible to the dose screening unit of

measure of milliliter.

PATIENT INSTRUCTIONS: //

Press Return to continue...

#### VistA Cannot Perform Max Daily Dose Order Check – Correctable

In Example 1, an order for Enoxaparin 100MG/ML INJ – 100mg SQ Q48H is entered. The presence of the frequency message indicates that VistA performed the Max Daily Dose Order Check. An error message is displayed for the Maximum Single Dose Order Check indicating that a weight is missing for the patient.

Example 1: VistA Cannot Perform Max Daily Dose Order Check – Correctable

Select Action: Quit// NO New Order

Eligibility:

RX PATIENT STATUS: OTHER FEDERAL//

DRUG: ENOX

Lookup: GENERIC NAME

ENOXAPARIN 100MG/ML INJ BL110

...OK? Yes// (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

There are 4 Available Dosage(s):

1\. 90 MILLIGRAMS (0.9ML)

2\. 100 MILLIGRAMS (1.0ML)

3\. 85 MILLIGRAMS (0.85ML)

4\. 95 MILLIGRAMS (0.95ML)

Select from list of Available Dosages (1-4), Enter Free Text Dose

or Enter a Question Mark (?) to view list: 2 100 MILLIGRAMS (1.0ML)

You entered 100 MILLIGRAMS (1.0ML) is this correct? Yes// YES

VERB: INJECT

ROUTE: //SQ SUBCUTANEOUS SQ

Schedule: Q48H

Now searching ADMINISTRATION SCHEDULE (#51.1) file...

Q48H Q48H

...OK? Yes// (Yes)

(Q48H)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

Dosing Checks could not be performed for Drug: ENOXAPARIN 100MG/ML INJ

Reason(s): Weight is required.

General dosing range for ENOXAPARIN 100MG/ML INJ (SUBCUTANEOUS): 20

milligram/day to 2 milligram/kilogram/day. Maximum daily dose is 2

milligram/kilogram/day.

Recommended frequency of ENOXAPARIN 100MG/ML INJ: Frequency of every 2 days

is below the frequency range of 1 to 2 administrations per day.

PATIENT INSTRUCTIONS:

Do you want to Continue? Y//

In Example 2, once a weight is entered for the patient, the same order is entered again and the results are different. A high dose warning for the Maximum Single Dose Order Check is displayed with a frequency message. The presence of the frequency message indicates that VistA performed the Max Daily Dose Order Check. No messages specific to the Max Daily Dose Order Check indicate that the daily dose did not exceed the max daily dose value. In other words, the daily dose for the order passed.

Example 2: VistA Cannot Perform Max Daily Dose Order Check – Corrected

TEST Ward: OBSERVATION

PID: XXX-XX-XXXX Room-Bed: Ht(cm): 152.40 (05/20/22)

DOB: 01/01/01 (121) Att: TEST Wt(kg): 47.00 (05/20/22)

(1)Orderable Item: ENOXAPARIN INJ

Instructions:

(2)Dosage Ordered: 100 MILLIGRAMS (1.0ML)

Duration: (3)Start: 05/20/2022 15:31

\(4\) Med Route: SUBCUTANEOUS

\(5\) Stop: 06/03/2022 15:31

\(6\) Schedule Type: CONTINUOUS

\(8\) Schedule: Q48H

\(9\) Admin Times: 1000

\(10\) Provider: TEST

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

ENOXAPARIN 100MG/ML INJ 1

\+ Enter ?? for more actions

ED Edit AC ACCEPT

Select Item(s): Next Screen// AC ACCEPT

ENOXAPARIN 100MG/ML INJ: Single dose of 100 milligrams exceeds the maximum

single dose of 1.5 milligrams/kilogram (75.15682 milligrams).

Recommended frequency of ENOXAPARIN 100MG/ML INJ: Frequency of every 2 days

is below the frequency range of 1 to 2 administrations per day.

Do you want to Continue? Y//

### IV Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New IV Order

When entering a new IV order through the pharmacy backdoor as shown in the example below, Dosing Order Checks will be performed after the expected first dose is displayed. If the dosage ordered exceeds the FDB recommended maximum single dose and/or maximum daily dose, warning message(s) for the respective dosing order check will be displayed to the user. The warning message will be indented and the drug name will precede the warning message. The drug name within the message will either be the IV Additive print name, strength and unit or if a PreMix IV Solution is involved, the IV Solution print name (1) and volume. In this example, the IV Additive print name, strength and unit is displayed.

If a Maximum Single Dose Order Check warning and/or Max Daily Dose Order Check warning is displayed, the user will be prompted with ‘Do you want to Continue?’ If the user accepts the default of ‘No’, the software will take them back to the ‘Select IV Type:’ prompt. If the user responds ‘Yes’, the program will proceed with the intervention dialog.

If a Maximum Single Dose Order Check and/or Max Daily Dose Order Check cannot be performed an error message for the respective Dosing Order Check or for both Dosing checks is displayed. The user will not be asked to enter an intervention to continue.

If the schedule within the order has been marked to be excluded from all dosing checks, no Dosing Order Checks will be performed. In this case, no message will be displayed to the user informing them of this. If the schedule within the order has been marked to be excluded from the Daily Dose Order Check, the Max Daily Dose Order Check will not be performed. The Maximum Single Dose Order Check will be performed. The user will not be displayed a message informing them of this.

New Order Entry through pharmacy backdoor options

Select Action: Quit// NO New Order Entry

Select DRUG:

Select IV TYPE: PIGGYBACK.

Select ADDITIVE: CEFAZOLIN

\*N/F\*

Restriction/Guideline(s) exist. Display? : (N/D): No// NO

Enter RETURN to continue or '^' to exit:

(The units of strength for this additive are in GM)

Strength: 10 10 GM

Select ADDITIVE:

Select SOLUTION: D550 5% DEXTROSE 50 ML

\*N/F\*

Restriction/Guideline(s) exist. Display? : (N/D/O/B): No// NO

Enter RETURN to continue or '^' to exit:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

INFUSION RATE: 30 INFUSE OVER 30 MINUTES

MED ROUTE: IVPB IV PIGGYBACK IVPB

SCHEDULE: Q12H

ADMINISTRATION TIMES: 09-21//

REMARKS:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* WARNING \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\* If OTHER PRINT INFO exceeds 60 characters, \*\*

\*\* 'Instructions too long. See Order View or BCMA for full text.' \*\*

\*\* will print on the IV label instead of the full text. \*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Enter RETURN to continue or '^' to exit:

OTHER PRINT INFO:

START DATE/TIME: OCT 14,2011@09:00// (OCT 14, 2011@09:00)

STOP DATE/TIME: OCT 24,2011@11:59//

PROVIDER: PROVIDER, ONE//

Orderable Item: CEFAZOLIN INJ

Give: IVPB Q12H

59

NHCU 10/14/11

110-1

CEFAZOLIN 10 GM

5% DEXTROSE 50 ML

Dose due at: \_\_\_\_\_\_\_\_

INFUSE OVER 30 MINUTES

Q12H

09-21

fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

<span id="Page_164" class="anchor"></span>Start date: OCT 14,2011 09:00 Stop date: OCT 24,2011 11:59

<span id="Page_123" class="anchor"></span>

Expected First Dose: OCT 14,2011@09:00

CEFAZOLIN 10 GM: Single dose of 10 grams exceeds the maximum single dose

of 3 grams.

CEFAZOLIN 10 GM: Total dose of 20 grams/day exceeds the maximum daily

dose of 12 grams/day.

Do you want to Continue? NO//

Select IV TYPE:

\*\*\*\*\*Or\*\*\*\*\*

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For CEFAZOLIN 1GM VI

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// O

Is this O.K.: YES// YES

NATURE OF ORDER: WRITTEN// W

...transcribing this non-verified order....

NON-VERIFIED IV Oct 14, 2011@08:59:50 Page: 1 of 2

Ward: NHCU A

PID: Room-Bed: 110-1 Ht(cm): 176.53 (12/30/05)

DOB: 10/01/75 (36) Wt(kg): 67.28 (01/09/06)

\*(1) Additives: Type: PIGGYBACK \<DIN\>

CEFAZOLIN 10 GM \*N/F\*

\(2\) Solutions:

5% DEXTROSE 50 ML \*N/F\*

Duration: (4) Start: 10/14/2011 09:00

\(3\) Infusion Rate: INFUSE OVER 30 MINUTES

\*(5) Med Route: IVPB (6) Stop: 10/24/2011 11:59

\*(7) Schedule: Q12H Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 09-21 Quantity: 0

\*(9) Provider: PROVIDER,ONE \[w\] Cum. Doses:

\*(10)Orderable Item: CEFAZOLIN INJ

Instructions:

\(11\) Other Print:

\+ Enter ?? for more actions

DC Discontinue RN (Renew) VF Verify

HD (Hold) OC (On Call) FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen// VF Verify .

1 Label needed for dose due at ...

10/14/11 0900 :

#### Finishing an IV Order 

The following example illustrates finishing an IV order with multiple prospective drugs that each generate multiple Dosing Order Check warnings.

For each prospective drug, in this case for each IV Additive that generates a Maximum Single Dose and/or Max Daily Dose Order Check warnings, the user will be prompted with a ‘Do you want to Continue?’ If they respond ‘No’, the program will take them back to the detailed order screen where the FINISH action was initiated. If the user responds ‘Yes’ they will have to log a pharmacy intervention. An intervention will have to be entered for each IV Additive that generated a Dosing Order Check warning as illustrated.

Finishing IV order with multiple prospective drugs

PENDING IV (ROUTINE) Nov 07, 2011@11:09:21 Page: 1 of 3

Ward: MICU

PID: Room-Bed: MICU-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/05/20 (91) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\(1\) Additives: Type: ADMIXTURE \<DIN\>

CALCIUM GLUCONATE 6 GM (1)

MAGNESIUM SULFATE 15 GM (1) \*N/F\*

POTASSIUM CHLORIDE 50 MEQ

\(2\) Solutions:

5% DEXTROSE 1000 ML

Duration: (4) Start: 11/07/2011 15:30

\(3\) Infusion Rate: 125 ml/hr

\*(5) Med Route: IV (6) Stop: 12/08/2011 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[es\] Cum. Doses:

\*(10)Orderable Item: CALCIUM GLUCONATE INJ,SOLN

Instructions:

\(11\) Other Print:

\+ Enter ?? for more actions

DC Discontinue FL Flag

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

PROVIDER COMMENTS:

place calcium in bag \#1 and magnesium in bag \#2

Select one of the following:

Y Yes (copy)

N No (don't copy)

! Copy and flag for display in a BCMA Message Box

E Copy and Edit

Copy the Provider Comments into Other Print Info (Yes/No/!/E): Yes (copy)

IV TYPE: ADMIXTURE//

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

<span id="Page_125" class="anchor"></span>

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

PENDING IV (ROUTINE) Nov 07, 2011@11:10:27 Page: 1 of 3

Ward: MICU

PID: Room-Bed: MICU-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/05/20 (91) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\(1\) Additives: Type: ADMIXTURE \<DIN\>

CALCIUM GLUCONATE 6 GM (1)

MAGNESIUM SULFATE 15 GM (1) \*N/F\*

POTASSIUM CHLORIDE 50 MEQ

\(2\) Solutions:

5% DEXTROSE 1000 ML

Duration: (4) Start: 11/07/2011 15:30

\(3\) Infusion Rate: 125 ml/hr

\*(5) Med Route: IV (6) Stop: 12/08/2011 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[es\] Cum. Doses:

\*(10)Orderable Item: CALCIUM GLUCONATE INJ,SOLN

Instructions:

\(11\) Other Print: place calcium in bag \#1 and magnesium in bag \#2

\+ Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Next Screen// ED Edit

Select FIELDS TO EDIT: 1

Select ADDITIVE: CALCIUM GLUCONATE//

ADDITIVE: CALCIUM GLUCONATE//

(The units of strength for this additive are in GM)

Strength: 6 GM//

BOTTLE: 1// 1

Select ADDITIVE: MAGNESIUM SULFATE 15 GM (1)

...OK? Yes// (Yes)

ADDITIVE: MAGNESIUM SULFATE//

Restriction/Guideline(s) exist. Display? : (N/D): No// NO

Enter RETURN to continue or '^' to exit:

(The units of strength for this additive are in GM)

Strength: 15 GM//

BOTTLE: 1// 2

Select ADDITIVE:

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Press Return to continue...

PENDING IV (ROUTINE) Nov 07, 2011@11:10:49 Page: 1 of 3

Ward: MICU

PID: Room-Bed: MICU-2 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 04/05/20 (91) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\(1\) Additives: Type: ADMIXTURE \<DIN\>

CALCIUM GLUCONATE 6 GM (1)

MAGNESIUM SULFATE 15 GM (2) \*N/F\*

POTASSIUM CHLORIDE 50 MEQ

\(2\) Solutions:

5% DEXTROSE 1000 ML

Duration: (4) Start: 11/07/2011 15:30

\(3\) Infusion Rate: 125 ml/hr

\*(5) Med Route: IV (6) Stop: 12/08/2011 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[es\] Cum. Doses:

\*(10)Orderable Item: CALCIUM GLUCONATE INJ,SOLN

Instructions:

\(11\) Other Print: place calcium in bag \#1 and magnesium in bag \#2

\+ Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Next Screen// AC Accept

CALCIUM GLUCONATE 6 GM: Single dose of 6 grams exceeds the maximum

single dose of 2 grams.

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For CALCIUM GLUCONATE 10% INJ

PROVIDER: PROVIDER,ONE LBB 119

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue ...

Would you like to edit this intervention? N// O

MAGNESIUM SULFATE 15 GM: Single dose of 15 grams exceeds the maximum

single dose of 12 grams.

MAGNESIUM SULFATE 15 GM: Total dose of 15 grams/day exceeds the maximum

daily dose of 12 grams/day.

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For MAGNESIUM SULFATE 1G/ML (50%) 2ML

<span id="Page_127" class="anchor"></span>

PROVIDER: PROVIDER,ONE LBB 119

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue ...

Would you like to edit this intervention? N// O

POTASSIUM CHLORIDE 50 MEQ: Single dose of 50 milliequivalents exceeds

the maximum single dose of 40 milliequivalents.

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For POTASSIUM CHLORIDE 20MEQ/10ML INJ

PROVIDER: PROVIDER,ONE OP 119

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// O

Orderable Item: CALCIUM GLUCONATE INJ,SOLN

Give: IV

109

MICU 11/07/11

MICU-2

CALCIUM GLUCONATE 6 GM (1)

MAGNESIUM SULFATE 15 GM (2)

POTASSIUM CHLORIDE 50 MEQ

5% DEXTROSE 1000 ML

Dose due at: \_\_\_\_\_\_\_\_

125 ml/hr

place calcium in bag \#1 and magnesium in bag \#2

fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: NOV 7,2011 15:30 Stop date: DEC 8,2011 11:59

Expected First Dose: NOV 7,2011@15:30

\*\*\* This change will cause a new order to be created. \*\*\*

Is this O.K.? YES//

NATURE OF ORDER: SERVICE CORRECTION// S

#### Editing an Order

In the example below, the editing of the infusion rate for an IV order with the IV Type of ‘Admixture’ results in a new order to be created and Dosing Order Checks to be performed. However, editing of the infusion rate will not always result in a Dosing Order Check being performed. The IV type of the order must be an ‘Admixture’, ‘Hyperal’, ‘Chemotherapy Admixture’, ‘Continuous Syringe’, or ‘Chemotherapy Continuous Syringe’.

Dosing Order Checks will only be performed when the schedule of an IV order is edited for IV Types of ‘Piggyback’, ‘Intermittent Syringe’, ‘Chemotherapy Piggyback’, or ‘Chemotherapy Intermittent Syringe’.

Dosing Order Checks will not be performed when the volume of an IV order is edited for IV Types of ‘Piggyback’, ‘Intermittent Syringe’, ‘Chemotherapy Piggyback’, or ‘Chemotherapy Intermittent Syringe’ with an IV Solution not marked as a PreMix.

Making an edit to the medication route, changing any IV Additive fields or IV Solution fields for any IV Solution marked as a PreMix, will cause Dosing Order Checks to be performed.

Dosing Order Checks will be performed after all edits are made and the user accepts the order.

Editing infusion rate for an IV Solution marked as PreMix

ACTIVE IV Apr 21, 2008@15:14 Page: 1 of 1

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

\*(1) Additives: Order number: 9 Type: ADMIXTURE \<DIN\>

\*(2) Solutions:

HEPARIN 25000U/D5W 250 ML \*N/F\*

Duration: \*(4) Start: 04/21/2008 15:30

\*(3) Infusion Rate: 15 ml/hr

\*(5) Med Route: IV \*(6) Stop: 04/22/2008 24:00

\*(7) Schedule: Last Fill: 04/21/2008 15:13

\(8\) Admin Times: Quantity: 1

\*(9) Provider: PSJPROVIDER,TWO \[w\] Cum. Doses: 1

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

Entry By: PSJPHARMACIST,ONE Entry Date: 04/21/08 15:10

Enter ?? for more actions

DC Discontinue RN Renew VF (Verify)

HD Hold OC On Call FL Flag

ED Edit AL Activity Logs

Select Item(s): Quit// ED Edit

Select FIELDS TO EDIT: 3

INFUSION RATE: 15 ml/hr//20 ml/hr

NUMBER OF LABELS PER DAY:

ACTIVE IV Apr 21, 2008@15:15:07 Page: 1 of 1

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

\*(1) Additives: Order number: 9 Type: ADMIXTURE \<DIN\>

\*(2) Solutions:

<span id="Page_129" class="anchor"></span> HEPARIN 25000U/D5W 250 ML \*N/F\*

Duration: \*(4) Start: 04/21/2008 15:30

\*(3) Infusion Rate: 20 ml/hr

\*(5) Med Route: IV \*(6) Stop: 04/22/2008 24:00

\*(7) Schedule: Last Fill: 04/21/2008 15:13

\(8\) Admin Times: Quantity: 1

\*(9) Provider: PSJPROVIDER,TWO \[w\] Cum. Doses: 1

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

Entry By: PSJPHARMACIST,ONE Entry Date: 04/21/08 15:10

Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Edit// AC Accept

HEPARIN 25000U/D5W 250 ML: The dose of 20 milliliters/hour exceeds the

maximum dose of 0.0245 milliliters/kilogram/hour (2.08684

milliliters/hour).

Do you want to Continue? N// n NO

ACTIVE IV Apr 21, 2008@15:14 Page: 1 of 1

Ward: 3AS CWAD

PID: Room-Bed: 300-1 Ht(cm): 187.96 (08/14/07)

DOB: 10/10/50 (57) Wt(kg): 83.41 (08/14/07)

\*(1) Additives: Order number: 9 Type: ADMIXTURE \<DIN\>

\*(2) Solutions:

HEPARIN 25000U/D5W 250 ML \*N/F\*

Duration: \*(4) Start: 04/21/2008 15:30

\*(3) Infusion Rate: 15 ml/hr

\*(5) Med Route: IV \*(6) Stop: 04/22/2008 24:00

\*(7) Schedule: Last Fill: 04/21/2008 15:13

\(8\) Admin Times: Quantity: 1

\*(9) Provider: PSJPROVIDER,TWO \[w\] Cum. Doses: 1

\(10\) Other Print:

\(11\) Remarks :

Room: GLRISC

Entry By: PSJPHARMACIST,ONE Entry Date: 04/21/08 15:10

Enter ?? for more actions

DC Discontinue RN Renew VF (Verify)

HD Hold OC On Call FL Flag

ED Edit AL Activity Logs

.

.

.

OR

Do you want to Continue? N// YES

Now creating Pharmacy Intervention

for HEPARIN 25000U/D5W 250 ML

PROVIDER: OPPROVIDER, ONE

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

Med Route: IV

48

\[9\]4010 3AS 04/21/08

300-1

HEPARIN 25000U/D5W 250 ML

Dose due at: \_\_\_\_\_\_\_\_

20 ml/hr

fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: APR 21,2008 15:30 Stop date: APR 22,2008 24:00

Expected First Dose: APR 21,2008@15:30

\*\*\* This change will cause a new order to be created. \*\*\*

Is this O.K.: Y//

#### Renewing of an Order

For this IV order in the example below there is only an IV Solution that is marked as a PreMix. The infusion rate is used to determine the single dose amount and Dose Unit. The infusion rate is in an acceptable format since it was entered through CPRS. The Numeric Dose is ’100’; the drug unit is ‘MCG’, the patient parameter is ‘KG’ and the Dose Rate Unit/Duration Rate is ‘MIN’. The single dose amount will be calculated by looking up the patient’s latest weight in KG which is ‘90‘and multiplying by 100. The single dose amount is calculated to be ‘9000’. The software uses the drug unit of ‘MCG’ to do a lookup into the DOSE UNITS file to find the FDB equivalent of ‘MICROGRAMS’ to send into the interface. ‘MINUTE’ will be sent into the interface for the Dose Rate Unit/Duration Rate. This can be verified by looking at the Dosing Order Check warning that is displayed.

Renewing IV Order with a free text infusion rate

ACTIVE IV Nov 07, 2011@15:00:56 Page: 1 of 1

Ward: MICU

PID: Room-Bed: MICU-2 Ht(cm): 170.00 (11/07/11)

DOB: 04/05/20 (91) Wt(kg): 90.00 (11/07/11)

\*(1) Additives: Order number: 6 Type: ADMIXTURE

\*(2) Solutions:

DOPAMINE 1600MCG/ML IN D5W 250 ML

Duration: \*(4) Start: 11/07/2011 15:30

\*(3) Infusion Rate: 100MCG/KG/MIN@1

\*(5) Med Route: IV \*(6) Stop: 12/08/2011 11:59

\*(7) Schedule: Last Fill: 11/07/2011 14:27

\(8\) Admin Times: Quantity: 1

\*(9) Provider: PROVIDER,ONE \[es\] Cum. Doses: 1

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

Entry By: PROVIDER,ONE Entry Date: 11/07/11 14:27

Enter ?? for more actions

DC Discontinue RN Renew VF (Verify)

HD Hold OC On Call FL Flag

ED Edit AL Activity Logs

<span id="Page_131" class="anchor"></span>Select Item(s): Quit// RN Renew

STOP DATE/TIME: DEC 8,2011@11:59//

PROVIDER: PROVIDER,ONE//

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Enhanced Order Checks cannot be performed for Local Drug: AMINOPHYLLINE 100MG

TAB

Reason(s): Drug not matched to NDF

Press Return to continue...

================================================================================

This patient is receiving the following order(s) that have a SIGNIFICANT Drug

Interaction with DOPAMINE 1600MCG/ML IN D5W 250 ML:

NON-VA Med: PHENYTOIN SOD 100MG CAP

Dosage: 100MG Schedule: EVERY 8 HOURS

\*\*\* REFER TO MONOGRAPH FOR SIGNIFICANT INTERACTION CLINICAL EFFECTS

================================================================================

Display Professional Interaction Monograph(s)? NO//

Do you want to Intervene with DOPAMINE 1600MCG/ML IN D5W 250 ML? NO//

DOPAMINE 1600MCG/ML IN D5W 250 ML: The dose of 9,000 micrograms/minute

exceeds the maximum dose of 50 micrograms/kilogram/minute (4,258.86364

micrograms/minute).

Press Return to continue...

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For DOPAMINE 400MG/D5W 250ML

PROVIDER: PROVIDER,ONE OP 119

RECOMMENDATION: ??

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

Med Route: IV

109

MICU 11/07/11

MICU-2

DOPAMINE 1600MCG/ML IN D5W 250 ML

Dose due at: \_\_\_\_\_\_\_\_

100MCG/KG/MIN

fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: NOV 7,2011 15:30 Stop date: DEC 8,2011 11:59

Expected First Dose: NOV 7,2011@15:30

#### Copy an IV Order

The following example illustrates the COPY action taken on an IV order that generates a Dosing Order Check warning.

Copy an IV Order

Inpatient Order Entry Aug 16, 2012@11:26:28 Page: 1 of 2

Ward: 2ASM

PID: Room-Bed: Ht(cm): 200.00 (08/16/12)

DOB: 07/14/33 (79) Wt(kg): 70.00 (08/16/12)

Sex: MALE Admitted: 08/14/12

Dx: CHEST PAIN Last transferred: \*\*\*\*\*\*\*\*

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 CEFAZOLIN 5 GM C 08/16/2012 08/26/2012 A

in 5% DEXTROSE 100 ML Q12H

2 in DOPAMINE 1600MCG/ML IN D5W 250 ML C 08/16/2012 09/16/2012 A

TITRATE

3 HEPARIN 25000 UNITS C 08/16/2012 09/16/2012 A

in 5% DEXTROSE 250 ML 20 ml/hr

4 POTASSIUM CHLORIDE 50 MEQ C 08/16/2012 09/16/2012 A

CALCIUM GLUCONATE 5 GM (2)

in 5% DEXTROSE 1000 ML 125 ml/hr

5 TEMAZEPAM CAP,ORAL C 08/15/2012 08/22/2012 A

Give: 30MG PO QHS

\+ Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Next Screen// 3

ACTIVE IV Aug 16, 2012@11:27 Page: 1 of 2

Ward: 2ASM

PID: Room-Bed: Ht(cm): 200.00 (08/16/12)

DOB: 07/14/33 (79) Wt(kg): 70.00 (08/16/12)

\*(1) Additives: Order number: 5 Type: ADMIXTURE \<DIN\>

HEPARIN 25000 UNITS \*N/F\*

\*(2) Solutions:

5% DEXTROSE 250 ML \*N/F\*

Duration: \*(4) Start: 08/16/2012 11:26

\*(3) Infusion Rate: 20 ml/hr

\*(5) Med Route: IV \*(6) Stop: 09/16/2012 11:59

\*(7) Schedule: Last Fill: 08/16/2012 11:26

\(8\) Admin Times: Quantity: 1

\*(9) Provider: PROVIDER,ONE \[w\] Cum. Doses: 1

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

\+ Enter ?? for more actions

DC Discontinue RN Renew VF (Verify)

HD Hold OC On Call FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen// CO CO

Do you want to copy this order? No// Y (Yes)

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

ACTIVE IV Aug 16, 2012@11:27:58 Page: 1 of 1

Ward: 2ASM

PID: Room-Bed: Ht(cm): 200.00 (08/16/12)

DOB: 07/14/33 (79) Wt(kg): 70.00 (08/16/12)

\*(1) Additives: Order number: 5 Type: ADMIXTURE \<DIN\>

HEPARIN 25000 UNITS \*N/F\*

\*(2) Solutions:

5% DEXTROSE 250 ML \*N/F\*

Duration: \*(4) Start: 08/16/2012 11:26

\*(3) Infusion Rate: 20 ml/hr

\*(5) Med Route: IV \*(6) Stop: 09/16/2012 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 1

\*(9) Provider: PROVIDER,ONE Cum. Doses: 1

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

Entry By: PHARMACIST,ONE Entry Date: 08/16/12 11:26

Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Edit// AC Accept

HEPARIN 25000 UNITS: The dose of 2,000 units/hour exceeds the maximum

dose of 24.5 units/kilogram/hour (1,718.56364 units/hour).

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For HEPARIN 10,000 U/ML 5ML VI

PROVIDER: PROVIDER,ONE OP

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

.

.

.

Med Route: IV

132

2ASM 08/16/12

NF

HEPARIN 25000 UNITS

5% DEXTROSE 250 ML

Dose due at: \_\_\_\_\_\_\_\_

20 ml/hr

fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: AUG 16,2012 11:26 Stop date: SEP 16,2012 11:59

Expected First Dose: AUG 16,2012@11:26

\*\*\* This change will cause a new order to be created. \*\*\*

Is this O.K.: Y// YES

NATURE OF ORDER: WRITTEN// W

3 6 9 12 15 18 21 24

..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:

A

N

Next delivery time is 1530 \*\*\*

Action (PB) B//

#### Adjusting Single Dose Amount 

In earlier scenarios there was discussion about how the single dose amount has to be adjusted for the Dosing Order Check. In this example, one bag of IV fluids containing Folic Acid will infuse over 16.12 hours. The frequency has to be rounded to 16 hours. The drug, Folic Acid, is not a drug that is administered via a continuous route as per FDB dosing records. The IV Type of the order is an ‘Admixture’ and the order is equal to or greater than 24 hours. The single dose is adjusted based on 16 hours. The full amount of ‘1000’ mg in one IV bag will not completely infuse over 16 hours. The dose is adjusted to ‘992’ to reflect this. The message will reflect the adjusted single dose amount and volume over the rounded time period. A note will display before the Dosing Order Check warnings. If the adjusted dose does not exceed the recommended maximum single dose for the drug, and no warning message is displayed, the user will not be informed that the single dose was adjusted for the Dosing Order Checks.

<span id="Page_135" class="anchor"></span>Adjusted Single Dose Amount for IV Order

PENDING IV (ROUTINE) Nov 07, 2011@15:25:49 Page: 1 of 3

Ward: MICU

PID: Room-Bed: MICU-2 Ht(cm): 170.00 (11/07/11)

DOB: 04/05/20 (91) Wt(kg): 90.00 (11/07/11)

\*(1) Additives: Type: ADMIXTURE \<DIN\>

FOLIC ACID 1000 MG

\*(2) Solutions:

0.9% SODIUM CHLORIDE 1000 ML \*N/F\*

<span id="Page_177" class="anchor"></span> Duration: (4) Start: 11/07/2011 15:30

\*(3) Infusion Rate: 62 ml/hr

\*(5) Med Route: IV (6) Stop: 12/08/2011 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[es\] Cum. Doses:

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

Entry By: PROVIDER,ONE Entry Date: 11/07/11 15:25

\+ Enter ?? for more actions

DC Discontinue FL Flag

ED Edit FN Finish

Select Item(s): Next Screen// FN Finish

IV TYPE: ADMIXTURE//

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

Enhanced Order Checks cannot be performed for Local Drug: AMINOPHYLLINE 100MG

TAB

Reason(s): Drug not matched to NDF

Press Return to continue...

PENDING IV (ROUTINE) Nov 07, 2011@15:26:30 Page: 1 of 3

Ward: MICU

PID: Room-Bed: MICU-2 Ht(cm): 170.00 (11/07/11)

DOB: 04/05/20 (91) Wt(kg): 90.00 (11/07/11)

\*(1) Additives: Type: ADMIXTURE \<DIN\>

FOLIC ACID 1000 MG

\*(2) Solutions:

0.9% SODIUM CHLORIDE 1000 ML \*N/F\*

Duration: (4) Start: 11/07/2011 15:30

\*(3) Infusion Rate: 62 ml/hr

\*(5) Med Route: IV (6) Stop: 12/08/2011 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[es\] Cum. Doses:

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

Entry By: PROVIDER,ONE Entry Date: 11/07/11 15:25

\+ Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Next Screen// AC Accept

PLEASE NOTE: The single dose of the IV Additive has been adjusted to

reflect the amount of drug infused over the nearest whole number of

hours (992 ML over 16 hours).

FOLIC ACID 1000 MG: Single dose of 992 milligrams exceeds the maximum

single dose of 5 milligrams.

FOLIC ACID 1000 MG: Total dose of 1,488 milligrams/day exceeds the

maximum daily dose of 5 milligrams/day.

Recommended frequency of FOLIC ACID 1000 MG: Frequency of 1.5

administrations per day exceeds the high frequency of 1 administration

per day.

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For FOLATE SODIUM 5MG/ML INJ 10ML

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention? N// O

Med Route: IV

109

MICU 11/07/11

MICU-2

FOLIC ACID 1000 MG

0.9% SODIUM CHLORIDE 1000 ML

Dose due at: \_\_\_\_\_\_\_\_

62 ml/hr

fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: NOV 7,2011 15:30 Stop date: DEC 8,2011 11:59

Expected First Dose: NOV 7,2011@15:30

#### Verifying a non-verified IV order

In the following example, a pharmacist has selected a non-verified IV order and taken the VERIFY action. Upon taking the action, order checks will be processed. In this example a Maximum Single Dose Order Check warning and a Max Daily Dose Order Check warning are displayed. Had the VERIFY action been taken with any other action that triggers order checks, order checks would have only been displayed once.

<span id="Page_137" class="anchor"></span>Verifying a non-verified IV order

<u>Inpatient Order Entry Mar 01, 2013@12:12:46 Page: 1 of 1</u>

Ward: 2ASM

PID: Room-Bed: Ht(cm): 200.00 (08/16/12)

DOB: 07/14/33 (79) Wt(kg): 70.00 (08/16/12)

Sex: MALE Admitted: 08/14/12

Dx: CHEST PAIN Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): 2.04

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

1 CEFAZOLIN INJ C 03/01/2013 03/11/2013 N

Give: 10 GM IVPB Q12H

Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Quit// 1

<u>NON-VERIFIED IV Mar 01, 2013@12:13:22 Page: 1 of 2</u>

Ward: 2ASM

PID: Room-Bed: Ht(cm): 200.00 (08/16/12)

DOB: 07/14/33 (79) Wt(kg): 70.00 (08/16/12)

\*(1) Additives: Type: PIGGYBACK \<DIN\>

CEFAZOLIN 10 GM \*N/F\*

\(2\) Solutions:

5% DEXTROSE 50 ML \*N/F\*

Duration: (4) Start: 03/01/2013 12:12

\(3\) Infusion Rate: INFUSE OVER 60 MINUTES

\*(5) Med Route: IVPB (6) Stop: 03/11/2013 11:59

\*(7) Schedule: Q12H Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: 09-21 Quantity: 0

\*(9) Provider: PROVIDER,ONE \[w\] Cum. Doses:

\*(10)Orderable Item: CEFAZOLIN INJ

Instructions: CEFAZOLIN 1GM VI

\(12\) Remarks :

\+ Enter ?? for more actions

DC Discontinue RN (Renew) VF Verify

HD (Hold) OC (On Call) FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen// VF Verify

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

Now Processing Enhanced Order Checks! Please wait...

CEFAZOLIN 10 GM: Single dose of 10 grams exceeds the maximum single dose

of 3 grams.

CEFAZOLIN 10 GM: Total dose of 20 grams/day exceeds the maximum daily

dose of 12 grams/day.

Do you want to Continue? NO//

.

#### Editing and then Verifying a non-verified IV order

In the example below, a non-verified IV order is edited and then verified through pharmacy backdoor options within a single order session. Only a Dosing Order Check is generated when the Infusion Rate field is edited from 50 to 40. Upon verification, enhanced order checks are processed and a drug interaction between Dopamine and Phenelzine is displayed for processing. The Dosing Order Check is not displayed again. In this case, since the Dosing Order Check was triggered during the Edit action, the same order check will not be displayed again during the Verify action.

Editing and then Verifying a non-verified IV order

Inpatient Order Entry Mar 25, 2013@18:05:42 Page: 1 of 2

Ward: 3AS

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 07/29/44 (68) Wt(kg): 100.00 (03/25/13)

Sex: MALE Admitted: 08/14/12

Dx: SHORTNESS OF BREATH Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 AMIODARONE TAB C 03/25/2013 04/01/2013 A

Give: 200MG PO TID

2 PHENELZINE SULFATE TAB C 03/25/2013 04/01/2013 A

Give: 15MG PO TID

3 WARFARIN TAB C 03/25/2013 03/26/2013 A

Give: 10MG PO QPM

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

4 CIMETIDINE TAB C 03/25/2013 04/24/2013 N

Give: 1200MG PO QHS

5 DOPAMINE 5000 MG C 03/25/2013 04/25/2013 N

\+ Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Next Screen// 5

NON-VERIFIED IV Mar 25, 2013@18:05:46 Page: 1 of 2

Ward: 3AS

<span id="Page_139" class="anchor"></span> PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 07/29/44 (68) Wt(kg): 100.00 (03/25/13)

\*(1) Additives: Type: ADMIXTURE \<OCI\>\<DIN\>

DOPAMINE 5000 MG

\*(2) Solutions:

5% DEXTROSE 250 ML \*N/F\*

Duration: (4) Start: 03/25/2013 20:00

\*(3) Infusion Rate: 50 ml/hr

\*(5) Med Route: IV (6) Stop: 04/25/2013 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[s\] Cum. Doses:

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

\+ Enter ?? for more actions

DC Discontinue RN (Renew) VF Verify

HD (Hold) OC (On Call) FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen// ED Edit

Select FIELDS TO EDIT: 3

INFUSION RATE: 50 ml/hr//40 ml/hr

NUMBER OF LABELS PER DAY:

NON-VERIFIED IV Mar 25, 2013@18:06:59 Page: 1 of 1

Ward: 3AS

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 07/29/44 (68) Wt(kg): 100.00 (03/25/13)

\*(1) Additives: Type: ADMIXTURE \<OCI\>\<DIN\>

DOPAMINE 5000 MG

\*(2) Solutions:

5% DEXTROSE 250 ML \*N/F\*

Duration: (4) Start: 03/25/2013 20:00

\*(3) Infusion Rate: 40 ml/hr

\*(5) Med Route: IV (6) Stop: 04/25/2013 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[s\] Cum. Doses:

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

Entry By: PHARMACIST,ONE Entry Date: 03/25/13 18:05

Enter ?? for more actions

AC Accept ED Edit

Select Item(s): Edit// AC Accept

DOPAMINE 5000 MG: The dose of 800 milligrams/hour exceeds the maximum

dose of 50 micrograms/kilogram/minute (255.53182 milligrams/hour).

Do you want to Continue? NO// YES

Now creating Pharmacy Intervention

For DOPAMINE 160MG/ML INJ

PROVIDER:

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

Med Route: IV

133

3AS 03/25/13

DOPAMINE 5000 MG

5% DEXTROSE 250 ML

Dose due at: \_\_\_\_\_\_\_\_

40 ml/hr

fld by: \_\_\_\_ Chkd by: \_\_\_\_

1\[1\]

Start date: MAR 25,2013 20:00 Stop date: APR 25,2013 11:59

Expected First Dose: MAR 25,2013@20:00

\*\*\* This change will cause a new order to be created. \*\*\*

Is this O.K.? YES//

NATURE OF ORDER: SERVICE CORRECTION// WRITTEN W

NON-VERIFIED IV Mar 25, 2013@18:18:39 Page: 1 of 2

Ward: 3AS

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 07/29/44 (68) Wt(kg): 100.00 (03/25/13)

\*(1) Additives: Type: ADMIXTURE \<OCI\>\<DIN\>

DOPAMINE 5000 MG

\*(2) Solutions:

5% DEXTROSE 250 ML \*N/F\*

Duration: (4) Start: 03/25/2013 20:00

\*(3) Infusion Rate: 40 ml/hr

\*(5) Med Route: IV (6) Stop: 04/25/2013 11:59

\*(7) Schedule: Last Fill: \*\*\*\*\*\*\*\*

\(8\) Admin Times: Quantity: 0

\*(9) Provider: PROVIDER,ONE \[w\] Cum. Doses:

\(10\) Other Print:

\(11\) Remarks :

IV Room: GLRISC

\+ Enter ?? for more actions

DC Discontinue RN (Renew) VF Verify

HD (Hold) OC (On Call) FL Flag

ED Edit AL Activity Logs

Select Item(s): Next Screen// VF Verify

Now doing allergy checks. Please wait...

Now processing Clinical Reminder Order Checks. Please wait ...

<span id="Page_141" class="anchor"></span>

Now Processing Enhanced Order Checks! Please wait...

================================================================================

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with DOPAMINE 5000 MG:

PHENELZINE SULFATE TAB C 03/25/13 04/01/13 A

Give: 15MG PO TID

Concurrent use of MAOIs may result in potentiation of sympathomimetic

effects, which may result in headaches, hypertensive crisis, toxic

neurological effects, and malignant hyperpyrexia. Fatalities have

occurred.

================================================================================

Display Professional Interaction Monograph(s)? NO//

Do you want to Continue with DOPAMINE 5000 MG? NO// YES

Now creating Pharmacy Intervention

For DOPAMINE 160MG/ML INJ

PROVIDER: PROVIDER,ONE OP

RECOMMENDATION: NO CHANGE

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Press Return to continue...

Would you like to edit this intervention? N// O

================================================================================

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

DOPAMINE 5000 MG

DOPAMINE 5000 MG ? \*\*\*\*\* \*\*\*\*\* N

in 5% DEXTROSE 250 ML 40 ml/hr

Class(es) Involved in Therapeutic Duplication(s): Pressors

================================================================================

Do you wish to continue with the current order? YES//

DOPAMINE 5000 MG ? \*\*\*\*\* \*\*\*\*\* N

in 5% DEXTROSE 250 ML 40 ml/hr

Enter DC to discontinue the above order or press \<RETURN\> to continue:

No action taken!

.

5 Labels needed for doses due at ...

<span id="Page_142" class="anchor"></span>03/25/13 2000 : 03/26/13 0100 : 03/26/13 0600 : 03/26/13 1100 : 03/26/13 1600 :

3 6 9 12 15 18 21 24

..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:..:

A

^ ^ ^ ^ ^

N

Next delivery time is 2000 \*\*\*

Action (PB) P// BYPASS

Inpatient Order Entry Mar 25, 2013@18:20:06 Page: 1 of 2

Ward: 3AS

PID: Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 07/29/44 (68) Wt(kg): 100.00 (03/25/13)

Sex: MALE Admitted: 08/14/12

Dx: SHORTNESS OF BREATH Last transferred: \*\*\*\*\*\*\*\*

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_\_\_\_

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - - - - -

1 AMIODARONE TAB C 03/25/2013 04/01/2013 A

Give: 200MG PO TID

2 DOPAMINE 5000 MG C 03/25/2013 04/25/2013 A

in 5% DEXTROSE 250 ML 40 ml/hr

3 PHENELZINE SULFATE TAB C 03/25/2013 04/01/2013 A

Give: 15MG PO TID

4 WARFARIN TAB C 03/25/2013 03/26/2013 A

Give: 10MG PO QPM

\- - - - - - - - - - - - - - N O N - V E R I F I E D - - - - - - - - - - - - - -

5 CIMETIDINE TAB C 03/25/2013 04/24/2013 N

\+ Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Next Screen//

# # Error Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three levels of errors have been established; System, Drug, and Order. System and Drug level errors were introduced with the release of MOCHA v1.0. Order level errors are introduced with Dosing Order Checks with the release of MOCHA v2.0.

## System Level Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a system level error occurs in MOCHA v2.0 and subsequent versions, no Drug Interaction, Duplicate Therapy, Dosing, or Pharmacogenomic Order Checks will be performed for any drugs. Other order checks that do not use the FDB database will still be performed such as Duplicate Drug, CPRS order checks, etc.

The ability to turn on and off Dosing Order Checks for all orders will be available in MOCHA v2.0 and subsequent versions. However, this functionality should not be used unless prior authorization has been received from Pharmacy Benefits Management (PBM). PBM will only authorize if local approval has been granted by the Medical Center Patient Safety Office and the Medical Center Director. PBM should be notified of this decision by the Pharmacy Chief via email to the <span class="mark">REDACTED</span> Outlook mail group. PBM in turn will notify Patient Care Services, the National Patient Safety Office and the Office of Information and Technology (OIT).

Examples of system level errors are displayed in the table below for Pharmacy and CPRS:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 40%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Level</strong></th>
<th><strong>Error Message</strong></th>
<th><strong>Reason</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>MOCHA v2.1 – Backdoor Pharmacy System Level Errors</strong></td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>Vendor Database cannot be reached.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Please perform a manual PGx Order check by using the check Pharmacogenomic Interaction option for Drug: &lt;DRUG NAME&gt; Reason(s): Pharmacogenomic Lab Data could not be retrieved at this time.</td>
<td><p>The Health Data Repository (HDR) could not be reached to retrieve the patient’s Pharmacogenomic lab data and the VA product the dispense drug is matched to is PGx eligible.</p>
<p>If the PGx action is Interruptive, the Action Text Long and the Monitoring Text Long will display to the user. If it is informative, that information will not display to the user.</p></td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>The connection to the vendor database has been disabled.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>Vendor database updates are being processed</td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>An unexpected error has occurred</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Dosing Checks could not be performed</td>
<td>Vendor Database cannot be reached.</td>
</tr>
<tr class="even">
<td>System</td>
<td>Dosing Checks could not be performed</td>
<td>The connection to the vendor database has been disabled.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Dosing Checks could not be performed</td>
<td>Vendor database updates are being processed</td>
</tr>
<tr class="even">
<td>System</td>
<td>Dosing Checks are not available, please complete a manual check for appropriate Dosing</td>
<td>Dosing Order Checks have been disabled*</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Dosing Checks could not be performed.</td>
<td>An unexpected error has occurred.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>MOCHA v2.1– CPRS System Level Errors</strong></td>
</tr>
<tr class="odd">
<td>System</td>
<td><p>These checks could not be completed for this patient:</p>
<p>Drug Interactions</p>
<p>Duplicate Therapy</p>
<p>Dosing</p></td>
<td>N/A</td>
</tr>
<tr class="even">
<td>System</td>
<td>Pharmacogenomic lab data could not be retrieved at this time. &lt;ORDERABLE ITEM NAME&gt; and &lt;GENE&gt;.</td>
<td><p>The Health Data Repository (HDR) could not be reached to retrieve the patient’s Pharmacogenomic lab data and the VA product the dispense drug is matched to is PGx eligible.</p>
<p>If the PGx action is Interruptive, the Action Text Long and the Monitoring Text Long will display to the user. If it is informative, that information will not display to the user.</p></td>
</tr>
<tr class="odd">
<td>System</td>
<td><p>These checks could not be completed for this patient:</p>
<p>Dosing</p></td>
<td><p>An unexpected error has occurred* or</p>
<p>Dosing Order Checks have been disabled.*</p></td>
</tr>
</tbody>
</table>

\* Reason not displayed to the user.

<span id="Page_145" class="anchor"></span>If the message, ‘Vendor database cannot be reached’ is displayed, this usually means that the link between VistA and the COTS database is down and the two systems are not communicating.

If the message, ‘Pharmacogenomic lab data could not be retrieved at this time’ is displayed, this usually means that the link between VistA and the HDR database that stores the PGx lab data is down. This occurs when the drug being ordered is a PGx eligible drug and the two systems are not communicating.

If the message, ‘The connection to the vendor database has been disabled’ is displayed, this indicates that a specific PDM option, *Enable/Disable Vendor Database Link* has been used to disable the interface.

If the message, ‘Dosing Checks are not available, please complete a manual check for appropriate Dosing’ is displayed, this indicates that a specific PDM option, *Enable/Disable Dosing Order Checks* has been used to disable Dosing Order Checks.

The pharmacy ADPAC or IRM support person should be contacted if any of the three messages that were just mentioned are displayed.

If the message, ‘Vendor database updates are being processed’ is displayed, this means that the FDB database is being updated. The standard and/or custom updates should not take long and will probably be done when there are few users are on the system. Most users will never see this reason.

If the message, ‘An unexpected error has occurred’ is displayed, this could indicate a problem in the software, or even a network issue. This should be reported immediately.

System level errors will be shown for every order being processed; once for the Enhanced Order Checks (i.e. Drug Interactions, Duplicate Therapy) and once when Dosing Order Checks are being performed. The exception to this is when Dosing Order Checks have been disabled using the PDM option, *Enable/Disable Dosing Order Checks*. The message stating that the ‘Dosing Checks are not available, please complete a manual check for appropriate Dosing’ will only be seen once per patient session.

## Drug Level Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second error level is for the drug. No Drug Interaction, Duplicate Therapy or Dosing Order Checks will be performed for a specific drug in this case.

When a user is processing an order, the user may see a drug level error for the prospective drug that is being processed or for a drug that is on the profile. If the drug level error is displayed for the prospective drug that is being processed, no Drug Interaction or Duplicate Therapy Order Checks will be performed against any profile drug (local or remote). If a drug level error exists for one of the profile drugs also, it will NOT be displayed because it would just be redundant. The only exception to this is when multiple prospective drugs, such as multiple IV Additives or multiple IV Solutions, marked as PreMix, are found within an IV order. In this case, a drug level error message may be displayed against one of the prospective drugs and another drug level error may be seen for a profile drug.

If a drug level error is displayed for the profile drug, no Drug Interaction or Duplicate Therapy Order Checks will be performed on that profile drug against any prospective drugs being processed within the patient session.

Profile drug errors will only be shown once per patient session. So if a user processes several more orders, the user will not see the error again. However, if the user exits the option or works on another patient and at some later time reselects this patient to process new orders or take action on any existing orders, the user will be shown the profile drug error once again.

<span id="Page_146" class="anchor"></span>If an order is edited and a new order is created, a drug level error will only be displayed once for both processes.

Examples of drug level errors are displayed in the table below for Pharmacy and CPRS:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Level</strong></th>
<th><strong>Error Message</strong></th>
<th><strong>Reason</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>MOCHA v2.1 – Backdoor Pharmacy Drug Level Errors</strong></td>
</tr>
<tr class="even">
<td>Drug (prospective)</td>
<td>Order Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate Dosing</td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p></td>
</tr>
<tr class="odd">
<td>Drug (profile)</td>
<td><p>Order Checks could not be done for &lt;Remote&gt; Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions and Duplicate Therapy.</p>
<p>&lt;Remote&gt; indicator only for remote outpatient medication orders</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p></td>
</tr>
<tr class="even">
<td>Drug</td>
<td>Enhanced Order Checks cannot be performed for Local or Local Outpatient Drug: &lt;DRUG NAME&gt;</td>
<td>Drug not matched to NDF</td>
</tr>
<tr class="odd">
<td>Drug (profile – pending outpatient or pending unit dose order)</td>
<td>Enhanced Order Checks cannot be performed for Orderable Item: &lt;OI Name&gt;</td>
<td>No Dispense Drug found</td>
</tr>
<tr class="even">
<td>Drug</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt; (only if edit performed on IP order and only when dosage check performed)</td>
<td>Drug not matched to NDF</td>
</tr>
<tr class="odd">
<td>Drug</td>
<td><p>Dosing Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for appropriate Dosing (only if edit performed on IP order and only when dosage check performed)</p>
<p>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy, appropriate Dosing, and Pharmacogenomics.</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p>
<p>If the VA Product the Dispense Drug is matched to does not have a GCNSEQNO and is PGx Eligible, Pharmacogenomics will be added to the error message.</p></td>
</tr>
<tr class="even">
<td colspan="3"><strong>FDB v4.5 – Backdoor Pharmacy Drug Level Errors</strong></td>
</tr>
<tr class="odd">
<td>Drug</td>
<td>Recommended frequency of &lt;DRUG NAME&gt;: Unable to convert units: &lt;DOSE UNIT&gt; to &lt;DOSE UNIT&gt;. A frequency check was not performed because the ordered dose of &lt;DOSE UNIT&gt; is not convertible to the dose screening unit of measure of &lt;DOSE UNIT&gt;.</td>
<td>The Dose Units in the VistA order may not have a match in the FDB tables for the drug.<br />
<br />
Notify the NDF team using Request Change to Dose Unit [PSS DOSE UNIT REQUEST] option to request a review/change.</td>
</tr>
<tr class="even">
<td>Drug</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt; Reason(s) for &lt;DRUG ROUTE&gt;: &lt;DRUG NAME&gt; is contraindicated for this patient. Do NOT prescribe/administer this drug by the CONTRAINDICATED &lt;DRUG ROUTE&gt;.</td>
<td>The chosen route is contraindicated and should not be selected.</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>MOCHA v2.1– CPRS Drug Level Errors</strong></td>
</tr>
<tr class="even">
<td>Drug (prospective)</td>
<td><p>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate Dosing.</p>
<p>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy, appropriate Dosing, and Pharmacogenomics.</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p>
<p>Drug not matched to NDF*</p>
<p>If the VA Product the Dispense Drug is matched to does not have a GCNSEQNO and is PGx Eligible, Pharmacogenomics will be added to the error message.</p></td>
</tr>
<tr class="odd">
<td>Drug (profile)</td>
<td><p>Order Checks could not be done for &lt;Remote&gt; Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions and Duplicate Therapy.</p>
<p>&lt;Remote&gt; indicator only for remote orders</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p>
<p>Drug not matched to NDF*</p></td>
</tr>
<tr class="even">
<td>Drug (prospective – outpatient and inpatient (UD))</td>
<td>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate Dosing.</td>
<td>No active dispense drug could be found *</td>
</tr>
<tr class="odd">
<td>Drug (prospective)</td>
<td>Dosing Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for appropriate Dosing</td>
<td>No active IV Additive/Solution marked for IV fluid order entry could be found*</td>
</tr>
</tbody>
</table>

\*Reason not displayed to user.

<u>Please Note:</u> \<Drug Name\> for error messages:

- CPRS simple orders (OP & IP & IV) àOI Name + Dosage Form (DF)
- CPRS complex orders (OP & IP & IV) à OI Name + DF (Dose=XX)
- OP & UD pharmacy backdoor simple orders àDispense Drug
- OP pharmacy backdoor complex orders àDispense Drug
- IV order with IV Additives (pharmacy backdoor) àIV Additive print name + Strength + Unit
- IV order with IV Solution (PreMix) pharmacy backdoor à IV Solution print name (1) + Volume

If a drug is not matched to NDF, a GCNSEQNO cannot be obtained to identify the drug to FDB in order to perform a Drug Interaction, Duplicate Therapy or Dosing Order Check. The reason Drug not matched to NDF will be displayed.

The software, within the error message text, will distinguish an inpatient vs. an outpatient order when processing inpatient medication orders. The inpatient order will have the text Local Drug displayed before the drug name, whereas the outpatient order will have the text Local Outpatient Drug displayed before the drug name.

A remote order will have the text Remote Drug displayed before the drug name.

The drug may be matched to NDF, but the VA Product, to which it is matched, may not have a GCNSEQNO assigned or the GCNSEQNO in our VA Product file does not match up with a valid GCNSEQNO in the FDB database. In these cases, a generic message will be displayed and the reasons will not be displayed to the user. An error message will not be displayed if the EXCLUDE DRG-DRG INTERACTION CK field for the VA Product is marked ‘Yes’.

In some rare cases you may also see drug level errors for the Orderable Item with reasons such as No Dispense Drug found for a profile pending outpatient order or a profile pending unit dose order. The reason this error is displayed is because the software could not find an active dispense drug. A generic error message will be displayed to the CPRS user in these cases.

If an active dispense drug cannot be found when an order is entered through the outpatient, inpatient or Non-VA Med dialog in CPRS, a generic message will be displayed for the prospective drug. An example is an active Orderable Item associated with an inactive Dispense Drug. The Dispense Drug is tied to an active IV Additive. When no active IV Additive/Solution is found for a prospective drug entered through the IV Fluid dialog in CPRS upon acceptance, a generic message is displayed indicating that Dosing Checks could not be performed. In all these cases, please jot down this information and report it to your Pharmacy ADPAC so that they can follow up or make corrections. For orders displaying a prospective drug error when entered through CPRS, the pharmacy user will be required to make edits to the drug and/or order to correct the problem when finishing the order through pharmacy backdoor options.

If it is a drug level error through Pharmacy options, the drug name is specified within the message. If it is for an Outpatient medication or an Inpatient unit dose order, the dispense drug name is displayed. If it is for an IV Additive within an IV order, the IV Additive’s print name, strength, and unit are displayed. If it is for an IV Solution marked as a PreMix within an IV order, the IV Solution’s print name and volume are displayed. If a dispense drug cannot be identified for an order, the software will display the orderable item name. Most error messages will provide a reason through pharmacy backdoor options.

For CPRS simple orders regardless of the type of order (i.e. outpatient, inpatient, IV), the error message will minimally display the Orderable Item Name and Dosage Form. For CPRS complex orders, the error message will display the Orderable Item Name, Dosage Form with the Dose specified in parenthesis.

## Order Level Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The final type of error is an order level error that is specific to an order and order type check. You will only see order level errors when Dosing Order Checks are performed.

The table below displays various order level errors seen through Pharmacy and CPRS. This is not a complete list. There are many other reasons that are returned by the vendor software when Dosing Order Checks cannot be performed in MOCHA.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Level</strong></th>
<th><strong>Error Message</strong></th>
<th><strong>Reason</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>MOCHA v2.1 – Backdoor Pharmacy Order Level Errors</strong></td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>One or more required patient parameters unavailable: Age</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Dose Route</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Dose Type</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Dose Rate</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Frequency</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Frequency greater than order duration.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Free Text Dosage could not be evaluated</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>FDB dosing information is not available for this drug.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td><p>Dosing Checks could not be performed for Drug:&lt;DRUG NAME&gt;</p>
<p>Reason(s) for TOPICAL route: No dosing information is available from the database.</p></td>
<td><p>No dosing information found in database.</p>
<p>If the medication route is not valid for the drug, but is not contraindicated, the message will display the route and the message that no dosing information is available from the database.</p></td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Free Text Infusion Rate could not be evaluated.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>An unexpected error has occurred</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>FDB v4.5 – Backdoor Pharmacy Order Level Errors</strong></td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug &lt;DRUG NAME&gt;</td>
<td>&lt;DRUG NAME&gt; has a management or monitoring precaution for this patient. The use of antineoplastic drugs in neonates, infants, and pediatric patients (age &lt;18 years) is protocol specific; please check the protocol for appropriate dosing of this agent.</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Reason(s) for &lt;ROUTE&gt; route: Screening supports the ordered drug. However, the combination of patient and order information does not result in a match.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Dose threshold screening was not performed. This chemo drug screening record is coded as a single dose per cycle.</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Dose threshold screening was not performed.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Maximum Single Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Weight is required</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Weight is required</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Weight is required</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Maximum Single Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Body surface area is required</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Body surface area is required</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Body surface area is required</td>
</tr>
<tr class="even">
<td colspan="3"><strong>MOCHA v2.1 CPRS Order Level Error</strong></td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Maximum Single Dose Check could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for appropriate Dosing</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Max Daily Dose Check could not be done for Drug:&lt;Drug Name&gt;, please complete a manual check for appropriate Dosing</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be done for Drug:&lt;Drug:&lt;Drug Name&gt;, please complete a manual check for appropriate Dosing</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Maximum Single Dose Check could not be done for Drug:&lt;DRUG NAME&gt;</td>
<td>No weight documented for patient.</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Max Daily Dose Check could not be done for Drug:&lt;DRUG NAME&gt;</td>
<td>No weight documented for patient.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be done for Drug:&lt;DRUG NAME&gt;</td>
<td>No weight documented for patient.</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Maximum Single Dose Check could not be done for Drug:&lt;DRUG NAME&gt;</td>
<td>No weight and/or height documented for patient.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Max Daily Dose Check could not be done for Drug:&lt;DRUG NAME&gt;</td>
<td>No weight and/or height documented for patient.</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be done for Drug:&lt;DRUG NAME&gt;</td>
<td>No weight and/or height documented for patient.</td>
</tr>
</tbody>
</table>

\* Reason not displayed to the user for all errors with the exception of those listed in the table.

If the age for a patient is not available, the first error will be displayed.

If the message ‘Invalid or Undefined Dose Route’ is displayed, the most likely reason is that your Local Medication Route used in the order is not matched to a Standard Medication Route. Remember the Standard Medication Route is mapped to an FDB Dose Route and without it the Dosing Order Check cannot be performed.

If the message ‘Free text dosage could not be evaluated’ is displayed, it means that the order has a free text dosage that the software cannot interpret. Many business rules have been created to try to evaluate free text dosages. However, care was taken that the dosage be correctly interpreted. Remember a Local Possible Dosage can always be created with the Dose Unit and Numeric Dose defined to prevent this order level error message from being displayed.

If the reason is ‘FDB dosing information is not available for this drug’, it does not mean that FDB does not have any dosing records for the drug being ordered, it just means that the data that was sent in for the drug may not have matched up to a particular record. This message may be displayed because your Local Medication Route is not associated with a FDB dose route that is found in any of the drug’s dosing records or the Dose Unit for your Local Possible Dosage does not match a FDB Dose Unit (mg vs. patch) for the drug.

### Warning Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be some messages returned that are not considered error messages, but warn a user that a drug is not recommended for the patient because of the patient’s age or dosing has not been established for a patient of a certain age. Two of these messages are listed in the table below.

| Level                                   | Warning Message                                  | Warning                                             |
|---------------------------------------------|------------------------------------------------------|---------------------------------------------------------|
| MOCHA v2.1 – Backdoor Pharmacy and CPRS |                                                      |                                                         |
| Order Level                                 | Maximum Single Dose Check Warning for \<DRUG NAME\>: | This drug is not recommended for a patient of this age. |
| Order Level                                 | Maximum Single Dose Check Warning for \<DRUG NAME\>: | Dosing is not established for a patient of this age.    |
| Order Level                                 | Dosing Order Check Warning for \<DRUG NAME\>:        | This drug is not recommended for a patient of this age. |
| Order Level                                 | Dosing Order Check Warning for \<DRUG NAME\>:        | Dosing is not established for a patient of this age.    |

# Appendix A – Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 40%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Level</strong></th>
<th><strong>Error Message</strong></th>
<th><strong>Reason</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>MOCHA v2.1– Backdoor Pharmacy System Level Errors</strong></td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>Vendor Database cannot be reached.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Please perform a manual PGx Order check by using the check Pharmacogenomic Interaction option for Drug: &lt;DRUG NAME NAME&gt; Reason(s): Pharmacogenomic Lab Data could not be retrieved at this time.</td>
<td><p>The Health Data Repository (HDR) could not be reached to retrieve the patient’s Pharmacogenomic lab data and the VA product the dispense drug is matched to is PGx eligible.</p>
<p>If the PGx action is Interruptive, the Action Text Long and the Monitoring Text Long will display to the user. If it is informative, that information will not display to the user.</p></td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed.</td>
<td>The connection to the vendor database has been disabled.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>Vendor database updates are being processed</td>
</tr>
<tr class="even">
<td>System</td>
<td>No Enhanced Order Checks can be performed</td>
<td>An unexpected error has occurred</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Dosing Checks could not be performed</td>
<td>Vendor Database cannot be reached.</td>
</tr>
<tr class="even">
<td>System</td>
<td>Dosing Checks could not be performed</td>
<td>The connection to the vendor database has been disabled.</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Dosing Checks could not be performed</td>
<td>Vendor database updates are being processed</td>
</tr>
<tr class="even">
<td>System</td>
<td>Dosing Checks are not available, please complete a manual check for appropriate Dosing</td>
<td>Dosing Order Checks have been disabled*</td>
</tr>
<tr class="odd">
<td>System</td>
<td>Dosing Checks could not be performed.</td>
<td>An unexpected error has occurred.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>MOCHA v2.1 – CPRS System Level Errors</strong></td>
</tr>
<tr class="odd">
<td>System</td>
<td><p>These checks could not be completed for this patient:</p>
<p>Drug Interactions</p>
<p>Duplicate Therapy</p>
<p>Dosing</p></td>
<td>N/A</td>
</tr>
<tr class="even">
<td>System</td>
<td>Pharmacogenomic lab data could not be retrieved at this time. &lt;ORDERABLE ITEM NAME&gt; and &lt;GENE&gt;.</td>
<td><p>The Health Data Repository (HDR) could not be reached to retrieve the patient’s Pharmacogenomic lab data and the VA product the dispense drug is matched to is PGx eligible.</p>
<p>If the PGx action is Interruptive, the Action Text Long and the Monitoring Text Long will display to the user. If it is informative, that information will not display to the user.</p></td>
</tr>
<tr class="odd">
<td>System</td>
<td><p>These checks could not be completed for this patient:</p>
<p>Dosing</p></td>
<td><p>An unexpected error has occurred*</p>
<p>or</p>
<p>Dosing Checks have been disabled.*</p></td>
</tr>
<tr class="even">
<td colspan="3"><strong>MOCHA v2.1 – Backdoor Pharmacy Drug Level Errors</strong></td>
</tr>
<tr class="odd">
<td>Drug (prospective)</td>
<td><p>Order Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate</p>
<p>Dosing</p>
<p>Order Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy, appropriate dosing, and Pharmacogenomics</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p>
<p>If the VA Product the Dispense Drug is matched to does not have a GCNSEQNO and is PGx Eligible, Pharmacogenomics will be added to the error message.</p></td>
</tr>
<tr class="even">
<td>Drug (profile)</td>
<td><p>Order Checks could not be done for &lt;Remote&gt; Drug: &lt;DRUG NAME&gt;, please complete a manual check for Drug Interactions and Duplicate Therapy</p>
<p>&lt;Remote&gt; indicator only for remote orders</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p></td>
</tr>
<tr class="odd">
<td>Drug (profile – pending outpatient or pending unit dose order)</td>
<td>Enhanced Order Checks cannot be performed for Orderable Item: &lt;OI Name&gt;</td>
<td>No Dispense Drug found</td>
</tr>
<tr class="even">
<td>Drug</td>
<td>Enhanced Order Checks cannot be performed for Local or Local Outpatient Drug: &lt;DRUG NAME&gt;</td>
<td>Drug not matched to NDF</td>
</tr>
<tr class="odd">
<td>Drug</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt; (only if edit performed on IP order and only when dosage check performed)</td>
<td>Drug not matched to NDF</td>
</tr>
<tr class="even">
<td>Drug</td>
<td><p>Dosing Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for appropriate Dosing (only if edit performed on IP order and only when dosage check performed)</p>
<p>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy, appropriate Dosing, and Pharmacogenomics.</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p>
<p>If the VA Product the Dispense Drug is matched to does not have a GCNSEQNO and is PGx Eligible, Pharmacogenomics will be added to the error message.</p></td>
</tr>
<tr class="odd">
<td colspan="3"><strong>FDB v4.5 – Backdoor Pharmacy Drug Level Errors</strong></td>
</tr>
<tr class="even">
<td>Drug</td>
<td>Recommended frequency of &lt;DRUG NAME&gt;: Unable to convert units: &lt;DOSE UNIT&gt; to &lt;DOSE UNIT&gt;. A frequency check was not performed because the ordered dose of &lt;DOSE UNIT&gt; is not convertible to the dose screening unit of measure of &lt;DOSE UNIT&gt;.</td>
<td>VA customization may exist in which the Dose Units were customized but the patient age is not within bounds of the customized age bands. VA NDF team to refer to PECS to introduce and/or update VA customizations for the patient ages.</td>
</tr>
<tr class="odd">
<td>Drug</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt; Reason(s) for &lt;DRUG ROUTE&gt;: &lt;DRUG NAME&gt; is contraindicated for this patient. Do NOT prescribe/administer this drug by the CONTRAINDICATED &lt;DRUG ROUTE&gt;.</td>
<td>The chosen route is contraindicated and should not be selected.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>MOCHA v2.1– CPRS Drug Level Errors</strong></td>
</tr>
<tr class="odd">
<td>Drug (prospective)</td>
<td><p>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate Dosing.</p>
<p>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy, appropriate Dosing, and Pharmacogenomics.</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p>
<p>Drug not matched to NDF*</p>
<p>If the VA Product* the Dispense Drug is matched to does not have a GCNSEQNO and is PGx Eligible, Pharmacogenomics will be added to the error message.</p>
<p>Drug not matched to NDF*</p></td>
</tr>
<tr class="even">
<td>Drug (profile)</td>
<td><p>Order Checks could not be done for &lt;Remote&gt; Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions and Duplicate Therapy.</p>
<p>&lt;Remote&gt; indicator only for remote orders.</p></td>
<td><p>No GCNSEQNO exists for VA Product*</p>
<p>Bad GCNSEQNO assigned to VA Product*</p>
<p>Drug not matched to NDF*</p></td>
</tr>
<tr class="odd">
<td>Drug (prospective – outpatient and inpatient (UD))</td>
<td>Order Checks could not be done for Drug: &lt;Drug Name&gt;, please complete a manual check for Drug Interactions, Duplicate Therapy and appropriate Dosing.</td>
<td>No active dispense drug could be found*</td>
</tr>
<tr class="even">
<td>Drug (prospective – IV order)</td>
<td>Dosing Checks could not be done for Drug: &lt;DRUG NAME&gt;, please complete a manual check for appropriate Dosing</td>
<td>No active IV Additive/Solution marked for IV Fluid order entry could be found*</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>MOCHA v2.1 – Backdoor Pharmacy Order Level Errors</strong></td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>One or more required patient parameters unavailable: Age</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Dose Route</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Dose Type</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Dose Rate</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Invalid or Undefined Frequency</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Max Daily Dose Check could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>Frequency greater than order duration.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>Free Text Dosage could not be evaluated</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>FDB dosing information is not available for this drug.</td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug:&lt;DRUG NAME&gt;</td>
<td>No dosing information found in database.</td>
</tr>
<tr class="odd">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td><p>Free Text Infusion Rate could not be</p>
<p>evaluated</p></td>
</tr>
<tr class="even">
<td>Order Level</td>
<td>Dosing Checks could not be performed for Drug: &lt;DRUG NAME&gt;</td>
<td>An unexpected error has occurred</td>
</tr>
</tbody>
</table>

| FDB v4.5 – Backdoor Pharmacy Order Level Errors |                                                                                                                            |                                                                                                                                                                                                                                                               |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Order Level                                         | Dosing Checks could not be performed for Drug \<DRUG NAME\>                                                                | \<DRUG NAME\> has a management or monitoring precaution for this patient. The use of antineoplastic drugs in neonates, infants, and pediatric patients (age \<18 years) is protocol specific; please check the protocol for appropriate dosing of this agent. |
| Order Level                                         | Dosing Checks could not be performed for Drug \<DRUG NAME\>                                                                | Reason(s) for \<ROUTE\> route: Screening supports the ordered drug. However, the combination of patient and order information does not result in a match.                                                                                                     |
| Order Level                                         | Max Daily Dose Check could not be performed for Drug: \<DRUG NAME\>                                                        | Dose threshold screening was not performed. This chemo drug screening record is coded as a single dose per cycle.                                                                                                                                             |
| Order Level                                         | Max Daily Dose Check could not be performed for Drug: \<DRUG NAME\>                                                        | Dose threshold screening was not performed.                                                                                                                                                                                                                   |
| Order Level                                         | Maximum Single Dose Check could not be performed for Drug:\<DRUG NAME\>                                                    | Weight is required                                                                                                                                                                                                                                            |
| Order Level                                         | Max Daily Dose Check could not be performed for Drug:\<DRUG NAME\>                                                         | Weight is required                                                                                                                                                                                                                                            |
| Order Level                                         | Dosing Checks could not be performed for Drug: \<DRUG NAME\>                                                               | Weight is required                                                                                                                                                                                                                                            |
| Order Level                                         | Maximum Single Dose Check could not be performed for Drug:\<DRUG NAME\>                                                    | Body surface area is required                                                                                                                                                                                                                                 |
| Order Level                                         | Max Daily Dose Check could not be performed for Drug:\<DRUG NAME\>                                                         | Body surface area is required                                                                                                                                                                                                                                 |
| Order Level                                         | Dosing Checks could not be performed for Drug: \<DRUG NAME\>                                                               | Body surface area is required                                                                                                                                                                                                                                 |
| MOCHA v2.1 CPRS Order Level Error               |                                                                                                                            |                                                                                                                                                                                                                                                               |
| Order Level                                         | Maximum Single Dose Check could not be done for Drug: \<Drug Name\>, please complete a manual check for appropriate Dosing | N/A                                                                                                                                                                                                                                                           |
| Order Level                                         | Max Daily Dose Check could not be done for Drug:\<Drug Name\>, please complete a manual check for appropriate Dosing       | N/A                                                                                                                                                                                                                                                           |
| Order Level                                         | Dosing Checks could not be done for Drug:\<Drug:\<Drug Name\>, please complete a manual check for appropriate Dosing       | N/A                                                                                                                                                                                                                                                           |
| Order Level                                         | Maximum Single Dose Check could not be done for Drug:\<DRUG NAME\>                                                         | No weight documented for patient.                                                                                                                                                                                                                             |
| Order Level                                         | Max Daily Dose Check could not be done for Drug:\<DRUG NAME\>                                                              | No weight documented for patient.                                                                                                                                                                                                                             |
| Order Level                                         | Dosing Checks could not be done for Drug:\<DRUG NAME\>                                                                     | No weight documented for patient.                                                                                                                                                                                                                             |
| Order Level                                         | Maximum Single Dose Check could not be done for Drug:\<DRUG NAME\>                                                         | No weight and/or height documented for patient.                                                                                                                                                                                                               |
| Order Level                                         | Max Daily Dose Check could not be done for Drug:\<DRUG NAME\>                                                              | No weight and/or height documented for patient.                                                                                                                                                                                                               |
| Order Level                                         | Dosing Checks could not be done for Drug:\<DRUG NAME\>                                                                     | No weight and/or height documented for patient.                                                                                                                                                                                                               |

\* Reason not displayed to user for all errors with the exception of those listed in the table.

<u>Please Note:</u> \<Drug Name\> for error messages:

CPRS simple orders (OP & IP & IV) àOI Name + Dosage Form (DF)

CPRS complex orders (OP & IP & IV) à OI Name + DF (Dose=XX)

OP & UD pharmacy backdoor simple orders àDispense Drug

OP pharmacy backdoor complex orders àDispense Drug

IV order with IV Additives (pharmacy backdoor) àIV Additive print name + Strength + Unit

IV order with IV Solution (PreMix) pharmacy backdoor à IV Solution print name (1) + Volume

| Level                                   | Warning Message                                  | Warning                                             |
|---------------------------------------------|------------------------------------------------------|---------------------------------------------------------|
| MOCHA v2.1 – Backdoor Pharmacy and CPRS |                                                      |                                                         |
| Order Level                                 | Maximum Single Dose Check Warning for \<DRUG NAME\>: | This drug is not recommended for a patient of this age. |
| Order Level                                 | Maximum Single Dose Check Warning for \<DRUG NAME\>: | Dosing is not established for a patient of this age.    |
| Order Level                                 | Dosing Order Check Warning for \<DRUG NAME\>:        | This drug is not recommended for a patient of this age. |
| Order Level                                 | Dosing Order Check Warning for \<DRUG NAME\>:        | Dosing is not established for a patient of this age.    |

# Appendix B – Standard Medication Routes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of April 2025, the following are the Standard Medication Routes.

| <u>Standard VA Medication Routes Name</u> | <u>FDB Route</u> <sup>\*</sup> |
|-----------------------------------------------|------------------------------------|
| ADDUCTOR CANAL BLOCK                      | ADDUCTOR CANAL BLOCK           |
| BUCCAL                                    | BUCCAL                         |
| CERVICAL                                  | CERVICAL                       |
| DENTAL                                    | DENTAL                         |
| ECTOPIC GESTATIONAL SAC                   | ECTOPIC GESTATIONAL SAC        |
| ENDOTRACHEAL                              | ENDOTRACHEAL                   |
| ENTERAL                                   | ORAL                           |
| EPIDURAL                                  | EPIDURAL                       |
| EXTRACORPOREAL                            | EXTRACORPOREAL                 |
| HAND BULB NEBULIZER                       | HAND BULB NEBULIZER            |
| IMPLANT                                   | IMPLANT                        |
| INFILTRATION                              | INFILTRATION                   |
| INFRACLAVICULAR                           | INFRACLAVICULAR                |
| INHALATION                                | INHALATION                     |
| INSTILLATION                              | INSTILLATION                   |
| INTERSCALENE                              | INTERSCALENE                   |
| INTRA-AMNIOTIC                            | INTRA-AMNIOTIC                 |
| INTRA-ARTERIAL                            | INTRA-ARTERIAL                 |
| INTRA-ARTICULAR                           | INTRA-ARTICULAR                |
| INTRA-PYELOCALYCEAL                       | INTRA-PYELOCALYCEAL            |
| INTRA-SUBACROMIAL SPACE                   | INTRA-SUBACROMIAL SPACE        |
| INTRA-UMBILICAL VEIN                      | INTRA-UMBILICAL VEIN           |
| INTRABURSAL                               | INTRABURSAL                    |
| INTRACAMERAL                              | INTRACAMERAL                   |
| INTRACANALICULAR                          | INTRACANALICULAR               |
| INTRACARDIAC                              | INTRACARDIAC                   |
| INTRACATHETER                             | INTRA-CATHETER                 |
| INTRACAUDAL                               | CAUDAL BLOCK                   |
| INTRACAVERNOSAL                           | INTRA-CAVERNOSAL               |
| INTRACAVITARY                             | INTRACAVITY                    |
| INTRACORONARY                             | INTRACORONARY                  |
| INTRADERMAL                               | INTRADERMAL                    |
| INTRADETRUSOR                             | INTRADETRUSOR                  |
| INTRADUCTAL                               | INTRADUCTAL                    |
| INTRALESIONAL                             | INTRALESIONAL                  |
| INTRALUMBAR                               | INTRALUMBAR                    |
| INTRALYMPHATIC                            | INTRALYMPHATIC                 |
| INTRAMUSCULAR                             | INTRAMUSCULAR                  |
| INTRAOCULAR                               | INTRAOCULAR                    |
| INTRAOSSEOUS                              | INTRAOSSEOUS                   |
| INTRAPERICARDIAL                          | INTRAPERICARDIAL               |
| INTRAPERITONEAL                           | INTRAPERITONEAL                |
| INTRAPLEURAL                              | INTRAPLEURAL                   |
| INTRAPROSTATIC                            | INTRAPROSTATIC                 |
| INTRASALIVARY GLAND                       | INTRASALIVARY GLAND            |
| INTRASPINAL                               | INTRASPINAL                    |
| INTRASYNOVIAL                             | INTRASYNOVIAL                  |
| INTRATHECAL                               | INTRATHECAL                    |
| INTRATRACHEAL                             | INTRATRACHEAL                  |
| INTRATYMPANIC                             | INTRATYMPANIC                  |
| INTRAUTERINE                              | INTRAUTERINE                   |
| INTRAVARICEAL                             | INTRAVARICEAL                  |
| INTRAVENOUS                               | INTRAVENOUS                    |
| INTRAVENTRICULAR                          | INTRAVENTRICULAR               |
| INTRAVESICAL                              | INTRAVESICAL                   |
| INTRAVITREAL                              | INTRAVITREAL                   |
| IONTOPHORESIS                             | IONTOPHORETIC                  |
| IPPB                                      | IPPB                           |
| IRRIGATION                                | IRRIGATION                     |
| JUXTASCLERAL                              | JUXTASCLERAL                   |
| MISCELLANEOUS                             | MISCELLANEOUS                  |
| MUCOUS MEMBRANE                           | MUCOUS MEMBRANE                |
| NASAL                                     | INTRANASAL                     |
| NEBULIZATION                              | NEBULIZATION                   |
| NOT APPLICABLE                            | NOT APPLICABLE                 |
| O2 AEROSOLIZATION                         | O2 AEROSOLIZATION              |
| OPHTHALMIC                                | OPHTHALMIC (EYE)               |
| ORAL                                      | ORAL                           |
| OTIC                                      | OTIC (EAR)                     |
| PERCUTANEOUS                              | PERCUTANEOUS                   |
| PERFUSION                                 | PERFUSION                      |
| PERIARTICULAR                             | PERIARTICULAR                  |
| PERIBULBAR                                | PERIBULBAR                     |
| PERINEURAL INJECTION                      | PERINEURAL INJECTION           |
| RECTAL                                    | RECTAL                         |
| RETROBULBAR                               | RETROBULBAR                    |
| SUBCONJUNCTIVAL                           | SUBCONJUNCTIVAL                |
| SUBCUTANEOUS                              | SUBCUTANEOUS                   |
| SUBDERMAL                                 | SUBDERMAL                      |
| SUBLESIONAL                               | SUBLESIONAL                    |
| SUBLINGUAL                                | SUBLINGUAL                     |
| SUBMUCOSAL                                | SUBMUCOSAL INJECTION           |
| SUBRETINAL                                | SUBRETINAL                     |
| SUBTENONS                                 | SUB-TENON                      |
| SUPRACHOROIDAL                            | SUPRACHOROIDAL                 |
| TENDON SHEATH INJ                         | TENDON SHEATH INJ              |
| TOPICAL                                   | TOPICAL                        |
| TRANSDERMAL                               | TRANSDERMAL                    |
| TRANSLINGUAL                              | TRANSLINGUAL                   |
| TRANSTRACHEAL                             | TRANSTRACHEAL                  |
| TRANSURETHRAL                             | TRANSURETHRAL                  |
| URETHRAL                                  | INTRA-URETHRAL                 |
| VAGINAL                                   | VAGINAL                        |

# Appendix C – DOSE UNITS File with FDB Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the DOSE UNITS file with FDB mapping.

| DOSE UNIT NAME                                  | SYNONYM                          | MAP TO FDB DOSE UNIT            | DOSE FORM INDICATOR |
|-----------------------------------------------------|--------------------------------------|-------------------------------------|-------------------------|
| AMPULE                                              | AMPULES                              | AMPULE                              | Y                       |
|                                                     | AMP                                  |                                     |                         |
|                                                     | AMPS                                 |                                     |                         |
| APPLICATION(S)                                      | APPLICATIONS                         | APPLICATIONS                        | Y                       |
|                                                     | APPLICATION                          |                                     |                         |
|                                                     | APPLIC                               |                                     |                         |
| APPLICATORFUL(S)                                    | APPFUL                               | APPLICATORFUL                       | Y                       |
|                                                     | APPLICATORFUL/S                      |                                     |                         |
|                                                     | APPLICATOR                           |                                     |                         |
|                                                     | APPLICATORFUL                        |                                     |                         |
|                                                     | APPLICATORFULS                       |                                     |                         |
|                                                     | APPLICATORS                          |                                     |                         |
| BAR(S)                                              | BAR                                  | BARS                                | Y                       |
|                                                     | BARS                                 |                                     |                         |
| BILLION CELLS                                       |                                      | BILLION CELLS                       | Y                       |
| CAP/TAB                                             | TAB-CAPS                             | TABLET-CAPSULE                      | Y                       |
|                                                     | TAB-CAP                              |                                     |                         |
|                                                     | TAB/CAP                              |                                     |                         |
|                                                     | TABLET-CAPSULE                       |                                     |                         |
|                                                     | TABLET-CAPSULES                      |                                     |                         |
| CAPLET(S)                                           | CAPLET                               | CAPLETS                             | Y                       |
|                                                     | CAPLETS                              |                                     |                         |
| CAPSULE(S)                                          | CAP                                  | CAPSULES                            | Y                       |
|                                                     | CAPS                                 |                                     |                         |
|                                                     | CAPSULE                              |                                     |                         |
|                                                     | CAPSULES                             |                                     |                         |
| CELL                                                | CELLS                                | CELL                                | Y                       |
| CENTIMETER(S)                                       | CENTIMETER                           | CENTIMETERS                         | Y                       |
|                                                     | CM                                   |                                     |                         |
|                                                     | CMS                                  |                                     |                         |
|                                                     | CENTIMETERS                          |                                     |                         |
| COLONY FORMING UNIT                                 | COLONY FORMING UNIT                  | COLONY FORMING UNIT                 | Y                       |
| DROP(S)                                             | DROP                                 | DROPS                               | Y                       |
|                                                     | DROPS                                |                                     |                         |
|                                                     | DRP                                  |                                     |                         |
|                                                     | DRPS                                 |                                     |                         |
|                                                     | GTT                                  |                                     |                         |
|                                                     | GTTS                                 |                                     |                         |
| EACH                                                | EA                                   | EACH                                | Y                       |
|                                                     | EACHES                               |                                     |                         |
| ELISA UNIT(S)                                       | EL UNIT                              | ELISA UNIT                          | N                       |
|                                                     | ELISA UNITS                          |                                     |                         |
|                                                     | ELISA UNIT                           |                                     |                         |
|                                                     | EL.U.                                |                                     |                         |
|                                                     | ELISA UNT                            |                                     |                         |
|                                                     | ELU                                  |                                     |                         |
| FILM(S)                                             | FILM                                 | FILMS                               | Y                       |
|                                                     | FILMS                                |                                     |                         |
| GRAM(S)                                             | G                                    | GRAMS                               | N                       |
|                                                     | GM                                   |                                     |                         |
|                                                     | GMS                                  |                                     |                         |
|                                                     | GRAM                                 |                                     |                         |
|                                                     | GRAMS                                |                                     |                         |
| IMPLANT(S)                                          | IMPLANT                              | IMPLANTS                            | Y                       |
|                                                     | IMPLANTS                             |                                     |                         |
| INCH(ES)                                            | IN                                   | INCHES                              | Y                       |
|                                                     | INCH                                 |                                     |                         |
|                                                     | INCHES                               |                                     |                         |
| INHALATION(S)                                       | INH                                  | INHALATIONS                         | Y                       |
|                                                     | INHALATION                           |                                     |                         |
|                                                     | INHL                                 |                                     |                         |
|                                                     | INHALATIONS                          |                                     |                         |
| INSERT(S)                                           | INSERT                               | INSERTS                             | Y                       |
|                                                     | INSERTS                              |                                     |                         |
| LITER(S)                                            | L                                    | LITERS                              | Y                       |
|                                                     | LITER                                |                                     |                         |
|                                                     | LITERS                               |                                     |                         |
|                                                     | LITRE(S)                             |                                     |                         |
| LOZENGE(S)                                          | LOZENGE                              | LOZENGES                            | Y                       |
|                                                     | LOZENGES                             |                                     |                         |
| MELT                                                | MELTS                                | MELT                                | Y                       |
| MG-PE                                               | MG PE                                | MILLIGRAM PHENYTOIN EQUIVALENT      | N                       |
|                                                     | MILLIGRAM PHENYTOIN EQUIVALENTS      |                                     |                         |
|                                                     | MILLIGRAM PHENYTOIN EQUIVALENT       |                                     |                         |
| MICROGRAM(S)                                        | MCG                                  | MICROGRAMS                          | N                       |
|                                                     | MCGS                                 |                                     |                         |
|                                                     | MICROGRAM                            |                                     |                         |
|                                                     | MICROGRAMS                           |                                     |                         |
| MICROGRAM DIETARY FOLATE                            | MICROGRAM DIETARY FOLATE EQUIVALENTS | MICROGRAM DIETARY FOLATE EQUIVALENT | N                       |
|                                                     | MCG DFE                              |                                     |                         |
| MILLICURIE                                          | MILLICURIES                          | MILLICURIE                          | Y                       |
|                                                     | MCI                                  |                                     |                         |
| MILLIGRAM(S)                                        | MGS                                  | MILLIGRAMS                          | N                       |
|                                                     | MILLIGRAM                            |                                     |                         |
|                                                     | MILLIGRAMS                           |                                     |                         |
|                                                     | MG                                   |                                     |                         |
| MICRO UNIT(S)                                       | MICRO UNIT                           | MICROUNITS                          | N                       |
|                                                     | MICRO UNITS                          |                                     |                         |
|                                                     | MICROUNIT                            |                                     |                         |
|                                                     | MICROUNITS                           |                                     |                         |
| MILLIEQUIVALENT(S)                                  | MILLIEQUIVALENT                      | MILLIEQUIVALENTS                    | N                       |
|                                                     | MILLIEQUIVALENTS                     |                                     |                         |
|                                                     | MEQ                                  |                                     |                         |
|                                                     | MEQS                                 |                                     |                         |
| MILLIGRAM FISH OIL                                  | MILLIGRAMS FISH OIL                  | MILLIGRAM FISH OIL                  | N                       |
|                                                     | MG FISH OIL                          |                                     |                         |
| MILLION CELLS                                       | MMU CELLS                            | MILLION CELLS                       | Y                       |
| MILLION PLAQUE FORMING UNITS                        | MPF UNIT                             | MILLION PLAQUE FORMING UNITS        | Y                       |
|                                                     | MPF UNITS                            |                                     |                         |
| MILLIONUNIT(S)                                      | MILI U                               | MILLION UNITS                       | N                       |
|                                                     | MILI UNIT                            |                                     |                         |
|                                                     | MILI UNITS                           |                                     |                         |
|                                                     | MILU                                 |                                     |                         |
|                                                     | MIU                                  |                                     |                         |
|                                                     | MU                                   |                                     |                         |
|                                                     | MILLION UNT                          |                                     |                         |
|                                                     | MILLION UNIT                         |                                     |                         |
|                                                     | MILLION UNITS                        |                                     |                         |
| MILLILITER(S)                                       | MILLILITER                           | MILLILITERS                         | Y                       |
|                                                     | MILLILITERS                          |                                     |                         |
|                                                     | MILILITERS                           |                                     |                         |
|                                                     | MILILITER                            |                                     |                         |
|                                                     | ML                                   |                                     |                         |
|                                                     | MLS                                  |                                     |                         |
|                                                     | CC                                   |                                     |                         |
|                                                     | CCS                                  |                                     |                         |
| MILLIMOLE(S)                                        | MILLIMOL                             | MILLIMOLES                          | N                       |
|                                                     | MILLIMOLE                            |                                     |                         |
|                                                     | MILLIMOLES                           |                                     |                         |
|                                                     | MILLIMOLS                            |                                     |                         |
|                                                     | MM                                   |                                     |                         |
|                                                     | MMOL                                 |                                     |                         |
|                                                     | MMOLE                                |                                     |                         |
|                                                     | MMOLES                               |                                     |                         |
|                                                     | MMOLS                                |                                     |                         |
| MILLIUNIT                                           | MILLIUNITS                           | MILLIUNIT                           | N                       |
|                                                     | NANOGRAMS                            |                                     |                         |
|                                                     | NG                                   |                                     |                         |
|                                                     | NGS                                  |                                     |                         |
| NANOGRAM(S)                                         | NANOGRAM                             | NANOGRAMS                           | N                       |
|                                                     | NANOGRAMS                            |                                     |                         |
|                                                     | NG                                   |                                     |                         |
|                                                     | NGS                                  |                                     |                         |
| PACKAGE(S)                                          | PACKAGE                              | PACKAGES                            | Y                       |
|                                                     | PACKAGES                             |                                     |                         |
|                                                     | PKGS                                 |                                     |                         |
|                                                     | PKG                                  |                                     |                         |
| PACKET(S)                                           | PACKET                               | PACKETS                             | Y                       |
|                                                     | PACKETS                              |                                     |                         |
| PAD(S)                                              | PAD                                  | PADS                                | Y                       |
|                                                     | PADS                                 |                                     |                         |
| PATCH(ES)                                           | PATCH                                | PATCHES                             | Y                       |
|                                                     | PATCHES                              |                                     |                         |
| PELLET(S)                                           | PELLET                               | PELLETS                             | Y                       |
|                                                     | PELLETS                              |                                     |                         |
| PIECE(S)                                            | PIECE                                | PIECES OF GUM                       | Y                       |
|                                                     | PIECE OF GUM                         |                                     |                         |
|                                                     | PIECES                               |                                     |                         |
|                                                     | PIECES OF GUM                        |                                     |                         |
| PLAQUE FORMING UNIT                                 | PF UNIT                              | PLAQUE FORMING UNIT                 | Y                       |
|                                                     | PLAQUE FORMING UNITS                 |                                     |                         |
| PUFF(S)                                             | PUFF                                 | PUFFS                               | Y                       |
|                                                     | PUFFS                                |                                     |                         |
| <span id="Appendix_C" class="anchor"></span>PUMP(S) | PUMP                                 | PUMPS                               | Y                       |
| SACHET(S)                                           | SACHET                               | SACHETS                             | Y                       |
|                                                     | SACHETS                              |                                     |                         |
| SCOOPFUL(S)                                         | SCOOP                                | SCOOPS                              | Y                       |
|                                                     | SCOOPFUL                             |                                     |                         |
|                                                     | SCOOPFULS                            |                                     |                         |
|                                                     | SCOOPS                               |                                     |                         |
|                                                     | SCOOPSFUL                            |                                     |                         |
|                                                     | SCP                                  |                                     |                         |
| SPRAY(S)                                            | SPR                                  | SPRAY                               | Y                       |
|                                                     | SPRAY                                |                                     |                         |
|                                                     | SPRAYS                               |                                     |                         |
| STRIP(S)                                            | STRIP                                | STRIPS                              | Y                       |
|                                                     | STRIPS                               |                                     |                         |
| SUPPOSITORY(IES)                                    | SUPP                                 | SUPPOSITORY                         | Y                       |
|                                                     | SUPPOSITORIES                        |                                     |                         |
|                                                     | SUPPOSITORY                          |                                     |                         |
|                                                     | SUPPOSITORY/IES                      |                                     |                         |
| TABLESPOONFUL(S)                                    | TABLESPOONFUL                        | TABLESPOONFUL                       | Y                       |
|                                                     | TABLESPOONFULS                       |                                     |                         |
| TABLET(S)                                           | TABLET                               | TABLETS                             | Y                       |
|                                                     | TABLETS                              |                                     |                         |
|                                                     | TABS                                 |                                     |                         |
|                                                     | TAB                                  |                                     |                         |
| TEASPOONFUL(S)                                      | TEASPOONFUL                          | TEASPOONFUL                         | Y                       |
|                                                     | TEASPOONFULS                         |                                     |                         |
| THOUSAND UNITS                                      | THOUU                                | THOUSAND UNITS                      | N                       |
|                                                     | THOUSAND UNIT                        |                                     |                         |
|                                                     | TU                                   |                                     |                         |
| TOWELETTE                                           | TOWELETTES                           | TOWELETTE                           | Y                       |
|                                                     | TOWEL                                |                                     |                         |
|                                                     | TOWELS                               |                                     |                         |
| TUBE                                                | TUBES                                | TUBE                                | Y                       |
| UNIT(S)                                             | U                                    | UNITS                               | N                       |
|                                                     | UNIT                                 |                                     |                         |
|                                                     | UNITS                                |                                     |                         |
|                                                     | UNT                                  |                                     |                         |
|                                                     | UNTS                                 |                                     |                         |
|                                                     | IU                                   |                                     |                         |
| VAGINAL INSERT                                      | VAGINAL INSERTS                      | VAGINAL INSERT                      | Y                       |
| VAGINAL RING                                        | VAG RING                             | VAGINAL RING                        | Y                       |
|                                                     | VAG RINGS                            |                                     |                         |
|                                                     | VAGINAL RINGS                        |                                     |                         |
| VIAL(S)                                             | VIAL                                 | VIALS                               | Y                       |
|                                                     | VIALS                                |                                     |                         |
|                                                     | VIL                                  |                                     |                         |
| WAFER(S)                                            | WAFER                                | WAFERS                              | Y                       |
|                                                     | WAFERS                               |                                     |                         |

# Appendix D – Dose Unit Conversion File (#51.25)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of April 2025, the following are the entries in the DOSE UNIT CONVERSION File.

| DOSE UNIT 1                            | DOSE UNIT 2 | CONVERSION FACTOR |
|--------------------------------------------|-----------------|-----------------------|
| APPFUL                                     | APPLICATORFUL   | 1                     |
| APPLIC                                     | APPLICATIONS    | 1                     |
| APPLICATIONS                               | APPLIC          | 1                     |
| APPLICATORFUL                              | APPFUL          | 1                     |
| BARS                                       | EACH            | 1                     |
| CAPLETS                                    | EACH            | 1                     |
| CAPSULES                                   | EACH            | 1                     |
| CENTIMETERS                                | INCHES          | 0.394                 |
| DROPS                                      | MILLILITERS     | 0.05                  |
| EACH                                       | BARS            | 1                     |
|                                            | TAPLET-CAPSULES | 1                     |
|                                            | CAPLETS         | 1                     |
|                                            | CAPSULES        | 1                     |
|                                            | FILMS           | 1                     |
|                                            | IMPLANTS        | 1                     |
|                                            | INSERTS         | 1                     |
|                                            | LOZENGES        | 1                     |
|                                            | PACKAGES        | 1                     |
|                                            | PADS            | 1                     |
|                                            | PELLETS         | 1                     |
|                                            | PIECES OF GUM   | 1                     |
|                                            | SACHETS         | 1                     |
|                                            | SCOOPS          | 1                     |
|                                            | STRIPS          | 1                     |
|                                            | SUPPOSITORY     | 1                     |
|                                            | TABLETS         | 1                     |
|                                            | VAGINAL RING    | 1                     |
|                                            | VIALS           | 1                     |
|                                            | WAFERS          | 1                     |
|                                            | PACKETS         | 1                     |
|                                            | PATCHES         | 1                     |
|                                            | VAGINAL INSERT  | 1                     |
| FILMS                                      | EACH            | 1                     |
| GRAMS                                      | MILLIGRAMS      | 1,000                 |
|                                            | MICROGRAMS      | 1,000,000             |
| IMPLANTS                                   | EACH            | 1                     |
| INCHES                                     | CENTIMETERS     | 2.54                  |
| INHALATIONS                                | SPRAYS          | 1                     |
|                                            | PUFFS           | 1                     |
| INSERTS                                    | EACH            | 1                     |
| LITERS                                     | MILLILITERS     | 1,000                 |
| LOZENGES                                   | EACH            | 1                     |
| MICROUNITS                                 | MILLION UNITS   | 0.001                 |
| <span id="Page_163" class="anchor"></span> | UNITS           | 0.000001              |
| MICROGRAMS                                 | GRAMS           | 0.000001              |
|                                            | MILLIGRAMS      | 0.001                 |
|                                            | NANOGRAMS       | 1,000                 |
| MILLIGRAMS                                 | GRAMS           | 0.001                 |
|                                            | MICROGRAMS      | 1,000                 |
|                                            | NANOGRAMS       | 1,000,000             |
| MILLILITERS                                | DROPS           | 20                    |
|                                            | LITERS          | 0.001                 |
|                                            | TABLESPOONFUL   | 0.066667              |
|                                            | TEASPOONFUL     | 0.2                   |
| MILLION UNITS                              | MICROUNITS      | 1,000                 |
|                                            | THOUSAND UNITS  | 1,000                 |
|                                            | UNITS           | 1,000,000             |
| NANOGRAMS                                  | MICROGRAMS      | 0.001                 |
|                                            | MILLIGRAMS      | 0.000001              |
| PACKAGES                                   | EACH            | 1                     |
| PACKETS                                    | EACH            | 1                     |
| PADS                                       | EACH            | 1                     |
| PATCHES                                    | EACH            | 1                     |
| PELLETS                                    | EACH            | 1                     |
| PIECES OF GUM                              | EACH            | 1                     |
| PUFFS                                      | SPRAYS          | 1                     |
|                                            | INHALATIONS     | 1                     |
| SACHETS                                    | EACH            | 1                     |
| SCOOPS                                     | EACH            | 1                     |
| SPRAYS                                     | INHALATIONS     | 1                     |
|                                            | PUFFS           | 1                     |
| STRIPS                                     | EACH            | 1                     |
| SUPPOSITORY                                | EACH            | 1                     |
| TABLESPOONFUL                              | MILLILITERS     | 15                    |
| TABLET                                     | EACH            | 1                     |
| TABLET-CAPSULES                            | EACH            | 1                     |
| TEASPOONFUL                                | MILLILITERS     | 5                     |
| THOUSAND UNITS                             | MILLION UNITS   | 0.001                 |
|                                            | UNITS           | 1,000                 |
| UNITS                                      | MICROUNITS      | 1,000,000             |
|                                            | THOUSAND UNITS  | 0.001                 |
|                                            | MILLION UNITS   | 0.000001              |
| VAGINAL INSERT                             | EACH            | 1                     |
| VAGINAL RING                               | EACH            | 1                     |
| VIALS                                      | EACH            | 1                     |
| WAFERS                                     | EACH            | 1                     |

# Appendix E – Inpatient Order Frequency Logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/095.png)

# Appendix F – Outpatient Order Frequency Logic for One-Time, On Call, and DOW Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/096.png)

# Appendix G – Outpatient Order Frequency Logic for Continuous and PRN Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dosing-order-check-version-2-1-user-manual-updated-p-1-262/097.png)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Additive</strong></td>
<td>A drug that is added to an IV Solution for the purpose of parental administration. An additive can be an electrolyte, a vitamin or other nutrient, or antibiotic.</td>
</tr>
<tr class="even">
<td><strong>Administration Schedule File</strong></td>
<td>The ADMINISTRATION SCHEDULE file (#51.1) contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule (e.g., QID, Q4H, and PRN). The administration time is entered in military time.</td>
</tr>
<tr class="odd">
<td><strong>Admixture</strong></td>
<td>An admixture is a type of intravenously administered medication comprised of any number of additives (including zero) in one solution. It is given at a specified flow rate; when one bottle or bag is empty, another is hung.</td>
</tr>
<tr class="even">
<td><strong>BSA</strong></td>
<td>Acronym for Body Surface Area</td>
</tr>
<tr class="odd">
<td><strong>Body Surface Area</strong></td>
<td>A measured or calculated surface of a human body.</td>
</tr>
<tr class="even">
<td><strong>Chemotherapy</strong></td>
<td>Chemotherapy is the treatment or prevention of cancer with chemical agents. The chemotherapy IV type administration can be a syringe, admixture or a piggyback. Once the subtype (syringe piggyback etc.) is selected, the order entry follows the same procedure as the type that corresponds to the selected subtype (e.g., piggyback type of chemotherapy follows the same entry procedure as regular piggyback</td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy Admixture</strong></td>
<td>The Chemotherapy “Admixture” IV type follows the same order entry procedure as the regular admixture IV type. This type is in use when the level of toxicity of the chemotherapy drug is high and is to be administered continuously over an extended period of time (e.g., seven days).</td>
</tr>
<tr class="even">
<td><strong>Chemotherapy Piggyback</strong></td>
<td>The Chemotherapy “Piggyback” IV type follows the same order entry procedure as the regular piggyback IV type. This type of chemotherapy is in use when the chemotherapy drug does not have time constraints on how fast it must be infused into the patient. These types are normally administered over a 30 - 60 minute interval.</td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy Syringe</strong></td>
<td>The Chemotherapy “Syringe” IV type follows the same order entry procedure as the regular syringe IV type. Its administration may be continuous or intermittent. The pharmacist selects this type when the level of toxicity of the chemotherapy drug is low and needs to be infused directly into the patient within a short time interval (usually 1-2 minutes).</td>
</tr>
<tr class="even">
<td><strong>Complex Order (Inpatient)</strong></td>
<td><p>An order that is created from CPRS using the Complex Order dialog and consists of one or more associated Inpatient Medication orders, known as “child” orders.</p>
<p>Inpatient Medications receives the parent order number from CPRS and links the child orders together. If an action of FN (Finish), VF (Verify), DC (Discontinue), or RN (Renew) is taken on one child order, the action must be taken on all of the associated child orders. For example:</p>
<ul>
<li><p>If one child order within a Complex Order is made active, all child orders in the Complex Order must be made active.</p></li>
<li><p>If one child order within a Complex Order is discontinued, all child orders in the Complex Order must be discontinued.</p></li>
<li><p>If one child order within a Complex Order is renewed, all child orders in the Complex Order must be renewed.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="Page_166" class="anchor"></span><strong>Complex Order (Outpatient)</strong></td>
<td>An order that is created from CPRS using the Complex Order dialog and consists of one or more dosing sequences.</td>
</tr>
<tr class="even">
<td><strong>Continuous IV order</strong></td>
<td>Inpatient Medications IV order not having an administration schedule. This includes the following IV types: Hyperal, Admixture, Non-Intermittent Syringe, and Non-Intermittent Syringe or Admixture Chemotherapy.</td>
</tr>
<tr class="odd">
<td><strong>Continuous Syringe</strong></td>
<td>A syringe type of IV that is administered continuously to the patient, similar to a hyperal IV type. This type of syringe is commonly used on outpatients and administered automatically by an infusion pump.</td>
</tr>
<tr class="even">
<td><strong>CPRS</strong></td>
<td>A VistA computer software package called Computerized Patient Record System. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application. All pending orders that appear in the Unit Dose and IV modules are initially entered through the CPRS package.</td>
</tr>
<tr class="odd">
<td><strong>Daily Dose Range</strong></td>
<td>A recommended dosage range for a patient based on age, dose type and dose route.</td>
</tr>
<tr class="even">
<td><strong>Daily Dose Range Order Check</strong></td>
<td>Dose Range Check provides healthcare professionals with general dosing and route-specific dosing range information for patients. Dosing is provided in Dose Units (for example: mg/day, mg/kg/day) as well as dosage form units (for example: each, milliliter, inhalations) for various dose types. With a specific patient age, the user can monitor the appropriateness of drug dosing. That is, users can verify that the SIG they want to use falls within the usual dosage range for a selected dose type, route and age group. The Dose Range Check information is not intended to recommend a specific dose; however, it can recommend a dosage range.</td>
</tr>
<tr class="odd">
<td><strong>DEA Special Handling</strong></td>
<td>The Drug Enforcement Agency special Handling code used for drugs to designate if they are over-the counter, narcotics, bulk compounds, supply items, etc.</td>
</tr>
<tr class="even">
<td><strong>Dispense Drug</strong></td>
<td>The Dispense Drug name has the strength attached to it (e.g., Acetaminophen 325 mg). The name alone without a strength attached is the Orderable Item name.</td>
</tr>
<tr class="odd">
<td><strong>Dosage Form</strong></td>
<td>Refers to the physical presentation of a drug. Dosage Form includes aerosol, capsule, cream, and so on.</td>
</tr>
<tr class="even">
<td><strong>Dosage Form File</strong></td>
<td>The DOSAGE FORM file (#50.606) contains all dosage forms and associated data that are used by Pharmacy packages and CPRS. The dosage form is used in SIG construction, default values and in the determination of the type of each dosage created for each application.</td>
</tr>
<tr class="odd">
<td><strong>Dosage Ordered</strong></td>
<td>Provides the single dose amount and Dose Unit for a drug within a medication order.</td>
</tr>
<tr class="even">
<td><strong>Dose Rate Unit</strong></td>
<td>The unit of measure for rate of the dose (HOUR, HR, H, MINUTE, MIN, DAY).</td>
</tr>
<tr class="odd">
<td><strong>Dose Route</strong></td>
<td>A term which represents the method of administering the drug.</td>
</tr>
<tr class="even">
<td><strong>Dose Type</strong></td>
<td>A term which identifies the purpose for which the dose is given (for example, loading dose, maintenance dose).</td>
</tr>
<tr class="odd">
<td><strong>Dose Unit</strong></td>
<td>A unit of measure commonly reported in the medical literature and reference sources, such as ‘MG’, ‘TABLET.</td>
</tr>
<tr class="even">
<td><span id="Page_167" class="anchor"></span><strong>Dose Units File</strong></td>
<td>The DOSE UNITS file (#51.24) was created to accomplish the mapping to First Databank (FDB). All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by Standards and Terminology Services (SRS), no local editing will be allowed. When Populating the Dose Unit field for a Local Possible Dosage, selection will be from this new file.</td>
</tr>
<tr class="odd">
<td><strong>Dose Unit Conversion File</strong></td>
<td>The DOSE UNIT CONVERSION file (#51.25) was created to convert one dose unit to another using a conversion factor so that a comparison can be made between two dose units when they are not equivalent. The dose unit used for the Dosing Order Check may not be the same dose unit First Databank (FDB) returns with the Dosing Order Check results.</td>
</tr>
<tr class="even">
<td><strong>Dosing Order Checks</strong></td>
<td>General term that refers to the Maximum Single Dose Order Check and Daily Dose Range Order Check.</td>
</tr>
<tr class="odd">
<td><strong>Drug File</strong></td>
<td>The DRUG file (#50) holds the information related to each drug that can be used to fill a prescription or medication order. It is pointed to from several other files and should be handled carefully, usually only by special individuals in the Pharmacy Service. Entries are not typically deleted, but rather made inactive by entering an inactive date.</td>
</tr>
<tr class="even">
<td><strong>Drug Level Error</strong></td>
<td>An error that prevents the mapping of a drug from the VistA database to the FDB MedKnowledge Framework database. The GCNSEQNO is used to map between the VA PRODUCT file (#50.68) to a drug in the FDB MedKnowledge Framework database. Example: A dispense drug in the local DRUG file (#50) that is being ordered is not matched to a VA Product in the VA PRODUCT file (#50.68). Therefore, a GCNSEQNO cannot be obtained.</td>
</tr>
<tr class="odd">
<td><strong>Dubois formula</strong></td>
<td><p>Calculation to measure the Body Surface Area in m<sup>2</sup>. It is</p>
<p>BSA (m²) = 0.20247 x Height(m)<sup>0.725</sup> x Weight(kg)<sup>0.425</sup></p></td>
</tr>
<tr class="even">
<td><strong>Duration</strong></td>
<td>A specific length of time. For Dosing Order Checks, the duration is set to 1 day.</td>
</tr>
<tr class="odd">
<td><strong>Duration Rate Unit</strong></td>
<td>The unit of measure for rate of the length of therapy (HOUR, HR, H, MINUTE, MIN, DAY)</td>
</tr>
<tr class="even">
<td><span id="Enhanced_Order" class="anchor"></span><strong>Enhanced Order Checks</strong></td>
<td>Drug – Drug Interaction, Duplicate Therapy, Dosing, and Pharmacogenomic order checks that are executed utilizing FDB’s MedKnowledge Framework APIs and database.</td>
</tr>
<tr class="odd">
<td><strong>FDB</strong></td>
<td>Acronym for First Databank.</td>
</tr>
<tr class="even">
<td><strong>Free Text Dosage</strong></td>
<td>Any combination of text, numbers, or special characters entered in no particular format in the DOSAGE ORDERED field for a medication order.</td>
</tr>
<tr class="odd">
<td><strong>Free Text Infusion Rate</strong></td>
<td>Any combination of text, numbers, or special characters entered in no particular format in the INFUSION RATE field for a continuous IV fluid order.</td>
</tr>
<tr class="even">
<td><strong>Frequency</strong></td>
<td>The number of administrations per day of a drug.</td>
</tr>
<tr class="odd">
<td><strong>Finish</strong></td>
<td>Term used for completing orders from Order Entry/Results Reporting V. 3.0.</td>
</tr>
<tr class="even">
<td><strong>GCNSEQNO</strong></td>
<td>A numeric value that represents a generic formulation. It is specific to the generic ingredient(s), route of administration, dosage form, and strength. The Formulation ID (GCN), in some cases, may have the same value for different dosage forms, strengths, or non-active ingredient list differences and therefore may be linked to more than one GCNSENO. But a GCNSEQNO is unique in its association with each combination of factors.</td>
</tr>
<tr class="odd">
<td><span id="Gene" class="anchor"></span><strong>Gene</strong></td>
<td>A gene is a section of an individual’s DNA that provides instructions for making proteins, including those that affect how the body processes medications.</td>
</tr>
<tr class="even">
<td><span id="Genotype" class="anchor"></span><strong>Genotype</strong></td>
<td>A genotype is a combination of alleles (version of a gene) which can influence how an individual processes medications.</td>
</tr>
<tr class="odd">
<td><strong>Infusion Rate</strong></td>
<td>The designated rate of flow of IV fluids into the patient.</td>
</tr>
<tr class="even">
<td><strong>Intermittent Syringe</strong></td>
<td>A syringe type of IV that is administered periodically to the patient according to an administration schedule.</td>
</tr>
<tr class="odd">
<td><span id="Page_168" class="anchor"></span><strong>IV Additives File</strong></td>
<td>The IV ADDITIVES file (#52.6) contains drugs that are used as additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.</td>
</tr>
<tr class="even">
<td><strong>IV Solutions File</strong></td>
<td>The IV SOLUTIONS file (#52.7) contains drugs that are used as primary solutions in the IV room. The solution must already exist in the Drug file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.</td>
</tr>
<tr class="odd">
<td><strong>Local Possible Dosages</strong></td>
<td>Local Possible Dosages are free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.</td>
</tr>
<tr class="even">
<td><strong>Maximum Single Dose (MSD)</strong></td>
<td>Maximum amount to be administered in a single dose</td>
</tr>
<tr class="odd">
<td><strong>Maximum Single Dose Order Check</strong></td>
<td>A safeguard incorporated in software when a new medication order is entered or acted upon to ensure that the single dose ordered for a patient does not exceed a recommended upper limit for a drug.</td>
</tr>
<tr class="even">
<td><strong>Maximum Daily Dose (MDD)</strong></td>
<td>Maximum amount to be administered in a 24 hour period.</td>
</tr>
<tr class="odd">
<td><strong>Max Daily Dose Order Check</strong></td>
<td>A safeguard incorporated in software when a new medication order is entered or acted upon to ensure that the daily dose ordered for a patient does not exceed a recommended upper limit for a drug.</td>
</tr>
<tr class="even">
<td><strong>Medication Instruction File</strong></td>
<td>The MEDICATION INSTRUCTION file (#51) is used by Outpatient Pharmacy and Unit Dose Special Instructions. (Not used by IV Other Print Info.) It contains the medication instruction name, expansion, and intended use.</td>
</tr>
<tr class="odd">
<td><strong>Medication Routes File</strong></td>
<td>The MEDICATION ROUTES file (#51.2) contains medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.</td>
</tr>
<tr class="even">
<td><strong>MedKnowledge Framework</strong></td>
<td>MedKnowledge Framework (Formerly Drug Information Framework [DIF])</td>
</tr>
<tr class="odd">
<td><strong>MOCHA</strong></td>
<td>Acronym for Medication Order Check Healthcare Application.</td>
</tr>
<tr class="even">
<td><strong>NDF</strong></td>
<td>Acronym for National Drug File</td>
</tr>
<tr class="odd">
<td><strong>National Drug File</strong></td>
<td>The National Drug File provides standardization of the local drug files in all VA medical facilities. Standardization includes the adoption of new drug nomenclature and drug classification and links the local drug file entries to data in the National Drug File. For drugs approved by the Food and Drug Administration (FDA), VA medical facilities have access to information concerning dosage form, strength and unit; package size and type; manufacturer’s trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among medical facilities.</td>
</tr>
<tr class="even">
<td><strong>Non-VA Meds</strong></td>
<td>Term that encompasses any Over-the-Counter (OTC) medications, Herbal supplements, Veterans Health Administration (VHA) prescribed medications but purchased by the patient at an outside pharmacy, and medications prescribed by providers outside VHA. All Non-VA Meds should be documented in patients’ medical records.</td>
</tr>
<tr class="odd">
<td><strong>Numeric Dose</strong></td>
<td>A single dose amount entered as a numeric value. The Numeric Dose with the Dose Unit make up the dosage ordered for a medication order.</td>
</tr>
<tr class="even">
<td><strong>Order Level Error</strong></td>
<td>An error that is returned from the FDB MedKnowledge Framework API or order information cannot be sent to the interface because of missing data. Example: Information is passed from VistA to FDB database, but the Dosing Order Check cannot be performed, because no FDB dosing information is available for the drug.</td>
</tr>
<tr class="odd">
<td><strong>Orderable Item</strong></td>
<td>An Orderable Item name has no strength attached to it (e.g., Acetaminophen). The name with a strength attached to it is the Dispense drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="even">
<td><span id="Page_169" class="anchor"></span><strong>Orderable Item File</strong></td>
<td>The ORDERABLE ITEM file (#101.43) is a CPRS file that provides the Orderable Items for selection within all Pharmacy packages. Pharmacy Orderable Items are a subset of this file.</td>
</tr>
<tr class="odd">
<td><strong>Order Check</strong></td>
<td>Order checks (Drug-Allergy/ADR interactions, Drug-Drug, Duplicate Drug, Duplicate Therapy, and Dosing) are performed when a new medication order is placed through either the CPRS or Inpatient Medications applications. They are also performed when medication orders are renewed, when Orderable Items are edited, or during the finishing process in Inpatient Medications. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error.</td>
</tr>
<tr class="even">
<td><strong>Order Sets</strong></td>
<td>An Order Set is a set of N prewritten orders. (N indicates the number of orders in an Order Set is variable.) Order Sets are used to expedite order entry for drugs that are dispensed to all patients in certain medical practices and procedures.</td>
</tr>
<tr class="odd">
<td><strong>Pending Order</strong></td>
<td>A pending order is one that has been entered by a provider through CPRS without Pharmacy finishing the order. Once Pharmacy has finished the order, it will become active.</td>
</tr>
<tr class="even">
<td><strong>Pharmacist Intervention</strong></td>
<td>A recommendation provided by a pharmacist through the system’s Intervention process acknowledging the existence of a critical drug-drug interaction, allergy/ADR interaction, dosing, high pharmacogenomic order checks and providing justification for its existence. There are two ways an intervention can be created, either via the Intervention Menu, or in response to Order Checks.</td>
</tr>
<tr class="odd">
<td><span id="Pharamacogenomics" class="anchor"></span><strong>Pharmacogenomics (PGx)</strong></td>
<td>Pharmacogenomics (PGx) is the application of genetic information to predict how a person will respond to medications. It uses genetic data to guide drug selection and dosing, helping ensure treatments are both safe and effective.</td>
</tr>
<tr class="even">
<td><strong>Pharmacy Orderable Item File</strong></td>
<td>The PHARMACY ORDERABLE ITEM file (#50.7) contains the Order Entry name for items that can be ordered in the Inpatient Medications and Outpatient Pharmacy packages.</td>
</tr>
<tr class="odd">
<td><span id="Phenotype" class="anchor"></span><strong>Phenotype</strong></td>
<td>A phenotype is the observable result of an individual’s genes; in pharmacogenomics, it refers to how the body responds to a drug, like whether you break it down quickly, slowly, or not at all.</td>
</tr>
<tr class="even">
<td><strong>Piggyback</strong></td>
<td>Small volume parenteral solution for intermittent infusion. A piggyback is comprised of any number of additives, including zero, and one solution the mixture is made in a small bag. The piggyback is given on a schedule (e.g., Q6H). Once the medication flows in, the piggyback is removed; another is not hung until the administration schedule calls for it.</td>
</tr>
<tr class="odd">
<td><strong>Possible Dosages</strong></td>
<td>Dosages that have a numeric dosage and numeric Dispense Units Per Dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to National Drug File. The National Drug File entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.</td>
</tr>
<tr class="even">
<td><strong>PreMix</strong></td>
<td>An IV Solution that is manufactured or compounded that contains additives.</td>
</tr>
<tr class="odd">
<td><strong>Prescription</strong></td>
<td>This term is now referred to throughout the software as medication orders.</td>
</tr>
<tr class="even">
<td><strong>Print Name</strong></td>
<td>Drug generic name as it is to appear on pertinent IV output, such as labels and reports. Volume or Strength is not part of the print name.</td>
</tr>
<tr class="odd">
<td><strong>Prospective Drug</strong></td>
<td>Drug being ordered or entered.</td>
</tr>
<tr class="even">
<td><strong>Route</strong></td>
<td>Refers to the route of administration, which is the site or method by which a drug is administered.</td>
</tr>
<tr class="odd">
<td><strong>Schedule</strong></td>
<td>The frequency of administration of a medication (e.g., QID, QDAILY, QAM, STAT, Q4H).</td>
</tr>
<tr class="even">
<td><strong>Schedule Type</strong></td>
<td>Codes include: O - one time (i.e., STAT - only once), P - PRN (as needed; no set administration times, C- continuous (given continuously for the life of the order; usually with set administration times, R - fill on request (used for items that are not automatically put in the cart - but are filled on the nurse’s request. These can be multidose items (e.g., eye wash, kept for use by one patient and is filled on request when the supply is exhausted), and OC - on call (one time with no specific time to be given, e.g., 1/2 hour before surgery).</td>
</tr>
<tr class="odd">
<td><strong>Sig</strong></td>
<td>The instructions printed on the label.</td>
</tr>
<tr class="even">
<td><strong>Single Dose Amount</strong></td>
<td>The numeric value of the dosage ordered for a medication order. For an IV order, this value can be represented by the IV Additive strength, numeric value of an IV Solution (PreMix) volume or IV order infusion rate or derived using a formula.</td>
</tr>
<tr class="odd">
<td><strong>Standard Medication Route File</strong></td>
<td>The STANDARD MEDICATION ROUTES file (#51.23) was created to map Local Medication Routes in VistA to an FDB Route in order to perform Dosing Order Checks. This file has been standardized by Standards and Terminology Service (STS) and is mapped to an FDB Route. It cannot be edited locally.</td>
</tr>
<tr class="even">
<td><strong>Start Date/Time</strong></td>
<td>The date and time an order is to begin.</td>
</tr>
<tr class="odd">
<td><strong>Stop Date/Time</strong></td>
<td>The date and time an order is to expire.</td>
</tr>
<tr class="even">
<td><strong>Strength</strong></td>
<td>The potency of a drug usually expressed in a metric quantity consisting of a value and unit, such as 500MG. Strength is usually a whole number.</td>
</tr>
<tr class="odd">
<td><strong>Syringe</strong></td>
<td>Type of IV that uses a syringe rather than a bottle or bag. The method of infusion for a syringe type IV may be continuous or intermittent.</td>
</tr>
<tr class="even">
<td><strong>System Level Error</strong></td>
<td>If this error occurs, no order checks can be performed. Example: Communication link to FDB database is down.</td>
</tr>
<tr class="odd">
<td><strong>VA Drug Class Code</strong></td>
<td>A drug classification system used by VA that separates drugs into different categories based upon their characteristics. Some cost reports can be run for VA Drug Class Codes.</td>
</tr>
<tr class="even">
<td><strong>VA Product File</strong></td>
<td>The VA PRODUCT file (#50.68).</td>
</tr>
<tr class="odd">
<td><strong>VistA</strong></td>
<td>Acronym for Veterans Health Information Systems and Technology Architecture, the new name for Decentralized Hospital Computer Program (DHCP).</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
A
Adjusting Single Dose Amount - IV, 176
C
C
Complex Order - Outpatient, 84
Complex Order – Unit Dose, 133
Copy Order - Outpatient, 94
CPRS, 216
D
D
Data required for dosage check, 11
Display Sequence of Order Checks, 8
Dosage Ordered, 15
Drug, 12
Drug Level Errors, 187
Duration, 76
Duration Rate, 76
E
E
Edit Order - IV, 169
Edit Order - Outpatient, 90
Edit Order - Unit Dose, 140
Error Handling, 186
Errors - Drug Level, 187
Errors - Order Level, 190
Errors - System Level, 186
Orders Excluded from Dosing Checks, 7
F
F
Finish Order - IV, 165
Finish Order - Outpatient, 88
Finish Order - Unit Dose, 133
Free Text Dose Error - Unit Dose, 145, 146
Frequency, 66
G
G
Glossary, 215
I
I
Inpatient Medications, 127
Introduction, 1
IV Module, 163
New Order - IV, 163
Orders Included for Dosage Checks, 7
O
O
How do Enhanced Order Checks work, 7
Order Entry, 81
Order Level Errors, 190
Outpatient Pharmacy, 81
Order Set, 219
P
P
Patient Parameters, 11
Process Flow, 7
R
R
Renew Order - IV, 172
Renew Order - Outpatient, 93
Renew Order – Unit Dose, 138
Required Data, 11
S
S
Simple Order - Outpatient, 82
Specific Sequence for Order Checks, 8
System Level Errors, 186
T
T
Technician Entered Order - Outpatient, 100
Trigger of Order Checks, 9
U
U
New Order - Unit Dose, 128
New Order Using an Order Set – Unit Dose, 130
V
V
Verification of an Order - Outpatient, 104
<span id="Page_173" class="anchor"></span>
