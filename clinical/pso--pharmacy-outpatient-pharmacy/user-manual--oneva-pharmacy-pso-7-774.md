---
title: OneVA Pharmacy User Manual (PSO*7*774)
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: OneVA Pharmacy  (PSO*7*774)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - pharmacy
  - oneva
  - prescription
  - class
  - fill
  - site
  - drug
  - refill
  - dispensing
  - partial
page_count: 0
word_count: 12550
section_count: 7
table_count: 2
figure_count: 3
appendix_count: 4
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_oneva_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_oneva_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_top" class="anchor"></span>Outpatient Pharmacy (PSO)

  <span id="_Toc82184094" class="anchor"></span>Version 7.0

  <span id="_Toc122007588" class="anchor"></span>OneVA Pharmacy User Manual
---

![](oneva-pharmacy-user-manual-pso-7-774/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

Revision History

When updates occur, the Title Page lists the new revised date, and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

<table>
<caption><p><span id="_Toc171325860" class="anchor"></span>Table 1: Conventions</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Patch</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2025</td>
<td>PSO*7*774</td>
<td><ul>
<li><p>Updated <a href="#_Introduction">Introduction</a></p></li>
<li><p>Updated <a href="#system-configuration">System Configuration</a></p></li>
<li><p>Updated <a href="#oneva-pharmacy-and-medication-profile-1">OneVA Pharmacy and Medication Profile</a></p></li>
<li><p>Updated <a href="#_Toc200104204">Figure 4: Test Patient’s Medication Profile</a></p></li>
<li><p>Updated <a href="#oneva-pharmacy-processing-within-patient-prescription-processing">OneVA Pharmacy Processing within Patient Prescription Processing</a></p></li>
<li><p>Updated <a href="#oneva-pharmacy-exception-messages">OneVA Pharmacy Exception Messages</a></p></li>
<li><p>Added <a href="#PSO_7_774_note">Note</a> under <a href="#oneva-pharmacy-exception-messages">OneVA Pharmacy Exception Messages</a></p></li>
<li><p>Updated <a href="#activity-log-entries">Activity Log Entries</a></p></li>
<li><p>Updated <a href="#oneva-pharmacy-prescription-report">OneVA Pharmacy Prescription Report</a></p></li>
<li><p>Added <a href="#PSO_7_774_note_2">Note</a> under <a href="#oneva-pharmacy-prescription-report">OneVA Pharmacy Prescription Report</a></p></li>
<li><p>Added <a href="#PSO_7_774_note_3">Note</a> under Figure 21: Host Site Entry Example</p></li>
<li><p>Updated <a href="#appendix-a-troubleshooting">Appendix A: Troubleshooting</a></p></li>
<li><p>Updated <a href="#appendix-c-frequently-asked-questions-faq">Appendix C: Frequently Asked Questions (FAQ)</a></p></li>
</ul></td>
</tr>
<tr class="even">
<td>07/2024</td>
<td>PSO*7*740</td>
<td><ul>
<li><p>Drug matching details updated in <a href="#drug-matching-process">3.1.1 Drug Matching Process</a></p></li>
<li><p><u>3.1.2 OneVA Pharmacy Exception Messages</u>: OneVA Drug Restrictions - Restricted Field and Clozapine.</p></li>
<li><p>Restricted drugs and Clozapine drugs added to 8. <a href="#appendix-c-frequently-asked-questions-faq">Appendix C: FAQ</a>.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>04/2024</td>
<td>PSO*7*736</td>
<td><p>OneVA messaging from VIERS to VDIF updates made to the following sections:</p>
<ul>
<li><p>1. <u>Introduction</u></p></li>
<li><p>2. <u>OneVA Pharmacy and Medication Profile</u></p></li>
<li><p>3. <u>Processing OneVA Refill/Partial</u></p></li>
<li><p>6. <u>Appendix A: Troubleshooting</u></p></li>
</ul></td>
</tr>
<tr class="even">
<td>08/2023</td>
<td>PSO*7*728</td>
<td><u>OneVA Pharmacy Exception Messages</u>: P15 update when laser label not selected</td>
</tr>
<tr class="odd">
<td>04/2023</td>
<td>PSO*7*643</td>
<td>OneVA user manual revised</td>
</tr>
</tbody>
</table>

<span id="_Toc171325860" class="anchor"></span>Table 1: Conventions

Table of Contents

[1. Introduction [1](#_Toc200091778)](\l)

List of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [System Configuration](#system-configuration)
    - [Documentation Conventions](#documentation-conventions)
  - [Getting Help](#getting-help)
    - [Related Manuals](#related-manuals)
- [OneVA Pharmacy and Medication Profile](#oneva-pharmacy-and-medication-profile)
  - [OneVA Pharmacy and Medication Profile](#oneva-pharmacy-and-medication-profile-1)
- [Processing OneVA Refill/Partial](#processing-oneva-refillpartial)
  - [OneVA Pharmacy Processing within Patient Prescription Processing](#oneva-pharmacy-processing-within-patient-prescription-processing)
    - [Drug Matching Process](#drug-matching-process)
    - [OneVA Pharmacy Exception Messages](#oneva-pharmacy-exception-messages)
- [Activity Log Entries](#activity-log-entries)
- [Reports](#reports)
  - [OneVA Pharmacy Prescription Report](#oneva-pharmacy-prescription-report)
- [Appendix A: Troubleshooting](#appendix-a-troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [Appendix B: Acronyms and Abbreviations](#appendix-b-acronyms-and-abbreviations)
- [Appendix C: Frequently Asked Questions (FAQ)](#appendix-c-frequently-asked-questions-faq)
- [Appendix D: Glossary](#appendix-d-glossary)
The OneVA Pharmacy software (patch PSO\*7\*454 - December 2016) provided the Department of Veterans Health Administration (VHA) the capability to allow Veterans traveling across the United States to refill or partial fill their active VA non-controlled substance prescriptions at any VA Pharmacy location regardless of where the prescription originated. Patch PSO\*7\*454 expanded available pharmacy information in VistA to Pharmacists, providing direct access to any active and refillable prescription from any VA Pharmacy location. Patch PSO\*7\*736 has replaced the query to the Veteran Information/Eligibility Record Services (VIERS) and Health Data Repository/Clinical Data Services Repository (HDR/CDS) repository with a query to the Veterans Data Information Exchange (VDIF).
The OneVA Pharmacy patch PSO\*7\*774 adds the functionality where prescriptions that are parked at the host site will now display with a “P” indicator in the patient’s medication profile at the Dispensing Site.
If a refill or partial request is made from the Dispensing site for a parked prescription, the system will automatically unpark it at the host site
If a refill is requested from the dispensing site on a prescription that has never been filled on the host site, it will be honored. The software will fill the original and this original can be sent to the Outpatient Pharmacy Automated Interface (OPAI) supported external automated dispensing robot.
The activity log and the audit trail at the HOST SITE will be updated for all fills (original, refills, partials) as well as automatically released if the system is set that way. The Copay and/or ECME claims will be triggered as needed, following the auto release logic
> **NOTE:** With PSO\*7\*774, a Refill Request on the dispensing site is what triggers either an original fill or refill on the host site.
> **NOTE:** With PSO\*7\*774, the ability to run a “Partial Fill Rx from Another VA Pharmacy” may not be selected for a remote medication that is both Parked and never been filled.
The overall OneVA Pharmacy software design has several components; they are:
1.  Veterans Health Information Systems and Technology Architecture (VistA)
2.  Health Level 7 (HL7) Messaging
3.  National HL7 Health Connect (an Intersystems HealthShare service)
4.  Veterans Data Information Exchange (VDIF)
VistA is the user interface where a Pharmacist uses the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] menu found within the VistA Outpatient Pharmacy package to query for and original fill/refill/partial fill patient’s active and refillable prescriptions from other VA Pharmacy VistA instances. HL7 messaging is used to query and receive remote prescription details to and from the HDR/CDS repository.
The VistA instance where the Veteran is requesting the refill or partial is considered the ‘dispensing’ VistA instance. The Pharmacist at the ‘dispensing’ VistA instance original fills, refills or partial fills a prescription that originated from another VA Pharmacy VistA instance and prints a prescription label. The VA Pharmacy VistA instance where the prescription originated from and currently exists is the ‘host’ VistA instance. The ‘host’ VistA instance is where the update to the prescription record is made once the fill is processed. The label data elements are extracted from the ‘host’ VistA instance and returned to the dispensing site via HL7 creating the OneVA Pharmacy label. The bar code on the label will only be valid at the host site but not at the dispensing site.
The OneVA Pharmacy software sends an HL7 message to VDIF National Health Connect to an existing TCP Service to request patient medications.
> **NOTE:** The OneVA HL7 Listener Service is using an existing connection that all 130+ VistAs have with the National HL7 Health Connect.
The medication data elements return to the dispensing site via HL7 messaging. Once the prescriptions arrive at the dispensing site, they display below any ‘local’ prescriptions on the Medication Profile view. The prescriptions display to the Pharmacist are sorted by VA Pharmacy site and prescription status. Note: With the introduction of PSO\*7\*774, the prescription status can now include “P” denoting PARKED with ACTIVE prescriptions. The dispensing Pharmacist can view the remote prescriptions and select one to original fill, refill or partially fill. For label printing, VistA triggers the HL7 message stream that executes during the original fill, refill or partial fill prescription processes. The host label data elements are returned to the dispensing site within the HL7 segment. The event triggers the Pharmacist to select the dispensing sites printing device to print a host label.
The OneVA Pharmacy patch, PSO\*7\*479, provided Pharmacists with the ability to request a reprint of the label when no error messages are returned when retrieving the label information from the host system.
The OneVA Pharmacy patch PSO\*7\*497 provided Pharmacists new functionality to fix the auto-suspend defect, limit refill/partial fill permissions to only those personnel who have the ‘PSORPH’ key(s), block prescriptions that contain a trade name in the “TRADE NAME”, identify titration prescriptions at the host site and to disallow refills of such titration prescriptions at the dispensing site.
The OneVA Pharmacy patch PSO\*7\*736 has replaced the query to the HDR/CDS repository with a query to the VDIF repository. This patch also includes modifications to the "PROVIDER HOLD" status abbreviation from "PH" to "HP" and also adds "DISCONTINUED BY PROVIDER", "DISCONTINUED (EDIT)", and "NON-VERIFIED" statuses for display on the patient’s medication profile for remote prescriptions.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy patch, PSO\*7\*479 requires the patch PSS\*1\*212 which delivers the ‘ONEVA PHARMACY FLAG Field (101)’ in the 'off' state. When this flag is in the 'off' state, the VDIF National Health Connect is not queried for external prescriptions and other VistA instances will not be able to (re)fill prescriptions that belong to the VistA instance with the flag set to the 'off' state.

<span id="_Toc200104201" class="anchor"></span>Figure 1: OneVA Pharmacy Flag Field Off

Select Rx (Prescriptions) \<TEST ACCOUNT\> Option: PATient Prescription Processing

Select PATIENT NAME: PSOPATIENT,EIGHT 4-4-74 000000001 NO

NSC VETERAN

Enrollment Priority: Category: IN PROCESS End Date:

PSOPATIENT,EIGHT (000-00-0001)

The OneVA Pharmacy flag is turned off. Queries will NOT be made to other VA Pharmacy locations.

REMOTE PRESCRIPTIONS AVAILABLE!

Display Remote Data? N//

.

When in the 'on' state, all prescription queries and actions may be taken for remote queries, original fills, refills, and partial fills. In order to process prescriptions from another VistA instance, that instance will also need to have its ‘ONEVA PHARMACY FLAG Field (#101)’ set to the 'on' state.

The OneVA Pharmacy flag can be turned on/off using the Pharmacy System Parameters Edit \[PSS SYS EDIT\] option in the Pharmacy Data Management (PDM) package.

<span id="_Toc200104202" class="anchor"></span>Figure 2: OneVA Pharmacy Flag Field On

Select OPTION NAME: PSS SYS EDIT Pharmacy System Parameters Edit

Pharmacy System Parameters Edit

PMIS PRINTER: PP8//

PMIS LANGUAGE: English//

WARNING LABEL SOURCE: NEW//

CMOP WARNING LABEL SOURCE: NEW//

OPAI WARNING LABEL SOURCE: NEW//

AUTOMATE CPRS REFILL:

ONEVA PHARMACY FLAG: ON// \<- The flag can be turned on/off here.

The OneVA Pharmacy patch, PSO\*7\*643 provides Pharmacists the ability to send a OneVA prescription refill or partial fill (and with PSO\*7\*774, an original fill) to the Outpatient Pharmacy Automated Interface (OPAI) to be filled by an external automated dispensing robot. No changes in current external interface parameters or setup are required. The same parameter setup used for the sending of local prescriptions to the OPAI will be utilized. The activity log at the host site is updated to provide an audit trail and to provide various dispensing information for a OneVA prescription original fill, refill or partial fill.

Both the dispensing site and host site must have patch PSO\*7\*643 installed for the OneVA prescription refill or partial fill (or original fill with the introduction of PSO\*7\*774) to be sent to the OPAI to be filled by a supported external automated dispensing robot. If the dispensing site has patch PSO\*7\*643 installed and requests a OneVA prescription refill from a host site that does not have patch PSO\*7\*643 installed, the following message will be displayed “The OneVA refill cannot be sent to the OPAI to be filled by a supported external automated dispensing robot. Both your site and the remote site must have this capability available at the same time. The remote site does not have this capability yet.”

<span id="_Toc200104203" class="anchor"></span>Figure 3: Message for Dispensing Site Requesting OneVA refill from Host Site That Does Not Have Patch PSO\*7\*643 Installed

.

.

Select Action:Quit// RF Refill Rx from Another VA Pharmacy

Remote site drug name: AMOXICILLIN 250MG CAP

Matching Drug Found for Dispensing: AMOXICILLIN 250MG CAP

Would you like to use the system matched drug for this refill/partial fill? NO// YES

Processing refill request. Please be patient as it may take a moment for the host site to respond and generate your label data...

The OneVA refill cannot be sent to the Outpatient Pharmacy Automation Interface (OPAI) to be filled by the Automated Dispensing Device (ADD). Both your site and the remote site must have this capability available at the same time. The remote site does not have this capability yet.

TRANSACTION SUCCESSFUL... The refill for RX \#763261 has been recorded on the prescription at the host system.

Select a printer to generate the label or '^' to bypass printing.

QUEUE TO PRINT ON

DEVICE: ONEVA NULL

.

.

.

If the host site has patch PSO\*7\*643 installed and a dispensing site that does not have patch PSO\*7\*643 installed requests a OneVA prescription refill or partial fill, no message will be displayed. The functionality (current state) present at the dispensing site will be used to process the OneVA prescription refill or partial fill. The OneVA refill or partial fill (or possibly original fill with the introduction of PSO\*7\*774) will NOT be sent to the OPAI to be filled by an external automated dispensing robot.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This *Outpatient Pharmacy V. 7.0 OneVA Pharmacy User Manual* includes documentation conventions, also known as notations, which are used consistently throughout this manual. Each convention is outlined below.

<table>
<caption><p><span id="_Toc466980800" class="anchor"></span>Table 2: Acronym &amp; Abbreviation Table</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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
<td>There are eight options on the Archiving menu.</td>
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
<td><p>&lt;Enter&gt; indicates that the Enter key (or Return key on some keyboards) must be pressed.</p>
<p>&lt;Tab&gt; indicates that the Tab key must be pressed.</p></td>
<td><p>Type Y for Yes or N for No and press &lt;Enter&gt;.</p>
<p>Press &lt;Tab&gt; to move the cursor to the next field.</p></td>
</tr>
<tr class="odd">
<td>![](oneva-pharmacy-user-manual-pso-7-774/002.png)Indicates especially important or helpful information.</td>
<td>![](oneva-pharmacy-user-manual-pso-7-774/003.png)Up to four of the last LAB results can be displayed in the message.</td>
</tr>
<tr class="even">
<td><p>![](oneva-pharmacy-user-manual-pso-7-774/004.png)</p>
<p>Indicates that options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.</p></td>
<td><p>![](oneva-pharmacy-user-manual-pso-7-774/005.png)</p>
<p>This option requires the security key PSOLOCKCLOZ.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc466980800" class="anchor"></span>Table 2: Acronym & Abbreviation Table

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

?, ??, ??? One, two or three question marks can be entered at any of the prompts for online help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

### Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals are located in the [Outpatient](https://www.va.gov/vdl/application.asp?appid=90) folder located on the [VistA Documentation Library (VDL).](http://www.va.gov/vdl)

#### Main Package Documentation

- Outpatient Pharmacy V. 7.0 Release Notes
- Outpatient Pharmacy V. 7.0 Manager’s User Manual
- Outpatient Pharmacy V. 7.0 Pharmacist’s User Manual
- Outpatient Pharmacy V. 7.0 Technician’s User Manual
- Outpatient Pharmacy V. 7.0 User Manual – Supplemental
- Outpatient Pharmacy V. 7.0 Technical Manual/Security Guide
- Dosing Order Check User Manual
- VistA to MOCHA Interface Document
- Outpatient Pharmacy V. 7.0 OneVA Pharmacy Installation Guide
- Outpatient Pharmacy V. 7.0 OneVA Pharmacy User Manual

#### Additional Documentation

Additional documentation related to specific projects is also located on the VDL. For example, there may be several different Release Notes documents that apply to specific projects. Also, there may be several sets of “Change Page” documents, which apply to changes made only for a specific package patch.

# OneVA Pharmacy and Medication Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## OneVA Pharmacy and Medication Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Effective with OneVA Pharmacy, the Medication Profile displays all active medications from other facilities. The medications are retrieved from the VDIF National Health Connect and are displayed below the ‘local’ or ‘Non-VA Med’ orders and are sorted/grouped by facility. The prescriptions originating from other VA Pharmacy locations display under a divider header line showing the site name, site number, and prescription status.

The example shown below displays three pages of a test patient’s Medication Profile, displaying the ‘local’ prescription orders followed by prescription orders that originated at other facilities. With PSO\*7\*774 introduced, some active prescription orders can be PARKED and therefore, could show a “P” alongside the “A” indicator.

<span id="_Toc200104204" class="anchor"></span>Figure 4: Test Patient’s Medication Profile

Medication Profile Jul 28, 2016@05:20:23 Page: 1 of 3

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0001 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------------ACTIVE-------------------------------------

1 10000126 FLUTICAS 100/SALMETEROL 50 INHL DISK 60 E\> 06-01 02-02 11 45

Qty: 2

2 10000128 NIACIN 250MG TAB 270 S\> 06-08 08-27 2 90

3 10000122 RAMIPRIL 5MG CAP 30 A\> 05-31 05-31 8 30

----------------------------------DISCONTINUED----------------------------------

4 10000125 HYDROCHLOROTHIAZIDE 25MG TAB 60 DC\>02-01 02-02 5 60

--------------------------------------HOLD--------------------------------------

5 10000127 LISINOPRIL 2.5MG TAB 90 H\> 03-10 - 3 90

------------------------------ CHYSHR TEST LAB (983) ACTIVE-------------------------------

\+ Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Next Screen//

Medication Profile Jul 28, 2016@05:20:46 Page: 2 of 3

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

\+

6 2718399 IBUPROFEN 800MG TAB 30 A 06-09 07-19 0 10

7 2718383 OMEPRAZOLE 10MG SA CAP 30 A<span class="mark">P</span> 02-02 - 11 30

8 2718397 VERAPAMIL HCL 120MG TAB 60 A 06-15 06-15 5 60

--------------------------- CHYSHR TEST LAB (983) DISCONTINUED----------------------------

9 2718398 ASPIRIN 325MG BUFFERED TAB 300 DC 03-15 03-15 2 90

------------------------------- CHYSHR TEST LAB (983) HOLD--------------------------------

10 2718400 ALBUTEROL 0.5% INHL SOLN 2 H 06-09 - 1 14

----------------------------- CHYSHR TEST LAB (983) SUSPENDED-----------------------------

11 2718401 CALCIUM GLUCONATE 500MG TAB 30 S 05-25 07-14 3 30

-------------------------DAYTSHR TEST LAB (984) ACTIVE--------------------------

\+ Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Next Screen//

Medication Profile Jul 28, 2016@05:16:31 Page: 3 of 3

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

\+

12 2718902 BANDAGE, GAUZE, ROLLER 2 IN X 6 YD 3 A 04-19 04-19 9 29

13 2718862 IBUPROFEN 800MG TAB 60 A<span class="mark">P</span> 05-31 - 11 30

13 2718744 OMEPRAZOLE 10MG SA CAP 60 A 05-03 05-03 5 60

----------------------DAYTSHR TEST LAB (984) DISCONTINUED-----------------------

14 2718745 QUINAPRIL 20MG TAB 30 DC 03-04 03-04 11 30

-------------------------DAYTSHR TEST LAB (984) EXPIRED-------------------------

15 2718746 AMOXICILLIN 250MG CAP 30 E 06-01 05-04 0 10

--------------------------DAYTSHR TEST LAB (984) HOLD---------------------------

16 2718747 CETIRIZINE HCL 10MG TAB 45 H 04-23 - 4 45

------------------------DAYTSHR TEST LAB (984) SUSPENDED------------------------

17 2718748 TRAZODONE HCL 50MG TAB 90 S 04-05 06-24 2 90

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

The OneVA Pharmacy patch (PSO\*7\*454 – December 2016) introduces the new view, ‘REMOTE OP Medications’, which displays the details of the remote prescription order. When selecting a OneVA Pharmacy prescription order from the Medication Profile screen, the new ‘REMOTE OP Medications’ page displays as shown in Figure 5:.

The OneVA Pharmacy patch PSO\*7\*497 updates the ‘REMOTE OP Medications’ display and introduces the new view for prescription orders that originated from other VA Pharmacy locations, the dispensing Pharmacy only has two actions available. They are:

- RF Refill Rx from Another VA Pharmacy
- PR Partial Fill Rx from Another VA Pharmacy

<span id="_Ref123818950" class="anchor"></span>Figure 5: REMOTE OP Medications

![Figure 5 above shows a prescription on the host site is in ACTIVE status. With the introduction of PSO\*7\*774, if it was also PARKED on the host site, then the header would show “ACT/PK” in lieu of “ACTIVE” in parentheses after “REMOTE OP Medications”.](oneva-pharmacy-user-manual-pso-7-774/006.png)

*Figure 5 above shows a prescription on the host site is in ACTIVE status. With the introduction of PSO\*7\*774, if it was also PARKED on the host site, then the header would show “ACT/PK” in lieu of “ACTIVE” in parentheses after “REMOTE OP Medications”.*

Users with PSORPH key will be able to use the above Remote OP Medications option. For users without the PSORPH key the system will display the following message when attempting to fill or refill a remote prescription.

\>\>\> Refill Rx from Another VA Pharmacy may not be selected at this point.

After the installation of PSO\*7\*774, the users without PSORPH Key will be displayed following message if the selected medication is Parked and have never been filled.

\>\>\> Partial Fill Rx from Another VA Pharmacy may not be selected at this point.

OneVA Pharmacy patch PSO\*7\*479 modifies routine PSORRX2 to add the following text if no error message is returned when retrieving the label information from the host system. The following text is displayed just prior to the Label Device: ‘ prompt:

For a refill (or also potentially an original fill with the introduction of PSO\*7\*774):

<span id="_Toc200104206" class="anchor"></span>Figure 6: Refill

TRANSACTION SUCCESSFUL... The refill for RX \#XXXXXX has been recorded on the prescription at the host system.

Select a printer to generate the label or '^' to bypass printing.

QUEUE TO PRINT ON

DEVICE:

For a partial fill:

<span id="_Toc200104207" class="anchor"></span>Figure 7: Partial Fill

TRANSACTION SUCCESSFUL... The partial for RX \#XXXXXX has been recorded on the prescription at the host system.

Select a printer to generate the label or '^' to bypass printing.

QUEUE TO PRINT ON

DEVICE:

# Processing OneVA Refill/Partial

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## OneVA Pharmacy Processing within Patient Prescription Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OneVA Pharmacy introduced messaging for prescriptions from other VA Pharmacy locations and displays them in the Medications Profile view. The query will only execute if the patient has been treated at more than one VA Medical Center. The query retrieves all prescriptions associated with the patient from the VDIF National Health Connect, which requires additional time. To execute the query to VDIF, the user must answer ‘YES’ to the ‘Would you like to query prescriptions from other OneVA Pharmacy locations?’ prompt. When the user responds ‘YES’ to the OneVA Pharmacy prompt, the system displays the OneVA Pharmacy Query Message.

![](oneva-pharmacy-user-manual-pso-7-774/007.png)The OneVA Pharmacy’s feature to query VDIF will not execute if the patient has only one entry in the ‘TREATING FACILITY LIST file (#391.91)’. Prior to validating the TREATING FACILITY LIST entries, the process filters on the following list of valid facility types: VAMC, M&ROC, M&ROC(M&RO), OC, OPC, CBOC, PRRTP, DOM, HCS, MC(M), MC(M&D), MORC, NHC, VANPH, SOC, SARRTP.

If there are not two or more valid entries, the system will not display the ‘Executing OneVA Pharmacy Query Message’ listed in the figure above nor will medications that originated from another VA Pharmacy location display on the Medication Profile view.

![](oneva-pharmacy-user-manual-pso-7-774/008.png)The system identifies and queries VDIF for all the prescriptions that are active, suspended, on hold, expired (within 120 days), or discontinued (within 120 days).

![](oneva-pharmacy-user-manual-pso-7-774/009.png)If the query connection to VDIF fails, a message will display stating ‘The system is down or not responding. Could not query prescriptions at other VA Pharmacy locations. The user should press return to continue and contact local support if this problem persists.

![](oneva-pharmacy-user-manual-pso-7-774/010.png)When the system is down message displays, the VistA session will continue to display the local/dispensing sites prescriptions on the Medication Profile view. There will be no indication if a patient is registered or has prescriptions on other sites (i.e., remote site/OneVA Pharmacy prescriptions will not display on the Medication Profile view.)

![](oneva-pharmacy-user-manual-pso-7-774/011.png)If the patient does not have any prescription records from other VA Pharmacy locations, matching the search criteria, a message will display stating the “Patient found with no prescription records matching search criteria.”

The OneVA Pharmacy patch PSO\*7\*643 introduces the sending of OneVA Rx refills/partial fills to the OPAI to be filled by an external automated dispensing robot when a OneVA Rx refill or partial is processed. With the introduction of OneVA Pharmacy patch PSO\*7\*774, OneVA original fills can also be sent to the OPAI to be filled by an external automated dispensing robot when a OneVA Rx refill request is processed which results in an original fill on the host site. The user is not prompted with whether or not to send the original fill/refill/partial fill to the OPAI. Whether or not the OneVA Rx original fill/refill/partial fill is sent to the OPAI is determined by the EXTERNAL INTERFACE parameter setting in the OUTPATIENT SITE File (#59). Additional parameters in the OUTPATIENT SITE File (#59) and DRUG File (#50) determine which supported external automated dispensing robot the original fill/refill/partial fill is routed to if more than one automated dispensing robot is associated with an Outpatient site.

![](oneva-pharmacy-user-manual-pso-7-774/012.png)By introducing the OneVA Pharmacy patch PSO\*7\*774, once a OneVA original fill/refill/partial fill is sent to the OPAI and the parameter ‘FILE RELEASE DATE/TIME’ in the OUTPATIENT SITE File (#59) is set to ‘Yes’, then the prescription will be auto-released on the host site at the top-file level (original fill), refill level (refill) or partial date level (partial fill).

<span id="_Toc200104208" class="anchor"></span>Figure 8: Example: OneVA Pharmacy Processing of a Refill

Select PATIENT NAME: PSOPATIENT,SIX 2-00-61 000000001 NO

NSC VETERAN

No Patient Warnings on file for PSOPATIENT,SIX.

Press RETURN to continue...

PSOPATIENT,SIX (000-00-0001)

No Allergy Assessment!

Press Return to continue:

Would you like to query prescriptions from other OneVA Pharmacy locations? NO// YES

Please wait. Checking for prescriptions at other VA Pharmacy locations. This may take a moment...

REMOTE PRESCRIPTIONS AVAILABLE!

Display Remote Data? N// O

Eligibility:

RX PATIENT STATUS: OUTPT NON-SC//

<u>Medication ProfileJul 27, 2016@10:11:28 Page: 1 of 1 </u>

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0001 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEFEMALE

CrCL: \<Not Found\> (CREAT: Not Found) BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

\<No local prescriptions found.\>

------------------------- ANYTOWN,OH(984) ACTIVE--------------------------

1 2718861 CETIRIZINE HCL 10MG TAB 30 A 05-21 07-07 7 30

2 2718863 HYDRALAZINE HCL 25MG TAB 60 A 05-11 05-11 5 60

3 2718862 IBUPROFEN 800MG TAB 60 A 05-31 05-31 11 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit//

Select Action: Quit// SO Select Order

Select Orders by number: (1-3): 3

<u>REMOTE OP Medications (ACTIVE)Jul 27, 2016@10:12:37 Page: 1 of 1</u>

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0001 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: FEB 13,1961 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEFEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

Site \#: 984(ANYTOWN,OH)

Rx \#: 2718862

Drug Name: IBUPROFEN 800MG TAB

Days Supply: 30

Quantity: 60

Refills: 11

Expiration Date: 06/01/17

Issue Date: 05/31/16

Stop Date: 06/01/17

Last Fill Date: 05/31/16

Sig: TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED --TAKE WITH

FOOD IF GI UPSET OCCURS/DO NOT CRUSH OR CHEW--

Enter ?? for more actions

RF Refill Rx from Another VA Pharmacy

PR Partial Fill Rx from Another VA Pharmacy

Select Action:Quit// RF Refill Rx from Another VA Pharmacy

Remote site drug name: IBUPROFEN 800MG TAB

Matching Drug Found for Dispensing: IBUPROFEN 800MG TAB

Would you like to use the system matched drug for this refill/partial fill? NO// YES

### Drug Matching Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Overall, three outcomes occur during the OneVA Pharmacy Drug Matching function. They are:

1.  One-to-One Exact Name Match
2.  One-to-Many VA Product ID Match
3.  No Drug Match

#### Drug Matching: One-to-One Exact Name Match

When the drug matching logic identifies a one-to-one exact name match at the dispensing site for the selected host prescription, the system displays the ‘Remote site drug name:’ and the ‘Matching Drug Found for Dispensing:’ and prompts the user to respond ‘YES’ or ‘NO’ as displayed in the following image.

<span id="_Toc200104209" class="anchor"></span>Figure 9: Drug Matching: One-to-One Exact Name Match

Remote site drug name: IBUPROFEN 800MG TAB

Matching Drug Found for Dispensing: IBUPROFEN 800MG TAB

Would you like to use the system matched drug for this refill/partial fill? NO//

#### Drug Matching: One-to-Many VA Product ID Match

If user selects ’NO’ during one-to-one exact name matching or an exact name match was not found, a match using VA product ID is attempted. When the drug matching logic identifies a one-to-many VA product ID match at the dispensing site for the selected host prescription, the system provides a list of one or more matching drugs to select from. If the user selects a local drug from the list, the system prompts the user to respond ‘YES’ or ‘NO’ to confirm the selection.

<span id="_Toc200104210" class="anchor"></span>Figure 10: One-to-Many VA Product ID Match

Remote site drug name: FAMOTIDINE 20MG TAB

No active drug name match found for FAMOTIDINE 20MG TAB.

Drugs matching the VA PRODUCT IDENTIFIER:

1\. 2439 FAMOTIDINE 20MG TAB 60'S GA301 This drug will not be processed without Drug Request Form 10-7144

2\. 7744 FAMOTIDINE 20MG (1/2 OF 20MG) TAB GA301

3\. 7745 FAMOTIDINE 20MG TAB 90'S GA301

Select Drug from list (1-3) or \<enter\> to quit processing.: <u>3</u> 7745 FAMOTIDINE 20MG TAB 90'S GA301

Would you like to use this drug?

#### Drug Matching: No Drug Match

The following example illustrates when no matching local drug is identified at the dispensing site for the selected remote site drug.

<span id="_Toc200104211" class="anchor"></span>Figure 11: Drug Matching: No Drug Match

Remote site drug name: CABERGOLINE 0.5MG TAB

No active drug name match found for CABERGOLINE 0.5MG TAB.

No other local match could be found for CABERGOLINE 0.5MG TAB.

You may need to update your Drug file to process this order.

### OneVA Pharmacy Exception Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are certain conditions under which a OneVA Prescription original fill/refill/partial fill cannot be processed. Those conditions are as follows:

- Patient’s prescription that originated from another VA Pharmacy location will deny the request for a prescription refill to be completed if it is requested "too soon" after the last original fill or refill so that prescriptions are not over-distributed.

> Unable to complete transaction. Cannot be refilled until MM/DD/YYYY.

- Patient’s prescription that originated from another VA Pharmacy location is not fillable when the prescription status is ‘discontinued’, ‘expired’, is on ‘hold’, or ‘suspended’.

> Only 'ACTIVE' remote prescriptions may be refilled at this time.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (refilled) when there are zero remaining refills. Note: Partial fills are allowed.

> Unable to complete transaction. Cannot refill Rx \# xxxxxxx. No refills left.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when the drug is classified as a controlled substance on the dispensing site.

> This is a controlled substance. Cannot refill Rx \# xxxxxxx.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when the drug is classified as a controlled substance on the host site.

> Unable to complete transaction. Rx \#xxxxxxx cannot be refilled.

> The associated drug is considered a controlled substance at the host facility.

- Patient’s prescription cannot be dispensed when the drug is restricted based on the RESTRICT FOR ONEVA PHARMACY (#907) field in the DRUG (#50) file at either/both sites. Note: The local site is checked first, if it is restricted, host site check will not be executed.

> Dispensing site RESTRICT FOR ONEVA PHARMACY refill exception:

> Local Drug is restricted from OneVA Pharmacy processing.

> Cannot refill Rx \# xxxxxxx.

> Dispensing site RESTRICT FOR ONEVA PHARMACY partial fill exception:

> Local Drug is restricted from OneVA Pharmacy processing.

> Cannot process partial fill for Rx \# xxxxxxx.

> Host site RESTRICT FOR ONEVA PHARMACY refill exception:

> Remote Site Drug is restricted from OneVA Pharmacy processing.

> Cannot refill Rx \# xxxxxxx.

> Host site RESTRICT FOR ONEVA PHARMACY partial fill exception:

> Remote Site Drug is restricted from OneVA Pharmacy processing.

> Cannot process partial fill for Rx \# xxxxxxx.

- Patient’s prescription cannot be dispensed when the drug is a Clozapine drug.

> Clozapine refill exception:

> This is a Clozapine prescription.

> Cannot refill Rx \# xxxxxxx.

> Clozapine partial fill exception:

> This is a Clozapine prescription.Cannot process a partial fill for Rx \# xxxxxxx.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when the drug is inactive, not marked for Outpatient Pharmacy or does not have a corresponding Pharmacy Orderable Item on the dispensing site.

> Remote site drug name: CALCIUM ACETATE 667MG (CA 167MG) TAB

> No active drug name match found for CALCIUM ACETATE 667MG (CA 167MG) TAB.

> No other local match could be found for CALCIUM ACETATE 667MG (CA 167MG) TAB.

> You may need to update your Drug file to process this order

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when the drug is inactive on the host site.

| Unable to complete transaction.                                 |
|-----------------------------------------------------------------|
| Drug is inactive for Rx# XXXXXXXX. Cannot process partial fill. |

<span id="_Toc171325862" class="anchor"></span>Table 3: Glossary

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when the drug has no dispensing site match.

> No local match could be found for \<DRUG NAME\>.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when no drug on the dispensing site has a matching VA Product IEN.

> Missing VA Product IEN. Rx \#xxxxxxx cannot be refilled.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when the prescription has a trade name.

Unable to complete transaction.

> This prescription cannot be refilled or partial filled because it has a value entered in the Rx trade name field.  Please follow local policy for obtaining a new prescription.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (original fill, refill or partial fill) when the prescription type is Titration.

Unable to complete transaction.

> Cannot refill prescription - type is Titration. You may request a partial fill.Note: Certain Exception Messages in bold text above indicate that a refill cannot be done. These Exception Messages do not currently discern that a refill request, with the introduction of patch PSO\*7\*774, on the dispensing site could result actually in an original fill on the host site. If desired at a late time, Exception Messaging logic could account for this in a later release.

<span id="_Toc200104212" class="anchor"></span>Figure 12. Transaction Successful

Processing refill request. Please be patient as it may take a moment for the host site to respond and generate your label data...

> TRANSACTION SUCCESSFUL... The refill for RX \#2718862 has been recorded on the prescription at the host system.

> Select a printer to generate the label or '^' to bypass printing.

> QUEUE TO PRINT ON

> DEVICE: ONEVA

> 1 ONEVA NULL NUL

> 2 ONEVAPRT\$PRT BAY PINES TEST LAB

> Choose 1-2\> 1 ONEVA NULL NUL

> Label queued!

> Refill complete for RX \#2718862.

> Press RETURN to continue:

> Updating prescription order list...

![](oneva-pharmacy-user-manual-pso-7-774/013.png)At the device prompt, if a user up-carets (“^”) to bypass printing an original fill, refill or partial fill, whichever was requested, will not be sent to the OPAI and will not be dispensed by the supported external automated dispensing robot.

![](oneva-pharmacy-user-manual-pso-7-774/014.png)At the device prompt, if a user enters a printer that is not defined in the DISPENSING SYSTEM PRINTER field (#2008) of the OUTPATIENT SITE FILE (#59), the prescription will not be sent to the OPAI for dispensing. A label will however print. An exception to this is if a laser label device is not selected, the label will also NOT print.

![](oneva-pharmacy-user-manual-pso-7-774/015.png)At the device prompt, if a user enters a printer and no printers are defined in the DISPENSING SYSTEM PRINTER field (#2008) of the OUTPATIENT SITE FILE (#59), the prescription will be sent to the OPAI for dispensing for a single external automated dispensing robot setup. For a multi dispensing robot setup, if no printers are defined in the DISPENSING SYSTEM PRINTER Field (#2008), and the DISPENSE DNS NAME field (#2006) and the DISPENSE DNS PORT Field (#2007) are not defined, the prescription WILL NOT be sent to the OPAI. If the DISPENSE DNS NAME and DISPENSE DNS PORT fields are populated for the multi dispensing robot setup, the prescription will be sent to the dispensing robot defined by the fields. In all three cases the label will print. An exception to this is if a laser label device is not selected, the label will also NOT print in all three cases.

OneVA Pharmacy remote original fill, remote refill and remote partial fill actions at times receive the following exception message:

> MESSAGE SENT TO TARGET VISTA; TIME OUT AWAITING REPLY

> Press RETURN to continue:

The user pressed RETURN and must execute the transaction steps for a second time. If the user repeats the transaction, the process successfully executes.

During the remote refill of a prescription order that originated from another VA Pharmacy location, the number of refills remaining is decremented by one and the last fill date is updated with the current date on the host VistA database. In the example displayed in the following image, the patient has ‘11’ refills remaining, and the last fill date was ‘05/31/16’. <span id="PSO_7_774_note" class="anchor"></span>Note: With the introduction of OneVA Pharmacy patch PSO\*7\*774, if a remote refill request of a prescription order originating from another VA Pharmacy location results in an original fill being done on the host site, the number of refills remaining will not be decremented by one.

<span id="_Toc122076254" class="anchor"></span>Figure 13: Remote OP Medications View for a Prescription

![](oneva-pharmacy-user-manual-pso-7-774/016.png)

Prescription label is provided for Figure 14. The label is identical to what would have been printed out at the host site.

<span id="_Ref123678524" class="anchor"></span>Figure 14: Prescription Label

No 984 XXX-XXX-0000 (35783/ ) 984 937-XXX-0000 (35783/ ) 984 (35783/ ) JUL 27,2016@10:7

Rx# 2718862 JUL 27,2016 Fill 2 of 12 Rx# 2718862 JUL 27,2016 Fill 2 of 12 Rx# 2718862 JUL 27,2016 Fil2

PSOPATIENT,SIX PSOPATIENT,SIX PSOPATIENT,SIX

TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED TAKE ONE TABLET BY MOUTH TWICE A DAY AS NEEDED

--TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT --TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT --TAKE WITH FOOD IF GI UPSET OCCURS/DO NOT

CRUSH OR CHEW-- CRUSH OR CHEW-- CRUSH OR CHEW--

PSOPROVIDER,ONE PSOPROVIDER,ONE PSOPROVIDER,ONE

Qty: 60 TAB Qty: 60 TAB Qty: 60 TAB

IBUPROFEN 800MG TAB IBUPROFEN 800MG TAB IBUPROFEN 800MG TAB

10 Refills remain prior to JUN 1,2017 Mfg \_\_\_\_\_\_\_\_ Lot# \_\_\_\_\_\_\_\_

PO BOX 415 COPAY Days Supply: 30 Tech\_\_\_\_\_\_\_\_\_\_RPh\_\_\_\_\_\_\_\_\_

ANYTOWN, OH 45428-0415

ADDRESS SERVICE REQUESTED Read FDA Med Guide

\*\*\*DO NOT MAIL\*\*\* Routing: WINDOW

Days supply: 30 Cap: SAFETY

Isd: MAY 31,2016 Exp: JUN 1,27

PSOPATIENT,SIX \*Indicate address change on back of this form Last Fill: 05/31/2016

\[ \] Permanent Pat. Stat ONSC Clinic: CINCI

\[ \] Temporary until \_\_/\_\_/\_\_ DRUG WARNING 8,10,19

Signature\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PSOPATIENT,SIX PSOPATIENT,SIX

Rx# 2718862

IBUPROFEN 800MG TAB Verified Allergies

DRUG WARNING: ------------------

DO NOT DRINK ALCOHOLIC BEVERAGES

when taking this medication. Non-Verified Allergies

TAKE WITH FOOD OR MILK. ----------------------

This is the same medication you

have been getting. Color, size Verified Adverse Reactions

or shape may appear different. --------------------------

Non-Verified Adverse Reactions

------------------------------

PSOPATIENT,SIX JUL 27,2016

Pharmacy Service (119)

VAMC ANYTOWN, OH

P.O. BOX 415

ANYTOWN, OH 45428-0415

Use the label above to mail the computer copies back to us. Apply enough postage to your envelope to ensure delivery.

The VA Notice of Privacy Practices, IB 10-163, which outlines your privacy rights, is available online at http://www.va.gov/Health/ or you may obtain a copy by writing the VHA Privacy Office (19F2), REDACTED,

Washington, DC 20420.

The OneVA Pharmacy patch retrieves the prescription information for the label from the host site and transmits the data back to the dispensing site for printing. As of this writing, there is no ‘REMOTE REPRINT’ option available for OneVA Pharmacy orders. The ‘REPRINT’ action is not operational for the OneVA Pharmacy original fills, refills or partials; however, plans are being made to release a new action option as part of a future OneVA Pharmacy project.

In order to reprint a label due to a paper jam, a malfunction of the printer, or the need to label multiple packages like inhalers, it is suggested to use the OneVA Pharmacy *Partial Fill Rx from Another VA Pharmacy* process and perform the transaction again.

OneVA Pharmacy Patch PSO\*7\*643 removed the ‘REPRINT’ notation on the refill/partial fill labels (which will also include original fill labels with the introduction of OneVA Pharmacy patch PSO\*7\*774). It was also removed from the Label log section in the Activity Log at the host site.

<span id="_Toc200104215" class="anchor"></span>Figure 15: OneVA Pharmacy Processing of a Partial Fill

<u>Medication Profile Jul 27, 2016@10:26:23 Page: 1 of 1</u>

PSOPATIENT,SIX \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: REDACTED Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEFEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

\<No local prescriptions found.\>

------------------------- ANYTOWN, OH (984) ACTIVE--------------------------

1 2718861 CETIRIZINE HCL 10MG TAB 30 A 05-21 07-07 7 30

2 2718863 HYDRALAZINE HCL 25MG TAB 60 A 05-11 05-11 5 60

3 2718862 IBUPROFEN 800MG TAB 60 A 05-31 07-27 10 30

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// 1

REMOTE OP Medications (ACTIVE)Oct 19, 2021@16:57:03 Page: 1 of 1

PSOPATIENT,SIX \<A\>

PID: 000-00-0000 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: REDACTED Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: FEFEMALE

CrCL: \<Not Found\> BSA (m2): \_\_\_\_\_\_\_

Site \#: 984 (ANYTOWN,OH)

Rx \#: 2718861

Drug Name: CETIRIZINE HCL 10MG TAB

Days Supply: 30

Quantity: 30

Refills: 7

Expiration Date: 05/22/17

Issue Date: 05/21/16

Stop Date: 05/22/17

Last Fill Date: 07/07/16

Sig: TAKE ONE TABLET BY MOUTH EVERY DAY

Enter ?? for more actions

RF Refill Rx from Another VA Pharmacy

PR Partial Fill Rx from Another VA Pharmacy

Select Action:Quit// PR Partial Fill Rx from Another VA Pharmacy

Remote site drug name: CETIRIZINE HCL 10MG TAB

Matching Drug Found for Dispensing: CETIRIZINE HCL 10MG TAB

Would you like to use the system matched drug for this

refill/partial fill? NO// YES

Enter Quantity: 10

DAYS SUPPLY: 10

Select PHARMACIST Name: ONEVARPH,ONE// ONEVARPH,ONE 192 ANYTOWN,OH

REMARKS: last refill lost

Processing partial fill request. Please be patient as it may take a moment

for the host site to respond and generate your label data...

TRANSACTION SUCCESSFUL... The partial for RX \#2718861 has been recorded on

the prescription at the host system.

Select a printer to generate the label or '^' to bypass printing.

QUEUE TO PRINT ON

DEVICE: ONEVA

1 ONEVA NULL NUL

2 ONEVAPRT\$PRT BAY PINES TEST LAB

Choose 1-2\> 1 ONEVA NULL NUL

Label queued!

Partial complete for RX \#2718861.

Press RETURN to continue:

Updating prescription order list...

The system displays a message informing that the prescription list is updating. The background process is retrieving the patient’s updated medication profile information from VDIF.

The system will redisplay the Medication Profile view showing the updated prescription information.

Use the OneVA Pharmacy Prescription Reports capability to review the partial fill activity for both the dispensing and host sites transactions. Follow this [LINK](#oneva-pharmacy-prescription-report) to the OneVA Pharmacy Report section for details.

Prescription label is provided for Figure 16:. The label is identical to what would have been printed out at the host site.

<span id="_Ref123678482" class="anchor"></span>Figure 16: Prescription Label

VAMC ANYTOWN, OH 45428-0415 VAMC ANYTOWN, OH 45428-0415 (PARTIAL)

984 xxx-xxx-0000 (35783/ ) 984 xxx-xxx-0000 (35783/ ) 984 (35783/ ) JUL 27,2016@10:0

Rx# 2718861 JUL 27,2016 Fill 2 of 9 Rx# 2718861 JUL 27,2016 Fill 2 of 9 Rx# 2718861 JUL 27,2016 Fil9

PSOPATIENT,SIX PSOPATIENT,SIX PSOPATIENT,SIX

TAKE ONE TABLET BY MOUTH DAILY TAKE ONE TABLET BY MOUTH DAILY TAKE ONE TABLET BY MOUTH DAILY

PSOPROVIDER,ONE PSOPROVIDER,ONE PSOPROVIDER,ONE

Qty: 10 TAB Qty: 10 TAB Qty: 10 TAB

CETIRIZINE HCL 10MG TAB CETIRIZINE HCL 10MG TAB CETIRIZINE HCL 10MG TAB

7 Refills remain prior to MAY 22,2017 Mfg \_\_\_\_\_\_\_\_ Lot# \_\_\_\_\_\_\_\_

PO BOX 415 Days Supply: 10 Tech\_\_\_\_\_\_\_\_\_\_RPh\_\_\_\_\_\_\_\_\_

ANYTOWN, OH 45428-0415

ADDRESS SERVICE REQUESTED

\*\*\*DO NOT MAIL\*\*\* Routing: WINDOW

Days supply: 10 Cap: SAFETY

Isd: MAY 21,2016 Exp: MAY 22,2017

PSOPATIENT,SIX \*Indicate address change on back of this form Last Fill: 05/23/2016

\[ \] Permanent Pat. Stat ONSC Clinic: CINCI

\[ \] Temporary until \_\_/\_\_/\_\_ DRUG WARNING 1,8

Signature\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PSOPATIENT,SIX PSOPATIENT,SIX

Rx# 2718861

CETIRIZINE HCL 10MG TAB Verified Allergies

DRUG WARNING: ------------------

-MAY CAUSE DROWSINESS-

Alcohol may intensify this effect. Non-Verified Allergies

USE CARE when driving or ----------------------

when operating dangerous machinery.

DO NOT DRINK ALCOHOLIC BEVERAGES Verified Adverse Reactions

when taking this medication. --------------------------

Non-Verified Adverse Reactions

------------------------------

PSOPATIENT,SIX JUL 27,2016

Pharmacy Service (119)

ANYTOWN

P.O. BOX 415

ANYTOWN, OH 45428-0415

Use the label above to mail the computer

copies back to us. Apply enough postage

to your envelope to ensure delivery.

The VA Notice of Privacy Practices, IB 10-163, which outlines your privacy rights, is available online at http://www1.va.gov/Health/ or you may obtain a copy by writing the VHA Privacy Office (19F2), 810 Vermont Avenue NW, Washington, DC 20420

# Activity Log Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*643 enhances the current activity log entries to provide an audit trail for OneVA refills and partial fills sent through the OPAI to a supported external automated dispensing robot for dispensing. The host site’s Activity log and label log entries document the facility name and station number where the OneVA refill/partial fill was dispensed. The ‘Initiator of Activity’ was corrected to reflect the remote Pharmacist’s name instead of ‘Postmaster’. Entries 4-5 illustrate a OneVA refill filled at a dispensing site DAYTSHR TEST LAB (984). Entries 6-9 illustrate a OneVA partial filled at a dispensing site, CHYSHR (983) which has multiple supported external automated dispensing robots.

Host Site Activity Log entries for a OneVA refill and Partial filled at dispensing facilities.

<span id="_Toc200104217" class="anchor"></span>Figure 17: Activity Log Entries

<u>Rx Activity Log Nov 30, 2021@11:31:15 Page: 1 of 3</u>

PSOPATIENT,ONE \<NO ALLERGY ASSESSMENT\>

PID: 000-00-0000 Ht(cm): 167.64 (11/05/2021)

DOB: REDACTED Wt(kg): 72.57 (11/05/2021)

Rx \#: 2722091 Original Fill Released: 10/25/21

Routing: Mail Finished by: PHARMACIST,TWO

Refill Log:

\# Log Date Refill Date Qty Routing Lot \# Pharmacist

===============================================================================

1 11/15/21 11/15/21 30 Window 5188 PHARMACIST,DAYTSHR

Division: 984 Dispensed: 11/15/21 Released: NDC: 63653-1171-05

Partial Fills:

\# Log Date Date Qty Routing Lot \# Pharmacist

===============================================================================

1 11/30/21 11/30/21 7 Window 5188 PHARMACIST,CHYSHR

Division: 983 RELEASED:

REMARKS: Ran out of meds

Activity Log:

\# Date/Time Reason Rx Ref Initiator Of Activity

===============================================================================

1 10/25/21@16:42:21 X-INTERFACE ORIGINAL PHARMACIST,LOCAL

Comments: Prescription sent to external interface.

2 10/25/21@16:42:23 X-INTERFACE ORIGINAL POSTMASTER

Comments: HL7 ID - 98468021393 MESSAGE TRANSMITTED TO OPTIFILL2

(10.224.21.245)

3 10/25/21@16:42:30 DISP COMPLETED ORIGINAL PHARMACIST,LOCAL

Comments: External Interface Dispensing is Complete. Filled By: TECH,TWO

Checking Pharmacist: PHARMACIST,TWO

Mail Tracking Info.: REGULAR MAIL3211025 received at 10/25/21@16:42:30

4 11/15/21 X-INTERFACE REFILL 1 PHARMACIST,DAYTSHR

Comments: Refill sent to external interface.

Processed at DAYTSHR TEST LAB (984)

5 11/15/21 DISP COMPLETED REFILL 1 PHARMACIST,DAYTSHR

Comments: External Interface Dispensing is Complete.

Processed at DAYTSHR TEST LAB (984)

Filled By: PERSON,ONE Checking Pharmacist: PHARMACIST,ONE

6 11/30/21 PARTIAL REFILL 1 PHARMACIST,CHYSHR

Comments: Ran out of meds Processed at CHYSHR (983)

7 11/30/21 X-INTERFACE PARTIAL PHARMACIST,CHYSHR

Comments: Partial sent to external interface.

Processed at CHYSHR (983)

8 11/30/21@16:39:04 X-INTERFACE ORIGINAL PHARMACIST,CHYSHR

Comments: HL7 ID - 98468540591 MESSAGE TRANSMITTED TO OPTIFILL2

(10.000.00.000) at CHYSHR(983)

9 11/30/21 DISP COMPLETED PARTIAL PHARMACIST,CHYSHR

Comments: External Interface Dispensing is Complete.

Processed at CHYSHR (983)

Filled By: PERSON,THREE Checking Pharmacist: PHARMACIST,THREE

> **NOTE:** With OneVA Pharmacy patch PSO\*7\*774, activity log entries for original fills will be similarly reflected, as with refills, with the main difference being the Rx Ref column will display “ORIGINAL” to reflect that an original fill was sent through the OPAI to a supported external automated dispensing robot for dispensing.

The label log entries 2-3 below display the facility name and station number where the OneVA refill/partial fills were dispensed. The ‘Printed By was corrected in Patch PSO\*7\*643 to reflect the remote Pharmacist’s name instead of ‘Postmaster’. Note: With the OneVA Pharmacy patch PSO\*7\*774, label log entries could also display the facility name and station number where original fills were dispensed with the Rx Ref column denoting “ORIGINAL” and the Comment including “Printed at \<dispensing site name and station number\>”.

<span id="_Toc200104218" class="anchor"></span>Figure 18. Label Log Entries

![](oneva-pharmacy-user-manual-pso-7-774/017.png)

Patch PSO\*7\*774 has introduced auto-release functionality whenever an original fill or refill is processed through the OPAI automated dispensing device (ADD) which could, if a prescription is ECME billable and the NDC for the medication on the host site is different than the one dispensed through the ADD, create ECME Log entries as shown in Figure 19 below showing a reversal/resubmittal to account for the NDC change.

Figure 19: ECME Log Entries

ECME Log:

\# Date/Time Rx Ref Initiator Of Activity

===============================================================================

1 5/1/25@12:18:11 ORIGINAL PSOAPPLICATIONPROXY,PSO

Comments: ECME:WINDOW FILL(NDC:00082-4179-01)-E REJECTED-pMUTUAL OF OMAHA

2 5/1/25@12:19:36 ORIGINAL DAVIS,ROBERT B

Comments: ECME:RESUBMIT FROM RX EDIT SCREEN-E PAYABLE-pMUTUAL OF OMAHA

3 5/1/25@12:23:49 ORIGINAL PSOAUTORELEASE,PROXY USER

Comments: Rev/Resubmit ECME:AUTO RELEASE(NDC:00082-4179-02)-pMUTUAL OF OMAHA

Copay transactions can also similarly be created in the activity log, where applicable, as part of the new auto-release functionality as shown in Figure 20 below.

Figure 20: Copay Activity Log

Copay Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

===============================================================================

1 05/01/25 COPAY RESET ORIGINAL PSOAUTORELEASE,PROXY USER

Comment: Copay Tier 2 Old value=No Copay New value=Copay

Note the use of the new PSOAUTORELEASE,PROXY USER also introduced as part of PSO\*7\*774 is reflected in Figures 19 and 20 to show an auto-release has occurred.

In addition to new auto-release capabilities, patch PSO\*7\*774 also will automatically UNPARK any original fills or refills (as the result of a refill request on the dispensing site) or partial fills (as the result of a partial fill request on the dispensing site) on the host site which are in a status of ACTIVE/PARKED. Figure 21 shows this UNPARK action reflected in the activity log. Note that existing proxy user PSOAPPLICATIONPROXY,PSO is the Initiator of Activity for this action.

Figure 21: Activity Log Reflecting UNPARK Action

Activity Log:

\# Date/Time Reason Rx Ref Initiator Of Activity

===============================================================================

1 5/1/25@12:17:18 EDIT ORIGINAL DAVIS,ROBERT B

Comments: Rx placed in Parked status (05-01-25)(P)

2 5/1/25@12:17:18 EDIT ORIGINAL DAVIS,ROBERT B

Comments: MAIL/WINDOW/PARK (P),FILL DATE (05-01-25)

3 5/1/25 EDIT ORIGINAL PSOAPPLICATIONPROXY,PSO

Comments: FILL DATE (05/01/25)

4 5/1/25@12:18:11 SUSPENSE ORIGINAL MIAN,NAEEM

Comments: SUSPENSE HOLD until 5/2/25 due to host reject error.

5 5/1/25 EDIT ORIGINAL PSOAPPLICATIONPROXY,PSO

Comments: Rx removed from Parked status (05-01-25)

# Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## OneVA Pharmacy Prescription Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO REMOTE RX REPORT\]

![](oneva-pharmacy-user-manual-pso-7-774/018.png)Note: Prior to the introduction of OneVA Pharmacy patch PSO\*7\*774, to account for copay billing, insurance billing, and subsequent refill capabilities all sites were asked to review the OneVA Pharmacy Reports and manually release prescriptions filled by other stations. Recommended frequency of reviewing these reports is no less than weekly. With PSO\*7\*774 installed and the parameter ‘FILE RELEASE DATE/TIME’ in the OUTPATIENT SITE File (#59) set to ‘Yes’, prescriptions can be auto-released when dispensed via an automated dispensing device sent through the OPAI, and therefore, manual release will likely be needed much less frequently.

The OneVA Pharmacy patch PSO\*7\*454 – December 2016 introduces the new menu option for retrieving the OneVA Pharmacy Prescription Reports. The *ONEVA Pharmacy Prescription Report* \[PSO REMOTE RX REPORT\] menu is located on the *Rx (Prescriptions)* \[PSO RX\] menu.

There are three new reports available on the menu with self-describing titles:

1.  Prescriptions dispensed for other Host Pharmacies
2.  Our prescriptions, filled by other facilities as the Dispensing Pharmacy
3.  All OneVA Pharmacy Prescription Activity

Each report can be searched by (1) Date Range (2) Patient or (3) Site. The type of report and search option selected determines the content shown on a report. All OneVA Pharmacy Prescription reports contain a summary page and a detailed page. All three reports have the same format and basic information.

A row number identifies each refill/partial fill. For each row the date processed, patient name, drug name, quantity dispensed, and the quantity supplied displays. There are four refill type values:

- RF – refills
- PR - partial fills
- OR – refills performed by other sites
- OP – partial fills performed by other sites

<span id="PSO_7_774_note_2" class="anchor"></span>Note: With the introduction of OneVA Pharmacy patch PSO\*7\*774, RF and OR refill type values also encompass original fills being done on the host site as a result of refill requests on the dispensing site.

The total cost is the sum of the costs of all items included in this report and is available on the report ‘Prescriptions we have dispensed for other Host Pharmacies’. The cost is calculated by using the dispensing sites ‘Price Per Dispense Unit’ and multiplying that by the quantity being dispensed.

To review more detailed information about a specific order, perform the following steps:

1.  Enter \<SI\> at the ‘Select Action’ prompt and press \<ENTER\>.

The system displays the action name and prompts for the item to display:

2.  Enter \<1\> at the ‘Enter a number’ prompt and press \<ENTER\>.

The following image displays the ‘Select Action’ and ‘Enter a number’ prompts.

The following is an example of the summary page layout for one of the OneVA Pharmacy reports and a detailed display of an individual order on the report.

<span id="_Toc200104219" class="anchor"></span>Figure 19: OneVA Pharmacy Reports

Patient Prescription Processing

FEE Fee Patient Inquiry

Check Drug Interaction

Complete Orders from OERR

Discontinue Prescription(s)

Edit Prescriptions

ePharmacy Menu ...

List One Patient's Archived Rx's

Manual Print of Multi-Rx Forms

OneVA Pharmacy Prescription Report

Reprint an Outpatient Rx Label

Signature Log Reprint

View Prescriptions

Select Rx (Prescriptions) \<TEST ACCOUNT\> Option: OneVA Pharmacy Prescription Ret

Report

1\. Prescriptions dispensed for other Host Pharmacies

2\. Our prescriptions, filled by other facilities as the Dispensing Pharmacy

3\. All OneVA Pharmacy Prescription Activity

Select item: (1-3): ?

Selecting 1 will display the list of prescriptions that our local facility has dispensed on behalf of other host Pharmacy locations as part of the OneVA Pharmacy program. Selecting 2 will display the list of prescriptions other VA Pharmacy locations have filled as a dispensing site for a prescription that originated from our location. Selecting 3 will list all prescriptions that either we have filled for other Pharmacy locations as the dispensing site or other Pharmacy locations have filled on our behalf.

Answer with 1, 2, or 3.

1\. Prescriptions dispensed for other Host Pharmacies

2\. Our prescriptions, filled by other facilities as the Dispensing Pharmacy

3\. All OneVA Pharmacy Prescription Activity

> Select item: (1-3): 3 All OneVA Pharmacy Prescription Activity

> Select one of the following:

> D DATE RANGE

> P PATIENT

> S SITE

> Search by: DATE RANGE

> Enter start date: Nov 16, 2021//12/12/21 (DEC 12, 2021)

> Enter end date: Dec 16, 2021// (DEC 16, 2021)

> <u>OneVA PHARMACY RX REPORT Dec 16, 2021@15:32:51 Page: 1 of 1</u>

> All OneVA Pharmacy Prescription Activity

> <u>\# DATE PATIENT DRUG NAME TYPE QTY DSUP</u>

> 1 DEC 13, 2021 PSOPATIENT,ONE CETIRIZINE HCL 10MG PR 1 1

> 2 DEC 13, 2021 PSOPATIENT,NINE ACETAMINOPHEN 325MG OP 2 2

> 3 DEC 13, 2021 PSOPATIENT,TWO MINOXIDIL 10MG TAB PR 4 4

> 4 DEC 13, 2021 PSOPATIENT,TWO METOPROLOL SUCCINATE RF 30 30

> 5 DEC 13, 2021 PSOPATIENT,TWO FOLIC ACID 1MG TAB PR 4 4

> 6 DEC 14, 2021 PSOPATIENT,FIFTEEN ROSUVASTATIN CA 20MG RF 30 30

> 7 DEC 14, 2021 PSOPATIENT,FIFTEEN AMIODARONE HCL (SAND PR 21 7

> 8 DEC 15, 2021 PSOPATIENT,TEN BENAZEPRIL HCL 10MG OR 7 7

> 9 DEC 15, 2021 PSOPATIENT,EIGHT DIPHENHYDRAMINE HCL PR 42 7

> 10 DEC 15, 2021 PSOPATIENT,EIGHT FUROSEMIDE 20MG TAB RF 60 30

> Total Cost for items in this report: \$37.12

> Enter ?? for more actions

Select Action:Quit// SI Select Item

Enter a number (1-3): 1

Patch PSO\*7\*643 added new fields from the REMOTE PRESCRIPTION LOG File (#52.09) to the detailed display below. There are some minor differences between the request type(s) of outside refill/outside partial fill requests for the host site and refill/partial fill requests for the dispensing site. The Internal Entry Number (IEN) of the Local (matched) drug displays next to the drug name in parenthesis for a Dispensing site entry. The Remote Filling Person, Remote Checking Pharmacist, OPAI Message ID, DISP ADD Name, and DISP ADD DNS are found for both the Dispensing and Host site entries. Patch PSO\*7\*643 corrected an issue that caused the Quantity and Days Supply not to display in the detailed view.

<span id="_Toc200104220" class="anchor"></span>Figure 20: Dispensing Site Entry Example

![](oneva-pharmacy-user-manual-pso-7-774/019.png)

The Host site entry will not have a value for the local (matched) drug label. The additional field displayed for the Host site will be either the Host Refill IEN or the Host Partial IEN depending on whether a refill or partial fill was dispensed.

<span id="_Toc200104221" class="anchor"></span>Figure 21: Host Site Entry Example

![](oneva-pharmacy-user-manual-pso-7-774/020.png)

<span id="PSO_7_774_note_3" class="anchor"></span>Note: With the introduction of the OneVA Pharmacy patch PSO\*7\*774, Request Types of OUTSIDE REFILL could initiate an original fill on the host site if the prescription in question was never filled. In those cases, the Host Refill IEN would be blank.

# Appendix A: Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OneVA Pharmacy introduces new functionality that allows a Pharmacist to original fill, refill or partial fill a prescription from another VA Pharmacy location. This software patch uses HL7 messaging to send and receive remote prescription details from another VA Pharmacy location. This allows a ‘dispensing’ (‘non-custodial’ or ‘local’ pharmacy) facility to original fill, refill or partial fill a prescription that originated from another VA Pharmacy location. The VA Pharmacy location where the prescription originated is the ‘host’ (‘remote’) facility.

The OneVA Pharmacy software sends the HL7 query message through the VDIF repository.

The prescriptions display below any ‘local’ prescriptions on the Medication Profile view. The Pharmacist can then view and choose a remote (host) prescription and will be able to original fill, refill or partially fill any active non-controlled substance prescription at either facility.

All OneVA Prescription original fills, refills and partial fills are logged into a new file called REMOTE PRESCRIPTION LOG (#52.09) for host and dispensing facilities. The entries are viewable using the *OneVA Pharmacy Prescription Report* functionality.

With this integrated VistA patch, several points of failure could occur. The systems design will allow the process to continue if any of the various integration points fail, however, remote prescriptions will not display to the Pharmacist on the Medication Profile view.

There are application error messages that will display during the search for the patient and the patient’s prescriptions. They are:

- No patient error message:

> PATIENT IDENTIFIER NOT FOUND

- Multiple patients returned error messages:

> MORE THAN ONE PATIENT RETURNED IN CALL TO VDIF

> MORE THAN ONE PATIENT FOUND ON RX DATABASE, CHECK ICN

- Patient returned; no prescription data returned error message:

> PATIENT FOUND WITH NO PRESCRIPTION RECORDS

- Patient returned; no prescription data matching filters returned error message:

> PATIENT FOUND WITH NO PRESCRIPTION RECORDS MATCHING SEARCH CRITERIA

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors are errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. For any significant error, please contact your local support.

# Appendix B: Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides the list of acronyms used throughout the document along with their descriptions.

| Acronym/Abbreviation       | Description                                                               |
|----------------------------|---------------------------------------------------------------------------|
| \[DIUSER\]                 | FileMan Menu                                                              |
| \[PSO LM BACKDOOR ORDERS\] | Patient Prescription Processing Menu                                      |
| \[PSO MANAGER\]            | Outpatient Pharmacy Manager Menu                                          |
| \[PSO MENU\]               | Pharmacy Menu                                                             |
| \[PSO REMOTE RX REPORT\]   | OneVA Pharmacy Prescription Report Menu                                   |
| \[PSO RX\]                 | Rx (Prescriptions) Menu                                                   |
| AITC                       | Austin Information Technology Center                                      |
| C/HDR                      | Clinical/Health Data Repository                                           |
| CDS                        | Clinical Data Services                                                    |
| CHYSHR                     | Chyshr Test Laboratory VistA instance                                     |
| Clin1                      | Clinical Product Support Team 1                                           |
| DAYTSHR                    | Daytshr Test Laboratory VistA instance                                    |
| DoD                        | Department of Defense                                                     |
| EPMO                       | Office of Information and Technology Enterprise Program Management Office |
| GOV                        | Government                                                                |
| HDR                        | Health Data Repository                                                    |
| HL7                        | Health Level 7                                                            |
| ICN                        | Integrated Control Number                                                 |
| IEN                        | Internal Entry Number                                                     |
| IOC                        | Initial Operating Capability                                              |
| IT                         | Information Technology                                                    |
| MLLP                       | Minimal Layer Protocol                                                    |
| MVI                        | Master Veteran Index                                                      |
| NPI                        | National Provider Identifier                                              |
| NSD                        | National Service Desk                                                     |
| OIT                        | Office of Information and Technology                                      |
| OMB                        | Office of Management and Budget                                           |
| OP                         | Outpatient Pharmacy                                                       |
| OP                         | OneVA Pharmacy Partial Fill                                               |
| OPAI                       | Outpatient Pharmacy Automated Interface                                   |
| OR                         | OneVA Pharmacy Refill                                                     |
| PDM                        | Pharmacy Data Management application namespace                            |
| PII                        | Personally Identifiable Information                                       |
| PR                         | Partial Refill (Local)                                                    |
| PSO                        | Outpatient Pharmacy application namespace                                 |
| RF                         | Refill (Local)                                                            |
| Rx                         | Prescription                                                              |
| SDM                        | Service Desk Manager                                                      |
| SOAP                       | Simple Object Access Protocol                                             |
| VA                         | Department of Veterans Affairs                                            |
| VAMC                       | Veterans Affairs Medical Center                                           |
| VDIF                       | Veterans Data Information Exchange                                        |
| VDL                        | VA Software Document Library                                              |
| VHA                        | Department of Veterans Health Administration                              |
| VIERS                      | Veteran Information/Eligibility Record Services                           |
| VistA                      | Veterans Health Information Systems and Technology Architecture           |

# Appendix C: Frequently Asked Questions (FAQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  What is the Value to me as the Veteran?

> The previous ‘Coordinated Care for Traveling Veterans’ handbook required either a visit to the Emergency Room/Urgent Care Center or a pharmacy clinic visit to obtain a new prescription. OneVA Pharmacy makes the best use of the prescription already on file at another VA medical center.

> Audience: Veteran

2)  What if I have never been registered at the VA where I’m trying to pick up my prescription?

> Veterans must register/enroll at the VA medical center in order for the pharmacy to see their records.

> Audience: Veteran

3)  Does OneVA Pharmacy benefit me if I’m not traveling?

> Use existing processes to contact the VA where your prescription is on file to request a refill.

> Audience: Veteran

4)  Do you still need to enter Allergies into the Pharmacy profile?

> VistA pharmacy will display allergies and adverse reactions from all remote facilities.

> Audience: Pharmacy

5)  Can we send the prescription to CMOP?

> OneVA Pharmacy is designed to provide an immediate fill at the Pharmacy window.

> Audience: Pharmacy

6)  Can any prescription be filled by OneVA Pharmacy?

> Controlled substances (CS at one or both facilities) cannot be filled via OneVA Pharmacy.

> Drugs not matched to the National Drug file cannot be filled via OneVA Pharmacy.

> Prescriptions with no remaining refills, on suspense or on hold cannot be filled.

> Clozapine drugs cannot be filled via OneVA Pharmacy. A clozapine prescription is identified by having the MONITOR ROUTINE Field (#17.5) in the DRUG File (#50) set to ‘PSOCLO1’.

> Restricted drugs cannot be filled via OneVA Pharmacy based on the RESTRICT FOR ONEVA PHARMACY (#907) field set to 1 in the DRUG (#50) file.

> Audience: Pharmacy, Veteran

7)  What should I do if I do not have the medication in stock?

> Order the medication if the Veteran can return the next day, mail from CMOP to a temporary address, utilize the Coordinated Care for Traveling Veteran Handbook. “What would a prudent Pharmacist do?”

> Audience: Pharmacy

8)  What information is kept in my VistA system and what information is kept at the host VistA system?

> The dispensing VistA system tracks the information in a new OneVA Pharmacy file – REMOTE PRESCRIPTION LOG File (#52.09) for reporting purposes. The original fill, refill or partial fill is tracked in the host system’s prescription file and activity log.

> Audience: Pharmacy

9)  What if it is too soon to fill?

> Prescription will not be available to refill. Partial fills will be an available option. Sites can use Remote Data Views to see the fill history from the host station, especially if there are concerns for frequent partial fill requests of the same Rx.

> Audience: Pharmacy

10) What is the dispensing name and address on the label?

> The host pharmacy will be the name and address printed on the label which is consistent with how CMOP processes prescriptions.

> Audience: Pharmacy

11) Are there any responsibilities for the host pharmacy in OneVA Pharmacy?

> To account for copay billing, insurance billing and subsequent refill capabilities all sites are asked to review the *OneVA Pharmacy Prescription Report* \[PSO REMOTE RX REPORT\] and manually release prescriptions filled by other stations. Recommended frequency of reviewing report is no less than weekly. With the OneVA Pharmacy patch PSO\*7\*774, prescriptions can now be auto-released if set up to do so, hence, manual release tasks may lessen considerably.

> Audience: Pharmacy

12) How does OneVA Pharmacy select the drug from my drug file?

> The original prescription resides in HealthShare's Summary Document Architecture (SDA). OneVA Pharmacy identifies the national drug file (NDF) “VA Product” for the prescription. Matching drugs in your local drug file are identified based on that NDF product. If there is a 1:1 match found, OneVA Pharmacy will recommend that drug. If there are multiple possible matches found, OneVA Pharmacy will present a pick list to select from.

> Audience: Pharmacy

13) How much information can you see from the Host prescription file?

> OneVA Pharmacy displays a limited subset of the prescription. Once the patient is registered, VistA Web can be utilized to see details of the prescription.

> Audience: Pharmacy

14) What if the original prescription uses an abbreviation that is not in our instruction file?

> The prescription label is generated from the host prescription file. This is consistent with how CMOP processes prescriptions.

> Audience: Pharmacy

15) OneVA Pharmacy reports show cost information, which system is used to calculate medication cost?

> The dispensing system’s cost is used in the report.

> Audience: Pharmacy

16) Can I send an OneVA Pharmacy prescription to automation via the Outpatient Pharmacy Automation Interfaces (OPAI)?

> Yes, patch PSO\*7\*643 allows OneVA Pharmacy prescription original fills, refills and partial fills to be sent to an external automated dispensing robot via the OPAI.

> Audience: Pharmacy

17) If a patient is requesting a medication that requires in-clinic administration, could I use OneVA Pharmacy?

> OneVA Pharmacy functionality is intended for outpatient prescriptions to be dispensed at the Pharmacy window.

> Audience: Pharmacy

18) How will a patient be notified that their OneVA prescription is ready for pickup?

> OneVA Pharmacy does not interface with prescription ready notification boards. Consider alternative processes and workflow. If, however, the OneVA Pharmacy original fill, refill or partial fill is sent to an external automated dispensing robot via the OPAI, the patient will be notified that their OneVA prescription is ready for pickup.

# Appendix D: Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions for common acronyms and terms used in this manual.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym/Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Action Profile</td>
<td>A list of all active and recently canceled or expired prescriptions for a patient sorted by classification. This profile also includes a signature line for each prescription to allow the physician to cancel or renew it.</td>
</tr>
<tr class="even">
<td>Activity Log</td>
<td>A log, by date, of changes made to or actions taken on a prescription. An entry is made in this log each time the prescription is edited, canceled, reinstated after being canceled, or renewed. An entry will be made into this log each time a label is reprinted. A CMOP activity log will contain information related to CMOP dispensing activities.</td>
</tr>
<tr class="odd">
<td>Allergy/ADR Information</td>
<td>Includes non-verified and verified allergy and/or adverse reaction information as defined in the Adverse Reaction Tracking (ART) package. The allergy data is sorted by type (DRUG, OTHER, FOOD). If no data is found for a category, the heading for that category is not displayed.</td>
</tr>
<tr class="even">
<td>Allergy Order Checks</td>
<td>The process that compares the drugs prescribed for a patient against that patient’s recorded allergies.</td>
</tr>
<tr class="odd">
<td>AMIS</td>
<td>Automated Management Information System</td>
</tr>
<tr class="even">
<td>Answer Sheet</td>
<td>An entry in the DUE ANSWER SHEET file. It contains the questions and answers of a DUE questionnaire. This term is also used to refer to the hard copy representation of a DUE ANSWER SHEET entry.</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Programming Interface</td>
</tr>
<tr class="even">
<td>APSP</td>
<td>Originally Indian Health Service Pharmacy's name space now owned by the Outpatient Pharmacy software.</td>
</tr>
<tr class="odd">
<td>BSA</td>
<td><p>Body Surface Area. The Dubois formula is used to calculate the Body Surface Area using the following formula:</p>
<p>BSA (m²) = 0.20247 x Height (m)0.725 x Weight (kg)0.425</p>
<p>The equation is performed using the most recent patient height and weight values that are entered into the vitals package.</p>
<p>The calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="even">
<td>Bypass</td>
<td>Take no action on a medication order.</td>
</tr>
<tr class="odd">
<td>CHAMPVA</td>
<td>CHAMPVA (Civilian Health and Medical Program of the Department of Veterans Affairs) is a cost-shared health benefits program established for the dependents and survivors of certain severely disabled and/or deceased veterans.</td>
</tr>
<tr class="even">
<td>Clinical Reminder Order Checks (CROC)</td>
<td>CPRS Order Checks that use Clinical Reminder functionality, both reminder terms and reminder definitions, to perform checks for groups of Orderable Items.</td>
</tr>
<tr class="odd">
<td>CMOP</td>
<td>Consolidated Mail Outpatient Pharmacy</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System. CPRS is an entry point in VistA that allows the user to enter all necessary orders for a patient in different packages (e.g., Outpatient Pharmacy, Inpatient Pharmacy, etc.) from a single-entry point.</td>
</tr>
<tr class="odd">
<td>CrCL</td>
<td><p>Creatinine Clearance. The CrCl value which displays in the pharmacy header is identical to the CrCl value calculated in CPRS. The formula approved by the CPRS Clinical Workgroup is the following:</p>
<p>Modified Cockcroft-Gault equation using Adjusted Body Weight in kg (if ht &gt; 60in)</p>
<p>This calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="even">
<td>Critical</td>
<td>Interactions with severe consequences that require some type of action (finding facts, contacting prescribers) to prevent potential serious harm.</td>
</tr>
<tr class="odd">
<td>DATUP</td>
<td>Data Update. Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the two centralized databases at Austin and Martinsburg.</td>
</tr>
<tr class="even">
<td>DEA</td>
<td>Drug Enforcement Agency</td>
</tr>
<tr class="odd">
<td>DEA Special Handling</td>
<td>The Drug Enforcement Agency special Handling code used for drugs to designate if they are over-the counter, narcotics, bulk compounds, supply items, etc.</td>
</tr>
<tr class="even">
<td>DHCP</td>
<td>See VistA.</td>
</tr>
<tr class="odd">
<td>DIF</td>
<td>Drug Information Framework</td>
</tr>
<tr class="even">
<td>Dispense Drug</td>
<td>The Dispense Drug name has the strength attached to it (e.g., Acetaminophen 325 mg). The name alone without a strength attached is the Orderable Item name.</td>
</tr>
<tr class="odd">
<td>DNS</td>
<td>Domain Name Server</td>
</tr>
<tr class="even">
<td>DoD</td>
<td>Department of Defense</td>
</tr>
<tr class="odd">
<td>Dosage Ordered</td>
<td>After the user has selected the drug during order entry, the dosage ordered prompt is displayed.</td>
</tr>
<tr class="even">
<td>Drug/Drug Interaction</td>
<td>The pharmacological or clinical response to the administration of a drug combination different from that anticipated from the known effects of the two agents when given alone.</td>
</tr>
<tr class="odd">
<td>DUE</td>
<td>Drug Usage Evaluation</td>
</tr>
<tr class="even">
<td>Enhanced Order Check</td>
<td>Drug – Drug Interaction, Duplicate Therapy, and Dosing order checks that are executed utilizing FDB’s MedKnowledge Framework APIs and database.</td>
</tr>
<tr class="odd">
<td>ETC</td>
<td>Enhanced Therapeutic Classification</td>
</tr>
<tr class="even">
<td>Expiration/Stop</td>
<td>The date on which a prescription is no longer active. Typically, this date is 30 days after the issue date for narcotics, 365 days after the issue date for other medications and 365 days after the issue date for supplies.</td>
</tr>
<tr class="odd">
<td>FDB</td>
<td>First DataBank</td>
</tr>
<tr class="even">
<td>Finish</td>
<td>Term used for completing orders from Order Entry/Results Reporting.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="even">
<td>HDR/CDS</td>
<td>Health Data Repository/Clinical Data Services Repository</td>
</tr>
<tr class="odd">
<td>HDR-Hx</td>
<td>Health Data Repository Historical</td>
</tr>
<tr class="even">
<td>HDR-IMS</td>
<td>Health Data Repository- Interim Messaging Solution</td>
</tr>
<tr class="odd">
<td>Issue Date</td>
<td>The date on which the prescription was written. This date is usually, but not always, the same as the first fill date. This date cannot be later than the first fill date.</td>
</tr>
<tr class="even">
<td>HFS</td>
<td>Host File Server</td>
</tr>
<tr class="odd">
<td>Health Insurance Portability and Accountability Act of 1996 (HIPAA)</td>
<td>A Federal law that makes several changes has the goal of allowing persons to qualify immediately for comparable health insurance coverage when they change their employment relationships. Title II, Subtitle F, of HIPAA gives HHS the authority to mandate the use of standards for the electronic exchange of health care data; to specify what medical and administrative code sets should be used within those standards; to require the use of national identification systems for health care patients, providers, payers (or plans), and employers (or sponsors); and to specify the types of measures required to protect the security and privacy of personally identifiable health care information. Also known as the Kennedy-Kassebaum Bill, the Kassebaum-Kennedy Bill, K2, or Public Law 104-191.</td>
</tr>
<tr class="even">
<td>JCAHO</td>
<td>Joint Commission on Accreditation of Healthcare Organizations</td>
</tr>
<tr class="odd">
<td>Label/Profile Monitor</td>
<td>A file for each printer which records, in the order in which they were printed, the last 1000 labels or profiles printed on that printer. This allows a rapid reprint of a series of labels or profiles that were damaged by a printer malfunction or other event.</td>
</tr>
<tr class="even">
<td>Local Possible Dosages</td>
<td>Free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.</td>
</tr>
<tr class="odd">
<td>Medication Instruction File</td>
<td>The MEDICATION INSTRUCTION file is used by Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion and intended use.</td>
</tr>
<tr class="even">
<td>Medication Order</td>
<td>A prescription.</td>
</tr>
<tr class="odd">
<td>Medication Profile</td>
<td>A list of all active or recently canceled or expired prescriptions for a patient sorted either by date, drug, or classification. Unlike the action profile, this profile is for information only and does not provide a signature line for a physician to indicate action to be taken on the prescription.</td>
</tr>
<tr class="even">
<td>Medication Routes File</td>
<td>The MEDICATION ROUTES file contains medication route names. The user can enter an abbreviation for each route to be used at the local site. The abbreviation will most likely be the Latin abbreviation for the term.</td>
</tr>
<tr class="odd">
<td>Med Route</td>
<td>The method in which the prescription is to be administered (e.g., oral, injection).</td>
</tr>
<tr class="even">
<td>NCCC</td>
<td>Acronym for National Clozapine Coordinating Center.</td>
</tr>
<tr class="odd">
<td>Non-Formulary Drugs</td>
<td>The medications that are defined as commercially available drug products, not included in the VA National Formulary.</td>
</tr>
<tr class="even">
<td>Non-VA Meds</td>
<td>Term that encompasses any Over-the-Counter (OTC) medications, Herbal supplements, Veterans Health Administration (VHA) prescribed medications but purchased by the patient at an outside pharmacy, and medications prescribed by providers outside VHA. All Non-VA Meds must be documented in patients’ medical records.</td>
</tr>
<tr class="odd">
<td>OneVA Pharmacy</td>
<td>Prescriptions that originated from another VistA instance other than the site dispensing the prescription.</td>
</tr>
<tr class="even">
<td>OPAI</td>
<td>Outpatient Pharmacy Automated Interface.</td>
</tr>
<tr class="odd">
<td>Order</td>
<td>Request for medication.</td>
</tr>
<tr class="even">
<td>Order Check</td>
<td>Order checks (drug-allergy/ADR interactions, drug-drug, duplicate drug, duplicate therapy, and dosing) are performed when a new medication order is placed through either the CPRS or Outpatient Pharmacy applications. They are also performed when medication orders are renewed, when Orderable Items are edited, or during the finishing process in Outpatient Pharmacy. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error.</td>
</tr>
<tr class="odd">
<td>Orderable Item</td>
<td>An Orderable Item name has no strength attached to it (e.g., Acetaminophen). The name with a strength attached to it is the Dispense drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="even">
<td>Partial Prescription</td>
<td>A prescription that has been filled for a quantity smaller than requested. A possible reason for a partial fill is that a patient is to return to the clinic in ten days, but the prescription calls for a thirty-day supply. Partials do count as workload but do not count against the total number of refills for a prescription.</td>
</tr>
<tr class="odd">
<td>Payer</td>
<td>In health care, an entity that assumes the risk of paying for medical treatments. This can be an uninsured patient, a self-insured employer, or a health care plan or Health Maintenance Organization (HMO).</td>
</tr>
<tr class="even">
<td>Pending Order</td>
<td>A pending order is one that has been entered by a provider through CPRS without Pharmacy finishing the order. Once Pharmacy has finished the order, it will become active.</td>
</tr>
<tr class="odd">
<td>Pharmacy Narrative</td>
<td>OUTPATIENT NARRATIVE field that may be used by pharmacy staff to display information specific to the patient.</td>
</tr>
<tr class="even">
<td>Polypharmacy</td>
<td>The administration of many drugs together.</td>
</tr>
<tr class="odd">
<td>POE</td>
<td>Acronym for Pharmacy Ordering Enhancements (POE) project. Patch PSO*7*46 contains all the related changes for Outpatient Pharmacy.</td>
</tr>
<tr class="even">
<td>Possible Dosages</td>
<td>Dosages that have a numeric dosage and numeric dispense units per dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to the DRUG file. The DRUG file entry must have a numeric strength, and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.</td>
</tr>
<tr class="odd">
<td>Prescription</td>
<td>This term is now referred to throughout the software as medication orders.</td>
</tr>
<tr class="even">
<td>Prescription Status</td>
<td><p>A prescription can have one of the following statuses.</p>
<p>Active - A prescription with this status can be filled or refilled.<br />
Canceled - This term is now referred to throughout the software as Discontinued. (See Discontinued.)<br />
Discontinued - This status is used when a prescription was made inactive either by a new prescription or by the request of a physician.<br />
Discontinued (Edit) - Discontinued (Edit) is the status used when a medication order has been edited and causes a new order to be created due to the editing of certain data elements.<br />
Deleted - This status is used when a prescription is deleted. Prescriptions are no longer physically deleted from the system but marked as deleted. Once a prescription is marked deleted no access is allowed other than view.<br />
Expired - This status indicates the expiration date has passed.</p>
<p>*Note: A prescription that was canceled or has expired more recently than the date specified by the cutoff date, typically 120 days in the past, can still be acted upon.<br />
Hold - A prescription that was placed on hold due to reasons determined by the Pharmacist.<br />
Non-verified - There are two types of non-verified statuses. Depending on a site parameter, prescriptions entered by a technician do not become active until a pharmacist reviews them. Until such review, they remain non-verified and cannot be printed, canceled, or edited except through the Verification menu.<br />
The second non-verified status is given to prescriptions when a drug/drug interaction is encountered during the new order entry or editing of a prescription.<br />
Pending - A prescription that has been entered through OERR.<br />
Refill - A second or subsequent filling authorized by the provider.<br />
Suspended - A prescription that will be filled at some future date.</p></td>
</tr>
<tr class="odd">
<td>Progress Notes</td>
<td>A component of Text Integration Utilities (TIU) that can function as part of CPRS.</td>
</tr>
<tr class="even">
<td>Provider</td>
<td>The person who authorized an order. Only users identified as providers who are authorized to write medication orders may be selected.</td>
</tr>
<tr class="odd">
<td>Reprinted Label</td>
<td>Unlike a partial prescription, a reprint does not count as workload.</td>
</tr>
<tr class="even">
<td>Questionnaire</td>
<td>An entry in the DUE QUESTIONNAIRE file. This file entry contains the set of questions related to a DUE as well as the drugs being evaluated.</td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>The frequency by which the doses are to be administered, such as Q8H, BID, NOW, etc.</td>
</tr>
<tr class="even">
<td>SDA</td>
<td>Summary Document Architecture</td>
</tr>
<tr class="odd">
<td>Sig</td>
<td>The instructions printed on the label.</td>
</tr>
<tr class="even">
<td>Significant</td>
<td>The potential for harm is either rare or generally known so that it is reasonable to expect that all prescribers have taken this information into account.</td>
</tr>
<tr class="odd">
<td>SOAP</td>
<td>Simple Object Access Protocol</td>
</tr>
<tr class="even">
<td>Speed Actions</td>
<td>See Actions.</td>
</tr>
<tr class="odd">
<td>Suspense</td>
<td>A prescription may not be able to be filled on the day it was requested. When the prescription is entered, a label is not printed. Rather, the prescription is put in the RX SUSPENSE file to be printed at a later date.</td>
</tr>
<tr class="even">
<td>Third (3rd) Party Claims</td>
<td>Health care insurance claims submitted to an entity for reimbursement of health care bills.</td>
</tr>
<tr class="odd">
<td>Time In</td>
<td>This is the time that the patient's name was entered into the computer.</td>
</tr>
<tr class="even">
<td>Time Out</td>
<td>This is the time that the patient's name was entered on the bingo board monitor.</td>
</tr>
<tr class="odd">
<td>TIU</td>
<td>Text Integration Utilities: a package for document handling, that includes Consults, Discharge summary, and Progress Notes, and will later add other document types such as surgical pathology reports. TIU components can be accessed for individual patients through the CPRS, or for multiple patients through the TIU interface.</td>
</tr>
<tr class="even">
<td>Titration</td>
<td>Titration is the process of gradually adjusting the dose of a medication until optimal results are reached.</td>
</tr>
<tr class="odd">
<td>TRICARE</td>
<td><p>TRICARE is the uniformed service health care program for: active-duty service members and their families retired service members and their families’ members of the National Guard and Reserves and their families’ survivors, and others who are eligible.</p>
<p>There are differences in how prescriptions for TRICARE beneficiaries are processed versus how prescriptions are processed for veterans.</p></td>
</tr>
<tr class="even">
<td>Units per Dose</td>
<td>The number of Units (tablets, capsules, etc.) to be dispensed as a Dose for an order. Fractional numbers will be accepted for medications that can be split.</td>
</tr>
<tr class="odd">
<td>VDIF</td>
<td>Veterans Data Information Exchange</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Acronym for Veterans Health Information Systems and Technology Architecture, the new name for Decentralized Hospital Computer Program (DHCP).</td>
</tr>
<tr class="odd">
<td>Wait Time</td>
<td>This is the amount of time it took to fill the prescription. It is the difference between Time In and Time Out. For orders with more than one prescription, the wait time is the same for each.</td>
</tr>
</tbody>
</table>