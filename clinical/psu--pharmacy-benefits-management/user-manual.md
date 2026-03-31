---
consolidated_title: "user manual change pages"
app_code: PSU
doc_type: UM
master_source: "PSU*4*19 User Manual Change Pages"
master_pub_date: July 2014
consolidated_from: 3 versions
prior_versions:
  - "PSU*4*10 User Manual Change Pages"
  - "PSU*4*12 User Manual Change Pages"
---

---
title: Pharmacy Benefits Management (PBM) User Manual
---

![](psu-4-19-user-manual-change-pages/001.png)

> Software Version 4.0

> Revised July 2014

> June 2005

> Department of Veterans Affairs

> Office of Information and Technology (OI&T) Product Development

# Revision History 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [MailMan Messages](#mailman-messages)
  - [Example: Subject of MailMan Message](#example-subject-of-mailman-message)
  - [Example MailMan Messages](#example-mailman-messages)
  - [Example MailMan Messages](#example-mailman-messages-1)
  - [Example MailMan Messages](#example-mailman-messages-2)
  - [Example MailMan Messages](#example-mailman-messages-3)
  - [Example MailMan Messages](#example-mailman-messages-4)
  - [Example MailMan Messages](#example-mailman-messages-5)
  - [Example MailMan Messages](#example-mailman-messages-6)
  - [Statistics Format](#statistics-format)
  - [Example MailMan Messages](#example-mailman-messages-7)
  - [Statistics Format](#statistics-format-1)
  - [Example MailMan Messages](#example-mailman-messages-8)
  - [Example MailMan Messages](#example-mailman-messages-9)
  - [Example MailMan Messages](#example-mailman-messages-10)
  - [Example MailMan Messages](#example-mailman-messages-11)
  - [Example MailMan Messages](#example-mailman-messages-12)
> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7/2014</p>
</blockquote></td>
<td><blockquote>
<p>i, 19, 27, 36,</p>
<p>45, 56, 72,</p>
<p>78, 83, 85-</p>
<p>88, 90-92,</p>
<p>95, 101,</p>
<p>106, 111</p>
</blockquote></td>
<td><blockquote>
<p>PSU*4*19</p>
</blockquote></td>
<td><blockquote>
<p>Revised title page.</p>
<p>Updated Inpatient and Outpatient Extracts to include a new Code Set Indicator field in sections 4.8.1 and 4.9.1, and include ICD10 in Data Element field name.</p>
<p>Updated MailMan Message examples to reflect the addition of Code Set Indicators.</p>
<p>Changed all instances of “double up arrow (^^)” to “up arrow (^)” within MailMan message descriptions.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1/2008</p>
</blockquote></td>
<td><blockquote>
<p>6-9</p>
</blockquote></td>
<td><blockquote>
<p>PSU*4*12</p>
</blockquote></td>
<td><blockquote>
<p>Move a Note from section 3.5 to section 3.2 and 3.3 to correspond with a change in patch PSU*4*12 that moves the trigger of the Patient demographic purge from the Retransmit Patient Demographic Data option to the PSU PSM Manual option and to the PSU PBM Auto option.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/2006</p>
</blockquote></td>
<td><blockquote>
<p>100-102</p>
</blockquote></td>
<td><blockquote>
<p>PSU*4*10</p>
</blockquote></td>
<td><blockquote>
<p>Updated Allergies/Adverse Events Information Statistics chart in section 4.11.1 Statistics Format and updated the example of the MailMan messages in section 4.11.2 Example MailMan Messages for patch PSU*4*10.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02/2006</p>
</blockquote></td>
<td><blockquote>
<p>iv, 115-132</p>
</blockquote></td>
<td><blockquote>
<p>PSU*4*3</p>
</blockquote></td>
<td><blockquote>
<p>PBM Extract Enhancements #3 project. Added Section 5. to Table of Contents. Added Section 5. HL7 Messages and 5.1. Data Specifications. Updated Glossary to include definitions of HL7 and HLO, and for page numbering purposes. Updated Index to include items from new section on HL7 Messages, and for page numbering purposes.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/2005</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Original Release of PBM V. 4.0 User Manual <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>
> *(This page included for two-sided copying.)*
ii Pharmacy Benefits Management V. 4.0 June 2005

# MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how the data is extracted and formatted into the MailMan messages. The MailMan messages are sent in an up-arrow (^) delimited format. Messages begin and end a dispensing record with a single up-arrow (^). When the package is extracting the data, a check is done on each free text field to see if an up-arrow is part of the text. If an up-arrow is discovered in the text, it will be converted to an apostrophe (').

> The subject of each message is composed for easier data manipulation and will look like the following:

## Example: Subject of MailMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- V. 4.0 Indicates that this data is from PBM V. 4.0.
- PBM PBM represents Pharmacy Benefits Management. The next two letters attached represent the package from which the data was extracted.
  - IV – Pharmacy Patient IV Module
  - UD – Pharmacy Patient Unit Dose Module
  - AR – Automatic Replenishment/Ward Stock Module
  - OP – Prescription Module
  - PR – Procurement Module
  - CS – Controlled Substances Module
  - PD – Patient Demographics Module
  - OV – Outpatient Visits Module
  - PTF – Inpatient PTF Records Module
  - PRO – Provider Information Module
  - AA – Allergies/Adverse Events
  - VI – Vitals/Immunizations Information Module
  - LR – Laboratory Module
- 29810 The date of the reporting period, in this example October 1998.
- 1/3 “1” represents the message number and “3” represents the total number of messages sent from this facility for this particular module. In this example, the header would indicate the first message of a total of 3 messages generated for the IV module.
- 499B4 The station number with suffix (broken down to the outpatient clinic or the inpatient division).
- GLRISC The name of the facility/outpatient clinic/division.

> When the data is being formatted into MailMan messages, additional lines will be added for records exceeding 235 characters. The first character of each additional line will be an asterisk (\*). A record will never be broken within a data piece. If a conversion of MailMan messages is

> being performed on a PC in a language such as FoxPro, ProComm, Keaterm, etc., the asterisk at the beginning of a line will inform the user that this line and the previous line should be concatenated together, thus validating the definitions of the delimited fields explained later in this document.

> A confirmation message will be generated whenever the program extracts data to be transmitted to the PBM section <span class="mark">REDACTED</span> for addition to the national database. Only those packages with requested data to be extracted will be listed. If no data is found for a package, the confirmation will list the module with “0” lines extracted and “1” message transmitted. A MailMan message will be generated if the extract program did not find any data for a specific module.

> Example confirmation messages are provided in the MailMan Messages section of this manual.

> If the *Automatic Pharmacy Statistics* option or *Manual Pharmacy Statistics* option complete successfully, a PBM Timing report is generated. This report displays the start and stop date/time of each extract and a final calculation of how long it took to run. Examples are provided in the MailMan Messages section of this document.

> ![](psu-4-19-user-manual-change-pages/002.png)Note: Extract times will vary depending on the system performance, the time extract is run (early in the morning or on a weekend versus in the middle of the day), and the amount of data extracted.

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format. The following is an example of the first (parent) data record sent for an IV order. Each IV additive and solution within an order will be sent as a separate data record.

> Example: IV – Detail Report Message

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 26%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMIV 30109 1/1 605 JERRY L PETTIS VAMC</p>
</blockquote></th>
<th><blockquote>
<p>[#10684]</p>
</blockquote></th>
<th rowspan="22"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>11/16/04@19:00 7132 lines</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>From: PBMPHARMACIST,FOUR In 'IN' basket. Page 1</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010901^120^P^A^N^000006404^11 ml/hr^000002705^1^RANITIDINE HCL 25MG/ML IN</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>J^GA301^00173-0363-39^^1^0^RANITIDINE (ZANTAC)^A^RANITIDINE HCL 25MG/ML INJ 10M</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>L VI^MG^.0362^150^^6^1002929700V843567^13868^3010901^1^0^0^0^150^0^0^0^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010901^120^^^^000006404^11 ml/hr^000002705^^SODIUM CHLORIDE 0.9% INJ^TN10</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>2^00264-1400-20^^1^0^0.9% NACL^S^SODIUM CHLORIDE 0.9% INJ 250ML^ML^0^250^^6^100</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>2929700V843567^^3010901^^^^^250^0^0^0^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010831^7^P^P^N^000007287^Q24H^000002224^1^CEFTRIAXONE NA 1GM/VIL INJ^AM10</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>3^00004-1964-01^^1^0^CEFTRIAXONE SOD INJ^A^CEFTRIAXONE SOD 1GM INJ VI^GM^19.01^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>2^^6RO^1002931500V483685^11247^3010901^1^0^0^0^2^0^0^0^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010831^7^^^^000007287^Q24H^000002224^^SODIUM CHLORIDE 0.9% INJ^TN102^0033</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>8-0049-18^^1^0^0.9% NACL^S^SODIUM CHLORIDE 0.9% INJ 100ML^ML^0^100^^6^100293150</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>0V483685^^3010901^^^^^100^0^0^0^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010831^124^P^P^Y^000003563^Q48H^000004287^1^GENTAMICIN SO4 40MG/ML INJ^AM</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>300^63323-0010-20^^1^0^GENTAMICIN^A^GENTAMICIN SULFATE 40MG/ML INJ^MG^.0015^70^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^6^1001835792V911934^4081^3010901^1^0^0^0^70^0^0^0^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010831^124^^^^000003563^Q48H^000004287^^SODIUM CHLORIDE 0.9% INJ^TN102^00</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>338-0049-18^^1^0^0.9% NACL^S^SODIUM CHLORIDE 0.9% INJ 100ML^ML^0^100^^6^1001835</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>792V911934^^3010901^^^^^100^0^0^0^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Enter RETURN to continue or '^' to exit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: IV - Statistical Data Message

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 1%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Subj: V. 4.0 PBMIV 30109 605 JERRY L PETTIS VAMC [#7569] 07/16/04@14:39</p>
<p>139 lines</p>
<p>From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>IV Statistical Data for SEP 1,2001 through SEP 30,2001</p>
</blockquote>
<p>Drug Total Number</p>
<p>Drug Name Strength Dispensed of bags</p></th>
<th rowspan="2"></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ACYCLOVIR NA 500MG/VI INJ MG 5600.00 7</p>
<p>ALBUMIN HUMAN 25% USP 50ML VI ML 350.00 4</p>
<p>ALEMTUZUMAB 10MG INJ *# MG 220.00 8</p>
<p>ALPHA 1-PROTEINASE INHIBITOR(HUMAN) *# MG 47319.00 9</p>
<p>ALTEPLASE RECOMBINANT 50MG INJ W/DIL VI MG 252.00 25</p>
<p>AMIKACIN SULFATE 250MG/ML INJ MG 30250.00 35</p>
<p>AMINO ACID III 10% 1000ML ML 258930.00 267</p>
<p>AMINOCAPROIC ACID 250MG/ML INJ 20ML VI MG 84000.00 14</p>
<p>AMIODARONE HCL 50MG/ML, 3ML AMP MG 900.00 2</p>
<p>AMPHOTERICIN B 50MG INJ VI MG 1675.00 35</p>
<p>AMPHOTERICIN B LIPOSOME 50MG INJ *# MG 8100.00 18</p>
<p>AMPICILLIN NA 1GM/VI INJ GM 2704.50 210</p>
<p>AMPICILLIN NA/SULBACTAM NA 1.5GM/VI INJ GM 1105.50 375</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Subj: V. 4.0 PBMIV 30109 605 JERRY L PETTIS VAMC [#7569] Page 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AMPICILLIN NA/SULBACTAM NA 3GM/VI INJ</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>123.00</td>
<td>41</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CALCIUM GLUCONATE 10% INJ 100ML VI</p>
</blockquote></td>
<td><blockquote>
<p>MEQ</p>
</blockquote></td>
<td>2861.00</td>
<td>267</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CALCIUM GLUCONATE 10% INJ 10ML VI</p>
</blockquote></td>
<td><blockquote>
<p>MEQ</p>
</blockquote></td>
<td>144.15</td>
<td>22</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CARBOPLATIN 150MG INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>MG</p>
</blockquote></td>
<td>5250.00</td>
<td>13</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CEFAZOLIN NA 1GM/VI INJ</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>1520.50</td>
<td>1152</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CEFOTAXIME 1GM INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>48.00</td>
<td>24</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CEFOTETAN DISODIUM 1GM INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>208.00</td>
<td>126</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CEFOTETAN DISODIUM 2GM INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>7.00</td>
<td>7</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CEFTAZIDIME 1GM INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>601.00</td>
<td>335</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CEFTRIAXONE SOD 1GM INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>336.00</td>
<td>209</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CEFTRIAXONE SOD 2GM INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>GM</p>
</blockquote></td>
<td>8.00</td>
<td>4</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CIMETIDINE 300MG/2ML INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>MG</p>
</blockquote></td>
<td>26300.00</td>
<td>36</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CIPROFLOXACIN 10MG/ML INJ 40ML VI</p>
</blockquote></td>
<td><blockquote>
<p>MG</p>
</blockquote></td>
<td>52265.00</td>
<td>162</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CLADRIBINE 1MG/ML INJ 10ML</p>
</blockquote></td>
<td><blockquote>
<p>MG</p>
</blockquote></td>
<td>30.00</td>
<td>3</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CLINDAMYCIN PHOS 600MG/4ML INJ AMP</p>
</blockquote></td>
<td><blockquote>
<p>MG</p>
</blockquote></td>
<td>419800.00</td>
<td>533</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CO-TRIMOXAZOLE 10ML INJ (SEPTRA INJ)</p>
</blockquote></td>
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td>21.80</td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CYCLOPHOSPHAMIDE 500MG INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>MG</p>
</blockquote></td>
<td>7400.00</td>
<td>11</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DACARBAZINE 200MG INJ VI</p>
</blockquote></td>
<td><blockquote>
<p>MG</p>
</blockquote></td>
<td>1700.00</td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAKINS SOLN MODIFIED HALF STRENGTH *</p>
</blockquote></td>
<td><blockquote>
<p>ML</p>
</blockquote></td>
<td>1000.00</td>
<td>1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>DESMOPRESSIN ACE 4MCG/ML INJ 1ML AMP</p>
</blockquote></td>
<td><blockquote>
<p>MCG</p>
</blockquote></td>
<td>330.00</td>
<td>2</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 12%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>IV STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient ICN</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>INTEGRATION CONTROL</p>
<p>NUMBER field</p>
</blockquote></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>Free Text.</p>
<p>Example: “1010185893V199552”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(# 991.01)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>If an ICN does not exist, send null.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(Values in both fields are concatenated with a “V”.)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Provider Local IEN</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON file (#200)</p>
</blockquote></td>
<td><blockquote>
<p>Internal Entry Number (IEN)</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Stop Date/Time of</p>
</blockquote></td>
<td><blockquote>
<p>UNIT DOSE</p>
</blockquote></td>
<td><blockquote>
<p>STOP DATE/TIME</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td rowspan="4"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order</p>
</blockquote></td>
<td><blockquote>
<p>multiple (#62) within</p>
</blockquote></td>
<td><blockquote>
<p>sub-field (#34)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>the PHARMACY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PATIENT file (#55)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Dispensed Amount</p>
</blockquote></td>
<td><blockquote>
<p>DISPENSE LOG</p>
<p>multiple (#71) within the UNIT DOSE</p>
<p>multiple (#62) within the PHARMACY PATIENT file (#55)</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT sub-field (#.03)</p>
<p>HOW sub-field (#.05)</p>
</blockquote></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>If the HOW sub-field (#.05) is set to “1” from Pick list, “2” Pre-exchange units, or “3” Extra Units dispensed, the AMOUNT sub-field (#.03) for each dispense drug shall be counted.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>The total dispensed amount shall be transmitted. If there is no amount to be counted for the reporting period, a value of “0” shall be transmitted.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Returned Amount</p>
</blockquote></td>
<td><blockquote>
<p>DISPENSE LOG</p>
<p>multiple (#71) within the UNIT DOSE</p>
<p>multiple (#62) within the PHARMACY PATIENT file (#55)</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT sub-field (#.03)</p>
<p>HOW sub-field (#.05)</p>
</blockquote></td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>If the HOW sub-field (#.05) is set to “4” returns, the AMOUNT sub-field (#.03) for each dispense drug shall be counted.</p>
<p>The total returned amount shall be transmitted. If there is no returned amount to be counted for the reporting period, a value of “0” shall be transmitted.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](psu-4-19-user-manual-change-pages/003.png)Note: Data pieces 2-7 and 21-23 in the table above shall repeat for each unit dose order containing more than one dispense drug. Data pieces 8-20 and 24-25 will hold specific dispense drug information.

> Within the UD extract, the DISPENSE DATE/TIME sub-field (#.01), DISPENSE DRUG sub- field (#.02), AMOUNT sub-field (#.03) and HOW sub-field (#.05) within the DISPENSE LOG multiple (#71) within the UNIT DOSE multiple (#62) in the PHARMACY PATIENT file (#55) shall be used to determine what was dispensed or returned. The Unit Dose record, with the current functionality, is not extracted if there is no dispensing activity (nothing dispensed or returned). This requirement shall not change.

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format. The following is an example of a data record sent. Each dispense drug within an order will be sent as a separate data record (pieces 22-45). Pieces 2-20 will repeat for each unit dose order containing more than one dispense drug.

> Within the AR/WS extract, Medical Center Divisions are selected from the MEDICAL CENTER DIVISION file (#40.8) NAME field (#.01). Outpatient Sites are selected from the OUTPATIENT SITE file (#59) NAME field (#.01). The user may select an active or inactive Outpatient Site. \*\*Inactive\*\* shall be displayed next to a selected inactive Outpatient Site.

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: AR/WS – Detail Report Message

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 26%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMAR 30109 1/1 605 JERRY L PETTIS VAMC</p>
</blockquote></th>
<th><blockquote>
<p>[#7421]</p>
</blockquote></th>
<th rowspan="21"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>07/15/04@16:56 383 lines</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^Unknown VA Product Name^CN103^00839-6001-92^ACETAMINOPHEN 650MG RTL</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>SUPP^^^0^EA^0.317^03 or 04^1^12^^9R^12^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^Unknown VA Product Name^RE400^00087-0572-03^ACETYLCYSTEINE 20% INHL</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>SOLN^^^0^ML^0.264^06 or 07^1^3^^6^3^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^ALBUTEROL 90MCG/SPRAY INHL,ORAL^RE102^59930-1560-01^ALBUTEROL 90MCG</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>200D ORAL INHL^^1^0^EA^1.650^06 or 07^1^99^^6^99^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^ALCOHOL,ISOPROPYL 70% LIQUID,TOP^DE101^00574-0067-16^ALCOHOL ISOPRO</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>PYL 70%^^1^0^ML^0.004^06 or 07^1^88318^^9^88318^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^AMIODARONE HCL (CORDARONE) 200MG TAB^CV300^00008-4188-04^AMIODARONE</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>HCL (CORDARONE) 200MG TAB^^1^0^TAB^1.164^06 or 07^1^15^^6RO^15^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^COMPOUND BENZOIN CONC LIQUID,TOP^DE900^10648-0800-08^BENZOIN TINCTU</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>RE SPRAY 135GM U4070^^0^0^BT^4.500^06 or 07^1^13^^9^13^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^BENZOCAINE 20% SPRAY,TOP^DE700^00283-0679-02^BENZOCAINE 20% TOP SPR</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>AY^^0^0^ML^0.203^06 or 07^60^1683^^6^1683^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^BENZOCAINE 20% GEL^NT300^00283-0871-31^BENZOCAINE 20% TOP GEL^^1^0^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>GM^4.700^06 or 07^1^6^^9^6^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^^30109^BISACODYL 10MG SUPP,RTL^RS300^00597-0052-50^BISACODYL 10MG RTL SUPP</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^^1^0^EA^0.027^03 or 04^1^62^^9^62^^</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: AR/WS - Data Records Not Broken Down To Outpatient Site or Inpatient Division Message

> Example: AR/WS - Statistical Data Message

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 1%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Subj: V. 4.0 PBMAR 30109 605 JERRY L PETTIS VAMC [#7422] 07/15/04@16:56</p>
<p>396 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Automatic Replenishment/Ward Stock Data Summary</p>
<p>SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC</p>
<p>Total Total</p>
<p>Dispensed Dispensed AMIS</p>
<p>DRUG NAME Units Cost Category</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ABSORB GEL COMP SPONGE STERILE SIZE 24.00 334.87 06 or 07</p>
<p>ABSORB GEL SPONGE STERILE SIZE 100 20.00 254.46 06 or 07</p>
<p>ABSORB HEMOSTAT 4IN X 8IN PKT # 18.00 356.63 06 or 07</p>
<p>ACCU-CHEK COMFORT CURVE HI/LO CONTL 36.00 151.92 06 or 07</p>
<p>ACCU-CHEK COMFORT CV(GLUCOSE) TEST 311.00 103.25 06 or 07</p>
<p>ACETAMINOPHEN 325MG TAB U/D 1174.00 15.26 03 or 04</p>
<p>ACETAMINOPHEN 325MG/10.15ML ELIXIR 170.00 23.29 06 or 07</p>
<p>ACETAMINOPHEN 650MG RTL SUPP 12.00 3.80 03 or 04</p>
<p>ACETAMINOPHEN 650MG/25ML ELIXIR U/D 11.00 1.48 03 or 04</p>
<p>ACETIC ACID 2/HC 1% OTIC SOLN 4.00 0.74 06 or 07</p>
<p>ACETYLCYSTEINE 20% INHL SOLN 3.00 0.79 06 or 07</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *\[A portion of this statistical data message has been removed to save space.\]*

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMAR 30109 605 JERRY</p>
</blockquote></th>
<th></th>
<th></th>
<th>PETTIS VAMC</th>
<th><blockquote>
<p>[#7422]</p>
</blockquote></th>
<th><blockquote>
<p>Page</p>
</blockquote></th>
<th>20</th>
<th></th>
<th></th>
<th rowspan="16"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>TROPICAMIDE 1% OPH SOLN</p>
</blockquote></th>
<th rowspan="12"></th>
<th rowspan="12"></th>
<th><blockquote>
<p>310.00</p>
</blockquote></th>
<th>456.94</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
<th rowspan="15"></th>
</tr>
<tr class="header">
<th><blockquote>
<p>TUBERCULIN PPD 5TU/0.1ML 1ML VIAL</p>
</blockquote></th>
<th><blockquote>
<p>27.00</p>
</blockquote></th>
<th>70.20</th>
<th>03</th>
<th>or</th>
<th><blockquote>
<p>04</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>TUBEX INJECTOR, 1 &amp; 2 ML SIZE,PLAST</p>
</blockquote></th>
<th><blockquote>
<p>14.00</p>
</blockquote></th>
<th>28.00</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>VERAPAMIL HCL 120MG TAB U/D</p>
</blockquote></th>
<th><blockquote>
<p>10.00</p>
</blockquote></th>
<th>0.76</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>VERAPAMIL HCL 240MG SR TAB U/D</p>
</blockquote></th>
<th><blockquote>
<p>20.00</p>
</blockquote></th>
<th>5.38</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>VITAMIN E 400 UNT CAP</p>
</blockquote></th>
<th><blockquote>
<p>20.00</p>
</blockquote></th>
<th>0.82</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>WARFARIN (COUMADIN) NA 2MG TAB</p>
</blockquote></th>
<th><blockquote>
<p>16.00</p>
</blockquote></th>
<th>2.01</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>WARFARIN SOD 5MG TAB U/D</p>
</blockquote></th>
<th><blockquote>
<p>6.00</p>
</blockquote></th>
<th>0.02</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>WATER STERILE FOR INJ USP 10ML VI</p>
</blockquote></th>
<th><blockquote>
<p>10.00</p>
</blockquote></th>
<th>1.76</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>X-PREP LIQUID 74ML #</p>
</blockquote></th>
<th><blockquote>
<p>20.00</p>
</blockquote></th>
<th>106.00</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ZZDIVALPROEX SODIUM 250MG EC TAB U/</p>
</blockquote></th>
<th><blockquote>
<p>26.00</p>
</blockquote></th>
<th>8.84</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ZZPSYLLIUM SF ORAL PWD</p>
</blockquote></th>
<th><blockquote>
<p>62.00</p>
</blockquote></th>
<th>2.29</th>
<th>06</th>
<th>or</th>
<th><blockquote>
<p>07</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>TOTALS</p>
</blockquote></th>
<th rowspan="3"></th>
<th rowspan="3"></th>
<th><blockquote>
<p>358359.0</p>
</blockquote></th>
<th>233776.1</th>
<th rowspan="3"></th>
<th rowspan="3"></th>
<th rowspan="3"></th>
</tr>
<tr class="header">
<th><blockquote>
<p>* Non-Formulary</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p># Not on National Formulary</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>PRESCRIPTION STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Duration</p>
</blockquote></td>
<td><blockquote>
<p>PRESCRIPTION file (#52)</p>
<p>MEDICATION INSTRUCTION</p>
<p>multiple (#113)</p>
</blockquote></td>
<td><blockquote>
<p>DURATION field (#4)</p>
</blockquote></td>
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>Duration can be entered in minutes, hours, days, weeks, or months. The internal format of the data shall be extracted, e.g. “14D or 14” represents 14 days, “1W” represents 1 week. If no duration exists a null value shall be transmitted.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Conjunction</p>
</blockquote></td>
<td><blockquote>
<p>PRESCRIPTION file (#52)</p>
<p>MEDICATION INSTRUCTION</p>
<p>multiple (#113)</p>
</blockquote></td>
<td><blockquote>
<p>CONJUNCTION</p>
<p>field (#5)</p>
</blockquote></td>
<td><blockquote>
<p>43</p>
</blockquote></td>
<td><blockquote>
<p>The internal format of the data shall be extracted.</p>
<p>Example: “A” for And, “T” for Then, and “X” for Except.</p>
<p>If no conjunction exists, a null value shall be transmitted.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Route</p>
</blockquote></td>
<td><blockquote>
<p>MEDICATION ROUTES</p>
<p>file (#51.2)</p>
</blockquote></td>
<td><blockquote>
<p>NAME field (#.01)</p>
</blockquote></td>
<td><blockquote>
<p>44</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Schedule</p>
</blockquote></td>
<td><blockquote>
<p>PRESCRIPTION file (#52)</p>
<p>MEDICATION INSTRUCTION</p>
<p>multiple (#113)</p>
</blockquote></td>
<td><blockquote>
<p>SCHEDULE field (#7)</p>
</blockquote></td>
<td><blockquote>
<p>45</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Verb</p>
</blockquote></td>
<td><blockquote>
<p>PRESCRIPTION file (#52)</p>
<p>MEDICATION INSTRUCTION</p>
<p>multiple (#113)</p>
</blockquote></td>
<td><blockquote>
<p>VERB field (#8)</p>
</blockquote></td>
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>If no verb is found, a null value will be transmitted.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](psu-4-19-user-manual-change-pages/004.png)Note: Pieces 38-46 can repeat for a complex outpatient medication order (\>1 dosing sequence). When a prescription is extracted that has more than one dosing sequence, the prescription record with the first dosing sequence shall be transmitted in the PBMOP MailMan message. The prescription record with ALL dosing sequences will be transmitted in the new PBMOP(MULTIDOSE) MailMan message. In this MailMan message pieces 38-46 will repeat for each additional dosing sequence.

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format. The following is an example of the first (parent) data record sent for a Prescription order. Each IV additive and solution within an order will be sent as a separate data record.

> Example: Prescription – Detail Report Message

> 56 Pharmacy Benefits Management V. 4.0 July 2014

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>PROCUREMENT STATISTICS DATA FIELD SPECIFICATIONS (DRUG ACCOUNTABILITY FILE #58.81)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Dispense Unit</p>
</blockquote></td>
<td><blockquote>
<p>DRUG file (#50)</p>
</blockquote></td>
<td><blockquote>
<p>DISPENSE UNIT</p>
<p>field (#14.5)</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order Unit</p>
</blockquote></td>
<td><blockquote>
<p>ORDER UNIT file (#51.5)</p>
</blockquote></td>
<td><blockquote>
<p>ABBREVIATION</p>
<p>field (#.01)</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NO DATA</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NO DATA</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Disp Unit Per Order Unit</p>
</blockquote></td>
<td><blockquote>
<p>DRUG file (# 50)</p>
</blockquote></td>
<td><blockquote>
<p>DISPENSE UNITS PER ORDER UNIT</p>
<p>field (#15)</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Qty Invoiced</p>
</blockquote></td>
<td><blockquote>
<p>DRUG ACCOUNTABILITY TRANSACTION file (#58.81)</p>
</blockquote></td>
<td><blockquote>
<p>QUANTITY field (#5)</p>
</blockquote></td>
<td><blockquote>
<p>17</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Price Per Order Unit</p>
</blockquote></td>
<td><blockquote>
<p>DRUG file (#50)</p>
</blockquote></td>
<td><blockquote>
<p>PRICE PER</p>
<p>ORDER UNIT field (#13)</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Total Cost</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>Formula = Qty Invoice/ Disp Units Per Order Unit * Price Per Order Unit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Manufacturer</p>
</blockquote></td>
<td><blockquote>
<p>DRUG ACCOUNTABILITY TRANSACTION file (#58.81)</p>
</blockquote></td>
<td><blockquote>
<p>MANUFACTURER</p>
<p>field (#12)</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Invoice Number</p>
</blockquote></td>
<td><blockquote>
<p>DRUG ACCOUNTABILITY TRANSACTION file (#58.81)</p>
</blockquote></td>
<td><blockquote>
<p>PRIME VENDOR</p>
<p>INVOICE field (#71)</p>
</blockquote></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NO DATA</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Within the Procurement extract, procurement data is extracted from the IFCAP file (#442), the DRUG ACCOUNTABILITY file (#58.81), and the DRUG ACCOUNTABILITY ORDER

> (Prime Vendor) file (#58.811). How much or how little data is extracted is dependent on what is implemented at the facility.

> Procurement data from the IFCAP file (#442) is limited to transactions with a cost center of 822400 (Pharmacy) and 828100 (SPD). Only completed prime vendor invoice data from the DRUG ACCOUNTABILITY ORDER (Prime Vendor) file (#58.811) will be extracted.

> Procurement data with dispensing transaction type of “1” (Receipt into Pharmacy) will be extracted from the DRUG ACCOUNTABILITY file (#58.81).

> Medical Center Divisions are selected from the MEDICAL CENTER DIVISION file (#40.8) NAME field (#.01). Outpatient Sites are selected from the OUTPATIENT SITE file (#59) NAME field (#.01). The user may select an active or inactive Outpatient Site. \*\*Inactive\*\* shall be displayed next to a selected inactive Outpatient Site.

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown below.

> Example: Procurement – Detail Report Message

> 72 Pharmacy Benefits Management V. 4.0 July 2014

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>CONTROLLED SUBSTANCES STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient ICN</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>INTEGRATION CONTROL NUMBER</p>
<p>field</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>Free Text. Example:</p>
<p>“1010185893V199552”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(# 991.01)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>If an ICN does not exist, send null.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>(Values in both fields are concatenated with a ‘V’.)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Within the CS extract, Medical Center Divisions are selected from the MEDICAL CENTER DIVISION file (#40.8) NAME field (#.01). Outpatient Sites are selected from the OUTPATIENT SITE file (#59) NAME field (#.01). The user may select an active or inactive Outpatient Site. \*\*Inactive\*\* shall be displayed next to a selected inactive Outpatient Site.

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: Controlled Substances – Detail Report Message

> 78 Pharmacy Benefits Management V. 4.0 July 2014 User Manual

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 12%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>PATIENT DEMOGRAPHICS STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Ethnicity</p>
</blockquote></td>
<td><blockquote>
<p>ETHNICITY</p>
</blockquote></td>
<td><blockquote>
<p>ETHNICITY</p>
</blockquote></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td rowspan="5"></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>INFORMATION</p>
</blockquote></td>
<td><blockquote>
<p>INFORMATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>multiple (#6) within</p>
</blockquote></td>
<td><blockquote>
<p>field (#.01)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>the PATIENT file</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>(#2)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Race (new)</p>
</blockquote></td>
<td><blockquote>
<p>RACE</p>
</blockquote></td>
<td><blockquote>
<p>RACE</p>
</blockquote></td>
<td><blockquote>
<p>20-29</p>
</blockquote></td>
<td rowspan="5"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>INFORMATION</p>
</blockquote></td>
<td><blockquote>
<p>INFORMATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>multiple (#2) within</p>
</blockquote></td>
<td><blockquote>
<p>field (#.01)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>the PATIENT file</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>(#2)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: Patient Demographics – Detail Report Message

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 25%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMPD 30109 1/20 605 JERRY L PETTIS VAMC</p>
</blockquote></th>
<th><blockquote>
<p>[#7732]</p>
</blockquote></th>
<th rowspan="21"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>07/20/04@18:22 10000 lines</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3040720^^2210000^83^^M^NSC^REQUIRED^^000003689^^^^^2870723^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3040720^^2521229^51^^M^NSC^MT COPAY EXEMPT^5^000002816^1002935271^00000611</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>8^1880^^2980322^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3040720^^2190822^84^WHITE, NOT OF HISPANIC ORIGIN^F^SERVICE CONNECTED 50%</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>to 100%^^1^000006505^1002191464^000007541^5547^^2870722^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3040720^^2570407^47^WHITE, NOT OF HISPANIC ORIGIN^M^SC LESS THAN 50%^^3^00</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>0005710^6050032171^^^^3011210^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3040720^^2500000^54^BLACK, NOT OF HISPANIC ORIGIN^M^^^^000007523^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3040720^^2500210^54^WHITE, NOT OF HISPANIC ORIGIN^M^SERVICE CONNECTED 50%</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>to 100%^^1^000008107^1002929577^000005697^12166^^2870731^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3040720^^2430516^61^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^MT COPAY REQUIRED^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>7^000004336^^^^^2940219^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3040720^^2300000^74^^M^NSC^REQUIRED^^000008604^^^^^^^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3040720^^2380523^66^HISPANIC, BLACK^M^SERVICE CONNECTED 50% to 100%^^1^569</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>485541^1002927098^000002716^5504^^2870723^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3040720^^2220000^82^WHITE, NOT OF HISPANIC ORIGIN^M^SERVICE CONNECTED 50%</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>to 100%^^1^000000881^1002927422^000000814^12163^^2870725^H^^^^^^^^^^^^</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *Report continued on next page*

> July 2014 Pharmacy Benefits Management V. 4.0 83

> Example: Patient Demographics – Detail Report Message (continued)

> Example: Patient Demographics –Timing Report Message

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 17%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY</p>
<p>[#7752] 07/20/04@18:23 6 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Patient Demographics</p>
</blockquote></th>
<th><blockquote>
<p>JUL 20,2004@14:05</p>
</blockquote></th>
<th><blockquote>
<p>JUL 20,2004@18:23</p>
</blockquote></th>
<th><blockquote>
<p>4 hrs, 18 min</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>NOTE: Timing for the Provider Data extract is not recorded when the</p>
<p>the IV, Unit Dose, Prescription, and Patient Demographics extracts are run concurrently.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Patient Demographics – Confirmation Message

<table>
<colgroup>
<col style="width: 80%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI</p>
<p>[#7753] 07/20/04@18:23 6 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>The chart below shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.</p>
<p>PACKAGE # Line items # MailMan msgs</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Patient Demographics 193959 20</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

8.  Outpatient Visits Extract

> In order to decrease the running time of the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option, the ability to extract a month’s worth of outpatient visit records from the VISIT file (#9000010) shall no longer be provided. The ability to extract outpatient visit records for any given timeframe directly from the VISIT file (#9000010) shall be retained with the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option.

> Outpatient Visit records extracted on a daily basis shall be stored in the new PBM PATIENT DEMOGRAPHICS file (#59.9) until they are compiled for transmission when the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option is run.

## Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Data element specifications for the current Outpatient Visit extract are provided in the table below.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>OUTPATIENT VISITS STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sender</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION file (#4)</p>
</blockquote></td>
<td><blockquote>
<p>STATION NUMBER</p>
<p>field (#99)</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Encounter Patient Status</p>
</blockquote></td>
<td><blockquote>
<p>VISIT file (#9000010)</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT STATUS</p>
<p>IN/OUT field (#15002)</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>“I” will be sent for Inpatient “O” will be sent for Outpatient</p>
<p>If no data exists, a null value is sent.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Date of Visit</p>
</blockquote></td>
<td><blockquote>
<p>VISIT file (#9000010)</p>
</blockquote></td>
<td><blockquote>
<p>VISIT/ADMIT</p>
<p>DATE &amp; TIME field (#.01)</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient SSN</p>
</blockquote></td>
<td><blockquote>
<p>VISIT FILE (# 9000010)</p>
<p>PATIENT file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>SOCIAL SECURITY</p>
<p>NUMBER field (#.09)</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>OUTPATIENT VISITS STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient ICN</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>INTEGRATION CONTROL</p>
<p>NUMBER field (# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
<p>(Values in both fields are concatenated with a “V”.)</p>
</blockquote></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Free Text.</p>
<p>Example: “1010185893V199552”</p>
<p>If an ICN does not exist, send null.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICD codes – Diagnosis</p>
</blockquote></td>
<td><blockquote>
<p>V POV file (#9000010.07)</p>
<p>&amp;</p>
<p>V CPT file (#9000010.18)</p>
<p>ICD DIAGNOSIS</p>
<p>file (#80)</p>
</blockquote></td>
<td><blockquote>
<p>POV field (#.01)</p>
<p>&amp; DIAGNOSIS field (#.05)</p>
</blockquote></td>
<td><blockquote>
<p>7-16</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis data is pulled from the POV field (#.01) in the</p>
<p>V POV file (#9000010.07) and</p>
<p>from the DIAGNOSIS field (#.05) in the V CPT file (#9000010.18).</p>
<p>Number of codes is limited to</p>
<p>10. If over 10, they will be truncated.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPT codes</p>
</blockquote></td>
<td><blockquote>
<p>CPT file (#81)</p>
</blockquote></td>
<td><blockquote>
<p>CPT CODE field (#.01)</p>
</blockquote></td>
<td><blockquote>
<p>17-26</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Code Set Indicator</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>27</p>
</blockquote></td>
<td><blockquote>
<p>Code set indicator values include 9 (contains ICD-9 codes only), 10 (contains ICD- 10 codes only, U (contains ICD-9 and ICD-10 codes), and “” (Null – contains no ICD-9 or ICD-10 codes).</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: Outpatient Visits – Detail Report Message

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 21%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMOV 29806 1/1 0 [#33424] 03/02/12@11:42</p>
</blockquote></th>
<th><blockquote>
<p>23 lines</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^0^O^3001016^xxxxxxxxx^5000000019V796730^800.00^^^^^^^^^^^^^^^^^^^^9</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^0^O^3000101^xxxxxxxxx^5000000000V196703^291.9^^^^^^^^^^32160^^^^^^^^^^9</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^0^O^3000101^xxxxxxxxx^5000000019V796730^800.00^^^^^^^^^^32100^^^^^^^^^^9</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^0^I^3010604^xxxxxxxxx^5000000003V639492^800.00^^^^^^^^^^20924^^^^^^^^^^9</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^0^O^3010606^xxxxxxxxx^^144.1^^^^^^^^^^00100^^^^^^^^^^9</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^0^O^3010606^xxxxxxxxx^^850.1^^^^^^^^^^85002^^^^^^^^^^9</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Outpatient Visits – Timing Report Message

<table style="width:100%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 18%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 XXXXXXXX</p>
<p>[#7256] 07/12/04@10:45 6 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Outpatient Visits</p>
</blockquote></th>
<th><blockquote>
<p>JUL 11,2004@18:00</p>
</blockquote></th>
<th><blockquote>
<p>JUL 12,2004@10:45</p>
</blockquote></th>
<th><blockquote>
<p>16 hrs, 45 min</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>NOTE: Timing for the Provider Data extract is not recorded when the</p>
<p>the IV, Unit Dose, Prescription, and Patient Demographics extracts are run concurrently.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Outpatient Visits – Confirmation Message

<table>
<colgroup>
<col style="width: 80%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 XXXXXXXX</p>
<p>[#7257] 07/12/04@10:45 6 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>The chart below shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.</p>
<p>PACKAGE # Line items # MailMan msgs</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Outpatient Visits 32807 4</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

9.  Inpatient PTF Record Extract

> Recent enhancements include an Inpatient Patient Treatment File (PTF) Record extract to collect inpatient treatment file data.

> For inpatient stays, the discharge date is used to identify and extract PTF records. The start date of this extract shall be the discharge date 30 days prior to the first date of the reporting period. For example, if the reporting period is the month of August, the start date for this extract shall be 8/1 minus 30 days. If a PTF record is identified twice, within the same reporting month, the record shall only be sent once.

## Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Data element specifications for the Inpatient PTF Record extract are defined in detail in the table below.

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 25%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>INPATIENT PTF RECORD STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sender (facility #)</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION file (#4)</p>
</blockquote></td>
<td><blockquote>
<p>STATION</p>
<p>NUMBER field (#99)</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>The software extracts the facility number at which the database resides to identify the sender of the MailMan message.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Unique PTF ID</p>
</blockquote></td>
<td><blockquote>
<p>PTF file (#45)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>A unique ID established by concatenating the facility number to the Internal Entry Number of the PTF record in the PTF file (#45).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admission Date for Inpatient Encounter</p>
</blockquote></td>
<td><blockquote>
<p>PTF file (#45)</p>
</blockquote></td>
<td><blockquote>
<p>ADMISSION</p>
<p>DATE field (#2)</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Internal format (minus time)</p>
<p>Example: “2980409”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Discharge Date for Inpatient Encounter</p>
</blockquote></td>
<td><blockquote>
<p>PTF file (#45)</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE</p>
<p>DATE field (#70)</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Internal format (minus time)</p>
<p>Example: “2980409”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient SSN</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>SOCIAL SECURITY</p>
<p>NUMBER field (#.09)</p>
</blockquote></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Internal format Example: “123456789”</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 25%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>INPATIENT PTF RECORD STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>INTEGRATION CONTROL</p>
<p>NUMBER field (#991.01)</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Internal format Example: “1234”</p>
<p>If ICN does not exist, send null.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT file (#2)</p>
</blockquote></td>
<td><blockquote>
<p>INTEGRATION CONTROL</p>
<p>NUMBER field (#991.01)</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Internal format Example: “1234”</p>
<p>If ICN does not exist, send null.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD codes – Diagnosis</p>
</blockquote></td>
<td><blockquote>
<p>ICD DIAGNOSIS file (#80)</p>
</blockquote></td>
<td><blockquote>
<p>CODE NUMBER</p>
<p>field (#.01)</p>
</blockquote></td>
<td>8-27</td>
<td><blockquote>
<p>Internal format Example: “341.8, 341.9”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPT Codes</p>
</blockquote></td>
<td><blockquote>
<p>ICD OPERATION/ PROCEDURE file (#80.1)</p>
</blockquote></td>
<td><blockquote>
<p>CODE NUMBER</p>
<p>field (#.01)</p>
</blockquote></td>
<td>28-43</td>
<td><blockquote>
<p>Internal format Example: “99.10,75.37”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Code Set Indicator</p>
</blockquote></td>
<td><blockquote>
<p>N/A.</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>44</p>
</blockquote></td>
<td><blockquote>
<p>Code set indicator values include 9 (contains ICD-9 codes only), 10 (contains ICD-10 codes only, U (contains ICD-9 and ICD-10 codes), and “” (Null – contains no ICD-9 or ICD-10 codes).</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: Inpatient PTF Records – Detail Report Message

> Example: Inpatient PTF Record – Timing Report Message

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>[#7268] 07/12/04@12:57 6 lines</p>
<p>From: PBMPHARMACIST,EIGHT In 'IN' basket.</p>
</blockquote></th>
<th><blockquote>
<p>Page 1</p>
</blockquote></th>
<th></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Inpatient PTF Record JUL 12,2004@12:56</p>
</blockquote></th>
<th><blockquote>
<p>JUL 12,2004@12:57</p>
</blockquote></th>
<th><blockquote>
<p>0 hrs, 1 min</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>NOTE: Timing for the Provider Data extract is not recorded when the</p>
<p>the IV, Unit Dose, Prescription, and Patient Demographics extracts are run concurrently.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Inpatient PTF Record – Confirmation Message

<table>
<colgroup>
<col style="width: 80%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 XXXXXXXX</p>
<p>[#7269] 07/12/04@12:57 6 lines</p>
<p>From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>The chart below shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.</p>
<p>PACKAGE # Line items # MailMan msgs</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Inpatient PTF Records</p>
<p>1481 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: Provider Data – Detail Report Message

> Example: Provider Data – Provider Summary Report Message

<table>
<colgroup>
<col style="width: 80%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMPRO 30109 605 JERRY L PETTIS VAMC [#7668] 07/18/04@19:41</p>
<p>432 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Provider Summary Report JUL 18, 2004</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SEP 01, 2001 through SEP 30, 2001</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Total Number of Incomplete Provider Records Extracted: 252</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>IEN Provider Name (SSN) Missing Data</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>3 PBMPROVIDER,ONE (????) SSN</p>
<p>78 PBMPROVIDER,TWO (0036) PROVIDER CLASS</p>
<p>238 PBMPROVIDER,THREE (5698) SPECIALTY SUBSPECIALTY</p>
<p>549 PBMPROVIDER,FOUR (????) SSN SPECIALTY SUBSPECIALTY</p>
<p>607 PBMPROVIDER,FIVE (6026) PROVIDER CLASS</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMPRO 30109 605 JERRY L PETTIS VAMC [#7668] Page 2</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>642 PBMPROVIDER,SIX (9499) PROVIDER CLASS</p>
<p>658 PBMPROVIDER,SEVEN (1826) SERVICE/SECTION</p>
<p>1131 PBMPROVIDER,EIGHT (6200) SERVICE/SECTION</p>
<p>1177 PBMPROVIDER,NINE (2889) SERVICE/SECTION</p>
<p>1495 PBMPROVIDER,TEN (6385) PROVIDER CLASS</p>
<p>1599 PBMPROVIDER,ELEVEN (5911) SERVICE/SECTION</p>
<p>1618 PBMPROVIDER,TWELVE (4511) SERVICE/SECTION</p>
<p>1834 PBMPROVIDER,THIRTEEN (3045) PROVIDER CLASS</p>
<p>1868 PBMPROVIDER,FOURTEEN (0711) PROVIDER CLASS SERVICE/SECTION SPECIALTY SUBSPECIALTY</p>
<p>1883 PBMPROVIDER,FIFTEEN (0660) SERVICE/SECTION</p>
<p>1896 PBMPROVIDER,SIXTEEN (7456) PROVIDER CLASS SPECIALTY SUBSPECIALTY</p>
<p>1897 PBMPROVIDER,SEVENTEEN (9472) PROVIDER CLASS</p>
<p>1919 PBMPROVIDER,EIGHTEEN (9754) PROVIDER CLASS</p>
<p>2001 PBMPROVIDER,NINETEEN (2958) PROVIDER CLASS</p>
<p>2023 PBMPROVIDER,TWENTY (0582) PROVIDER CLASS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>ALLERGIES/ADVERSE EVENTS INFORMATION STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Observed/Historical Flag</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
<p>ALLERGIES file (#120.8)</p>
</blockquote></td>
<td><blockquote>
<p>OBSERVED/HISTO</p>
<p>RICAL field (#6)</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Internal Format.</p>
<p>“o” for Observed “h” for Historical</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mechanism</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
<p>ALLERGIES file (#120.8)</p>
</blockquote></td>
<td><blockquote>
<p>MECHANISM field (#17)</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>Internal format.</p>
<p>“A” for Allergy</p>
<p>“P” for Pharmacologic “U” for Unknown</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Event Date/Time</p>
</blockquote></td>
<td><blockquote>
<p>ADVERSE REACTION</p>
<p>REPORTING file (#120.85)</p>
</blockquote></td>
<td><blockquote>
<p>DATE/TIME OF</p>
<p>EVENT field (#.01)</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>Internal Format (date). Example: “3011001.0900”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Observed – Severity</p>
</blockquote></td>
<td><blockquote>
<p>ADVERSE REACTION</p>
<p>REPORTING file (#120.85)</p>
</blockquote></td>
<td><blockquote>
<p>SEVERITY field (#14.5)</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>External format.</p>
<p>Mild Moderate Severe</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sign/Symptom(s)</p>
</blockquote></td>
<td><blockquote>
<p>REACTIONS</p>
<p>multiple (#10) in PATIENT</p>
<p>ALLERGIES file (#120.8)</p>
</blockquote></td>
<td><blockquote>
<p>REACTION sub-</p>
<p>field (#.01)</p>
<p>or</p>
<p>OTHER REACTION</p>
<p>sub-field (#1) (Free text)</p>
</blockquote></td>
<td><blockquote>
<p>14-19</p>
</blockquote></td>
<td><blockquote>
<p>If the sign/symptom entered in the REACTION sub-field (#.01) equals “OTHER REACTION”, the value for the sign/symptom shall be extracted from the OTHER REACTION sub-field (#1).</p>
<p>This is where the free text sign/symptom is stored.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](psu-4-19-user-manual-change-pages/005.png)Note: Pieces 14-19 of this record will repeat for each sign/symptom. The record will allow for up to six sign/symptoms to be extracted and transmitted.

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: Allergies/Adverse Events – Detail Report Message

> July 2014 Pharmacy Benefits Management V. 4.0 101

> Example: Allergies/Adverse Events –Timing Report Message

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 17%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Subj: PBM TIMING for report JUN 01, 2001 to JUN 30, 2001 from 605 JERRY</p>
<p>[#8673] 08/10/04@11:48 6 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Allergies/Adverse Ev</p>
</blockquote></th>
<th><blockquote>
<p>AUG 10,2004@11:47</p>
</blockquote></th>
<th><blockquote>
<p>AUG 10,2004@11:48</p>
</blockquote></th>
<th><blockquote>
<p>0 hrs, 1 min</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>NOTE: Timing for the Provider Data extract is not recorded when</p>
<p>the IV, Unit Dose, Prescription, and Patient Demographics extracts are run concurrently.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Allergies/Adverse Events – Confirmation Message

<table>
<colgroup>
<col style="width: 80%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: PBM Stats for JUN 01, 2001 to JUN 30, 2001 from 605 JERRY L PETTI</p>
<p>[#8674] 08/10/04@11:48 6 lines</p>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>The chart below shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.</p>
<p>PACKAGE # Line items # MailMan msgs</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Allergies/Adverse Events 7 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 12%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>VITALS/IMMUNIZATIONS INFORMATION STATISTICS DATA FIELD SPECIFICATIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DATA ELEMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FILE #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD #</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PIECE # IN RECORD SENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rate</p>
<p>(a numeric value associated with this vital measurement)</p>
</blockquote></td>
<td><blockquote>
<p>GMRV VITAL MEASUREMENT</p>
<p>file (#120.5)</p>
</blockquote></td>
<td><blockquote>
<p>RATE field (#1.2)</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Free text.</p>
<p>Example: “70” for weight; “140/80” for blood pressure.</p>
<p>Or</p>
<p>Users can enter a reason for omission, such as “REFUSE, PASS, or UNAVAILABLE.”</p>
<p>Pain scale codes:</p>
<p>0 – Patient verbalizes no pain. 1-10 – Patient verbalizes pain with “1” representing minimal pain and “10” representing worst imaginable pain.</p>
<p>99 – Patient unable to respond/communicate pain level.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Unit associate with rate ( if applicable)</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Free text.</p>
<p>Regardless of how the user enters a measurement, the software automatically converts the value and stores it in a standard format. The following units will be transmitted for a specific vital type:</p>
<p>Weight – “lb” Height – “in”</p>
<p>Pulse Oximetry – “%”</p>
<p>Null value will be sent for Blood Pressure, Pain, and Pulse since there is no unit associated with these vital types.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Qualifier(s) 1 - 4</p>
</blockquote></td>
<td><blockquote>
<p>GMRV VITAL</p>
<p>QUALIFIER file (#120.52)</p>
</blockquote></td>
<td><blockquote>
<p>QUALIFIER field (#.01)</p>
</blockquote></td>
<td><blockquote>
<p>11-14</p>
</blockquote></td>
<td><blockquote>
<p>Free text</p>
<p>Example: weight may have the following qualifiers: “dry” or “actual”.</p>
<p>Not all measurements will have an associated qualifier. A measurement can have multiple qualifiers. Currently, the maximum number of qualifiers a vital may have is 4.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

> Example: Vitals/Immunizations Information – Detail Report Message

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 26%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMVI 30109 1/4 605 JERRY L PETTIS VAMC</p>
</blockquote></th>
<th><blockquote>
<p>[#8675]</p>
</blockquote></th>
<th rowspan="22"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>08/10/04@11:55 10000 lines</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>From: PBMPHARMACIST,TWO In 'IN' basket. Page 1</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010901.1055^V^000007446^1006019979V41089^^BLOOD PRESSURE^146/83^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010901.1055^V^000007446^1006019979V41089^^PAIN^6^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010901.1055^V^000007446^1006019979V41089^^PULSE^93^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010921.07^V^000003035^1002936262V619083^^BLOOD PRESSURE^112/50^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010916.1714^V^000003035^1002936262V619083^^HEIGHT^71^IN^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010921.07^V^000003035^1002936262V619083^^PAIN^0^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010921.07^V^000003035^1002936262V619083^^PULSE^80^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010916.1714^V^000003035^1002936262V619083^^WEIGHT^150^LBS^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010927.1002^V^000004026^1002930709V651569^^BLOOD PRESSURE^112/40^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010927.1002^V^000004026^1002930709V651569^^HEIGHT^66^IN^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010927.1002^V^000004026^1002930709V651569^^PAIN^7^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010927.1002^V^000004026^1002930709V651569^^PULSE^52^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010927.1002^V^000004026^1002930709V651569^^WEIGHT^200.9^LBS^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010919.1034^V^000000971^1002929377V415816^^BLOOD PRESSURE^110/58^^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010919.1034^V^000000971^1002929377V415816^^PULSE^62^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010919.1034^V^000000971^1002929377V415816^^WEIGHT^185.2^LBS^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>^605^3010919.0743^V^000004414^1002946917V569685^^BLOOD PRESSURE^115/63^^^^^^</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>^605^3010917.0949^V^000004414^1002946917V569685^^HEIGHT^70^IN^^^^^</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Enter RETURN to continue or '^' to exit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following examples.

> Example: Lab – Detail Report Message

> Example: Lab - Laboratory Statistical Summary Message

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 24%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: From:</p>
</blockquote></th>
<th><blockquote>
<p>V. 4.0 PBMLR 29808 556PA PBMPHARMACIST,TWELVE in</p>
</blockquote></th>
<th><blockquote>
<p>NC-PRRTP [#7571162] 17</p>
<p>'IN' basket. Page 1</p>
</blockquote></th>
<th><blockquote>
<p>Sep</p>
</blockquote></th>
<th><blockquote>
<p>98</p>
</blockquote></th>
<th><blockquote>
<p>02:55</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>Lines</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th colspan="8"><blockquote>
<p>Laboratory Statistical Summary Data for AUG 1,1998 through AUG 31,1998 Total Patients 9</p>
<p>Total Laboratory Tests 35</p>
<p>Select MESSAGE Action: IGNORE (in IN basket)// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Laboratory Statistical Data Message

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: V. 4.0 PBMLR 29808 556PA NC-PRRTP [#7571163] 17</p>
</blockquote></th>
<th><blockquote>
<p>Sep</p>
</blockquote></th>
<th><blockquote>
<p>98</p>
</blockquote></th>
<th><blockquote>
<p>02:55</p>
</blockquote></th>
<th>39</th>
<th><blockquote>
<p>Lines</p>
</blockquote></th>
<th rowspan="34"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>From: PBMPHARMACIST,TWELVE in 'IN' basket. Page 1</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>Laboratory Statistical Data for AUG 1,1998 through AUG 31,1998</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>Patient SSN VA CODE Laboratory Results Flag Date/Time Taken</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>000004322 CV800 CREATININE 1.0 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>07/01/98</th>
<th colspan="2"><blockquote>
<p>0818</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>POTASSIUM 3.8 mmol/L</p>
</blockquote></th>
<th></th>
<th></th>
<th>07/01/98</th>
<th colspan="2"><blockquote>
<p>0818</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>000008348 HS502 GLUCOSE 211. mg/dL</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>07/28/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HEMOGLOBIN A1C 10.9 %</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>07/28/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>000002996 CV200 CREATININE 1.3 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>CV350 CHOLESTEROL 175. mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SGOT 26. U/L</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>TRIGLYCERIDES 268. mg/dL</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>HDL CHOLESTEROL 31 mg/dl</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>LDL CHOLESTEROL 90 mg/dl</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>CV800 CREATININE 1.3 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>POTASSIUM 4.7 mmol/L</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>HS502 GLUCOSE 155. mg/dL</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SGOT 26. U/L</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0718</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>HEMOGLOBIN A1C 5.8 %</p>
</blockquote></th>
<th></th>
<th></th>
<th>02/10/98</th>
<th colspan="2"><blockquote>
<p>0719</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000003405 CV200 CREATININE .9 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>03/31/98</th>
<th colspan="2"><blockquote>
<p>0724</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>000009656 CV350 CHOLESTEROL 281. mg/dL</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>06/03/98</th>
<th colspan="2"><blockquote>
<p>0725</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SGOT 23. U/L</p>
</blockquote></th>
<th></th>
<th></th>
<th>06/03/98</th>
<th colspan="2"><blockquote>
<p>0725</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>TRIGLYCERIDES 239. mg/dL</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>06/03/98</th>
<th colspan="2"><blockquote>
<p>0725</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HDL CHOLESTEROL 37 mg/dl</p>
</blockquote></th>
<th></th>
<th></th>
<th>06/03/98</th>
<th colspan="2"><blockquote>
<p>0725</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>LDL CHOLESTEROL 196 mg/dl</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>06/03/98</th>
<th colspan="2"><blockquote>
<p>0725</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000006829 CV200 CREATININE .9 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>07/14/98</th>
<th colspan="2"><blockquote>
<p>0723</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>GA301 CREATININE .9 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>07/14/98</th>
<th colspan="2"><blockquote>
<p>0723</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HS502 GLUCOSE 286. mg/dL</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>07/31/98</th>
<th colspan="2"><blockquote>
<p>0723</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SGOT 83. U/L</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>07/14/98</th>
<th colspan="2"><blockquote>
<p>0723</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>GLUCOSE, 2HR PP 405. mg/dl</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>07/31/98</th>
<th colspan="2"><blockquote>
<p>1010</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>HEMOGLOBIN A1C 7.4 %</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>07/14/98</th>
<th colspan="2"><blockquote>
<p>0723</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000006902 CV200 CREATININE 1.1 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>06/23/98</th>
<th colspan="2"><blockquote>
<p>1442</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>GA301 CREATININE 1.1 mg/dL</p>
</blockquote></th>
<th></th>
<th></th>
<th>06/23/98</th>
<th colspan="2"><blockquote>
<p>1442</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>000003405 CV350 CHOLESTEROL 237. mg/dL</p>
</blockquote></th>
<th><blockquote>
<p>H</p>
</blockquote></th>
<th></th>
<th>07/29/98</th>
<th colspan="2"><blockquote>
<p>0707</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSU*4*12 User Manual Change Pages

## PBM Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSU PBM MANAGER MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *PBM Manager Menu* \[PSU PBM MANAGER MENU\] option grants the user access to the following options:

- *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] allows the user to manually run individual or combined extracts for a time period of their own choosing.
- *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\] allows the user to resend the prior month’s patient demographic data to the PBM national database should the background job be interrupted. Patient demographic data is held for a period of 75 days before being purged.
- *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] allows the user to map Area of Uses (AOUs) from the AR/WS application, Narcotic Area of Uses (NAOUs) from the Controlled Substances application, and Pharmacy Locations from the Drug Accountability application to a specific Medical Center Division or Outpatient site.

## Manual Pharmacy Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSU PBM MANUAL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option is used to gather the statistical information for a selected date range from the following files:

1.  Pharmacy Patient IV Subfile File \# 55.01
2.  Pharmacy Patient UD Subfile File \# 55.06
3.  AR/WS Stats File File \# 58.5
4.  Prescription File \# 52

> 5\. Procurement File \#442, \# 58.811, \# 58.81

6.  Controlled Substances File \# 58.81
7.  Patient Demographics File \# 2
8.  Outpatient Visits File \# 9000010, \# 9000010.07
9.  Inpatient PTF Record File \# 45

> 10\. Provider Data File \# 200, \# 7, \# 49, \#8932.1

11. Allergy/Adverse Event File \# 120.8, \# 120.85
12. Vitals/Immunization Record File \# 120.5, \#9999999.14
13. Laboratory File \# 60, \# 63

> This data can be collected for ALL of the files listed or for one or more specific files. A summary of data or a detailed report by drug can be delivered in a mail message or in a hard copy report.

> ![](psu-4-12-user-manual-change-pages/002.png)Note: Patient demographic data is retained in the PBM file for 75 days, after which time it is purged.

> Example: Generating a Monthly Report for a Specific Package and Transmitting it Via MailMan

> Select OPTION NAME: PSU PBM

1.  PSU PBM AUTO Automatic Pharmacy Statistics
2.  PSU PBM JOB CHECK Pharmacy Background Job Check
3.  PSU PBM MANAGER MENU Manager Menu Options
4.  PSU PBM MANUAL Manual Pharmacy Statistics CHOOSE 1-4: 4 PSU PBM MANUAL Manual Pharmacy Statistics Manual Pharmacy Statistics

> The Pharmacy Benefits Management (PBM) report will extract statistics from one or more of the following files:

1.  Pharmacy Patient IV Sub-file File \# 55.01
2.  Pharmacy Patient UD Sub-file File \# 55.06
3.  AR/WS Stats File \# 58.5
4.  Prescription File \# 52

> 5\. Procurement File \# 442,# 58.811,# 58.81

6.  Controlled Substances File \# 58.81
7.  Patient Demographics File \# 2
8.  Outpatient Visits File \# 9000010,# 9000010.07
9.  Inpatient PTF Record File \# 45

> 10\. Provider Data File \# 200,# 7,# 49,# 8932.1

11. Allergy/Adverse Event File \# 120.8,# 120.85
12. Vitals/Immunization Record File \# 120.5,# 9999999.14
13. Laboratory File \# 60,# 63

> This data can be collected for ALL of the files listed or for one or more specific files. A summary of data or a detailed report by drug can be delivered to you in a mail message or in a hard copy report.

> Is this the monthly report? YES

> Select Month/Year: 09/01 (SEP 2001)

> Do you want a copy of this report sent to you in a MailMan message? NO// YES

> Send this to the PBM section for addition to the master file? NO// YES

> Select one or more of the following:

1.  IVs
2.  Unit Dose
3.  AR/WS
4.  Prescription
5.  Procurement
6.  Controlled Substances
7.  Patient Demographics
8.  Outpatient Visits
9.  Inpatient PTF Records
10. Provider Data
11. Allergies/Adverse Events
12. Vitals/Immunizations Information

> *report continues*

> 6 Pharmacy Benefits Management V. 4.0 January 2008

> If the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option completes successfully, the following two additional reports are generated. Examples are provided in the MailMan Messages section of this document.

> PBM Timing Report: The PBM Timing report displays the start and stop date/time of each extract and a final calculation of how long it took to run. Extract times will vary depending on the system performance, the time that the extract is run (early in the morning, on a weekend versus in the middle of the day), and the amount of data extracted.

> Confirmation Message: The confirmation message shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.

## Automatic Pharmacy Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSU PBM AUTO\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The site should assign the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option to the Pharmacy Supervisor’s menu. This option is used to gather the pharmacy statistics for the previous month from the following files:

1.  Pharmacy Patient IV Subfile File \# 55.01
2.  Pharmacy Patient UD Subfile File \# 55.06
3.  AR/WS Stats File File \# 58.5
4.  Prescription File \# 52

> 5\. Procurement File \#442, \# 58.811, \# 58.81

6.  Controlled Substances File \# 58.81
7.  Patient Demographics File \# 2
8.  Outpatient Visits File \# 9000010, \# 9000010.07
9.  Inpatient PTF Record File \# 45

> 10\. Provider Data File \# 200, \# 7, \# 49, \#8932.1

11. Allergy/Adverse Event File \# 120.8, \# 120.85

> January 2008 Pharmacy Benefits Management V. 4.0 7

12. Vitals/Immunization Record File \# 120.5, \#9999999.14
13. Laboratory File \# 60, \# 63

> This option is executed as a background job each month. The statistics are gathered and then sent to the national PBM section <span class="mark">REDACTED</span> via MailMan messages.

> When scheduling the monthly frequency for this option to be executed, please remember to schedule it to run after the *Update AMIS Stats File* \[PSGW UPDATE AMIS STATS\] option has been executed.

> ![](psu-4-12-user-manual-change-pages/003.png)Note: To decrease the running time of the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option, the ability to extract all patient records from the PATIENT file (#2) every month is no longer provided. This functionality is still available through the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option.

> ![](psu-4-12-user-manual-change-pages/004.png)Note: Patient demographic data is retained in the PBM file for 75 days, after which time it is purged.

> If the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option completes successfully, the following two additional reports are generated. Examples are provided in the MailMan Messages section of this manual.

> PBM Timing Report: The PBM Timing report displays the start and stop date/time of each extract and a final calculation of how long it took to run. Extract times will vary depending on the system performance, the time that the extract is run (early in the morning, on a weekend versus in the middle of the day), and the amount of data extracted.

> Confirmation Message: The confirmation message shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.

## Pharmacy Background Job Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSU PBM JOB CHECK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Pharmacy Background Job Check* \[PSU PBM JOB CHECK\] option checks to see if the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option ran to completion. A MailMan message will be sent to the local and remote members of the facility’s PSU PBM mail group and to the PBM national database at <span class="mark">REDACTED</span> if the report has not completed in six days.

> Population of the PSU PBM JOB field (#90) in the PHARMACY SYSTEM file (#59.7) with a date/time verifies completion. This option is scheduled automatically by the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option and normally does not need user intervention. In case of computer outage, it could be run manually.

> Example: Pharmacy Background Job Check MailMan Message

## Retransmit Patient Demographic Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSU RETRANSMIT PATIENT DATA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option retransmits patient demographic data stored in the PBM file. When a user first enters the option, the software displays the purpose of this option and the first date there is data available for retransmission. The user shall be asked if this is a monthly report. If the response is “Yes”, the user shall be prompted to enter a Month/Year. If the response is ‘No’, the user shall be asked to enter a start date and end date. The user shall not be allowed to retransmit data for the current date. A message shall be displayed to the user stating that the current date is not selectable. If statistical data is not available for the entire month/year, start date, or end date selected, the software shall display a message to the user indicating either the range of dates for which statistical data is available or the start or end date of selectable data. The user shall be prompted to reenter the month/year, start date, or end date.

> Example: Retransmission For a Month of Statistical Data.

> Example: Retransmission For Two Weeks of Statistical Data.

> The user shall then be prompted with “Do you want a copy of this report sent to you in a MailMan message?”. If the user responds Yes, the message shall be sent to the user executing the option, and to local and remote members of the PSU PBM mail group. The user shall then be prompted with “Send this to the PBM section for addition to the master file?”. If the user responds Yes, the message shall be sent to the PBM national database. Only monthly reports shall be transmittable to the PBM national database. The user shall not be prompted to send the message to the master file if the user enters a timeframe other than a month.

> The user shall be asked when they wish to run the job. The user shall be able to immediately run the job or queue it at a later date/time.

> 10 Pharmacy Benefits Management V. 4.0 June 2005
