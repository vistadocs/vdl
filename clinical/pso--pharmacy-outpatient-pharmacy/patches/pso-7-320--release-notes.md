---
title: PSO*7*320 PLQE FY09 Qtr2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PLQE FY09 Qtr2
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*320
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - table
  - class
  - style
  - width
  - contents
  - strong
  - colspan
  - action
  - profile
page_count: 0
word_count: 1167
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/ps0_7_p320_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/ps0_7_p320_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-320-plqe-fy09-qtr2-release-notes/001.png)

OUTPATIENT PHARMACY V. 7.0

> RELEASE NOTES

## PSO\*7\*320

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## August 2009

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Office of Enterprise Development

> *(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [PSO\7\320](#pso7320)
  - [August 2009](#august-2009)
- [Introduction](#introduction)
- [New “Display Remote Data” Prompt](#new-display-remote-data-prompt)
- [New Hidden Action](#new-hidden-action)
- [Action Profile (132 Column Printout) Update](#action-profile-132-column-printout-update)
- [Remote Prescriptions Text on Report](#remote-prescriptions-text-on-report)
> PSO\*7\*320 provides the ability to view a patient’s remote prescription data within Outpatient Pharmacy V. 7.0 using the Remote Data Interoperability (RDI) interface to retrieve data from the Health Data Repository (HDR).
> Several areas of Outpatient Pharmacy were updated to accommodate for the enhancement. These areas include *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\], *Complete Orders from OERR* \[PSO LMOE FINISH\], *Action Profile (132 COLUMN PRINTOUT)* \[PSO ACTION PROFILE\], *Pull Early from Suspense* \[PSO PNDRX\], and *Print from Suspense File* \[PSO PNDLBL\].
> Additionally, three new protocols and two new list templates were added. The following are the three new protocols: PSO RDI VISITS MENU, PSO RDI BOTH, and PSO RDI REMOTE. The new list templates are PSO RDI VISITS and PSO RDI VISITS DETAIL.
> The following information provides descriptions of the enhancement details within each option.

# New “Display Remote Data” Prompt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user can access the patient’s remote prescription data from two areas: *Patient Prescription Processing* and *Complete Orders from OERR*. After entering from one of the two areas, the same prompt is presented to the user in order to proceed to the remote data. Additionally, a hidden action to display those remote prescriptions has been added to each area.

> Patient Prescription Processing

> If RDI is active and a patient has prescriptions at another location, when the user selects the patient to enter a new order from *Patient Prescription Processing*, the new “Display Remote Data?” prompt appears.

> Complete Orders from OERR

> From *Complete Orders from OERR,* when the user answers YES to the “Do you want to see Medication Profile?” prompt, if RDI is active and a patient has prescriptions at another location, the user is prompted with the new “Display Remote Data?” prompt.

> New “Display Remote Data” Prompt

> If the user responds NO, then the normal procedure occurs for each area. If the user responds

> YES, the “Remote Facilities Visited” screen appears such as the following example.

> Example: Patient’s Remote Facilities Visited

> To display the prescriptions at the remote pharmacy location, enter DR (for Display Remote Pharmacy Data) at the “Action” prompt. The “Medication Profile – Remote” screen appears such as the following example.

> Example: Patient’s Remote Medication Profile

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 5%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Medication Profile - Remote</p>
<p>Patient: PSOPATIENT,ONE</p>
</blockquote></th>
<th><blockquote>
<p>Dec</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>30, 2008@17:29:43</p>
<p>(000-00-0000)</p>
</blockquote></th>
<th colspan="2"><p>Page: 1 of 2</p>
<p>DOB: 01/02/1967</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="8"><blockquote>
<p>RX# DRUG ST QTY ISSUED LAST FILLED HDR CHEYENNE</p>
<p>712885 AMOXICILLIN TRIHYDRATE 250MG CAP A 90 11/06/08 11/06/08</p>
<p>SIG: TAKE ONE CAPSULE BY MOUTH THREE TIMES A DAY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>712886</p>
</blockquote></td>
<td><blockquote>
<p>PROVIDER:</p>
<p>DILTIAZEM</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>MCKAY,ELMER</p>
<p>(INWOOD) 240MG CAP,SA</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>30 11/28/08</p>
</blockquote></td>
<td><blockquote>
<p>11/28/08</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>712888</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>SIG: TAKE ONE CAPSULE BY MOUTH EVERY DAY PROVIDER: MCKAY,ELMER</p>
<p>LABETALOL HCL 200MG TAB A 60 12/30/08</p>
</blockquote></td>
<td><blockquote>
<p>12/30/08</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>712887</p>
</blockquote></td>
<td colspan="6"><blockquote>
<p>SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY PROVIDER: MCKAY,ELMER</p>
<p>SIMVASTATIN 20MG TAB A 15 12/09/08</p>
</blockquote></td>
<td><blockquote>
<p>12/09/08</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>SIG: TAKE ONE-HALF TABLET BY MOUTH EVERY EVENING TESTING FOR PATTESTING FOR PATIENT TESTING FOR PATTESTING FOR PATIENTENT INTRUCTION ON SIG1 TESTING FOR PATIENT INTRUCTION ON SIG1 TESTING FOR PATIENT REPLACE IENT WITH IENT TESTING FOR PATIENT</p>
<p>+ Enter ?? for more actions</p>
<p>Select Action:Next Screen//</p>
</blockquote></td>
</tr>
</tbody>
</table>

# New Hidden Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] and *Complete Orders from OERR* \[PSO LMOE FINISH\] on the “Medication Profile” screen, a new hidden ListMan action called DR \[DISPLAY REMOTE\] has been added to display a patient's remote prescriptions. The following is a list of the hidden actions available.

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 28%" />
<col style="width: 6%" />
<col style="width: 26%" />
<col style="width: 6%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>The RP RN</p>
<p>DC</p>
</blockquote></th>
<th><blockquote>
<p>following actions are Reprint (OP)</p>
<p>Renew (OP)</p>
<p>Discontinue (OP)</p>
</blockquote></th>
<th><blockquote>
<p>also OTH DN</p>
<p>RD</p>
</blockquote></th>
<th><blockquote>
<p>available:</p>
<p>Other OP Actions Down a Line</p>
<p>Re Display Screen</p>
</blockquote></th>
<th><blockquote>
<p>DR QU</p>
<p>LS</p>
</blockquote></th>
<th><blockquote>
<p>Display Remote Quit</p>
<p>Last Screen</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>RL</p>
</blockquote></td>
<td><blockquote>
<p>Release (OP)</p>
</blockquote></td>
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>Print List</p>
</blockquote></td>
<td><blockquote>
<p>FS</p>
</blockquote></td>
<td><blockquote>
<p>First Screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RF</p>
</blockquote></td>
<td><blockquote>
<p>Refill (OP)</p>
</blockquote></td>
<td><blockquote>
<p>PS</p>
</blockquote></td>
<td><blockquote>
<p>Print Screen</p>
</blockquote></td>
<td><blockquote>
<p>GO</p>
</blockquote></td>
<td><blockquote>
<p>Go to Page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PP</p>
</blockquote></td>
<td><blockquote>
<p>Pull Rx (OP)</p>
</blockquote></td>
<td><blockquote>
<p>&gt;</p>
</blockquote></td>
<td><blockquote>
<p>Shift View to Right</p>
</blockquote></td>
<td><blockquote>
<p>+</p>
</blockquote></td>
<td><blockquote>
<p>Next Screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IP</p>
</blockquote></td>
<td><blockquote>
<p>Inpat. Profile (OP)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;</p>
</blockquote></td>
<td><blockquote>
<p>Shift View to Left</p>
</blockquote></td>
<td><blockquote>
<p>-</p>
</blockquote></td>
<td><blockquote>
<p>Previous Screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RS</p>
</blockquote></td>
<td><blockquote>
<p>Reprint Sig Log</p>
</blockquote></td>
<td><blockquote>
<p>SL</p>
</blockquote></td>
<td><blockquote>
<p>Search List</p>
</blockquote></td>
<td><blockquote>
<p>ADPL</p>
</blockquote></td>
<td><blockquote>
<p>Auto Display(On/Off)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CM Manual Queue to CMOP</p>
<p>Select Action: Quit//</p>
</blockquote></td>
<td><blockquote>
<p>RDD</p>
</blockquote></td>
<td><blockquote>
<p>Fill/Rel Date Disply</p>
</blockquote></td>
<td><blockquote>
<p>UP</p>
</blockquote></td>
<td><blockquote>
<p>Up a Line</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Action Profile (132 Column Printout) Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSO ACTION PROFILE\]

> If a patient has remote prescriptions, they are printed at the end of the report as demonstrated in the following example.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Select Output Reports Option: <strong>action</strong> Profile (132 COLUMN PRINTOUT) Action or Informational (A or I): A// <strong>I</strong> Informational</p>
<p>By Patient, Clinic or Clinic Group (P/C/G): P// <strong>&lt;Enter&gt;</strong> atient</p>
<p>Do you want this Profile to print in 80 column or 132 column: 132// <strong>&lt;Enter&gt;</strong></p>
<p>Select PATIENT NAME: <strong>OPPATIENT,TEN</strong> OPPATIENT,TEN SC VETERAN</p>
<p>Profile Expiration/Discontinued Cutoff: (0-9999): 120// <strong>&lt;Enter&gt;</strong></p>
<p>DEVICE: <em><strong>[Select Print Device</strong>]</em> GENERIC INCOMING TELNET</p>
<p>Informational Rx Profile Run Date: JUL 11,2007 Page: 1 Sorted by drug classification for Rx's currently active and for those Rx's that have been inactive less than 120 days. Site: VAMC ALBANY (500)</p>
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
<p>Name : OPPATIENT,TEN ID#: 3456</p>
<p>DOB : APR 4,1944 Address : 4 ANYSTREET DR.</p>
<p>ANYCITY, NEW YORK 12345</p>
</blockquote>
<p>Phone : 723-5678</p>
<blockquote>
<p>WEIGHT(Kg): HEIGHT(cm):</p>
<p>DISABILITIES:</p>
<p>ALLERGIES: ASPIRIN-DRUG, METRONIDAZOLE 250MG TAB, METRONIDAZOLE PWDR, PENICILLIN</p>
<p>,</p>
<p>ADVERSE REACTIONS:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Medication/Supply Rx#</p>
<p>Status Expiration Provider</p>
<p>Date</p>
<p>Classification: CN101 - OPIOID ANALGESICS</p>
<p>ACETAMINOPHEN AND CODEINE 30MG Qty: 40 for 31 Days 100003</p>
<p>273 Active 07-16-2007 OPPROVIDER,ONE</p>
<p>COSIGNER: OPPROVIDER,FOUR</p>
<p>Sig: TAKE 2 TABLETS BY MOUTH EVERY SU FOR 10 DAYS WITH FOOD</p>
<p>Filled: 06-15-2007 Past Fills: 06-15-2007 Remaining Refills: 0 Clinic: INFIRMARY</p>
<p>Price: $1.48</p>
</blockquote></td>
</tr>
</tbody>
</table>

> example continues

> PENDING ORDERS

> Drug: ASPIRIN BUFFERED 325MG TAB

> Eff. Date: 10-04-2000Qty: 10 Refills: 3 Prov: OPPROVIDER,ONE Sig: TAKE 1 CAP,ORAL BY MOUTH TWICE A DAY

> Drug: HYDROCHLOROTHIAZIDE 50MG

> Eff. Date: 10-04-2000Qty: 10 Refills: 3 Prov: OPPROVIDER,ONE Sig: TAKE 2 TAB BY MOUTH TWICE A DAY

> MEDICATION PROFILE FROM OTHER VAMC(s) Page: 2

> Date Printed: 12/22/2008

> Patient: OPPATIENT,TEN DOB: 04/04/1944

> ===============================================================================

> RX \# DRUG ST QTY ISSUED LAST FILLED

> =============================================================================== HDR CHEYENNE

> 712885 AMOXICILLIN TRIHYDRATE 250MG CAP A 90 11/06/08 11/06/08 SIG: TAKE ONE CAPSULE BY MOUTH THREE TIMES A DAY

> PROVIDER: PSOPROVIDER,ONE

> 712886 DILTIAZEM (INWOOD) 240MG CAP,SA A 30 11/28/08 11/28/08 SIG: TAKE ONE CAPSULE BY MOUTH EVERY DAY

> PROVIDER: PSOPROVIDER,ONE

> 712887 SIMVASTATIN 20MG TAB A 15 12/09/08 12/09/08 SIG: TAKE ONE-HALF TABLET BY MOUTH EVERY EVENING TESTING

> FOR PATTESTING FOR PATIENT TESTING FOR PATTESTING FOR PATIENTENT INTRUCT ION ON SIG1 TESTING FOR PATIENT INTRUCTION ON SIG1 TESTING FOR PATIENT REPLACE IENT WITH IENT TESTING FOR PATIENT INTRUCTION ON SIG1 TESTING FOR PATI

> PROVIDER: PSOPROVIDER,ONE

# Remote Prescriptions Text on Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the *Pull Early from Suspense* \[PSO PNDRX\] and *Print from Suspense File* \[PSO PNDLBL\] options, if the patient has remote prescriptions, then the text “THIS PATIENT HAS PRESCRIPTIONS AT OTHER FACILITIES” will appear on the report as shown in the following example.