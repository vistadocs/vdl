---
title: MPI HL7 Interface Specification
doc_type: INT
doc_label: Interface Specification
doc_layer: anchor
doc_subject: MPI HL7
app_code: MPIF
app_name: Master Patient Index
section: INF
app_status: active
pkg_ns: MPIF
patch_ver: 1.0
patch_id: MPIF*1.0
group_key: "MPIF:MPIF:1.0"
file_numbers: 
  - 13
  - 799
security_keys: []
menu_options: 23
description: 
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - table
  - patient
  - message
  - sent
  - contents
  - span
  - segment
page_count: 0
word_count: 79430
section_count: 73
table_count: 95
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/mpif_1_0is.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/mpif_1_0is.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=16"
---

---
title: |
  Master Patient Index (MPI)

  Version 1.0

  HL7 Interface Specifications
---

![](mpi-hl7-interface-specification/001.png)

April 1999

Office of Information and Technology (OIT)

Revision History

<span id="_Toc3901207" class="anchor"></span>Table i. Documentation revision history

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3/2019</td>
<td><p>Modified some of the HL7 message examples to include the Name Components that are sent in the OBX segment in ADT-A08 messages sent from VistA to MPI and the ERR segment in ACK-A31 application acknowledgement messages sent from VistA to MPI.</p>
<p><em>For details, see the entry in this table on the following pages dated 10/2014, ClearQuest Request MVI 3454, Patch MPI*1.0*95.</em></p></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>10/2018</td>
<td><p>Documentation updates are listed by patch designation and RTC Story.</p>
<p>Companion Patches MPI*1.0*123, DG*5.3*967, RG*1.0*70, and MPIF*1.0*68/Story #783361 (VETS360)</p>
<p>Security Level values added to Sequence 5 in the “Table 3‑34. OBX: Observation/Result, HL7 attributes”</p>
<ul>
<li><p>Security Level</p>
<ul>
<li><blockquote>
<p>0 = Non Sensitive</p>
</blockquote></li>
<li><blockquote>
<p>1 = Sensitive</p>
</blockquote></li>
</ul></li>
</ul>
<p>The following OBX segment example entries added to “Figure 2‑61. ADT-A08 Update Patient Information msg: Sent <em><u>to</u></em> MVI <em><u>from</u></em> VistA”</p>
<ul>
<li><p>OBX^^CE^SECURITY LEVEL^^0~NON-SENSITIVE~L^^^^^^F</p></li>
<li><p>OBX^^CE^SECURITY REASON^^VET~Veteran~L^^^^^^F Only from CORP and BIRLS</p></li>
</ul>
<p>The following OBX segment example entry added to “Figure 2‑65. ADT-A31 Update Person Information msg: Sent from VistA to MVI”</p>
<ul>
<li><p>OBX^^CE^SECURITY LEVEL^^0~NON-SENSITIVE~L^^^^^^F</p></li>
</ul>
<p>The following OBX segment example entries added to Figure 2‑85. ADT-A31 Update Person Information msg: Sent <em><u>from</u></em> the MVI <em><u>to</u></em> PSIM”</p>
<ul>
<li><p>OBX^19^CE^SECURITY LEVEL^^V_0~Not Sensitive~L^^^^^^F</p></li>
<li><p>OBX^20^CE^SECURITY REASON^^NVE~Non-VBA VA Employee~L^^^^^^F</p></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>4/2017</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story.</p>
<p>Patch MPI*1*113/RTC Story 455464: “Add new field in HL7 messaging sent from MPI to VistA and PSIM on MPI side.”</p>
<ul>
<li><p>The following value was added to “Table 3‑39. HL7 Table 0200: Name type:”</p></li>
</ul>
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N</td>
<td>Nickname (Preferred Name)</td>
</tr>
</tbody>
</table>
<ul>
<li><blockquote>
<p>PREFERRED NAME field added to the PID Segment, shown in “</p>
</blockquote></li>
</ul>
<p>MSH^~|\&amp;^RG ADT^984~DAYTSHR.FO-REDACTED.GOV~DNS^RG ADT^200M~TLMPI.FO-REDACTED.GOV~DNS^20070625100545-0400^^ADT~A08^98459402631^T^2.4^^^AL^AL^USAEVN^^^^^35198~MVIPATIENT~PATIENT1~~~~~~USVHA&amp;&amp;0363~L~~~NI~VA FACILITY ID&amp;984&amp;L^^984</p>
<p><strong>PID</strong>^1^1010005729V870655^1010005729V870655~~~USVHA&amp;&amp;0363~NI~VA FACILITY ID&amp;200M&amp;L|<strong>666010255</strong>~~~USSSA&amp;&amp;0363~SS~VA FACILITY ID&amp;984&amp;L|552151092~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;984&amp;L|<strong>666010256</strong>~~~USSSA&amp;&amp;0363~SS~VA FACILITY ID&amp;984&amp;L~~20070625|1010002493V683214~~~USVHA&amp;&amp;0363~NI~VA FACILITY ID&amp;984&amp;L~~20070625^^<strong>MVISQA~PIDTSTB</strong> MID~SFIX~~~~L|PREFERRED NAME~~~~~~N|<strong>ALIASLNA~ALIASFNA</strong>~~~~~A^MOMSMITH~~~~~~M^19800202^M^^""^222 PERM TST ADDRESS~TAMPA, FL~""~""~""~""~VAB1~""~""|~~TAMPA~FL~~~N|<strong>333 CONFIDENTIAL ADDRESS</strong>~""~<strong>SAINT PETERSBURG~FL~33716</strong>~""~VACAA~""~""~~~20070625&amp;20080625^""^111-1111~PRN~PH|222-2222~WPN~PH|<strong>555-5555</strong>~ORN~<strong>CP</strong>|<strong>666-6666</strong>~BPN~<strong>BP</strong>|~NET~INTERNET~<strong>ONE.SQA@MPI.COM</strong>^222-2222^555)555-5555~VACPN~PH^""^""^^666010255^^^""^TAMPA FL^N^^^^^20150512^Y^^^</p>
<p>PV1^1^O^""^^^^^^^^^^^^^^^ACTIVE DUTY^^^^^^^^^^^^^^^^^^^^^^^^^^20070625^^^^^^1535241</p>
<p>ZPD^1^^^^^^^^^^^^^^^^""^^^^""^^^^^^^^^^^^^""</p>
<p>ZSP^1^0^""^""^""^""^""^""^^""</p>
<p>ZEL^1^""^""^""^""^""^""^1^ACTIVE DUTY^""^""^""^""^""^""^""^""^""^""^""^""^""</p>
<p>ZCT^1^1^""^""^""^""^""^""^""^1^1^""^""^""^""^""^""</p>
<p>ZFF^2^.01;.02;.03;.092;.093;.09;.2403;.301;1901;391;.111;.112;.131;.132;</p>
<ul>
<li><blockquote>
<p>Figure 3‑2. Sample Message Patient Identification PID Segment”</p>
</blockquote></li>
</ul>
<p>Patch MPI*1*113/RTC Story 445322: “Synchronize Date of Death to VBA.”</p>
<ul>
<li><p>The following OBX segment example entry was added to “Figure 2‑85. ADT-A31 Update Person Information msg: Sent <em><u>from</u></em> the MVI <em><u>to</u></em> PSIM:”</p></li>
</ul>
<p>OBX^14^TS^NEW DATE OF DEATH STATUS^^20170107^^^^^^P^</p>
<ul>
<li><p>Added NEW DATE OF DEATH STATUS fields to “Table 3‑34. OBX: Observation/Result, HL7 attributes.”</p></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>1/2017</td>
<td><p>Patches MPI*1.0*108 and MPI*1.0*110 documentation updates:</p>
<ul>
<li><blockquote>
<p>RTC Story #323004: Enhance processing of Date of Death from Correlated Lines of business.</p>
</blockquote></li>
<li><blockquote>
<p>RTC Story #339758: MVI sends all LOB systems the DOD and related information.</p>
</blockquote></li>
<li><blockquote>
<p>RTC Story #327993: Add OBX for stopping catastrophic edit check in processing A08 messages.</p>
</blockquote></li>
</ul>
<p>Other updates: Removed all references to RSA in the message structures and narratives (old scheduling redesign - no longer active).</p></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>3/2016</td>
<td><p>Patch MPI*1.0*106 documentation updates, RTC Story #172813.</p>
<p>New Veteran Benefits Administration(VBA)/CORP (200CORP, 200BRLS) fields (value = Y/N) sent via A08 HL7 message, SEQ 3 - Observation Identifier field. Included in <em>“ Table 3‑34. OBX: Observation/Result, HL7 attributes.”</em></p>
<p><strong>Rule text in HL7 OBX segment Mumps Variable with Value</strong></p>
<p>VBA 101 UPDATE ARRAY("VBA101Update")=VAL</p>
<p>SSN VERIFICATION STATUS  ARRAY("SSNStatus")=VAL</p>
<p>VBA SHARE UPDATE ARRAY("VBAShareUpdate")=VAL</p>
<p>OPEN CLAIM INDICATOR ARRAY("VBAOpenClaimInd")=VAL</p>
<p>AUTHORIZED AWARD INDICATOR ARRAY("VBAAuthAwardInd")=VAL</p>
<p><strong>OBX segment Text Mumps Variable with Value</strong></p>
<p>COMPARE INDICATED POTENTIAL MISMATCH ARRAY("CompIndPotMismatch")=VAL</p>
<p>NOTE: If “Y,” is sent via OBX text (above), <em><u>only</u></em> the correlation view will be updated, and a 'Potential Mismatch Task'(#257) and a new milestone 'MVI_CORRELATION_UPDATE_POTENTIAL_MISMATCH' will be logged.</p></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>12/2015</td>
<td>Patch DG*5.3*915 documentation update, only. Updated glossary entry for Registration Process.</td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>9/2015</td>
<td><p>Documentation updates, Patches MPI*1*102, MPIF*1.0*61 and DG*5.3*915:</p>
<p>(RTC Story #173993)</p>
<ul>
<li><p>PERSON TYPE values were added to the OBX Segment, shown in “Table 3‑34. OBX: Observation/Result, HL7 attributes”:</p></li>
</ul>
<ul>
<li><blockquote>
<p>SEQ 2, element name: Value Type</p>
</blockquote></li>
<li><blockquote>
<p>SEQ 3, element name: Observation Identifier</p>
</blockquote></li>
<li><blockquote>
<p>SEQ 5, element name: Person Type (multiple definitions added)</p>
</blockquote></li>
</ul>
<ul>
<li><p>PERSON TYPE added to the following message examples:</p></li>
</ul>
<ul>
<li><p><em>“</em>Figure 2‑61. ADT-A08 Update Patient Information msg: Sent to MVI from VistA<em>”</em></p></li>
</ul>
<p>OBX^^CE^PERSON TYPE^^VET~VETERAN~L^^^^^^F</p>
<p>OBX^^CE^PERSON TYPE^^DEP~DEPENDANT~L^^^^^^F</p>
<ul>
<li><blockquote>
<p>“Figure 2‑85. ADT-A31 Update Person Information msg: Sent <em><u>from</u></em> the MVI <em><u>to</u></em> PSIM”</p>
</blockquote></li>
</ul>
<blockquote>
<p>OBX^11^CE^PERSON TYPE^^VET~VETERAN~L^^^^^^F</p>
<p>OBX^11^CE^PERSON TYPE^^DEP~DEPENDENT~L^^^^^^F</p>
</blockquote>
<p>(RTC Story #173194)</p>
<ul>
<li><p>Self-Identified Gender added to the OBX Segment, passed from the Primary View in in the following two messages:</p></li>
</ul>
<ul>
<li><blockquote>
<p>“Figure 2‑69. ADT-A31 Update Person Information msg: Sent to VistA from MVI”</p>
</blockquote></li>
<li><blockquote>
<p>“Figure 2‑82. ADT-A31 Update Person Information msg: Sent to VistA from MVI”</p>
</blockquote></li>
</ul>
<blockquote>
<p>OBX^2^CE^SELF ID GENDER^^M~Male~L</p>
</blockquote>
<p>(RTC Story #170758)</p>
<ul>
<li><p>The fields: Death Indicator (PID Segment) and Death Score (OBX Segment) were added to “Figure 2‑72. ADT~A31 HL7 Message sent <em><u>from</u></em> the MVI for Primary View sync with PSIM”</p></li>
</ul>
<blockquote>
<p>PID^1^ … ^20141125^Y^^^</p>
<p>OBX^2^CE^AUTHORITY SCORE^^""~------------760~L^^^^^F</p>
</blockquote>
<ul>
<li><p>AUTHORITY SCORE values were added to the OBX Segment, shown in “Table 3‑34. OBX: Observation/Result, HL7 attributes”</p></li>
</ul>
<ul>
<li><blockquote>
<p>SEQ 2, element name: Value Type</p>
</blockquote></li>
<li><blockquote>
<p>SEQ 3, element name: Observation Identifier</p>
</blockquote></li>
<li><p>SEQ 5, element name: Person Type (multiple definitions added)</p></li>
</ul>
<ul>
<li><p>Patient Death Date (DOD) and Patient Death Indicator were added to “</p></li>
</ul>
<p>MSH^~|\&amp;^RG ADT^984~DAYTSHR.FO-REDACTED.GOV~DNS^RG ADT^200M~TLMPI.FO-REDACTED.GOV~DNS^20070625100545-0400^^ADT~A08^98459402631^T^2.4^^^AL^AL^USAEVN^^^^^35198~MVIPATIENT~PATIENT1~~~~~~USVHA&amp;&amp;0363~L~~~NI~VA FACILITY ID&amp;984&amp;L^^984</p>
<p><strong>PID</strong>^1^1010005729V870655^1010005729V870655~~~USVHA&amp;&amp;0363~NI~VA FACILITY ID&amp;200M&amp;L|<strong>666010255</strong>~~~USSSA&amp;&amp;0363~SS~VA FACILITY ID&amp;984&amp;L|552151092~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;984&amp;L|<strong>666010256</strong>~~~USSSA&amp;&amp;0363~SS~VA FACILITY ID&amp;984&amp;L~~20070625|1010002493V683214~~~USVHA&amp;&amp;0363~NI~VA FACILITY ID&amp;984&amp;L~~20070625^^<strong>MVISQA~PIDTSTB</strong> MID~SFIX~~~~L|PREFERRED NAME~~~~~~N|<strong>ALIASLNA~ALIASFNA</strong>~~~~~A^MOMSMITH~~~~~~M^19800202^M^^""^222 PERM TST ADDRESS~TAMPA, FL~""~""~""~""~VAB1~""~""|~~TAMPA~FL~~~N|<strong>333 CONFIDENTIAL ADDRESS</strong>~""~<strong>SAINT PETERSBURG~FL~33716</strong>~""~VACAA~""~""~~~20070625&amp;20080625^""^111-1111~PRN~PH|222-2222~WPN~PH|<strong>555-5555</strong>~ORN~<strong>CP</strong>|<strong>666-6666</strong>~BPN~<strong>BP</strong>|~NET~INTERNET~<strong>ONE.SQA@MPI.COM</strong>^222-2222^555)555-5555~VACPN~PH^""^""^^666010255^^^""^TAMPA FL^N^^^^^20150512^Y^^^</p>
<p>PV1^1^O^""^^^^^^^^^^^^^^^ACTIVE DUTY^^^^^^^^^^^^^^^^^^^^^^^^^^20070625^^^^^^1535241</p>
<p>ZPD^1^^^^^^^^^^^^^^^^""^^^^""^^^^^^^^^^^^^""</p>
<p>ZSP^1^0^""^""^""^""^""^""^^""</p>
<p>ZEL^1^""^""^""^""^""^""^1^ACTIVE DUTY^""^""^""^""^""^""^""^""^""^""^""^""^""</p>
<p>ZCT^1^1^""^""^""^""^""^""^""^1^1^""^""^""^""^""^""</p>
<p>ZFF^2^.01;.02;.03;.092;.093;.09;.2403;.301;1901;391;.111;.112;.131;.132;</p>
<ul>
<li><p>Figure 3‑2. Sample Message Patient Identification PID Segment”</p></li>
</ul>
<ul>
<li><p><strong>PID</strong>^1^ … TAMPA FL^N^^^^^20150512^Y^^^</p></li>
</ul>
<ul>
<li><p>Updated the VistA description in “Table 3‑37. PID: Patient Identification, HL7 attributes” in SEQ 30, element name: “Patient Death Indicator”</p></li>
</ul>
<ul>
<li><p><em>“Only sent from the MPI in A31 message to PSIM.”</em></p></li>
</ul>
<ul>
<li><p>Updated the field definition in: “PID-30 Patient Death Indicator (ID) 00741”</p></li>
</ul>
<ul>
<li><p><em>“This field indicates whether the patient is deceased. Refer to HL7 Table 0136 – Yes/No Indicator for valid values.”</em></p></li>
</ul>
<ul>
<li><p>Updated glossary entry for Registration Process.</p></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>3/2015</td>
<td><p>Patch MPI*1.0*99 documentation updates:</p>
<p>ClearQuest Request MVI 4599:</p>
<ul>
<li><blockquote>
<p>HC IdM requested an enhancement to TK PV Audit to display when an update to the Primary View originates from a PCE task being dispositioned.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The routine MPIRPC11 associated with RPC: MPI UPDATE PRIMARY VIEW was modified to pass an optional input array value "UserOption" containing the TK Task Number, if defined, to routine MPIA31H for transmission to PSIM in the OBX segment of the A31 HL7 update message. Example:</p>
</blockquote></li>
</ul>
<blockquote>
<p>OBX^^CE^USEROPTION^^TK Task Number</p>
</blockquote>
<p>ClearQuest Request MVI 4778:</p>
<ul>
<li><blockquote>
<p>HC IdM requested support for exchanging Social Security Administrative (SSA) verification statuses (SSA Values) with DoD.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The A28 and A08 HL7 message OBX parser code was enhanced to parse the Social Security Administrative Verification Status value to the array subscript of ("SSAStatus").</p>
</blockquote></li>
<li><blockquote>
<p>The A31 HL7 message builder code to PSIM was enhanced to generate the OBX segment with the Social Security Administrative Verification Status value.</p>
</blockquote></li>
</ul></li>
</ul>
<p>ClearQuest Request MVI 4729 and ClearQuest Request MVI 4729:</p>
<ul>
<li><blockquote>
<p>The ADT-A19 HL7 message receiver code was enhanced to parse the ZEL, ZSP and OBX segments to extract/initialize the Veteran Y/N, Patient Type, Period of Service and Self-Identified Gender values. The corresponding VistA changes were exported in Patch DG*5.3*902.</p>
</blockquote></li>
</ul>
<p>ClearQuest Request MVI 4778:</p>
<ul>
<li><blockquote>
<p>Filtering on person types is an interim solution to enhance MVI to support the exchange of identities with DoD for Veteran population. This is preliminary work for Increment 14. Identity Interoperability Person Type value is parsed to the array subscript of ("IIPType") in the A28 and A08 HL7 message OBX code. The A31 HL7 message builder code to PSIM has been enhanced to generate the OBX segment with the Identity Interoperability Person Type value.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Additional changes for Increment 13:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Updated Index and Glossary.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>10/2014</td>
<td><p>Documentation updates:</p>
<p>ClearQuest Request MVI 2921, Patch MPI*1.0*95 and ClearQuest Request MVI 3467, Patch MPIF*1.0*59</p>
<ul>
<li><p>(1 of 2) The following changes were made to the ADT-A08 HL7 message to include the population of Self Identified Gender. <strong>NOTE:</strong> This can also be in ADT-A31 HL7 message. Only ADT-A08 was updated with this example.</p></li>
</ul>
<ul>
<li><blockquote>
<p>The <em>“ADT-A08 Update Patient Information msg: Sent to MVI from VistA”</em> HL7 msg example was updated to show the additional OBX Segment:</p>
</blockquote></li>
</ul>
<blockquote>
<p>OBX^^CE^[Observation Identifier]^^[Observation Value]</p>
</blockquote>
<ul>
<li><p>(2 of 2) The following sequence elements were updated in the OBX Segment, in the “OBX: Observation/Result, HL7 attributes” table:</p></li>
</ul>
<ul>
<li><blockquote>
<p>#2, Element Name: Value Type:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>CE = Self-Identified Gender</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>#3, Element Name: Observation Identifier:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>SELF ID GENDER</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>#5, Element Name: Observation Value can be:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>M for Male</p>
</blockquote></li>
<li><blockquote>
<p>F for Female</p>
</blockquote></li>
<li><blockquote>
<p>TM for Transmale/Transman/Female-to-Male</p>
</blockquote></li>
<li><blockquote>
<p>TF for Transfemale/Transwoman/Male-to-Female</p>
</blockquote></li>
<li><blockquote>
<p>O for Other</p>
</blockquote></li>
<li><blockquote>
<p>N for individual chooses not to answer</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>10/2014</td>
<td><p>Documentation updates:</p>
<p>ClearQuest Request MVI 3454, Patch MPI*1.0*95<br />
ClearQuest Request MVI 3453, Patch DG*5.3*876;<br />
ClearQuest Request MVI 3975, Patch MPIF*1.0*59<br />
ClearQuest Request MVI 3976, Patch RG*1.0*61</p>
<ul>
<li><blockquote>
<p>(1 of 2) The ADT-A08 HL7 message from VistA to MPI was changed to include in an OBX segment the Name Components stored in the Name Components file (#20) for the patient. The <em>“ADT-A08 Update Patient Information msg: Sent to MVI from VistA”</em> HL7 message example was updated to show the additional OBX segment:</p>
</blockquote></li>
</ul>
<p>OBX^^CE^NAME COMPONENTS^^[Patient .01 field value] ~[Family Name]~[Given Name]~[Middle Name]~[Suffix]~[Prefix]</p>
<ul>
<li><p>(2 of 2) The ACK-A31 HL7 Application Level Acknowledgement from VistA to MPI was changed to include an ERR segment that contains the Name Components stored in the Name Components file (#20) for the patient. The <em>“ADT-A31 Update Person Information msg: Application acknowledgement sent from VistA to MVI”</em> HL7 message examples were updated to show the additional ERR segment:</p></li>
</ul>
<p>ERR^~~~&amp;[Patient .01 field value]&amp;[Family Name]&amp;[Given Name]&amp;[Middle Name]&amp;[Suffix]&amp;[Prefix]</p></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>9/2014</td>
<td><p>Documentation updates:</p>
<p>ClearQuest Request MVI 3392, Patch MPI*1.0*97:</p>
<ul>
<li><p>Change was made to the following HL7 messages and to the OBX Segment to include the population of the ROI and IPP (processing of OBX segment) on creation of the correlation in either path:</p></li>
</ul>
<ul>
<li><blockquote>
<p>A28 Add New Record</p>
</blockquote></li>
<li><blockquote>
<p>A24 Add New Correlation</p>
</blockquote></li>
<li><blockquote>
<p>OBX—Observation/Result, HL7 Segment updates w/following sequences: 1, 3, and 5</p>
</blockquote></li>
</ul>
<p>Additional changes for Increment 12:</p>
<ul>
<li><blockquote>
<p>HC IdM recommended changes to name references: 1) MPI to MVI (where appropriate) and 2) Patient to Person (where appropriate).</p>
</blockquote>
<ul>
<li><blockquote>
<p>The term “Patient” is used when the reference is to VistA PATIENT file (#2). The “MPI” nomenclature is used to display these test data occurrences because the MPI component of the MVI interacts with the PATIENT file (#2). </p>
</blockquote></li>
<li><blockquote>
<p>All other references are made to “Person” and to the MVI (which overall includes the MPI, PSIM, and TK).</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>Housekeeping—Update to the following HL7 Msg examples:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>MFN-M05—Update Treating Facility msg: Received from MPI</p>
</blockquote></li>
<li><blockquote>
<p>MFN-M05—Update Treating Facility msg: Application acknowledgement sent to MPI</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>2/2014</td>
<td><p>ClearQuest Request MVI 3038, Patch DG*5.3*874</p>
<ul>
<li><blockquote>
<p>The <em><u>active</u></em> Veteran’s Health Identity Card (VHIC) number was added to the list of identifiers in the PID segment (PID-4) on the VistA side.</p>
</blockquote></li>
<li><blockquote>
<p>Format:</p>
</blockquote></li>
</ul>
<blockquote>
<p>[VIC Card #]~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;742V1&amp;L</p>
</blockquote>
<ul>
<li><blockquote>
<p>Example of VHIC number in PID-4 repeated twice for interoperability between DoD and VA because this patient has two active VHIC numbers:</p>
</blockquote></li>
</ul>
<blockquote>
<p>999~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;742V1&amp;L|999999~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;742V1&amp;L</p>
</blockquote></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>5/2013</td>
<td><p>ClearQuest Request MVI 1544, Patch MPI*1.0*92</p>
<ul>
<li><blockquote>
<p>Added field: PID-25   Birth order   (NM)   00128. This is the Multiple Birth Order, which is a number other than zero. This data only comes from DoD.</p>
</blockquote></li>
<li><blockquote>
<p>Updated organizational references in documentation.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>5/2012</td>
<td><p>IMPORTANT NOTE:</p>
<blockquote>
<p>The Version number 2.21 as it appeared on the title page and in the filename of this manual was removed. The correct version number of the MPI HL7 Interface Specification is v1.0, which is the same version number Master Patient Index software. This will only change if the software versioning is upgraded.</p>
</blockquote></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>5/2012</td>
<td><p>ClearQuest Request MVI 789, HL7 message MFN~M05 updates:</p>
<ul>
<li><blockquote>
<p>Assigning Authority and ID Type are parsed from MFE Segment for HL7 MFN~M05 v2.4 and v3.</p>
</blockquote></li>
<li><blockquote>
<p>Code modified to handle more than 245 characters in MFE segment.</p>
</blockquote></li>
<li><blockquote>
<p>Examples:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Figure 2‑92. MFN-M05 Update Treating Facility msg: Assigning Authority and Id Type are parsed from MFE segment for HL7 MFN~M05 v2.4 and v3.</p>
</blockquote></li>
<li><blockquote>
<p>Figure 2‑93. MFN-M05 Update Treating Facility msg: Assigning Authority and Id Type are parsed from MFE segment, more than 245 characters long, for HL7 MFN~M05 v2.4 and v3.</p>
</blockquote></li>
</ul></li>
</ul>
<p>HL7 segment updates:</p>
<ul>
<li><blockquote>
<p>ClearQuest Request MVI 789) MFE: Updated to handle HL 3.0 format for ID data. Examples in documentation.</p>
</blockquote></li>
<li><blockquote>
<p>ClearQuest Request MVI 937) PID 3: Added TIN and FIN fields to the Seq #3.</p>
</blockquote></li>
<li><blockquote>
<p>ClearQuest Request MPI_CR989 [MPI_CodeCR2338] -- correction from previous release) PID 32: Added catastrophic and non-catastrophic entries.</p>
</blockquote></li>
<li><blockquote>
<p>ClearQuest Request MVI 799) OBX Segment in A08 and A31 from VistA side (File #799) may include:</p>
</blockquote></li>
</ul>
<blockquote>
<p>OBX^^CE^OLDER RECORD^^Y</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>10/2011</td>
<td><p>ClearQuest requests MVI_531 and MVI_533 for Patch MPI*1*89:</p>
<p>Added the values:</p>
<ul>
<li><blockquote>
<p>ROI SIGNED</p>
</blockquote></li>
<li><blockquote>
<p>IPP LEVEL</p>
</blockquote></li>
</ul>
<p>to the OBX segment’s:</p>
<ul>
<li><blockquote>
<p>#3 “Observation Identifier”</p>
</blockquote></li>
<li><blockquote>
<p>#5 “Observation Value”</p>
</blockquote></li>
</ul>
<p>and to the example in the HL7 message A31, <em>“ADT/ACK—Update Person Information.”</em></p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/2011</td>
<td>Reviewed document then converted this document to a Section 508 compliant PDF.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>6/2011</td>
<td><p>MPI_CR2420 (MPI_CodeCR2437) Patch MPI*1*86—Headline: "Match and potential match thresholds returned in K22 query response"</p>
<ul>
<li><blockquote>
<p>Updated example in the QBP/RSP—Find Candidates (QBP) and Response (RSP) (events Q22 and K22) HL7 msg</p>
</blockquote></li>
<li><blockquote>
<p>Sequence QRI-3 Algorithm descriptor:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Updated User-defined Table 0393 – Match algorithms w/entry for INTIATE 7.5.</p>
</blockquote></li>
<li><blockquote>
<p>Added example of QRI Segment showing AUTO-LINK THRESHOLD and TASK THRESHOLD field values from the MPI PARAMETER file (#985.1) for sequence 3.</p>
</blockquote></li>
</ul>
<blockquote>
<p>Example:</p>
<p>102-145~INITIATE</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>3/2011</td>
<td><p>MPI_CR2342—Headline: "Add specific text to cover the RCP-2 Attended and Unattended expected values."</p>
<p>The field has been updated with the following explanation:</p>
<p>"The RCP-2 [Quantity limited request (CQ) 00031] field should be passed with a value of 1 for all unattended searches so that there will be one and only one matched record return. For attended searches that desire matched record and potential match record(s), the value of RCP-2 should be greater than 1."</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>9/2010</td>
<td><p>MPI_CR1772 (MPI_CodeCR1932)—Patch MPI*1*77: Changes have been made to VistA Health Level Seven (HL7) messaging to support a new process format for the Update Treating Facility (MFN~M05) HL7 message and for updating fields in the VistA TREATING FACILITY LIST file (#391.91)</p>
<p>Updates to new MFN~M05 message examples:</p>
<ul>
<li><blockquote>
<p>Retain old MFN~M05 message examples for My HealtheVet.</p>
</blockquote></li>
<li><blockquote>
<p>Include updated MFN~M05 message examples for all other applications.</p>
</blockquote></li>
</ul>
<p>Updated the Master File Entry Segment:</p>
<ul>
<li><blockquote>
<p>MFE-1: Added new value “MDC” in the Record-level Event Code Table 0180 for sending deactivated entries.</p>
</blockquote></li>
<li><blockquote>
<p>MFE-2: Explained and provided example of the use of incremental numbers used to define unique occurrences of the same Station Number when sent multiple times in the same HL7 message.</p>
</blockquote></li>
<li><blockquote>
<p>MFE-4: Included HL7 Table 0363 – for Assigning authority. Updated table with new entries USDOD and USVBA.</p>
</blockquote></li>
<li><blockquote>
<p>PID-3: Updated HL7 Table 0203 to include USDOD.</p>
</blockquote></li>
</ul>
<p><strong>NOTE:</strong> The Master File Update Acknowledgment (MFK~M05) response builder code has been modified to generate a response using the new format.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>5/2010</td>
<td>MPI_CR1716 (MPI_CodeCR1761): The PID builder in VistA was modified to include confidential phone number.  Confidential phone number is being added with Patch DG*5.3*754. This is needed for the VOA effort.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>11/2009</td>
<td>Final updates to documentation in preparation for national release via Patches MPI*1*62 and MPI*1*71.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>10/05/09</td>
<td>Updated the VA008─Religion Table adding the remainder of the entries included in the HL7 2.4 Standard.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>8/17/09</td>
<td>MPI_CodeCR1708: Healthcare Identity Management (HC IdM) name change to Healthcare Identity Management (HC IdM).</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>12/30/08</td>
<td><p>MPI_CR960(MPI_CodeCR1474: PID segment in HL7 spec for ethnicity is not documented correctly in PID-22 Ethnic group (CE) 00125. This is being released with Patch MPI*1*62. Correction as follows:</p>
<blockquote>
<p>H Hispanic or Latino</p>
<p>N Not Hispanic or Latino</p>
<p>U Unknown by Patient</p>
<p>D Declined to Answer</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>11/01/08</td>
<td><p>MPI_CR1264 (MPI_CodeCR1274): New values and updated value in File #13 Religion for released with Patch MPI*1*62.</p>
<p><strong>NOTE:</strong> Patch DG*5.3*782 modified the entries in the Religion file (#13) and added new fields.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>10/30/08</td>
<td><p>MPI_CR1362(MPI_CodeCR1473): Corrected the field name listed below. Released with Patch MPI*1*62.</p>
<ul>
<li><blockquote>
<p><strong>From:</strong><br />
ZPD-10 POW Status Indicated?</p>
</blockquote></li>
<li><blockquote>
<p><strong>To:<br />
</strong>ZPD-17 POW Status Indicated?</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>10/30/08</td>
<td><p>MPI_CR1361(MPI_CodeCR1472): Update OBX Segment, Seq #5 SSN VERIFICATION values to add codes listed below. Released with Patch MPI*1*62.</p>
<blockquote>
<p>0-New Record</p>
<p>1-In-Process</p>
<p>2-Invalid Per SSA</p>
<p>3-Resent to SSA,</p>
<p>4-Verified</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>10/06/08</td>
<td><p>Updates submitted by Danny Reed released with Patch MPI*1*62:</p>
<ul>
<li><blockquote>
<p>Change Request MPI_CR1038(MPI_CodeCR1469): 3.1.1.1.3 - Enhancement to MPI VQQ Interface Specification</p>
</blockquote></li>
<li><blockquote>
<p>Change Request MPI_CR1039(MPI_CodeCR1470): 3.1.1.1.4 - Enhancement to MPI QBP/Q22 FindCandidate Interface Specification</p>
</blockquote></li>
<li><blockquote>
<p>Change Request MPI_CR1041(MPI_CodeCR1471): 3.1.1.2.1 - Enhancement to MPI RSP/K22 FindCandidate Interface Specification</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/13/07</td>
<td><p>Updated A08 description to show PV1 as a required segment.</p>
<p>Update PV1 description to show that VistA sends no value to patient class but MPI will send N.</p>
<p>Update examples for A19 and A31 to show PV1 segment being sent.</p>
<p>QRD, seq 7 in A19 (RD and 1) were reversed.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>10/12/07</td>
<td>Updated PID segment, Seq 32 to reflect that "N" is mapped to "R" before sending to PSIM</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>8/7/07</td>
<td>Updated the MSA and ERR segments to note PSIM difference. Including an example A31 application ack with an ERR segment.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>7/20/07</td>
<td>Updated the OBX segment, sequence #2 and the PV2 segment, sequences #8, #14, and #46. Also added field definition for PV2, sequence #46.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>6/25/07</td>
<td>Added PID example. Re-introduced pink font to show changes. Previously content marked for deletion was deleted as per Danny Reed. Reformatted examples. Recompiled TOC and Index entries. Made other content changes based on feedback from Cindy Heuer.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/22/07</td>
<td><p>In Chapter 2, Trigger Events and Definitions, item "Update to fields on an existing MPI entry" (4<sup>th</sup> row in the first table), please change (RSA will still get the A08 message for these processes) to (RSA will still get the A08 message for <strong>their</strong> processes)</p>
<p>NOTE: As of 7/22/2016 RSA referenced have been removed from the manual. RSA is no longer active.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>6/22/07</td>
<td>Section 2.12 has Example 2, then Example 3, but no Example 1 preceding them. Changed Example 2 to be 1 and 3 to be 2</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/22/07</td>
<td><p>Adding the following statement to the introduction paragraph.</p>
<p>There are references in this document to the VistA HL7 package enhancement known as HLO which stands for HL7 Optimized, so from this point forward this will be referenced with the acronym HLO.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>6/22/07</td>
<td><p>Changed the following references:</p>
<p>In section 2.4 example #5 and in section 2.7 example #2 changed the reference to HLO to be via HLO instead of HLO Message.</p>
<p>Example: Message FROM the MPI TO PSIM via HLO</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/22/07</td>
<td>Added additional information in the table of identifiers in Section 3.15 PID-3 to identify the Temporary, Permanent and Deactivated ICN ID State difference based on effective and expiration dates</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>1/19/07</td>
<td>Updating Chapter 2 table and examples of messages.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>11/13/06</td>
<td>Adding HLO differences to the MSH segment. Providing HLO examples for the A43, A24 and A31 messages</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>7/27/06</td>
<td><p>Making changes to support primary view:</p>
<p>EVN segment for A31 messages will have Seq #2 be the date last updated from 985 or 985.5 depending upon the type of update (primary view or correlation)</p>
<p>OBX segment added to A31 message for the sending of the SSN Verification Status field.</p>
<p>PID segment, adding ID State for the ICN will be passed in PID 3 by populating the effective date to indicate Permanent, by populating the expiration date to indicate Deactivated and with neither effective or expiration date to indicate that the ID State is Temporary.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>5/15/06</td>
<td>Q22 query updated to include additional parameters for searching</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/24/06</td>
<td>Implemented feedback based on a review of the VA HL7 Tables (Chapter 4 in the documentation) by HSD&amp;D Message Administration, M&amp;IS. Also, general edits to grammar, punctuation, formatting, captions, and re-indexed the manual.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>4/04/06</td>
<td>Updated OBX segment field 5 Observed Value for changes to SSN Verification Status values.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/04/06</td>
<td><p>Section 2.4</p>
<p>1. Updated Example 3 ADT-A24 description to include reference to the local ID and ICN in the captured message</p>
<p>Section 2.6</p>
<p>1. Updated the A40 Capture to include the DFN in the MRG segment as well as 200M when referencing a National ICN.</p>
<p>Section 2.8</p>
<p>1. Updated the A04 captured with 200M when referencing National ICN</p>
<p>Section 2.9</p>
<p>1. Updated the A08 captured with 200M when referencing National ICN</p>
<p>Section 2.12</p>
<p>1. Updated the A31 captured with 200M when referencing National ICN</p>
<p>Section 2.14</p>
<p>1. Updated the A40 captured with 200M when referencing National ICN</p>
<p>2. Updated Example 1 and 2 to include a valid ICN, it appeared that the ICN that was in the capture had been scrubbed erroneously.</p>
<p>Section 3.10</p>
<p>1. Removed note on MSA-3</p>
<p>2. Updated description on MSA-1 to include when an AA, AE and AR should be passed.</p>
<p>Section 3.13</p>
<p>1. Replaced OBX-5 table description t reference to the VUID to internal value</p>
<p>Section 3.15</p>
<p>1. Updated the PID-3 table to separate Deprecated ICN reference to local and national</p>
<p>2. Updated table PID-11 to include VAB4 in the table listing.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>3/31/06</td>
<td>Updating PID Segment for inclusion of SSN Verification Status, Pseudo SSN Reason. Including a note about encoding characters and HL7 delimiters being included in the HL7 messages. Updating examples to ensure that Place of Birth State and the State address fields are shown as the state code and not completely spelt out, to be in line with the standard. 200M is listed as the authoritative source when the National ICN is passed in the PID segment. Updating PID to include field 32 for Identity Reliability Code.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>1/23/06</td>
<td>Updating PID segment for inclusion of bad address indicator, foreign address, confidential address and category, alias SSN, and change assigning authority on national ICNs. Add Pager #, cell phone #, and e-mail address and work phone into PID-13. These are related to the MPI Changes 3 project.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>11/18/05</td>
<td><p>Updated all examples for messaging. Added appendix for subscribing applications. Updated section 1.1</p>
<p>Edits to grammar, punctuation, and formatting.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>9/26/05</td>
<td><p>Add Section 2.16 and to the trigger events table ADT-A37 to support the Unlink of the MyHealtheVet project</p>
<p>Removed the sections column in the messages and trigger events table in section 2.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/10/05</td>
<td><p>Update the ADT-A24 messages figure 2.9, 2.13 and 2.14 to move the PD1 segment between PID1 and PID2</p>
<p>This correction was made as part of the MPI*1*35 patch</p>
<p>Modified the MFN-M05 figure 2-37 to pass the AL instead of NE in the MFI segment.</p>
<p>Also updated Figure titled: "A24—Link Patient Information message example" to include the ICN history entries with the date (not the time) that ICN became inactive.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>6/01/05</td>
<td><p>Updated references of the national ICN to use the MPI's station# of 200M.</p>
<p>Also removed the repeatable symbols off of the ADT-A43 message.</p></td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>5/31/05</td>
<td><p>Included ADT-A24 examples of the resolution of an MPI duplicate:</p>
<ul>
<li><blockquote>
<p>First form w/top level ICN value</p>
</blockquote></li>
<li><blockquote>
<p>Second form w/all identifiers</p>
</blockquote></li>
</ul>
<p>Also corrected the A28 Add Patient msg example to delete some repeated ICNs in the PID^1 and PID^2 segments.</p></td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>5/06/05</td>
<td>Updated the QPD segment table to include sequence QPD-6.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>4/15/05</td>
<td>Updated the ZCT, ZEL, ZEM, and ZPD segments, and corrected the patient DFN to "271" in the QPD^Q22 sequence of Figure 2‑31.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/13/05</td>
<td>Updated sequences 2, 3, and 4 in the ZEL―VA Specific Patient Eligibility segment.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>4/13/05</td>
<td>Incorporated the dfn changes to the ADT-A43 messaging</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>2/04/05</td>
<td><p>Accepted past updates.</p>
<p>In section 2.0 added hyperlinks to the messages. Also change the heading on the different ADT-A31 message constructs so that each implementation can be easily identified.</p></td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>12/17/04</td>
<td>Incorporated all feedback from developers (Danny Reed and Chris Chesney) and make final edits for release to the VistA Documentation Library (VDL).</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>10/28/04</td>
<td>Review and update</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>10/27/04</td>
<td>Updated to include PIMS segments (i.e. AL1, NK1, OBX &amp; Z* (ZCT, ZEL, ZEM, ZFF, ZPD, ZSP), including sequence translations for each. (Changes still pending.)</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>10/30/03</td>
<td>ZPD segments added to messages. Segments sent with messages updated to include all Z-Segments.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>8/01/03</td>
<td>Updated PID segment.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>5/14/03</td>
<td>No content changes; made minor format changes only (e.g., table/figure numbering scheme, format of "VistA").</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>2/04/03</td>
<td>Reformatted document to follow the SS Technical Writers Style Guide &amp; SOP. Also, updated broken links and clarified text/reference ambiguities.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>10/29/02</td>
<td>Made minor modifications and formatting on message examples.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>10/29/02</td>
<td>Formatting changes to document.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>10/21/02</td>
<td>Made some adjustments to the ADT-A19 QRD information.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>10/15/02</td>
<td>Final revisions, organization, and adding of CMOR Change messages and Query messages.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>10/07/02</td>
<td>Adding MFN-M05.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>7/19/02</td>
<td>Added ADT-A01, A03, and A37 HL7 Messages.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>3/18/02</td>
<td>Create Interface Analysis document and begin process of gathering "raw materials" for specifications.</td>
<td>Master Patient Index team</td>
</tr>
</tbody>
</table>

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

Figures

[Figure 2‑19. ADT-A24 Link Patient Information msg: Application acknowledgement returned to MVI  
[Figure 2‑34. RSP-K22 Commit acknowledgement: Response msg from QBP-Q22 back to sending system  
[Figure 2‑49. ADT-A40 Merge Patient Identifier List msg: Commit acknowledgement returned to MVI  
[Figure 2‑59. ADT-A04 Register a Patient msg: Application acknowledgement sent from MVI to VistA  
[2-30](#_Toc131832246)](#_Toc131832246)

[Figure 2‑60. ADT-A04 Register a Patient msg: Commit acknowledgement returned to MVI from VistA  
[Figure 2‑63. ADT-A08 Update Patient Information msg: Application acknowledgement sent from MVI  
[2-33](#_Toc3901153)](#_Toc3901153)

[Figure 2‑64. ADT-A08 Update Patient Information msg: Commit acknowledgement returned to MVI  
[Figure 2‑67. ADT-A31 Update Person Information msg: Application acknowledgement sent from MVI  
[Figure 2‑79. ADT-A31 Update Person Information msg: Commit acknowledgement sent from CMOR  
[Figure 2‑86. ADT-A31 Update Person Information msg: Sent *from* the MVI *to* PSIM: Commit ACK  
[Figure 2‑112. ADT-A37 Unlink Patient Information msg: Commit acknowledgement sent from MVI  
[2-61](#_Toc131832284)](#_Toc131832284)

[Figure 2‑113. ADT-A37 Unlink Patient Information msg: Application acknowledgement sent to MVI  
Tables

Orientation

How to Use this Manual

This manual uses several methods to highlight different aspects of the material:

- Various terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each:

|             |                                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| Term    | Description                                                                                   |
| CAUTION | Used to caution the reader to take special notice of critical information.                        |
| NOTE    | Used to inform the reader of additional noteworthy or related information for a topic or subject. |
| REF     | Refers the reader to additional reading material.                                                 |

<span id="_Toc131832197" class="anchor"></span>Table ii. Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Example HL7 messages are shown in a *non*-proportional font and enclosed within a box.
- "Snapshots" of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface type.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter or Return key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.
- Uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Person and user names will be formatted as follows:

> \[Application Name\]PERSON,\[fictitious given name\] and \[Application Name\]USER,\[fictitious given name\] respectively.

> The "Fictitious given name" represents a fabricated given name for the person or user. This is done to more clearly represent person and user names used in descriptive text in this documentation. For example, for the Master Veteran Index (MVI) test patient and user names would be documented as follows: MVIPATIENT,NANCY; MVIPATIENT,SAM; MVIPATIENT,DEBRA; etc. and MVIUSER,RICH; MVIUSER,JOHN; etc.

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

> **NOTE:** Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. Please refer to the *Master Patient Index (MPI) VistA Technical Manual* for further information.

Help at Prompts

VistA software provides online help and commonly used system default prompts. In character-based mode, users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in any VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual* located at the VA Web site: [VA FileMan documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=5) .

Intended Audience/Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- VA FileMan data structures and terminology
- Microsoft Windows
- M programming language

It provides an overall explanation of the MPI/PD HL7 interface specifications contained in MPI/PD VistA software, version 1.0. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere.

Reference Materials

Readers who wish to learn more about the Master Patient Index (MPI) / Patient Demographic (PD) software should consult the following VA Web sites:

- VA Software Document Library Web site:

> [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

- The MPI/PD VistA product documentation, as found at the link above, includes the following manuals:
- *Master Patient Index/Patient Demographics (MPI/PD) User Manual*
- *Master Patient Index/Patient Demographics (MPI/PD) HL7 Interface Specifications*
- *Master Patient Index/Patient Demographics (MPI/PD) Technical Manual*
- *Master Patient Index/Patient Demographics (MPI/PD) Programmer Manual*
- *Master Patient Index (MPI) Monograph*
- All VistA documentation is made available online in both Microsoft Word format and Adobe Acrobat Portable Document Format (PDF).
- The HL7 Standard documentation for current and previous versions is available at the following Web site:

> [HL7 Specifications on the Messaging & Interface Services Web site](http://vista.med.va.gov/messaging/msgadmin/hl7_specifications.asp)  
> *NOTE: This is an internal VA Web site and is not available to the public.*Legal DisclaimersSoftware

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. VA software has no patent/copyright/trademark protections and can be distributed freely via the Freedom of Information Act (FOIA). Pursuant to title 17 Section 105 of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [HL7 Commit Acknowledgement and Application Level Acknowledgements Requirements](#hl7-commit-acknowledgement-and-application-level-acknowledgements-requirements)
  - [HL7 Delimiter(s) Included Data in Field Value](#hl7-delimiters-included-data-in-field-value)
  - [Background Jobs](#background-jobs)
  - [Direct Connect](#direct-connect)
  - [VistA References](#vista-references)
- [Trigger Events & Message Definitions](#trigger-events-message-definitions)
  - [ADT/ACK: Add Person or Patient Information (Event A28)](#adtack-add-person-or-patient-information-event-a28)
  - [ADT/ACK: Admit/Visit Notification (Event A01)](#adtack-admitvisit-notification-event-a01)
  - [ADT/ACK: Discharge/End Visit (Event A03)](#adtack-dischargeend-visit-event-a03)
  - [ADT/ACK: Link Patient Information (Event A24)](#adtack-link-patient-information-event-a24)
  - [QBP/RSP: Find Candidates (QBP) and Response (RSP) (events Q22 and K22)](#qbprsp-find-candidates-qbp-and-response-rsp-events-q22-and-k22)
  - [ADT/ACK: Merge Patient Identifier List (Event A40)](#adtack-merge-patient-identifier-list-event-a40)
  - [ADT/ACK: Move Patient Information Patient Identifier List (Event A43)](#adtack-move-patient-information-patient-identifier-list-event-a43)
  - [ADT/ACK: Register a Patient (Event A04)](#adtack-register-a-patient-event-a04)
  - [ADT/ACK: Update Patient Information (Event A08)](#adtack-update-patient-information-event-a08)
  - [ADT/ACK: Update Person Information (Event A31)](#adtack-update-person-information-event-a31)
  - [ADT/ACK: Update CMOR (Event A31)](#adtack-update-cmor-event-a31)
  - [ADT/ACK: Enterprise Update Person Information (Event A31)](#adtack-enterprise-update-person-information-event-a31)
  - [MFN: Update Treating Facility (Event M05)](#mfn-update-treating-facility-event-m05)
  - [QRY/ADR: Patient Query (Event A19)](#qryadr-patient-query-event-a19)
  - [VQQ: Query for Patient Matches (Event Q02)](#vqq-query-for-patient-matches-event-q02)
  - [VQQ-Q02: Batch Format (i.e., the Local/Missing ICN Resolution Job)](#vqq-q02-batch-format-ie-the-localmissing-icn-resolution-job)
  - [ADT/ACK: Unlink Patient Information (Event A37)](#adtack-unlink-patient-information-event-a37)
- [Message Segments](#message-segments)
  - [BHS: Batch Header Segment](#bhs-batch-header-segment)
    - [BHS-1 Batch Field Separator (ST) 00081](#bhs-1-batch-field-separator-st-00081)
    - [BHS-2 Batch Encoding Characters (ST) 00082](#bhs-2-batch-encoding-characters-st-00082)
    - [BHS-3 Batch Sending Application (ST) 00083](#bhs-3-batch-sending-application-st-00083)
    - [BHS-4 Batch Sending Facility (ST) 00084](#bhs-4-batch-sending-facility-st-00084)
    - [BHS-5 Batch Receiving Application (ST) 00085](#bhs-5-batch-receiving-application-st-00085)
    - [BHS-6 Batch Receiving Facility (ST) 00086](#bhs-6-batch-receiving-facility-st-00086)
    - [BHS-7 Batch Creation Date/Time (TS) 00087](#bhs-7-batch-creation-datetime-ts-00087)
    - [BHS-8 Batch Security (ST) 00088](#bhs-8-batch-security-st-00088)
    - [BHS-9 Batch Name/ID/Type (ST) 00089](#bhs-9-batch-nameidtype-st-00089)
    - [BHS-10 Batch Comment (ST) 00090](#bhs-10-batch-comment-st-00090)
    - [BHS-11 Batch Control ID (ST) 00091](#bhs-11-batch-control-id-st-00091)
    - [BHS-12 Reference Batch Control ID (ST) 00092](#bhs-12-reference-batch-control-id-st-00092)
  - [BTS: Batch Trailer Segment](#bts-batch-trailer-segment)
    - [BTS-1 Batch Message Count (ST) 00093](#bts-1-batch-message-count-st-00093)
    - [BTS-2 Batch Comment (ST) 00090](#bts-2-batch-comment-st-00090)
    - [BTS-3 Batch Totals (NM) 00095](#bts-3-batch-totals-nm-00095)
  - [DSC: Continuation Pointer Segment](#dsc-continuation-pointer-segment)
    - [DSC-1 Continuation pointer (ST) 00014](#dsc-1-continuation-pointer-st-00014)
    - [DSC-2 Continuation style (ID) 01354](#dsc-2-continuation-style-id-01354)
  - [ERR: Error Segment](#err-error-segment)
    - [ERR-1 Error Code and Location (CM) 00024](#err-1-error-code-and-location-cm-00024)
  - [EVN: Event Type Segment](#evn-event-type-segment)
    - [EVN-1 Event Type Code (ID) 00099](#evn-1-event-type-code-id-00099)
    - [EVN-2 Recorded Date/Time (TS) 00100](#evn-2-recorded-datetime-ts-00100)
    - [EVN-3 Date/Time Planned Event (TS) 00101](#evn-3-datetime-planned-event-ts-00101)
    - [EVN-4 Event Reason Code (IS) 00102](#evn-4-event-reason-code-is-00102)
    - [EVN-5 Operator ID (XCN) 00103](#evn-5-operator-id-xcn-00103)
    - [EVN-6 Event Occurred (TS) 01278](#evn-6-event-occurred-ts-01278)
    - [EVN-7 Event Facility (HD) 01534](#evn-7-event-facility-hd-01534)
  - [MFA: Master File Acknowledgement Segment](#mfa-master-file-acknowledgement-segment)
    - [MFA-1 Record-Level Event Code (ID) 00664](#mfa-1-record-level-event-code-id-00664)
    - [MFA-2 MFN Control ID (ST) 00665](#mfa-2-mfn-control-id-st-00665)
    - [MFA-3 Event Completion Date/Time (TS) 00668](#mfa-3-event-completion-datetime-ts-00668)
    - [MFA-4 MFN Record Level Error Return (CE) 00669](#mfa-4-mfn-record-level-error-return-ce-00669)
    - [MFA-5 Primary Key Value - MFA (CE) 01308](#mfa-5-primary-key-value-mfa-ce-01308)
    - [MFA-6 Primary Key Value Type - MFA (ID) 01320](#mfa-6-primary-key-value-type-mfa-id-01320)
  - [MFE: Master File Entry Segment](#mfe-master-file-entry-segment)
    - [MFE-1 Record-Level Event Code (ID) 00664](#mfe-1-record-level-event-code-id-00664)
    - [MFE-2 MFN Control ID (ST) 00665](#mfe-2-mfn-control-id-st-00665)
    - [MFE-3 Effective Date/Time (TS) 00662](#mfe-3-effective-datetime-ts-00662)
    - [MFE-4 Primary Key Value - MFE (Varies) 00667](#mfe-4-primary-key-value-mfe-varies-00667)
    - [MFE-5 Primary Key Value Type (ID) 01319](#mfe-5-primary-key-value-type-id-01319)
  - [MFI: Master File Identification Segment](#mfi-master-file-identification-segment)
    - [MFI-1 Master File Identifier (CE) 00658](#mfi-1-master-file-identifier-ce-00658)
    - [MFI-3 File-Level Event Code (ID) 00660](#mfi-3-file-level-event-code-id-00660)
    - [MFI-6 Response Level Code (ID) 00663](#mfi-6-response-level-code-id-00663)
  - [MRG: Merge Patient Information Segment](#mrg-merge-patient-information-segment)
    - [MRG-1 Prior Patient Identifier List (CX) 00211](#mrg-1-prior-patient-identifier-list-cx-00211)
    - [MRG-2 Prior Alternate Patient ID (CX) 00212](#mrg-2-prior-alternate-patient-id-cx-00212)
    - [MRG-3 Prior Patient Account Number (CX) 00213](#mrg-3-prior-patient-account-number-cx-00213)
    - [MRG-4 Prior Patient ID (CX) 00214](#mrg-4-prior-patient-id-cx-00214)
    - [MRG-5 Prior Visit Number (CX) 01279](#mrg-5-prior-visit-number-cx-01279)
    - [MRG-6 Prior Alternate Visit ID (CX) 01280](#mrg-6-prior-alternate-visit-id-cx-01280)
    - [MRG-7 Prior Patient Name (XPN) 01281](#mrg-7-prior-patient-name-xpn-01281)
  - [MSA: Message Acknowledgement Segment](#msa-message-acknowledgement-segment)
    - [MSA-1 Acknowledgement Code (ID) 00018](#msa-1-acknowledgement-code-id-00018)
    - [MSA-2 Message Control ID (ST) 00010](#msa-2-message-control-id-st-00010)
    - [MSA-3 Text message (ST) 00020](#msa-3-text-message-st-00020)
    - [MSA-5 Delayed Acknowledgement Type (ID) 00022](#msa-5-delayed-acknowledgement-type-id-00022)
    - [MSA-6 Error Condition (CE) 00023](#msa-6-error-condition-ce-00023)
  - [MSH: Message Header Segment](#msh-message-header-segment)
    - [MSH-1 Field Separator (ST) 00001](#msh-1-field-separator-st-00001)
    - [MSH-2 Encoding Characters (ST) 00002](#msh-2-encoding-characters-st-00002)
    - [MSH-3 Sending Application (HD) 00003](#msh-3-sending-application-hd-00003)
    - [MSH 4 -Sending Facility (HD) 00004](#msh-4-sending-facility-hd-00004)
    - [MSH-5 Receiving Application (HD) 00005](#msh-5-receiving-application-hd-00005)
    - [MSH-6 Receiving Facility (HD) 00006](#msh-6-receiving-facility-hd-00006)
    - [MSH-7 Date/Time of Message (TS) 00007](#msh-7-datetime-of-message-ts-00007)
    - [MSH-9 Message Type (CM) 00009](#msh-9-message-type-cm-00009)
    - [MSH-10 Message Control ID (ST) 00010](#msh-10-message-control-id-st-00010)
    - [MSH-11 Processing ID (PT) 00011](#msh-11-processing-id-pt-00011)
    - [MSH-12 Version ID (VID) 00012](#msh-12-version-id-vid-00012)
    - [MSH-15 Accept Acknowledgement Type (ID) 00015](#msh-15-accept-acknowledgement-type-id-00015)
    - [MSH-16 Application Acknowledgement Type (ID) 00016](#msh-16-application-acknowledgement-type-id-00016)
    - [MSH-17 Country Code (ID) 00017](#msh-17-country-code-id-00017)
  - [NTE: Notes and Comments Segment](#nte-notes-and-comments-segment)
    - [NTE-1 Set ID–NTE (SI) 00096](#nte-1-set-idnte-si-00096)
    - [NTE-2 Source of Comment (ID) 00097](#nte-2-source-of-comment-id-00097)
    - [NTE-3 Comment (FT) 00098](#nte-3-comment-ft-00098)
  - [OBX: Observation/Result, HL7 Segment](#obx-observationresult-hl7-segment)
  - [PD1: Patient Additional Demographic Segment](#pd1-patient-additional-demographic-segment)
    - [PD1-3 Patient Primary Facility (XON) 00756](#pd1-3-patient-primary-facility-xon-00756)
    - [Yes/No Indicator Table](#yesno-indicator-table)
  - [PID: Patient Identification Segment](#pid-patient-identification-segment)
    - [PID-1 Set ID ‑ PID (SI) 00104](#pid-1-set-id-pid-si-00104)
    - [PID-2 Patient ID (CX) 00105](#pid-2-patient-id-cx-00105)
    - [PID-3 Patient identifier list (CX) 00106](#pid-3-patient-identifier-list-cx-00106)
    - [PID-4 Alternate patient ID - PID (CX) 00107](#pid-4-alternate-patient-id-pid-cx-00107)
    - [PID-5 Patient name (XPN) 00108](#pid-5-patient-name-xpn-00108)
    - [PID-6 Mother's maiden name (XPN) 00109](#pid-6-mothers-maiden-name-xpn-00109)
    - [PID-7 Date/time of birth (TS) 00110](#pid-7-datetime-of-birth-ts-00110)
    - [PID-8 Administrative sex (IS) 00111](#pid-8-administrative-sex-is-00111)
    - [PID-9 Patient alias (XPN) 00112](#pid-9-patient-alias-xpn-00112)
    - [PID-10 Race (CE) 00113](#pid-10-race-ce-00113)
    - [PID-11 Patient address (XAD) 00114](#pid-11-patient-address-xad-00114)
    - [PID-12 County code (IS) 00115](#pid-12-county-code-is-00115)
    - [PID-13 Phone number - home (XTN) 00116](#pid-13-phone-number-home-xtn-00116)
    - [PID-14 Phone number ‑ business (XTN) 00117](#pid-14-phone-number-business-xtn-00117)
    - [PID-15 Primary language (CE) 00118](#pid-15-primary-language-ce-00118)
    - [PID-16 Marital status (CE) 00119](#pid-16-marital-status-ce-00119)
    - [PID-17 Religion (CE) 00120](#pid-17-religion-ce-00120)
    - [PID-18 Patient account number (CX) 00121](#pid-18-patient-account-number-cx-00121)
    - [PID-19 SSN number ‑ patient (ST) 00122](#pid-19-ssn-number-patient-st-00122)
    - [PID-20 Driver's license number - Patient (DLN) 00123](#pid-20-drivers-license-number-patient-dln-00123)
    - [PID-21 Mother's identifier (CX) 00124](#pid-21-mothers-identifier-cx-00124)
    - [PID-22 Ethnic group (CE) 00125](#pid-22-ethnic-group-ce-00125)
    - [PID-23 Birth place (ST) 00126](#pid-23-birth-place-st-00126)
    - [PID-24 Multiple birth indicator (ID) 00127](#pid-24-multiple-birth-indicator-id-00127)
    - [PID-25 Birth order (NM) 00128](#pid-25-birth-order-nm-00128)
    - [PID-26 Citizenship (CE) 00129](#pid-26-citizenship-ce-00129)
    - [PID-27 Veterans military status (CE) 00130](#pid-27-veterans-military-status-ce-00130)
    - [PID-28 Nationality (CE) 00739](#pid-28-nationality-ce-00739)
    - [PID-29 Patient death date and time (TS) 00740](#pid-29-patient-death-date-and-time-ts-00740)
    - [PID-30 Patient Death Indicator (ID) 00741](#pid-30-patient-death-indicator-id-00741)
    - [PID-31 Identity Unknown Indicator (ID) 01535](#pid-31-identity-unknown-indicator-id-01535)
    - [PID-32 Identity Reliability Code (IS) 01536](#pid-32-identity-reliability-code-is-01536)
    - [PID-33 Last Update Date/Time (TS) 01537](#pid-33-last-update-datetime-ts-01537)
    - [PID-34 Last Update Facility (HD) 01538](#pid-34-last-update-facility-hd-01538)
    - [PID-35 Species Code (CE) 01539](#pid-35-species-code-ce-01539)
    - [PID-36 Breed Code (ID) 01540](#pid-36-breed-code-id-01540)
    - [PID-37 Strain (ST) 01541](#pid-37-strain-st-01541)
    - [PID-38 Production Class Code (CE) 01542](#pid-38-production-class-code-ce-01542)
  - [PV1: Patient Visit Segment](#pv1-patient-visit-segment)
    - [PV1-2 Patient Class](#pv1-2-patient-class)
    - [PV1-44 Admit Date/Time (TS) 00174](#pv1-44-admit-datetime-ts-00174)
  - [PV2: Patient Visit Segment – Additional Information](#pv2-patient-visit-segment-additional-information)
    - [PV2-8 Expected admit date/time (TS) 00188](#pv2-8-expected-admit-datetime-ts-00188)
    - [PV2-14 Previous service date (DT) 00715](#pv2-14-previous-service-date-dt-00715)
    - [PV2-46 Patient Status Effective Date (DT) 01549](#pv2-46-patient-status-effective-date-dt-01549)
  - [QAK: Query Acknowledgement Segment](#qak-query-acknowledgement-segment)
    - [QAK-1 Query Tag (ST) 00696](#qak-1-query-tag-st-00696)
    - [QAK-2 Query Response Status (ID) 00708](#qak-2-query-response-status-id-00708)
    - [QAK-3 Message query name (CE) 01375](#qak-3-message-query-name-ce-01375)
    - [QAK-4 Hit count total (NM) 01434](#qak-4-hit-count-total-nm-01434)
  - [QPD: Query Parameter Definition Segment](#qpd-query-parameter-definition-segment)
    - [QPD-1 Message query name (CE) 01375](#qpd-1-message-query-name-ce-01375)
    - [QPD-2 Query tag (ST) 00696](#qpd-2-query-tag-st-00696)
    - [QPD-3 User parameters (Varies) 01435](#qpd-3-user-parameters-varies-01435)
    - [QPD-4 User parameters (Varies) 01435](#qpd-4-user-parameters-varies-01435)
    - [QPD-5 User parameters (Varies) 01435](#qpd-5-user-parameters-varies-01435)
    - [QPD-6 User parameters (Varies) 01435](#qpd-6-user-parameters-varies-01435)
  - [QRD: Original-Style Query Definition Segment](#qrd-original-style-query-definition-segment)
    - [QRD-1 Query Date/Time (TS) 00025](#qrd-1-query-datetime-ts-00025)
    - [QRD-2 Query Format Code (ID) 00026](#qrd-2-query-format-code-id-00026)
    - [QRD-3 Query Priority (ID) 00027](#qrd-3-query-priority-id-00027)
    - [QRD-4 Query ID (ST) 00028](#qrd-4-query-id-st-00028)
    - [QRD-5 Deferred Response Type (ID) 00029](#qrd-5-deferred-response-type-id-00029)
    - [QRD-6 Deferred Response Date/Time (TS) 00030](#qrd-6-deferred-response-datetime-ts-00030)
    - [QRD-7 Quantity Limited Request (CQ) 00031](#qrd-7-quantity-limited-request-cq-00031)
    - [QRD-8 Who Subject Filter (XCN) 00032](#qrd-8-who-subject-filter-xcn-00032)
    - [QRD-9 What Subject Filter (CE) 00033](#qrd-9-what-subject-filter-ce-00033)
    - [QRD-10 What Department Data Code (CE) 00034](#qrd-10-what-department-data-code-ce-00034)
    - [QRD-11 What Data Code Value Qual (CM) 00035](#qrd-11-what-data-code-value-qual-cm-00035)
    - [QRD-12 Query Results Level (ID) 00036](#qrd-12-query-results-level-id-00036)
  - [QRI: Query Response Instance Segment](#qri-query-response-instance-segment)
  - [RCP: Response Control Parameter Segment](#rcp-response-control-parameter-segment)
    - [RCP-1 Query priority (ID) 00027](#rcp-1-query-priority-id-00027)
    - [RCP-2 Quantity limited request (CQ) 00031](#rcp-2-quantity-limited-request-cq-00031)
    - [RCP-3 Response modality (CE) 01440](#rcp-3-response-modality-ce-01440)
    - [RCP-4 Execution and delivery time (TS) 01441](#rcp-4-execution-and-delivery-time-ts-01441)
    - [RCP-5 Modify indicator (ID) 01443](#rcp-5-modify-indicator-id-01443)
    - [RCP-6 Sort-by field (SRT) 01624](#rcp-6-sort-by-field-srt-01624)
    - [RCP-7 Segment group inclusion (ID) 01594](#rcp-7-segment-group-inclusion-id-01594)
  - [RDF: Table Row Definition Segment](#rdf-table-row-definition-segment)
    - [RDF-1 Number of columns per row (NM) 00701](#rdf-1-number-of-columns-per-row-nm-00701)
    - [RDF-2Column Description (RCD) 00702](#rdf-2column-description-rcd-00702)
  - [RDT: Table Row Data Segment](#rdt-table-row-data-segment)
    - [RDT-1 Column value (Variable) 00703](#rdt-1-column-value-variable-00703)
  - [VTQ: Virtual Table Query Request Segment](#vtq-virtual-table-query-request-segment)
    - [VTQ-1 Query tag (ST) 00696](#vtq-1-query-tag-st-00696)
    - [VTQ-2 Query/Response Format Code (ID) 00697](#vtq-2-queryresponse-format-code-id-00697)
    - [VTQ-3 VT Query Name (CE) 00698](#vtq-3-vt-query-name-ce-00698)
    - [VTQ-4 Virtual Table Name (CE) 00699](#vtq-4-virtual-table-name-ce-00699)
    - [VTQ -5 Selection Criteria (QSC) 00700](#vtq-5-selection-criteria-qsc-00700)
  - [ZCT: VA Specific Emergency Contact Segment](#zct-va-specific-emergency-contact-segment)
  - [ZEL: VA Specific Patient Eligibility Segment](#zel-va-specific-patient-eligibility-segment)
  - [ZEM: VA Specific Employment Information Segment](#zem-va-specific-employment-information-segment)
  - [ZET: VA Specific Event Reason for Date of Last Treatment Segment](#zet-va-specific-event-reason-for-date-of-last-treatment-segment)
    - [ZET-1 Event Reason Code Name](#zet-1-event-reason-code-name)
    - [ZET-2 Patient Primary Facility](#zet-2-patient-primary-facility)
  - [ZFF: VA Specific File/Field Segment](#zff-va-specific-filefield-segment)
  - [ZPD: VA Specific Patient Information Segment](#zpd-va-specific-patient-information-segment)
    - [ZPD-17 POW Status Indicated?](#zpd-17-pow-status-indicated)
    - [ZPD-34 PSEUDO SSN REASON](#zpd-34-pseudo-ssn-reason)
  - [ZSP: VA Specific Service Period Segment](#zsp-va-specific-service-period-segment)
- [VA HL7 Tables](#va-hl7-tables)
  - [Table VA001: Yes/No](#table-va001-yesno)
  - [Table VA002: Current Means Test Status](#table-va002-current-means-test-status)
  - [Table VA004: Eligibility](#table-va004-eligibility)
  - [Table VA005: Disability Retirement From Military](#table-va005-disability-retirement-from-military)
  - [Table VA006: Eligibility Status](#table-va006-eligibility-status)
  - [Table VA008: Religion](#table-va008-religion)
  - [Table VA010: Means Test Indicator](#table-va010-means-test-indicator)
  - [Table VA011: Period of Service](#table-va011-period-of-service)
  - [Table VA012: Type of Insurance](#table-va012-type-of-insurance)
  - [Table VA015: Enrollment Status](#table-va015-enrollment-status)
  - [Table VA016: Reason Canceled/Declined](#table-va016-reason-canceleddeclined)
  - [Table VA021: Enrollment Priority](#table-va021-enrollment-priority)
  - [Table VA022: Radiation Exposure Method](#table-va022-radiation-exposure-method)
  - [Table VA023: Prisoner of War Location](#table-va023-prisoner-of-war-location)
  - [Table VA024: Source of Enrollment](#table-va024-source-of-enrollment)
  - [Table VA036: MST Status](#table-va036-mst-status)
  - [Table VA046: Agent Orange Exposure Location](#table-va046-agent-orange-exposure-location)
  - [Table NPCD 001: National Patient Care Database Error Codes](#table-npcd-001-national-patient-care-database-error-codes)
Overview of Master Veteran Index (MVI)
The Master Veteran Index (MVI) is the authoritative source for *<u>person identity data</u>*. It maintains identity data for persons across VA systems, provides a unique universal identifier for each person, stores identity data as correlations for each system where a person is known, provides a probabilistic matching algorithm, and includes the Master Patient Index (MPI), Person Service Identity Management (PSIM), and Toolkit (TK). It maintains a “gold copy” known as a “Primary View” of the person’s identity data. Broadcasts identity trait updates to systems of interest.
The MPI Austin is the data store of person records and one of the component pieces of the Master Veteran Index. It is a cross-reference or index of persons that includes the person's related identifiers and other patient identifying information. The MVI is used to associate a person's identifiers among multiple ID-assigning entities, possibly including a Health Data Repository, to support the consolidation and sharing of a patient’s health care information across VHA. The MVI is the authoritative source for *<u>patient identity</u>*.
Overview Of the Master Veteran (MVI) Index Hl7 Interface Specifications
This interface specification is intended to identify the VistA information that will be shared as part of the MVI. The sharing of this information will be triggered by specific VistA events. Both the exact events and the messages used to share this data will be reviewed.
MVI makes use of and creates messages using the abstract message approach and encoding rules specified by the HL7 standard. The HL7 VistA application will be used for communicating data associated with various events that occur in health care environments.
The formats of these messages conform to HL7 interface standards, Version 2.4.
> **NOTE:** There are references in this document to the VistA HL7 package enhancement known as HLO which stands for HL7 Optimized (HLO). HLO is a tool available to developers and is used on the MPI to speed up outbound messages to PSIM.
REF: For more information on why a person doesn't have an ICN, please refer to the Appendix "Why Doesn't a Patient Have a National ICN?" located in the *Master Patient Index/Patient Demographics (MPI/PD) VistA User* or *ExceptionHandling* Manuals on the VA Web site: [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

## HL7 Commit Acknowledgement and Application Level Acknowledgements Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An HL7 Commit and Application Level Acknowledgement are required for the majority of messages document here. Each message details whether or not each is expected and the format for these acknowledgements.

The HL7 Commit Acknowledgement is required for ALL messages. It allows the sender to know that the message has been successfully received. The commit acknowledgement is not for anything more than that. The Commit ACK is expected back over the same socket connection as the original message was sent. For those applications using VistA HL7, the commit ACK is generated and processed by VistA HL7.

The Application Level Acknowledgement is required for most all messages. It allows the sender to know how the processing of this specific message went. Was it was successful or was there a problem. For a number of messages sent by the MVI, it is the Application Level Acknowledgement that triggers the completion of the event that resulted in the original message. Without the receipt of that application acknowledgement, the process remains incomplete. The application level acknowledgement is not to be sent back over the same socket as the commit acknowledgement but rather over a subsequent connection.

## HL7 Delimiter(s) Included Data in Field Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is possible to have HL7 delimiters are part of a data field within a given segment. To avoid issues with the parsing of the message these delimiters are encoded. Below is taken from Section 2.10 of the 2.4 HL7 Standards:

2.10 Use of escape sequences in text fields

2.10.1 Formatting codes

When a field of type TX, FT, or CF is being encoded, the escape character may be used to signal certain special characteristics of portions of the text field. The escape character is whatever display ASCII character is specified in the \<escape character\> component of *MSH-2-encoding characters*. For purposes of this section, the character \\ will be used to represent the character so designated in a message. An escape sequence consists of the escape character followed by an escape code ID of one character, zero (0) or more data characters, and another occurrence of the escape character. The following escape sequences are defined:

|             |                                 |
|-------------|---------------------------------|
| \H\\        | start highlighting              |
| \N\\        | normal text (end highlighting)  |
| \F\\        | field separator                 |
| \S\\        | component separator             |
| \T\\        | subcomponent separator          |
| \R\\        | repetition separator            |
| \E\\        | escape character                |
| \Xdddd...\\ | hexadecimal data                |
| \Zdddd...\\ | locally defined escape sequence |

The escape sequences for field separator, component separator, subcomponent separator, repetition separator, and escape character are also valid within an ST data field.

No escape sequence may contain a nested escape sequence.

## Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

UPDATE BATCH JOB FOR HL7 v2.3 \[VAFC BATCH UPDATE\]

Updates to specific patient demographic data will trigger the broadcasting of a HL7 ADT-A08 message. Because there is no set way of identifying when an edit to patient information is complete, these edit events are marked as needing to be transmitted in the ADT/HL7 PIVOT file (#391.71). The background job VAFC BATCH UPDATE (scheduled TaskMan job) periodically broadcasts the HL7 ADT-A08 message, containing any changes to data, to the MVI.

LOCAL/MISSING ICN RESOLUTION BACKGROUND \[MPIF LOC/MIS ICN RES\]

The Local and Missing ICN background process looks at the Local ICN ("AICNL") and Missing ICN ("AMPIMIS") cross-references and sends batch messages to the MVI requesting an ICN (100 persons per message). How do persons receive a Local ICN? Persons can receive a Local ICN if an attempt to contact the MVI fails. How does a person’s get the Missing ICN cross-reference set? The Missing ICN cross-reference is set when a package adds a person record to the PATIENT file (#2), but does not communicate with the MVI.

> **NOTE:** Options that add patients to the PATIENT file (#2) AND communicate with the MVI are:

- Load/Edit Patient Data \[DG LOAD PATIENT DATA\]
- Register a Patient \[DG REGISTER PATIENT\]
- Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\]

The following option communicates with the MVI and can obtain ICNs for person entries in PATIENT file (#2), but does not add person entries to the MVI:

- Local/Missing ICN Resolution background job

REF: For more information on why a patient doesn't have an ICN, please refer to the Appendix "Why Doesn't a Patient Have a National ICN?" located in the Master Patient Index/Patient Demographics (MPI/PD) VistA User and Exception Handling Manuals and found on the VA Web site:  
[MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

## Direct Connect

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Direct Connect is a real-time Transmission Control Protocol/Internet Protocol (TCP/IP) connection to the Master Veteran Index to allow for an immediate request for an ICN. It is activated during the Register A Patient, Load/Edit Patient Data, and Electronic 10-10EZ Processing processes when:

> 1\. A new person record is added to the system, or

> 2\. A person record exists but doesn't have an ICN.

In addition, by utilizing the Potential Match Review (PMR) action within the MPI/PD EXCEPTION HANDLING option, for Potential Match exceptions, the TCP/IP direct connection with the MVI will occur. This event causes creation of a VQQ-Q02 and is sent to the MVI to find out if the person is known.

The Display Only Query option, used to view the data the MVI knows about a patient, and also utilizes the TCP/IP direct connect with the MVI. A VQQ-Q02 query is sent to the MVI. If the MVI knows the patient or finds a list of potential matches, the data is displayed to the users. No data is updated at the site or the MVI. If the MVI does not know the person, a message is displayed stating so.

## VistA References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPI/PD software maintains the following VistA fields, Table 1‑1, in the PATIENT file (#2), as well as the list of systems that know this person by this ICN, in the TREATING FACILITY file (#391.91) at all VistA sites.

| Field Number | Field Name                |
|------------------|-------------------------------|
| 2,.01            | NAME                          |
| 2,.02            | SEX                           |
| 2,.024           | SELF IDENTIFIED GENDER        |
| 2,.03            | DATE OF BIRTH                 |
| 2,.05            | MARITAL STATUS                |
| 2,.08            | RELIGIOUS PREFERENCE          |
| 2,.09            | SOCIAL SECURITY NUMBER        |
| 2,.111           | STREET ADDRESS \[LINE 1\]     |
| 2,.1112          | ZIP+4                         |
| 2,.112           | STREET ADDRESS \[LINE 2\]     |
| 2,.113           | STREET ADDRESS \[LINE 3\]     |
| 2,.114           | CITY                          |
| 2,.115           | STATE                         |
| 2,.116           | ZIP CODE                      |
| 2,.117           | COUNTY                        |
| 2,.1171          | PROVINCE                      |
| 2,.1172          | POSTAL CODE                   |
| 2,.1172          | COUNTRY                       |
| 2,.121           | BAD ADDRESS INDICATOR         |
| 2,.131           | PHONE NUMBER \[RESIDENCE\]    |
| 2,.132           | PHONE NUMBER \[WORK\]         |
| 2,.133           | EMAIL ADDRESS                 |
| 2,.134           | PHONE NUMBER \[CELLULAR\]     |
| 2,.211           | K-NAME OF PRIMARY NOK         |
| 2,.219           | K-PHONE NUMBER                |
| 2,.2403          | MOTHER'S MAIDEN NAME          |
| 2,.301           | SERVICE CONNECTED?            |
| 2,.302           | SERVICE CONNECTED PERCENTAGE  |
| 2,.31115         | EMPLOYMENT STATUS             |
| 2,.313           | CLAIM NUMBER                  |
| 2,.323           | PERIOD OF SERVICE             |
| 2,.351           | DATE OF DEATH                 |
| 2,.352           | DEATH ENTERED BY              |
| 2,.353           | SOURCE OF NOTIFICATION        |
| 2,.354           | DATE OF DEATH LAST UPDATED    |
| 2,.355           | LAST EDITED BY                |
| 2,.361           | PRIMARY ELIGIBILITY CODE      |
| 2,.525           | POW STATUS INDICATED?         |
| 2,2              | RACE INFORMATION              |
| 2,6              | ETHNICITY INFORMATION         |
| 2,391            | TYPE                          |
| 2,991.01         | INTEGRATION CONTROL NUMBER    |
| 2,991.02         | ICN CHECKSUM                  |
| 2,991.03         | COORDINATING MASTER OF RECORD |
| 2,991.04         | LOCALLY ASSIGNED ICN          |
| 2,991.05         | SUBSCRIPTION CONTROL NUMBER   |
| 2,991.06         | CMOR ACTIVITY SCORE           |
| 2,991.07         | SCORE CALCULATION DATE        |
| 2,991.08         | TEMPORARY ID NUMBER           |
| 2,991.09         | FOREIGN ID NUMBER             |
| 2,991.1          | FULL ICN                      |
| 2,994            | MULTIPLE BIRTH INDICATOR      |
| 2,1901           | VETERAN (Y/N)?                |
| 2.01,.01         | ALIAS                         |
| 2.01,1           | ALIAS SSN                     |
| 2.0991,.01       | FULL ICN HISTORY              |
| 2.0992,.01       | ICN HISTORY                   |

<span id="_Ref410609732" class="anchor"></span>Table ‑. Data elements monitored in the PATIENT file (#2) for changes

The MPI/PD software also maintains the integrity of person identity at all other known systems via the HL7 ICN maintenance messages listed below. VistA software can obtain an ICN or retrieve a list of associated system via the supported VistA references listed below (more information can be obtained through the FORUM DBA menu):

> **NOTE:** SUBSCRIPTION CONTROL NUMBER (#991.05) is no longer utilized by the MPI/PD software in the PATIENT file (#2).

| Name | IA | Reference Type | Custodial Package      | Description                                                                                                                                                                          |
|----------|--------|--------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MPIF001  | 2701   | Supported          | Master Patient Index—VistA | Function APIs to return values on the MPI node in the PATIENT file (#2). This DBIA documents some entry points for accessing the MPI node in the PATIENT file for use by VistA packages. |
| MPIFAPI  | 2702   | Supported          | Master Patient Index—VistA | Functions to return the MPI node, the name of the HL7 Logical Link for the MPI, and to return the next Local Integration Control Number. These APIs are provided for VistA packages.     |
| VAFCTFU1 | 2990   | Supported          | Registration               | Function API's that will return a list of systems associated with a specific ICN or DFN.                                                                                                 |
| VAFCQRY  | 3630   | Private            | Registration               | Function API's used to build generic PID, EVN, and PD1 segments in the new HL7 2.4 format that will include all of the person identifiers (ICN(s), SSN, Claim Number and DFN).           |

<span id="_Toc131832198" class="anchor"></span>Table ‑. MVI-related Integration Agreement (IA) references

# Trigger Events & Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the MPI trigger events as well as the HL7 messages that help to establish and maintain the integrity of the unique identification of a person throughout the VHA Enterprise.

REF: For more information on which HL7 messages apply specifically to non-VistA systems see "Appendix A" in this documentation.

> **NOTE:** Primary View Initialization, as reference in Table 2‑1, Trigger Event "Update to fields on an existing MVI entry," is a process that occurs on the MVI. This process applies significant enhancements to the MVI business logic to support a more centralized approach to creating and maintaining an Enterprise "Primary View" of the person’s record based on Business Rules instead of CMOR values.  “Primary View” is the centralized enterprise “View” of a person on the MVI after the initialization process has been executed, making existing persons on the MVI “Primary View Initialized.”

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 21%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Trigger Event</strong></th>
<th><strong>Event Supported HL7 V2.4 Message</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Query MVI for match</td>
<td><p><a href="#vqq-query-for-patient-matches-event-q02">VTQ-Q02</a></p>
<p>/</p></td>
<td><p>The MVI will accept a query for person information. The current search algorithm uses Name, DOB, and SSN (if available) for its search. Results are returned in an ACK/Q02 (changed from ADT-A31 in patches MPI*1.0*32 and MPIF*1.0*38)</p>
<p><strong>NOTE:</strong> supported for internal VistA VAMC messaging).</p>
<p>This find Candidates query is used to return a list of one ICN candidates for a given local identifier (i.e. dfn/station#). The query can also be used to establish a correlation to an ICN and/or an association to an existing correlated id (i.e. dfn/station#).</p>
<p><strong>NOTE:</strong> Supported for external VistA VAMC messaging.</p></td>
</tr>
<tr class="even">
<td>Add new patient to the MVI</td>
<td>(via Local/Missing ICN Resolution Job)</td>
<td><p>The MVI will accept new patient adds via ADT-A28 (add person or patient information). The MPI will in-turn broadcast back an ADT-A24 (link patient information) message.</p>
<p>The MVI will add a new patient if the VQQ-Q02 is sent in the form of the Local/Missing ICN Resolution Job and the patient is not found. The MVI will return the ICN in the ACK/Q02 Local/Missing ICN Resolution job response.</p></td>
</tr>
<tr class="odd">
<td>Link to an existing patient on the MVI</td>
<td><a href="#adtack-link-patient-information-event-a24">ADT-A24</a></td>
<td>The MVI will accept an ADT-A24 (link patient information) message for the purpose of matching a sites patient to an existing ICN. The sites current demographic values will also be stored as a result.</td>
</tr>
<tr class="even">
<td>Update to fields on an existing MVI entry</td>
<td>,</td>
<td><p>The MVI will accept patient updates via ADT-A04 (register a patient) or ADT-A08 (update patient information) and will broadcast out to the authoritative source system if the update came from a non-authoritative source system and to all systems if it came from the authoritative source system for all patients that haven't been Primary View Initialized.</p>
<p>Once a patient has been Primary View Initialized the updates will be sent out to all systems in need of the update via an ADT-A31 message.</p></td>
</tr>
<tr class="odd">
<td>Update Person Information outside of an event</td>
<td></td>
<td><p>The MPI will accept an ADT-A31 (update person information) and update the appropriate entry on the MPI depending on if the message is from the CMOR (MPI VETERAN/CLIENT file [#985]) or a treating facility (ASSOCIATED FACILITY file [#985.5]).</p>
<p>The MPI also broadcast out an ADT-A31 message to synchronize the identity management elements to the MPI Patient "primary view".</p></td>
</tr>
<tr class="even">
<td>Update to date last treated</td>
<td>,</td>
<td>The MPI will accept updates to date last treated and event reason via ADT-A01 (admit/visit notification) and/or ADT-A03 (Discharge and/or clinic checkouts). If the update changes the sites current MPI date last treated or event reason the MPI will broadcast a MFN-M05.</td>
</tr>
<tr class="odd">
<td>Resolution of duplicates at the site where both entries exist on the MVI</td>
<td></td>
<td>The MPI will accept a resolution of a duplicate from a site via ADT-A40 (merge patient - patient identifier list). The MPI will in-turn broadcast out an ADT-A24 (link patient information).</td>
</tr>
<tr class="even">
<td>Resolution of duplicates on the MVI</td>
<td></td>
<td>The MPI will notify sites of a duplicate resolution via ADT-A24 (link patient information).</td>
</tr>
<tr class="odd">
<td>Identification and resolution of a mismatched patient</td>
<td></td>
<td>The MPI will notify sites of a mismatched patient via ADT-A43 (move patient - patient identifier list). This maintenance message is used to update a record's ICN (i.e. enterprise ID trait).</td>
</tr>
<tr class="even">
<td>Change of CMOR assignment</td>
<td></td>
<td>The MPI will accept a change in CMOR assignment via an ADT-A31 from the current CMOR via ADT-A31 (update person information).</td>
</tr>
<tr class="odd">
<td>Patient Query</td>
<td></td>
<td>The sending site is requesting patient demographic information to be returned for a specific ICN via the QRY-A19 (patient query) message. The data is returned in an ADR message to the requesting site.</td>
</tr>
<tr class="even">
<td>Unlink Patient</td>
<td></td>
<td>The sending site is requesting to unlink its patient record from an ICN. This action reverses the Link.</td>
</tr>
<tr class="odd">
<td>Treating Facility List Update</td>
<td></td>
<td><p>The MPI will send out an MFN-M05 if the treating facility list is modified or if the date last treated or event reason changes.</p>
<p>This message can be generated as a result of another message being processed on the MPI or maybe triggered manually.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref170545101" class="anchor"></span>Table ‑. Trigger events and message definitions

HL7 Messages

Each HL7 message is composed of segments. Segments contain logical groupings of data. Segments can be optional or repeatable. In the HL7 Standard documentation, square brackets (\[\]) indicate segments are optional, curly brackets ({}) indicate segments are repeatable. For each message type there is a list of HL7 standard segments. This section describes the HL7 messages that help to establish and maintain the integrity of the unique identification of a person throughout the VHA Enterprise.

> **NOTE:** The VistA data is mapped to fields within these segments. The elements/contents of each of these message segments is defined in the section titled "Message Segments" in this manual.

## ADT/ACK: Add Person or Patient Information (Event A28)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this message is to establish a person on the Master Veteran Index so that the record can be viewed across the enterprise and to allow multiple systems and respective Master Veteran databases to communicate activity related to a person regardless of whether that person is currently a patient on each system. Each system has an interest in the database activity of the others in order to maintain data integrity across an enterprise. To the enterprise systems, the person may be a current patient, a potential future patient, or never be needed. These events can be used to also maintain another MVI (Master Veteran Index) or enterprise database.

The person whose data is being sent should be identified in the PID segment using the [PID-3 - patient identifier list](#pid-3-patient-identifier-list-cx-00106). An A28 requests the establishment of an ICN and stores the person identifiers (e.g., social security number, claim#, or other unique identifiers) as passed in the . Other identifiers such as deprecated identifiers (i.e., local ICN) can be sent in the [PID-4 -alternate patient identifier list](#pid-4-alternate-patient-id---pid-cx-00107), which will also be stored as an alternate id on the MVI for that system to be included in subsequent communicates from the MVI. Each new system will need to register their identifier list and assigning authority with the MVI development group.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A28^ADT_A28 ADT Message Chapter

[MSH](#msh-message-header-segment) Message Header 2

Event Type 3

[PID](#pid-patient-identification-segment) Patient Identification 3

\[ \] Additional Demographics 3

Patient Visit 3

\[ \] VA Specific Patient Information Segment

\[{[OBX](#obx-observationresult-hl7-segment)}\] Observation/Result 7

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A28^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example Message Sent *<u>to</u>* the MVI *<u>from</u>* VistANOTE: Only VistA systems can add persons to the MVI at this time.

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20021003100450-0500^^ADT~A28^000167546^P^2.4^^^AL^AL^

EVN^^^^^12556~MVIUSER~ONE\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^^500

PID^1^^500000558V314240\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20021003\|666777765\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|100000088\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^MVIPATIENT~CAROL ~L\~\~\~~L^""^19230807^F^^^""~""~""~""~""\~~P~""\|\~~""~""\~\~~N^""^""^""^^""^""^^^^^^^^^^^^""^^

PD1^^^VAMCSITE~D~500

ZPD^1^^^^^^^^^^^^^^^^Y^^^^

<span id="_Toc131832200" class="anchor"></span>Figure ‑. ADT-A28 Add Person or Patient Information msg: Sent from VistA to MVI

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20051020050056-0500^^ACK^2001653335787^P^2.4

MSA^CA^000167546

<span id="_Toc3901092" class="anchor"></span>Figure ‑. ADT-A28 Add Person or Patient Information msg: Commit acknowledgement sent from MVI to sending system

Application Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20041206112926-0500^^ACK~A28^200895618^P^2.4^^^AL^NE^

MSA^AA^000167546^^^^DFN=100000088

<span id="_Toc3901093" class="anchor"></span>Figure ‑. ADT-A28 Add Person or Patient Information msg: Application acknowledgement sent from MVI to sending system

Commit Level Acknowledgement Returned*<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20051109124639-0400^^ACK^55385465^P^2.4

MSA^CA^200895618

<span id="_Toc131832203" class="anchor"></span>Figure ‑. ADT-Add Person or Patient Information msg: Commit acknowledgement returned to MVI

## ADT/ACK: Admit/Visit Notification (Event A01)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An A01 event is intended to be used for "Admitted" patients only. An A01 event is sent as a result of a patient undergoing the admission process. It signals the beginning of a patient's stay in a healthcare facility. This information is entered in the primary Patient Administration system (VistA PIMS Admit a Patient option \[DG ADMIT PATIENT\]). It includes short stay and "John Doe" (e.g., patient name is unknown) admissions. It will be sent to the MVI to update the Patient Master File fields date last treated and event reason.

> **NOTE:** The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A01^ADT_A01 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 3

\[ \] Additional Demographics 3

Patient Visit 3

\[ \] VA Specific Patient Information Segment

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A01^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

> Message Header 2

> Message Acknowledgement 2

Example Message Sent *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~REDACTED.VA.

GOV~DNS^20021004111252-0500^^ADT~A01^5000167926^P^2.4^^^AL^AL^US

EVN^A1^20021004111123-0500^^A1^12564~MVIUSER~TWO\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^20021004111123-0500^500

PID^1^1000002722V121387^1000002722V121387\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|500000564V890138\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20021004105118-0500^^MVIPATIENT~FIRSTNAME~MIDDLENAME\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19540430^

F^^^""~""~""~""~""\~~P~""\|\~~PROVIDENCE~RI\~\~~N^""^""^""^^M^0^^^^^^^^^^^^""^^

PD1^^^VAMCSITE~D~500

PV1^1^I^10B MED~""~""~&500^^^""~""~""^623~MVIDOCTOR~ONE^^^2^^^^^^^^SC VETERAN^^^2^^^^^^^^^^^^^^^^^^500A^^^^^20021004111123-0500^""

ZPD^1^^^^^^^^^^^^^^^^Y^^^^

<span id="_Toc131832204" class="anchor"></span>Figure ‑. ADT-A01 Admit/Visit Notification msg: Sent from VistA to MVI

Commit Level Acknowledgement Sent *<u>from</u>* MVI *<u>to</u>* the Sending System

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20051020060001-0500^^ACK^2001653344643^P^2.4

MSA^CA^5000167926

<span id="_Toc131832205" class="anchor"></span>Figure ‑. ADT-A01 Admit/Visit Notification msg: Commit acknowledgement sent from MVI to sending system

Application Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20021004111258-0500^^ACK~A01^200101854^P^2.4^^^AL^NE^USA

MSA^AA^500167926^0

<span id="_Toc131832206" class="anchor"></span>Figure ‑. ADT-A01 Admit/Visit Notification msg: Application acknowledgement sent from MVI to sending system

Commit Level Acknowledgement Returned *<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~MPI-REDACTED~DNS^20051114103124-0500^^ACK^50027446^P^2.4

MSA^CA^500167926

<span id="_Toc131832207" class="anchor"></span>Figure ‑. ADT-A01 Admit/Visit Notification msg: Commit acknowledgement returned to MVI

## ADT/ACK: Discharge/End Visit (Event A03)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An A03 event signals the end of a patient's stay in a healthcare facility. It signals that the patient's status has changed to "discharged" and that a discharge date has been recorded. (VistA PIMS Discharge a Patient option \[DG DISCHARGE PATIENT\]). It is also captured when the patient checks out of a non-stop code clinic. (VistA PIMS Appointment Check-in/Check-out option \[SDAM APPT CHECK IN/OUT\]—checkout action.) The MVI will capture this event in order to update the following:

- On the MVI: Fields DATE LAST TREATED (#29) and ADT/HL7 EVENT REASON (#30) located in the MPI FACILITY ASSOCIATION file (#985.5).
- In VistA: Fields DATE LAST TREATED (#.03) and ADT/HL7 EVENT REASON (#.07) located in the TREATING FACILITY LIST file (#391.91).

For non-admitted patients, an A03 event signals the end of a patient's visit to a healthcare facility. It could be used to signal the end of a visit for a one-time or recurring outpatient who is not assigned to a bed. It could also be used to signal the end of a visit to the Emergency Room.

> **NOTE:** The only data updated on the MVI from the ADT-A03 message is the Date Last Treated and Event Reason. No other demographic fields are reviewed or updated.

REF: The "Chapter" references below refer to the HL7 Standard Version 2.4 documentation.

ADT^A03^ADT_A03 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 3

\[ \] Additional Demographics 3

Patient Visit 3

\[ \] VA Specific Patient Information Segment

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A03^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example Message Sent *<u>to</u>* the MVI *<u>from</u>* a VistA System

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~REDACTED.VA.

GOV~DNS^20021003121509-0500^^ADT~A03^000167794^P^2.4^^^AL^AL^US

EVN^A2^20021003121048-0500^^A2^12564~MVIUSER~TWO\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^20021003121048-0500^500

PID^1^1000000703V285248^1000000703V285248\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|500000561V641849\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20021003113450-0500\|500000562V707794\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20021003120852-0500^^MVIPATIENT~DAKOTA\~~TST\~\~~L^""^19370525^M^^^""~""~""~""~""\~~P~""\|\~~""~""\~\~~N^""^""^""^^""^""^^^^^^^^^^^^""^^

PD1^^^VAMCSITE~D~500

PV1^1^I^10B MED~""~""~&500^^^10B MED~""~""^623~MVIDOCTOR~ONE^^^2^^^^^^^^SC VETERAN^^^2^^^^^^^^^^^^^^^17^^^^^^^^20021003120920-0500^20021003121048-0500

ZPD^1^^^^^^^^^^^^^^^^Y^^^^

<span id="_Toc131832208" class="anchor"></span>Figure ‑. ADT-A03 Discharge/End Visit msg: Sent to MVI from VistA

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20051020060001-0500^^ACK^2001653344643^P^2.4

MSA^CA^000167794

<span id="_Toc131832209" class="anchor"></span>Figure ‑. ADT-A03 Discharge/End Visit msg: Commit acknowledgement sent from MVI to sending system

Application Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20021003121526-0500^^ACK~A03^200101662^P^2.4^^^AL^NE^USA

MSA^CA^000167794^

<span id="_Toc131832210" class="anchor"></span>Figure ‑. ADT-A03 Discharge/End Visit msg: Application acknowledgement sent from MVI to sending system

Commit Level Acknowledgement Returned *<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~MPI-REDACTED~DNS^20051114103124-0500^^ACK^50027446^P^2.4

MSA^CA^200101662

<span id="_Toc131832211" class="anchor"></span>Figure ‑. ADT-A03 Discharge/End Visit msg: Commit acknowledgement returned to MVI

## ADT/ACK: Link Patient Information (Event A24)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The A24 event is used when the patient in the first PID segment needs to be linked to the patient in the second PID segment and when both patient identifiers identify the same patient. Linking two or more patients does not require the actual merging of patient information; following a link event, the affected patient data records should remain distinct. For example, hospital A, hospital B, and hospital C would each keep their own records on a patient, but an A24 link event would be sent to the VHA MVI to enable the coupling of ID information with the Enterprise ID number (ICN or VPID). This event is not meant to link mothers and babies since a field exists () for that purpose. This event is a bi-directional event it is used to link a hospital record ID to the Enterprise ID (ICN or VPID) as identified above or from the MVI out to signal either the linking of two hospital records or two enterprise id's. When the A24 event involves two different ICNs, the first ICN replaces the second ICN.

> **NOTE:** VistA MPI/PD Business Rule for DUPLICATE ICNs

> This business rule prevents two different patient records from having the same ICN value. More than one patient in a single PATIENT file (#2) cannot have the same ICN. For example, let's say that the MPI returned an ICN to your local PATIENT file (#2) for a patient who previously did not have one assigned. If that same ICN is currently assigned to a different patient in your PATIENT file (#2), an exception (problem) message is sent to the MPIF EXCEPTIONS mail group, and the patient is sent to the MPI to be added as a new ICN entry. \[Change made with MPIF\*1.0\*43, RG\*1.0\*43 and MPI\*1.0\*38, prior to these patches, the patient would have received a Local ICN\].

When this message is sent, the fields included should be pertinent to communicate this event. When other important fields change, it is recommended that the A08 (update patient information) event be used in addition.

> **NOTE:** Other demographic fields are not updated from the A24. If there are other data changes an ADT-A31 message should be triggered.

REF: The "Chapter" references below refer to the HL7 Standard Version 2.4 documentation.

ADT^A24^ADT_A24 ADT Message Chapter

Message Header 2

Event Type 3

Patient (1) Identification 3

\[ \] Patient (1) Additional Demographics 3

\[ \] Patient (1) Visit 3

Patient (2) Identification 3

\[ \] Patient (2) Additional Demographics (Not sent) 3

\[ \] Patient (2) Visit (Not Sent) 3

\[ \] VA Specific Patient Information Segment (Not sent from the MVI; however, this segment is sent from VistA.)

\[{[OBX](#obx-observationresult-hl7-segment)}\] Observation/Result 7

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A24^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ADT-A24 Example 1

The example message below is an ADT-A24 message sent from the VAMC (identified by station# 500) to the MVI. The key pieces of information is PID-3 in both PID segments which contain the ICN that the system is requesting that its source ID (100000082) be linked to ICN 1001170560V235869. This same message example would be used by a non-VistA system to request linkage of the non-VistA system to the ICN specified in the 1<sup>st</sup> PID segment.

ADT-A24 Message Sent *<u>to</u>* the MVI *<u>from</u>* the Sending System Attempting to Subscribe to the ICN

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20020921203833-0500^^ADT~A24^000167165^P^2.4^^^AL^AL^

EVN^^^^^12556~MVIUSER~ONE\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^^500

PID^1^1000000560V235869^1000000560V235869\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|

000064567\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|100000082\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^MVIPATIENT~PTNAME3\~\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19780303^M^^^876 TIGER DRIVE~""~BIRMINGHAM~AL~35209\~~P~""\|\~~TUSCALOOSA~AL\~\~~N^073^(876)555-5555^""^^M^0^^^^^^^^^^^^""^^

PD1^^^VAMCSITE2~D~998

PID^2^1000000560V235869^1000000560V235869\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|

000064567\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|100000082\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^MVIPATIENT~PTNAME3\~\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19780303^M^^^876 TIGER DRIVE~""~BIRMINGHAM~AL~35209\~~P~""\|\~~TUSCALOOSA~AL\~\~~N^073^(876)555-5555^""^^M^0^^^^^^^^^^^^""^^

ZPD^1^^^^^^^^^^^^^^^^Y^^^^

<span id="_Toc131832212" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: message sent to MVI

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.FO-

VAMCSITE.VA.GOV~DNS^20051024133014-0500^^ACK^2001661670143^P^2.4

MSA^CA^000167165

<span id="_Toc131832213" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Commit acknowledgement sent from MVI to sending system

Application Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20020921203840-0500^^ACK~A24^200100069^P^2.4^^^AL^NE^

MSA^AA^000167165^^^^DFN=100000082

<span id="_Toc131832214" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Application acknowledgement sent from MVI to sending system

Commit Level Acknowledgement Returned *<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^MPI-REDACTED~DNS^20051109124551-0500^^ACK^500917674^P^2.4

MSA^CA^200100069

<span id="_Toc131832215" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Commit acknowledgement returned to MVI

ADT-A24 Example 2

The example message below is an ADT-A24 message sent from the MVI to a subscribing system to tell them of a change in ICN assignment. The key piece of information is in PID-3 in the PID segments, which contain the ICN that the subscribing system is to update. The ICN value in PID2 is being updated to the ICN value in PID1.

> **NOTE:** When the MPI initiates the ADT-A24 to tell a subscriber that a change to ICN has happened, until the Application Level Acknowledgement is returned, the subscriber is not moved to the ICN in the 1<sup>st</sup> PID segment. It is part of the complete processing of the ADT-A24 event.

> **NOTE:** Fewer fields are populated in the ADT-A24 message when it originates on the MPI and is sent to VistA and non-VistA systems. This is because the MPI doesn't store all the fields that VistA does.

ADT-A24 Message Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System, Notifying Sending System of Change to ICN Assignment

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^20041110132901-0500^^ADT~A24^200890416^P^2.4^^^AL^AL^

EVN^A24^20041110132901-0500

PID^1^^1008520398V272129\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|036664114\~\~~USSSA&

&0363~SS~VA FACILITY ID&553&L\|7171324\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^^

MVIPATIENT~CAROL\~\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19690303^F^^^\~~NEW YORK CITY~36\~\~~N^^^^^^

PD1^^^VAMCSITE1,MI~D~553

PID^2^^100852999V383128\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|036664114\~\~~USSSA&

&0363~SS~VA FACILITY ID&553&L\|7171324\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^^

MVIPATIENT~CAROL\~\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19690303^F^^^\~~NEW YORK CITY~36\~\~~N^^^^^^

<span id="_Toc131832216" class="anchor"></span>Figure 2‑. ADT-A24 Link Patient Information msg: Sent from MVI to sending system

Commit Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^

200M~MPI-REDACTED~DNS^20051024133014-0500^^ACK^2001661670143^P^2.4

MSA^CA^2000890416

<span id="_Toc131832217" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Commit acknowledgement sent to MVI from sending system

Application Level Acknowledgement Returned to MVI *<u>from</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^

200M~MPI-REDACTED~DNS^20041110132914-0400^^ACK~A24^55370230^P^2.4^^^AL^NE^

MSA^AA^200890416^^^^ICN=1008520398V272129

<span id="_Toc131832218" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Application acknowledgement returned to MVI

Commit Level Acknowledgement Returned *<u>from</u>* the MVI *<u>to</u>* Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^20051109124551-0500^^ACK^200917675^P^2.4

MSA^CA^55370230

<span id="_Toc131832219" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Commit acknowledgement returned from MVI to sending system

ADT-A24 Example 3

The example message below is an ADT-A24 message sent from the MVI to a subscribing system to tell them of a change in the local identifier. The key piece of information is in PID-3 in the PID segments, which contain the local identifier. The local identifier value in PID2 (5000) is being updated to the local identifier value in PID1 (100000087).

The ADT-A24 is sent from the MVI to sites after a local duplicate record merge has occurred, notifying the subscriber(s) of the change to the local identifier (DFN).

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20020921203833-0500^^ADT~A24^200167165^P^2.4^^^AL^AL^

EVN^^^^^12556~MVIUSER~ONE\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^^500

PID^1^1001170566V325869^1001170566V325869\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|

000064567\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|100000087\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^MVIPATIENT~PTNAME3\~\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19780303^M^^^876 TIGER DRIVE~""~BIRMINGHAM~AL~35209\~~P~""\|\~~TUSCALOOSA~AL\~\~~N^073^(876)555-5555^""^^M^0^^^^^^^^^^^^""^^

PD1^^^VAMCSITE2~D~998

PID^2^1001170565V325869^1001170565V325869\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|000064567\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|5000\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^MVIPATIENT~PTNAME3\~\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19780303^M^^^876 TIGER DRIVE~""~BIRMINGHAM~AL~35209\~~P~""\|\~~TUSCALOOSA~AL\~\~~N^073^(876)555-5555^""^^M^0^^^^^^^^^^^^""^^

<span id="_Toc131832220" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Sent from MVI to sites after local merge notifying subscriber(s) of change to DFN

Commit Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* Sending System

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20051024133014-0500^^ACK^50016616^P^2.4

MSA^CA^200167165

<span id="_Toc131832221" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Commit acknowledgement sent to MVI from sending system

Application Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* Sending System

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20020921203840-0500^^ACK~A24^500111069^P^2.4^^^AL^NE^

MSA^AA^200167165^^^^DFN=100000087

<span id="_Toc3901113" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Application acknowledgement sent to MVI from sending system

Commit Level Acknowledgement Returned *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^20051109124551-0500^^ACK^200917333^P^2.4

MSA^CA^500111069

<span id="_Toc131832223" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Commit acknowledgement returned from MVI to sending system

ADT-A24 Example 4

The example message below is an ADT-A24 message sent from the VistA site to tell them MVI that they just linked to another ICN during the Potential Match Review process. The key piece of information is in PID-3 in the PID segments, which contain the Primary ICN (1008520566V385026) and Deprecated ICN (1008520577V394026). The Deprecated ICN value in PID2 (1008520577V394026) is being updated to the Primary ICN value in PID1 (1008520566V385026).

Message Sent *<u>to</u>* the MVI *<u>from</u>* VistA to Link PID2 ICN to PID1 ICN

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20020921203833-0500^^ADT~A24^5000167165^P^2.4^^^AL^AL

EVN^A24^20050401125324-0500

PID^1^^1000000566V385026\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666233445\~\~~USSSA&&

0363~SS~VA FACILITY ID&200M&L\|000000549\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L

1008520577V394026\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20020207^^DRI~FRIDAY~

AFTERNOON\~\~\~~L^MVIPATIENT~APRIL\~\~\~\~~M^19610401^M^^^\~~BUTLER~42\~\~~N^^^^^^^^^^^^^^^^^^^^

PID^2^^1008520577V394026\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666233445\~\~~USSSA&&

0363~SS~VA FACILITY ID&200M&L\|000000549\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^DRI~

FRIDAY~AFTERNOON\~\~\~~L^MVIPATIENT~APRIL\~\~\~\~~M^19610401^M^^^\~~BUTLER~42\~\~~N^^^^^^^^^^^^^^^^^^^^

PD1^^^VAMCSITE~D~500

<span id="_Toc3901115" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Sent to the MVI from VistA to Link PID2 ICN to PID1 ICN

Application Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20020921203840-0500^^ACK~A24^200100069^P^2.4^^^AL^NE^

MSA^AA^5000167165^^^^DFN=10000549

<span id="_Toc3901116" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Application acknowledgement sent from MVI to sending system

Commit Level Acknowledgement Returned *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.FO-

VAMCSITE.VA.GOV~DNS^20051024133014-0500^^ACK^2001661670143^P^2.4

MSA^CA^5000167165

<span id="_Toc3901117" class="anchor"></span>Figure ‑. ADT-A24 Link Patient Information msg: Commit acknowledgement sent from MVI to sending system

ADT-A24 Example 5 – Message *<u>from</u>* the MVI *<u>to</u>* PSIM via HLO

The example message below is an ADT-A24 message sent from the MVI to tell PSIM that they need to link two ICNs together. The key piece of information is in PID-3 in the first PID segments, which contain the Primary ICN (1000000877V600753) and Deprecated ICN (1008521212V088641). The Deprecated ICN value in PID2 (1008521212V088641) is being updated to the Primary ICN value in PID1 (1000000877V600753).

Message *<u>from</u>* the MVI *<u>to</u>* PSIM via HLO

MSH^~\|\\^MPI^200M~HL7.MPI-REDACTED:5026~DNS^PSIM^

HL7.200PS~TSTCRN.REDACTED.VA.GOV:5027~DNS^

20061107082414-0500^^ADT~A24~^200M 780^P~^2.4^^^AL^AL^USA

EVN^A24^20061107082414-0500^^^^^500

PID^1^^1000000877V600753\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L~

20040915114610~\|666888889\~\~~USSSA&&0363~SS~VA FACILITY ID&200M&L^

^MVIPATIENT~MARV\~\~\~\~~L^^19900303^M^^^^^^^^3^^^^^^^^^^^^^^^^^

PID^2^^1008521212V088641\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~

\|666888889\~\~~USSSA&&0363~SS~VA FACILITY ID&200M&L^

^MVIPATIENT~MARVIN\~\~\~\~~L^^19900303^M^^^^^^^^^^^^^^^^^^^^^^^^^\|

PD1^^^VAMCSITE1,MI~D~553

<span id="_Toc3901118" class="anchor"></span>Figure ‑. Message sent *<u>from</u>* the MVI to PSIM via HLO

Accept ACK:

MSH\|^~\\\|PSIM\|553^HL7.TSTCRN.REDACTED.VA.GOV:5027^DNS\|MPI\|

200M^HL7.MPI-REDACTED:5026^DNS\|

20061107082419-0400\|\|ACK \|553 354\|P^\|2.4\|\|\|AL\|NE\|

MSA\|AA\|200M 780\|\|

<span id="_Toc3901119" class="anchor"></span>Figure ‑. Message *<u>from</u>* the MVI *<u>to</u>* PSIM via HLO: Accept ACK

Application ACK:

MSH\|^~\\\|PSIM\|553^HL7.TSTCRN.REDACTED.VA.GOV:5027^DNS\|MPI\|

200M^HL7.MPI-REDACTED:5026^DNS\|

20061107082419-0400\|\|ACK^A24^ACK\|553 355\|P^\|2.4\|\|\|AL\|NE\|

MSA\|AA\|553 355\|

<span id="_Toc3901120" class="anchor"></span>Figure ‑. Message *<u>from</u>* the MVI *<u>to</u>* PSIM via HLO: Application ACK

## QBP/RSP: Find Candidates (QBP) and Response (RSP) (events Q22 and K22)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This query/response returns list of candidates matching demographic data specified by the input parameters. This HL7 message is designed for interaction between a client system and the MVI. The query consists of a set of demographics for a person, and the response is the list of candidates considered by the MVI to match that set.

Each returned person, specified by a PID segment, can also have an optional *QRI - Query Response Instance* segment containing information about the quality of the match.

The RSP-K22 message is the application level acknowledgement to the QBP-Q22 message and must be processed at the non-VistA system. The RSP-K22 message tells the QBP-Q22 sender the results of processing said message.

> **NOTE:** At this time the MPI only supports queries by DFN/Site pair.

QBP^Q22^QBP_Q21 Query By Parameter Chapter

Message Header 2

Query Parameter Definition Segment 5

Response Control Parameters 5

\[\] Continuation Pointer 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

RSP^K22^RSP_K22 Segment Pattern Response Group Control Chapter

Message Header 2

[MSA](#msa-message-acknowledgement-segment) Message Acknowledgement 2

\[\] Error 2

Query Acknowledgement 5

Query Parameter Definition Segment 5

Query Result Cluster,

{ Begin PID Group

\[ Patient Identification 3

\[\]\] Additional Demographics 5

Query Response Instance 5

} End PID Group,

End Query Results

\[ \] Continuation Pointer 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example Groups of Q22/K22 Query and Response Message Pairs

The following are example groups of Q22/K22 query and response message pairs. In each group, the first message is the QBP-Q22 query sent to the MVI and the second message is the RSP-K22 response sent back to the sending system resulting from the query. These example scenarios show:

1.  Site/DFN pair is found on the MVI—Query processed.
2.  Sending site is not found in the MPI SITE MONITOR file—Query rejected.
3.  Site/DFN pair is not known to the MVI—No match found on the MVI.

Depending on the value passed in the QPD segment, for the User Parameter field (sequence \#6) the query may also add an Association of the sending site to the DFN/Site pair, and/or add the sending site as a system of interest for the ICN associated with this DFN/Site pair or if the DFN/Site pair isn't known create a record of interest so that when it does become known to the MVI it can associate the sending site with it and inform the sending site of the ICN.

Figure 2‑31 shows a QBP-Q22 query sent *<u>to</u>* the MVI

MSH^~\|\\^MPI^888~DEVELOPER.VA.GOV~DNS^MPI^200M~MPI-REDACTED~DNS^200412091430-0500^^QBP~Q22^888387888^P^2.4^^^AL^AL^

QPD^Q22~FIND CANDIDATES~HL72.4^888387888^@PID.3.1~271\|@PID.3.2~""\|@PID.3.3~""\|

@PID.3.4~USVHA&&0363\|@PID.3.5~PI\|@PID.3.6~VA FACILITY ID&500&L^VHA MPI^1.0^BT

RCP^I^1~RD^R^^N^

<span id="_Ref96231358" class="anchor"></span>Figure ‑. QBP-Q22 Find Candidates query message sent to MVI

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPI^200M~MPI-REDACTED~DNS^MPI^888~DEVELOPER.VA.GOV~DNS

^20051028060001-0500^^ACK^2001672355556^P^2.4

MSA^CA^888387888

<span id="_Toc131832225" class="anchor"></span>Figure ‑. QBP-Q22 Find Candidates query msg sent to MVI: Commit acknowledgement sent from MVI to sending system

This query, Figure 2‑31, is asking both (BT) a treating facility entry and a site association to be created for sending station 888 for patient with a DFN equal to 271 at Station Number 500. If that DFN/Site pair is found, add the sending site to the site association for the treating facility for station 500 *and* add the sending site as its own treating facility. Returning RSP-K22 message with the PID segment containing the information regarding this patient, indicating that the patient was found. (Figure 2-16).

> **NOTE:** If a treating facility entry is created for an ICN as a result of the QBP~Q22 query, that will trigger back out to all systems subscribing to that ICN a treating facility update message (MFN-M05).

MSH^~\|\\^MPI^200M~MPI-REDACTED~DNS^MPI^888~DEVELOPER.VA.GOV~DNS^

20041210123536-0500^^RSP~K22^200896113^P^2.4^^^AL^NE^

MSA^AA^888387888

QAK^888387888^OK^Q22~FIND CANDIDATES~HL72.4^1

> QPD^Q22~FIND CANDIDATES~HL72.4^888387888^@PID.3.1~271\|@PID.3.2~""\|@PID.3.3~""\|

@PID.3.4~USVHA&&0363\|@PID.3.5~PI\|@PID.3.6~VA FACILITY ID&500&L^VHA MPI^1.0^BT

PID^1^^1000008794V381470\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|000456780\~\~~USSSA&&

0363~SS~VA FACILITY ID&500&L\|271\~\~~USVHA&&0363~PI~VA FACILITYID&500&L^^  
MVIPATIENT~PATIENT1\~\~\~\~~L^^19810808^M^^^^^^^^^^^^^^^^^^^^^198705211140-0500^^

<span id="_Ref96231407" class="anchor"></span>Figure ‑. RSP-K22 Response msg from QBP-Q22 back to sending system: Site/DFN pair found on MVI

> **NOTE:** Notice in Figure 2‑33 that the number 1 at the end of the QAK segment signifying the number of matches. This will correspond to the number of PID segment(s) returned as matches to the query criteria. Since we are working just with Site/DFN at this time the response will either contain no matches or 1 match.

Commit Level Acknowledgement Returned *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPI^888~DEVELOPER.VA.GOV~DNS^MPI^200M~MPI-REDACTED~DNS

^20051028060001-0500^^ACK^2001672355647^P^2.4^^\|

MSA^CA^200896113^Message Processed

<span id="_Toc131832227" class="anchor"></span>Figure ‑. RSP-K22 Commit acknowledgement: Response msg from QBP-Q22 back to sending system

Messaging Example when Sending Facility is Unknown to MVI

This query, Figure 2-17, is asking both (BT) a treating facility entry and a site association to be created for sending station 777 for patient with a DFN equal to 22710 at Station Number 500. If that DFN/Site pair is found, add the sending site to the site association for the treating facility for station 500 *and* add the sending site as its own treating facility. Returning RSP-K22 message with the PID segment containing the information regarding this patient, indicating that the patient was found.

MSH^~\|\\^MPI^777~MVIDEVELOPER.MED.VA.GOV~DNS^MPI^200M~MPI-REDACTED~DNS^

200410140939-0500^^QBP~Q22^7777387888^P^2.4

QPD^Q22~FIND CANDIDATES~HL72.4^888387888^@PID.3.1~22710\|@PID.3.2~""\|@PID3.3~""\|

@PID.3.4~USVHA&&0363\|@PID.3.5~PI\|@PID.3.6~VA FACILITY ID&500&L^VHA MPI^1.0^BT

RCP^I^1~RD^R^^N^

<span id="_Ref96231622" class="anchor"></span>Figure ‑. QBP-Q22 Find Candidates query msg sent to MVI

Commit Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^MPI^200M~MPI-REDACTED~DNS^MPI^777~DEVELOPER.VA.GOV~DNS

^20051028060001-0500^^ACK^2001672355646^P^2.4

MSA^CA^7777387888

<span id="_Toc131832229" class="anchor"></span>Figure ‑. QBP-Q22 Find Candidates query msg sent to MVI: Commit acknowledgement sent to the MVI from sending system

The RSP-K22 response message, Figure 2‑37, shows that the sending site was not found in the MPI SITE MONITOR file. Hence, the QBP-Q22 message is rejected by sending back the RSP-K22 message as follows.

MSH^~\|\\^MPI^200M~MPI-REDACTED~DNS^MPI^777~MVIDEVELOPER.MED.VA.GOV~DNS^

20050215082223-0500^^RSP~K22^200899812^P^2.4^^^AL^NE^

MSA^AR^7777387888^System isn't in MPI Site Monitor file - rejected

QAK^7777387888^AR^Q22~FIND CANDIDATES~HL72.4^0

QPD^Q22~FIND CANDIDATES~HL72.4^888387888^@PID.3.1~22710\|@PID.3.2~""\|@PID3.3~""

\|@PID.3.4~USVHA&&0363\|@PID.3.5~PI\|@PID.3.6~VA FACILITY ID&500&L^VHA MPI^1.0^BT

<span id="_Ref96231718" class="anchor"></span>Figure ‑. RSP-K22 Response msg from QBP-Q22 back to sending system: sending site not found on MVI

Commit Level Acknowledgement Returned *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPI^777~DEVELOPER.VA.GOV~DNS^MPI^200M~MPI-REDACTED~DNS^

20051028060001-0500^^ACK^2001672355777^P^2.4

MSA^CA^200899812

<span id="_Toc131832231" class="anchor"></span>Figure ‑. RSP-K22 Response msg from QBP-Q22: Commit acknowledgement

This query, Figure 2-19, is asking for a site association (AS) to be created for sending station 888 for patient with a DFN equal to 22710 at Station Number 500. If that DFN/Site pair is found, add the sending site to the site association for the treating facility for station 500. Returning RSP-K22 message with the QAK segment containing 0 match notation and no PID segment (Figure 2-20).

Figure 2‑39 Shows a QBP-Q22 Query Sent *<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^MPI^888~DEVELOPER.VA.GOV~DNS^MPI^200M~MPI-REDACTED~DNS^

200412091430-0500^^QBP~Q22^888387888^P^2.4

QPD^Q22~FIND CANDIDATES~HL72.4^888387888^@PID.3.1~22710\|@PID.3.2~""\|@PID3.3~""\|

@PID.3.4~USVHA&&0363\|@PID.3.5~PI\|@PID.3.6~VA FACILITY ID&500&L^VHA MPI^1.0^AS

RCP^I^1~RD^R^^N^

<span id="_Ref96232696" class="anchor"></span>Figure ‑. QBP-Q22 Find Candidates query msg sent to MVI

Commit Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* the Sending System

MSH^~\|\\^MPI^200M~MPI-REDACTED~DNS^MPI^888~MVIDEVELOPER.MED.VA.GOV~DNS^

20051028060001-0500^^ACK^2001672355807^P^2.4

MSA^CA^888387888

<span id="_Toc131832233" class="anchor"></span>Figure ‑. QBP-Q22 Find Candidates query msg: Commit acknowledgement sent to MVI

Figure 2‑41, shows an example RSP-K22 response when a Site/DFN pair is not found (no match found) on the MVI.

MSH^~\|\\^MPI^200M~MPI-REDACTED~DNS^MPI^888~MVIDEVELOPER.MED.VA.GOV~DNS^

20050215081307-0500^^RSP~K22^200899809^P^2.4^^^AL^NE^

MSA^AA^888387888

QAK^888387888^NF^Q22~FIND CANDIDATES~HL72.4^0

QPD^Q22~FIND CANDIDATES~HL72.4^888387888^@PID.3.1~22710\|@PID.3.2~""\|@PID3.3~""\|

@PID.3.4~USVHA&&0363\|@PID.3.5~PI\|@PID.3.6~VA FACILITY ID&500&L^VHA MPI^1.0^AS

<span id="_Ref96232766" class="anchor"></span>Figure ‑. RSP-K22 Response msg from QBP-Q22 back to sending system: Site/DFN pair not known to MVI

Commit Level Acknowledgement Returned *<u>from</u>* the MVI *<u>to</u>* the Sending System

MSH^~\|\\^MPI^888~MVIDEVELOPER.MED.VA.GOV~DNS^MPI^200M~MPI-REDACTED~DNS^

20051028060001-0500^^ACK^2001672355887^P^2.4

MSA^CA^200899809

<span id="_Toc3901132" class="anchor"></span>Figure ‑. RSP-K22 Response msg from QBP-Q22: Commit acknowledgement

Figure 2‑43 shows an example of the QBP-Q22 message sent from the MVI to PSIM to search for match(es) or potential match(es) for the traits passed.

MSH^~\|\\^MPI APP^200M~HL7.MPI.REDACTED.VA.GOV:5026~DNS^PSIM^200PS~ps-dev.commserv.healthevet.va.gov:8090~DNS^20090105104810-0500^^QBP~Q22~^200M 110659^T~^2.4^^^AL^AL^USA

QPD^Q22~Find Candidates~HL72.4^1^@PID.3~000456789\~\~~USSSA&&0363~SS~VA FACILITY ID

&553&L\|@PID.3\~\~\~~USVBA&&0363~PN~VA FACILITY ID&553&L\|@PID.5~MVIPATIENT~PATIENT1\~\~\~\~\~~

L\|@PID.11~Street line1~Street line2~VAMCSITE~NY~12144\~~P~Street line3\|@PID.7~1955

0722\|@PID.13~(518)555-5555~PRN~PH\|@PID.8~F\|@PID.24~N\|^INITIATE^7.5

RCP^I^100~RD^R^^N^^

<span id="_Ref219105534" class="anchor"></span>Figure ‑. QBP-Q22 msg sent from MVI to PSIM to search for match(es) based on traits passed

Figure 2‑44 shows an example of the RSP-K22 response from PSIM when the MVI has sent a QBP-Q22 to search for match(es) or potential match(es) for the traits passed.

MSH^~\|\\^PSIM^200PS~200PS.FO-REDACTED.GOV~DNS^MPI APP^200M~TLMPI.FO-REDACTED.GOV~DNS^20090106082334.975-0500^^RSP~K22^12312482149750906562915^T^2.4^^^AL^NE

MSA^AA^200M 110659

QAK^1^OK^Q22~Find Candidates~HL72.4^4

QPD^Q22~Find Candidates~HL72.4^1^@PID.3~000456789\~\~~USSSA&&0363~SS~VA FACILITY ID&553&L\|@PID.3\~\~\~~USVBA&&0363~PN~VA FACILITY ID&553&L\|@PID.5~MVIPATIENT~PATIENT1\~\~\~\~\~~L\|@PID.11~Street line1~Street line2~VAMCSITE~NY~12144\~~P~Street line3\|@PID.7~19550722\|@PID.13~(518)555-5555~PRN~PH\|@PID.8~F\|@PID.24~N\|^INITIATE^7.5

PID^1^^1000000921V771535\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666000702\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^MVIPATIENT~PATIENT1\~\~\~\~~L

QRI^86^^102-145~INITIATE

PID^2^^1000000921V771535\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L^^MVIPATIENT~PATIENT1\~\~\~\~~L

QRI^86^^102-145~INITIATE

PID^3^^1000000438V882204\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|7171584\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^^MVIPATIENT~PATIENT1\~\~\~\~~L

QRI^23^^102-145~INITIATE

PID^4^^1000000438V882204\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L^^MVIPATIENT~PATIENT1\~\~\~\~~L

QRI^23^^102-145~INITIATE

<span id="_Ref219105475" class="anchor"></span>Figure ‑. Example query for list of persons matching the name MVIPATIENT,ONE with the gender Male, SSN 666456789, and other traits noted

Two candidates were returned. Notice the number 2 at the end of the QAK segment signifying the number of matches. Each has a PID and QRI segment, and the QRI segment in each case gives a confidence factor for each of the candidates

Figure 2‑45, shows an example of the QBP-Q22 and the responding RSP-K22 when no match was found for the patient being searched for.

MSH^~\|\\^MPI APP^200M~HL7.MPI-REDACTED:5026~DNS^PSIM^200PS~ps-dev.commserv.healthevet.va.gov:8090~DNS^20081031093516-0500^^QBP~Q22~^200M 109030^P~^2.4^^^AL^AL^USA

QPD^Q22~Find Candidates~HL72.4^1^@PID.3~666542849\~\~~USSSA&&0363~SS~VA FACILITY ID

&500&L\|@PID.5~MVIDEVELOPER~ALIAS~TOM\~\~\~\~~L\|@PID.11\~\~\~\~\~\~\~\~~P\|@PID.7~19700202\|@PID.13~\|@PID.8~M\|^INITIATE^7.5

RCP^I^100~RD^R^^N^^

MSH^~\|\\^PSIM^200PS~200PS.FO-REDACTED.GOV~DNS^MPI APP^200M~MPI-REDACTED~DNS^20081031093529.963-0500^^RSP~K22^12254601299760267621555^P^2.4^^^AL^NE

MSA^AA^200M 109030

QAK^1^NF^Q22~Find Candidates~HL72.4^0

QPD^Q22~Find Candidates~HL72.4^1^@PID.3~666542849\~\~~USSSA&&0363~SS~VA FACILITY ID

&500&L\|@PID.5~MVIDEVELOPER~ALIAS~TOM\~\~\~\~~L\|@PID.11\~\~\~\~\~\~\~\~~P\|@PID.7~19700202\|@PID.13\|@PID.8~M\|^INITIATE^7.5

<span id="_Ref219105690" class="anchor"></span>Figure ‑. Example of QBP-Q22 and the responding RSP-K22 when no match was found for the patient being searched for.

## ADT/ACK: Merge Patient Identifier List (Event A40)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A merge has been done at the patient record level (i.e., DFN and/or record ID on the Associated System). That is, two [PID-3 - patient identifier list](#pid-3-patient-identifier-list-cx-00106) identifiers have been merged into one.

An A40 event is used to signal a merge of records for a patient that was incorrectly filed under two different identifiers. The "incorrect source identifier", identified in the MRG segment ([MRG-1 - prior patient identifier list](#mrg-1-prior-patient-identifier-list-cx-00211)) is to be merged with the required "correct target identifier" of the same "identifier type code" component identified in the PID segment (). The "incorrect source identifier" would then logically never be referenced in future transactions. It is noted that some systems may still physically keep this "incorrect identifier" for audit trail purposes or other reasons associated with database index implementation requirements. However, the current VHA MVI implementation does not support the referencing of the merged record id but identify that there are potential benefits to supporting that functionality so future implementation will support that function.

The result of the ADT-A40 message being processed at the MVI is an ADT-A24 Link Patient message sent to each site in the treating facility list and any sites in the site association list for those treating facilities (including the site that did the merge), not including the site that the ADT-A40 message was received from, with the "FROM" ICN/DFN in MRG-1 (1001170164V123456/112978) to change the "TO" ICN/DFN in PID-3 (1001169886V995666/7169971).

The ADT-A40 message is sent during the special processing routine section of the VistA Duplicate Record Merge software, which happens before the actual merging of the PATIENT (#2) file entries has happened. Once the merge has successfully completed, an ADT-A31 message is sent to the MVI with the current view of the TO record, which may contain different information for other fields stored on the MVI as a result of the merge.

The MFN-M05 message may also be triggered if the result of the linking of the two ICNs resulted in a new treating facility list.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A40^ADT_A40 ADT Message Chapter

Message Header 2

Event Type 3

{ Patient Identification 3

\[ \] Additional Demographics 3

Merge Information 3

\[ \] } Patient Visit 3

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A40^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example Message Sent to the MVI From VistA

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20021015094425-0500^^ADT~A40^5000168695^P^2.4^^^AL^AL^

EVN^^^^^12564~MVIUSER~ONE\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^^500

PID^1^1000009886V995666^1000009886V995666\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|000094344\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|7169971\~\~~USVHA&&

0363~PI~VA FACILITY ID&500&L\|1000094344\~\~~USVBA&&0363~PN~VA FACILITY ID&500&L\|

666600373V383422\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20011005120510-0500\|

1000009143V626477\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20020611130452-0500\|1000009878V490521\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20020611152848-0500^^MVIPATIENT~CAROL~MIDDILE NAME\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19690303^F ^^^500 MAIN STREET~NOT USED~JACKSONVILLE~NC~28546\~~P~NOT USED\|\~~PROVIDENCE~RI\~\~~N^""^555-555-5555^""^^""^""^^^^^^^^^^^^20020506^^

PD1^^^VAMCSITE~D~500

MRG^1001170164V123456\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|112978\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^^^^^^MVIPATIENT~TWELEVE~

MIDDLE\~\~\~~L

<span id="_Toc131832236" class="anchor"></span>Figure ‑. ADT- A40 Merge Patient Identifier List msg: Sent to MVI from VistA

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* VistA

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20051028060001-0500^^ACK^2001672355997^P^2.4

MSA^CA^5000168695

<span id="_Toc131832237" class="anchor"></span>Figure ‑. ADT-A40 Merge Patient Identifier List msg: Commit acknowledgement sent from MVI to VistA

Application Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* VistA

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20021015094438-0500^^ACK~A40^200103350^P^2.4^^^AL^NE^

MSA^AA^5000168695^^^^DFN=7169971

<span id="_Toc131832238" class="anchor"></span>Figure ‑. ADT-A40 Merge Patient Identifier List msg: Application acknowledgement sent from MVI to VistA

Commit Level Acknowledgement Returned to the MVI From VistA

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20051028060001-0500^^ACK^500167235^P^2.4

MSA^CA^200103350

<span id="_Toc131832239" class="anchor"></span>Figure ‑. ADT-A40 Merge Patient Identifier List msg: Commit acknowledgement returned to MVI

## ADT/ACK: Move Patient Information Patient Identifier List (Event A43)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A move has been done at the patient record id level (i.e., a records ID moves from one ICN to another ICN) on the MVI. Identifier to be moved in the and [MRG-1 - prior patient identifier list](#mrg-1-prior-patient-identifier-list-cx-00211) will have the same value. The "from" (incorrect source patient ID) and "to" (correct target patient ID) identifiers have different values. All subordinate data sets associated with the identifier in [MRG-1 - prior patient identifier list](#mrg-1-prior-patient-identifier-list-cx-00211) are moved along with the identifier, from the "incorrect source patient ID" to the "correct target patient ID".

This event and the message syntax do, however, allow for the specification of a "new identifier" ([PID-3 - Patient identifier list](#pid-3-patient-identifier-list-cx-00106)), which may be application and/or implementation specific and therefore require site negotiation.

The fields included when this message is sent should be pertinent to communicate this event. When demographic data in other fields change, it is recommended that the A08 (update patient information) event be used in conjunction with this message. Since every system handles merges differently, an ADT-A31 (update person information) message could also be used instead of the ADT-A08 (update patient information). The HL7 2.4 specification documents the following usage: *The fields included when this message is sent should be the fields pertinent to communicate this event. When other fields change, it is recommended that the A31 (update person information) event be used for person level updates and A08 (update patient information) event for patient level updates.* However, all PID data associated with the "correct target identifier" ([PID-3 - Patient identifier list](#pid-3-patient-identifier-list-cx-00106)) are treated as updated information.

The "incorrect source identifier" would then logically never be referenced in future transactions. It is noted that some systems may still physically keep this "incorrect identifier" for audit trail purposes or other reasons associated with database index implementation requirements. However, currently within the VHA MVI implementation we do not support the referencing of the merged records but identify that there are potential benefits to supporting that reference and plan to support them in future releases.

> **NOTE:** ADT-A43 messages are only supported as an outbound message from the MPI. Inbound ADT-A43 messages will be negatively acknowledged.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A43 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 3

\[\] Additional Demographics 3

Merge Information 3

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A43^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example 1: Message Sent *<u>from</u>* MVI *<u>to</u>* Receiving System

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20020921204232-0500^^ADT~A43^200100101^P^2.4^^^AL^AL^

EVN^A43^20020921204232-0500^20020921204232-0500^^12556~MVIUSER~FOUR\~\~\~\~\~~USVHA&&

0363~L\~\~~NI~VA FACILITY ID&200M&L

PID^1^^1008520572V991480\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100000551\~\~~USVHA

&&0363~PI~VA FACILITY ID&500&L^^MVIPATIENT~PATIENT1~E\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^2780203^M

^^^^^^^^^^^000064567^^^^^^^^^^^^

MRG^1000000560V235869\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100000551\~\~~USVHA

&&0363~PI~VA FACILITY ID&500&L^^^^^^MVIPATIENT~PATIENT1~E\~\~\~~L

<span id="_Toc131832240" class="anchor"></span>Figure ‑. ADT-A43 Move Patient Information Patient Identifier List msg: Sent from MVI to subscribing system

Commit Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* Receiving System

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20051028060001-0500^^ACK^2001672355997^P^2.4

MSA^CA^200100101

<span id="_Toc131832241" class="anchor"></span>Figure ‑. ADT-A43 Move Patient Information Patient Identifier List msg: Commit acknowledgement sent to MVI

Application Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* the Receiving System

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20020921204250-0500^^ACK~A43^500167189^P^2.4^^^AL^NE^

MSA^AA^200100101^

<span id="_Toc131832242" class="anchor"></span>Figure ‑. ADT-A43 Move Patient Information Patient Identifier List msg: Application acknowledgement sent to MVI

Commit Level Acknowledgement Returned *<u>to</u>* the Receiving System *<u>from</u>* the MVI

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20051028060001-0500^^ACK^2001672355997^P^2.4

MSA^CA^500167189

<span id="_Toc131832243" class="anchor"></span>Figure ‑. ADT-A43 Move Patient Information Patient Identifier List msg: Commit acknowledgement returned from MVI to sending system

Example 2: Message Sent *<u>from</u>* MVI *<u>to</u>* PSIM via HLO

MSH^~\|\\^MPI^200M~HL7.MPI-REDACTED:5026~DNS^

PSIM^HL7.200PS~TSTCRN.REDACTED.VA.GOV:5027~DNS^

20061107082545-0500^^ADT~A43~^200M 782^P~^2.4^^^AL^AL^USA

EVN^A43^20061107082545-0500^^^^^200M^20061107082545-0500^^12564~CHESNEY~CHRISTI

NE\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&200M&L

PID^1^^1008521514V195551\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L~20061107082545~

\|666000107\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|666888889\~\~~USSSA&&0363~SS~VA F

ACILITY ID&200M&L^^MVIPATIENT~MARVIN\~\~\~\~~L^^19900303^M^^^^^^^^^^^^^^^^^^^^^^^^^

PD1^^^VAMCSITE~D~500

MRG^1000000877V600753\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|

666000107\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|666888889

\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L^^^^^^MVIPATIENT~MARV\~\~\~\~~L

<span id="_Toc3901144" class="anchor"></span>Figure ‑. Message Sent *<u>from</u>* MVI *<u>to</u>* PSIM via HLO

Commit ACK:

MSH\|^~\\\|PSIM\|553^HL7.TSTCRN.REDACTED.VA.GOV:5027^DNS\|MPI\|

200M^HL7.MPI-REDACTED:5026^DNS\|

20061107082419-0400\|\|ACK \|553 354\|P^\|2.4\|\|\|AL\|NE\|

MSA\|CA\|200M 782\|\|

<span id="_Toc3901145" class="anchor"></span>Figure ‑. Message Sent *<u>from</u>* MVI *<u>to</u>* PSIM via HLO: Commit ACK

Application Level ACK:

MSH\|^~\\\|PSIM\|553^HL7.TSTCRN.REDACTED.VA.GOV:5

027^DNS\|MPI\|200M^HL7.MPI-REDACTED:5026^DNS

\|20061107082549-0400\|\|ACK^A43^ACK\|553 357\|P^\|2.4\|\|\|AL\|NE\|

MSA\|AA\|200M 782

<span id="_Toc3901146" class="anchor"></span>Figure ‑. Message Sent *<u>from</u>* MVI *<u>to</u>* PSIM via HLO: Application Level ACK

## ADT/ACK: Register a Patient (Event A04)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An A04 event signals that the patient has been registered via the Register a Patient option \[DG REGISTER A PATIENT\]. It does not indicate that the person actually had a treatment session at that time, just that the registration event happened.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A04^ADT^A04 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 3

\[ \] Patient Additional Demographics 3

Patient Visit 3

\[\] Patient Visit – additional information 3

\[{}\] Observation/Result 7

\[\] VA Specific Patient Information Segment

\[\] VA Specific Service Period Segment (Passed but not used by MVI)

\[\] VA Specific Patient Eligibility Segment (Passed but not used by MVI)

\[\] VA Specific Emergency Contact Segment (Passed but not used by MVI)

\[\] VA Specific Employment Information Segment (Passed but not used by MVI)

\[\] VA Specific File/Field Segment (Passed but not used by MVI)

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A04^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example Message Sent *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~MPI-REDACTED~DNS^20021015084748-0500^^ADT~A04^500168673^P^2.4^^^AL^AL^US

EVN^^^^^12564~MVIUSER~TWO\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^^500

PID^1^1000009886V995666^1000009886V995666\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|000094344\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|7169971\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|000094344\~\~~USVBA&&0363~PN~VA FACILITY ID&500&L\|

666600373V383422\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20011005120510-0500\|

1000009143V626477\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20020611130452-0500\|

1000009878V490521\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20020611152848-0500^

^MVIPATIENT~JAMIE~MIDDLE NAME\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19690303^F^^^500 MAIN STREET~NOT USED~JACKSONVILLE~NC~99999\~~P~NOT USED\|\~~PROVIDENCE~RI\~\~~N^""^555-555-5555^

""^^""^""^^^^^^^^^^^^20020506^^

PD1^^^VAMCSITE~D~500^""

PV1^1^O^""^^^^^^^^^^^^^^^SC VETERAN^^^^^^^^^^^^^^^^^^^^^500A^^^^^^^^^^^15403

OBX^1

ZPD^1^^PROVIDENCE^RI^""^MVIFATHER,ONE^MVIMOTHER,TWO^""^20020506^""^0^""^""^6^""^""^""^0^""^""^""

ZSP^1^1^^""^""^""^""^""

ZEL^1^3^036-99-4344\~~^4344^""^000094344^""^1^SC VETERAN^""^""^""^""^""^""^""^""^

""^""^""^""^""

ZCT^1^1^MVISPOUSE,FOUR^""^""^""^""^""^""

ZEM^1^1^""^""^""^""^""^""

ZFF^2^

<span id="_Toc3901147" class="anchor"></span>Figure ‑. ADT-A04 Register a Patient msg: Sent to MVI from VistA

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* VistA

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20051020060001-0500^^ACK^2001653355533^P^2.4

MSA^CA^500168673

<span id="_Toc131832245" class="anchor"></span>Figure ‑. ADT-A04 Register a Patient msg: Commit acknowledgement sent from MVI to VistA

Application Level Acknowledgement Sent *<u>from</u>* MVI *<u>to</u>* VistANOTE: Error message returned as an example, this does not indicate that there is a need to resend the message. This actually generated a data quality exception on the MPI for the HC IDM team to address.

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20021015084805-0500^^ACK~A04^200103324^P^2.4^^^AL^NE^USA

MSA^AA^500168673^ Unable to update field 48 in MPI FACILITY ASSOCIATION ( \#985.5) file due to: The value '1' for field POW STATUS INDICATED? in file MPI FACILITY ASSOCIATION is not valid.

<span id="_Toc131832246" class="anchor"></span>Figure ‑. ADT-A04 Register a Patient msg: Application acknowledgement sent from MVI to VistA

Commit Level Acknowledgement Returned *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~MPI-AUSTING.MED.VA.GOV~DNS^20051020060001-0500^^ACK^5004563^P^2.4

MSA^CA^200103324

<span id="_Toc131832247" class="anchor"></span>Figure ‑. ADT-A04 Register a Patient msg: Commit acknowledgement returned to MVI from VistA

## ADT/ACK: Update Patient Information (Event A08)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This trigger event is used when any patient information has changed but when no other trigger event has occurred. For example, an A08 event can be used to notify the receiving systems of a change of address or a name change. We recommend that the A08 transaction be used to update fields that are not related to any of the other trigger events. The A08 event can include information specific to an episode of care, but it can also be used for demographic information only.

> **NOTE:** Updates to specific patient demographic data will trigger the broadcasting of a HL7 ADT-A08 message. Because there is no set way of identifying when an edit to patient information is complete, these edit events are marked as needing to be transmitted in the ADT/HL7 PIVOT file (#391.71). The background job VAFC BATCH UPDATE (scheduled TaskMan job) periodically broadcasts the HL7 ADT-A08 message, containing any changes to data, to the MPI.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A08^ADT_A08 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 3

\[ \] Patient Additional Demographics 3

Patient Visit 3

\[\] Patient Visit – additional information 3

\[{}\] Observation/Result 7

\[\] VA Specific Patient Information Segment

\[\] VA Specific Service Period Segment

\[\] VA Specific Patient Eligibility Segment

\[\] VA Specific Emergency Contact Segment (Passed but not used by MVI)

\[\] VA Specific Employment Information Segment (Passed but not used ")

\[\] VA Specific File/Field Segment (Passed but not used by MVI)

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A08^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Message Sent *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~MPI.REDACTED.VA.GOV~DNS^20150608070503-0500^^ADT~A08^PTTEST001^T^2.4^^^AL^AL^USA

EVN^^^^^12707~MVIUSER~USERNAME\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^^500

PID^1^1008691316V935296^1008691316V935296\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666933933\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|""\~\~~USDOD&&0363~TIN~VA FACILITY ID&500&L\|""\~\~~USDOD&&0363~FIN~VA FACILITY ID&500&L\|100005148\~\~~USVHA&&0363~PI~VA FACILITYID&500&L\|1008691316V935296\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20120201\|1008691316V935296\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20120919^^MVIPATIENT~FIRSTNAME~MIDDLENAME\~\~\~~L^""^19350602^M^^""^""~""~""~""~""~""~P~""~""\|\~~""~""\~\~~N^""^""^""^^""^""^^666933933^^^""^""^^^^^^20160704^^

PV1^1^O^""^^^^^^^^^^^^^^^SC VETERAN^^^^^^^^^^^^^^^^^^^^^^^^^^20141212^^^^^^22482

OBX^^CE^NAME COMPONENTS^^MVIPATIENT,FIRSTNAME MIDDLENAME~MVIPATIENT~FIRSTNAME~MIDDLENAME\~~

OBX^^CE^DATE OF DEATH DATA^^8~SPOUSE/NEXT OF KIN/OTHER PERSON~L^^^^^^R^^^20160908150311-0400^^101102~MVIUSER~USERNAME~""""\~\~\~\~~USVHA&&0363~L\~\~~PN~VA FACILITY ID&608&L

OBX^^CE^DATE OF DEATH DOCUMENTS^^DC~DEATH CERTIFICATE~L

OBX^^CE^DATE OF DEATH OPTION^^VDE~DEATH ENTRY~L

OBX^^CE^NOTIFY PROVIDER^^608~MANCHESTER~L

OBX^^CE^IIPT^^D5~ DOD ASSOCIATE FOR ID CARD OR CLEARANCE~L^^^^^^F

OBX^^CE^PERSON TYPE^^VET~VETERAN~L^^^^^^F

OBX^^CE^PERSON TYPE^^DEP~DEPENDANT~L^^^^^^F

OBX^^CE^SECURITY LEVEL^^0~NON-SENSITIVE~L^^^^^^F

OBX^^CE^SECURITY REASON^^VET~Veteran~L^^^^^^F *Only from CORP and BIRLS* ZPD^1^^^^^^^^^^^^^^^^""^^^^""^^^^^^^^^^^^^""

ZSP^1^1^^""^""^""^""^""^^""^""

ZEL^1^""^""^""^""^""^""^1^SC VETERAN^""^""^""^""^""^""^""^""^""^""^""^""^""

ZCT^1^1^""^""^""^""^""^""^""

ZEM^1^1^""^""^""^""^""^""^

ZFF^2^.01;

<span id="_Toc131832248" class="anchor"></span>Figure ‑. ADT-A08 Update Patient Information msg: Sent *<u>to</u>* MVI *<u>from</u>* VistA

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* Receiving System

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20051020060001-0500^^ACK^2001688355533^P^2.4

MSA^CA^500167099

<span id="_Toc131832249" class="anchor"></span>Figure ‑. ADT-A08 Update Patient Information msg: Commit acknowledgement sent from MVI to VistA

Application Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* Receiving System

MSH^~\|\\^RG ADT^200M~MPI-REDACTED~DNS^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^20020921133639-0500^^ACK~A08^20099963^P^2.4^^^AL^NE^USA

MSA^AA^500167099

<span id="_Toc3901153" class="anchor"></span>Figure ‑. ADT-A08 Update Patient Information msg: Application acknowledgement sent from MVI

Commit Level Acknowledgement Returned *<u>to</u>* the MVI *<u>from</u>* Receiving System

MSH^~\|\\^RG ADT^500~DEVCRN.REDACTED.VA.GOV~DNS^RG ADT^200M~MPI-REDACTED~DNS^20051020060001-0500^^ACK^2001688355533^P^2.4

MSA^CA^20099963

<span id="_Toc131832251" class="anchor"></span>Figure ‑. ADT-A08 Update Patient Information msg: Commit acknowledgement returned to MVI

## ADT/ACK: Update Person Information (Event A31)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An A31 event can be used to update person information on the MVI. It is similar to an A08 (update patient information) event, but an A08 (update patient information) event should be used to update patient information for a current episode. An A31 can also be used for back loading MVI information for the person, or for back loading person and historical information.

To maintain backward compatibility with previous releases, the PV1 segment is required.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A31^ADT_A31 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 3

\[\] Patient Additional Demographics 3

Patient Visit 555-5555 3

\[{}\] Patient Visit - Additional Information 3

\[{}\] Observation/Result 7

\[\] VA Specific Patient Information Segment

\[\] VA Specific Service Period Segment

\[\] VA Specific Patient Eligibility Segment

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A31^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[\] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example 1: Message Sent *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20021015081501-0500^^ADT~A31^500168669^P^2.4^^^AL^AL^

EVN^^^^^12564~MVIUSER~ONE\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^^500

PID^1^1000000438V882204^1000000438V882204\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666000511\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|000999888\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|""\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\~~20070119\|000888999\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\~~20070119\|500001172V334232\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20041119\|500001171V156387\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20041119\|1001169748V365863\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20020919\|500000677V794406\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20030428\|500001144V475995\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20041029\|1008520379V265382\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\~~20050202^^MVIPATIENT~BEN THUR~TWO\~\~\~~L\|CHES\~\~\~\~\~~A\|MVIPATIENT~BENSIX\~\~\~\~~A\|MVIPATIENT~BENSEVEN\~\~\~\~~A\|PATIENTONE~BENEIGHT\~\~\~\~~A\|MVIPATIENT~PTNAME\~\~\~\~~A\|MVIPATIENT~BENEE\~\~\~\~~A\|MVIPATIENT~BENELEVEN\~\~\~\~~A\|^PATNAME\~\~\~\~\~~M^18701231^M^^2106-3-SLF\~~0005~2106-3\~~CDC^TESTING\E\\E\\TREAT\E\\E\\AVERILL PARK~NY~12018~""~P~TREATT\E\\E\\083\|\~~JACKSONVILLE~NC\~\~~N\|STREET1\E\\E\\STREET2\E\\E\\JACKSONVILLE~NC~28546~""~VACAE~STREET 3\E\\E\\E\\133\~\~~20060123&\|STREET1\E\\E\\STREET2\E\\E\\JACKSONVILLE~NC~28546~""~VACAA~STREET3\E\\E\\E\\133\~\~~20060123&\|STREET1\E\\E\\STREET2\E\\E\\JACKSONVILLE~NC~28546~""~VACAC~STREET3\E\\E\\E\\133\~\~~20060123&\|STREET1\E\\E\\STREET2\E\\E\\JACKSONVILLE~NC~28546~""~VACAM~STREET3\E\\E\\E\\133\~\~~20060123&\|STREET1\E\\E\\STREET2\E\\E\\JACKSONVILLE~NC~28546~""~VACAO~STREET3\E\\E\\E\\133\~\~~20060123&^083^(518)555-5555~PRN~PH\|(910)888-8888~WPN~PH\|(910)333-3333~ORN~CP\|~NET~INTERNET~BCDEFR@EC.RR.COM^(910)888-8888^^S^""^^000999888^^^2186-5-SLF\~~0189~2186-5\~~CDC^JACKSONVILLE NC^N^^^^^""^^

PD1^^^VAMCSITE~D~500

PV1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^20060919093712-0500

PV2^^^^^^^^^200702020800-0500^^^^^^20060919093712-0500^^^^^^^^^CR^^^^^^^^^^^^^^^^^^^^^^200609221451-0500

OBX^^^LAST RADIOLOGY EXAM DATE/TIME^^^^^^^^F^^^20060920095712-0500

OBX^^^LAST LAB TEST DATE/TIME^^^^^^^^F^^^20061021092712-0500

OBX^^^ACTIVE PRESCRIPTIONS^^Y

OBX^^CE^DATE OF DEATH DATA^^""^^^^^^R^^^""^^""

OBX^^CE^SECURITY LEVEL^^0~NON-SENSITIVE~L^^^^^^F

ZPD^1^^^^^^^^^^^^^^^^Y^^^^GREEN^^^^^^^^^^^^^""

ZSP^1^0^""^""^""^""^""^""

ZEL^1^""^""^""^""^""^""^1^SC VETERAN^""^""^""^""^""^""^""^""^1^1^""^""^""

ZEL^2^6^012-26-7845\~~^7845^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""

ZEL^3^9^012-26-7845\~~^7845^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""^""

<span id="_Toc131832252" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent from VistA to MVI

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* VistA

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20051028060001-0500^^ACK^2001699955997^P^2.4

MSA^CA^5000168669

<span id="_Toc131832253" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Commit acknowledgement sent from MVI to VistA

Application Level Acknowledgement Sent From the MVI *<u>to</u>* VistA

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20021015081512-0500^^ACK~A31^200103314^P^2.4^^^AL^NE^

MSA^AA^500168669^^^^DFN=7169807

<span id="_Toc131832254" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Application acknowledgement sent from MVI

Commit Level Acknowledgement Returned *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20051028060001-0500^^ACK^5005997^P^2.4

MSA^CA^200103314

<span id="_Toc131832255" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Commit acknowledgement returned to MVI

Example 2: Message Sent *<u>from</u>* the MVI *<u>to</u>* VistA

MSH^~\|\\^MPIF TRIGGER^200M~MPI.REDACTED.VA.GOV~DNS^

MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20070119131025-0500^^ADT~A31^20

0958862^T^2.4^^^AL^AL^

EVN^A31^20070119131025-0500^^^^^200M

PID^1^^1000000438V882204\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L~20041202~\|666000511\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|000999888\~\~~USSSA&&0363~SS~VA FACILITY ID&200M&L\|000456789\~\~~USSSA&&0363~SS~VA FACILITY ID&200M&L\~~20070119^^MVIPATIENT~FIRSTNAME~MIDDLENAME\~\~\~~L\|TESTING~PTNAME\~\~\~\~~A^PATNAME\~\~\~\~\~~M^18701231^M^2106-3\~~0005~2106-3\~~CDC^^\~~JACKSONVILLE~NC\~\~~N^^(518)555-5555~PRN~PH^^^S^^^^^^2186-5\~~2186~2186-5\~~CDC^^N^^^^^^^^^

PD1^^^VAMCSITE~D~500

PV1^^N

OBX^1^CE^SSN VERIFICATION STATUS^^4~VERIFIED~L

OBX^2^CE^SELF ID GENDER^^M~Male~L

ZPD^1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""

<span id="_Ref424823860" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent to VistA from MVI

Commit Level Acknowledgement Sent *<u>from</u>* VistA *to* the MVI

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20060327154529-0500^^ACK^50034892^P^2.4

MSA^CA^200168669

<span id="_Toc3901160" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Commit acknowledgement sent from VistA to MVI

Application Level Acknowledgement Sent *<u>from</u>* VistA *to* the MVI

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20060327154531-0500^^ACK~A31^50034893^P^2.4^^^AL^NE^

MSA^AA^200168669

ERR^\~\~~&MVIPATIENT,FIRSTNAME MIDDLENAME&MVIPATIENT&FIRSTNAME&MIDDLENAME&&

<span id="_Toc3901161" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Application acknowledgement sent from VistA to MVI

Example 3: Message sent *<u>from</u>* the MVI for Primary View sync with PSIM

MSH^~\|\\^MPI^200M~HL7.MPI-REDACTED:5026~DNS^PSIM^

HL7.200PS~TSTCRN.REDACTED.VA.GOV:5027~DNS^

20061107082515-0500^^ADT~A31~^200M 781^P~^2.4^^^AL^AL^USA

EVN^A31^20060310110609-0500^^^^^500

PID^1^^1000000877V600753\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L~

20040915114610~\|666000107\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|

888888889\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L^

^MVIPATIENT~MARVIN\~\~\~\~~L^^19900303^M^^^^^^^^^^^^^^^^^^^^^20141125^Y^^^

PD1^^^VAMCSITE1,MI~D~553

PV1^N

OBX^1^CE^SSN VERIFICATION STATUS^^~""~L

OBX^2^CE^AUTHORITY SCORE^^""~------------760~L^^^^^F

OBX^3^CE^SELF ID GENDER^^""~""~L

OBX^4^CE^USEROPTION^^14709~TASK NUMBER~L

OBX^5^CE^DATE OF DEATH DATA^^3~DEATH CERTIFICATE ON FILE~L^^^^^^R^^^20141125171157-0500^^12633~MVIPATIENT~RONNIE~""\~\~\~\~~USVHA&&0363~L\~\~~PN~VA FACILITY ID&500&L

OBX^6^CE^SSA_VERIFICATION_STATUS^^V~SSN is Verified on name, DOB and Sex code~L^^^^^^F

OBX^7^CE^IIPT^^V1~Veteran (per VA)~L^^^^^^F

OBX^9^CE^IPP LEVEL^^4~VERY HIGH CONFIDENCE~L

ZPD^1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""

<span id="_Ref424820177" class="anchor"></span>Figure ‑. ADT~A31 HL7 Message sent *<u>from</u>* the MVI for Primary View sync with PSIM

Commit ACK

MSH\|^~\\\|PSIM\|553^HL7.TSTCRN.REDACTED.VA.GOV:5027^DNS\|MPI\|

200M^HL7.MPI-REDACTED:5026^DNS\|

20061107082519-0400\|\|ACK \|553 356\|P^\|2.4\|\|\|AL\|NE\|

MSA\|CA\|200M 781\|\|

<span id="_Toc3901163" class="anchor"></span>Figure ‑. Message Sent *<u>from</u>* the MVI *<u>to</u>* PSIM: Commit ACK

Application Level ACK

MSH\|^~\\\|MPI\|553^HL7.TSTCRN.REDACTED.VA.GOV:5027^DNS\|MPI\|

200M^HL7.MPI-REDACTED:5026^DNS\|

20061107082519-0400\|\|ACK^A31^ACK\|553 356\|P^\|2.4\|\|\|AL\|NE\|

MSA\|AA\|200M 781

<span id="_Toc3901164" class="anchor"></span>Figure ‑. Message Sent *<u>from</u>* the MVI *<u>to</u>* PSIM: Application Level ACK

Example of PSIM Sending Application Level Acknowledgment with Error Condition Reported

MSH^~\|\\^PSIM^200PS~HL7.200PS.REDACTED:8090~DNS^MPI^200M~MPI-REDACTED:15026~DNS^20070807083138.839-0600^^ACK^1186493498839130265-9715^P^2.4^^^AL^NE^USA

MSA^AE^200M 1259620

ERR^\~\~~&Cannot locate VPID 0000001011191168V130766000000

<span id="_Toc3901165" class="anchor"></span>Figure ‑. Message Sent *<u>from</u>* PSIM with Error Condition Reported: Application Level ACK

## ADT/ACK: Update CMOR (Event A31)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ALERT:</strong> <strong>This message is no longer being utilized for updating the CMOR as the<br />
CMOR concept has been replaced.</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** The second occurrence of this message is included specifically to document the VHA MPI/PD implementation of the CMOR functionality and is not to be used by external MPI/PD applications.

An A31 event can be used to update person information on an MVI. It is similar to an A08 (update patient information) event, but an A08 (update patient information) event should be used to update patient information for a current episode. For this particular instance of A31, it is being used to request a change of CMOR, approve/disapprove a change of CMOR and actually change the CMOR.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

Example: Message Sent Requesting Change of CMOR

ADT^A31^ADT_A31 ADT Message Chapter

Message Header 2

Patient Identification 2

[[NTE](#nte-notes-and-comments-segment)](#nte-notes-and-comments-segment) Notes and Comments segment 2

Event Type 3

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Message Sent *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^RG CIRN^500^RG CIRN^500^20021015131109-0500^^ADT~A31^500168699^P^2.3^^

^AL^NE^USA

PID^1^1001169749V410755^100000017~2~M10^3124^MPIPATIENT~SEVEN~J~JR^""^19240601^M^^^""~""~""~""~""\~\~~""~""^^""^""^^""^29^^666623124^^^^^^^^^

NTE^^P^555-555-5555^CAPTURES OF MESSAGES^^500-39^500

EVN^A31^3021015^^^MVIUSER,ONE M

<span id="_Toc131832256" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent to the MVI requesting CMOR change

> **NOTE:** There is not an application level acknowledgement sent for this message.

Commit Level Acknowledgement Message Sent *<u>to</u>* the MVI *<u>from</u>* VistA

MSH^~\|\\^RG CIRN^500^RG CIRN^500^20051114114456-0500^^ACK^200917720^P^2.3

MSA^CA^500168699

<span id="_Toc131832257" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Commit acknowledgement

Example: Message Received at CMOR for Approving/Disapproving CMOR Change Request

ADT^A31^ADT_A31 ADT Message Chapter

Message Header 2

Event Type 3

Notes and Comments segment 2

Patient Identification 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

MSH^~\|\\^MPIF CMOR CHNG^999^MPIF CMOR CHNG^999^20021015133724^^

ADT~A31^99978507^P^2.3^^^AL^NE^

EVN^A31^3021015^^^MVIUSER,ONE M

NTE^^P^910-353-7455^OKAY^4^500-39

PID^1^1001169749V410755^57295~8~M10^3124^MPIPATIENT~SEVEN~J~JR^""^19240601^M^^^""~""~""~""~""\~\~~""~""^^""^""^^""^29^^666623124^^^^^^^^^^

<span id="_Toc131832258" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Received regarding CMOR change

> **NOTE:** There is not an application level acknowledgement sent for this message.

Commit Level Acknowledgement Sent *<u>to</u>* the MVI *<u>from</u>* the CMOR

MSH^~\|\\^MPIF CMOR RSLT^999^MPIF CMOR RSLT^999^20051114114511-0500^^ACK^

200917724^T^2.3

MSA^CA^99978507

<span id="_Toc131832259" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Commit acknowledgement sent from CMOR

Example: Message Sent Changing CMOR

ADT^A31^ADT_A31 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 2

Patient Visit 3

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

MSH^~\|\\^MPIF CMOR RSLT^999^MPIF CMOR RSLT^999^20021015133722^^ADT~A31^

99978505^P^2.3^^^AL^NE^USA

EVN^A31^3021015^^^Automatic Processing

PID^1^1001169749V410755^57295~8~M10^^MVIPATIENT~SEVEN~J~JR^""^19240601^M^^^""~""~""~""~""\~\~~""~""^^""^""^^""^29^^666623124^^^^^^^^^^

PV1^^^500^^^999

<span id="_Toc131832260" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent to MVI changing CMOR

> **NOTE:** There is not an application level acknowledgement sent for this message.

Commit Level Acknowledgement Sent *<u>from</u>* the MVI *<u>to</u>* Requesting VistA System

MSH^~\|\\^MPIF CMOR RSLT^^MPIF CMOR RSLT^553^2005111411451

7-0500^^ACK^50027450^P^2.3

MSA^CA^200917727

<span id="_Toc131832261" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Commit acknowledgement sent to requesting VistA site

## ADT/ACK: Enterprise Update Person Information (Event A31)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The third occurrence of this message is included specifically to document the ADT-A31 message being triggered from the MPI Austin side.

An A31 event can be used to update person information on VistA. It is similar to an A08 (update patient information) event, but an A08 (update patient information) event should be used to update patient information for a current episode. For this particular instance of A31, it is being used to synchronize the treating facilities with the CMOR's data as it exists on the MVI or the Primary View data once the patient has been primary view initialized on the MVI.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A31^ADT_A31 ADT Message Chapter

Message Header 2

Event Type 3

Patient Identification 3

\[\] Patient Additional Demographics 3

Patient Visit 3

\[\] VA Specific Patient Information Segment

ACK^COMMIT Commit Level Acknowledgement Chapter

> Message Header 2

> Message Acknowledgement 2

ACK^A31^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[\] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example 1: Message Sent *<u>from</u>* the MVI *<u>to</u>* VistA

MSH^~\|\\^MPIF TRIGGER^200M~MPI.REDACTED.VA.GOV~DNS^

MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20070119131025-0500^^ADT~A31^20

0958862^T^2.4^^^AL^AL^

EVN^A31^20070119131025-0500^^^^^200M

PID^1^^1000000438V882204\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L~20041202~\|666000511\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|000999888\~\~~USSSA&&0363~SS~VA FACILITY ID&200M&L\|000456789\~\~~USSSA&&0363~SS~VA FACILITY ID&200M&L\~~20070119^^MPIPATIENT~PTLASTNAME~MIDDLENAME\~\~\~~L\|TESTING~PTNAME\~\~\~\~~A^PATNAME\~\~\~\~\~~M^18701231^M^2106-3\~~0005~2106-3\~~CDC^^\~~JACKSONVILLE~NC\~\~~N^^(518)555-5555~PRN~PH^^^S^^^^^^2186-5\~~2186~2186-5\~~CDC^^N^^^^^20160704^^^^

PD1^^^VAMCSITE~D~500

PV1^^N

OBX^1^CE^SSN VERIFICATION STATUS^^4~VERIFIED~L

OBX^2^CE^SELF ID GENDER^^M~Male~L

OBX^3^CE^DATE OF DEATH DATA^^8~SPOUSE/NEXT OF KIN/OTHER PERSON~L^^^^^^R^^^20160908150408-0400^^101102~MVIUSER~USERNAME~""""\~\~\~\~~USVHA&&0363~L\~\~~PN~VA FACILITY ID&608&L

ZPD^1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""

<span id="_Ref424824066" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent to VistA from MVI

Commit Level Acknowledgement Sent *<u>from</u>* VistA *<u>to</u>* the MVI

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20060327154529-0500^^ACK^50034892^P^2.4

MSA^CA^200168669

<span id="_Toc3901173" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Commit acknowledgement sent from VistA to MVI

Application Level Acknowledgement Sent *<u>from</u>* VistA *<u>to</u>* the MVI

MSH^~\|\\^MPIF TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20060327154531-0500^^ACK~A31^50034893^P^2.4^^^AL^NE^

MSA^AA^200168669

ERR^\~\~~&MPIPATIENT,PTLASTNAME MIDDLENAME&MPIPATIENT&PTLASTNAME&MIDDLENAME&&

<span id="_Toc3901174" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Application acknowledgement sent from VistA to MVI

Example 2: Message Sent *<u>from</u>* the MVI *<u>to</u>* PSIM

MSH^~\|\\^MPI APP^200M~HL7.MPI.REDACTED.VA.GOV:5026~DNS^PSIM^200PS~vaauspsimweblogic3.vha.med.va.gov:8090~DNS^20150608100857-0400^^ADT~A31~^200M 1179830^T~^2.4^^^AL^AL^USA

EVN^A31^20150608100856-0400^^^12707~MVIUSER~USERNAME\~\~\~\~\~~USVHA&&0363~L\~\~~PN~VA FACILITY ID&500&L^^500

PID^1^^1008691316V935296\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L~20140604~\|100005148\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|666933933\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|""\~\~~USDOD&&0363~TIN~VA FACILITY ID&200DOD&L\|""\~\~~USDOD&&0363~FIN~VA FACILITY ID&200DOD&L\|""\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\~~20150608^^MVIUSER~NEW~NAME~""~""\~~L\|""~""~""~""~""\~~A^""\~\~\~\~\~~M^19350602^M^^""^\~~""~""\~~""~N\|""~""~""~""~""~""~P~""^^""^^^""^^^^^^""^^""^""^^^^20160704^^^A^

PD1^^^VAMCSITE~D~500

PV1^^N

OBX^1^CE^SSN VERIFICATION STATUS^^""~""~L

OBX^2^CE^ROI SIGNED^^""~""~L

OBX^3^CE^IPP LEVEL^^""~""~L

OBX^4^CE^PATIENT TYPE^^8~SC VETERAN~L

OBX^5^CE^VETERAN Y/N^^Y~Yes~L

OBX^6^CE^PERIOD OF SERVICE^^""~""~L

OBX^7^CE^SELF ID GENDER^^""~""~L

OBX^8^CE^DATE OF DEATH DATA^^8~SPOUSE/NEXT OF KIN/OTHER PERSON~L^^^^^^R^^^20160908150408-0400^^101102~MPIPATIENT~DAN~""""\~\~\~\~~USVHA&&0363~L\~\~~PN~VA FACILITY ID&608&L

OBX^9^CE^NOTIFY PROVIDER^^608~MANCHESTER VAMC~L

OBX^10^CE^DATE OF DEATH DOCUMENTS^^DC~DEATH CERTIFICATE~L

OBX^11^CE^DATE OF DEATH OPTION^^VDE~DEATH ENTRY~L

OBX^12^CE^DATE OF DEATH DISCHARGE DT^^^^^^^^^""""

OBX^13^CE^DATE OF DEATH OVR REASON^^""""

OBX^14^TS^NEW DATE OF DEATH STATUS^^20170107^^^^^^P^

OBX^15^CE^SSA VERIFICATION STATUS^^""~""~L^^^^^^R

OBX^16^CE^IIPT^^D5~DOD ASSOCIATE FOR ID CARD OR CLEARANCE~L^^^^^^F

OBX^17^CE^PERSON TYPE^^VET~VETERAN~L^^^^^^F

OBX^18^CE^PERSON TYPE^^DEP~DEPENDENT~L^^^^^^F

OBX^19^CE^SECURITY LEVEL^^V_0~Not Sensitive~L^^^^^^F

OBX^20^CE^SECURITY REASON^^NVE~Non-VBA VA Employee~L^^^^^^F

ZPD^1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""

<span id="_Ref424820321" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent *<u>from</u>* the MVI *<u>to</u>* PSIM

Commit ACK

MSH\|^~\\\|PSIM\|553^HL7.TSTCRN.REDACTED.VA.GOV:5027^DNS\|MPI\|

200M^HL7.MPI-REDACTED:5026^DNS\|

20061107082519-0400\|\|ACK \|553 356\|P^\|2.4\|\|\|AL\|NE\|

MSA\|CA\|200M 781\|\|

<span id="_Toc3901176" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent *<u>from</u>* the MVI *<u>to</u>* PSIM: Commit ACK

Application Level ACK

MSH\|^~\\\|MPI\|553^HL7.TSTCRN.REDACTED.VA.GOV:5027^DNS\|MPI\|

200M^HL7.MPI-REDACTED:5026^DNS\|

20061107082519-0400\|\|ACK^A31^ACK\|553 356\|P^\|2.4\|\|\|AL\|NE\|

MSA\|AA\|200M 781

<span id="_Toc3901177" class="anchor"></span>Figure ‑. ADT-A31 Update Person Information msg: Sent *<u>from</u>* the MVI *<u>to</u>* PSIM: Application Level ACK

> **NOTE:** This ADT-A31 message is sent from the MPI to VistA. Fewer fields are populated in the ADT-A31 message when it originates on the MPI and is sent to VistA. This is because the MPI doesn't store all the fields that VistA does.

## MFN: Update Treating Facility (Event M05)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The treating facility list is a list of systems that know a specific Integration Control Number (ICN). The list can contain systems that are not VAMC like FHIE or HDR. The list is built and updated as a result of systems identifying the system knows a particular ICN either via the MVI approved query and subsequent ADT-A28 Add patient or ADT-A24 Link HL7 message.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

MFN^M05 Master File update Chapter

Message Header 2.24.1

[MFI](#mfi-master-file-identification-segment) Master File Identification Segment 8.4.1

{[MFE](#mfe-master-file-entry-segment) Master File Entry Segment 8.4.2

} ZET is the event reason for date of last treatment N/A

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

MFK^M05 Master File update Acknowledgement Chapter

Message Header 2.24.1

Master File Identification Segment 8.4.1

{ Master File Entry Segment 8.4.2

[MFA](#mfa-master-file-acknowledgement-segment)} Master File Acknowledgement Segment 8.4.3

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

> **NOTE:** My HealtheVet Applications must continue using the original format of the MFN^M05 HL7 Message. An example of the original HL7 message is shown a few pages following titled ""

Example: Message Received *<u>from</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^200M~MPI.REDACTED.VA.GOV~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20140129145237-0500^^MFN~M05^2005021396^T^2.4^^^AL^AL^USA

MFI^TFL^^REP^^^NE^500~VAMCSITE

MFE^MAD^500-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100003470\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX^

ZET^^

MFE^MDC^500-2^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100003472\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX^

ZET^^

MFE^MAD^553-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100002205\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^CX^

ZET^^

MFE^MAD^200PS-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|\~\~~USVHA&&0363~PI~VA FACILITY ID&200PS&L^CX^

ZET^^

MFE^MAD^200NKP-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|KP99000456789\~\~~&1.3.6.1.4.1.26580&ISO\~~&1.3.6.1.4.1.26580&ISO^

ZET^^

MFE^MDC^200LR3-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|LR84848\~\~~USVHA&&0363~PI~VA FACILITY ID&200LR3&L^CX^

ZET^

<span id="_Toc131832266" class="anchor"></span>Figure ‑. MFN-M05 Update Treating Facility msg: Received from MVI

Commit Level Acknowledgement Sent *<u>to</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI-REDACTED~DNS^20051111094136-0400^^ACK^673105227963^P^2.4

MSA^CA^20096036

<span id="_Toc131832267" class="anchor"></span>Figure ‑. MFN-M05 Update Treating Facility msg: Commit acknowledgement sent to MVI

Application Level Acknowledgement Sent *<u>to</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI.REDACTED.VA.GOV~DNS^20140129145244-0500^^MFK~M05^500661841^T^2.4^^^AL^NE^USA

MSA^AA^2005021396^

MFI^TFL^^REP^^^NE^500~VAMCSITE

MFE^MAD^500-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100003470\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX^

MFA^MAD^500-1^20140129145244-0500^S

MFE^MDC^500-2^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100003472\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX^

MFA^MDC^500-2^20140129145244-0500^S

MFE^MAD^553-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100002205\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^CX^

MFA^MAD^553-1^20140129145244-0500^S

MFE^MDC^200LR3-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|LR84848\~\~~USVHA&&0363~PI~VA FACILITY ID&200LR3&L^CX^

MFA^MDC^200LR3-1^20140129145244-0500^U~Update of 200LR3 Failed at 500 due to unknown Institution IEN 0 passed into TF update.^

MFE^MAD^200NKP-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|KP99000456789\~\~~&1.3.6.1.4.1.26580&ISO\~~&1.3.6.1.4.1.26580&ISO^

MFA^MAD^200NKP-1^20140129145244-0500^S

MFE^MAD^200PS-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|\~\~~USVHA&&0363~PI~VA FACILITY ID&200PS&L^CX^

MFA^MAD^200PS-1^20140129145244-0500^S

<span id="_Toc131832268" class="anchor"></span>Figure ‑. MFN-M05 Update Treating Facility msg: Application acknowledgement sent to MVI

Commit Level Acknowledgement Returned *<u>from</u>* MVI to Sending System

MSH^~\|\\^VAFC TRIGGER^200M~MPI-REDACTED~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20051111084137-0500^^ACK^2001705747823^P^2.4

MSA^CA^5008304

<span id="_Toc131832269" class="anchor"></span>Figure ‑. MFN-M05 Update Treating Facility msg: Commit acknowledgement sent from MVI

Assigning Authority and Id Type are parsed from MFE Segment for HL7 MFN~M05 v2.4 and v3

As of Patch DG\*5.3\*837 changes were made to the HL7 MFN~M05 Treating Facility List Update message to parse MFE segments that can be more than 245 characters long. Assigning Authority and Id Type are parsed from the MFE segment of the message for both HL7 v2.4 and v3.0. Also, the existing deletion logic for removing Treating Facility entries in the TREATING FACILITY LIST file (#391.91) while processing the MFN~M05 message was modified. The following are examples of the updates.

MSH^~\|\\^VAFC TRIGGER^200M~MPI.REDACTED.VA.GOV~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20120105095556-0500^^MFN~M05^200NKPTFUPD^T^2.4^^^AL^AL^USA

MFI^TFL^^REP^^^NE^500~VAMCSITE

MFE^MAD^500-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100003470\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX

ZET^^

MFE^MAD^200PS-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|\~\~~USVHA&&0363~PI~VA FACILITY ID&200PS&L^CX

ZET^^

MFE^MAD^200NKP-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|KP99000456789\~\~~&1.3.6.1.4.1.26580&ISO\~~&1.3.6.1.4.1.26580&ISO^CX

ZET^

<span id="_Ref320486480" class="anchor"></span>Figure ‑. MFN-M05 Update Treating Facility msg: Assigning Authority and Id Type are parsed from MFE segment for HL7 MFN~M05 v2.4 and v3

MSH^~\|\\^VAFC TRIGGER^200M~MPI.REDACTED.VA.GOV~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20120107095656-0500^^MFN~M05^200NMVTFUPD1^T^2.4^^^AL^AL^USA

MFI^TFL^^REP^^^NE^500~VAMCSITE

MFE^MAD^500-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100003470\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX

ZET^^

MFE^MAD^200PS-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|\~\~~USVHA&&0363~PI~VA FACILITY ID&200PS&L^CX

ZET^^

MFE^MAD^553-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100002205\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^CX

ZET^^

MFE^MAD^200NKP-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|KP99000456789\~\~~&1.3.6.1.4.1.26580&ISO\~~&1.3.6.1.4.1.26580&ISO^CX

ZET^^

MFE^MDC^500-2^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|100003472\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX

ZET^^

MFE^MAD^200NMV-1^^1000001932V600083\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|KP990004567893049580394850938409580398409580398405983498569874958798745986798475968798798347992837492387492837492837948237598798798273948729038798273\~\~~&2.16.840.1.113883.3.190.6.100.1&ISO\~~&2.16.840.1.113883.3.190.6.100.1&ISO^CX

ZET^^

<span id="_Ref320486485" class="anchor"></span>Figure ‑. MFN-M05 Update Treating Facility msg: Assigning Authority and Id Type are parsed from MFE segment, more than 245 characters long, for HL7 MFN~M05 v2.4 and v3

MFN^M05 HL7 Message Examples for My HealtheVet ApplicationsExample: Message Received *<u>from</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^200M~MPI-REDACTED~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20020916085620-0500^^MFN~M05^20096036^P^2.4^^^AL^AL^US

MFI^TFL^^UPD^^^AL^500~VAMCSITE

MFE^MUP^500^20020913112211-0500^500~VAMCSITE~VA~1001170419V238836~ICN~VA

ZET^A1

MFE^MUP^553^^553~VAMCSITE1~VA~1001170419V238836~ICN~VA

ZET^

MFE^MUP^998^^998~VAMCSITE2~VA~1001170419V238836~ICN~VA

ZET^

<span id="_Toc3901184" class="anchor"></span>Figure ‑. MFN-M05 for My Healthevet Applications Update Treating Facility msg: Received from MVI

Commit Level Acknowledgement Sent *<u>to</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI-REDACTED~DNS^20051111094136-0400^^ACK^673105227963^P^2.4

MSA^CA^20096036

<span id="_Toc3901185" class="anchor"></span>Figure ‑. MFN-M05 for My Healthevet Applications Update Treating Facility msg: Commit acknowledgement sent to MVI

Application Level Acknowledgement Sent *<u>to</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI-REDACTED~DNS^20051111094130-0500^^MFK~M05^5008304^P^2.4^^^AL^NE^US

MSA^AA^500164930^0

MFI^TFL^^UPD^^^AL^500~VAMCSITE

MFE^MUP^500^20020913112211-0500^500~VAMCSITE~VA~1001170419V238836~ICN~VA

MFA^MUP^500^20041108122753-0500^S

MFE^MUP^553^^553~VAMCSITE1,MI~VA~1001170419V238836~ICN~VA

MFA^MUP^553^20041108122753-0500^S

MFE^MUP^998^^998~VAMCSITE2~VA~1001170419V238836~ICN~VA

MFA^MUP^998^20041108122753-0500^S

<span id="_Toc3901186" class="anchor"></span>Figure ‑. MFN-M05 for My Healthevet Applications Update Treating Facility msg: Application acknowledgement sent to MVI

Commit Level Acknowledgement Returned *<u>from</u>* MVI to Sending System

MSH^~\|\\^VAFC TRIGGER^200M~MPI-REDACTED~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20051111084137-0500^^ACK^2001705747823^P^2.4

MSA^CA^5008304

<span id="_Toc3901187" class="anchor"></span>Figure ‑. MFN-M05 for My Healthevet Applications Update Treating Facility msg: Commit acknowledgement sent from MVI

## QRY/ADR: Patient Query (Event A19)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following trigger event is served by QRY (a query from another system) and ADR (a response from a Patient Administration system).

Another application determines a need for Patient Administration data about a patient and sends a query to the Patient Administration system. The Who Filter in the QRD can identify the patient or account number upon which the query is defined and can contain a format code of "R" (record-oriented). If the query is based on the Patient ID and there are data associated with multiple accounts, the problem of which account data should be returned becomes an implementation issue. The ADT event-type segment, if included in the response, describes the last event for which the Patient Administration system initiated an unsolicited update.

> **NOTE:** At this time, the QRY-A19 message is only triggered from the MPI to any of the sites in the Treating Facility list and any associated systems related to those treating facilities.

> **NOTE:** The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

QRY^A19^QRY_A19 Patient Query Chapter

Message Header 2

[QRD](#qrd-original-style-query-definition-segment) Query Definition 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ADR^A19^ADR_A19 ADT Response Chapter

Message Header 2

Message Acknowledgement 2

\[\] Error 2

\[ \] Query Acknowledgement (Not built by the MVI) 5

Query Definition 2

Event Type 3

Patient Identification 3

\[ \] Patient Additional Demographics 3

Patient Visit 3

\[{[OBX](#obx-observationresult-hl7-segment)}\] Observation/Result 7

\[ \] VA Specific Patient Information Segment

\[[ZSP](#zsp-va-specific-service-period-segment)\] VA Specific Service Period Segment

\[[ZEL](#zel-va-specific-patient-eligibility-segment)\] VA Specific Patient Eligibility Segment

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example 1: When the Patient is Known at the Facility by the ICN Known at the MVIQuery Message Sent *<u>from</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^200M~MPI-REDACTED~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20021002160803-0500^^QRY~A19^200101031^P^2.4^^^AL^AL^US

QRD^20021002160803-500^R^I^0000170555^^^1~RD^1000170555V098765\~\~\~\~\~\~\~~USVHA&&0363~NI\~\~\~\~~VA FACILITY ID&500&L\|666645123\~\~\~\~\~\~\~~USSSA&&0363~SS\~\~\~\~~VA FACILITY ID&500&L^DEM^^^

<span id="_Toc131832270" class="anchor"></span>Figure ‑. QRY-A19 Patient Query msg: Sent from MVI

Commit Level Acknowledgement Sent *<u>to</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI-REDACTED~DNS^20051104073709-0400^^ACK^50085379^P^2.4

MSA^CA^200101031

<span id="_Toc131832271" class="anchor"></span>Figure ‑. QRY-A19 Patient Query msg: Commit acknowledgement sent to MVI

Query Results Received When Patient is Known at Queried Facility

MSH^~\|\\^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI-REDACTED~DNS^20021002160814-0500^^ADR~A19^500167426^P^2.4^^^AL^NE^US

MSA^AA^200101031^

QRD^20021002160803-500^R^I^1000170555V098765^^^RD~1^1000170555V098765\~\~\~\~\~\~\~~USVHA&&0363~NI\~\~\~\~~VA FACILITY ID&500&L\|666645123\~\~\~\~\~\~\~~USSSA&&0363~SS\~\~\~\~~VA FACILITY ID&500&L^DEM^^^

EVN^A1^20020913112211-0500^^A1^.5~POSTMASTER\~\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L^20020913112211-0500^500

PID^1^^1000170555V098765\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L^^MVIPATIENT~PTNAME3~FIRSTNAME\~\~\~~L^MVIMAIDEN\~\~\~\~\~~M^19450403^M^^^123 TEST~LINE2~PELHAM~AL~34124\~~P~LINE3\|

\~~BIRMINGHAM~AL\~\~~N^117^""^""^^S^9^^^^^^^^^^^^""^^

PV1^N

OBX^^CE^SELF ID GENDER^^O~Other

OBX^^CE^NAME COMPONENTS^^MPIPATIENT,FIRSTNAME D~MPIPATIENT~FIRSTNAME~D\~~

ZPD^1^^^^^^^^^^^^^^^^""^^^^""^^^^^^^^^^^^^""

ZSP^1^0^""^8^""^""^""^""^^""^""

ZEL^1^^^^^^^1^SC VETERAN

<span id="_Toc131832272" class="anchor"></span>Figure ‑. QRY-A19 Patient Query msg: Query results received when patient is known at queried facility

Commit Level Acknowledgement Sent *<u>from</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^200M~MPI-REDACTED~DNS^VAFC TRIGGER^500~DEVCRN.REDACTED.VA.GOV~DNS^20051104073723-0500^^ACK^200917444^P^2.4

MSA^CA^500167426

<span id="_Toc131832273" class="anchor"></span>Figure ‑. QRY-A19 Patient Query msg: Commit acknowledgement sent from MVI

Example 2: When the Patient is Not Known at the Facility by ICN Known at MVIQuery Message Sent *<u>from</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^200M~MPI-REDACTED~DNS^VAFC TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^20051104073703-0500^^QRY~A19^200917406^P^2.4^^^AL^AL^US

QRD^20051104073703-0500^R^I^1000170555V098765^^^1~RD^1000170555V098765\~\~\~\~\~\~\~~USVHA&&0363

~NI\~\~\~\~~VA FACILITY ID&200M&L\|7169826\~\~\~\~\~\~\~~USVHA&&0363~PI\~\~\~\~~VA FACILITY ID&553&L^DEM^^^

<span id="_Toc131832274" class="anchor"></span>Figure ‑. QRY-A19─Query Message sent from MVI

Commit Level Acknowledgement Sent *<u>to</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI-REDACTED~DNS^20051104073709-0400^^ACK^55385379^P^2.4

MSA^CA^200917406

<span id="_Toc131832275" class="anchor"></span>Figure ‑. QRY-A19─Query Message sent from MVI: Commit acknowledgement sent to MVI

Query Results Received When Patient is NOT Known at Queried Facility

MSH^~\|\\^VAFC TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^VAFC TRIGGER^200M~MPI-REDACTED~DNS^20051104073710-0400^^ADR~A19^55385380^P^2.4^^^AL^NE^US

MSA^AA^200917406^Unknown ICN#1000170555V098765 and SSN#

QRD^20051104073703-500^R^I^1008520116^^^1~RD^1000170555V098765\~\~\~\~\~\~\~~USVHA&&0363~NI\~\~\~\~~VA FACILITY ID&200M&L^DEM^^^

<span id="_Toc131832276" class="anchor"></span>Figure ‑. QRY-A19─Query results received when patient is NOT known at queried facility

Commit Level Acknowledgement Returned *<u>from</u>* the MVI

MSH^~\|\\^VAFC TRIGGER^200M~MPI-REDACTED~DNS^VAFC TRIGGER^553~TSTCRN.REDACTED.VA.GOV~DNS^20051104073723-0500^^ACK^200917413^P^2.4

MSA^CA^55385380

<span id="_Toc131832277" class="anchor"></span>Figure ‑. QRY-A19─Query results received when patient is NOT known at queried facility: Commit acknowledgement returned from MVI

## VQQ: Query for Patient Matches (Event Q02)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this message is to query the Master Veteran Index (MVI) to see if the patient in question exists or potentially exists. The query is utilized in three different ways:

> 1\. Via the real-time connection with the MVI where the query is just seeing what the MVI has for display only purposes.

> 2\. Via the real-time connection with the MVI where the query is being used to see if the patient in question is known.

> 3\. Via the background process as part of a batch message to see if the patient is known on the MVI and if the patient is not known (no matches, not even potential matches), is added to the MVI.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

VQQ^Q02 Message Chapter

Message Header 2

Virtual Table Query 2

Table Row Definition 2

ACK^Q02 Message Chapter

Message Header 2

Message Acknowledgement 2

Query Acknowledgement 2

Table Row Definition 2

{} Table Row Data 2

Example: Real-Time Connection Query Sent *<u>to</u>* the MVI

MSH\|^~\\\|MPI_LOAD\|500\|MPI-ICN\|\|\|\|VQQ^Q02\|100000082-1\|

VTQ\|100000082\|T\|VTQ_PID_ICN_NO_LOAD\|ICN\|@00108.1^EQ^MVIPATIENT^AND~@00122^EQ^000064567^AND~@00108.2^EQ^TEN^AND~@00110^EQ^19780303

RDF\|24\|@00108.1^ST^20~@00122^ST^9~@00110^ST^8~@00756^ST^3~@00105^ST^19~@00108.2^ST^20~@00169^ST^99~@00740^ST^8~@00108.3^ST^16~@00111^ST^1~@00126.1^ST^30~@00126.2^ST^3~@00108.5^ST^15~@00108.4^ST^10~@00109.1^ST^20~@ZEL6^ST^9~@CASE#^ST^69~POW^ST^1~@00127^ST^1~@00112.1^ST^30~@00112.2^ST^25~@00112.3^ST^25~@00112.5^ST^10~@00112.4^ST^10

<span id="_Hlt131916069" class="anchor"></span>Figure ‑. VQQ-Q02─Real-Time Connection Query msg: Sent to MVI

Example: Real-Time Connection Query Returned *<u>from</u>* the MVI

MSH\|^~\\\|MPI\|MPI\|MPI_LOAD\|500\|\|\|ACK^Q02\|100000082-1\|P\|2.3

MSA\|AA\|100000082-1

QAK\|100000082\|OK

RDF\|24\|@00108.1^ST^20~@00122^ST^9~@00110^ST^8~@00756^ST^3~@00105^ST^19~@00108.2^ST^20~@00169^ST^99~@00740^ST^8~@00108.3^ST^16~@00111^ST^1~@00126.1^ST^30~@00126.2^ST^3~@00108.5^ST^15~@00108.4^ST^10~@00109.1^ST^20~@ZEL6^ST^9~@CASE#^ST^69

RDT\|MVIPATIENT\|000064567\|19780203\|998\|1000000560V235869\|INDY\|998~\|\|E\|M\|JASPER\|AL\|\|\|PUPPY\|

<span id="_Toc131832279" class="anchor"></span>Figure ‑. VQQ-Q02─Real-Time Connection Query msg: Returned from MVI

## VQQ-Q02: Batch Format (i.e., the Local/Missing ICN Resolution Job)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** There can be up-to 100 patients per batch message, when sent via the Local/Missing ICN Resolution Job.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

VQQ^Q02 Message Chapter

Batch Message Header 2

{ Message Header 2

Virtual Table Query 2

} Table Row Definition 2

[BTS](#bts-batch-trailer-segment) Batch Trailer Segment 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^Q02 Message Chapter

Batch Message Header 2

{ Message Header 2

Message Acknowledgement 2

Query Acknowledgement 2

Table Row Definition 2

{}} Table Row Data 2

Batch Trailer Segment 2

Example: VQQ-Q02 Used in a Batch Message (i.e., the Local/Missing ICN Resolution Job) Sent *<u>to</u>* the MVI

BHS^~\|\\^MPIF-STARTUP^500^MPIF MPI^^20020913111339-0500^^~P~VQQ\|Q02~2.3~AL~NE^

^500149126^

MSH^~\|\\^MPIF-STARTUP^500^^^^^VQQ~Q02^500152422-1^^2.3^^^AL^NE

VTQ^100000042^T^VTQ_PID_ICN_NO_LOAD^ICN^@00108.1~EQ~NEW~AND\|@00108.2~EQ~PATIENT~AND\|@00110~EQ~19400203~AND\|@00111~EQ~M~AND\|@00108.4~EQ~ATWE~AND\|@00108.3~EQ~FOR

RDF^17^@00108.1~ST~20\|@00122~ST~9\|@00110~ST~8\|@00756~ST~3\|@00105~ST~19\|@00108.2~ST~20\|@00169~ST~99\|@00740~ST~8\|@00108.3~ST~16\|@00111~ST~1\|@00126.1~ST~30\|@00126.2~ST~3\|@00108.5~ST~15\|@00108.4~ST~10\|@00109.1~ST~20\|@ZEL6~ST~9\|@CASE#~ST~69

BTS^1

<span id="_Toc131832280" class="anchor"></span>Figure ‑. VQQ-Q02─Real-Time Connection Query batch msg: Sent to MVI

Commit Level Acknowledgement sent *<u>from</u>* the MVI

BHS^~\|\\^MPIF MPI^500^MPIF-STARTUP^500^20051114120003-0500^^~P~ACK^CA^

2001708000178^51129

MSA^CA^500149126

<span id="_Toc131832281" class="anchor"></span>Figure ‑. VQQ-Q02─Real-Time Connection Query batch msg: Commit acknowledgement sent from MVI

Example: VQQ-Q02 Used in a Batch Message Returned *<u>from</u>* the MVI

BHS^~\|\\^MPIF MPI^MPI^MPIF-STARTUP^500^20020913111358-500^^~P~ACK\|Q02~2.3~NE~NE^AA~

^20049759^500149126

MSH^~\|\\^MPI^MPI^MPIF-STARTUP^500^^^ACK^500152422-1^P^2.3

MSA^AA^500152422-1

QAK^100000042^OK

RDF^17^@00108.1~ST~20\|@00122~ST~9\|@00110~ST~8\|@00756~ST~3\|@00105~ST~19\|@00108.2~ST~20\|@00169~ST~99\|@00740~ST~8\|@00108.3~ST~16\|@00111~ST~1\|@00126.1~ST~30\|@00126.2~ST~3\|@00108.5~ST~15\|@00108.4~ST~10\|@00109.1~ST~20\|@ZEL6~ST~9\|@CASE#~ST~69

RDT^NEW^^^500^1001170233V211078^PATIENT^500\|^^FOR^^^^^^^

BTS^1

<span id="_Toc131832282" class="anchor"></span>Figure ‑. VQQ-Q02─Real-Time Connection Query batch msg: Returned from MVI

## ADT/ACK: Unlink Patient Information (Event A37)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The A37 event unlinks a patient from an identifier. An A37 event can be used to unlink a systems patient from an existing entry on the MVI.

REF: The "Chapter" reference below refers to the HL7 Standard Version 2.4 documentation.

ADT^A37^ADT_A37 ADT Message Chapter

Message Header 2

Event Type 3

Patient (1) Identification 3

\[ \] Patient (1) Additional Demographics 3

\[ \] Patient (1) Visit 3

Patient (2) Identification 3

\[ \] Patient (2) Additional Demographics 3

\[ \] Patient (2) Visit 3

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

ACK^A37^ACK Application Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

\[ \] Error 2

ACK^COMMIT Commit Level Acknowledgement Chapter

Message Header 2

Message Acknowledgement 2

Example: Message Sent *<u>to</u>* the MVI

This message indicates that the MHV application is requesting that the MHV ID 123 be unlinked from the 1001170560V235869 ICN (sequence 3 in PID2) and not be linked with another ICN (null in sequence 3 of PID1).

MSH^~\|\\^MPIF TRIGGER^200MHV~MYHEAL.MED.VA.GOV^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20020921202421-0500^^ADT~A37^200100057^P^2.4^^^AL^AL^

EVN^A37^20020921202421-0500^20020921202421-0500^^USER NAME

PID^1^^""\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|123\~\~~USVHA&&0363~PI~VA FACILITY ID&200MHV&L^^MHVPATIENT~JAMIE\~\~\~\~~L^PUPPY\~\~\~\~\~~M^2780203^M^^^^^^^^^^^111111111^^^^^^^^

PID^2^^1000000560V235869\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|123\~\~~USVHA&&0363

~PI~VA FACILITY ID&200MHV&L^^MHVPATIENT~JAMIE~E\~\~\~~L^PUPPY\~\~\~\~\~~M^2780203^M^^

^^^^^^^^^111111111^^^^^^^^^^^^

<span id="_Toc131832283" class="anchor"></span>Figure ‑. ADT-A37 Unlink Patient Information msg: Sent to MVI

Commit Level Acknowledgement Sent *<u>from</u>* the MVI

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^200MHV~MYHEAL.MED.VA.GOV~DNS^20051028060001-0500^^ACK^2001672355997^P^2.4

MSA^CA^200100057

<span id="_Toc131832284" class="anchor"></span>Figure ‑. ADT-A37 Unlink Patient Information msg: Commit acknowledgement sent from MVI

Application Level Acknowledgement Sent *<u>to</u>* the MVI

MSH^~\|\\^MPIF TRIGGER^200M~MPI-REDACTED~DNS^MPIF TRIGGER^200MHV~

MYHEAL.MED.VA.GOV~DNS^20020921202425-0500^^ACK~A37^200167161^P^2.4^^^AL^NE^

MSA^AA^200100057^

<span id="_Toc86584213" class="anchor"></span>Figure ‑. ADT-A37 Unlink Patient Information msg: Application acknowledgement sent to MVI

Commit Level Acknowledgement Sent TO the MVI

MSH^~\|\\^MPIF TRIGGER^200MVH~MYHEAL.MED.VA.GOV~DNS^MPIF TRIGGER^200M~MPI-REDACTED~DNS^20051028060001-0500^^ACK^2001672355997^P^2.4

MSA^CA^200167161

<span id="_Toc131832286" class="anchor"></span>Figure ‑. ADT-A37 Unlink Patient Information msg: Commit acknowledgement sent to MVI

Page intentionally left blank for double-sided print copy.

# Message Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the HL7 message segments supported by VistA and used specifically by the MPI/PD software. All standard HL7 segments and sequence/field definitions involved with MVI processes are listed in tables in this section. However, only the VistA data passed by the MVI is mapped to the standard HL7 sequences/fields within these segment tables and subsequently translated.

The HL7 message segments documented in this chapter are listed as follows:

- BHS: Batch Header Segment
- BTS: Batch Trailer Segment
- DSC: Continuation Pointer Segment
- ERR: Error Segment
- EVN: Event Type Segment
- MFA: Master File Acknowledgement Segment
- MFE: Master File Entry Segment
- MFI: Master File Identification Segment
- MRG: Merge Patient Information Segment
- MSA: Message Acknowledgement Segment
- MSH: Message Header Segment
- NTE: Notes and Comments Segment
- OBX: Observation/Result, HL7 Segment
- PD1: Patient Additional Demographic Segment
- PID: Patient Identification Segment
- PV1: Patient Visit Segment
- PV2: Patient Visit Segment – Additional Information
- QAK: Query Acknowledgement Segment
- QPD: Query Parameter Definition
- QRD: Original-Style Query Definition Segment
- QRI: Query Response Instance Segment
- RCP: Response Control Parameter Segment
- RDF: Table Row Definition Segment
- RDT: Table Row Data Segment
- VTQ: Virtual Table Query Request Segment
- ZCT: VA Specific Emergency Contact Segment
- ZEL: VA Specific Patient Eligibility Segment
- ZEM: VA Specific Employment Information Segment
- ZET: VA Specific Event Reason for Date of Last Treatment Segment
- ZFF: VA Specific File/Field Segment
- ZPD: VA Specific Patient Information Segment
- ZSP: VA Specific Service Period Segment

## BHS: Batch Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BHS segment defines the start of a batch.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 23%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>VistA Element Name</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Field Separator</td>
<td>Recommended value is <strong>^</strong> (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = \ (back</p>
<p>slash)</p>
<p>Subcomponent = &amp;</p>
<p>(ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Application</td>
<td><p>When originating from facility and is MPI Initialization:</p>
<p>MPI-STARTUP</p>
<p>When originating from MPI in response to Initialization:</p>
<p>MPIF MPI</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Facility</td>
<td>Station's facility number where Initial Batch request came from</td>
</tr>
<tr class="odd">
<td>5</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Application</td>
<td><p>When originating from facility for Initialization:</p>
<p>MPIF MPI</p>
<p>When originating from MPI:</p>
<p>MPI-STARTUP</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Facility</td>
<td>Station's facility number where Initial Batch request came from</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Batch Creation Date/Time</td>
<td>Date and time batch message was created</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Name/ID/Type</td>
<td><p>When originating from facility:</p>
<p>Component 1: Not used</p>
<p>Component 2: P</p>
<p>Component 3:</p>
<p>Sub Component 1:</p>
<p>message type: VQQ</p>
<p>Sub Component 2:</p>
<p>event type code:Q02</p>
<p>Component 4: 2.3</p>
<p>Component 5: AL</p>
<p>Component 6: NE</p>
<p>When originating from MPI:</p>
<p>Component 1: Not used</p>
<p>Component 2: P</p>
<p>Component 3:</p>
<p>Sub Component 1:</p>
<p>message type: ACK</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>80</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Comment</td>
<td><p>When originating from facility: (not used)</p>
<p>When originating from MPI:</p>
<p>Component 1: CA</p>
<p>(<em>Refer to table )</em></p>
<p>Component 2: Text Message, (not used)</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Control ID</td>
<td>Automatically generated by VistA HL7 Package</td>
</tr>
<tr class="even">
<td>12</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Reference Batch Control ID</td>
<td><p>When from MPI: Batch Control ID of batch message being acknowledged</p>
<p>When from facility: (not used)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc131832288" class="anchor"></span>Table ‑. BHS: Batch Header, HL7 attributes

BHS Field Definitions

### BHS-1 Batch Field Separator (ST) 00081

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the separator between the segment ID and the first real field, BHS-2 Batch Encoding Characters (ST) 00082. As such it serves as the separator and defines the character to be used as a separator for the rest of the message. Recommended value is \|, (ASCII 124).

### BHS-2 Batch Encoding Characters (ST) 00082

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the four characters in the following order:

- Component separator—Recommended values are ^ (ASCII 94).
- Repetition Separator—Recommended values are ~(ASCII 126).
- Escape Characters—Recommended values are \\ (ASCII 92).
- Subcomponent Separator—Recommended values are & (ASCII 38).

### BHS-3 Batch Sending Application (ST) 00083

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field uniquely identifies the sending application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site-defined.

When the sites initiate the message, MPIF-STARTUP is used. When the message is initiated by the MVI, MVI is used.

### BHS-4 Batch Sending Facility (ST) 00084

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the address of one of several occurrences of the same application within the sending system. Absent other considerations, the Medicare Provider ID might be used with an appropriate sub-identifier in the second component. Entirely user-defined.

Station Number of site making initial query request.

### BHS-5 Batch Receiving Application (ST) 00085

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field uniquely identifies the receiving applications among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site-defined.

When the sites initiate the message, MPIF MVI is used. When the message is initiated by the MVI, MPIF-STARTUP is used.

### BHS-6 Batch Receiving Facility (ST) 00086

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field identifies the receiving application among multiple identical instances of the application running on behalf of different organizations.

REF: For more information, please refer to the comments in the "BHS-4 Batch Sending Facility (ST) 00084" topic in this manual. Entirely site-defined.

Station Number of site making initial query request.

### BHS-7 Batch Creation Date/Time (TS) 00087

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date/time that the sending system created the message. If the time zone is specified, it will be used throughout the message as the default time zone.

### BHS-8 Batch Security (ST) 00088

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

### BHS-9 Batch Name/ID/Type (ST) 00089

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field can be used by the application processing the batch. It can have extra components if needed.

> Component 1:

> Component 2: P

> Component 3:

> Subcomponent 1: Message type

> Subcomponent 2: Event type

> Component 4: 2.3

### BHS-10 Batch Comment (ST) 00090

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is a comment field that is not further defined in the HL7 protocol.

When originating from facility: this field is not used.

When originating from MVI:Component 1: CA, (*Refer to table )*

> Component 2: Text Message, this field is not used.

### BHS-11 Batch Control ID (ST) 00091

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is used to uniquely identify a particular batch. It can be echoed back in BHS-12 Reference Batch Control ID (ST) 00092, if an answering batch is needed.

Automatically generated by the VistA Health Level 7 (HL7) application.

### BHS-12 Reference Batch Control ID (ST) 00092

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the value of BHS-11 Batch Control ID (ST) 00091 when this batch was originally transmitted. Not present on the initial batch query message from the VistA site.REF: For more information, please refer to the definition in the "BHS-11 Batch Control ID (ST) 00091" topic in this manual.

## BTS: Batch Trailer Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BTS segment defines the end of a batch.

| SEQ | LEN | DT | R/O | RP/# | Item# | Element Name    | <span class="smallcaps">VistA</span> Description |
|---------|---------|--------|---------|----------|-----------|---------------------|------------------------------------------------------|
| 1       | 10      | ST     |         |          | 00093     | Batch Message Count | Number of messages within batch                      |
| 2       | 80      | ST     |         |          | 00090     | Batch Comment       | Passed but not used by MPI.                          |
| 3       | 100     | CM     |         | Y        | 00095     | Batch Totals        | Passed but not used by MPI.                          |

<span id="_Toc131832289" class="anchor"></span>Table ‑. BTS: Batch Trailer, HL7 attributes

BTS Field Definitions

### BTS-1 Batch Message Count (ST) 00093

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the count of the individual messages contained within the batch.

### BTS-2 Batch Comment (ST) 00090

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is not used by the MVI software.

### BTS-3 Batch Totals (NM) 00095

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is not used by the MVI software.

## DSC: Continuation Pointer Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DSC segment is used in the continuation protocol.

| SEQ | LEN | DT | OPT | RP | TBL | Item | Element Name     |
|---------|---------|--------|---------|--------|---------|----------|----------------------|
| 1       | 180     | ST     | O       |        |         | 00014    | Continuation Pointer |
| 2       | 1       | ID     | O       |        |         | 01354    | Continuation Style   |

<span id="_Toc131832290" class="anchor"></span>Table ‑. DSC: Continuation Pointer, HL7 Attributes

DSC Field Definitions

### DSC-1 Continuation pointer (ST) 00014

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the continuation pointer. In an initial query, this field is not present. If the responder returns a value of null or not present, then there is no more data to fulfill any future continuation requests.

### DSC-2 Continuation style (ID) 01354

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: Indicates whether this is a fragmented message, or if it is part of an interactive continuation message (see Section 5.6.3, "Interactive continuation of response messages").

REF: Refer for valid values.

| Value | Description          |
|-----------|--------------------------|
| F         | Fragmentation            |
| I         | Interactive Continuation |

<span id="_Toc131832291" class="anchor"></span>Table ‑. HL7 Table 0398: Continuation style code

## ERR: Error Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERR segment is used to add error comments to Acknowledgement messages.

| SEQ | LEN | DT | OPT | RP/# | TBL# | Item | Element Name        |
|---------|---------|--------|---------|----------|----------|----------|-------------------------|
| 1       | 80      | CM     | R       | Y        |          | 00024    | Error Code and Location |

<span id="_Toc131832292" class="anchor"></span>Table ‑. ERR: Error, HL7 attributes

ERR Field Definitions

### ERR-1 Error Code and Location (CM) 00024

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<segment ID (ST)\> ^ \<sequence (NM)\> ^ \<field position (NM)\> ^ \<code identifying error (CE)\>

Definition: This field identifies an erroneous segment in another message. The second component is an index if there is more than one segment of type \<segment ID\>. For systems that do not use the HL7 Encoding Rules, the data item number may be used for the third component. The fourth component (which references , (as a CE data type) is restricted from having any subcomponents as the subcomponent separator is now the CE's component separator.

REF: For a listing of , please refer to section 3.10.5, "MSA-6 Error Condition (CE) 00023."

> **NOTE:** This will only be used when communicating between PSIM and the MPI when the application level acknowledgement needs to record an error condition has happened on the PSIM side.

## EVN: Event Type Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EVN segment is used to communicate necessary trigger event information to receiving applications.

REF: The valid event types for all chapters are contained in Table 3‑6 in this manual, "EVN: Event Type."

| SEQ | LEN | DT | OPT | RP/# | TBL | Item | Element Name        | VistA Description                      |
|---------|---------|--------|---------|----------|---------|----------|-------------------------|--------------------------------------------|
| 1       | 3       | ID     | B       |          |         | 00099    | Event Type Code         | Refer to table                             |
| 2       | 26      | TS     | R       |          |         | 00100    | Recorded Date/Time      | Date/Time Event Occurred                   |
| 3       | 26      | TS     | O       |          |         | 00101    | Date/Time Planned Event | Not populated or used by the MPI           |
| 4       | 3       | IS     | O       |          |         | 00102    | Event Reason Code       | Refer to table                             |
| 5       | 250     | XCN    | O       | Y        |         | 00103    | Operator ID             | User causing event                         |
| 6       | 26      | TS     | O       |          |         | 01278    | Event Occurred          | Date/Time of Event                         |
| 7       | 180     | HD     | O       |          |         | 01534    | Event Facility          | Station Number of facility sending message |

<span id="_Ref31700085" class="anchor"></span>Table ‑. EVN: Event Type, HL7 attributes

EVN Field Definitions

### EVN-1 Event Type Code (ID) 00099

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: *This field has been retained for backward compatibility only.* We recommend using the second component (trigger event) of [MSH-9 - Message Type](#_MSH-9__Message) to transmit event type code information. This field contains the events corresponding to the trigger events described in this section (e.g., admission, transfer, or registration).

|           |                         |
|-----------|-------------------------|
| Value | Description         |
| A1        | Patient Admission       |
| A2        | Patient Discharge       |
| A3        | Patient Clinic Checkout |
| A24       | Link Patient            |
| A31       | CMOR Change Request     |
| A37       | Unlink Patient          |
| A43       | Mismatched Patient      |

<span id="_Toc3901218" class="anchor"></span>Table ‑. HL7 Table 0003 EVN: ADT/R Event Type Codes

### EVN-2 Recorded Date/Time (TS) 00100

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When sent from site:Definition: This field contains the patient date/time of last treatment. This value is also stored on the local VistA system in the TREATING FACILITY file (#391.91) and can be obtained via the VistA supported API TFL^VAFCTFU1 (IA \#2990).

When sent from the MVI:Definition: This field contains the corresponding date last updated field for the Primary View, contained in MPI VETERAN/CLIENT file \#985, or the corresponding date last updated field for the Correlation's View, contained in MPI FACILITY ASSOCIATION file \#985.5.

### EVN-3 Date/Time Planned Event (TS) 00101

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Passed but not used by MVI.

### EVN-4 Event Reason Code (IS) 00102

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date last treated event reason. Below is a list of the currently supported values.

| Value | Description         |
|-----------|-------------------------|
| A1        | Patient Admission       |
| A2        | Patient Discharge       |
| A3        | Patient Clinic Checkout |
| A24       | Link Patient            |
| A31       | CMOR Change Request     |
| A37       | Unlink Patient          |

<span id="_Toc131832295" class="anchor"></span>Table ‑. User-defined Table 0062: Event Reason

### EVN-5 Operator ID (XCN) 00103

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<ID number (ST)\> ^ \<family name (ST)\> \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\>

> Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

> Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

> Subcomponents of assigning facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Definition: This field identifies the individual responsible for triggering the event. Refer to for suggested values.

| Value | Description                 |
|-------|-----------------------------|
|       | No suggested values defined |

<span id="_Toc131832296" class="anchor"></span>Table ‑. User-defined Table 0188─Operator ID

Example value:

Internal VistA ien from File \#200~lastname~firstname~middlename\~\~\~\~~"USVHA"&&"0363"~"L"\~\~~"NI"~"VA FACILITY ID"&station#&"L"

12584~LASTNAME~FIRSTNAME\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&500&L

<span id="_Hlt476034640" class="anchor"></span>Figure ‑. EVN: Event Type Segment example

### EVN-6 Event Occurred (TS) 01278

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date/time that the event actually occurred. For example, on a transfer (A02 transfer a patient), this field would contain the date/time the patient was actually transferred. This value is also stored on the local VistA system in the TREATING FACILITY file (#391.91) and can be obtained via the VistA supported API TFL^VAFCTFU1 (IA \#2990).

### EVN-7 Event Facility (HD) 01534

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

Definition: This field identifies the actual facility where the event occurred as differentiated from the sending facility (MSH-4). It would be the facility at which the Operator (EVN-5) has entered the event.

Use Case: System A is where the patient is originally registered. This registration message is sent to an MVI, System B. The MVI needs to broadcast the event of this update and would become the sending facility. This new field would allow for retention of knowledge of the originating facility where the event occurred.

## MFA: Master File Acknowledgement Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Technical Steward for the MFA segment is CQ.

The MFA segment contains the following fields:

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 25%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>VistA Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>3</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>00664</td>
<td>Record-Level Event Code</td>
<td><p>Type of Update:</p>
<p>MUP – update TF</p>
<p>MAD – Add TF</p>
<p>MDL – delete TF</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>ST</td>
<td>C</td>
<td></td>
<td></td>
<td>00665</td>
<td>MFN Control ID</td>
<td>Station number data from MPI's gold copy of the correlated/linked system id's</td>
</tr>
<tr class="odd">
<td>3</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00668</td>
<td>Event Completion Date/Time</td>
<td>Last Treatment Date/Time</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td><a href="#TABLE_0181">0181</a></td>
<td>00669</td>
<td>MFN Record Level Error Return</td>
<td>Status</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>N</td>
<td>Y</td>
<td>9999</td>
<td>01308</td>
<td>Primary Key Value - MFA</td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>6</td>
<td>3</td>
<td>ID</td>
<td>N</td>
<td>Y</td>
<td>0355</td>
<td>01320</td>
<td>Primary Key Value Type - MFA</td>
<td>Passed but not used by MPI.</td>
</tr>
</tbody>
</table>

<span id="_Toc131832298" class="anchor"></span>Table ‑. MFA: Master File Acknowledgement, HL7 attributes

MFA Field Definitions

### MFA-1 Record-Level Event Code (ID) 00664

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field defines record-level event for the master file record identified by the MFI segment and the primary key in this segment.

REF: For a list of valid values, please refer to Table 3‑14 in this manual, "."

### MFA-2 MFN Control ID (ST) 00665

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field uniquely identifies the particular record (identified by the MFE segment) being acknowledged by this MFA segment. When returned to the originating system via the MFA segment, this field allows the target system to precisely identify which change to this record is being acknowledged.

### MFA-3 Event Completion Date/Time (TS) 00668

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field contains the field contains the last treatment date at that facility. This information is currently being used to update the local VistA Treating Facility (#391.71). The Treating Facility file information is used by VistA CPRS-RDV to allow the user to identify whether they want to pull remote data or not.

### MFA-4 MFN Record Level Error Return (CE) 00669

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field contains the status of the requested update. Site-defined table, specific to each master file being updated via this transaction.

REF: For a list of suggested values, please refer to Table 3‑11 in this manual, "."

All such tables will have at least the following two return code values:

| Value | Description                                               |
|-----------|---------------------------------------------------------------|
| S         | Successful posting of the record defined by the MFE segment   |
| U         | Unsuccessful posting of the record defined by the MFE segment |

<span id="_Ref104385394" class="anchor"></span>Table ‑. User-defined Table <span id="TABLE_0181" class="anchor"></span>0181: MFN Record-level Error Return

### MFA-5 Primary Key Value - MFA (CE) 01308

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.Definition: This field contains the HL7 data type of *MFE-4 - Primary key value*. The valid values for the data type of a primary key are listed in.

| Value | Description     |
|-------|-----------------|
| PL    | Person location |
| CE    | Coded element   |

<span id="_MFA_-_master" class="anchor"></span>Table ‑. HL7 Table 0355─Primary key value type

> **NOTE:** This table contains data types for MFE-4 values present in HL7 defined master files. As HL7 adopts a new master file that contains a data type for MFE-4 not defined in Table 0355, the data type will be added to Table 0355. For locally defined master files, this table can be locally extended with other HL7 data types as defined in section 2.6.6.

### MFA-6 Primary Key Value Type - MFA (ID) 01320 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

## MFE: Master File Entry Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Technical Steward for the MFE segment is CQ.

| SEQ | LEN | DT | OPT | RP# | TBL# | Item | Element Name        | VistA Description                                     |
|---------|---------|--------|---------|---------|----------|----------|-------------------------|-----------------------------------------------------------|
| 1       | 3       | ID     | R       |         |          | 00664    | Record-Level Event Code | Type of Update                                            |
| 2       | 20      | ST     | C       |         |          | 00665    | MFN Control ID          | Station Number                                            |
| 3       | 26      | TS     | O       |         |          | 00662    | Effective Date/Time     | Date Last Treated for non-VAMC systems this would be null |
| 4       | 200     | Varies | R       | Y       |          | 00667    | Primary Key Value - MFE | Site and ICN involved                                     |
| 5       | 3       | ID     | N       | Y       | 0355     | 01319    | Primary Key Value Type  |                                                           |

<span id="_Toc131832301" class="anchor"></span>Table ‑. MFE: Master File Entry, HL7 attributes

MFE Field Definitions

### MFE-1 Record-Level Event Code (ID) 00664

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field defines the record-level event for the master file record identified by the MFI segment and the primary key field in this segment.

REF: For a list of valid values, please refer to Table 3‑14 in this manual, "."

| Value | Description                          |
|-----------|------------------------------------------|
| MAD       | Add record to master file                |
| MDL       | Delete record from master file           |
| MUP       | Update record for master file            |
| MDC       | Deactivate/Merged record for master file |

<span id="_Ref104385343" class="anchor"></span>Table ‑. HL7 Table 0180: Record-level Event Code

> **NOTE:** If the file-level event code is "REP" (replace file), then each MFE segment must have a record-level event code of "MAD" (add record to master file).

### MFE-2 MFN Control ID (ST) 00665

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: A number or other identifier that uniquely identifies this change to this record from the point of view of the originating system. When returned to the originating system via the MFA segment, this field allows the target system to precisely identify which change to this record is being acknowledged. This field will contain a unique identifier, which will be VHA's STATION NUMBER (#99) of the INSTITUTION file (#4). The assumption is that prior to subscribing to the MVI for patient identification management that there will be a formal process of setting up the necessary communication and uniquely identification of the new system.

> **NOTE:** This segment does not contain a Set ID field. The [MFE-2 - MFN control ID](#_MFE-2__) implements a more general concept than the Set ID. It takes the place of the SET ID in the MFE segment.

> **NOTE:** In situations where the same Station Number is sent multiple times in the same HL7 message to define unique segments, an incremented number is concatenated with a hyphen at the end of each Station Number. See example as follows with Station Numbers underlined:

> MFE^MAD^<u>500-1</u>^20020913112211-0500^1001170419V238836\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|123\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX

> ZET^A1

> MFE^MDC^<u>500-2</u>^20020913112211-0500^1001170419V238836\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|234\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L^CX

### MFE-3 Effective Date/Time (TS) 00662

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date of last treatment if the system is a system that would contain that type of data.

### MFE-4 Primary Key Value - MFE (Varies) 00667

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<STATION#\> ^ \<INSTITUTION NAME\> ^ \<"VA"\> ^ \<ICN\> ^ \<"ICN"\> ^ \<"VA"\> ^

Definition: This field will contain the unique identifier from MFE-2, the name of the unique system, the system (VA), the VHA unique identifier or ICN, and the system again.

#### Assigning authority (HD): The assigning authority is a unique identifier of the system (or organization or agency or department) that creates the data.  It is a HD data type.  Assigning authorities are unique across a given HL7 implementation.  *User-defined Table 0363 – Assigning authority* is used as the HL7 identifier for the user-defined table of values for the first sub-component, namespace ID.  

| Value  | Description                                           |
|--------|-------------------------------------------------------|
| AUSDVA | Australia - Dept. of Veterans Affairs                 |
| AUSHIC | Australia - Health Insurance Commission               |
| CANAB  | Canada - Alberta                                      |
| CANBC  | Canada - British Columbia                             |
| CANMB  | Canada - Manitoba                                     |
| CANNB  | Canada - New Brunswick                                |
| CANNF  | Canada - Newfoundland                                 |
| CANNS  | Canada - Nova Scotia                                  |
| CANNT  | Canada - Northwest Territories                        |
| CANNU  | Canada - Nanavut                                      |
| CANON  | Canada - Ontario                                      |
| CANPE  | Canada - Prince USERNAME Island                       |
| CANQC  | Canada - Quebec                                       |
| CANSK  | Canada - Saskatchewan                                 |
| CANYT  | Canada - Yukon Territories                            |
| NLVWS  | NL - Ministerie van Volksgezondheid, Welzijn en Sport |
| USCDC  | US Center for Disease Control                         |
| USHCFA | US Healthcare Finance Authority                       |
| USSSA  | US Social Security Administration                     |
| USDOD  | US Department of Defense                              |
| USVBA  | US Veterans Benefits Administration                   |

<span id="_Toc3901226" class="anchor"></span>Table ‑. User-defined HL7 Table 0363 – Assigning authority

### MFE-5 Primary Key Value Type (ID) 01319 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

## MFI: Master File Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A treating facility list identifies the systems that know a particular Integration Control Number (ICN). This list is maintained on the MVI and synchronized as systems are added, updated, or deleted from the list. The MFI segment is used to identify the type master file, in this case Treating Facility (TFL).

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>VistA Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td><a href="#TABLE_0175">0175</a></td>
<td>00658</td>
<td>Master File Identifier</td>
<td>TFL</td>
</tr>
<tr class="even">
<td>2</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>00659</td>
<td>Master File Application Identifier</td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>3</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>00660</td>
<td>File-Level Event Code</td>
<td><p>Type of update</p>
<p>UPD or REP</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00661</td>
<td>Entered Date/Time</td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00662</td>
<td>Effective Date/Time</td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>00663</td>
<td>Response Level Code</td>
<td>Site Station Number~Name?</td>
</tr>
</tbody>
</table>

<span id="_Toc131832303" class="anchor"></span>Table ‑. MFI: Master File Identification, HL7 attributes

MFI Field Definitions

### MFI-1 Master File Identifier (CE) 00658

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field is a CE data type that identifies a standard HL7 master file. The table below (Table 3‑17) was extended by local agreement to include "TFL."

REF: For a list of valid values, please refer to Table 3‑17 in this manual, "."

| Value | Description                    |
|-----------|------------------------------------|
| TFL       | Treating Facility list master file |

<span id="_Ref104385465" class="anchor"></span>Table ‑. HL7 Table <span id="TABLE_0175" class="anchor"></span>0175: Master File Identifier Code

### MFI-3 File-Level Event Code (ID) 00660

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REF: For a list of valid values, please refer to Table 3‑18 in this manual, "."

| Value | Description                                                                             |
|-----------|---------------------------------------------------------------------------------------------|
| REP       | Replace current version of this master file with the version contained in this message      |
| UPD       | Change file records as defined in the record-level event codes for each record that follows |

<span id="_Ref104385506" class="anchor"></span>Table ‑. HL7 Table 0178: File Level Event Code

### MFI-6 Response Level Code (ID) 00663

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: These codes specify the application response level defined for a given Master File Message at the MFE segment level as defined in (Table 3‑19 in this manual). Required for MFN-Master File Notification message. Specifies additional detail (beyond [MSH-15 - Accept Acknowledgement type](#_MSH-15_Accept_acknowledgment_type () and ) for application-level <u>Acknowledgement</u> paradigms for Master Files transactions. and operate as defined in Chapter 2 in the HL7 Standard Version 2.4 documentation.

| Value | Description                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------|
| AL        | Always. All MFA segments (whether denoting errors or not) must be returned via the application-level Acknowledgement message |

<span id="_Ref104385551" class="anchor"></span>Table ‑. HL7 Table 0179: Response Level

## MRG: Merge Patient Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRG segment provides receiving applications with information necessary to initiate the merging of patient data as well as groups of records. It is intended that this segment be used throughout the standard to allow the merging of registration, accounting, and clinical records within specific applications.

The assigning authority, the fourth component of the patient identifiers, is a HD data type that is uniquely associated with the assigning authority that originally assigned the number. A given institution, or group of intercommunicating institutions, should establish a list of assigning authorities that may be potential assignors of patient identification (and other important identification) numbers. The assigning authority must be unique across applications at a given site. This field is required in HL7 implementations that have more than a single Patient Administration application assigning such numbers.

| SEQ | LEN | DT | OPT | RP | TBL | Item | Element Name              | VistA Description                       |
|---------|---------|--------|---------|--------|---------|----------|-------------------------------|---------------------------------------------|
| 1       | 250     | CX     | R       | Y      |         | 00211    | Prior Patient Identifier List | Integration Control Number of "FROM" record |
| 2       | 250     | CX     | B       | Y      |         | 00212    | Prior Alternate Patient ID    | Not populated or used by the MPI.           |
| 3       | 250     | CX     | O       |        |         | 00213    | Prior Patient Account Number  | Not populated or used by the MPI.           |
| 4       | 250     | CX     | B       |        |         | 00214    | Prior Patient ID              | Not populated or used by the MPI.           |
| 5       | 250     | CX     | O       |        |         | 01279    | Prior Visit Number            | Not populated or used by the MPI.           |
| 6       | 250     | CX     | O       |        |         | 01280    | Prior Alternate Visit ID      | Not populated or used by the MPI.           |
| 7       | 250     | XPN    | O       | Y      |         | 01281    | Prior Patient Name            | Patient's Name                              |

<span id="_Toc131832307" class="anchor"></span>Table ‑. MRG: Merge Patient Information, HL7 attributes

MRG Field Definitions

### MRG-1 Prior Patient Identifier List (CX) 00211

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \< assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \< assigning facility (HD) ^ \<effective date (DT)\> ^ \<expiration date (DT)\>

> Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

> Subcomponents of assigning facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Definition: This field contains the prior patient identifier list. This field contains a list of potential "old" numbers to match. Only one old number can be merged with one new number in a transaction.

REF: For a list of valid values, please refer to "HL7 Table 0061—Check Digit Scheme" in the HL7 Standard Version 2.4 documentation.

The assigning authority and identifier type code are strongly recommended for all CX data types.

### MRG-2 Prior Alternate Patient ID (CX) 00212

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \< assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \< assigning facility (HD) ^ \<effective date (DT)\> ^ \<expiration date (DT)\>

> Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

> Subcomponents of assigning facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Definition: *This field has been retained for backward compatibility only.* Use [MRG-1 - Prior patient identifier list](#_MRG-1_Prior_patient_identifier list) for all patient identifiers. This field contains the prior alternate patient identifier.

REF: For a list of valid values, please refer to "HL7 Table 0061—Check Digit Scheme" in the HL7 Standard Version 2.4 documentation.

This field is passed but not used by the MVI software.

The assigning authority and identifier type code are strongly recommended for all CX data types.

### MRG-3 Prior Patient Account Number (CX) 00213

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

### MRG-4 Prior Patient ID (CX) 00214

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

### MRG-5 Prior Visit Number (CX) 01279

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

### MRG-6 Prior Alternate Visit ID (CX) 01280

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

### MRG-7 Prior Patient Name (XPN) 01281

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient name is passed for this value.Components: In Version 2.3, replaces the PN data type. \<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

> Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

Definition: This field contains the prior name of the patient. This field is passed but not used by MVI to change a patient name.

## MSA: Message Acknowledgement Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSA segment contains information sent while acknowledging another message.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>VistA Desc</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>00018</td>
<td>Acknowledgement Code</td>
<td>Refer to Table</td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>00010</td>
<td>Message Control ID</td>
<td>Message Control ID of message being acknowledged</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00020</td>
<td>Text Message</td>
<td><p>Error condition returned from processing original message.</p>
<p><strong>NOTE:</strong> The error text is returned in the ERR segment ONLY with PSIM messaging. See ERR segment for more information.</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>15</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00021</td>
<td>Expected Sequence Number</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td>B</td>
<td></td>
<td>0102</td>
<td>00022</td>
<td>Delayed Acknowledgement Type</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00023</td>
<td>Error Condition</td>
<td>ICN or DFN associated with original message processed.</td>
</tr>
</tbody>
</table>

<span id="_Toc131832308" class="anchor"></span>Table ‑. MSA: Message Acknowledgement, HL7 attributes

MSA Field Definitions

### MSA-1 Acknowledgement Code (ID) 00018

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains an Acknowledgement code.

AA is sent when the application successfully processed and executed the requested function.

AE is sent when the application was unsuccessful in executing the requested IdM function due to an internal application error.

AR is sent when the application if the application is unable to locate the patient within its database. This would be the case if MVI erroneously sent a system a message for a patient that is not known to that system.

REF: For more information, please refer to the message processing rules in the HL7 Version 2.4 documentation.

REF: For a list of valid values, please refer to Table 3‑22 in this manual, .

| Value | Description                                                                        |
|-----------|----------------------------------------------------------------------------------------|
| AA        | Original mode: Application Accept - Enhanced mode: Application Acknowledgement: Accept |
| AE        | Original mode: Application Error - Enhanced mode: Application Acknowledgement: Error   |
| AR        | Original mode: Application Reject - Enhanced mode: Application Acknowledgement: Reject |
| CA        | Enhanced mode: Accept Acknowledgement: Commit Accept                                   |
| CE        | Enhanced mode: Accept Acknowledgement: Commit Error                                    |
| CR        | Enhanced mode: Accept Acknowledgement: Commit Reject                                   |

<span id="_Ref104385592" class="anchor"></span>Table ‑. HL7 Table 0008: Acknowledgement Code

### MSA-2 Message Control ID (ST) 00010

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the message control ID of the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

### MSA-3 Text message (ST) 00020

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This optional field further describes an error condition. This text may be printed in error logs or presented to an end user.

Use of *MSA-3-text message* and *MSA-6-error condition* are deprecated in favor of *ERR-1*-*Error code and location*. The ERR segment allows for richer descriptions of the erroneous conditions.

> **NOTE:** The error text is returned in the ERR segment ONLY with PSIM messaging. See ERR segment definition for more information.

### MSA-5 Delayed Acknowledgement Type (ID) 00022

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is passed but not used by the MVI software.

Definition: *This field has been retained for backward compatibility.*

| Value | Description                                   |
|-------|-----------------------------------------------|
| D     | Message received, stored for later processing |
| F     | Acknowledgement after processing              |

<span id="_Toc131832310" class="anchor"></span>Table ‑. HL7 Table 0102: Delayed Acknowledgement type

### MSA-6 Error Condition (CE) 00023

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field allows the acknowledging system to use a user-defined error code to further specify the error text sent in MSA-3. The error codes listed below are pulled from the HL7 v2.4 standard table 0357, however locally identified text can be passed as well by leaving the identifier blank and coding scheme as "L". This will be used to raise an exception on the central MVI system.

| Error Condition Code | Error Condition Text   | Description/Comment                                                                                                                   |
|--------------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Success              |                            |                                                                                                                                           |
| 0                        | Message accepted           | Success. Optional, as the AA conveys success. Used for systems that must always return a status code.                                     |
| 200                      | Unsupported message type   | The Message Type is not supported.                                                                                                        |
| 201                      | Unsupported event code     | The Event Code is not supported.                                                                                                          |
| 202                      | Unsupported processing ID  | The Processing ID is not supported.                                                                                                       |
| 203                      | Unsupported version id     | The Version ID is not supported.                                                                                                          |
| 204                      | Unknown key identifier     | The ID of the patient, order, etc., was not found. Used for transactions other than additions (e.g., transfer of a non-existent patient). |
| 205                      | Duplicate key identifier   | The ID of the patient, order, etc., already exists. Used in response to addition transactions (Admit, New Order, etc.).                   |
| 206                      | Application record locked  | The transaction could not be performed at the application storage level (e.g., database locked).                                          |
| 207                      | Application internal error | A catchall for internal errors not explicitly covered by other codes.                                                                     |

<span id="_Ref104385100" class="anchor"></span>Table ‑. HL7 Table 0357: Message Error Condition Codes

## MSH: Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 22%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>VistA Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>00001</td>
<td>Field Separator</td>
<td>Recommended value is <strong>^</strong> (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>00002</td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = <strong>\</strong> (back slash)</p>
<p>Subcomponent = &amp;</p>
<p>(ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td><a href="#TABLE_0361">0361</a></td>
<td>00003</td>
<td>Sending Application</td>
<td><p>When originating from facility and the message type is A01, A03, A04 or A08:</p>
<p>RG ADT</p>
<p>When originating from facility and the message type is A28 or A24:</p>
<p>MPIF TRIGGER</p>
<p>When originating from facility OR MPI and the message type is A31, A37, A43 or A24:</p>
<p>MPIF TRIGGER</p>
<p>When originating from facility or MPI and the message type is MFN or MFK or A19:</p>
<p>VAFC TRIGGER</p>
<p>When originating from facility and the message type is a query via the Direct Connect:</p>
<p>MPI_LOAD</p>
<p>When originating from MPI and the message type is the response to the query via the Direct Connect or via the Q22/K22 query/response:</p>
<p>MPI</p>
<p>For batch queries:</p>
<p>MPI-STARTUP</p>
<p>Change CMOR messages:</p>
<p>RG CIRN</p>
<p>MPIF CMOR CHNG</p>
<p>MPIF CMOR RSLT</p>
<p>When the message type is A24, A31 or A43 and is sent via HLO from the MPI:</p>
<p>MPI</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>00004</td>
<td>Sending Facility</td>
<td><p>When originating from facility:</p>
<p>Station's facility number</p>
<p>When originating from MPI and message is the batch query:</p>
<p>MPI</p>
<p>When originating from the MPI and not the batch query:</p>
<p>200M</p>
<p>When originating from the MPI and the message type is A24, A31 or A43 and is being sent via HLO the port number of HLO listener for the sending site will be included at the end of the domain name preceded by a colon.</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>00005</td>
<td>Receiving Application</td>
<td><p>When originating from facility and the message type is A01, A03, A04 or A08:</p>
<p>RG ADT</p>
<p>When originating from facility and the message type is A28 or A24:</p>
<p>MPIF TRIGGER</p>
<p>When originating from facility OR MPI and the message type is A31, A37, A43 or A24:</p>
<p>MPIF TRIGGER</p>
<p>When originating from facility or MPI and the message type is MFN or MFK or A19:</p>
<p>VAFC TRIGGER</p>
<p>When originating from facility and the message type is a query via the Direct Connect:</p>
<p>MPI_LOAD</p>
<p>When originating from MPI and the message type is the response to the query via the Direct Connect or via the Q22/K22 query/response:</p>
<p>MPI</p>
<p>For batch queries:</p>
<p>MPI-STARTUP</p>
<p>Change CMOR messages:</p>
<p>RG CIRN</p>
<p>MPIF CMOR CHNG</p>
<p>MPIF CMOR RSLT</p>
<p>When the message type is A24, A31 or A43 and is sent via HLO from the MPI:</p>
<p>PSIM</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>00006</td>
<td>Receiving Facility</td>
<td><p>When message is originating at the facility to the MPI and the message is related to the CMOR Change:</p>
<p>Station Number of facility sending message</p>
<p>When the message is originating from the facility to the MPI and the message is the Query (batch or real-time): there is no value sent</p>
<p>Otherwise, when the message is originating at the facility to the MPI:</p>
<p>200M</p>
<p>When originating from the MPI and the message type is A24, A31 or A43 and is being sent via HLO the port number of HLO listener for the receiving site will be included at the end of the domain name preceded by a colon.</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>00007</td>
<td>Date/Time Of Message</td>
<td>Date and time message was created</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00008</td>
<td>Security</td>
<td>(not used)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>13</td>
<td>CM</td>
<td>R</td>
<td></td>
<td></td>
<td>00009</td>
<td>Message Type</td>
<td><p><u>2 Components</u></p>
<p>Refer to Table 0076</p>
<p>Refer to Table 0003</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>00010</td>
<td>Message Control ID</td>
<td><p>Automatically generated by VistA HL7 Package</p>
<p><strong>NOTE:</strong> The HLO message number will include a space.</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>3</td>
<td>PT</td>
<td>R</td>
<td></td>
<td></td>
<td>00011</td>
<td>Processing ID</td>
<td><strong>P</strong> (production)</td>
</tr>
<tr class="even">
<td>12</td>
<td>60</td>
<td>VID</td>
<td>R</td>
<td></td>
<td></td>
<td>00012</td>
<td>Version ID</td>
<td><strong>2.3</strong> (Version 2.3) or <strong>2.4</strong> (version 2.4)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00013</td>
<td>Sequence Number</td>
<td>(not used)</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00014</td>
<td>Continuation Pointer</td>
<td>(not used)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00015</td>
<td>Accept Acknowledgement Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00016</td>
<td>Application Acknowledgement Type</td>
<td><p>AL (always acknowledge)</p>
<p>Unless related to the Change of CMOR messages then is NE (never acknowledge)</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00017</td>
<td>Country Code</td>
<td>USA</td>
</tr>
<tr class="even">
<td>18</td>
<td>16</td>
<td>ID</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00692</td>
<td>Character Set</td>
<td>(not used)</td>
</tr>
<tr class="odd">
<td>19</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00693</td>
<td>Principal Language Of Message</td>
<td>(not used)</td>
</tr>
<tr class="even">
<td>20</td>
<td>20</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>01317</td>
<td>Alternate Character Set Handling Scheme</td>
<td>(not used)</td>
</tr>
<tr class="odd">
<td>21</td>
<td>10</td>
<td>ID</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>01598</td>
<td>Conformance Statement ID</td>
<td>(not used)</td>
</tr>
</tbody>
</table>

<span id="_Toc131832312" class="anchor"></span>Table ‑. MSH: Message Header, HL7 attributes

MSH Field Definitions

### MSH-1 Field Separator (ST) 00001

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the separator between the segment ID and the first real field, *MSH-2-encoding characters*. As such it serves as the separator and defines the character to be used as a separator for the rest of the message. Recommended value is \|, (ASCII 124).

### MSH-2 Encoding Characters (ST) 00002

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the four characters in the following order:

- Component separator—Recommended values are ^ (ASCII 94).
- Repetition Separator—Recommended values are ~(ASCII 126).
- Escape Characters—Recommended values are \\ (ASCII 92).
- Subcomponent Separator—Recommended values are & (ASCII 38).

### MSH-3 Sending Application (HD) 00003

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

Definition: This field uniquely identifies the sending application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site-defined.

The [User-defined Table 0361: Sending/Receiving Application](#HL0361) (Table 3‑26 in this manual) is used as the user-defined table of values for the first component, as shown below:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Value</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MPI</td>
<td><p>When originating from MPI and the message type is the response to the query via the Direct Connect.</p>
<p>This is also used for the QBP~Q22 query to the MPI and the responding RSP~K22.</p>
<p>When the HLO messages are sent from the MPI for the message types A24, A31 and A43 MPI is also sent.</p></td>
</tr>
<tr class="even">
<td>MPI_LOAD</td>
<td>When originating from facility and the message type is a query via the Direct Connect.</td>
</tr>
<tr class="odd">
<td>MPIF CMOR CHNG</td>
<td>This will be used when communicating a CMOR change via an ADT-A31 message.</td>
</tr>
<tr class="even">
<td>MPIF CMOR RSLT</td>
<td>This will be used when communicating a CMOR Change via an ADT-A31 message.</td>
</tr>
<tr class="odd">
<td>MPIF TRIGGER</td>
<td>When originating from facility or the MPI and the message type is ADT-A24, ADT-A31 (MPI update message), ADT-A37, or ADT-A43.</td>
</tr>
<tr class="even">
<td>MPIF TRIGGER</td>
<td>When originating from facility and the message type is ADT-A24 or ADT-A28.</td>
</tr>
<tr class="odd">
<td>MPI-STARTUP</td>
<td>For batch queries.</td>
</tr>
<tr class="even">
<td>RG ADT</td>
<td>When originating from facility and the message type is ADT-A01, ADT-A03, ADT-A04, and ADT-A08 messages.</td>
</tr>
<tr class="odd">
<td>RG CIRN</td>
<td>This will be used when sending a change of CMOR ADT-A31 message.</td>
</tr>
<tr class="even">
<td>VAFC TRIGGER</td>
<td>When originating from facility or MPI and the message type is MFN-M05 Treating Facility Master file update message</td>
</tr>
</tbody>
</table>

<span id="_Ref104385644" class="anchor"></span>Table ‑. User-defined Table <span id="TABLE_0361" class="anchor"></span>0361: Sending/Receiving Application

### MSH 4 -Sending Facility (HD) 00004

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

Definition: This field further describes the sending application, . With the promotion of this field to an HD data type, the usage has been broadened to include not just the sending facility but also other organizational entities (entirely site-defined), such as:

> a\. The organizational entity responsible for sending application.

> b\. The responsible unit.

> c\. A product or vendor's identifier, etc.

The (Table 3‑27 in this manual) is used as the HL7 identifier for the user-defined table of values for the first component, as shown below:

| Value                           | Description             |
|-------------------------------------|-----------------------------|
| \<vha_station#^HL7.domainname^DNS\> | No suggested values defined |

<span id="_Ref104385679" class="anchor"></span>Table ‑. User-defined Table 0362: Sending/Receiving Facility

### MSH-5 Receiving Application (HD) 00005

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

Definition: This field uniquely identifies the receiving application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site‑defined.

The User-defined Table 0361: Sending/Receiving Application (Table 3‑26 in this manual) is used as the HL7 identifier for the user-defined table of values for the first component.

### MSH-6 Receiving Facility (HD) 00006

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<namespace ID (IS)\> ^ \<universal ID (ST)\> ^ \<universal ID type (ID)\>

Definition: This field identifies the system that is communicating the event. The (Table 3‑27 in this manual) is used as the HL7 identifier for the user-defined table of values for the first component. Entirely site‑defined.

### MSH-7 Date/Time of Message (TS) 00007

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date/time that the sending system created the message. If the time zone is specified, it will be used throughout the message as the default time zone.

> **CAUTION:** This field was made required in Version 2.4. Messages with versions prior to 2.4 are *not* required to value this field. This usage supports backward compatibility.

### MSH-9 Message Type (CM) 00009 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<message type (ID)\> ^ \<trigger event (ID)\> ^ \<message structure (ID)\>

Definition: This field contains the message type, trigger event, and the message structure ID for the message.

The first component is the message type code defined by HL7 Table 0076—Message Type. The second component is the trigger event code defined by . The third component is the abstract message structure code defined by HL7 Table 0354—Message Structure. This table has two columns. The first column contains the value of this code, which describes a particular HL7 "abstract message structure definition" in terms of segments. The second column of Table 0354 lists the various HL7 trigger events that use the particular abstract message definition.

REF: For more information on the HL7 Table 0076—Message Type and HL7 Table 0354—Message Structure, please refer to the HL7 Standard Version 2.4 documentation.

The receiving system uses this field to recognize the data segments, and possibly, the application to which to route this message. The second component is not required on response or Acknowledgement messages.

### MSH-10 Message Control ID (ST) 00010

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgement segment (MSA).

### MSH-11 Processing ID (PT) 00011

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<processing ID (ID)\> ^ \<processing mode (ID)\>

Definition: This field is used to decide whether to process the message as defined in HL7 Application (level 7) Processing rules. The first component defines whether the message is part of a production, training, or debugging system. The second component is not currently used.

REF: For a list of valid values, please refer to Table 3‑28 in this manual, "."

| Value | Description |
|-----------|-----------------|
| P         | Production      |

<span id="_Ref104385765" class="anchor"></span>Table ‑. HL7 Table 0103: Processing ID

### MSH-12 Version ID (VID) 00012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<version ID (ID)\> ^ \<internationalization code (CE)\> ^ \<internal version ID (CE)\>

Definition: This field is matched by the receiving system to its own version to be sure the message will be interpreted correctly. Beginning with Version 2.3.1, it has two additional "internationalization" components, for use by HL7 international affiliates. The \<internationalization code\> is CE data type (using the ISO country codes where appropriate), which represents the HL7 affiliate. The \<internal version ID\> is used if the HL7 Affiliate has more than a single 'local' version associated with a single US version. The \<internal version ID\> has a CE data type, since the table values vary for each HL7 Affiliate.

| Value | Description | Date      |
|-----------|-----------------|---------------|
| 2.3       | Release 2.3     | March 1997    |
| 2.4       | Release 2.4     | November 2000 |

<span id="_Hlt478371358" class="anchor"></span>Table ‑. HL7 Table 0104: Version ID

### MSH-15 Accept Acknowledgement Type (ID) 00015

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field identifies the conditions under which accept Acknowledgements are required to be returned in response to this message. Required for enhanced Acknowledgement mode.

REF: For a list of valid values, please refer to Table 3‑30 in this manual, "."

### MSH-16 Application Acknowledgement Type (ID) 00016

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the conditions under which application Acknowledgements are to be returned in response to this message. Required for enhanced Acknowledgement mode.

The following table contains the possible values for and :

| Value | Description              |
|-----------|------------------------------|
| AL        | Always                       |
| NE        | Never                        |
| ER        | Error/reject conditions only |
| SU        | Successful completion only   |

<span id="_Ref104385793" class="anchor"></span>Table ‑. HL7 Table 0155: Accept/Application Acknowledgement Conditions

> **NOTE:** If and are omitted (or are both null), the original <u>Acknowledgement</u> mode rules are used.

### MSH-17 Country Code (ID) 00017

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the country of origin for the message. It will be used primarily to specify default elements, such as currency denominations. The values to be used are those of ISO 3166, which are reprinted here upon written approval from ANSI.[^1]. The ISO 3166 table has three separate forms of the country code: HL7 specifies that the 3-character (alphabetic) form be used for the country code.

REF: For the 3-character codes as defined by ISO 3166 table, please refer to Table 3‑31 in this manual, "."

| Value | Description |
|-----------|-----------------|
| USA       | UNITED STATES   |

<span id="_Ref104385827" class="anchor"></span>Table ‑. HL7 Table 0399: Country Code

## NTE: Notes and Comments Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NTE segment is defined here for inclusion in messages defined in other chapters. It is commonly used for sending notes and comments.

|         |         |        |         |        |         |          |                   |                                                      |
|---------|---------|--------|---------|--------|---------|----------|-------------------|------------------------------------------------------|
| SEQ | LEN | DT | OPT | RP | TBL | Item | Element Name  | VistA Description                                |
| 1       | 4       | SI     | O       |        |         | 00096    | Set ID - NTE      | Passed but not used by MPI.                          |
| 2       | 8       | ID     | O       |        |         | 00097    | Source of Comment | "P" sent always                                      |
| 3       | 65536   | FT     | O       | Y      |         | 00098    | Comment           | Phone number of person making request                |
| 4       | 250     | FT     |         |        |         |          | Reviewer comments | This is from Reviewer comments field in File \#984.9 |
| 5       |         | FT     |         |        |         |          |                   | Status of request                                    |
| 6       |         | FT     |         |        |         |          |                   | Request number                                       |
| 7       |         | FT     |         |        |         |          |                   | Station Number of requestor                          |
|         |         |        |         |        |         |          |                   |                                                      |
| 9       |         | FT     |         |        |         |          |                   | Current CMOR                                         |

<span id="_Toc131832319" class="anchor"></span>Table ‑. NTE: Notes and Comments, HL7 attributes

NTE Field Definitions

### NTE-1 Set ID–NTE (SI) 00096

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field may be used where multiple NTE segments are included in a message. Their numbering must be described in the application message definition.

### NTE-2 Source of Comment (ID) 00097

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is used when source of comment must be identified. This table may be extended locally during implementation.

REF: For a list of valid values, please refer to Table 3‑33 in this manual, "."

| Value | Description                                    |
|-----------|----------------------------------------------------|
| L         | Ancillary (filler) department is source of comment |
| P         | Order (placer) is source of comment                |
| O         | Other system is source of comment                  |

<span id="_Ref104385866" class="anchor"></span>Table ‑. HL7 Table 0105: Source of Comment

### NTE-3 Comment (FT) 00098

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the comment contained in the segment.

> **NOTE:** In the current HL7 version, this is a FT rather than a TX data type. Since there is no difference between a FT data type without any embedded formatting commands, and a TX data type, this change is compatible with the previous version.

## OBX: Observation/Result, HL7 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The OBX─Observation/Result segment is passed but not used by the MPI software. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment.

The OBX segment is used to transmit a single observation or observation fragment. It represents the smallest indivisible unit of a report. Its structure is summarized in Figure 7-5.

Its principal mission is to carry information about observations in report messages. But the OBX can also be part of an observation order (see Section 4.2, "Order Message Definitions"). In this case, the OBX carries clinical information needed by the filler to interpret the observation the filler makes. For example, an OBX is needed to report the inspired oxygen on an order for a blood oxygen to a blood gas lab, or to report the menstrual phase information, which should be included on an order for a pap smear to a cytology lab. Appendix 7A includes codes for identifying many of pieces of information needed by observation producing services to properly interpret a test result. OBX is also found in other HL7 messages that need to include patient clinical information.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP</th>
<th>TBL</th>
<th>Item</th>
<th><blockquote>
<p>Element Name</p>
</blockquote></th>
<th><blockquote>
<p><strong>VistA Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>10</td>
<td>SI</td>
<td>O</td>
<td></td>
<td></td>
<td>00569</td>
<td>Set ID - OBX</td>
<td><blockquote>
<p>Not used</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>0125</td>
<td>00570</td>
<td>Value Type</td>
<td><blockquote>
<p>CE - Security Log, SSN Verification, Active Prescriptions and older records, IPP, ROI, Self-Identified Gender, USEROPTION, DATE OF DEATH DATA, IIPT, PERSON TYPE, SSA_VERIFICATION_STATUS and AUTHORITY SCORE.</p>
<p>TS - Last Radiology Exam date/time and Last Lab Test date/time, NEW DATE OF DEATH STATUS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>590</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>00571</td>
<td>Observation Identifier</td>
<td><blockquote>
<p>38.1^SECURITY LOG (Passed but not used by MPI)</p>
<p>SSN VERIFICATION (sent by ESR to MPI and MPI to subscribers from ESR update based upon business rules)</p>
<p>ACTIVE PRESCRIPTIONS (only received at the MPI from the VistA sites, not sent out by the MPI)</p>
<p>LAST RADIOLOGY EXAM DATE/TIME (only received at the MPI from the VistA sites, not sent out by the MPI)</p>
<p>LAST LAB TEST DATE/TIME (only received at the MPI from the VistA sites, not sent out by the MPI)</p>
<p>OLDER RECORD (only received at the MPI from the VistA sites, not sent out by the MPI)</p>
<p>ROI SIGNED</p>
<p>IPP LEVEL (aka LEVEL OF ASSURANCE)</p>
<p>SELF ID GENDER</p>
<p>USEROPTION</p>
<p>DATE OF DEATH DATA</p>
<p>IIPT</p>
<p>PERSON TYPE</p>
<p>NEW DATE OF DEATH STATUS</p>
<p>SSA_VERIFICATION_STATUS</p>
<p>AUTHORITY SCORE (only sent for Primary View sync with PSIM.)</p>
<p>VBA/CORP (200CORP, 200BRLS) fields:</p>
</blockquote>
<ul>
<li><blockquote>
<p>VBA 101 UPDATE</p>
</blockquote></li>
<li><blockquote>
<p>VBA SHARE UPDATE</p>
</blockquote></li>
<li><blockquote>
<p>OPEN CLAIM INDICATOR</p>
</blockquote></li>
<li><blockquote>
<p>AUTHORIZED AWARD INDICATOR</p>
</blockquote></li>
<li><blockquote>
<p>COMPARE INDICATED MISMATCH POTENTIAL</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td>C</td>
<td></td>
<td></td>
<td>00572</td>
<td>Observation Sub-ID</td>
<td><blockquote>
<p>Not used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>65536<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>*</td>
<td>C</td>
<td>Y<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
<td></td>
<td>00573</td>
<td>Observation Value</td>
<td><blockquote>
<p>Sensitive = 1</p>
<p>Not Sensitive or No Value = 0</p>
<p>SSN VERIFICATION (see table below):</p>
<p>&lt;value&gt;^&lt;text&gt;^"L"</p>
<p>valid verification text:</p>
<p>value text</p>
<p>----------------------------------</p>
<p>Null</p>
<p>0 = New Record</p>
<p>1 = In-Process</p>
<p>2 = Invalid Per SSA</p>
<p>3 = Resend to SSA</p>
<p>4 = Verified</p>
<p>Active Prescriptions:</p>
<p>Y = for Yes active prescriptions</p>
<p>N = for No current active prescriptions</p>
<p>Older Records:</p>
<p>Y = for yes older records</p>
<p>ROI SIGNED = Y or N</p>
<p>IPP LEVEL (aka LEVEL OF ASSURANCE):</p>
<p>1 = NO CONFIDENCE</p>
<p>2 = CONFIDENT</p>
<p>3 = HIGH CONFIDENCE</p>
<p>4 = VERY HIGH CONFIDENCE</p>
<p>SELF ID GENDER can contain one of the following set of code values:</p>
</blockquote>
<ul>
<li><p>M = Male</p></li>
<li><p>F = Female</p></li>
<li><p>TM = Transmale/Transman/Female-to-Male</p></li>
<li><p>TF = Transfemale/Transwoman/Male-to-Female</p></li>
<li><p>O = Other</p></li>
<li><p>N = individual chooses not to answer</p></li>
</ul>
<p>USEROPTION can contain any Task Number value from Toolkit.</p>
<blockquote>
<p>DATE OF DEATH DATA:</p>
</blockquote>
<ul>
<li><blockquote>
<p>1 = INPATIENT AT VAMC;</p>
</blockquote></li>
<li><blockquote>
<p>2 = NON-VA MEDICAL FACILITY;</p>
</blockquote></li>
<li><blockquote>
<p>3 = DEATH CERTIFICATE ON FILE;</p>
</blockquote></li>
<li><blockquote>
<p>4 = VBA;</p>
</blockquote></li>
<li><blockquote>
<p>5 = VA INSURANCE;</p>
</blockquote></li>
<li><blockquote>
<p>6 = SSA;</p>
</blockquote></li>
<li><blockquote>
<p>7 = NCA;</p>
</blockquote></li>
<li><blockquote>
<p>8 = NEXT OF KIN/FAMILY/FRIEND;</p>
</blockquote></li>
<li><blockquote>
<p>9 = OTHER;</p>
</blockquote></li>
</ul>
<blockquote>
<p>IIPT - Identity Interoperability Person Type (IIPT) – set of codes:</p>
</blockquote>
<ul>
<li><blockquote>
<p>V1 = Veteran (per VA) </p>
</blockquote></li>
<li><blockquote>
<p>V2 = VA Beneficiary </p>
</blockquote></li>
<li><blockquote>
<p>D6 = VA Sourced person* </p>
</blockquote></li>
<li><blockquote>
<p>D7 = Prior DoD Person </p>
</blockquote></li>
<li><blockquote>
<p>D8 = Non DoD Person </p>
</blockquote></li>
<li><blockquote>
<p>D1 = Military (current) </p>
</blockquote></li>
<li><blockquote>
<p>D2 = Retiree </p>
</blockquote></li>
<li><blockquote>
<p>D3 = DOD Family member </p>
</blockquote></li>
<li><blockquote>
<p>D4 = DOD civilian</p>
</blockquote></li>
<li><blockquote>
<p>D5 = DOD Associate for ID card or clearance</p>
</blockquote></li>
</ul>
<p>Person Type:</p>
<ul>
<li><blockquote>
<p>VET Veteran</p>
</blockquote></li>
<li><blockquote>
<p>PAT Patient</p>
</blockquote></li>
<li><blockquote>
<p>HUM Humanitarian</p>
</blockquote></li>
<li><blockquote>
<p>EMP Employee</p>
</blockquote></li>
<li><blockquote>
<p>VOL Volunteer</p>
</blockquote></li>
<li><blockquote>
<p>STU Student</p>
</blockquote></li>
<li><blockquote>
<p>TRN Trainee</p>
</blockquote></li>
<li><blockquote>
<p>CON Contractor</p>
</blockquote></li>
<li><blockquote>
<p>USR User</p>
</blockquote></li>
<li><blockquote>
<p>BEN Beneficiary</p>
</blockquote></li>
<li><blockquote>
<p>DEP Dependent</p>
</blockquote></li>
<li><blockquote>
<p>REP Representative of Veteran</p>
</blockquote></li>
<li><blockquote>
<p>COL Collateral Patient</p>
</blockquote></li>
<li><blockquote>
<p>LCG Legal Relationship: Care Giver</p>
</blockquote></li>
<li><blockquote>
<p>LFD Legal Relationship: Fiduciary</p>
</blockquote></li>
<li><blockquote>
<p>LPA Legal Relationship: POA</p>
</blockquote></li>
<li><blockquote>
<p>LLG Legal Relationship: Legal Guardian</p>
</blockquote></li>
</ul>
<p>New Date of Death Status:</p>
<ul>
<li><blockquote>
<p>Date of Death (HL7 Format)</p>
</blockquote></li>
</ul>
<blockquote>
<p>SSA Verification Status – set of codes:</p>
</blockquote>
<ul>
<li><blockquote>
<p>1 = SSN not in SSA file</p>
</blockquote></li>
<li><blockquote>
<p>2 = Name and DOB match, sex code does not. </p>
</blockquote></li>
<li><blockquote>
<p>3 = Name and sex code match, DOB does not </p>
</blockquote></li>
<li><blockquote>
<p>4 = Name matches, sex code and DOB do not. </p>
</blockquote></li>
<li><blockquote>
<p>5 = Name does not match, DOB and sex code not checked. </p>
</blockquote></li>
<li><blockquote>
<p>V = SSN is verified on name, DOB, and sex code</p>
</blockquote></li>
</ul>
<p>Authority Scores, each is separated by a dash (-). They are added in order as listed below.</p>
<ul>
<li><p>SURNAME PRIMARY VIEW SCORE</p></li>
<li><p>FIRST NAME PRIMARY VIEW SCORE</p></li>
<li><p>MIDDLE NAME PRIMARY VIEW SCORE</p></li>
<li><p>PREFIX PRIMARY VIEW SCORE</p></li>
<li><p>SUFFIX PRIMARY VIEW SCORE</p></li>
<li><p>DOB PRIMARY VIEW SCORE</p></li>
<li><p>GENDER PRIMARY VIEW SCORE</p></li>
<li><p>SSN PRIMARY VIEW SCORE</p></li>
<li><p>MMN PRIMARY VIEW SCORE</p></li>
<li><p>MULT BIRTH PRIMARY VIEW SCORE</p></li>
<li><p>POB CITY PRIMARY VIEW SCORE</p></li>
<li><p>POB STATE PRIMARY VIEW SCORE</p></li>
<li><p>DOD PRIMARY VIEW SCORE</p></li>
</ul>
<blockquote>
<p>VBA/CORP (200CORP, 200BRLS) fields. Value = Y or N (Yes or No)</p>
</blockquote>
<ul>
<li><blockquote>
<p>VBA 101 UPDATE</p>
</blockquote></li>
</ul>
<blockquote>
<p>Y = Manual Change of Identity Traits w/Document/evidence coming from VBA Central Office (Station # 101).</p>
</blockquote>
<ul>
<li><blockquote>
<p>VBA SHARE UPDATE</p>
</blockquote></li>
</ul>
<blockquote>
<p>Y = Manual Change of Identity Traits with documentation/evidence.</p>
</blockquote>
<ul>
<li><blockquote>
<p>OPEN CLAIM INDICATOR</p>
</blockquote></li>
</ul>
<blockquote>
<p>Y = Any open claim (exclude 800s-system generated reminder work items) Corp DB and BDN. (24 hour window of update).</p>
</blockquote>
<ul>
<li><blockquote>
<p>AUTHORIZED AWARD INDICATOR</p>
</blockquote></li>
</ul>
<blockquote>
<p>Y = Running award, benefits being paid from Corp DB and BDN.</p>
</blockquote>
<ul>
<li><blockquote>
<p>COMPARE INDICATED MISMATCH POTENTIAL</p>
</blockquote></li>
</ul>
<blockquote>
<p>Y = Indicates the MVI update ONLY the Correlation, log the Milestone, and log the Potential Mismatch Task.</p>
</blockquote>
<p>Security Level</p>
<ul>
<li><p>0 = Non-Sensitive</p></li>
<li><p>1 = Sensitive</p></li>
</ul></td>
</tr>
<tr class="even">
<td>6</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00574</td>
<td><blockquote>
<p>Units</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00575</td>
<td><blockquote>
<p>References Range</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>5</td>
<td>ID</td>
<td>O</td>
<td>Y/5</td>
<td>0078</td>
<td>00576</td>
<td><blockquote>
<p>Abnormal Flags</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>5</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00577</td>
<td><blockquote>
<p>Probability</p>
</blockquote></td>
<td><blockquote>
<p>not used.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td>Y</td>
<td>0080</td>
<td>00578</td>
<td><blockquote>
<p>Nature of Abnormal Test</p>
</blockquote></td>
<td><blockquote>
<p>not used.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0085</td>
<td>00579</td>
<td><blockquote>
<p>Observation Result Status</p>
</blockquote></td>
<td><blockquote>
<p>F=Results entered, Not verified (Passed but not used by MPI)</p>
<p>R= Results entered, Not verified</p>
</blockquote>
<p>New Date of Death Status:</p>
<blockquote>
<p>P = Pending</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00580</td>
<td><blockquote>
<p>Date Last Observation Normal Value</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td>20</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00581</td>
<td><blockquote>
<p>User Defined Access Checks</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00582</td>
<td><blockquote>
<p>Date/Time of the Observation</p>
</blockquote></td>
<td><blockquote>
<p>Date if found in VistA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00583</td>
<td><blockquote>
<p>Producer's ID</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td>80</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>00584</td>
<td><blockquote>
<p>Responsible Observer</p>
</blockquote></td>
<td><blockquote>
<p>Name if found in VistA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00936</td>
<td><blockquote>
<p>Observation Method</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td>22</td>
<td>EL</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>01479</td>
<td><blockquote>
<p>Equipment Instance Identifier</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>01480</td>
<td><blockquote>
<p>Date/Time of the Analysis</p>
</blockquote></td>
<td><blockquote>
<p>not used</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>The length of the observation value field is variable, depending upon value type. See <em>OBX-2-value type</em>.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>May repeat for multipart, single answer results with appropriate data types, e.g., CE, TX, and FT data types.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<span id="_Toc131832321" class="anchor"></span>Table ‑. OBX: Observation/Result, HL7 attributes

## PD1: Patient Additional Demographic Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** PD1-3 (Patient Primary Facility) is the only field used by the MPI software in the PD1─Patient Additional Demographic segment. All other fields in this segment are passed but not used by the MPI. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment.

The patient additional demographic segment contains demographic information that is likely to change about the patient.

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP#</strong></th>
<th><strong>TBL</strong></th>
<th><strong>Item</strong></th>
<th><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VistA Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td>Y</td>
<td>0223</td>
<td>00755</td>
<td><blockquote>
<p>Living Dependency</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0220</td>
<td>00742</td>
<td><blockquote>
<p>Living Arrangement</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>XON</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00756</td>
<td><blockquote>
<p>Patient Primary Facility</p>
</blockquote></td>
<td>Coordinating Master of Record</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>XCN</td>
<td>B</td>
<td>Y</td>
<td></td>
<td>00757</td>
<td><blockquote>
<p>Patient Primary Care Provider Name &amp; ID No.</p>
</blockquote></td>
<td><blockquote>
<p>Passed but not used by MPI.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0231</td>
<td>00745</td>
<td><blockquote>
<p>Student Indicator</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0295</td>
<td>00753</td>
<td><blockquote>
<p>Handicap</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0315</td>
<td>00759</td>
<td><blockquote>
<p>Living Will Code</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>8</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0316</td>
<td>00760</td>
<td><blockquote>
<p>Organ Donor Code</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00761</td>
<td><blockquote>
<p>Separate Bill</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CX</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00762</td>
<td><blockquote>
<p>Duplicate Patient</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0215</td>
<td>00743</td>
<td><blockquote>
<p>Publicity Code</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00744</td>
<td><blockquote>
<p>Protection Indicator</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>01566</td>
<td><blockquote>
<p>Protection Indicator Effective Date</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>14</td>
<td>250</td>
<td>XON</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>01567</td>
<td><blockquote>
<p>Place of Worship</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0435</td>
<td>01548</td>
<td><blockquote>
<p>Advance Directive Code</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0441</td>
<td>01569</td>
<td><blockquote>
<p>Immunization Registry Status</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>01570</td>
<td><blockquote>
<p>Immunization Registry Status Effective Date</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>18</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>01571</td>
<td><blockquote>
<p>Publicity Code Effective Date</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>5</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0140</td>
<td>01572</td>
<td><blockquote>
<p>Military Branch</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="even">
<td>20</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0141</td>
<td>00486</td>
<td><blockquote>
<p>Military Rank/Grade</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>3</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0142</td>
<td>00487</td>
<td><blockquote>
<p>Military Status</p>
</blockquote></td>
<td>Passed but not used by MPI.</td>
</tr>
</tbody>
</table>

<span id="_Toc131832322" class="anchor"></span>Table ‑. PD1: Patient Additional Demographic, HL7 attributes

PD1 Field Definition

### PD1-3 Patient Primary Facility (XON) 00756

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<organization name (ST)\> ^ \<organization name type code (ID)\> ^ \<ID number (ID)\> ^ \<check digit (NM)\> ^ \< check digit scheme (ID)\> ^ \<assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\>

Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Subcomponents of assigning facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Definition: This field contains the name and identifier that specifies the "primary care" healthcare facility or Coordinating Master of Record (CMOR) site selected by the software or requests from the facilities. In the future this will more than likely transition to the OneVHA demographic database (EDB), OneVA demographic database or some central patient demographic database.

### Yes/No Indicator Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actual interpretation of Yes/No is context sensitive.

| Value | Description |
|-------|-----------------|
| Y     | Yes             |
| N     | No              |

<span id="_Ref133586077" class="anchor"></span>Table ‑. HL7 Table 0136: Yes/no indicator

## PID: Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying and demographic information that, for the most part, is not likely to change frequently.

From V2.4 onwards, the demographics of animals can also be sent in the PID segment (see PID-35 to PID-38).

The assigning authority, the fourth component of the patient identifiers, is a HD data type that is uniquely associated with the assigning authority that originally assigned the number. A given institution, or group of intercommunicating institutions, should establish a list of assigning authorities that may be potential assignors of patient identification (and other important identification) numbers. The list will be one of the institution's master dictionary lists. Since third parties (other than the assignors of patient identification numbers) may send or receive HL7 messages containing patient identification numbers. This field is required in HL7 implementations that have more than a single Patient Administration application assigning such numbers. The assigning authority and identifier type codes are strongly recommended for all CX data types.

With HL7 V2.3, the nomenclature for the fourth component of the patient identifiers was changed from "assigning facility ID" to "assigning authority." While the identifier may be unique to a given healthcare facility (for example, a medical record assigned by facility A in Hospital XYZ), the identifier might also be assigned at a system level (for example a corporate person index or enterprise number spanning multiple facilities) or by a government entity, for example a nationally assigned unique individual identifier. While a facility is usually an assigning authority, not all assigning authorities are facilities. Therefore, the fourth component is referred to as an assigning authority, but retains backward compatibility using the construct of the HD data type.

REF: For more information on the HD data type, please refer to Section 2.9 of HL7 Standard Version 2.4 documentation.

Additionally, CX data types support the use of assigning facility (HD) as the sixth component.

Example: Message Patient Identification PID Segment

<span id="_Ref424819864" class="anchor"></span>MSH^~\|\\^RG ADT^984~DAYTSHR.FO-REDACTED.GOV~DNS^RG ADT^200M~TLMPI.FO-REDACTED.GOV~DNS^20070625100545-0400^^ADT~A08^98459402631^T^2.4^^^AL^AL^USA

EVN^^^^^35198~MVIPATIENT~PATIENT1\~\~\~\~\~~USVHA&&0363~L\~\~~NI~VA FACILITY ID&984&L^^984

PID^1^1010005729V870655^1010005729V870655\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666010255\~\~~USSSA&&0363~SS~VA FACILITY ID&984&L\|552151092\~\~~USVHA&&0363~PI~VA FACILITY ID&984&L\|666010256\~\~~USSSA&&0363~SS~VA FACILITY ID&984&L\~~20070625\|1010002493V683214\~\~~USVHA&&0363~NI~VA FACILITY ID&984&L\~~20070625^^MVISQA~PIDTSTB MID~SFIX\~\~\~~L\|PREFERRED NAME\~\~\~\~\~~N\|ALIASLNA~ALIASFNA\~\~\~\~~A^MOMSMITH\~\~\~\~\~~M^19800202^M^^""^222 PERM TST ADDRESS~TAMPA, FL~""~""~""~""~VAB1~""~""\|\~~TAMPA~FL\~\~~N\|333 CONFIDENTIAL ADDRESS~""~SAINT PETERSBURG~FL~33716~""~VACAA~""~""\~\~~20070625&20080625^""^111-1111~PRN~PH\|222-2222~WPN~PH\|555-5555~ORN~CP\|666-6666~BPN~BP\|~NET~INTERNET~ONE.SQA@MPI.COM^222-2222^555)555-5555~VACPN~PH^""^""^^666010255^^^""^TAMPA FL^N^^^^^20150512^Y^^^

PV1^1^O^""^^^^^^^^^^^^^^^ACTIVE DUTY^^^^^^^^^^^^^^^^^^^^^^^^^^20070625^^^^^^1535241

ZPD^1^^^^^^^^^^^^^^^^""^^^^""^^^^^^^^^^^^^""

ZSP^1^0^""^""^""^""^""^""^^""

ZEL^1^""^""^""^""^""^""^1^ACTIVE DUTY^""^""^""^""^""^""^""^""^""^""^""^""^""

ZCT^1^1^""^""^""^""^""^""^""^1^1^""^""^""^""^""^""

ZFF^2^.01;.02;.03;.092;.093;.09;.2403;.301;1901;391;.111;.112;.131;.132;

Figure ‑. Sample Message Patient Identification PID Segment

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP</th>
<th>TBL</th>
<th>Item</th>
<th>Element Name</th>
<th><strong>VistA Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>O</td>
<td></td>
<td></td>
<td>00104</td>
<td>Set ID - PID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>CX</td>
<td>B</td>
<td></td>
<td></td>
<td>00105</td>
<td>Patient ID</td>
<td>ICN, including V checksum for backwards compatibility</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CX</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>00106</td>
<td>Patient Identifier List</td>
<td><p>Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, all alias SSNs which will correspond directly to the alias name in the name field (pid-5).</p>
<p>The ID State for the primary ICN will be determined based upon the following: ID State for a deactivated ICN will have the expiration date only set; ID State for a temporary ICN will have neither the expiration nor effective date set; ID State for a permanent ICN will have the effective date only set.</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>CX</td>
<td>B</td>
<td>Y</td>
<td></td>
<td>00107</td>
<td>Alternate Patient ID - PID</td>
<td>Active Veteran’s Health Identity Card (VHIC) numbers</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>XPN</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>00108</td>
<td>Patient Name</td>
<td>Patient Name and all Alias entries</td>
</tr>
<tr class="even">
<td>6</td>
<td>250</td>
<td>XPN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00109</td>
<td>Mother's Maiden Name</td>
<td>Mother's Maiden Name</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00110</td>
<td>Date/Time of Birth</td>
<td>Date of Birth</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td></td>
<td>00111</td>
<td>Administrative Sex</td>
<td>Sex</td>
</tr>
<tr class="odd">
<td>9</td>
<td>250</td>
<td>XPN</td>
<td>B</td>
<td>Y</td>
<td></td>
<td>00112</td>
<td>Patient Alias</td>
<td>Not used. Alias is passed in PID-5</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00113</td>
<td>Race</td>
<td>Race Information</td>
</tr>
<tr class="odd">
<td>11</td>
<td>250</td>
<td>XAD</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00114</td>
<td>Patient Address</td>
<td><p>Permanent:</p>
<ul>
<li><p>Street Address [Line 1]</p></li>
<li><p>Street Address [Line 2]</p></li>
<li><p>Street Address [Line 3]</p></li>
<li><p>City</p></li>
<li><p>State</p></li>
<li><p>ZIP+4</p></li>
<li><p>County Code</p></li>
<li><p>Country Code</p></li>
<li><p>Provence</p></li>
<li><p>Postal Code [incorporating foreign address]</p></li>
<li><p>Bad Address Indicator (only for Permanent address)</p></li>
</ul>
<p>Place of Birth:</p>
<ul>
<li><p>Place of Birth [City]</p></li>
<li><p>Place of Birth [State]</p></li>
</ul>
<p>Confidential Address:</p>
<ul>
<li><p>Street Address line 1</p></li>
<li><p>Street Address line 2</p></li>
<li><p>Street Address line 3</p></li>
<li><p>City</p></li>
<li><p>State</p></li>
<li><p>Zip+4</p></li>
<li><p>County Code</p></li>
<li><p>Confidential Address Category</p></li>
<li><p>Start And End Date</p></li>
<li><p>Country Code</p></li>
<li><p>Provender</p></li>
<li><p>Post Code (incorporating confidential foreign address)</p></li>
</ul>
<p><strong>NOTE:</strong> Foreign address information (province, postal code, and country) may be included in the PID segment in existing fields.</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>4</td>
<td>IS</td>
<td>B</td>
<td></td>
<td>0289</td>
<td>00115</td>
<td>County Code</td>
<td>County</td>
</tr>
<tr class="odd">
<td>13</td>
<td>250</td>
<td>XTN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00116</td>
<td>Phone Number - Home</td>
<td><ul>
<li><blockquote>
<p>Phone Number [Residence]</p>
</blockquote></li>
<li><blockquote>
<p>Work Number</p>
</blockquote></li>
<li><blockquote>
<p>Cell Phone</p>
</blockquote></li>
<li><blockquote>
<p>Pager Number</p>
</blockquote></li>
<li><blockquote>
<p>E-Mail Address</p>
</blockquote></li>
<li><blockquote>
<p>Confidential Phone Number</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>14</td>
<td>250</td>
<td>XTN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00117</td>
<td>Phone Number - Business</td>
<td>Phone Number [Work] only for backwards compatibility should use PID-13</td>
</tr>
<tr class="odd">
<td>15</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0296</td>
<td>00118</td>
<td>Primary Language</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>16</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00119</td>
<td>Marital Status</td>
<td>Marital Status</td>
</tr>
<tr class="odd">
<td>17</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00120</td>
<td>Religion</td>
<td>Religious Preference</td>
</tr>
<tr class="even">
<td>18</td>
<td>250</td>
<td>CX</td>
<td>O</td>
<td></td>
<td></td>
<td>00121</td>
<td>Patient Account Number</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>16</td>
<td>ST</td>
<td>B</td>
<td></td>
<td></td>
<td>00122</td>
<td>SSN Number - Patient</td>
<td>SSN – for backwards compatibility</td>
</tr>
<tr class="even">
<td>20</td>
<td>25</td>
<td>DLN</td>
<td>O</td>
<td></td>
<td></td>
<td>00123</td>
<td>Driver's License Number - Patient</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>250</td>
<td>CX</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00124</td>
<td>Mother's Identifier</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>22</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0189</td>
<td>00125</td>
<td>Ethnic Group</td>
<td>Ethnicity Information</td>
</tr>
<tr class="odd">
<td>23</td>
<td>250</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00126</td>
<td>Birth Place</td>
<td>Place of birth city and place of birth state – backwards compatibility</td>
</tr>
<tr class="even">
<td>24</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00127</td>
<td>Multiple Birth Indicator</td>
<td>Multiple Birth Indicator [Y for multiple birth]</td>
</tr>
<tr class="odd">
<td>25</td>
<td>2</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00128</td>
<td>Birth Order</td>
<td>Populated if the Multiple Birth Indicator (field #PID-24) = Yes <em><u>and</u></em> if the Birth Order is sent by DoD.</td>
</tr>
<tr class="even">
<td>26</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0171</td>
<td>00129</td>
<td>Citizenship</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0172</td>
<td>00130</td>
<td>Veterans Military Status</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>28</td>
<td>250</td>
<td>CE</td>
<td>B</td>
<td></td>
<td>0212</td>
<td>00739</td>
<td>Nationality</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>29</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00740</td>
<td>Patient Death Date and Time</td>
<td>Date of Death</td>
</tr>
<tr class="even">
<td>30</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00741</td>
<td>Patient Death Indicator</td>
<td>Only sent from the MPI in A31 message to PSIM</td>
</tr>
<tr class="odd">
<td>31</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>01535</td>
<td>Identity Unknown Indicator</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>32</td>
<td>20</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0445</td>
<td>01536</td>
<td>Identity Reliability Code</td>
<td>Only sent from the MPI in A31 message. Used by PSIM.</td>
</tr>
<tr class="odd">
<td>33</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>01537</td>
<td>Last Update Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>34</td>
<td>40</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>01538</td>
<td>Last Update Facility</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>35</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td>0446</td>
<td>01539</td>
<td>Species Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>36</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td>0447</td>
<td>01540</td>
<td>Breed Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>37</td>
<td>80</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>01541</td>
<td>Strain</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>38</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>2</td>
<td>0429</td>
<td>01542</td>
<td>Production Class Code</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Hlt479197644" class="anchor"></span>Table ‑. PID: Patient Identification, HL7 attributes

PID Field Definitions

### PID-1 Set ID ‑ PID (SI) 00104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the number that identifies this transaction. For the first occurrence of the segment, the sequence number shall be one, for the second occurrence, the sequence number shall be two, etc.

### PID-2 Patient ID (CX) 00105

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is being populated with the VHA MVI integration control number \[ICN\], including V and the ICN Checksum for backwards compatibility ONLY. ICN should be retrieved from PID-3.

### PID-3 Patient identifier list (CX) 00106

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<ID (ST)\> ^ \<check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \< assigning authority (HD)\> ^ \<identifier type code (ID)\> ^ \< assigning facility (HD) ^ \<effective date (DT)\> ^ \<expiration date (DT)\>

Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Definition: This field contains the list of identifiers (one or more) used by the healthcare facility to uniquely identify a patient (e.g., VistA internal id \[DFN\], Claim number, VHA MVI integration control number \[ICN\], social security number, unique individual identifier, etc.). Refer to *HL7 Table 0061 - Check digit scheme* for valid values. The arbitrary term of "internal ID" has been removed from the name of this field for clarity. Refer also to [HL7 Table 0203 - Identifier type](#HL70203) and *User-defined Table 0363 - Assigning authority* for valid values. The currently supported values are listed below.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td><span id="HL70203" class="anchor"></span><strong>Identifier</strong></td>
<td><strong>Assigning Authority</strong></td>
<td><strong>Identifier type</strong></td>
<td><p><strong>Assigning Location</strong></p>
<p><strong>unique station# id</strong></p></td>
<td><strong>Expiration date</strong></td>
<td><strong>Effective date</strong></td>
</tr>
<tr class="even">
<td>National ICN <strong></strong></td>
<td>USVHA</td>
<td>NI</td>
<td>200M</td>
<td><p>If populated, the ICN ID State is considered Deactivated</p>
<p>If both Expiration Date and Effective date are not populated the ICN ID State is Temporary</p></td>
<td><p>If populated, the ID State of the ICN is Permanent (see note above)</p>
<p>If both Expiration Date and Effective date are not populated the ICN ID State is Temporary</p></td>
</tr>
<tr class="odd">
<td>Local ICN</td>
<td>USVHA</td>
<td>NI</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SSN</td>
<td>USSSA</td>
<td>SS</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alias SSN</td>
<td>USSSA</td>
<td>SS</td>
<td>Unique station # id</td>
<td>Date/Time of segment being built</td>
<td></td>
</tr>
<tr class="even">
<td>VistA id (DFN)</td>
<td>USVHA</td>
<td>PI</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CLAIM#</td>
<td>USVBA</td>
<td>PN</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Deprecated National ICN (resolved duplicate pair)</td>
<td>USVHA</td>
<td>NI</td>
<td>200M</td>
<td><p>Replacement date/time</p>
<p>Also, indicates that the ID State is Deactivated</p></td>
<td></td>
</tr>
<tr class="odd">
<td>Deprecated local ICN</td>
<td>USVHA</td>
<td>NI</td>
<td>unique station# id</td>
<td>Replacement date/time</td>
<td></td>
</tr>
<tr class="even">
<td>DOD EDIPN</td>
<td>USDOD</td>
<td>NI</td>
<td>200DOD</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>TIN</td>
<td>USDOD</td>
<td>TIN</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FIN</td>
<td>USDOD</td>
<td>FIN</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc3901249" class="anchor"></span>Table ‑. HL7 Table 0203: Identifier type

\*\* NOTE: If both the Expiration and Effective dates are null then this indicates that the ICN has a temporary ID State.

### PID-4 Alternate patient ID - PID (CX) 00107

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Active* Veteran’s Health Identification Card (VHIC) Numbers Added to PID-4 Segment

As of Patch DG\*5.3\*874 Veteran’s Health Identity Card (VHIC) number was added to the PID segment (PID-4). Format:

> \[VHIC Card \#\]\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L

Example of active VHIC number in PID-4 repeated twice for interoperability between DoD and VA because this patient has two active VHIC numbers:

> PID(1)="PID^1^1000003594V373737^1000003594V373737\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|000321234\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|""""\~\~~USDOD&&0363~TIN~VA FACILITY ID&500&L\|""""\~\~~USDOD&&0363~FIN~VA FACILITY ID&500&L\|100004184\~\~~USVHA&&0363~PI~VA FA"

> PID(2)="CILITY ID&500&L^999\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L\|999999\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L^MVIPATIENT~PTNAME3\~\~\~\~~L^MVIMOTHERSMAIDEN\~\~\~\~\~~M^99999999^M^^2106-3-SLF\~~0005~2106-3\~~CDC^""""~""""~""""~""""~""""~""""~P~""""~""""\|\~~Patient Address ANY TOWN~CA\~\~~N^""""^""""^""""^^S^29^^000321234"

> PID(3)="^^^2186-5-SLF\~~0189~2186-5\~~CDC^Place of Birth Address ANY TOWN CA^^^^^^""""^^"

> **NOTE:** Only active VHIC numbers are included.

### PID-5 Patient name (XPN) 00108

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: In Version 2.3, replaces the PN data type. \<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

Definition: This field contains the names of the patient, the primary or legal name of the patient is reported first. Therefore, the name type code in this field should be "L - Legal". Refer to [<u>HL7 Table 0200 - Name type</u>](#HL70200) for valid values. Repetition of this field is allowed for representing the same name in different character sets. Note that "last name prefix" is synonymous to "own family name prefix" of previous versions of HL7, as is "second and further given names or initials thereof" to "middle initial or name". Multiple given names and/or initials are separated by spaces.

| Value | Description               |
|-------|---------------------------|
| L     | Legal Name                |
| M     | Maiden Name               |
| A     | Alias Name                |
| N     | Nickname (Preferred Name) |

<span id="_Toc131832325" class="anchor"></span>Table ‑. HL7 Table 0200: Name type

### PID-6 Mother's maiden name (XPN) 00109

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: In Version 2.3, replaces the PN data type. \<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<name type code (ID) \> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \<name assembly order (ID)\>

Subcomponents of family name: \<family name (ST)\> & \<own family name prefix (ST)\> & \<own family name (ST)\> & \<family name prefix from partner/spouse (ST)\> & \<family name from partner/spouse (ST)\>

Definition: This field contains the family name under which the mother was born (i.e., before marriage). It is used to distinguish between patients with the same last name.

### PID-7 Date/time of birth (TS) 00110

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the patient's date and time of birth.

### PID-8 Administrative sex (IS) 00111

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the patient's sex. Refer to [<u>User-defined</u> <u>Table 0001 -</u> <u>Administrative sex</u>](#HL70001) for suggested values.

| Value | Description |
|-------|-------------|
| F     | Female      |
| M     | Male        |

<span id="_Toc131832326" class="anchor"></span>Table ‑. User-defined Table 0001: Administrative sex

### PID-9 Patient alias (XPN) 00112

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used. Alias should be retrieved from PID-5.

### PID-10 Race (CE) 00113

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field refers to the patient's race. Refer to for suggested values. The second triplet of the CE data type for race (alternate identifier, alternate text, and name of alternate coding system) is reserved for governmentally assigned codes.

> **NOTE:** Table values contain a pre-calculated Mod 10 check digits, separated by a dash.

| Value | Description                           |
|-----------|-------------------------------------------|
| 1002-5    | American Indian or Alaska Native          |
| 2028-9    | Asian                                     |
| 2054-5    | Black or African American                 |
| 2076-8    | Native Hawaiian or Other Pacific Islander |
| 2106-3    | White                                     |
| 2131-1    | Other Race                                |

<span id="_Ref133588291" class="anchor"></span>Table ‑. User-defined Table 0005: Race

### PID-11 Patient address (XAD) 00114

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: In Version 2.3 and later, replaces the AD data type. \<street address (ST)\> ^ \<other designation (ST)\> ^ \<city (ST)\> ^ \<state or province (ST)\> ^ \<zip or postal code (ST)\> ^ \<country (ID)\> ^ \< address type (ID)\> ^ \<other geographic designation (ST)\> ^ \<county/parish code (IS)\> ^ \<census tract (IS)\> ^ \<address representation code (ID)\> ^ \<address validity range (DR)\>

Subcomponents of street address: \<street address (ST)\> & \<street name (ST)\> & \<dwelling number (ST)\>

Definition: This field contains the mailing address of the patient. Address type codes are defined in *HL7 Table 0190 - Address type*. Multiple addresses for the same person may be sent in the following sequence: The primary mailing address must be sent first in the sequence (for backward compatibility); if the mailing address is not sent, then a repeat delimiter must be sent in the first sequence.

| Value | Description                                          |
|-------|------------------------------------------------------|
| N     | Birth (nee) (birth address, not otherwise specified) |
| P     | Permanent                                            |
| VAB1  | VA - Bad Address, Undeliverable                      |
| VAB2  | VA Bad Address, Homeless                             |
| VAB3  | VA Bad Address, Other                                |
| VAB4  | VA Bad Address, Address Not Found                    |
| VACAA | VA - Confidential Address Appointment/Scheduling     |
| VACAC | VA - Confidential Address Copayments/Veteran Billing |
| VACAE | VA - Confidential Address Eligibility/Enrollment     |
| VACAM | VA - Confidential Address Medical Records            |
| VACAO | VA - Confidential Address All Others                 |

<span id="_Toc131832328" class="anchor"></span>Table ‑. HL7 Table 0190: Address type

### PID-12 County code (IS) 00115

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: *This field has been retained for backward compatibility.* This field contains the patient's county code. The county can now be supported in the county/parish code component of the XAD data type (*PID-11 - Patient Address*). Refer to *User-defined Table 0289 - County/parish* for suggested values

### PID-13 Phone number - home (XTN) 00116

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] ^ \<telecommunication use code (ID)\> ^ \<telecommunication equipment type (ID)\> ^ \<e-mail address (ST)\> ^ \<country code (NM)\> ^ \<area/city code (NM)\> ^ \<phone number (NM)\> ^ \<extension (NM)\> ^ \<any text (ST)\>

Definition: This field contains the patient's personal phone numbers. All personal phone numbers for the patient are sent in the following sequence. The first sequence is considered the primary number (for backward compatibility). If the primary number is not sent, then a repeat delimiter is sent in the first sequence. Refer to *HL7 Table 0201 - Telecommunication use code* and *HL7 Table 0202 - Telecommunication equipment type* for valid values.

| Value | Description                       |
|-------|-----------------------------------|
| BPN   | Beeper Number                     |
| EMR   | Emergency Number (not used)       |
| NET   | Network (email) Address           |
| ORN   | Other Residence Number (not used) |
| PRN   | Primary Residence Number          |
| VHN   | Vacation Home Number (not used)   |
| WPN   | Work Number                       |
| VACPN | Confidential Phone Number         |

<span id="_Toc3901254" class="anchor"></span>Table ‑. HL7 Table 0201 Telecommunication Use Code

| Value    | Description                                                     |
|----------|-----------------------------------------------------------------|
| BP       | Beeper                                                          |
| CP       | Cellular Phone                                                  |
| Internet | Internet Address: Use Only if Telecommunication Use Code is NET |
| PH       | Telephone                                                       |

<span id="_Toc131832330" class="anchor"></span>Table ‑. HL7 Table 0202 Telecommunication Equipment Type

### PID-14 Phone number ‑ business (XTN) 00117

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \[NNN\] \[(999)\]999-9999 \[X99999\] \[B99999\] \[C any text\] ^ \<telecommunication use code (ID)\> ^ \<telecommunication equipment type (ID)\> ^ \<e-mail address (ST)\> ^ \<country code (NM)\> ^ \<area/city code (NM)\> ^ \<phone number (NM)\> ^ \<extension (NM)\> ^ \<any text (ST)\>

Definition: This field contains the patient's business telephone numbers. All business numbers for the patient are sent in the following sequence. The first sequence is considered the patient's primary business phone number (for backward compatibility). If the primary business phone number is not sent, then a repeat delimiter must be sent in the first sequence. Refer to *HL7 Table 0201 - Telecommunication use code* and *HL7 Table 0202 - Telecommunication equipment type* for valid values.

### PID-15 Primary language (CE) 00118

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-16 Marital status (CE) 00119

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field contains the patient's marital (civil) status. Refer to [*User-defined Table 0002 - Marital status*](#HL70002) for suggested values.

|           |                 |
|-----------|-----------------|
| Value | Description |
| A         | Separated       |
| D         | Divorced        |
| M         | Married         |
| S         | Never Married   |
| W         | Widowed         |
| U         | Unknown         |

<span id="_Toc131832331" class="anchor"></span>Table ‑. User-defined Table 0002: Marital status

### PID-17 Religion (CE) 00120

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field contains the patient's religion, for example, Baptist, Catholic, Methodist, etc. Refer to for suggested values.

| Value | Description              |
|-----------|------------------------------|
| 0         | ROMAN CATHOLIC CHURCH        |
| 1         | JUDAISM                      |
| 2         | EASTERN ORTHODOX             |
| 3         | BAPTIST                      |
| 4         | METHODIST                    |
| 5         | LUTHERAN                     |
| 6         | PRESBYTERIAN                 |
| 7         | UNITED CHURCH OF CHRIST      |
| 8         | EPISCOPALIAN                 |
| 9         | ADVENTIST                    |
| 10        | ASSEMBLY OF GOD              |
| 11        | BRETHREN                     |
| 12        | CHRISTIAN SCIENTIST          |
| 13        | CHURCH OF CHRIST             |
| 14        | CHURCH OF GOD                |
| 15        | DISCIPLES OF CHRIST          |
| 16        | EVANGELICAL COVENANT         |
| 17        | FRIENDS                      |
| 18        | JEHOVAH'S WITNESSES          |
| 19        | LATTER DAY SAINTS            |
| 20        | ISLAM                        |
| 21        | NAZARENE                     |
| 22        | OTHER                        |
| 23        | PENTECOSTAL                  |
| 24        | PROTESTANT                   |
| 25        | PROTESTANT, NO DENOMINATION  |
| 26        | REFORMED                     |
| 27        | SALVATION ARMY               |
| 28        | UNITARIAN-UNIVERSALISM       |
| 29        | UNKNOWN/NO PREFERENCE        |
| 30        | NATIVE AMERICAN              |
| 31        | ZEN BUDDHISM                 |
| 32        | AFRICAN RELIGIONS            |
| 33        | AFRO-CARIBBEAN RELIGIONS     |
| 34        | AGNOSTICISM                  |
| 35        | ANGLICAN                     |
| 36        | ANIMISM                      |
| 37        | ATHEISM                      |
| 38        | BABI & BAHA'I FAITHS         |
| 39        | BON                          |
| 40        | CAO DAI                      |
| 41        | CELTICISM                    |
| 42        | CHRISTIAN (NON-SPECIFIC)     |
| 43        | CONFUCIANISM                 |
| 44        | CONGREGATIONAL               |
| 45        | CYBERCULTURE RELIGIONS       |
| 46        | DIVINATION                   |
| 47        | FOURTH WAY                   |
| 48        | FREE DAISM                   |
| 49        | FULL GOSPEL                  |
| 50        | GNOSIS                       |
| 51        | HINDUISM                     |
| 52        | HUMANISM                     |
| 53        | INDEPENDENT                  |
| 54        | JAINISM                      |
| 55        | MAHAYANA                     |
| 56        | MEDITATION                   |
| 57        | MESSIANIC JUDAISM            |
| 58        | MITRAISM                     |
| 59        | NEW AGE                      |
| 60        | NON-ROMAN CATHOLIC           |
| 61        | OCCULT                       |
| 62        | ORTHODOX                     |
| 63        | PAGANISM                     |
| 64        | PROCESS, THE                 |
| 65        | REFORMED/PRESBYTERIAN        |
| 66        | SATANISM                     |
| 67        | SCIENTOLOGY                  |
| 68        | SHAMANISM                    |
| 69        | SHIITE (ISLAM)               |
| 70        | SHINTO                       |
| 71        | SIKISM                       |
| 72        | SPIRITUALISM                 |
| 73        | SUNNI (ISLAM)                |
| 74        | TAOISM                       |
| 75        | THERAVADA                    |
| 76        | UNIVERSAL LIFE CHURCH        |
| 77        | VAJRAYANA (TIBETAN)          |
| 78        | VEDA                         |
| 79        | VOODOO                       |
| 80        | WICCA                        |
| 81        | YAOHUSHUA                    |
| 82        | ZOROASTRIANISM               |
| 83        | ASKED BUT DECLINED TO ANSWER |

<span id="_Toc3901257" class="anchor"></span>Table ‑. User-defined Table 0006: Religion

### PID-18 Patient account number (CX) 00121

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-19 SSN number ‑ patient (ST) 00122

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is populated for backwards compatibility only. SSN should be retrieved from PID-3.

### PID-20 Driver's license number - Patient (DLN) 00123

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-21 Mother's identifier (CX) 00124

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-22 Ethnic group (CE) 00125 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field further defines the patient's ancestry. Refer to User-defined Table 0189 - Ethnic group for suggested values. The second triplet of the CE data type for ethnic group (alternate identifier, alternate text, and name of alternate coding system) is reserved for governmentally assigned codes. In the US, a current use is to report ethnicity in line with US federal standards for Hispanic origin.

| Value  | Description            |
|--------|------------------------|
| 2135-2 | HISPANIC OR LATINO     |
| 2186-5 | NOT HISPANIC OR LATINO |
| 0000-0 | DECLINED TO ANSWER     |
| 9999-4 | UNKNOWN BY PATIENT     |

<span id="_Toc131832333" class="anchor"></span>Table ‑. User-defined Table 0189: Ethnic group

### PID-23 Birth place (ST) 00126 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is populated for backward compatibility only. Data should be pulled from PID-11.

### PID-24 Multiple birth indicator (ID) 00127

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field indicates whether the patient was part of a multiple birth. Refer to *HL7 Table 0136 - Yes/No Indicator* for valid values.

### PID-25 Birth order (NM) 00128

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: Populated if the Multiple Birth Indicator (field \#PID-24) = Yes *<u>and</u>* if the Birth Order is sent by DoD.

### PID-26 Citizenship (CE) 00129

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-27 Veterans military status (CE) 00130

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-28 Nationality (CE) 00739

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-29 Patient death date and time (TS) 00740

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date and time at which the patient death occurred.

### PID-30 Patient Death Indicator (ID) 00741

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field indicates if the patient is deceased. Refer to Table 3‑36. HL7 Table 0136: Yes/no indicator for valid values.

### PID-31 Identity Unknown Indicator (ID) 01535

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-32 Identity Reliability Code (IS) 01536

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains a coded value used to communicate information regarding the reliability of patient/person identifying data transmitted via a transaction. Values could indicate that certain fields on a PID segment for a given patient/person are known to be false (e.g., use of default or system-generated values for Date of Birth or Social Security Number. Refer to for suggested values.

| Value                                                      | Description                                                                                 |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| P                                                          | Pending                                                                                     |
| A                                                          | Accepted all fields                                                                         |
| R                                                          | Some fields were excepted                                                                   |
| C                                                          | Reject–Catastrophic – all fields were rejected                                              |
| N is stored on the MPI but mapped to R for sending to PSIM | Reject – Non Catastrophic edit – all fields were rejected but not due to catastrophic edit. |
| AC                                                         | Catastrophic Edit Accept                                                                    |
| AN                                                         | Non-Catastrophic Edit Accept                                                                |

<span id="_Toc3901259" class="anchor"></span>Table ‑. User-defined Table 0445: Identity Reliability Code

### PID-33 Last Update Date/Time (TS) 01537

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-34 Last Update Facility (HD) 01538

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-35 Species Code (CE) 01539

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-36 Breed Code (ID) 01540

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-37 Strain (ST) 01541

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

### PID-38 Production Class Code (CE) 01542

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is not used.

## PV1: Patient Visit Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Only fields used by the MPI in the PV1 segment are PV1-44 Admit Date/Time and PV1-2 Patient Class. All other fields may or may not be populated depending on the message type; however, none of them are used by the MPI.

> **NOTE:** This segment is only included in A01, A03, A04, A08, and A31.

The PV1 segment is used by Registration/Patient Administration applications to communicate information on an account or visit-specific basis. The default is to send account level data. To use this segment for visit level data must be valued to "V". The value of PV-51 affects the level of data being sent on the PV1 and any other segments that are part of the associated PV1 hierarchy (e.g., ROL, DG1, or OBX).

The facility ID, the optional fourth component of each patient location field, is a HD data type that is uniquely associated with the healthcare facility containing the location. A given institution, or group of intercommunicating institutions, should establish a list of facilities that may be potential assignors of patient locations. The list will be one of the institution's master dictionary lists. The facility ID must be unique across facilities at a given site. This field is required for HL7 implementations that have more than a single healthcare facility with bed locations, since the same \<point of care\> ^ \<room\> ^ \<bed\> combination may exist at more than one facility.

| SEQ | LEN | DT | OPT | RP/# | TBL | Item | Element Name          | VistA Desc                              |
|---------|---------|--------|---------|----------|---------|----------|---------------------------|---------------------------------------------|
| 1       | 4       | SI     | O       |          |         | 00131    | Set ID - PV1              | Passed but not used by MPI.                 |
| 2       | 1       | IS     | R       |          |         | 00132    | Patient Class             | MPI will pass N to PSIM                     |
| 3       | 80      | PL     | O       |          |         | 00133    | Assigned Patient Location | Passed but not used by MPI.                 |
| 4       | 2       | IS     | O       |          | 0007    | 00134    | Admission Type            | Passed but not used by MPI.                 |
| 5       | 250     | CX     | O       |          |         | 00135    | Preadmit Number           | Passed but not used by MPI.                 |
| 6       | 80      | PL     | O       |          |         | 00136    | Prior Patient Location    | Passed but not used by MPI.                 |
| 7       | 250     | XCN    | O       | Y        | 0010    | 00137    | Attending Doctor          | Passed but not used by MPI.                 |
| 8       | 250     | XCN    | O       | Y        | 0010    | 00138    | Referring Doctor          | Passed but not used by MPI.                 |
| 9       | 250     | XCN    | B       | Y        | 0010    | 00139    | Consulting Doctor         | Passed but not used by MPI.                 |
| 10      | 3       | IS     | O       |          | 0069    | 00140    | Hospital Service          | Passed but not used by MPI.                 |
| 11      | 80      | PL     | O       |          |         | 00141    | Temporary Location        | Passed but not used by MPI.                 |
| 12      | 2       | IS     | O       |          | 0087    | 00142    | Preadmit Test Indicator   | Passed but not used by MPI.                 |
| 13      | 2       | IS     | O       |          | 0092    | 00143    | Re-admission Indicator    | Passed but not used by MPI.                 |
| 14      | 6       | IS     | O       |          | 0023    | 00144    | Admit Source              | Passed but not used by MPI.                 |
| 15      | 2       | IS     | O       | Y        | 0009    | 00145    | Ambulatory Status         | Passed but not used by MPI.                 |
| 16      | 2       | IS     | O       |          | 0099    | 00146    | VIP Indicator             | Passed but not used by MPI.                 |
| 17      | 250     | XCN    | O       | Y        | 0010    | 00147    | Admitting Doctor          | Passed but not used by MPI.                 |
| 18      | 2       | IS     | O       |          | 0018    | 00148    | Patient Type              | Passed but not used by MPI.                 |
| 19      | 250     | CX     | O       |          |         | 00149    | Visit Number              | Passed but not used by MPI.                 |
| 20      | 50      | FC     | O       | Y        | 0064    | 00150    | Financial Class           | Passed but not used by MPI.                 |
| 21      | 2       | IS     | O       |          | 0032    | 00151    | Charge Price Indicator    | Passed but not used by MPI.                 |
| 22      | 2       | IS     | O       |          | 0045    | 00152    | Courtesy Code             | Passed but not used by MPI.                 |
| 23      | 2       | IS     | O       |          | 0046    | 00153    | Credit Rating             | Passed but not used by MPI.                 |
| 24      | 2       | IS     | O       | Y        | 0044    | 00154    | Contract Code             | Passed but not used by MPI.                 |
| 25      | 8       | DT     | O       | Y        |         | 00155    | Contract Effective Date   | Passed but not used by MPI.                 |
| 26      | 12      | NM     | O       | Y        |         | 00156    | Contract Amount           | Passed but not used by MPI.                 |
| 27      | 3       | NM     | O       | Y        |         | 00157    | Contract Period           | Passed but not used by MPI.                 |
| 28      | 2       | IS     | O       |          | 0073    | 00158    | Interest Code             | Passed but not used by MPI.                 |
| 29      | 1       | IS     | O       |          | 0110    | 00159    | Transfer to Bad Debt Code | Passed but not used by MPI.                 |
| 30      | 8       | DT     | O       |          |         | 00160    | Transfer to Bad Debt Date | Passed but not used by MPI.                 |
| 31      | 10      | IS     | O       |          | 0021    | 00161    | Bad Debt Agency Code      | Passed but not used by MPI.                 |
| 32      | 12      | NM     | O       |          |         | 00162    | Bad Debt Transfer Amount  | Passed but not used by MPI.                 |
| 33      | 12      | NM     | O       |          |         | 00163    | Bad Debt Recovery Amount  | Passed but not used by MPI.                 |
| 34      | 1       | IS     | O       |          | 0111    | 00164    | Delete Account Indicator  | Passed but not used by MPI.                 |
| 35      | 8       | DT     | O       |          |         | 00165    | Delete Account Date       | Passed but not used by MPI.                 |
| 36      | 3       | IS     | O       |          | 0112    | 00166    | Discharge Disposition     | Passed but not used by MPI.                 |
| 37      | 25      | CM     | O       |          | 0113    | 00167    | Discharged to Location    | Passed but not used by MPI.                 |
| 38      | 250     | CE     | O       |          | 0114    | 00168    | Diet Type                 | Passed but not used by MPI.                 |
| 39      | 2       | IS     | O       |          | 0115    | 00169    | Servicing Facility        | Passed but not used by MPI.                 |
| 40      | 1       | IS     | B       |          | 0116    | 00170    | Bed Status                | Passed but not used by MPI.                 |
| 41      | 2       | IS     | O       |          | 0117    | 00171    | Account Status            | Passed but not used by MPI.                 |
| 42      | 80      | PL     | O       |          |         | 00172    | Pending Location          | Passed but not used by MPI.                 |
| 43      | 80      | PL     | O       |          |         | 00173    | Prior Temporary Location  | Passed but not used by MPI.                 |
| 44      | 26      | TS     | O       |          |         | 00174    | Admit Date/Time           | Currently admitted – date/time of admission |
| 45      | 26      | TS     | O       | Y        |         | 00175    | Discharge Date/Time       | Passed but not used by MPI.                 |
| 46      | 12      | NM     | O       |          |         | 00176    | Current Patient Balance   | Passed but not used by MPI.                 |
| 47      | 12      | NM     | O       |          |         | 00177    | Total Charges             | Passed but not used by MPI.                 |
| 48      | 12      | NM     | O       |          |         | 00178    | Total Adjustments         | Passed but not used by MPI.                 |
| 49      | 12      | NM     | O       |          |         | 00179    | Total Payments            | Passed but not used by MPI.                 |
| 50      | 250     | CX     | O       |          | 0203    | 00180    | Alternate Visit ID        | Passed but not used by MPI.                 |
| 51      | 1       | IS     | O       |          | 0326    | 01226    | Visit Indicator           | Passed but not used by MPI.                 |
| 52      | 250     | XCN    | B       | Y        | 0010    | 01274    | Other Healthcare Provider | Passed but not used by MPI.                 |

<span id="_Toc131832335" class="anchor"></span>Table ‑. PV1: Patient Visit, HL7 attributes

PV1 Field Definition

### PV1-2 Patient Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is used by systems to categorize patients by site. It does not have a consistent industry-wide definition. It is subject to site-specific variations. Refer to for suggested values.

| Value | Description        |
|-------|--------------------|
| E     | Emergency          |
| I     | Inpatient          |
| O     | Outpatient         |
| P     | Preadmit           |
| R     | Recurring patient  |
| B     | Obstetrics         |
| C     | Commercial Account |
| N     | Not Applicable     |
| U     | Unknown            |

<span id="_Toc3901261" class="anchor"></span>Table ‑. User-defined Table 0004 - Patient class

"Commercial Account" is used by reference labs for specimen processing when the service is billed back to a third party. A registration is processed for the specimen to facilitate the subsequent billing. The identity of the patient may be known or unknown. In either case, for billing and statistical purposes, the patient class is considered a commercial account due to the third party billing responsibility.

"Not Applicable" is used only in cases where the PV1 segment itself is not applicable but is retained in the message definitions for backwards compatibility (for example when a managed care system sends A28, A29, or A31 messages to indicate the enrolment of a patient in the system and there is no scheduled "visit" or "encounter" and hence the entire PV1 segment is not applicable).

> **NOTE:** MPI will send 'N' to PSIM for Patient Class.

### PV1-44 Admit Date/Time (TS) 00174

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the current admit date/time or the last registration date/time. Using the PV1-2 Patient Class to determine if it's an admission date/time or a registration date/time.

## PV2: Patient Visit Segment – Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PV2 segment is a continuation of information contained on the PV1 segment.

> **NOTE:** Only fields used by the MPI in the PV2 segment is PV2-8 Expected Admit Date/time for the next scheduled appointment, PV2-14 Previous Service Date for the last admission date, and PV2-46 Patient Status Effective Date for the last registration date (date only, time not included). All other fields may or may not be populated depending on the message type; however, none of them are used by the MPI.

> **NOTE:** This segment is only included in A04, A08, and A31.

The PV2 segment is a continuation of information contained on the PV1 segment.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>ELEMENT NAME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>80</td>
<td>PL</td>
<td>C</td>
<td></td>
<td></td>
<td>00181</td>
<td>Prior Pending Location [not passed to MPI]</td>
</tr>
<tr class="even">
<td>2</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0129</td>
<td>00182</td>
<td>Accommodation Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00183</td>
<td>Admit Reason [not passed to MPI]</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00184</td>
<td>Transfer Reason [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>5</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00185</td>
<td>Patient Valuables [not passed to MPI]</td>
</tr>
<tr class="even">
<td>6</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00186</td>
<td>Patient Valuables Location [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>7</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00187</td>
<td>Visit User Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00188</td>
<td>Expected Admit Date/Time (used for the Next Scheduled Appointment)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00189</td>
<td>Expected Discharge Date/Time [not passed to MPI]</td>
</tr>
<tr class="even">
<td>10</td>
<td>3</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00711</td>
<td>Estimated Length of Inpatient Stay [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>11</td>
<td>3</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00712</td>
<td>Actual Length of Inpatient Stay [not passed to MPI]</td>
</tr>
<tr class="even">
<td>12</td>
<td>50</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00713</td>
<td>Visit Description [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>13</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00714</td>
<td>Referral Source Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>14</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00715</td>
<td>Previous Service Date (used for the Last Admission Date)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00716</td>
<td>Employment Illness Related Indicator [not passed to MPI]</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td></td>
<td>00717</td>
<td>Purge Status Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>17</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00718</td>
<td>Purge Status Date [not passed to MPI]</td>
</tr>
<tr class="even">
<td>18</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0214</td>
<td>00719</td>
<td>Special Program Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00720</td>
<td>Retention Indicator [not passed to MPI]</td>
</tr>
<tr class="even">
<td>20</td>
<td>1</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00721</td>
<td>Expected Number of Insurance Plans [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>21</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0215</td>
<td>00722</td>
<td>Visit Publicity Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00723</td>
<td>Visit Protection Indicator [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>23</td>
<td>250</td>
<td>XON</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00724</td>
<td>Clinic Organization Name [not passed to MPI]</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0216</td>
<td>00725</td>
<td>Patient Status Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td></td>
<td>00726</td>
<td>Visit Priority Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>26</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00727</td>
<td>Previous Treatment Date [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>27</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td></td>
<td>00728</td>
<td>Expected Discharge Disposition [not passed to MPI]</td>
</tr>
<tr class="even">
<td>28</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00729</td>
<td>Signature on File Date [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>29</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00730</td>
<td>First Similar Illness Date [not passed to MPI]</td>
</tr>
<tr class="even">
<td>30</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0218</td>
<td>00731</td>
<td>Patient Charge Adjustment Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>31</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0219</td>
<td>00732</td>
<td>Recurring Service Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>32</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00733</td>
<td>Billing Media Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>33</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00734</td>
<td>Expected Surgery Date and Time [not passed to MPI]</td>
</tr>
<tr class="even">
<td>34</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00735</td>
<td>Military Partnership Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>35</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00736</td>
<td>Military Non-Availability Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>36</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00737</td>
<td>Newborn Baby Indicator [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>37</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00738</td>
<td>Baby Detained Indicator [not passed to MPI]</td>
</tr>
<tr class="even">
<td>38</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>01543</td>
<td>Mode of Arrival Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>39</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>01544</td>
<td>Recreational Drug Use Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>40</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>01545</td>
<td>Admission Level of Care Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>41</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>01546</td>
<td>Precaution Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>42</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>01547</td>
<td>Patient Condition Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>43</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td></td>
<td>00759</td>
<td>Living Will Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>44</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td></td>
<td>00760</td>
<td>Organ Donor Code [not passed to MPI]</td>
</tr>
<tr class="odd">
<td>45</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>01548</td>
<td>Advance Directive Code [not passed to MPI]</td>
</tr>
<tr class="even">
<td>46</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>01549</td>
<td><p>Patient Status Effective Date (used for the Last Registration Date)</p>
<p><strong>NOTE:</strong> Does not include Time.</p></td>
</tr>
<tr class="odd">
<td>47</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>01550</td>
<td>Expected LOA Return Date/Time [not passed to MPI]</td>
</tr>
</tbody>
</table>

<span id="_Toc3901262" class="anchor"></span>Table ‑. HL7 Attribute Table - PV2 – Patient visit – additional information

PV2 Field Definition

### PV2-8 Expected admit date/time (TS) 00188

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date and time that the patient has as their next scheduled outpatient appointment.

### PV2-14 Previous service date (DT) 00715

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date of the last admission at this facility.

### PV2-46 Patient Status Effective Date (DT) 01549

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date of the last registration at this facility.

## QAK: Query Acknowledgement Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Only field QAK-2 (Query Response Status) is used in the response to the Local/Missing ICN Resolution job and the K22 response to the Q22 query.

The QAK segment contains information sent with responses to a query. Although the QAK segment is required in the responses to the enhanced queries it may appear as an optional segment placed after the (optional) ERR segment in any query response (message) to any original mode query.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP</strong></th>
<th><strong>TBL</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>MPI Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>32</td>
<td>ST</td>
<td>C</td>
<td></td>
<td></td>
<td>00696</td>
<td>Query Tag</td>
<td><p>Local/Missing ICN Resolution job or real-time query (VQQ): DFN of patient sent to MPI for ICN assignment</p>
<p>RSP/K22: Original Query Message ID</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td><a href="#HL70208">0208</a></td>
<td>00708</td>
<td>Query Response Status</td>
<td><p>Local/Missing ICN Resolution job or real-time query (VQQ):</p>
<ul>
<li><blockquote>
<p>NO DATA</p>
</blockquote></li>
<li><blockquote>
<p>NO DATA – POTENTIAL MATCHES FOUND</p>
</blockquote></li>
<li><blockquote>
<p>OK</p>
</blockquote></li>
</ul>
<p>RSP/K22: Refer to Table 0208</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>01375</td>
<td>Message Query Name</td>
<td><p>Local/Missing ICN Resolution job or real-time query (VQQ): (Not used)</p>
<p>RSP/K22: Q22^Find Candidates^HL72.4</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>01434</td>
<td>Hit Count</td>
<td><p>Local/Missing ICN Resolution job or real-time query (VQQ): (not used)</p>
<p>RSP/K22: 0 or 1 for DFN/Site query.</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>10</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>01622</td>
<td>This payload</td>
<td>Passed but not used by the MPI.</td>
</tr>
<tr class="even">
<td>6</td>
<td>10</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>01623</td>
<td>Hits remaining</td>
<td>Passed but not used by the MPI.</td>
</tr>
</tbody>
</table>

<span id="_Toc131832336" class="anchor"></span>Table ‑. QAK: Query Acknowledgement, HL7 attributes

QAK Field Definition

### QAK-1 Query Tag (ST) 00696 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field may be valued by the initiating system to identify the query, and may be used to match response messages to the originating query. If it is valued, the responding system is required to echo it back as the first field in the query Acknowledgement segment (QAK). This field differs from *MSA-2-message control ID* in that its value remains constant for each message (i.e., all continuation messages) associated with the query, whereas *MSA-2-Message control ID* may vary with each continuation message, since it is associated with each individual message, not the query as a whole. *QAK-1-Query tag* is not conditional on the presence of the *QRD-1-Query ID* field in the original mode queries: in the original mode queries *QAK-1-Query tag* is

Local/Missing ICN Resolution job or real-time query (VQQ): DFN of patient sent to MVI for ICN assignment

RSP/K22: Original Query Message ID

### QAK-2 Query Response Status (ID) 00708 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field allows the responding system to return a precise response status. It is especially useful in the case where no data is found that matches the query parameters, but where there is also no error. It is defined with (Table 3‑53 in this manual), as shown below:

Local/Missing ICN Resolution job or real-time query (VQQ): NO DATA, NO DATA – POTENTIAL MATCHES FOUND, or OK

RSP/K22: Table values used.

| Value | Description                             |
|-----------|---------------------------------------------|
| OK        | Data found, no errors (this is the default) |
| NF        | No data found, no errors                    |
| AE        | Application error                           |
| AR        | Application reject                          |

<span id="_Ref104385883" class="anchor"></span>Table ‑. HL7 Table 0208: Query Response Status

### QAK-3 Message query name (CE) 01375

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field contains the name of the query. These names are assigned by the function-specific chapters of this specification. Site-specific event replay query names begin with the letter "Z." Refer to for suggested values.

Local/Missing ICN Resolution job or real-time query (VQQ): This field is not used

RSP/K22: Q22^Find Candidates^HL72.4

### QAK-4 Hit count total (NM) 01434

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field, when used, contains the total number of records found by the Server that matched the query. For tabular responses, this is the number of rows found. For other response types, the Conformance Statement defines the meaning of a "hit."

Local/Missing ICN Resolution job or real-time query (VQQ): This field is not used

RSP/K22: 0 or 1 for DFN/Site query.

## QPD: Query Parameter Definition Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QPD segment defines the parameters of the query.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP</strong></th>
<th><strong>TBL</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>MPI Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>0471</td>
<td>01375</td>
<td>Message Query Name</td>
<td>Q22^Find Candidates^HL72.4</td>
</tr>
<tr class="even">
<td>2</td>
<td>32</td>
<td>ST</td>
<td>C</td>
<td></td>
<td></td>
<td>00696</td>
<td>Query Tag</td>
<td>Original Message ID</td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td>256</td>
<td>varies</td>
<td></td>
<td></td>
<td></td>
<td>01435</td>
<td>User Parameters (in successive fields)</td>
<td><p>DFN/Station Number</p>
<p>or</p>
<p>Last name, first name, date of birth and social security number, etc.</p></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td>256</td>
<td>varies</td>
<td></td>
<td></td>
<td></td>
<td>01435</td>
<td>Matching Algorithm Name</td>
<td><p>VHA MPI</p>
<p>or</p>
<p>INITIATE</p></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td>256</td>
<td>varies</td>
<td></td>
<td></td>
<td></td>
<td>01435</td>
<td>Matching Algorithm Version</td>
<td><p>1.0</p>
<p>or</p>
<p>7.5</p></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td>2</td>
<td>varies</td>
<td></td>
<td></td>
<td></td>
<td>01435</td>
<td>User parameters</td>
<td><p>TF = add the site sending the query to the Treating Facility List.</p>
<p>AS = add the site sending the query to the site association for the Treating Facility for the site associated with the DFN.</p>
<p>BT = add both the TF and the AS.</p>
<p>NT = don't add a TF or an AS (If nothing is passed the default will be NT).</p>
<p>When user parameters are last name, first name, etc, only NT will be supported at this time.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc131832338" class="anchor"></span>Table ‑. QPD─Query Parameter Definition, HL7 attributes

QPD Field Definitions

### QPD-1 Message query name (CE) 01375 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field contains the name of the query. These names are assigned by the function-specific chapters of this specification. It is one to one with the conformance statement for this query name, and it is in fact an identifier for that conformance statement. Site-specific query names begin with the letter "Z." Refer to for suggested values.

Q22^Find Candidates^HL72.4

### QPD-2 Query tag (ST) 00696 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field may be valued by the initiating system to identify the query, and may be used to match response messages to the originating query. If this field is valued, the responding system is required to echo it back as the first field in the query acknowledgement segment (QAK).

This field differs from *MSA-2-Message control ID* in that its value remains constant for each message (i.e. all continuation messages) associated with the query, whereas *MSA-2-Message control ID* may vary with each continuation message, since it is associated with each individual message, not the query as a whole.

> **NOTE:** *Implementation considerations: *It is not necessary to value this field in implementations where the only return message on the socket will be the response to the query that was just sent. Conversely, in an "asynchronous" implementation where many queries, responses, and other messages may be communicated bidirectionally over the same socket, it is essential that this field be valued so that the Client knows to which query the Server is responding.

Original Message ID

### QPD-3 User parameters (Varies) 01435 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: These successive parameter fields hold the values that the Client passes to the Server.

The client data is presented as a sequence of HL7 fields. Beginning at *QPD-3-User parameters*, the remaining fields of the QPD segment carry user parameter data. Each QPD user parameter field corresponds to one parameter defined in the Conformance Statement, where each name, type, optionality, and repetition of each parameter has been specified. While these parameters are understood to be usually "anded" together, the user must inspect the required Conformance Statement to properly understand each. Except in the QSC variant, the parameter names do not need to be stated in the query; they are understood to be positional based on the Conformance Statement.

Each parameter field may be specified in the Conformance Statement to be of any single data type, including the complex QIP and QSC types. Parameter fields may also contain the sort control (SRT) field or the segment group (ID) field defined in Sections 5.4.5.3.1 and 5.4.5.3.2 below.

Parameter fields in the QPD segment appear in the same order as in the Conformance Statement.

1<sup>st</sup> implementation: DFN/Station numberPID.3 = \<dfn\>\~\~~USVHA&&0363~PI~VA FACILITY ID&\<station \#\>&L@PID.3.1^\<dfn\>@PID.3.2^\<null\>@PID.3.3^\<null\>@PID.3.4^USVHA&&0363@PID.3.5^PI@PID.3.6^VA FACILITY ID&\<station#\>&L

2<sup>nd</sup> implementation: Last Name, First Name, Date of Birth, Social Security Number

@PID.5.1^\<last name\>

@PID.5.2^\<first name\>

@PID.5.3^\<null\>

@PID.5.4^\<null\>

@PID.5.5^\<null\>

@PID.5.6^\<null\>

@PID.5.7^L

@PID.7^\<date of birth in HL7 format\>

@PID.3.1^\<social security number\>

@PID.3.2^\<null\>

@PID.3.3^\<null\>

@PID.3.4^USVHA&&0363

@PID.3.5^SS

@PID.3.6^VA FACILITY ID&\<station#\>&L

MVI implementation of QBP/Q22 to send to PSIM for the Initiate Algorithm implementation

- SSN

> @PID.3^\<ssn\>^\<null\>^\<null\>^USVHA&&0363^SS^VA FACILITY ID&\<station#\>&L

- Claim Number

> @PID.3^\<claim number\>^\<null\>^\<null\>^\<null\>^USVBA&&0363^PN^VA FACILITY ID&\<station#\>&L

- Name

> @PID.5^\<last name\>^\<first name\>^\<middle\>^\<suffix\>^\<\>^\<\>^\<\>^\<L\>

- Physical Address

> @PID.11^\<Physical Address Line 1\>^\<Physical Address Line 2\>^\<Physical Address City\>^\<Physical Address State\>^\<Physical Address Zip Code\>^\<country\>^P

- Date of Birth

> @PID.7^\<date of birth in HL7 format\>

- Home Phone (Area Code & Number)

> @PID.13^\<Home Phone\>

- Gender

> @PID.8^\<Gender\>

- Date of Last Treatment

> @EVN.2^\<Last Treatment Date \>

- Date of Death

> @PID.29^\<date of death\>

- Multiple Birth Indicator

> @PID.24^\<multiple birth indicator\>

- Place of Birth City and State

> @PID.11^\<\>^\<\>^\<Place of birth City\>^\<Place of birth State\>^\<\>^\<country\>^N

- Race (repeatable)

> @PID.10^\<race\>^\<\>^\<coding scheme\>

- Ethnicity

> @PID.22^\<ethnicity\>^\<\>^\<coding scheme\>

- Mother’s Maiden Name

> @PID.5^\<mothers maiden name\>^\<\>^\<\>^\<\>^\<\>^\<\>^\<\>^\<M\>

- Marital Status

> @PID.16^\<marital status\>^\<\>^\<coding scheme\>

Example: MVI implementation of QBP/Q22

MSH^~\|\\^MPI APP^200M~HL7.MPI-REDACTED:5026~DNS^PSIM^200PS~ps-dev.commserv.healthevet.va.gov:8090~DNS^20081031093516-0500^^QBP~Q22~^200M 109030^P~^2.4^^^AL^AL^USA

QPD^Q22~FIND CANDIDATES~HL72.4^888387888^@PID.5~SMITH~JOHN\~\~\~\~\~~L\|

@PID.3~000456789\~\~~USVHA&&0363~SS~VA FACILITY ID&553&L\|@PID.3~000456789\~\~~

USVBA&&0363~PN~VA FACILITY ID&553&L\|@PID.7~500 MAIN STREET~NOT USED~JACKSONVILLE~NC~28546\~~P~NOT USED\|@PID.7~20020506\|@PID.13~(555)555-0000\|@PID.8~M\|@EVN.2~20080312\|@PID.29~20080222\|@PID.24~Y\|@PID.11\~\~~New York City~NY\~~USA~N\|@PID.10~1002-5\~~HL005\|@PID.22~H\~~HL0189\|@PID.5~SMITH\~\~\~\~\~\~~M\|@PID.16~M\~~HL0002^INITIATE^7.5

RCP^I^1000~RD^R^^N^

### QPD-4 User parameters (Varies) 01435 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Matching Algorithm Name

Value will be when incoming from non-PSIM application: VHA MVI

Value will be when going to PSIM from the MVI: INITIATE

### QPD-5 User parameters (Varies) 01435 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Matching Algorithm Version

When matching algorithm name is VHA MVI Value will be: 1.0

When matching algorithm name is INITIATE value will be: 7.5

### QPD-6 User parameters (Varies) 01435 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Record Linking ActionValue will be when Algorithm is VHA MVI one of the following:

> TF = add the site sending the query to the Treating Facility List

> AS = add the site sending the query to the site association for the Treating Facility for the site associated with the DFN

> BT = add both the TF and the AS

> NT = add neither the TF or the AS (If nothing is passed the default will be NT)

> **NOTE:** QPD usage for query by example variant: The query by example is an extension of Query By Parameter (QBP) in which search parameters are passed by sending them in the segment, which naturally carries them. Thus if one wanted to perform a "find_candidates" query using query by example, one would send the demographics information on which to search in the PID and/or PD1 segments leaving blank those fields in the segment sent which are not query parameters. If, for example, religion were not one of the query parameters, PID-17 would be left blank when the PID was sent in the query. Parameters which do not occur naturally in an HL7 message, such as search algorithm, confidence level, etc, would continue to be carried in the QPD segment as they are in the Query by Parameter. The segments and fields available for use as query parameters would be specified in the Conformance Statement for the query.

Value will be when Algorithm is INITIATE: NT (doesn't need to be specified, default value)

## QRD: Original-Style Query Definition Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QRD segment is used to define a query.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 26%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>MPI Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>00025</td>
<td>Query Date/Time</td>
<td>Date/Time query built</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>00026</td>
<td>Query Format Code</td>
<td>R – for record orientated response</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>00027</td>
<td>Query Priority</td>
<td>I for immediate</td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>00028</td>
<td>Query ID</td>
<td>Integration Control Number</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0107</td>
<td>00029</td>
<td>Deferred Response Type</td>
<td>No value passed by the MPI</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00030</td>
<td>Deferred Response Date/Time</td>
<td>No value passed by the MPI</td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td>CQ</td>
<td>R</td>
<td></td>
<td></td>
<td>00031</td>
<td>Quantity Limited Request</td>
<td>1&lt;component separator&gt; RD</td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td>XCN</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>00032</td>
<td>Who Subject Filter</td>
<td>repeat patient ID list including ICN,SSN AND site/DFN</td>
</tr>
<tr class="odd">
<td>9</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>00033</td>
<td>What Subject Filter</td>
<td><p>DEM for demographics</p>
<p>GID for Generate new identifier</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>00034</td>
<td>What Department Data Code</td>
<td>No value passed by the MPI</td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>CM</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00035</td>
<td>What Data Code Value Qual</td>
<td>No value passed by the MPI</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0108</td>
<td>00036</td>
<td>Query Results Level</td>
<td>No value passed by the MPI</td>
</tr>
</tbody>
</table>

<span id="_Toc131832339" class="anchor"></span>Table ‑. QRD: Original-Style Query Definition, HL7 attributes

QRD Field Definitions

### QRD-1 Query Date/Time (TS) 00025 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the date the query was generated by the application program.

### QRD-2 Query Format Code (ID) 00026 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field refers to valid values in the (Table 3‑56 in this manual), as shown below:

| Value | Description                       |
|-----------|---------------------------------------|
| R         | Response is in record-oriented format |
| T         | Response is in tabular format         |

<span id="_Ref104385904" class="anchor"></span>Table ‑. HL7 Table 0106: Query/Response Format Code

The MVI is always passing R.

### QRD-3 Query Priority (ID) 00027

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the time frame in which the response is expected.

REF: For a list of valid values, please refer to Table 3‑57 in this manual, "." Table values and subsequent fields specify time frames for response.

| Value | Description |
|-----------|-----------------|
| I         | Immediate       |

<span id="_Ref104385940" class="anchor"></span>Table ‑. HL7 Table 0091: Query Priority

### QRD-4 Query ID (ST) 00028

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains a unique identifier for the query. Assigned by the querying application. Returned intact by the responding application.

Integration Control Number is passed as the value used for lookup at the site.

### QRD-5 Deferred Response Type (ID) 00029

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No value passed by the MVI.

### QRD-6 Deferred Response Date/Time (TS) 00030 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No value passed by the MVI.

### QRD-7 Quantity Limited Request (CQ) 00031 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<quantity (NM)\> ^ \<units (CE)\>

Definition: This field contains the maximum length of the response that can be accepted by the requesting system. Valid responses are numerical values (in the first component) given in the units specified in the second component.

REF: For a list of valid entries for the second component, please refer to Table 3‑58 in this manual, "." Default is LI (lines).

| Value | Description |
|-----------|-----------------|
| RD        | Records         |

<span id="_Ref104385965" class="anchor"></span>Table ‑. HL7 Table 0126: Quantity Limited Request

### QRD-8 Who Subject Filter (XCN) 00032 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<ID number (ST)\> ^ \<family name (FN)\> ^ \<given name (ST)\> ^ \<second and further given names or initials thereof (ST)\> ^ \<suffix (e.g., JR or III) (ST)\> ^ \<prefix (e.g., DR) (ST)\> ^ \<degree (e.g., MD) (IS)\> ^ \<source table (IS)\> ^ \<assigning authority (HD)\> ^ \<name type code (ID)\> ^ \<identifier check digit (ST)\> ^ \<code identifying the check digit scheme employed (ID)\> ^ \<identifier type code (IS)\> ^ \<assigning facility (HD)\> ^ \<name representation code (ID)\> ^ \<name context (CE)\> ^ \<name validity range (DR)\> ^ \< name assembly order (ID)\>

> Subcomponents of assigning authority: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

> Subcomponents of assigning facility: \<namespace ID (IS)\> & \<universal ID (ST)\> & \<universal ID type (ID)\>

Definition: This field contains the list of identifiers (one or more) used by the healthcare facility to uniquely identify a patient (e.g., VistA Internal ID \[DFN\], Claim Number, VHA MVI Integration Control Number \[ICN\], Social Security Number \[SSN\], unique individual identifier, etc.).

REF: For a list of valid values, please refer to "HL7 Table 0061—Check Digit Scheme" in the HL7 Standard Version 2.4 documentation. The arbitrary term of "internal ID" has been removed from the name of this field for clarity.

Future supported values are listed below:

|                |                         |                     |                        |                     |
|----------------|-------------------------|---------------------|------------------------|---------------------|
| Identifier | Assigning Authority | Identifier type | Assigning Location | Expiration date |
| National ICN   | USVHA                   | NI                  | 200M                   |                     |
| SSN            | USSSA                   | SS                  | unique station# id     |                     |
| VistA ID (DFN) | USVHA                   | PI                  | unique station# id     |                     |

<span id="_Toc131832343" class="anchor"></span>Table ‑. VA Patient identifiers

> **NOTE:** This field should *not* have been a required field. However, for backwards compatibility it remains a required field. There are some queries in the standard that have not required this field.

### QRD-9 What Subject Filter (CE) 00033 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field describes the kind of information that is required to satisfy the request. Valid values define the type of transaction inquiry and may be extended locally during implementation. DEM is the only value currently being utilized.

| Value | Description         |
|-----------|-------------------------|
| DEM       | Demographics            |
| GID       | Generate new identifier |

<span id="_Toc131832344" class="anchor"></span>Table ‑. HL7 Table 0048: What Subject Filter

REF: For detailed examples of use of various query filter fields, please refer to the "*HL7 Implementation Guide*."

### QRD-10 What Department Data Code (CE) 00034 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No value passed by the MVI.

### QRD-11 What Data Code Value Qual (CM) 00035 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No value passed by the MVI.

### QRD-12 Query Results Level (ID) 00036

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No value passed by the MVI.

## QRI: Query Response Instance Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QRI segment is used to indicate the weight match for a returned record (where the responding system employs a numeric algorithm) and/or the match reason code (where the responding system uses rules or other match options).

Examples of the use of this segment appear in Section 3.6, “MVI Queries.”

| SEQ | LEN | DT  | OPT | RP/# | TBL#             | ITEM# | ELEMENT NAME         |
|-----|-----|-----|-----|------|------------------|-------|----------------------|
| 1   | 10  | NM  | O   |      |                  | 01436 | Candidate Confidence |
| 2   | 2   | IS  | O   | Y    | [0392](#HL70392) | 01437 | Match Reason Code    |
| 3   | 250 | CE  | O   |      | [0393](#HL70393) | 01438 | Algorithm Descriptor |

<span id="_Toc495909696" class="anchor"></span>Table ‑. HL7 Attribute Table – QRI – Query Response Instance

QRI Field Definitions

#### QRI-1   Candidate confidence   (NM)   01436 

Definition: This field contains a numeric value indicating the match weight or confidence level associated with the record.

Example: \|0.88\| or \|12.32\|

One use of this optional field is in Patient Look-up transactions where the searching system employs a numeric algorithm for determining potential matches to patient/person look-ups.

Score returned from the Initiate Algorithm.

#### QRI-2   Match reason code   (IS)   01437 

Definition: This field contains a coded value indicating what search components (e.g., name, birth date, social security number) of the record returned matched the original query where the responding system does not assign numeric match weights or confidence levels. In short, it provides a method for passing a descriptive indication of why a particular record was found.

Refer to *[User-defined Table 0392  - Match reason](#HL70392)* for suggested values.

| <span id="HL70392" class="anchor"></span>Value | Description                     |
|------------------------------------------------|---------------------------------|
| DB                                             | Match on Date of Birth          |
| NA                                             | Match on Name (Alpha Match)     |
| NP                                             | Match on Name (Phonetic Match)  |
| SS                                             | Match on Social Security Number |

<span id="_Toc495909699" class="anchor"></span>Table ‑. User-defined Table 0392 – Match reason

#### QRI-3   Algorithm descriptor   (CE)   01438 

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (IS)\>

Definition: This field contains a text value indicating the name or identity of the specific search algorithm to which the *RCP-5 Search confidence threshold* and the *QRI-1 Candidate confidence* refer. Note that there are sometimes significant differences among the algorithms in their numeric scales (e.g., one is 0-100, another might be 10 – 20) as well as their meanings of the same value (two algorithms with an 80% match might not return the same records). Refer to for suggested values.

| Value         | Description                              |
|---------------|------------------------------------------|
| LINKSOFT_2.01 | Proprietary algorithm for LinkSoft v2.01 |
| MATCHWARE_1.2 | Proprietary algorithm for MatchWare v1.2 |
| INITIATE      | Proprietary algorithm for Initiate 7.5   |

<span id="_Toc3901274" class="anchor"></span>Table ‑. User-defined Table 0393 – Match algorithms

Example: \|MATCHWARE_1.2^^HL7nnnn\| or \|LINKSOFT_2.01^HL7nnnn\|

One use of this optional field is in Patient Look-up transactions where the searching system employs a numeric algorithm for determining potential matches to patient/person look-ups.

Example: 102-145~INITIATE

- In the example above, the value 102 represents the TASK THRESHOLD in the MPI PARAMETER file (#985.1).
- In this example above, the value 145 represents the AUTO-LINK THRESHOLD in the MPI PARAMETER file (#985.1).

## RCP: Response Control Parameter Segment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RCP segment is used to restrict the amount of data that should be returned in response to query.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP</strong></th>
<th><strong>TBL</strong></th>
<th><strong>Item#</strong></th>
<th><strong>Element name</strong></th>
<th><strong>MPI Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>00027</td>
<td>Query Priority</td>
<td>I</td>
</tr>
<tr class="even">
<td>2</td>
<td>10</td>
<td>CQ</td>
<td>O</td>
<td></td>
<td></td>
<td>00031</td>
<td>Quantity Limited Request</td>
<td><ol type="1">
<li><p>when algorithm is VHA MPI</p></li>
</ol>
<p>100 when algorithm is INITIATE</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>01440</td>
<td>Response Modality</td>
<td>R</td>
</tr>
<tr class="even">
<td>4</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>01441</td>
<td>Execution and Delivery Time</td>
<td>No value will be passed</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>01443</td>
<td>Modify Indicator</td>
<td>N</td>
</tr>
<tr class="even">
<td>6</td>
<td>512</td>
<td>SRT</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>01624</td>
<td>Sort-by Field</td>
<td>Passed but not used for the VHA MPI or Initiate implementations</td>
</tr>
<tr class="odd">
<td>7</td>
<td>256</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td></td>
<td>01594</td>
<td>Segment group inclusion</td>
<td>Passed but not used for the VHA MPI or Initiate implementations</td>
</tr>
</tbody>
</table>

<span id="_Toc131832345" class="anchor"></span>Table ‑. RCP: Response Control Parameter, HL7 Attribute

RCP Field Definitions

### RCP-1 Query priority (ID) 00027 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field contains the time frame in which the response is expected. Refer to for valid values. Table values and subsequent fields specify time frames for response.

Always immediate.

| Value | Description |
|-------|-------------|
| D     | Deferred    |
| I     | Immediate   |

<span id="_Toc131832346" class="anchor"></span>Table ‑. HL7 Table 0091: Query priority

### RCP-2 Quantity limited request (CQ) 00031 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<quantity (NM)\> ^ \<units (CE)\>

Definition: This field contains the maximum length of the response that can be accepted by the requesting system. Valid entries are numerical values (in the first component) given in the units specified in the second component. Default is LI (lines).

REF: Refer to for valid entries for the second component. In a segment pattern response, a line is defined as a single segment.

The RCP-2 field should be passed with a value of 1 for all unattended searches so that there will be one and only one matched record return. For attended searches that desire matched record and potential match record(s), the value of RCP-2 should be greater than 1.

For DFN/Station \# the range would be 0-1. (To be revisited when we have other search methods).

For INITIATE algorithm name the range would be 0-100.

| Value | Description | Message Usage | Comment                                     |
|-----------|-----------------|-------------------|-------------------------------------------------|
| CH        | Characters      | RSP/RTB/RDY       | Used where size of input buffer has limitations |
| LI        | Lines           | RTB/RDY           |                                                 |
| PG        | Pages           | RDY               |                                                 |
| RD        | Records         | RSP/RTB/RDY       | In RSP record = hit                             |
| ZO        | Locally defined |                   |                                                 |

<span id="_Toc131832347" class="anchor"></span>Table ‑. HL7 Table 0126: Quantity limited request

### RCP-3 Response modality (CE) 01440 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (IS)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<alternate coding system (IS)\>

Definition: This field specifies the timing and grouping of the response message(s). Refer to for valid values.

We would always be Real Time, possible batch in the future.

| Value | Description                                                                     |
|-----------|-------------------------------------------------------------------------------------|
| R         | Real Time                                                                           |
| T         | Bolus (a series of responses sent at the same time without use of batch formatting) |
| B         | Batch                                                                               |

<span id="_Toc131832348" class="anchor"></span>Table ‑. HL7 Table 0394: Response modality

### RCP-4 Execution and delivery time (TS) 01441 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specifies the time the response is to be returned. This field is only valued when *RCP-1-Query priority* contains the value D (Deferred).

Only used for deferred queries (Response modality)

### RCP-5 Modify indicator (ID) 01443 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field specifies whether the subscription is new or is being modified. Refer to for valid values.

New one each time.

| Value | Description       |
|-----------|-----------------------|
| N         | New Subscription      |
| M         | Modified Subscription |

<span id="_Toc131832349" class="anchor"></span>Table ‑. HL7 Table 0395: Modify indicator

### RCP-6 Sort-by field (SRT) 01624 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<sort-by field/parameter (varies)\> ^ \<sequencing (ID)\>

Definition: For queries requesting a tabular response, this field specifies by which fields the response is to be sorted, and the order(s) in which sorting is to be performed. When the QSC variant is not in use, the values specified for the first component in this field are derived from the ColName field of the Output Specification and Commentary. When the QSC variant is used, the values are derived from the ColName field of the Input/Output Specification and Commentary.

Each repetition of this field specifies a single sort field. Thus, the first repetition of this field specifies the primary sort field; the second repetition specifies the secondary sort field; etc.

We would NOT use for the DFN/Site query since there is only 1 value or 0 value returned.

### RCP-7 Segment group inclusion (ID) 01594 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: Specifies those optional segment groups which are to be included in the response. Refer to for values for Segment Group. This is a repeating field, to accommodate inclusion of multiple segment groups. The default for this field, not present, means that all relevant groups are included.

Default is not present, which includes all relevant groups.

> **NOTE:** Although the codes for segment groups are taken from , the exact segment-level definition of a segment group (e.g. PIDG) is given only in the conformance statement of the query in which this segment group appears.

For example:

| Value | Description |
|-----------|-----------------|
| PIDG      | PID group       |
| OBRG      | OBR group       |
| ORCG      | ORC group       |
| RXAG      | RXA group       |
| RXDG      | RXD group       |
| RXEG      | RXE group       |
| RXOG      | RXO group       |
| etc       |                 |

<span id="_Toc131832350" class="anchor"></span>Table ‑. HL7 Table 0391: Segment group

> **NOTE:** *HL7 Table 0391 – Segment group* currently includes no values defined by HL7. As values are agreed upon in conformance statements balloted by HL7 Technical Committees, they will be included in this table.

## RDF: Table Row Definition Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RDF segment defines the content of the row data segments (RDT) in the Tabular Data Response Message (TBR). It is used in two ways:

> 1\. As an optional segment in the SPQ message (Stored Procedure Request) or the VQQ (Virtual Table Query) message, this segment can be used to limit the number of columns returned and to specify what column positions the fields occupy (where supported, these features can be used to override the defaults for the particular query). If omitted, all fields defined for the query are returned in their default column order.

> 2\. As a required segment on the tabular data response message (TBR), this segment defines the contents of the table row data (RDT) segments that follow.

| SEQ | LEN | DT | OPT | RP/# | TBL# | Item# | Element Name          |
|---------|---------|--------|---------|----------|----------|-----------|---------------------------|
| 1       | 3       | NM     | R       |          |          | 00701     | Number of Columns per Row |
| 2       | 40      | RCD    | R       | Y        |          | 00702     | Column Description        |

<span id="_Toc131832351" class="anchor"></span>Table ‑. RDF: Table Row Definition, HL7 attributes

RDF Field Definitions

### RDF-1 Number of columns per row (NM) 00701

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field specifies the number of data columns (and therefore the number of fields) contained within each row of returned data.

24 passed for the number of fields potentially returned in response.

### RDF-2Column Description (RCD) 00702

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<Segment field name (ST)\> ^ \<HL7 data type (ST)\> ^ \<maximum column width (NM)\>

Definition: Each repetition of this field consists of three components:

> Component 1: HL7 field number,

> Component 2: data type,

> Component 3: maximum length.

The HL7 field designation numbers and translations for each are as follows:

| Field                                       | HL7 Field# | Data Type | Max Length |
|-------------------------------------------------|----------------|---------------|----------------|
| Last Name                                       | 00108.1        | ST            | 30             |
| SSN                                             | 00122          | ST            | 9              |
| DOB                                             | 00110          | TS            | 8              |
| CMOR                                            | 00756          | ST            | 6              |
| ICN                                             | 00105          | ST            | 19             |
| First Name                                      | 00108.2        | ST            | 30             |
| Treating Facilities (multiple entries possible) | 00169          | ST            | 999            |
| Date of Death                                   | 00740          | TS            | 8              |
| Middle Name                                     | 00108.3        | ST            | 16             |
| Sex                                             | 00111          | ST            | 1              |
| POB- City                                       | 00126.1        | ST            | 30             |
| POB – State                                     | 00126.2        | ST            | 3              |
| Name Prefix                                     | 00108.5        | ST            | 15             |
| Name Suffix                                     | 00108.4        | ST            | 10             |
| Mother's Maiden Name                            | 00109.1        | ST            | 20             |
| Claim Number                                    | ZEL6           | ST            | 9              |
| MPI DUP CASE#                                   | CASE#          | ST            | 69             |
| POW Status                                      | POW            | ST            | 1              |
| Multiple Birth Indicator                        | 00127          | ST            | 1              |
| Alias Last Name                                 | 00112.1        | ST            | 30             |
| Alias First Name                                | 00112.2        | ST            | 25             |
| Alias Middle Name                               | 00112.3        | ST            | 25             |
| Alias Prefix                                    | 00112.5        | ST            | 10             |
| Alias Suffix                                    | 00112.4        | ST            | 10             |

<span id="_Toc131832352" class="anchor"></span>Table ‑. HL7 field designation numbers and translations

REF: For a list of relational operators, please refer to Table 3‑75 in this manual, "HL7 Table 0209: Relational operator."

REF: For a list of relational conjunctions, please refer to Table 3‑76 in this manual, "HL7 Table 0210: Relational conjunction"

## RDT: Table Row Data Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RDT segment contains the row data of the tabular data response message (TBR).

| SEQ | LEN  | DT   | OPT | RP/# | TBL# | Item | Element Name |
|---------|----------|----------|---------|----------|----------|----------|------------------|
| 1-n     | Variable | Variable | R       |          |          | 00703    | Column Value     |

<span id="_Toc131832353" class="anchor"></span>Table ‑. RDT: Table Row Data, HL7 attributes

RDT Field Definition

### RDT-1 Column value (Variable) 00703

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field is a requested field. Fields occur in the position order defined for the query or table, (unless overridden by an optional RDF segment on a stored procedure request or virtual table query message), separated by field delimiters.

Values returned correspond directly to the values in the RDF: Table Row Definition Segment. If that field isn't populated, no value is passed.

| Field                                       | HL7 Field# | Data Type | Max Length |
|-------------------------------------------------|----------------|---------------|----------------|
| Last Name                                       | 00108.1        | ST            | 30             |
| SSN                                             | 00122          | ST            | 9              |
| DOB                                             | 00110          | TS            | 8              |
| CMOR                                            | 00756          | ST            | 6              |
| ICN                                             | 00105          | ST            | 19             |
| First Name                                      | 00108.2        | ST            | 30             |
| Treating Facilities (multiple entries possible) | 00169          | ST            | 999            |
| Date of Death                                   | 00740          | TS            | 8              |
| Middle Name                                     | 00108.3        | ST            | 16             |
| Sex                                             | 00111          | ST            | 1              |
| POB- City                                       | 00126.1        | ST            | 30             |
| POB – State                                     | 00126.2        | ST            | 3              |
| Name Prefix                                     | 00108.5        | ST            | 15             |
| Name Suffix                                     | 00108.4        | ST            | 10             |
| Mother's Maiden Name                            | 00109.1        | ST            | 20             |
| Claim Number                                    | ZEL6           | ST            | 9              |
| MPI DUP CASE#                                   | CASE#          | ST            | 69             |
| POW Status                                      | POW            | ST            | 1              |
| Multiple Birth Indicator                        | 00127          | ST            | 1              |
| Alias Last Name                                 | 00112.1        | ST            | 30             |
| Alias First Name                                | 00112.2        | ST            | 25             |
| Alias Middle Name                               | 00112.3        | ST            | 25             |
| Alias Prefix                                    | 00112.5        | ST            | 10             |
| Alias Suffix                                    | 00112.4        | ST            | 10             |

<span id="_Toc131832354" class="anchor"></span>Table ‑. HL7 field designation numbers and translations

## VTQ: Virtual Table Query Request Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VTQ segment is used to define queries that are responded to with the Tabular Data Message (TBR). The VTQ query message is an alternate method to the EQQ query message that some systems may find easier to implement, due to its use of HL7 delimiters that separate components of the selection definition, and its limited selection criteria. Queries involving complex selection criteria (nested operators, etc.) may need to be formatted as an EQL segment.

> **NOTE:** As with the other query methods, the functional chapters define specific queries supported as VTQ messages. Please refer to the functional chapters in the HL7 Version 2.4 documentation for the lists of HL7-defined virtual tables, selection lists, and criteria.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 21%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>Item</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>MPI Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>32</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00696</td>
<td>Query Tag</td>
<td>DFN of patient at site</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>00697</td>
<td>Query/Response Format Code</td>
<td>T</td>
</tr>
<tr class="odd">
<td>3</td>
<td>60</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>00698</td>
<td>VT Query Name</td>
<td><p>2 possible values listed below</p>
<p>VTQ_PID_ICN VTQ_PID_ICN</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>60</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>00699</td>
<td>Virtual Table Name</td>
<td>ICN</td>
</tr>
<tr class="odd">
<td>5</td>
<td>256</td>
<td>QSC</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00700</td>
<td>Selection Criteria</td>
<td>Fields used in Query</td>
</tr>
</tbody>
</table>

<span id="_Toc131832355" class="anchor"></span>Table ‑. VTQ: Virtual Table Query Request, HL7 attributes

VTQ Field Definitions

### VTQ-1 Query tag (ST) 00696

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field may be valued by the initiating system to identify the query, and may be used to match response messages to the originating query. If it is valued, the responding system is required to echo it back as the first field in the query Acknowledgement segment (QAK). This field differs from [MSA-2-message control ID](#_MSA-2__Message) in that its value remains constant for each message (i.e., all continuation messages) associated with the query, whereas may vary with each continuation message, since it is associated with each individual message, not the query as a whole.

### VTQ-2 Query/Response Format Code (ID) 00697

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field refers to HL7 Table 0106: Query/Response Format Code (Table 3‑56 in this manual), which lists valid values. At this point in time the only value used is T.

### VTQ-3 VT Query Name (CE) 00698

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

Definition: This field contains the name of the virtual table query.

<span class="smallcaps"><u>Name</u> <u>Function</u></span>

VTQ_PID_ICN_LOAD_1 Used to tell MVI that this is in initialization phase.

VTQ_PID_ICN_NO_LOAD Used to inquire to the MVI without any addition to MVI.

VTQ_DISPLAY_ONLY_QUERY Used to tell MVI that this is the Display Only Query.

EXACT_MATCH_QUERY Used to tell the MVI that only exact matches should be returned based upon business rules.

### VTQ-4 Virtual Table Name (CE) 00699

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

Definition: This field contains the name of the virtual table being referenced. This table name may refer to an HL7-defined segment, an HL7 virtual table, or a site-specific "Z table."

Integration Control Number (ICN).

REF: For more information HL7 virtual tables, please refer to the functional chapters in the HL7 Standard Version 2.4 documentation.

### VTQ -5 Selection Criteria (QSC) 00700

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Components: \<segment field name (ST)\> ^ \<relational operator (ID)\> ^ \<value (ST)\> ^ \<relational conjunction (ID)\>

Definition: Each repetition of this field defines a column in the RDT segment: the first repetition defines the first column of the RDT segment; the second repetition defines the second column of the RDT segments, etc.

This field indicates the conditions that qualify the rows to be returned in the query response. (This field conveys the same information as the "WHERE" clause in the corresponding SQL expression of the query, but is formatted differently.) It is comprised of the following components:

- A relational operator.
- The value to which the field will be compared.

| Field                  | HL7 Field# | Data Type | Max Length | Notes        |
|----------------------------|----------------|---------------|----------------|------------------|
| Last Name                  | 00108.1        | ST            | 30             | Must be present  |
| SSN                        | 00122          | ST            | 9              | Not sent if null |
| DOB                        | 00110          | TS            | 8              | Not sent if null |
| First Name                 | 00108.2        | ST            | 30             | Not sent if null |
| Date of Death              | 00740          | TS            | 8              | Not sent if null |
| Middle Name                | 00108.3        | ST            | 16             | Not sent if null |
| Sex                        | 00111          | ST            | 1              | Not sent if null |
| POB- City                  | 00126.1        | ST            | 30             | Not sent if null |
| POB – State                | 00126.2        | ST            | 3              | Not sent if null |
| Name Suffix                | 00108.4        | ST            | 10             | Not sent if null |
| Permanent Physical Address | 00114          | XAD           | 250            | Not sent if null |
| Physical Address Line 2    | 00114          |               |                | Not sent if null |
| Physical Address Line 3    | 00114          |               |                | Not sent if null |
| Physical Address City      | 00114          |               |                | Not sent if null |
| Physical Address State     | 00114          |               |                | Not sent if null |
| Physical Address Zip Code  | 00114          |               |                | Not sent if null |
| Home Phone                 | 00116          | XTN           | 250            | Not sent if null |
| Last Activity Date         |                |               |                | Not sent if null |
| Multiple Birth Indicator   | 00127          | ID            | 1              | Not sent if null |
| Race                       | 00113          | CE            | 250            | Not sent if null |
| Ethnicity                  | 00125          | CE            | 250            | Not sent if null |
| Marital Status             | 00119          | CE            | 250            | Not sent if null |

> **NOTE:** All fields are sent with equals, except DOB, which can be equals or generic. Generic is used for imprecise DOB.

REF: For a list of relational operators, please refer to Table 3‑75 in this manual, "HL7 Table 0209: Relational operator."

|                         |                       |
|-------------------------|-----------------------|
| Relational Operator | Value             |
| EQ                      | Equal                 |
| NE                      | Not Equal             |
| LT                      | Less than             |
| GT                      | Greater than          |
| LE                      | Less than or equal    |
| GE                      | Greater than or equal |
| CT                      | Contains              |
| GN                      | Generic               |

<span id="_Ref104386065" class="anchor"></span>Table ‑. HL7 Table 0209: Relational operator

If more than one comparison is to be made to select qualifying rows, a conjunction relating this repetition of the field to the next. Table provides a list of relational conjunctions.

|                            |          |
|----------------------------|----------|
| Relational Conjunction | Note |
| AND                        | Default  |
| OR                         |          |

<span id="_Ref104386089" class="anchor"></span>Table ‑. HL7 Table 0210: Relational conjunction

Hence, the segment (shown below) causes a response to be generated from the virtual table defined by the PID segment. All rows containing the name field subcomponents defined in the selection criteria field (last name = "Evans," first name = "Carolyn") will be selected for the response. The RDF segment will define the columns returned from each selected row.

VTQ\|100000082\|T\|VTQ_PID_ICN_NO_LOAD\|ICN\|@00108.1^EQ^MVIPATIENT^AND~@00122^EQ^000064567^AND~@00108.2^EQ^TEN^AND~@00110^EQ^19780303

NOTES:

- As previously stated, the VTQ segment does not, and is not intended to, provide as robust selection function as native EQQ query. It is offered as a simpler alternative.
- When applied to strings, the relational operators LT, GT, LE, and GE imply an alphabetic comparison.
- A "generic" comparison selects a record for inclusion in the response if the beginning of the designated field matches the select string.
- Where a repeating field is specified as an operand, a match on any instance of that field qualifies the row for inclusion in the response message.
- AND takes precedence over OR. More sophisticated precedence rules require that the query be expressed as an SQL message, or a stored procedure for the query may be written and referenced with the SPR segment.

## ZCT: VA Specific Emergency Contact Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The ZCT―VA Specific Emergency Contact segment is passed but not used by the MPI software. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment. This is not a required segment. It may or may not be present in all messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>VistA Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>NEXT OF KIN (NOK)</p>
<p><strong>NOTE:</strong> Value is always 1 for patient requested</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>35</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>K-NAME OF PRIMARY NOK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>K-RELATIONSHIP TO PATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>106</td>
<td>AD</td>
<td></td>
<td>Y</td>
<td></td>
<td><blockquote>
<p>Component 1:K-STREET ADDRESS (LINE 1)</p>
<p>Component 2:K-STREET ADDRESS (LINE 2) &amp; K-<br />
STREET ADDRESS (LINE 3)</p>
<p>Component 3: K-CITY</p>
<p>Component 4: K-STATE (abbreviation)</p>
<p>Component 5: K-ZIP code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td>106</td>
<td>AD</td>
<td></td>
<td>Y</td>
<td></td>
<td>K-ADDRESS SAME AS PATIENT'S?</td>
</tr>
<tr class="odd">
<td>6</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td><blockquote>
<p>K-PHONE NUMBER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td><blockquote>
<p>K-WORK PHONE NUMBER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>K-ADDRESS SAME AS PATIENT'S?</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PRIMARY NOK</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc131832358" class="anchor"></span>Table ‑. ZCT―VA Specific Emergency Contact, HL7 attributes

## ZEL: VA Specific Patient Eligibility Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The ZEL―VA Specific Patient Eligibility segment is passed but not used by the MPI software. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment. This is not a required segment. It may or may not be present in all messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>VistA Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ELIGIBILITY or PRIMARY ELIGIBILITY CODE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>16</td>
<td>CX</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>LONG ID or PRIMARY LONG ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>CX</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SHORT ID or PRIMARY SHORT ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DISABILITY RET. FROM MILITARY?</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CLAIM NUMBER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CLAIM FOLDER LOCATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>VETERAN (Y/N)?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ELIGIBILITY STATUS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ELIGIBILITY STATUS DATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ELIGIBILITY INTERIM RESPONSE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td>50</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ELIGIBILITY VERIF. METHOD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RECEIVING A&amp;A BENEFITS?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RECEIVING HOUSEBOUND BENEFITS?</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RECEIVING A VA PENSION?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RECEIVING A VA DISABILITY?</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>AGENT ORANGE EXPOS. INDICATED?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RADIATION EXPOSURE INDICATED?</p>
</blockquote></td>
</tr>
<tr class="even">
<td>20</td>
<td>1</td>
<td>ID</td>
<td>Y</td>
<td></td>
<td></td>
<td><blockquote>
<p>ENVIRONMENTAL CONTAMINANTS?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>21</td>
<td>5</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TOTAL ANNUAL VA CHECK AMOUNT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>22</td>
<td>22</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RADIATION EXPOSURE METHOD</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc131832359" class="anchor"></span>Table ‑. ZEL―VA Specific Patient Eligibility, HL7 attributes

## ZEM: VA Specific Employment Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The ZEM―VA Specific Employment Information segment is passed but not used by the MPI software. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment. This is not a required segment. It may or may not be present in all messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>VistA Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PATIENT DATA REQUESTED?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>EMPLOYMENT STATUS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>EMPLOYER NAME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>OCCUPATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Component 1: EMPLOYER STREET [LINE 1]</p>
<p>Component 2: EMPLOYER STREET [LINE 2] AND</p>
<p>EMPLOYER STREET [LINE 3]</p>
<p>Component 3: EMPLOYER CITY</p>
<p>Component 4: EMPLOYER STATE</p>
<p>Component 5: EMPLOYER ZIP CODE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>TN</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>EMPLOYER PHONE NUMBER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>GOVERNMENT AGENCY</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc131832360" class="anchor"></span>Table ‑. ZEM―VA Specific Employment Information, HL7 attributes

## ZET: VA Specific Event Reason for Date of Last Treatment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a VA defined segment used to transmit event reason for date of last treatment.

> **NOTE:** The ZET—Event Reason for Date of Last Treatment segment is passed but not used by the MPI software. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment. This is not a required segment. It may or may not be present in all messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 42%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>SEQ</strong></td>
<td><strong>LEN</strong></td>
<td><strong>DT</strong></td>
<td><strong>OPT</strong></td>
<td><strong>RP/#</strong></td>
<td><strong>TBL#</strong></td>
<td><strong>Item</strong></td>
<td><blockquote>
<p><strong>Element Name</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td>2</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>EVENT REASON CODE NAME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td>90</td>
<td>XON</td>
<td>O</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PATIENT PRIMARY FACILITY</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc131832361" class="anchor"></span>Table ‑. ZET: Event Reason for Date of Last Treatment, HL7 attributes

ZET Field Definitions

### ZET-1 Event Reason Code Name 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition (ZZ011): This field defines the corresponding event that has occurred. The possible values are:

> A1: Admission

> A2: Discharge

> A3: Clinic check-out

### ZET-2 Patient Primary Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field defines the facility at which the event has taken place.

Component 1: Name

Component 2: Station Number

## ZFF: VA Specific File/Field Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The ZFF―VA Specific File/Field segment is passed but not used by the MPI software. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment. This is not a required segment. It may or may not be present in all messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>VistA Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>20</td>
<td>NM</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>FILE NUMBER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>150</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>FIELD NUMBER(S)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc131832362" class="anchor"></span>Table ‑. ZFF―VA Specific File/Field, HL7 attributes

## ZPD: VA Specific Patient Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>A</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>VistA Element Name</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID - PATIENT ID (always 1) (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>60</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>REMARKS (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PLACE OF BIRTH [CITY] (Use the one passed in the PID segment—Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PLACE OF BIRTH [STATE] (Use the one passed in the PID segment—Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CURRENT MEANS TEST STATUS (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>35</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>FATHER'S NAME (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>35</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>MOTHER'S NAME (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RATED INCOMPETENT? (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE OF DEATH (use the one in the PID segment)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td>48</td>
<td>PN</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>COLLATERAL SPONSOR'S NAME (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Active Health Insurance? (Passed but not used by MPI)</p>
<p><strong>NOTE:</strong> This field comes from the Patient file (#2) looking at the values of a number of fields.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ELIGIBLE FOR MEDICAID? (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE MEDICAID LAST ASKED (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RACE (use the one in the PID segment—Passed but not used by MPI)</p>
<p><strong>NOTE:</strong> RACE is the old field, and not the RACE INFORMATION multiple.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>RELIGIOUS PREFERENCE (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Homeless Indicator (Passed but not used by MPI) name has been removed.</p>
<p><strong>NOTE:</strong> This is a computed field derived from VISTA Social Work package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>POW STATUS INDICATED?</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TYPE OF INSURANCE (Passed but not used by MPI)</p>
<p><strong>NOTE:</strong> Derived from the MAJOR CATEGORY field (#.03) in the TYPE OF PLAN file (#355.1).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA14</td>
<td><blockquote>
<p>MEDICATION COPAYMENT EXEMPTION (Passed but not used by MPI)</p>
<p><strong>NOTE:</strong> This is a computed field derived from VISTA Integrated Billing package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>20</td>
<td>22</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>POW CONFINEMENT LOCATION (Passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>21</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PRIMARY CARE TEAM</p>
<p><strong>NOTE:</strong> Derived from the NAME field (#.01) in the TEAM file (#404.51).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>22</td>
<td>3</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>GI INSURANCE POLICY? (passed but not used by MPI) – Yes, No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>23</td>
<td>10</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>AMOUNT OF GI INSURANCE (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>24</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>MOST RECENT DATE OF CARE (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>25</td>
<td>10</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>MOST RECENT LOCATION OF CARE (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>26</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>2ND MOST RECENT DATE OF CARE (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>27</td>
<td>10</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>2<sup>ND</sup> MOST RECENT LOCATION OF CARE (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>28</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE RULED INCOMPETENT (CIVIL) (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>29</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE RULED INCOMPETENT (VA) (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>30</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SPINAL CORD INJURY (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>31</td>
<td>3</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SOURCE OF NOTIFICIATION (passed but not used by MPI)</p>
<p>[1:INPATIENT AT VAMC</p>
<p>2:NON-VA MEDICAL FACILITY</p>
<p>3:DEATH CERTIFICATE ON FILE</p>
<p>4:VBA</p>
<p>5:VA INSURANCE</p>
<p>6:SSA</p>
<p>7:NCA</p>
<p>8:NEXT OF KIN/FAMILY/FRIEND</p>
<p>9:OTHER]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>32</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DATE OF DEATH LAST UPDATED (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>33</td>
<td>3</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA048</td>
<td><blockquote>
<p>FILIPINO VETERAN PROOF (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>34</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Pseudo SSN Reason –</p>
<p>'R' FOR REFUSED TO PROVIDE</p>
<p>'S' FOR SSN UNKNOWN/FOLLOW-UP REQUIRED</p>
<p>'N' FOR NO SSN ASSIGNED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>35</td>
<td>15</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA018</td>
<td><blockquote>
<p>AGENCY/ALLIED COUNTRY (passed but not used by MPI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>36-39</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>NOT DEFINED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>40</td>
<td>1</td>
<td>IS</td>
<td></td>
<td>R</td>
<td></td>
<td><blockquote>
<p>Emergency Response Indicator (Passed by not used by MPI)</p>
<p>[K: Hurricane Katrina</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc131832363" class="anchor"></span>Table ‑. ZPD―VA Specific Patient Information, HL7 attributes

ZPD Field Definition

These are the only two fields, which the MVI is pulling data. The MVI will also send the Pseudo SSN Reason out in the ZPD segment.

### ZPD-17 POW Status Indicated?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field defines the Prisoner of War status of the patient. The POW Status Indicator? value is a Yes/No field pulled from the PATIENT (#2) file, field POW STATUS INDICATED? (# .525).

### ZPD-34 PSEUDO SSN REASON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definition: This field defines reason that a pseudo SSN has been collected for the patient. Field 17 is the only field that is being taken from the ZPD segment. The PSEUDO SSN REASON value is a set of codes pulled from the PATIENT (#2) file, field PSEUDO SSN REASON (#.0906).

| R   | REFUSED TO PROVIDE                 |
|-----|------------------------------------|
| S   | FOR SSN UNKNOWN/FOLLOW-UP REQUIRED |
| N   | NO SSN ASSIGNED;                   |

<span id="_Toc3901294" class="anchor"></span>Table ‑. Possible values for PSEUDO SSN REASON

## ZSP: VA Specific Service Period Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The ZSP―VA Specific Service Period segment is passed but not used by the MPI software. However, this segment can be used by any software subscribing to the MPI messages defined in the documentation as containing this segment. This is not a required segment. It may or may not be present in all messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><blockquote>
<p><strong>VistA Element Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>SET ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td><blockquote>
<p>SERVICE CONNECTED?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>SERVICE CONNECTED PERCENTAGE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>PERIOD OF SERVICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>VIETNAM SERVICE INDICATED?</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc131832365" class="anchor"></span>Table ‑. ZSP―VA Specific Service Period, HL7 attributes

# VA HL7 Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** For information referring to Race, see "Table 3‑41. User-defined Table 0005: Race" in this documentation.

## Table VA001: Yes/No

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|           |                 |
|-----------|-----------------|
| Value | Description |
| 0         | NO              |
| 1         | YES             |

<span id="_Toc131832366" class="anchor"></span>Table 4‑1. VA001: Yes/No

## Table VA002: Current Means Test Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Type of Care (#.03) field of Means Test Status (#408.32) file.

| Value | Description                      |
|-----------|--------------------------------------|
| 0         | Exempt (LTC C0-Pay Exempt Test)      |
| 1         | Non- Exempt (LTC C0-Pay Exempt Test) |
| A         | MT COPAY EXEMPT                      |
| B         | CATEGORY B                           |
| C         | MT COPAY REQUIRED                    |
| E         | EXEMPT                               |
| G         | GMT COPAY REQUIRED                   |
| I         | INCOMPLETE                           |
| L         | NO LONGER APPLICABLE                 |
| M         | NON-EXEMPT                           |
| N         | NO LONGER REQUIRED                   |
| P         | PENDING ADJUDICATION                 |
| R         | REQUIRED                             |

<span id="_Toc131832367" class="anchor"></span>Table ‑. VA002: Current Means Test Status

## Table VA004: Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Name (#.01) field of MAS Eligibility Code (#8.1) file.

| Value | Description               |
|-----------|-------------------------------|
| 1         | SERVICE CONNECTED 50% to 100% |
| 2         | AID & ATTENDANCE              |
| 3         | SC LESS THAN 50%              |
| 4         | NSC - VA PENSION              |
| 5         | NSC                           |
| 6         | OTHER FEDERAL AGENCY          |
| 7         | ALLIED VETERAN                |
| 8         | HUMANITARIAN EMERGENCY        |
| 9         | SHARING AGREEMENT             |
| 10        | REIMBURSABLE INSURANCE        |
| 12        | CHAMPVA                       |
| 13        | COLLATERAL OF VET.            |
| 14        | EMPLOYEE                      |
| 15        | HOUSEBOUND                    |
| 16        | MEXICAN BORDER WAR            |
| 17        | WORLD WAR I                   |
| 18        | PRISONER OF WAR               |
| 19        | TRICARE/CHAMPUS               |
| 21        | CATASTROPHIC DISABILITY       |
| 22        | PURPLE HEART RECIPIENT        |
| 23        | REFUSED MT CO-PAY             |

<span id="_Toc131832368" class="anchor"></span>Table ‑. VA004: Eligibility

## Table VA005: Disability Retirement From Military

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Disability Ret. From Military? (#.362) field of Patient (#2) file.

| Value | Description                                               |
|-----------|---------------------------------------------------------------|
| 0         | NO                                                            |
| 1         | YES, RECEIVING MILITARY RETIREMENT                            |
| 2         | YES, RECEIVING MILITARY RETIREMENT IN LIEU OF VA COMPENSATION |
| 3         | UNKNOWN                                                       |

<span id="_Toc131832369" class="anchor"></span>Table ‑. VA005: Disability Retirement From Military

## Table VA006: Eligibility Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Eligibility Status (#.3611) field of Patient (#2) file.

| Value | Description         |
|-----------|-------------------------|
| P         | PENDING VERIFICATION    |
| R         | PENDING RE-VERIFICATION |
| V         | VERIFIED                |

<span id="_Toc131832370" class="anchor"></span>Table ‑. VA006: Eligibility Status

> **NOTE:** For information referring to Race, see "Table 3‑41. User-defined Table 0005: Race" in this documentation.

## Table VA008: Religion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Code (#3) field of Religion (#13) file.

| Value | Description              |
|-----------|------------------------------|
| 0         | ROMAN CATHOLIC CHURCH        |
| 1         | JUDAISM                      |
| 2         | EASTERN ORTHODOX             |
| 3         | BAPTIST                      |
| 4         | METHODIST                    |
| 5         | LUTHERAN                     |
| 6         | PRESBYTERIAN                 |
| 7         | UNITED CHURCH OF CHRIST      |
| 8         | EPISCOPALIAN                 |
| 9         | ADVENTIST                    |
| 10        | ASSEMBLY OF GOD              |
| 11        | BRETHREN                     |
| 12        | CHRISTIAN SCIENTIST          |
| 13        | CHURCH OF CHRIST             |
| 14        | CHURCH OF GOD                |
| 15        | DISCIPLES OF CHRIST          |
| 16        | EVANGELICAL COVENANT         |
| 17        | FRIENDS                      |
| 18        | JEHOVAH'S WITNESSES          |
| 19        | LATTER DAY SAINTS            |
| 20        | ISLAM                        |
| 21        | NAZARENE                     |
| 22        | OTHER                        |
| 23        | PENTECOSTAL                  |
| 24        | PROTESTANT                   |
| 25        | PROTESTANT, NO PREFERENCE    |
| 26        | REFORMED                     |
| 27        | SALVATION ARMY               |
| 28        | UNITARIAN-UNIVERSALISM       |
| 29        | UNKNOWN/NO PREFERENCE        |
| 30        | NATIVE AMERICAN              |
| 31        | ZEN BUDDHISM                 |
| 32        | AFRICAN RELIGIONS            |
| 33        | AFRO-CARIBBEAN RELIGIONS     |
| 34        | AGNOSTICISM                  |
| 35        | ANGLICAN                     |
| 36        | ANIMISM                      |
| 37        | ATHEISM                      |
| 38        | BABI & BAHA'I FAITHS         |
| 39        | BON                          |
| 40        | CAO DAI                      |
| 41        | CELTICISM                    |
| 42        | CHRISTIAN (NON-SPECIFIC)     |
| 43        | CONFUCIANISM                 |
| 44        | CONGREGATIONAL               |
| 45        | CYBERCULTURE RELIGIONS       |
| 46        | DIVINATION                   |
| 47        | FOURTH WAY                   |
| 48        | FREE DAISM                   |
| 49        | FULL GOSPEL                  |
| 50        | GNOSIS                       |
| 51        | HINDUISM                     |
| 52        | HUMANISM                     |
| 53        | INDEPENDENT                  |
| 54        | JAINISM                      |
| 55        | MAHAYANA                     |
| 56        | MEDITATION                   |
| 57        | MESSIANIC JUDAISM            |
| 58        | MITRAISM                     |
| 59        | NEW AGE                      |
| 60        | NON-ROMAN CATHOLIC           |
| 61        | OCCULT                       |
| 62        | ORTHODOX                     |
| 63        | PAGANISM                     |
| 64        | PROCESS, THE                 |
| 65        | REFORMED/PRESBYTERIAN        |
| 66        | SATANISM                     |
| 67        | SCIENTOLOGY                  |
| 68        | SHAMANISM                    |
| 69        | SHIITE (ISLAM)               |
| 70        | SHINTO                       |
| 71        | SIKISM                       |
| 72        | SPIRITUALISM                 |
| 73        | SUNNI (ISLAM)                |
| 74        | TAOISM                       |
| 75        | THERAVADA                    |
| 76        | UNIVERSAL LIFE CHURCH        |
| 77        | VAJRAYANA (TIBETAN)          |
| 78        | VEDA                         |
| 79        | VOODOO                       |
| 80        | WICCA                        |
| 81        | YAOHUSHUA                    |
| 82        | ZOROASTRIANISM               |
| 83        | ASKED BUT DECLINED TO ANSWER |

<span id="_Toc3901301" class="anchor"></span>Table ‑. VA008: Religion

## Table VA010: Means Test Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AS        | This Means Test category includes all compensable service-connected (0-100%) veterans and special category veterans. Special category veterans include: Mexican Border War and World War I veterans; former Prisoners of War; and patients receiving care for conditions potentially related to exposure to either Agent Orange (Herbicides), Ionizing Radiation or Environmental Contaminants. This category also includes 0% non-compensable service-connected veterans when they are treated for a service-connected condition.                                                                                                               |
| AN        | This Means Test category includes NSC veterans who are required to complete VA Form 10-10F (Financial Worksheet) and those NSC veterans in receipt of VA pension, aid and attendance, housebound allowance, or entitled to State Medicaid. This category may also include 0% non-compensable service-connected veterans when they are not treated for a service-connected condition and are placed in this category based on completion of a Means Test.                                                                                                                                                                                         |
| C         | This Means Test category includes those veterans who, based on income and/or net worth, are required to reimburse VA for care rendered. This category also includes those pending adjudication. This category may also include 0% non-compensable service-connected veterans when they are not treated for a service-connected condition and are placed in this category based on completion of a Means Test.                                                                                                                                                                                                                                    |
| N         | This Means Test category includes only non-veterans receiving treatment at VA facilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| X         | This Means Test category includes treatment of patients who are not required to complete the Means Test for the care being provided. If the veteran was admitted prior to July 1, 1986 with no change in the level of care being received, (i.e., if the patient was in the Nursing Home Care Unit (NHCU) on June 30, 1986 and has remained in the NHCU since that date with no transfer to the hospital for treatment), the "X" Means Test indicator will be accepted. This category also includes patients admitted to the domiciliary, patients seen for completion of a compensation and pension examination, and Class II dental treatment. |
| U         | This Means Test category includes only those patients who require a Means Test, and the Means Test has not been done/completed. The Austin Automation Center (AAC) will not accept an OPC transaction unless the Means Test has been completed.                                                                                                                                                                                                                                                                                                                                                                                                  |

<span id="_Toc131832373" class="anchor"></span>Table ‑. VA010: Means Test Indicator

## Table VA011: Period of Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description            |
|-----------|----------------------------|
| 0         | KOREAN                     |
| 1         | WORLD WAR I                |
| 2         | WORLD WAR II               |
| 3         | SPANISH AMERICAN           |
| 4         | PRE-KOREAN                 |
| 5         | POST-KOREAN                |
| 6         | OPERATION DESERT SHIELD    |
| 7         | VIETNAM ERA                |
| 8         | POST-VIETNAM               |
| 9         | OTHER OR NONE              |
| A         | ARMY - ACTIVE DUTY         |
| B         | NAVY, MARINE - ACTIVE DUTY |
| C         | AIR FORCE - ACTIVE DUTY    |
| D         | COAST GUARD - ACTIVE DUTY  |
| E         | RETIRED, UNIFORMED FORCES  |
| F         | MEDICAL REMEDIAL ENLIST    |
| G         | MERCHANT SEAMEN - USPHS    |
| H         | OTHER USPHS BENEFICIARIES  |
| I         | OBSERVATION/EXAMINATION    |
| J         | OFFICE OF WORKERS COMP     |
| K         | JOB CORPS/PEACE CORPS      |
| L         | RAILROAD RETIREMENT        |
| M         | BENEFICIARIES-FOREIGN GOV  |
| N         | HUMANITARIAN (NON-VET)     |
| O         | CHAMPUS RESTORE            |
| P         | OTHER REIMBURS. (NON-VET)  |
| Q         | OTHER FEDERAL - DEPENDENT  |
| R         | DONORS (NON-VET)           |
| S         | SPECIAL STUDIES (NON-VET)  |
| T         | OTHER NON-VETERANS         |
| U         | CHAMPVA - SPOUSE, CHILD    |
| V         | CHAMPUS                    |
| W         | CZECHOSLOVAKIA/POLAND SVC  |
| X         | PERSIAN GULF WAR           |
| Y         | CAV/NPS                    |
| Z         | MERCHANT MARINE            |

<span id="_Toc131832374" class="anchor"></span>Table ‑. VA011: Period of Service

## Table VA012: Type of Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|           |                       |
|-----------|-----------------------|
| Value | Description       |
| 0         | NO INSURANCE          |
| 1         | MAJOR MEDICAL         |
| 2         | DENTAL                |
| 3         | HMO                   |
| 4         | PPO                   |
| 5         | MEDICARE              |
| 6         | MEDICAID              |
| 7         | CHAMPUS               |
| 8         | WORKMAN COMP          |
| 9         | INDEMNITY             |
| 10        | PRESCRIPTION          |
| 11        | MEDICARE SUPPLEMENTAL |
| 12        | ALL OTHER             |

<span id="_Toc131832375" class="anchor"></span>Table ‑. VA012: Type of Insurance

## Table VA015: Enrollment Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                            |     |
|-----------|--------------------------------------------|-----|
| 1         | UNVERIFIED                                 |     |
| 2         | VERIFIED                                   |     |
| 3         | INACTIVE                                   |     |
| 4         | REJECTED                                   |     |
| 5         | SUSPENDED                                  |     |
| 6         | TERMINATED                                 |     |
| 7         | CANCELED/DECLINED                          |     |
| 8         | EXPIRED                                    |     |
| 9         | PENDING                                    |     |
| 10        | NOT ELIGIBLE                               |     |
| 11        | REJECTED; FISCAL YEAR                      |     |
| 12        | REJECTED; MID-CYCLE                        |     |
| 13        | REJECTED; STOP NEW ENROLLMENTS             |     |
| 14        | REJECTED; INITIAL APPLICATION BY VAMC      |     |
| 15        | PENDING; NO ELIGIBILITY CODE               |     |
| 16        | PENDING; MEANS TEST REQUIRED               |     |
| 17        | PENDING; ELIGIBILITY STATUS IS UNVERIFIED  |     |
| 18        | PENDING; OTHER                             |     |
| 19        | NOT ELIGIBLE; REFUSED TO PAY COPAY         |     |
| 20        | NOT ELIGIBLE; INELIGIBLE DATE              |     |
| 21        | PENDING; PURPLE HEART UNCONFIRMED          |     |
| 22        | REJECTED; BELOW ENROLLMENT GROUP THRESHOLD |     |

<span id="_Toc131832376" class="anchor"></span>Table ‑. VA015: Enrollment Status

## Table VA016: Reason Canceled/Declined

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description        |
|-----------|------------------------|
| 1         | DISSATISFIED WITH CARE |
| 2         | GEOGRAPHIC ACCESS      |
| 3         | OTHER INSURANCE        |
| 4         | OTHER                  |

<span id="_Toc131832377" class="anchor"></span>Table ‑. VA016: Reason Canceled/Declined

## Table VA021: Enrollment Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-----------|-----------------|
| 1         | Priority 1      |
| 2         | Priority 2      |
| 3         | Priority 3      |
| 4         | Priority 4      |
| 5         | Priority 5      |
| 6         | Priority 6      |
| 7         | Priority 7      |
| 8         | Priority 8      |

<span id="_Toc131832378" class="anchor"></span>Table ‑. VA021: Enrollment Priority

## Table VA022: Radiation Exposure Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description      |
|-----------|----------------------|
| 2         | Nagasaki – Hiroshima |
| 3         | Nuclear Testing      |
| 4         | Both                 |

<span id="_Toc131832379" class="anchor"></span>Table ‑. VA022: Radiation Exposure Method

## Table VA023: Prisoner of War Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description        |
|-----------|------------------------|
| 4         | WORLD WAR I            |
| 5         | WORLD WAR II – EUROPE  |
| 6         | WORLD WAR II – PACIFIC |
| 7         | KOREAN                 |
| 8         | VIETNAM                |
| 9         | OTHER                  |
| A         | PERSIAN GULF WAR       |
| B         | YUGOSLAVIA CONFLICT    |

<span id="_Toc131832380" class="anchor"></span>Table ‑. VA023: Prisoner of War Location

## Table VA024: Source of Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-----------|-----------------|
| 1         | VAMC            |
| 2         | HEC             |
| 3         | OTHER VAMC      |

<span id="_Toc131832381" class="anchor"></span>Table ‑. VA024: Source of Enrollment

## Table VA036: MST Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                  |
|-----------|----------------------------------|
| U         | UNKNOWN, NOT SCREENED            |
| Y         | YES, SCREENED REPORTS MST        |
| N         | NO, SCREENED DOES NOT REPORT MST |
| D         | SCREENED, DECLINES TO ANSWER     |

<span id="_Toc131832382" class="anchor"></span>Table ‑. VA036: MST Status

## Table VA046: Agent Orange Exposure Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-----------|-----------------|
| K         | KOREAN DMZ      |
| U         | UNKNOWN         |
| V         | VIETNAM         |

<span id="_Toc131832383" class="anchor"></span>Table ‑. VA046: Agent Orange Exposure Location

## Table NPCD 001: National Patient Care Database Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Example listing of possible values.

| Value | Description    |
|-----------|--------------------|
| 100       | Event Type Segment |
| 200       | Patient Name       |
| 205       | Date of Birth      |
| 210       | Sex                |
| 215       | Race               |

<span id="_Toc131832384" class="anchor"></span>Table ‑. NPCD 001: National Patient Care Database Error Codes

Page intentionally left blank for double-sided print copy.

<span id="_Toc131832193" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>.001 Field</strong></td>
<td><blockquote>
<p>A field containing the internal entry number of the record.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>.01 Field</strong></td>
<td><blockquote>
<p>The one field that must be present for every file and file entry. It is also called the NAME field. At a file's creation the .01 field is given the label NAME. This label can be changed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>10-10EZ</strong></td>
<td><blockquote>
<p>Form used to apply for health benefits.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>abbreviated response</strong></td>
<td><blockquote>
<p>This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>accept agreement</strong></td>
<td><blockquote>
<p>Part of the validation and agreement to the privacy regulations associated with IdM Toolkit (IdM TK).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>access code</strong></td>
<td><blockquote>
<p>A code that, along with the Verify code, allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than 6 and less than 20 characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. It is used by the Kernel's Sign-on/Security system to identify the user (see Verify Code).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ACK</strong></td>
<td><blockquote>
<p>General Acknowledgement message. The ACK message is used to respond to a message where there has been an error that precludes application processing or where the application does not define a special message type for the response.<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>acknowledgement - accept level</strong></td>
<td><blockquote>
<p>The receiving system commits the message to safe storage in a manner that releases the sending system from any obligation to resend the message. A response is returned to the initiator indicating successful receipt and secure storage of the information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>acknowledgement - application level</strong></td>
<td><blockquote>
<p>The appropriate application on the receiving system receives the transaction and processes it successfully. The receiving system returns an application-dependent response to the initiator.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>active patients</strong></td>
<td><blockquote>
<p>Patients who have been seen at a site within the past three years.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ADPAC</strong></td>
<td><blockquote>
<p>Automated Data Processing Application Coordinator.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ADR</strong></td>
<td><blockquote>
<p>The Administrative Data Repository is the authoritative data store within VHA for cross-cutting person administrative information. The Administrative Data Repository contains identification and cross-cutting demographics data as well as other administrative information. Patient Information Management System (PSIM) uploads the identity demographic data to the ADR. May also include subset of the Enrollment database. May also be referred to as ADR-N or ADR-L to designate a national or local instance.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ADT</strong></td>
<td><blockquote>
<p>Admission Discharge and Transfer- Part of the Patient Information Management System (PIMS).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ADT/HL7 PIVOT File</strong></td>
<td><blockquote>
<p>Changes to any of the fields of person information will be recorded and an entry created in the ADT/HL7 PIVOT file (#391.71). When an update to a person's treating facility occurs, this event is to be added to the ADT/HL7 PIVOT file (#391.71) and marked for transmission. A background job will collect these updates and broadcast the appropriate HL7 message (ADT-A08 Patient Update).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>AITC</strong></td>
<td><blockquote>
<p>The Master Veteran Index (MVI) is located at the Austin Information Technology Center (AITC).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>alerts</strong></td>
<td><blockquote>
<p>Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient's clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ancillary reviewer</strong></td>
<td><blockquote>
<p>This can be a single person or group of people given the responsibility to conduct reviews of potential duplicate record pairs with data in files other than the PATIENT file (#2). For example, selected personnel in Laboratory, Radiology, and Pharmacy.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ANSI</strong></td>
<td><blockquote>
<p>American National Standards Institute.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ANSI M</strong></td>
<td><blockquote>
<p>The M (formerly known as MUMPS) programming language is a standard recognized by the American National Standard Institute (ANSI). M stands for Massachusetts Utility Multi-programming System.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>API</strong></td>
<td><blockquote>
<p>Program calls provided for use by application programmers. APIs allow programmers to carry out standard computing activities without needing to duplicate utilities in their own software. APIs also further DBA goals of system integration by channeling activities, such as adding new users, through a limited number of callable entry points. VistA APIs fall into the following three categories:</p>
</blockquote>
<ul>
<li><p>The first category is "Supported API" These are callable routines, which are supported for general use by all VistA applications.</p></li>
<li><p>The second category is "Controlled Subscription API." These are callable routines for which you must obtain an Integration Agreement (IA - formerly referred to as a DBIA) to use.</p></li>
<li><p>The third category is "Private API," where only a single application is granted permission to use an attribute/function of another VistA package.</p></li>
<li><p>These IAs are granted for special cases, transitional problems between versions, and release coordination.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>application</strong></td>
<td><blockquote>
<p>Any software that executes logic or rules which allow people to interface with the computer and programs which collect, manipulate, summarize, and report data and information. .</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>application coordinator</strong></td>
<td><blockquote>
<p>Designated individuals responsible for user-level management and maintenance of an application package such as IFCAP, Lab, Pharmacy, Mental Health, etc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>application programmer interface (API)</strong></td>
<td><blockquote>
<p>Program calls provided for use by application programmers. APIs allow programmers to carry out standard computing activities without needing to duplicate utilities in their own software. APIs also further DBA goals of system integration by channeling activities, such as adding new users, through a limited number of callable entry points.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>application server</strong></td>
<td><blockquote>
<p>Software/hardware for handling complex interactions between users, business logic, and databases in transaction-based, multi-tier applications. Application servers, also known as app servers, provide increased availability and higher performance.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>array</strong></td>
<td><blockquote>
<p>An arrangement of elements in one or more dimensions. An M array is a set of nodes referenced by subscripts that share the same variable name.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>asynchronous</strong></td>
<td><blockquote>
<p>Without regular time relationship; unexpected or unpredictable with respect to the execution of a program's instructions; a physical transfer of data to or from a device that occurs without a regular or predictable time relationship. Contrast with synchronous.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Asynchronous Transfer Mode (ATM)</strong></td>
<td><blockquote>
<p>A high-speed connection-oriented data transmission method that provides bandwidth on demand through packet-switching techniques using fixed-sized cells. ATM supports both time-sensitive and time-insensitive traffic, and is defined in CCITT standards as the transport method for B-ISDN services. Cell-switching technology that operates at high data rates: up to 622 Mbps currently, but potential data rates could reach Gbps. ATM runs on an optical fiber network that uses Synchronous Optical Network (SONET) protocols for moving data between ATM switches.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>at-sign ("@")</strong></td>
<td><blockquote>
<p>A VA FileMan security Access code that gives the user programmer-level access to files and to VA FileMan's developer features. See Programmer Access. Also, the character "@" (i.e., at-sign, Shift-2 key on most keyboards) is used at VA FileMan field prompts to delete data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>attribute</strong></td>
<td><blockquote>
<p>VHA Definition:</p>
</blockquote>
<ul>
<li><p>These are Persons Traits or Meta-Data about the Primary View or the Correlation.</p></li>
</ul>
<blockquote>
<p>Identity Hub™ Definition:</p>
</blockquote>
<ul>
<li><p>Members have attributes, like Name, Gender, Address, Phone, Birth Date, SSN.</p></li>
<li><p>Attributes are stored in tables according to Segments. Segments are “attribute types” The MEMPHONE segment can hold Home Phone, Cell Phone, and Fax Number information.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>authentication</strong></td>
<td><blockquote>
<p>Verifying the identity of the end-user.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>authorization</strong></td>
<td><blockquote>
<p>Granting or denying user access or permission to perform a function.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Auto Link Threshold or Threshold, Auto Link</strong></td>
<td><blockquote>
<p>The Auto Link Threshold is the level that a Comparison Score must meet or exceed in order for two or more Identity Profiles to be considered the same unique Person Identity.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>auto-update</strong></td>
<td><blockquote>
<p>The term "auto-update" refers to fields that are updated from a central database (i.e., the Master Veteran Index).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Bad Address Indicator (BAI)</strong></td>
<td><blockquote>
<p>The Bad Address Indicator field applies to the address at which the person resides. This field should be set as follows (if applicable):</p>
</blockquote>
<ul>
<li><p>"UNDELIVERABLE" - Bad Address based on returned mail.</p></li>
<li><p>"HOMELESS" - Patient is known to be homeless.</p></li>
<li><p>"OTHER" - Other Bad Address Reason</p></li>
</ul>
<blockquote>
<p>Setting this field will prevent a Bad Address from being shared with HEC and other VAMC facilities. It will also be used to block Means Test Renewal Letters from being sent. Once the Bad Address Indicator is set, incoming “newer" addresses will automatically remove the Bad Address Indicator, and allow the "updated" address to be transmitted to HEC and other VAMC Facilities.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>batch acknowledgements</strong></td>
<td><blockquote>
<p>The format of a HL7 batch acknowledgement message consists entirely of a group of ACK (acknowledgment) messages. In the case of MVI, batch acknowledgements are returned during the initialization process and during the Local/Missing ICN Resolution job. The background job files the ICN, updates the MVI, and then the associated treating facilities and systems. Data returned from this process constitute the acknowledgment of the batch message.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>batch messages</strong></td>
<td><blockquote>
<p>There are instances when it is convenient to transfer a batch of HL7 messages. Common examples related to MVI are queries sent to the MVI for an ICN during the initialization process, the resolution of Local or Missing ICNs, and. Such a batch could be sent online using a common file transfer protocol. In the case of the MVI, the HL7 Batch Protocol uses the Batch Header Segment (BHS) and Batch Trailer Segment (BTS) message segments to delineate the batch.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>batch protocol, Hl7</strong></td>
<td><blockquote>
<p>The protocol generally uses File Header Segment (FHS), BHS, BTS, and File Trailer Segment (FTS) segments to delineate the batch. In the case of the MPI, the protocol only uses the BHS and BTS segments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>BHIE</strong></td>
<td><blockquote>
<p>Bidirectional Health Information Exchange (<a href="http://vaww.oed.portal.va.gov/products/vler/FIST/BHIE/default.aspx">Bidirectional Health Information Exchange (BHIE</a><br />
<em><strong>NOTE:</strong> This is an internal VA Web site and is not available to the public.</em> )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>bulletins</strong></td>
<td><blockquote>
<p>Electronic mail messages that are automatically delivered by VistA MailMan under certain conditions. For example, a bulletin can be set up to "fire" when database changes occur, such as adding a new Institution in the INSTITUTION file (#4). Bulletins are fired by bulletin-type cross-references.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>business requirements</strong></td>
<td><ul>
<li><blockquote>
<p>Requirements state the customer needs the project output will satisfy. Requirements typically start with phrase “The system shall …” Business requirements refers to how the project will satisfy the business mission of the customer.</p>
</blockquote></li>
<li><blockquote>
<p>Business requirements refer to business functions of the project, such as project management, financial management, or change management.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>business rule</strong></td>
<td><ul>
<li><blockquote>
<p>A policy imposed by the business, or an external entity, on the system used in the process of conducting that business.</p>
</blockquote></li>
<li><blockquote>
<p>A special category of a requirement. A business rule is directive, policy, or procedure within an organization that describes the relationship between two or more entities. Business rules may also come from outside sources such as government regulations and membership association guidelines.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Cache</strong></td>
<td><blockquote>
<p>Cache memory is a small area of very fast RAM used to speed exchange of data. Also, a file or directory included on your computer's hard drive which automatically stores the text and graphics from a web page you pull up, which, in turn, allows you to go back to that web page, without having to wait for the information to reload.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>CAIP</strong></td>
<td><blockquote>
<p>Cross-Application Integration Protocol. A framework which provides both applications and services with support for software procedure calls across systems and applications that rely upon infrastructure and middleware technologies, while simultaneously minimizing the direct dependencies of these same applications and services upon these enabling technologies.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>callable entry point</strong></td>
<td><blockquote>
<p>An authorized programmer call that may be used in any VistA application package. The DBA maintains the list of DBIC-approved entry points.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>CAPRI</strong></td>
<td><blockquote>
<p>Compensation &amp; Pension Records Interchange (CAPRI). This Graphical User Interface (GUI) software is used to access veterans’ electronic medical records throughout the VA. The Healthcare Identity Management (HC IdM) Team uses CAPRI as a resource for reviewing patient demographic and clinical data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>catastrophic edit</strong></td>
<td><blockquote>
<p>Changes that occur to two or more of the specified set of identity traits during an edit of a person's record.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>CE</strong></td>
<td><blockquote>
<p>Coded Element data type. This data type transmits codes and the text associated with the code. This type has six components, as follows: identifier, text, name of coding system, alternate identifier, alternate text, and name of alternate coding system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>CHDR</strong></td>
<td><blockquote>
<p>Clinical Data Repository (CDR) Health Data Repository</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Checksum</strong></td>
<td><blockquote>
<p>The result of a mathematical computation involving the individual characters of a routine or file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>client</strong></td>
<td><blockquote>
<p>A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. In an object-oriented environment, a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Clinical Patient Record System (CPRS)</strong></td>
<td><blockquote>
<p>Clinical Patient Record System provides a computer-based person record and organizes and presents all relevant data on a person in a way that directly supports clinical decision-making. CPRS integrates the extensive set of clinical and administrative applications available within VistA.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>CM</strong></td>
<td><blockquote>
<p>Composite data type. A field that is a combination of other meaningful data fields. Each portion is called a component.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>common menu</strong></td>
<td><blockquote>
<p>The Common menu consists of options that are available to all users. Entering two question marks at the menus select prompt displays any secondary menu options available to the signed-on user, along with the common options available to all users.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>component separator</strong></td>
<td><blockquote>
<p>The component separator is used to separate adjacent components of some data fields. Its use is described in the descriptions of the relevant data fields. The character that represents the component separator is specified for each message as the first character in the Encoding Characters data field of the MSH segment. Absent other considerations it is recommended that all sending applications use "^"as the component separator. However, all applications are required to accept whatever character is included in the Message Header and use it to parse the message.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>controlled subscription integration agreement</strong></td>
<td><blockquote>
<p>This applies where the IA describes attributes/functions that must be controlled in their use. The decision to restrict the IA is based on the maturity of the custodian package. Typically, these IAs are created by the requesting package based on their independent examination of the custodian package's features. For the IA to be approved, the custodian grants permission to other VistA packages to use the attributes/functions of the IA; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package. An example is the extension of permission to allow a package (e.g., Spinal Cord Dysfunction) to define and update a component that is supported within the Health Summary package file structures.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>correlation</strong></td>
<td><blockquote>
<p>Comparison of person identity traits for multiple records with the Primary View in the ADR and/or MVI databases.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>COTS</strong></td>
<td><blockquote>
<p>Commercial Off The Shelf applications sold by vendors through public catalogue listings. COTS software is not intended to be customized or enhanced.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>CQ</strong></td>
<td><blockquote>
<p>Composite Quantity with Units data type. The first component is a quantity and the second is the units in which the quantity is expressed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>cross reference</strong></td>
<td><blockquote>
<p>There are several types of cross-references available. Most generally, a VA FileMan cross-reference specifies that some action be performed when the field's value is entered, changed, or deleted. For several types of cross-references, the action consists of putting the value into a list; an index used when looking-up an entry or when sorting. The regular cross-reference is used for sorting and for lookup; you can limit it to sorting only.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>data attribute</strong></td>
<td><blockquote>
<p>A characteristic unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>data dictionary (DD)</strong></td>
<td><blockquote>
<p>The Data Dictionary is a global containing a description of the kind of data that is stored in the global corresponding to a particular file. VA FileMan uses the data internally for interpreting and processing files.</p>
<p>It contains the definitions of a file's elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file's elements or data attributes; programmers review the definitions of a file's internal structure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>data dictionary access</strong></td>
<td><blockquote>
<p>A user's authorization to write/update/edit the data definition for a computer file. Also known as DD Access.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>data integrity</strong></td>
<td><blockquote>
<p>This term refers to the condition of patient records in terms of completeness and correctness. It also refers to the process in which a particular patient’s data is synchronized at all the sites in which that person receives care.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>data type</strong></td>
<td><blockquote>
<p>A specific field or type of information, such as Name, Social Security Number, etc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>database</strong></td>
<td><blockquote>
<p>A set of data, consisting of at least one file, that is sufficient for a given purpose. The VistA database is composed of a number of VA FileMan files. A collection of data about a specific subject, such as the PATIENT file (#2); a data collection has different data fields (e.g. patient name, SSN, Date of Birth, and so on). An organized collection of data about a particular topic.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>database management system (DBMS)</strong></td>
<td><blockquote>
<p>A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Date of Death</strong></td>
<td><blockquote>
<p>A person may be entered as deceased at a treating facility. If a shared patient is flagged as deceased, an RG CIRN DEMOGRAPHIC ISSUES bulletin is sent to each treating facility telling where, when, and by whom the deceased date was entered. Each site can then review whether the patient should be marked as deceased at their site.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>DBA</strong></td>
<td><blockquote>
<p>Database Administrator, oversees software development with respect to VistA Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>DBIA</strong></td>
<td><blockquote>
<p>Database Integration Agreement (see Integration Agreements [IA]).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>default</strong></td>
<td><blockquote>
<p>Response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the Enter (or Return) key. To change the default answer, type in your response.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>delimiter</strong></td>
<td><blockquote>
<p>Special character used to separate a field, record, or string. VA FileMan uses the caret character ("^") as the delimiter within strings.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>demographic data</strong></td>
<td><blockquote>
<p>Identifying descriptive data about a person, such as: name, sex, date of birth, marital status, religious preference, SSN, address, etc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>demographics</strong></td>
<td><blockquote>
<p>Information about a person, such as name, address, service record, next of kin, and so on.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Department of Veterans Affairs</strong></td>
<td><blockquote>
<p>The Department of Veterans Affairs (formerly known as the Veterans Administration.)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>device</strong></td>
<td><blockquote>
<p>Peripheral connected to the host computer, such as a printer, terminal, disk drive, modem, and other types of hardware and equipment associated with a computer. The host files of underlying operating systems may be treated like devices in that they may be written to (e.g., for spooling).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>DFN</strong></td>
<td><blockquote>
<p>Data File Number. This is the patient <a href="http://vaww.vista.med.va.gov/iss/acronyms/i-acronyms.asp#ien">IEN</a> (.001 Field) in the PATIENT file (#2). Additionally, this is a defined variable in VistA that refers to the IEN of the patient currently in memory.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>dictionary</strong></td>
<td><blockquote>
<p>Database of specifications of data and information processing resources. VA FileMan's database of data dictionaries is stored in the FILE of files (#1).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Direct Connect</strong></td>
<td><blockquote>
<p>The Direct Connect is a real-time TCP/IP connection to the MPI to allow for an immediate request for an ICN. Direct Connect is activated when using any of the following PIMS options:</p>
</blockquote>
<ul>
<li><p>Register A Patient,</p></li>
<li><p>Load/Edit Patient Data,</p></li>
<li><p>Electronic 10-10EZ Processing,</p></li>
</ul>
<blockquote>
<p>and when using the:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Display Only Query</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>direct mode utility</strong></td>
<td><blockquote>
<p>A programmer call that is made when working in direct programmer mode. A direct mode utility is entered at the MUMPS prompt (e.g., &gt;D ^XUP). Calls that are documented as direct mode utilities cannot be used in application software code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>DNS</strong></td>
<td><blockquote>
<p>Domain Name Server</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>DOB</strong></td>
<td><blockquote>
<p>Date of Birth</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>DOD</strong></td>
<td><blockquote>
<p>IdM– Date of Death</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>DoD</strong></td>
<td><blockquote>
<p>Department of Defense.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>domain</strong></td>
<td><blockquote>
<p>A site for sending and receiving mail.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>double quotes ("")</strong></td>
<td><blockquote>
<p>Symbol used in front of a Common option's menu text or synonym to select it from the Common menu. For example, the five-character string "TBOX" selects the User's Toolbox Common option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Duplicate Record Merge: Patient Merge</strong></td>
<td><blockquote>
<p>Patient Merge is a VistA application that provides an automated method to eliminate duplicate patient records within the VistA database (i.e., the VistA PATIENT file [#2]).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>DUZ</strong></td>
<td><blockquote>
<p>Locally defined variable in VistA that refers to the IEN of the logged on user (From the New Person file).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>DUZ(0)</strong></td>
<td><blockquote>
<p>Locally defined variable that holds the File Manager Access Code of the signed-on user.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>electronic signature code</strong></td>
<td><blockquote>
<p>Secret password that some users may need to establish in order to sign documents via the computer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>eligibility codes</strong></td>
<td><blockquote>
<p>Codes representing the basis of a patient's eligibility for care.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>encryption</strong></td>
<td><blockquote>
<p>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional, that is, they only encode and the resulting data cannot be unscrambled (e.g. access/verify codes).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>entry</strong></td>
<td><blockquote>
<p>VA FileMan record. An internal entry number (IEN, the .001 field) uniquely identifies an entry in a file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>error trap</strong></td>
<td><blockquote>
<p>A mechanism to capture system errors and record facts about the computing context such as the local symbol table, last global reference, and routine in use. Operating systems provide tools such as the %ER utility. The Kernel provides a generic error trapping mechanism with use of the ^%ZTER global and ^XTER* routines. Errors can be trapped and, when possible, the user is returned to the menu system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ESR</strong></td>
<td><blockquote>
<p>Enrollment Systems Redesign is a centralized and Reengineered enrollment system.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>event type</strong></td>
<td><blockquote>
<p>Type of HL7 message generated (i.e., ADT-A24, ADT-A28).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>exception</strong></td>
<td><blockquote>
<p>A task that has encountered an error in personal data. Any Data Quality issue that requires detailed documentation. HC IdM finds an Exception based on business rules.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>extrinsic function</strong></td>
<td><blockquote>
<p>Extrinsic function is an expression that accepts parameters as input and returns a value as output that can be directly assigned.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>facility</strong></td>
<td><blockquote>
<p>Geographic location at which VA business is performed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>FHIE</strong></td>
<td><blockquote>
<p>Federal Health Information Exchange – A Federal IT health care initiative that facilitates the secure electronic one-way exchange of patient medical information between Government health organizations.</p>
<p>The project participants are the Department of Defense (DoD) and the Department of Veterans Affairs (VA). (<a href="http://vaww.va.gov/FHIE-BHIE/">BHIE Intranet Site</a><br />
<em><strong>NOTE:</strong> This is an internal VA Web site and is not available to the public.</em>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>field</strong></td>
<td><blockquote>
<p>HL7: An HL7 field is a string of characters defined by one of the HL7 data types.<br />
<br />
VistA: In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file's data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>field components</strong></td>
<td><blockquote>
<p>A field entry may also have discernible parts or components. For example, the person's name is recorded as last name, first name, and middle initial, each of which is a distinct entity separated by a component delimiter (sub-subfield in ASTM e1238-94).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>field separator</strong></td>
<td><blockquote>
<p>The HL7 field separator separates two adjacent data fields within an HL7 segment. It also separates the segment ID from the first data field in the segment. The value that represents the field separator may be defined differently for each message. Whatever character is the fourth character of the MSH segment serves as the field separator for all segments in the message. Absent other considerations, it is recommended that all sending applications use "|" as the field separator. However, all receiving applications are required to accept whatever character is included in this position and use it to parse the message.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>file</strong></td>
<td><blockquote>
<p>Set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>File Manager (VA FileMan)</strong></td>
<td><blockquote>
<p>VistA's Database Management System (DBMS). The central component of Kernel that defines the way standard VistA files are structured and manipulated.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>FIN</strong></td>
<td><blockquote>
<p>Foreign ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>FIPS</strong></td>
<td><blockquote>
<p>Standards published by the U.S. National Institute of Standards and Technology, after approval by the Department of Commerce; used as a guideline for federal procurements.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>FOIA</strong></td>
<td><blockquote>
<p>Freedom of Information Act</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>FORUM</strong></td>
<td><blockquote>
<p>The central E-mail system within VistA. Developers use FORUM to communicate at a national level about programming and other issues. FORUM is located at the OI Field Office—Washington, DC (162-2).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>free text</strong></td>
<td><blockquote>
<p>A DATA TYPE that can contain any printable characters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>FT</strong></td>
<td><blockquote>
<p>Formatted Text data type. This data type is derived from the string data type by allowing the addition of embedded formatting instructions. These instructions are limited to those that are intrinsic and independent of the circumstances under which the field is to be displayed, FT supports width-independent and device-independent text display.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>FTP</strong></td>
<td><blockquote>
<p>File Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>function point count (FPC)</strong></td>
<td><blockquote>
<p>The function point method is used to establish a meaningful unit-of-work measure and can be used to establish baseline costs and performance level monitors. Function point analysis centers on its ability to measure the size of any software deliverable in logical, user-oriented terms. Rather than counting lines of code, function point analysis measures the functionality being delivered to the end user.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>GAL</strong></td>
<td><blockquote>
<p>Global Address List.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Gender</strong></td>
<td><blockquote>
<p>The following are listed in Legacy Vista as Standard Gender values:</p>
</blockquote>
<ul>
<li><blockquote>
<p>F – Female</p>
</blockquote></li>
<li><blockquote>
<p>M – Male</p>
</blockquote></li>
</ul>
<blockquote>
<p>SDS table Values:</p>
</blockquote>
<ul>
<li><blockquote>
<p>F – Female</p>
</blockquote></li>
<li><blockquote>
<p>M – Male</p>
</blockquote></li>
<li><blockquote>
<p>A – Ambiguous</p>
</blockquote></li>
<li><blockquote>
<p>N – Not Applicable</p>
</blockquote></li>
<li><blockquote>
<p>O - Other</p>
</blockquote></li>
<li><blockquote>
<p>U – Unknown</p>
</blockquote></li>
<li><blockquote>
<p>UN – Undifferentiated</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>global variable</strong></td>
<td><blockquote>
<p>Variable that is stored on disk (M usage).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>GUI</strong></td>
<td><blockquote>
<p>Graphical User Interface.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>HC IdM</strong></td>
<td><blockquote>
<p>Healthcare Identity Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HD</strong></td>
<td><blockquote>
<p>Hierarchic Designator data type.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>HDR</strong></td>
<td><blockquote>
<p>Health Data Repository – A repository of clinical information normally residing on one or more independent platforms for use by clinicians and other personnel in support of patient-centric care. The data is retrieved from heritage, transaction-oriented systems and is organized in a format to support clinical decision-making in support of patient care. Formerly known as Clinical Data Repository.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Health Level 7 (HL7) Batch Protocol</strong></td>
<td><blockquote>
<p>Protocol utilized to transmit a batch of HL7 messages. The protocol generally uses FHS, BHS, BTS and FTS segments to delineate the batch. In the case of the MPI, the protocol only uses the BHS and BTS segments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Health Level Seven (HL7)</strong></td>
<td><blockquote>
<p>National standard for electronic data exchange/messaging protocol. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Health Level Seven (HL7) VistA</strong></td>
<td><blockquote>
<p>Messaging system developed as VistA software that follows the HL7 Standard for data exchange.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Healthcare Identity Management (HC IdM)</strong></td>
<td><blockquote>
<p>The Healthcare Identity Management team (formerly the Identity Management Data Quality team)</p>
</blockquote>
<ul>
<li><blockquote>
<p>Serves as business steward for person identity data for the person's electronic health record (such as name, SSN, date of birth, gender, mother’s maiden name, place of birth) as well as managing the person's longitudinal health record across the enterprise.</p>
</blockquote></li>
<li><blockquote>
<p>Defines business rules and processes governing healthcare identity management data collection and maintenance.</p>
</blockquote></li>
<li><blockquote>
<p>Monitors and resolves data integrity issues and conflicts on the MVI and local systems related to the individual’s identity data within their health record, including the resolution of duplicates, mismatches and catastrophic edits to person identity, which affect person care and safety.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>HealtheVet-VistA</strong></td>
<td><blockquote>
<p>The next generation of VistA, HealtheVet-VistA, will retain all of the capabilities of legacy VistA but will provide enhanced flexibility for future health care and compliance with the One VA Enterprise Architecture. It will allow seamless data sharing between all parts of VA to benefit veterans and their families.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>HEC</strong></td>
<td><blockquote>
<p>Health Eligibility Center.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Help Frames</strong></td>
<td><blockquote>
<p>Entries in the HELP FRAME file (#9.2) that can be distributed with application packages to provide online documentation. Frames can be linked with other related frames to form a nested structure.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Help Prompt</strong></td>
<td><blockquote>
<p>The brief help that is available at the field level when entering one or more question marks.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HINQ</strong></td>
<td><blockquote>
<p>Hospital Inquiry- The HINQ module provides the capability to request and obtain veteran eligibility data via the VA national telecommunications network. Individual or group requests are sent from a local computer to a remote Veterans Benefits Administration (VBA) computer where veteran information is stored. The VBA network that supports HINQ is composed of four computer systems located in regional VA payment centers.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>HIPAA</strong></td>
<td><blockquote>
<p>Health Insurance Portability and Accountability Act – A law passed by Congress in 1996 that requires the Department of Health and Human Services to implement regulations that will require the use of specific standards related to health care claims, code sets, identifiers (individual, provider, employer, and health plan), and security. Protects the privacy of individually identifiable health information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7</strong></td>
<td><blockquote>
<p>Health Level 7 – National standard for electronic data exchange/messaging protocol. A standards organization primarily focused on message-oriented middleware for healthcare. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>HLO</strong></td>
<td><blockquote>
<p>HL7 Optimized. VistA HL7 package routines.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ICN</strong></td>
<td><blockquote>
<p>Persons are assigned a unique identifier, Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to patients when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ID</strong></td>
<td><blockquote>
<p>Coded Value data type. The value of such a field follows the formatting rules for a ST field except that it is drawn from a table of legal values. Examples of ID fields include religion and sex.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ID State</strong></td>
<td><blockquote>
<p>An attribute of the ICN, which describes the state of the record as Permanent, Temporary, or Deactivated. ID State is composed of the following two fields from the MPI VETERAN/CLIENT file (#985):</p>
</blockquote>
<ul>
<li><blockquote>
<p>ID STATE (#80) is a set of codes: PERMANENT, TEMPORARY, and DEACTIVATED. Auditing is enabled for this field.</p>
</blockquote></li>
<li><blockquote>
<p>DATE OF ID STATE (#81) identifies when the ID STATE field was last updated.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Identity Management Toolkit (IdM TK)</strong></td>
<td><blockquote>
<p>The User Interface for the HealthCare Identity Management team. The IdM Toolkit will provide functionality to allow HC IdM staff to search and view identity and exception information. This includes the ability to view the Primary View record and any associated correlations, correlation data, history, audit trails, and HC IdM Tasks captured by PSIM and MPI. In addition, functionality is provided to support the re-hosting transition for a side-by-side comparison of ADR and MPI information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Identity Services</strong></td>
<td><blockquote>
<p>A business and data service that provides a consistent interface for access and maintenance of person identification to trusted client applications and services. It is the authoritative source for person identification in the Veterans Health Administration (VHA) domain.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>IdM</strong></td>
<td><blockquote>
<p>Identity Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>IdM TK</strong></td>
<td><blockquote>
<p>Toolkit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>IdM Toolkit (IdM TK) Administrator</strong></td>
<td><blockquote>
<p>An IdM Toolkit Administrator is a user with additional privileges and security beyond the IdM Toolkit User's available functionality in the system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>IEN</strong></td>
<td><blockquote>
<p>Internal Entry Number. The IEN number and Station Number comprise the Source ID of the person targeted for the search. The Source ID is used to uniquely identify a person.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Initiate Identity Hub™</strong></td>
<td><blockquote>
<p>The Initiate Identity Hub™ is a third-party proprietary off-the-shelf software package that makes use of a Probabilistic Matching Algorithm.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Initiate Identity<br />
Hub</strong></td>
<td><blockquote>
<p>Initiate Systems Inc. software that provides a trusted on-demand system of record for multiple organizations or other entities by accurately identifying the relevant duplicate and fragmented records and linking them – within, as well as across, all data sources</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>input template</strong></td>
<td><blockquote>
<p>A pre-defined list of fields that together comprise an editing session.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Institution</strong></td>
<td><blockquote>
<p>A Department of Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Integration Agreements (IA)</strong></td>
<td><blockquote>
<p>Integration Agreements define agreements between two or more VistA software applications to allow access to one development domain by another. VistA software developers are allowed to use internal entry points (APIs) or other software-specific features that are not available to the general programming public. Any software developed for use in the VistA environment is required to adhere to this standard; as such, it applies to vendor products developed within the boundaries of DBA assigned development domains (e.g., MUMPS AudioFax). An IA defines the attributes and functions that specify access. The DBA maintains and records all IAs in the Integration Agreement database on FORUM. Content can be viewed using the DBA menu or the Health Systems Design &amp; Development's Web page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Integration Control Number (ICN)</strong></td>
<td><blockquote>
<p>Persons are assigned a unique identifier, known as an Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to persons when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>internal entry number (IEN)</strong></td>
<td><blockquote>
<p>The number used to identify an entry within a file. Every record has a unique internal entry number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>IP</strong></td>
<td><blockquote>
<p>Integration Point</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>IRM</strong></td>
<td><blockquote>
<p>Information Resource Management. A service at VA medical centers responsible for computer management and system security.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>IS</strong></td>
<td><blockquote>
<p>Coded value for user defined table's data type.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ISO</strong></td>
<td><blockquote>
<p>Information Security Officer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ISS</strong></td>
<td><blockquote>
<p>Infrastructure and Security Services (now known as Common Services Security Program).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>IV&amp;V</strong></td>
<td><blockquote>
<p>IV&amp;V is the principal activity that oversees the successful implementation and execution of all internal control processes for financial and interfacing systems.</p>
<p>In order to ensure overall systems integrity, IV&amp;V is accomplished organizationally independent from the elements that acquire, design, develop or maintain the system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Kernel</strong></td>
<td><blockquote>
<p>VistA software that functions as an intermediary between the host operating system and other VistA software applications so that VistA software can coexist in a standard operating-system-independent computing environment. Kernel provides a standard and consistent user and programmer interface between software applications and the underlying M implementation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>LAN</strong></td>
<td><blockquote>
<p>Local Area Network.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>LAYGO Access</strong></td>
<td><blockquote>
<p>A user's authorization to create a new entry when editing a computer file. (Learn As You GO allows you the ability to create new file entries.)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>LDAP</strong></td>
<td><blockquote>
<p>Lightweight Directory Access Protocol.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Lookup</strong></td>
<td><blockquote>
<p>To find an entry in a file using a value for one of its fields.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>M (ANSI Standard)</strong></td>
<td><blockquote>
<p>Massachusetts General Hospital Utility Multi-Programming System (M, formerly named MUMPS). The Mumps language originated in the mid-60's at the Massachusetts General Hospital. Although most implementations are proprietary, consolidated into the hands of a small number of companies, an open source version of the language has been developed which is distributed freely under the GNU GPL and LGPL licenses.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>mail message</strong></td>
<td><blockquote>
<p>An entry in the MESSAGE file (#3.9). The VistA electronic mail system (MailMan) supports local and remote networking of messages.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Mailman</strong></td>
<td><blockquote>
<p>VistA software that provides a mechanism for handling electronic communication, whether it's user-oriented mail messages, automatic firing of bulletins, or initiation of server-handled data transmissions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>manager account</strong></td>
<td><blockquote>
<p>UCI that can be referenced by non-manager accounts such as production accounts. Like a library, the MGR UCI holds percent routines and globals (e.g., ^%ZOSF) for shared use by other UCIs.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>mandatory field</strong></td>
<td><blockquote>
<p>Field that requires a value. A null response is not valid.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>master files</strong></td>
<td><blockquote>
<p>A set of common reference files used by one or more application systems. These common reference files need to be synchronized across the various applications at a given site. The Master Files Notification transactions provide a way of maintaining this synchronization.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Master Patient Index (Austin) or MPI Austin</strong></td>
<td><blockquote>
<p>The MPI is a separate computer system located at the Austin Information Technology Center. It maintains a record for VA patients and stores data such as a unique patient identifier and Treating Facility lists (which tracks the sites where that ICN is known).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Master Patient Index or MPI</strong></td>
<td><blockquote>
<p>Master Patient Index is a cross-reference or index of patients that includes the patient’s related identifiers and other patient identifying information. It is used to associate a patient’s identifiers among multiple ID-assigning entities, possibly including a Health Data Repository, to support the consolidation and sharing of a patient’s health care information across VHA. The MPI is the authoritative source for patient identity.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Master Patient Index/Patient Demographics (MPI/PD) VistA or MPI/PD</strong></td>
<td><blockquote>
<p>Master Patient Index/Patient Demographics (MPI/PD) software initializes entries in the PATIENT file (#2) with the Master Patient Index, itself. The initialization process assigns an Integration Control Number (ICN), Coordinating Master of Record (CMOR), and creates a Treating Facility list of all sites at which the patient has received care. This information is then updated in the PATIENT file (#2) at all sites where the patient has been treated.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Master Veteran Index or MVI</strong></td>
<td><blockquote>
<p>The authoritative source for person identity data. Maintains identity data for persons across VA systems. Provides a unique universal identifier for each person. Stores identity data as correlations for each system where a person is known. Provides a probabilistic matching algorithm. (Includes MPI, PSIM, and IdM TK) Maintains a “gold copy” known as a “Primary View” of the person’s identity data. Broadcasts identity trait updates to systems of interest. Maintains a record locator service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>match threshold</strong></td>
<td><blockquote>
<p>The Match Threshold is the level at which an Identity Profile must score against a set of identity traits in order to be considered a match. For most enterprise applications the Match Threshold would be set at or near the Auto Link Threshold. Internal Identity Management Systems (MPI/PSIM) may use a lower score, perhaps the Task Threshold, as a Match Threshold for identity management decision processes.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>menu</strong></td>
<td><blockquote>
<p>List of choices for computing activity. A menu is a type of option designed to identify a series of items (other options) for presentation to the user for selection. When displayed, menu-type options are preceded by the word "Select" and followed by the word "option" as in Select Menu Management option: (the menu's select prompt).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>menu system</strong></td>
<td><blockquote>
<p>The overall Menu Manager logic as it functions within the Kernel framework.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>menu text</strong></td>
<td><blockquote>
<p>The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User's Toolbox is the menu text of the XUSERTOOLS option. The option's synonym is TBOX.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>message</strong></td>
<td><blockquote>
<p>A message is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example, the ADT Message type is used to transmit portions of a patient's ADT data from one system to another. A three-character code contained within each message identifies its type.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>message delimiters</strong></td>
<td><blockquote>
<p>In constructing a message certain characters are used. These include the Segment Terminator, the Field Separator, the Component Separator, the Sub-Component Separator, Repetition Character, and the Escape Character.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>message event type</strong></td>
<td><blockquote>
<p><strong>Asynchronous</strong> HL7 the Message Event Type. Example ADT-A24</p>
<p><strong>Synchronous</strong> interactions PS will log the primary interaction type. Example: Add, Search, Update, and Resolve Duplicate.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>message segments</strong></td>
<td><blockquote>
<p>Each HL7 message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A [ ] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category, there will be a list of HL7 standard segments and/or "Z" segments used for the message.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>message type</strong></td>
<td><blockquote>
<p>Each message has a message type that defines its purpose. For example, the ADT Message Type is used to transmit portions of a patient's ADT data from one system to another. A 3-character code contained within each message identifies its type.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>MFN</strong></td>
<td><blockquote>
<p>Master Files Change Notification message.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Mirror Testing</strong></td>
<td><blockquote>
<p>Functional testing in a non-production VistA system that is maintained by the VA Medical Center (VAMC) and is normally a mirror (snapshot copy) of their production system as of the date the copy was created. The resultant “mirror” account is normally isolated from external VA systems, is scrambled to protect PHI and PII, and is refreshed (recopied from production) on a periodic basis. Users can modify mirror account data without the changes being transmitted to external systems or affecting the site’s live production database. These qualities enable site testers to execute high-priority test scenario scripts provided by the development team and note the success or failure of each script.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>MMN</strong></td>
<td><blockquote>
<p>Mother's Maiden Name: The family name under which the mother was born (i.e., before marriage). It is used to distinguish between patients with the same last name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>MPI initialization</strong></td>
<td><blockquote>
<p>The process of initializing a site's PATIENT file (#2) with the Master Patient Index (MPI). Initialization synchronizes PATIENT file (#2) information (for active shared patients) with the MPI and identifies facilities where the patient has been treated. This process transfers the Integration Control Number (ICN), and Treating Facility list for each patient to the patient's record in the VistA PATIENT file (#2) at all sites where the patient has been treated. It is also possible to initialize an individual patient to the MPI. This is done through menu options. The initial synchronization of PATIENT file (#2) information (for active, shared patients) with the Master Patient Index and with the patient's treating facilities is an important step in the implementation of the MPI/PD software system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>namespace</strong></td>
<td><blockquote>
<p>A convention for naming VistA package elements. The Database Administrator (DBA) assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>namespacing</strong></td>
<td><blockquote>
<p>Convention for naming VistA software elements. The DBA assigns unique two to four character string prefix for software developers to use in naming routines, options, and other software elements so that software can coexist. The DBA also assigns a separate range of file numbers to each software application.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>NDBI</strong></td>
<td><blockquote>
<p>National Database Integration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>NM</strong></td>
<td><blockquote>
<p>Numeric data type. A number represented as a series of ASCII numeric characters consisting of an optional leading sign (+ or -), the digits, and an optional decimal point.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>node</strong></td>
<td><blockquote>
<p>In a tree structure, a point at which subordinate items of data originate. An M array element is characterized by a name and a unique subscript. Thus the terms: node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or "pieces" reserved for data attributes such as name.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>NPI</strong></td>
<td><blockquote>
<p>National Provider Index</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>null</strong></td>
<td><blockquote>
<p>Empty—A field or variable that has no value associated with it is null.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>numeric field</strong></td>
<td><blockquote>
<p>Response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OBX</strong></td>
<td><blockquote>
<p>Observation/result message. OBX is intended to cover all types of patient specific observation reports except pharmacy.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OI</strong></td>
<td><blockquote>
<p>Office of Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OI&amp;T</strong></td>
<td><blockquote>
<p>Office of Information Technology</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OIFO</strong></td>
<td><blockquote>
<p>Office of Information Field Office.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>option</strong></td>
<td><blockquote>
<p>An entry in the OPTION file (#19). As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>option name</strong></td>
<td><blockquote>
<p>Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text "Menu Management"). Options are namespaced according to VistA conventions monitored by the DBA.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>package (software)</strong></td>
<td><blockquote>
<p>The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>person correlation</strong></td>
<td><blockquote>
<p>A profile of an Identity that is maintained by an Associated System and is correlated to only one ICN. (Source - PIDS)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Person Identification Service</strong></td>
<td><blockquote>
<p>The Person Identification Service (PIDS) is an OMG Interface Specification standard responsible for the identification, correlation, and search within and across a specified domain (A domain is a sphere of influence. For instance, a person has an identifier issued by the Social Security Administration [Social Security Number] which is different that their identifier issued by the State Department [Passport Number]. Both the Social Security Administration and State Department could be considered separate domains.) for identifiers based upon a provided set of search criteria traits. Essentially, this service provides for the assignment and reconciliation of multiple identifiers across domains and in supporting multiple implementation topologies. CORBA specification from OMG. (Source - PIDS)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PIMS</strong></td>
<td><blockquote>
<p>Patient Information Management System- VistA software package that includes Registration and Scheduling packages.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PKI</strong></td>
<td><blockquote>
<p>Public Key Infrastructure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PL</strong></td>
<td><blockquote>
<p>Patient Location data type.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PN</strong></td>
<td><blockquote>
<p>Person Name data type. A name includes multiple free text components: family name, given name, middle initial or name, suffix, prefix, and degree.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>POB (City)</strong></td>
<td><blockquote>
<p>PLACE OF BIRTH [CITY]: The city in which this applicant was born (or foreign country if born outside the U.S.).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>POB (State)</strong></td>
<td><blockquote>
<p>PLACE OF BIRTH [STATE]: State in which patient was born.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>pointer</strong></td>
<td><blockquote>
<p>The address at which a data value is stored in computer memory. A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward). Pointers can be an efficient means for applications to access data by referring to the storage location at which the data exists.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Potential Match Threshold</strong></td>
<td><blockquote>
<p>The level at which an Identity Profile must score against a set of identity traits in order to be considered a Potential Match for HC IdM decision processes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>primary key</strong></td>
<td><blockquote>
<p>A Data Base Management System construct, where one or more fields uniquely define a record (entry) in a file (table). The fields are required to be populated for every record on the file, and are unique, in combination, for every record on the file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>primary menu</strong></td>
<td><blockquote>
<p>The list of options presented at sign-on. Each user must have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by Information Resource Management (IRM). This menu should include most of the computing activities the user needs.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>primary reviewer</strong></td>
<td><blockquote>
<p>This can be a single person or group of people given the overall responsibility to initiate reviews of potential duplicate record pairs. For example, selected personnel in Patient Administration or a task force or group formed to oversee and conduct the effort of reducing or eliminating the occurrence of duplicate records in the site's database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Primary View</strong></td>
<td><blockquote>
<p>Provides the most accurate, current, and complete identity information for a VA patient. The Primary View from the MVI business rules make determinations about data additions and updates to identity traits (Name, SSN, Date of Birth, Gender, Mother's Maiden Name, Place of Birth, and Multiple Birth Indicator) based on the authoritativeness of the update or edits as they are received by the MVI.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>private integration agreement</strong></td>
<td><blockquote>
<p>Where only a single application is granted permission to use an attribute/function of another VistA package. These IAs are granted for special cases, transitional problems between versions, and release coordination. A Private IA is also created by the requesting package based on their examination of the custodian package's features. Example: one package distributes a patch from another package to ensure smooth installation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>probabilistic comparison score</strong></td>
<td><blockquote>
<p>In a Probabilistic Search, these are the points assigned to an identity to indicate the level of confidence of matching to a given set of traits.</p>
<p>If the Comparison Score is above a certain level called the Match Threshold, then the profile is considered to be a match and the profile would be returned to the calling application.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>probabilistic matching algorithm</strong></td>
<td><blockquote>
<p>A method to determine that a person identity profile has been matched in the PS Datastore based on the Comparison Score, which is calculated for each profile compared to the set of traits used for matching.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>probabilistic search</strong></td>
<td><blockquote>
<p>A search using a matching algorithm to determine that a person's identity profile matches a set of defined traits. The algorithm assigns a comparison score and returns results based on a defined match threshold.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>prompt</strong></td>
<td><blockquote>
<p>The computer interacts with the user by issuing questions called prompts, to which the user issues a response.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>protocol</strong></td>
<td><blockquote>
<p>Entry in the PROTOCOL file (#101). Used by the Order Entry/Results Reporting (OE/RR) package to support the ordering of medical tests and other activities.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PS</strong></td>
<td><blockquote>
<p>Product Support</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Pseudo SSN Reason</strong></td>
<td><blockquote>
<p>The reason that a pseudo SSN has been collected for the patient. The PSEUDO SSN REASON value is a set of codes pulled from the PATIENT (#2) file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>pseudo-SSNs</strong></td>
<td><blockquote>
<p>False Social Security Numbers that are calculated internally to VistA and cannot be mistaken for valid SSNs because they end in P.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PSIM</strong></td>
<td><blockquote>
<p>Person Service Identity Management (PSIM) enumerates and maintains person identities.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>QRY</strong></td>
<td><blockquote>
<p>Query message.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>queuing</strong></td>
<td><blockquote>
<p>Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). Kernel's TaskMan module handles the queuing of tasks.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Queuing Required</strong></td>
<td><blockquote>
<p>Option attribute that specifies that the option must be processed by Task Manager (the option can only be queued). The option may be invoked and the job prepared for processing, but the output can only be generated during the specified times.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>receiving site</strong></td>
<td><blockquote>
<p>Receiving Site- As it relates to HL7 Messages, it is the site that the message was sent to.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>record</strong></td>
<td><blockquote>
<p>Set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>REEME</strong></td>
<td><blockquote>
<p>Registration/Eligibility/Enrollment Maintenance and Enhancement</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>registration process</strong></td>
<td><p>During a registration, the person is checked against the entries in the Master Veteran Index (MVI) to determine if the person is already established or needs to be added. As of Patch DG*5.3*915 “Enterprise Search” replaced Register Once in the registration process to include Department of Defense (DoD) patients in an “extended” patient lookup if no patients are found on the MVI.</p>
<p>Within the Register a Patient [DG REGISTER PATIENT] option, the initial patient lookup search remains unchanged. That is, if a patient lookup performed in the site’s local VistA system returns one or more <em><u>existing</u></em> patients, the Registration user is asked to confirm the patient’s identity. However, if the patient is <em><u>not</u></em> found in the site’s local VistA system, the user is prompted to perform an “Enterprise Search,” which includes searching the DoD system if none found on the MVI. If the user chooses not to do an Enterprise Search, the software returns the user to the Select PATIENT prompt.</p>
<p>As of Patch DG*5.3*915, an Enterprise Search is required to add <em><u>new</u></em> patients to the local VistA system via the Register a Patient [DG REGISTER PATIENT] option.</p>
<p><strong>Using the Enterprise Search functionality:</strong></p>
<p>Upon choosing to do an Enterprise Search, the Registration user is presented with a series of prompts to enter the search criteria. If insufficient search criteria have been entered, the system displays a message requesting the user to enter the search criteria again. Sufficient search criteria entered automatically sends a query to the MVI to attempt to find possible matches. If matches <em><u>are not</u></em> found on the MVI, the query is automatically sent to the DoD system to find matches.</p>
<p>Patient matches that are found are returned grouped as an Auto Link or Potential Match for the registration staff to review. If a patient entry is selected, their data from the MVI (or DoD) is automatically loaded into the new patient's record. If that patient is already enrolled in the VA system, a query is sent to obtain the patient's Enrollment record prior to entering the registration screens. Then the registration process continues as normal.</p>
<p>Other possible results returned from an Enterprise Search:</p>
<ul>
<li><p>If too many matches are returned from the Enterprise Search, then the user is prompted to provide updated (more specific) search criteria to return a more limited search result list from which to select.</p></li>
<li><p>If no patients are found on the MVI or if the connection to the MVI is down, the user will be prompted to add the patient based upon the data previously entered.</p></li>
<li><p>If the matches returned are above the Auto Link threshold, then the user <em>must</em> select one of the patients returned from the query (Auto Link threshold or Potential Match threshold) or hold the security key, DG MVI ADD PT, to override the selection.</p></li>
<li><p>NOTE: Records that are returned from the Enterprise Search of the MVI or DoD systems are displayed in the closest match order based upon score.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>remote procedure call (RPC)</strong></td>
<td><blockquote>
<p>Remote Procedure Call is a protocol that one program can use to request a service from a program located on another computer network. Essentially M code may take optional parameters to do some work and then return either a single value or an array back to the client application.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>repeated value</strong></td>
<td><blockquote>
<p>Some fields may contain many repeat fields. For example, the diagnoses field may contain many different diagnoses.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>repetition separator</strong></td>
<td><blockquote>
<p>The repetition separator is used in some data fields to separate multiple occurrences of a field. It is used only where specifically authorized in the descriptions of the relevant data fields. The character that represents the repetition separator is specified for each message as the second character in the Encoding Characters data field of the MSH segment. Absent other considerations it is recommended that all sending applications use "~" as the repetition separator. However, all applications are required to accept whatever character is included in the Message Header and use it to parse the message.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>requesting site</strong></td>
<td><blockquote>
<p>Requesting Site as it relates to HL7 Messages, it is the site initiating a message to another site requesting some action be taken.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>required field</strong></td>
<td><blockquote>
<p>A mandatory field, one that must not be left blank. The prompt for such a field will be repeated until the user enters a valid response.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Resolution Journal Case Number</strong></td>
<td><blockquote>
<p>IDM – Number associated with each Resolution Journal Case. Used by the HealthCare Identity Management (HC IdM) team to document detailed information mostly for duplicate exception resolution but may also be used to denote details for resolving any type of exception.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>RG CIRN DEMOGRAPHIC ISSUES mail group</strong></td>
<td><blockquote>
<p>The RG CIRN DEMOGRAPHIC ISSUES bulletin controls the sending of the following person related bulletin:</p>
</blockquote>
<ul>
<li><p>Person Related Bulletin—REMOTE SENSITIVITY INDICATED</p></li>
</ul>
<ul>
<li><p>Cause—person is marked as sensitive at the sending site but not at receiving site.</p></li>
<li><p>Action to take—No action: message is informational</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>routine</strong></td>
<td><blockquote>
<p>Program or a sequence of instructions called by a program that may have some general or frequent use. M routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>SAC</strong></td>
<td><blockquote>
<p>Standards and Conventions. Through a process of quality assurance, all VistA software is reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>SACC</strong></td>
<td><blockquote>
<p>VistA's Standards and Conventions Committee. This Committee is responsible for maintaining the SAC.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>scheduling options</strong></td>
<td><blockquote>
<p>The technique of requesting that Task Manager run an option at a given time, perhaps with a given rescheduling frequency.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Screen Editor</strong></td>
<td><blockquote>
<p>VA FileMan's Screen-oriented text editor. It can be used to enter data into any WORD-PROCESSING field using full-screen editing instead of line-by-line editing.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ScreenMan forms</strong></td>
<td><blockquote>
<p>Screen-oriented display of fields, for editing or simply for reading. VA FileMan's Screen Manager is used to create forms that are stored in the FORM file (#.403) and exported with a software application. Forms are composed of blocks (stored in the BLOCK file [#.404]) and can be regular, full screen pages or smaller, "pop-up" pages.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>screen-oriented</strong></td>
<td><blockquote>
<p>A computer interface in which you see many lines of data at a time and in which you can move your cursor around the display screen using screen navigation commands. Compare to Scrolling Mode.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>security key</strong></td>
<td><blockquote>
<p>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>segment</strong></td>
<td><blockquote>
<p>An HL7 segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or they may be allowed to repeat. Each segment is identified by a unique three-character code known as the Segment ID.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>segment (record)</strong></td>
<td><blockquote>
<p>A typed aggregate of fields (fields) describing one complete aspect of a message. For example, the information about one order is sent as type of segment (OBR), the information related to an observation is sent as another segment (OBX).</p>
<p>The segment in a message is analogous to a record in a database, and in previous versions of the standard we used record in place of the word segment. We have changed the nomenclature to be consistent with HL7 and other standards organizations in this version.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>segment terminator</strong></td>
<td><blockquote>
<p>The segment terminator is the last character of every segment. It is always the ASCII CR character (hex 0D).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>sending site</strong></td>
<td><blockquote>
<p>Sending Site—As it relates to HL7 Messages, it is the site that is transmitting the message to another site.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>sensitive patient</strong></td>
<td><blockquote>
<p>Person whose record contains certain information, which may be deemed sensitive by a facility, such as political figures, employees, patients with a particular eligibility or medical condition. If a shared patient is flagged as sensitive at one of the treating sites, a bulletin is sent to the DG SENSITIVITY mail group at each subscribing site telling where, when, and by whom the flag was set. Each site can then review whether the circumstances meet the local criteria for sensitivity flagging.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>server</strong></td>
<td><blockquote>
<p>The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION file (#19). An automated mail protocol that is activated by sending a message to a server at another location with the "S.server" syntax. A server's activity is specified in the OPTION file (#19) and can be the running of a routine or the placement of data into a file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>set of codes</strong></td>
<td><blockquote>
<p>Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer rejects the response.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>shared patient</strong></td>
<td><blockquote>
<p>A person who has been seen at more than one VistA site. The MVI keeps the Treating Facility list updated every time a new facility is added. The MVI broadcasts out an updates to the treating facility list, including date last treated and event reason.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>SI</strong></td>
<td><blockquote>
<p>Sequence ID data type. A positive integer in the form of a NM field.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Site Manager/IRM Chief</strong></td>
<td><blockquote>
<p>At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as a liaison to the CIO Field Offices.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>software (package)</strong></td>
<td><blockquote>
<p>The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>source ID</strong></td>
<td><blockquote>
<p>A Source ID is a term used to describe the components that define a unique correlation. There are 4 components of a Source ID in MVI:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Assigning Authority (ex. USVHA)</p>
</blockquote></li>
<li><blockquote>
<p>Assigning Location (ex. Station #)</p>
</blockquote></li>
<li><blockquote>
<p>IDType (e.g. NI, PI, EI)</p>
</blockquote></li>
<li><blockquote>
<p>Internal Identifier - A code used at the assigning location used to uniquely identify a person.</p>
</blockquote></li>
</ol>
<blockquote>
<p>The Initiate Identity Hub also uses the term Source ID, but with a slightly different context. The Source ID in the IDHub is the unique identifier of a correlated system.. The fourth Source ID component, IEN, would translate to the Member ID in the ID HUB. Thus, the IDHub uses 2 components to uniquely identify a member: Source ID and Member ID.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>spacebar return</strong></td>
<td><blockquote>
<p>You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Special Queuing</strong></td>
<td><blockquote>
<p>Option attribute indicating that Task Manager should automatically run the option whenever the system reboots.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>SSA</strong></td>
<td><blockquote>
<p>Social Security Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>SSDI</strong></td>
<td><blockquote>
<p>Social Security Death Index (SSDI). The SSDI is a database used for genealogical research as well as enabling users to locate a death certificate, find an obituary, and discover cemetery records and track down probate records. The Healthcare Identity Management (HC IdM) Team uses the SSDI (<a href="http://www.genealogybank.com/gbnk/ssdi/">Social Security Death Index Web site</a> ) as a resource for verifying patients’ dates of death.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>SSN</strong></td>
<td><blockquote>
<p>Social Security Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>SSN Verification Status</strong></td>
<td><p>Possible values of this field used on the MVI for the Enrollment System Redesign (ESR) correlation are:</p>
<ul>
<li><p>NEW RECORD</p></li>
<li><p>IN-PROCESS</p></li>
<li><p>INVALID PER SSA</p></li>
<li><p>RESEND TO SSA</p></li>
<li><p>VERIFIED</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>ST</strong></td>
<td><blockquote>
<p>String data type. String Data is left justified with trailing blanks optional. Any printable ASCII characters are allowed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>station identifier</strong></td>
<td><blockquote>
<p>The number assigned to a VAMC facility or a System Association. The station identifier may be three characters in length designating the facility as a parent organization or up to six characters in length designating the facility as a child of a parent organization.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>subcomponent separator</strong></td>
<td><blockquote>
<p>The subcomponent separator is used to separate adjacent subcomponents of some data fields. Its use is described in the descriptions of the relevant data fields. The character that represents the subcomponent separator is specified for each message as the fourth character in the Encoding Characters data field of the MSH segment. Absent other considerations it is recommended that all sending applications use "&amp;" as the subcomponent separator. However, all applications are required to accept whatever character is included in the Message Header and use it to parse the message.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>subscriber</strong></td>
<td><blockquote>
<p>A subscriber is an entity, which receives updates to a patient's descriptive data from other sites. All treating facilities are also made subscribers as part of the MPI/PD processes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>subscript</strong></td>
<td><blockquote>
<p>A symbol that is associated with the name of a set to identify a particular subset or element. In M, a numeric or string value that: is enclosed in parentheses, is appended to the name of a local or global variable, and identifies a specific node within an array.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>supported reference integration agreement</strong></td>
<td><blockquote>
<p>This applies where any VistA application may use the attributes/functions defined by the IA (these are also called "Public "). An example is an IA that describes a standard API such as DIE or VADPT. The package that creates/maintains the Supported Reference must ensure it is recorded as a Supported Reference in the IA database. There is no need for other VistA packages to request an IA to use these references; they are open to all by default.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>synchronized patient data</strong></td>
<td><blockquote>
<p>Key descriptive fields in the PATIENT file (#2) that are updated in all the descriptive subscriber's PATIENT files whenever the fields are edited by a subscriber.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>synchronous</strong></td>
<td><blockquote>
<p>Refers to events that are synchronized, or coordinated, in time. Synchronous events have characteristics such as the interval between transmitting A and B being the same as between B and C, and completing the current operation before the next one is started. Contrast with asynchronous.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>systems of interest</strong></td>
<td><blockquote>
<p>The term "systems of interest" refers to VA facilities that have seen patients and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a patient (e.g., Federal Health Information Exchange [FHIE], HomeTeleHealth, Person Service Identity Management [PSIM], Health Data Repository [HDR], etc).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Task Manager</strong></td>
<td><blockquote>
<p>Kernel module that schedules and processes background tasks (also called TaskMan)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Task Threshold or Threshold, Task</strong></td>
<td><blockquote>
<p>The Task Threshold (also called the Clerical Review Threshold) is a value that is less than the Auto Link Threshold. A Comparison Score above the Task Threshold and below the Auto Link Threshold needs to be reviewed by an Identity Management expert to determine whether the Identity Profile is either a match or not a match for the traits being compared.</p>
<p>The Task Threshold is determined and tuned by Identity Management experts and may change over time as software systems and business processes improve. The ideal goal for automated identity matching is to minimize the difference between the Task Threshold and the Auto Link Threshold.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>TCP/IP</strong></td>
<td><blockquote>
<p>Transaction Control Protocol/Internet Protocol. A set of protocols for Layers 3 (Network) and 4 (Transfer) of the OSI network model. TCP/IP has been developed over a period of 15 years under the auspices of the Department of Defense. It is a de facto standard, particularly as higher-level layers over Ethernet. Although it builds upon the OSI model, TCP/IP is not OSI-compliant.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>template</strong></td>
<td><blockquote>
<p>Means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file (#.402), print specifications are stored in the PRINT TEMPLATE file (#.4), and search or sort specifications are stored in the SORT TEMPLATE file (#.401).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Testing Service</strong></td>
<td><blockquote>
<p>The mission of Testing Service is to provide testing environments, independent testing services, and capacity metrics that will support improvement of the overall quality, performance and safety of both Health<em><u>e</u></em>Vet and legacy VistA systems. </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>TIN</strong></td>
<td><blockquote>
<p>Temporary ID Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Toolkit (IdM TK)</strong></td>
<td><blockquote>
<p>The User Interface for the HealthCare Identity Management team. The Toolkit provides functionality to allow HC IdM staff to search and view identity and exception information. This includes the ability to view the Primary View record and any associated correlations, correlation data, history, audit trails, and HC IdM Tasks captured by MVI. In addition, functionality is provided to support the re-hosting transition for a side-by-side comparison of ADR and MVI information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Treating Facility</strong></td>
<td><blockquote>
<p>Any facility (VAMC) where a person has applied for care, or has been added to the local PATIENT file (#2) (regardless of VISN) and has identified this person to the MVI will be placed in the TREATING FACILITY LIST file (#391.91).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Treating Facility List</strong></td>
<td><blockquote>
<p>Table of institutions at which the person has received care. This list is used to create subscriptions for the delivery of person clinical and demographic information between sites.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>trigger</strong></td>
<td><blockquote>
<p>A type of VA FileMan cross-reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>trigger event</strong></td>
<td><blockquote>
<p>The event that initiates an exchange of messages is called a trigger event. The HL7 Standard is written from the assumption that an event in the real world of health care creates the need for data to flow among systems. The real-world event is called the trigger event. For example, the trigger event "a patient is admitted" may cause the need for data about that patient to be sent to a number of other systems. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code may not be associated with more than one message type.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>TS</strong></td>
<td><blockquote>
<p>Time Stamp data type. Contains the exact time of an event, including the date and time.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>TSPR</strong></td>
<td><blockquote>
<p>Technical Services Project Repository</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>TX</strong></td>
<td><blockquote>
<p>Text data type. String data meant for user display on a terminal or printer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>UAT</strong></td>
<td><blockquote>
<p>User Acceptance Testing.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>UCI</strong></td>
<td><blockquote>
<p>User Class Identification, a computing area. The MGR UCI is typically the Manager's account, while VAH or ROU may be Production accounts.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>UFT</strong></td>
<td><blockquote>
<p>User Functional Testing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong><u>U</u>nique <u>P</u>atient <u>I</u>dentifier (UPI)</strong></td>
<td><ul>
<li><p><strong>Outward Facing UPI (Social Security Number [SSN]):</strong> Requirements that apply to what the user sees (<u>outward facing</u>) should be what is currently stated in P&amp;LMS policy; currently still the Social Security Number (SSN).</p></li>
<li><p><strong>Inward Facing UPI (Integration Control Number [ICN]):</strong> Any requirements that refer to <u>inward facing</u> functions (internal clinical applications patient lookups) should use the Integration Control Number (ICN).</p></li>
<li><p><strong>Potential replacement for SSN as Outward Facing UPI (EDIPI):</strong> DoD EDIPI may eventually become the outward facing unique patient identifier (UPI), which is why the new VHIC 4.0 cards contain the EDIPI. However, there are some Veterans for whom the DoD has not provided EDIPI’s; therefore, VA has not announced the EDIPI as the official outward facing UPI and will not do so until VA and DoD have closed that gap to ensure all Veterans can be assigned the EDIPI.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>user access</strong></td>
<td><blockquote>
<p>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access.</p>
<p>The user's access level determines the degree of computer use and the types of computer programs available. The System Manager assigns the user an access level.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA</strong></td>
<td><blockquote>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA Domiciliary</strong></td>
<td><blockquote>
<p>Provides comprehensive health and social services in a VA facility for eligible veterans who are ambulatory and do not require the level of care provided in nursing homes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA FileMan</strong></td>
<td><blockquote>
<p>VistA's Database Management System (DBMS). The central component that defines the way standard VistA files are structured and manipulated.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA Hospital</strong></td>
<td><blockquote>
<p>An institution that is owned, staffed and operated by VA and whose primary function is to provide inpatient services.</p>
<p><strong>NOTE:</strong> Each division of an integrated medical center is counted as a separate hospital.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA Medical Center (VAMC)</strong></td>
<td><blockquote>
<p>A unique VA site of care providing two or more types of services that reside at a single physical site location. The services provided are the primary service as tracked in the VHA Site Tracking (VAST) (i.e., VA Hospital, Nursing Home, Domiciliary, independent outpatient clinic (IOC), hospital-based outpatient clinic (HBOC), and CBOC).</p>
<p>The definition of VA medical center does not include the Vet Centers as an identifying service.</p>
<p><strong>NOTE:</strong> This definition was established by the Under Secretary for Health.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA Nursing Home Care Units (NHCU)</strong></td>
<td><blockquote>
<p>Provide care to individuals who are not in need of hospital care, but who require nursing care and related medical or psychosocial services in an institutional setting. VA NHCUs are facilities designed to care for patients who require a comprehensive care management system coordinated by an interdisciplinary team. Services provided include nursing, medical, rehabilitative, recreational, dietetic, psychosocial, pharmaceutical, radiological, laboratory, dental and spiritual.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>variable</strong></td>
<td><blockquote>
<p>Character, or group of characters, that refer(s) to a value. M (previously referred to as MUMPS) recognizes 3 types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign-off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term "global" may refer either to a global variable or a global array. A special variable is defined by systems operations (e.g., $TEST).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VBA SHARE</strong></td>
<td><blockquote>
<p>This is a VBA application which is utilized by the Regional Offices to access BIRLS, C&amp;P, PIF, PHF, Corporate Database, Social Security and COVERS records. The Healthcare Identity Management (HC IdM) Team uses VBA SHARE as a resource for verifying patient identity data as well as military information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Verify Code</strong></td>
<td><blockquote>
<p>The Kernel's Sign-on/Security system uses the Verify code to validate the user's identity. This is an additional security precaution used in conjunction with the Access code. Verify codes shall be at least eight characters in length and contain three of the following four kinds of characters: letters (lower- and uppercase), numbers, and, characters that are neither letters nor numbers (e.g., "#", "@" or "$"). If entered incorrectly, the system does not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Vet Center</strong></td>
<td><blockquote>
<p>A data source under the direct supervision of the Readjustment Counseling Service (RCS). The Vet Center provides professional readjustment counseling, community education, outreach to special populations, brokering of services with community agencies, and access to important links.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VHA</strong></td>
<td><blockquote>
<p>Veterans Health Administration.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VIS</strong></td>
<td><blockquote>
<p>Veterans Information Solution (VIS). This intranet-based application is designed to provide a consolidated view of information about veterans and active service members. The HC IdM Team uses VIS as a resource for verifying patient identity data as well as military information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VISN</strong></td>
<td><blockquote>
<p>Veterans Integrated Service Network</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VistA</strong></td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture (VistA) of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). VistA software, developed by the VA, is used to support clinical and administrative functions at VHA sites nationwide. It is both roll-and-scroll- and GUI-based software that undergoes a quality assurance process to ensure conformity with namespacing and other VistA standards and conventions (see <a href="http://vaww.oed.portal.va.gov/communities/app_dev/sac/default.aspx">SAC</a>).</p>
<p>Server-side code is written in M, and, via Kernel, runs on all major M implementations regardless of vendor. Client-side code is written in Java or Borland Delphi and runs on the Microsoft operating system.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VPID (replaced with ICN.)</strong></td>
<td><blockquote>
<p>Veterans Administration Personal Identifier – An enterprise-level identifier uniquely identifying VA „persons‟ across the entire VA domain.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>WAN</strong></td>
<td><blockquote>
<p>Wide Area Network.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>XCN</strong></td>
<td><blockquote>
<p>Extended Composite ID Number and Name data type. In version 2.3, use instead of the CN data type.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>XON</strong></td>
<td><blockquote>
<p>Extended composite name and ID number for organizations data type.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>XPN</strong></td>
<td><blockquote>
<p>Extended person name data type. In version 2.3, replaces the PN data type.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>XTN</strong></td>
<td><blockquote>
<p>Extended telecommunications number data type. In version 2.3, replaces the TN data type.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Z segment</strong></td>
<td><blockquote>
<p>All message type and trigger event codes beginning with Z are reserved for locally defined messages. No such codes will be defined within the HL7 Standard.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Glossary description taken from the Health Level Seven, Version 2.3.1 documentation © 1999, Final Standard 05/999. Editor: Don A. Kruse, Atomic Moving Images™.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

> **NOTE:** For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the VA Security and Other Common Services Legacy Glossary Web site :

> [VA Glossary: Terms and Definitions Unofficial Intranet Website)](http://vista.med.va.gov/iss/glossary.asp)  
> *NOTE: This is an internal VA Web site and is not available to the public.*

> For a comprehensive list of acronyms, please visit the Office of Information and Technology (OI&T) Master Glossary Web site:

> [VA OI&T Master Glossary Web site](http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx)  
> *NOTE: This is an internal VA Web site and is not available to the public.*

<span id="_Toc131832194" class="anchor"></span>Appendix A—Communication with MPI Specification Agreement

The table below shows a list of messages found in the MVI HL7 Specification. Each HL7 message indicates if it applies to a non-VistA system. All messages must be processed and all messages expect Commit and Application Level Acknowledgements.

> **NOTE:** Currently, VistA applications update demographic information on the MVI using the following HL7 messages:

- ADT-A04—Register a Patient
- ADT-A08—Update Patient Information
- ADT-A31 – Update Person Information

> In the future, enterprise level applications coming from Person Services that need to update demographic information on the MVI in coordination with the enterprise view of patient record will use the following HL7 message:

- ADT-A31—Update Person Information

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 21%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Trigger Event</strong></th>
<th><strong>Event Supported HL7 V2.4 Message</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Query MVI for match</td>
<td>/RSP-K22</td>
<td><p>The MVI will accept a query for patient information. The current search algorithm uses Name, DOB, and SSN (if available) for its search. Results are returned in an ACK/Q02 (changed from ADT-A31 in patches MPI*1.0*32 and MPIF*1.0*38) (<strong>NOTE:</strong> supported for internal VistA VAMC messaging)</p>
<p>This find Candidates query is used to return a list of one ICN candidates for a given local identifier (i.e. dfn/station#). The query can also be used to establish a correlation to an ICN and/or an association to an existing correlated id (i.e. dfn/station#).</p>
<p><strong>NOTE:</strong> Supported for external VistA VAMC messaging.</p></td>
</tr>
<tr class="even">
<td>Add new patient to the MVI</td>
<td>(via Local/Missing ICN Resolution Job)</td>
<td><p>The MVI will accept new patient adds via ADT-A28 (add person or patient information). The MVI will in-turn broadcast back an ADT-A24 (link patient information) message.</p>
<p>The MVI will add a new patient if the VQQ-Q02 is sent in the form of the Local/Missing ICN Resolution Job and the patient is not found. The MVI will return the ICN in the ACK/Q02 Local/Missing ICN Resolution job response.</p></td>
</tr>
<tr class="odd">
<td>Link to an existing patient on the MVI</td>
<td></td>
<td>The MVI will accept an ADT-A24 (link patient information) message for the purpose of matching a sites patient to an existing ICN. The sites current demographic values will also be stored as a result.</td>
</tr>
<tr class="even">
<td>Update to fields on an existing MVI entry</td>
<td>,</td>
<td>The MVI will accept patient updates via ADT-A04 (register a patient) or ADT-A08 (update patient information) and will broadcast out to the authoritative source system if the update came from a non-authoritative source system and to all systems if it came from the authoritative source system.</td>
</tr>
<tr class="odd">
<td>Update Person Information outside of an event</td>
<td></td>
<td><p>The MVI will accept an ADT-A31 (update person information) and update the appropriate entry on the MVI depending on if the message is from the CMOR (MPI VETERAN/CLIENT file [#985]) or a treating facility (ASSOCIATED FACILITY file [#985.5]).</p>
<p>The MVI also broadcast out an ADT-A31 message to synchronize the identity management elements to the MVI Patient "primary view".</p></td>
</tr>
<tr class="even">
<td>Update to date last treated</td>
<td><p>,</p>
<p>,</p></td>
<td>The MVI will accept updates to date last treated and event reason via ADT-A01 (admit/visit notification) and/or ADT-A03 (Discharge and/or clinic checkouts). If the update changes the sites current MVI date last treated or event reason the MVI will broadcast a MFN-M05</td>
</tr>
<tr class="odd">
<td>Resolution of duplicates at the site where both entries exist on the MVI</td>
<td>,</td>
<td>The MVI will accept a resolution of a duplicate from a site via ADT-A40 (merge patient - patient identifier list). The MVI will in-turn broadcast out an ADT-A24 (link patient information).</td>
</tr>
<tr class="even">
<td>Resolution of duplicates on the MVI</td>
<td></td>
<td>The MVI will notify sites of a duplicate resolution via ADT-A24 (link patient information).</td>
</tr>
<tr class="odd">
<td>Identification and resolution of a mismatched patient</td>
<td></td>
<td>The MVI will notify sites of a mismatched patient via ADT-A43 (move patient - patient identifier list) This maintenance message is used to update a records ICN (i.e. enterprise ID trait)</td>
</tr>
<tr class="even">
<td>Change of CMOR assignment</td>
<td></td>
<td>The MVI will accept a change in CMOR assignment via an ADT-A31 from the current CMOR via ADT-A31 (update person information)</td>
</tr>
<tr class="odd">
<td>Patient Query</td>
<td></td>
<td>The sending site is requesting patient demographic information to be returned for a specific ICN via the QRY-A19 (patient query) message. The data is returned in an ADR message to the requesting site.</td>
</tr>
<tr class="even">
<td>Unlink Patient</td>
<td></td>
<td>The sending site is requesting to unlink its patient record from an ICN. This action reverses the Link.</td>
</tr>
<tr class="odd">
<td>Treating Facility List Update</td>
<td></td>
<td><p>The MVI will send out an MFN-M05 if the treating facility list is modified or if the date last treated or event reason changes.</p>
<p>This message can be generated as a result of another message being processed on the MVI or maybe triggered manually.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref120110863" class="anchor"></span>Table A-1. HL7 messages for non-VistA systems

<span id="_Toc131832195" class="anchor"></span>Index

> A

A01 Event, 2-6

A03 Event, 2-8

A04 Event, 2-29

A08 Event, 2-32

A19 Event, 2-52

A24 Event, 2-10, 2-14, 2-16

A28 Event, 2-3

A31 Event, 2-35, 2-40, 2-43

message sent requesting CMOR change, 2-40, 2-43

A37 Event, 2-60

A40 Event, 2-23

A43 Event, 2-26

Accept Acknowledgment Type, MSH-15, 3-37

Acknowledgment Code, MSA-1, 3-26

Acronyms (CSSP & VistA Legacy)

Web page address, 30

Add Person or Patient Information

ADT-A28, 2-3

Commit ACK returned to MVI from sending system, 2-5

Commit ACK sent from MVI to sending system, 2-4

msg sent to MVI, 2-4

Administrative sex, PID-8, 3-57

Admit a Patient option, 2-6

Admit Date/Time, PV1-44, 3-72

Admit/Visit Notification

ADT-A01, 2-6

App ACK sent from MVI to sending system, 2-7

Commit ACK returned to MVI from sending system, 2-7

Commit ACK sent from MVI to sending system, 2-7

msg sent to MVI, 2-7

ADT/HL7 PIVOT File (#391.71), 1-3, 2-32

ADT-A01 (Admit/Visit Notification), 2-6

App ACK sent from MVI to sending system, 2-7

Commit ACK returned to MVI from sending system, 2-7

Commit ACK sent from MVI to sending system, 2-7

msg sent to MVI, 2-7

ADT-A03 (Discharge/End Visit), 2-8

App ACK sent from MVI to sending system, 2-9

Commit ACK returned to MVI from sending system, 2-9

Commit ACK sent from MVI to sending system, 2-9

msg sent to MVI, 2-9

ADT-A04 (Register a Patient), 2-29

App ACK sent from MVI to sending system, 2-30

Commit ACK returned to MVI from sending system, 2-31

Commit ACK sent from MVI to sending system, 2-30

msg sent to MVI, 2-30

ADT-A08 (Update Patient Information), 2-32

App ACK sent from MVI to receiving system, 2-33

Commit ACK returned to MVI from receiving system, 2-34

Commit ACK sent from MVI to receiving system, 2-33

msg sent to MVI, 2-33

SELF ID GENDER, 2-33

ADT-A24 (Link Patient Information), 2-10

App ACK sent from MVI to sending system, 2-12, 2-15

App ACK sent to MVI, 2-13, 2-14

attempting to Subscribe to ICN, 2-11

Commit ACK returned from MVI to sending system, 2-13, 2-14, 2-15

Commit ACK returned to MVI from sending system, 2-12

Commit ACK sent from MVI to sending system, 2-12

Commit ACK sent to MVI, 2-13, 2-14

msg sent from MVI to sending system, 2-13

msg sent to MVI, 2-11

msg sent to MVI from site to Link PID2 ICN to PID1 ICN, 2-15

notify sending system of change to ICN assignment, 2-13

ADT-A28 (Add Person or Patient Information), 2-3

App ACK sent from MVI to sending system, 2-4

Commit ACK returned to MVI from sending system, 2-5

Commit ACK sent from MVI to sending system, 2-4

msg sent to MVI, 2-4

ADT-A31 (Enterprise Update Person Information), 2-43

ADT-A31 (Update CMOR), 2-40

Commit ACK sent to MVI from CMOR, 2-41

Commit ACK sent to MVI from VistA, 2-41

msg received at CMOR for approving/disapproving CMOR change request, 2-41

msg sent to the MVI requesting CMOR change, 2-40

ADT-A31 (Update Person Information), 2-35

App ACK sent from MVI to VistA, 2-37

App ACK sent to PSIM from MVI, 2-39, 2-46

App ACK sent to VistA from MVI, 2-38, 2-44

Commit ACK returned to MVI from VistA, 2-37

Commit ACK sent from MVI to VistA, 2-36

Commit ACK sent from PSIM with error condition reported, 2-39

Commit ACK sent to PSIM from MVI, 2-38, 2-45

Commit ACK sent to VistA, 2-42

Commit ACK sent to VistA from MVI, 2-37, 2-44

msg sent from MVI to PSIM, 2-38, 2-45

msg sent from MVI to VistA, 2-37, 2-44

msg sent from VistA to MVI, 2-36

ADT-A37 (Unlink Patient Information)

App ACK sent to MVI, 2-61

Commit ACK sent from MVI to sending system, 2-61

Commit ACK sent to MVI, 2-61

msg sent to MVI, 2-61

ADT-A40 (Merge Patient—Patient Identifier List), 2-23

App ACK sent from MVI to sending system, 2-24

Commit ACK returned to MVI from sending system, 2-25

Commit ACK sent from MVI to sending system, 2-24

msg sent to MVI, 2-24

ADT-A43 (Move Patient Information─Patient Identifier List), 2-26

App ACK sent from MVI to PSIM via HLO, 2-28

App ACK sent to MVI, 2-27

Commit ACK returned to MVI from receiving system, 2-28

Commit ACK sent from MVI to PSIM via HLO, 2-28

Commit ACK sent to MVI, 2-27

msg from MVI to receiving system, 2-27

msg from PSIM via HLO, 2-28

Algorithm descriptor, QRI-3, 3-90

Alternate patient ID, PID-4

Active VHIC number(s), 3-56

Appendix A

Communication with MVI Specification Agreement, 1

Application Acknowledgment Type, MSH-16, 3-37

Application and Commit Level Acknowledgement requirements, 1-2

Appointment Check-in/Check-out option, 2-8

ASSOCIATED FACILITY File (#985.5), 2-2, 2

Assumptions About the Reader, xxxi

B

Background Messages

Local/Missing ICN Resolution Background Job, 1-3

UPDATE BATCH JOB FOR HL7 v2.3, 1-3

Batch Comment, BHS-10, 3-6

Batch Comment, BTS-2, 3-7

Batch Control ID, BHS-11, 3-6

Batch Creation Date/Time, BHS-7, 3-5

Batch Encoding Characters, BHS-2, 3-4

Batch Field Separator, BHS-1, 3-4

Batch Header

BHS-1, Batch Field Separator, 3-4

BHS-10, Batch Comment, 3-6

BHS-11, Batch Control ID, 3-6

BHS-12, Reference Batch Control ID, 3-6

BHS-2, Batch Encoding Characters, 3-4

BHS-3, Batch Sending Application, 3-4

BHS-4, Batch Sending Facility, 3-4

BHS-5, Batch Receiving Application, 3-5

BHS-6, Batch Receiving Facility, 3-5

BHS-7, Batch Creation Date/Time, 3-5

BHS-8, Batch Security, 3-5

BHS-9, Batch Name/ID/Type, 3-5

Batch Header Segment, 3-2

Batch Message Count, BTS-1, 3-7

Batch Messages

real-time connection query returned from MVI, 2-59

real-time connection query sent to MVI, 2-58

Batch Name/ID/Type, BHS-9, 3-5

Batch Receiving Application, BHS-5, 3-5

Batch Receiving Facility, BHS-6, 3-5

Batch Security, BHS-8, 3-5

Batch Sending Application, BHS-3, 3-4

Batch Sending Facility, BHS-4, 3-4

Batch Totals, BTS-3, 3-7

Batch Trailer

BTS-1, Batch Message Count, 3-7

BTS-2, Batch Comment, 3-7

BTS-3, Batch Totals, 3-7

Batch Trailer Segment, 3-7

BHS, 3-2, 3-7

Field Definitions, 3-4

Birth order, PID-25, 3-65

Birth place (ST), PID-23, 3-65

Breed Code, PID-36, 3-67

BTS

Field Definitions, 3-7

C

Candidate confidence, QRI-1, 3-89

Citizenship, PID-26, 3-65

Column Description, RDF-2, 3-95

Column Value, RDT-1, 3-98

Comment, NTE-3, 3-40

Commit and Application Level Acknowledgement requirements, 1-2

Common Services Security Program & VistA Legacy

Acronyms

Web page address, 30

Glossary

Web page address, 30

Communication with MVI Specification Agreement, 1

Completion Date/Time, MFA-3, 3-15

Contents, xvii

Continuation pointer, 3-8

Continuation Pointer

DSC-1, Continuation pointer, 3-8

DSC-2, Continuation style, 3-8

Continuation pointer, DSC-1, 3-8

Continuation style, DSC-2, 3-8

Control ID, MFA-2, 3-15

Control ID, MFE-2, 3-18

Country code, MSH-17, 3-38

County code, PID-12, 3-59

D

Date/time of birth, PID-7, 3-57

Date/Time of Message, MSH-7, 3-35

Date/Time Planned Event, EVN-3, 3-11

Deferred Response Date/Time, QRD-6, 3-86

Deferred Response Type, QRD-5, 3-86

Delayed Acknowledgment Type, MSA-5, 3-27

Delimiter(s) Included Data in Field Value, HL7, 1-2

DG ADMIT PATIENT option, 2-6

DG DISCHARGE PATIENT option, 2-8

DG REGISTER A PATIENT option, 2-29

Direct Connect, 1-4

Discharge a Patient option, 2-8

Discharge/End Visit

ADT-A03, 2-8

App ACK sent from MVI to sending system, 2-9

Commit ACK returned to MVI from sending system, 2-9

Commit ACK sent from MVI to sending system, 2-9

msg sent to MVI, 2-9

Display Only Query option, 1-4

DSC, 3-8

Field Definitions, 3-8

E

Effective Date/Time, MFE-3, 3-18

Encoding Characters, MSH-2, 3-33

Enterprise Search

registration process, 21

Enterprise Update Person Information

ADT-A31, 2-43

ERR, 3-9

Field Definitions, 3-9

Error

ERR-1, Error Code and Location (CM), 3-9

Error Code and Location (CM), ERR-1, 3-9

Error Condition, MSA-6, 3-27

Error Segment, 3-9

Ethnic group, PID-22, 3-64

Event Facility, EVN-7, 3-13

Event Occurred, EVN-6, 3-13

Event Reason Code Name, ZET-17, 3-112

Event Reason Code, EVN-4, 3-12

Event Reason for Date of Last Treatment Segment, 3-108

Event Reason for Date of Last Treatment, ZET-1, 3-108

Event Type

EVN-1, Event Type Code, 3-10

EVN-2, Recorded Date/Time, 3-11

EVN-3, Date/Time Planned Event, 3-11

EVN-4, Event Reason Code, 3-12

EVN-5, Operator ID, 3-12

EVN-6, Event Occurred, 3-13

EVN-7, Event Facility, 3-13

Event Type Code, EVN-1, 3-10

Event Type Segment, 3-10

example, 3-13

events

A01, 2-6

A03, 2-8

A04, 2-29

A08, 2-32

A19, 2-52

A24, 2-10

A28, 2-3

A31, 2-35, 2-40, 2-43

A37, 2-60

A40, 2-23

A43, 2-26

K22, 2-17

M05, 2-47

Q02, 2-56, 2-58

Q22, 2-17

EVN, 3-10

example, 3-13

Field Definitions, 3-10

example messages

Add Person or Patient Information

App ACK sent from MVI to sending system, 2-4

Commit ACK returned to MVI from sending system, 2-5

Commit ACK sent from MVI to sending system, 2-4

Sent to MVI, 2-4

Admit/Visit Notification

App ACK sent from MVI to sending system, 2-7

Commit ACK returned to MVI from sending system, 2-7

Commit ACK sent from MVI to sending system, 2-7

Sent to MVI, 2-7

Discharge/End Visit

App ACK sent from MVI to sending system, 2-9

Commit ACK returned to MVI from sending system, 2-9

Commit ACK sent from MVI to sending system, 2-9

Sent to MVI, 2-9

EVN—Event Type Segment, 3-13

Find Candidates query

Commit ACK returned from MVI to sending system, 2-19

Commit ACK sent from MVI to sending system, 2-18

Commit ACK sent to MVI, 2-20, 2-21

Sent to MVI, 2-18

Find Candidates query—create site association

Sent to MVI, 2-20

Find Candidates query—sending facility unknown to MVI

Sent to MVI, 2-19

Link Patient Information

App ACK sent from MVI to sending system, 2-12, 2-15

App ACK sent to MVI, 2-13, 2-14

attempting to Subscribe to ICN, 2-11

Commit ACK returned from MVI to sending system, 2-13, 2-14, 2-15

Commit ACK returned to MVI from sending system, 2-12

Commit ACK sent from MVI to sending system, 2-12

Commit ACK sent to MVI, 2-13, 2-14

notify sending system of change to ICN assignment, 2-13

Sent from MVI to PSIM via HLO, 2-16

Sent from MVI to sending system, 2-13

Sent from MVI to site, notifying sending system of duplicate record merge, 2-14

Sent to MVI, 2-11

Sent to MVI from site to Link PID2 ICN to PID1 ICN, 2-15

Merge Patient—Patient Identifier List

App ACK sent from MVI to sending system, 2-24

Commit ACK returned to MVI from sending system, 2-25

Commit ACK sent from MVI to sending system, 2-24

Sent to MVI, 2-24

Move Patient Information─Patient Identifier List

App ACK sent from MVI to PSIM via HLO, 2-28

App ACK sent to MVI, 2-27

Commit ACK returned to MVI from receiving system, 2-28

Commit ACK sent from MVI to PSIM via HLO, 2-28

Commit ACK sent to MVI, 2-27

Sent from MVI to receiving system, 2-27

Sent from PSIM via HLO, 2-28

Patient Query

Commit ACK sent from MVI, 2-54, 2-55

Commit ACK sent to MVI, 2-53, 2-55

Patient is known at queried facility, 2-53

Patient not known at queried facility, 2-55

Sent from MVI, 2-53, 2-55

Patient Query batch

Commit ACK sent from MVI, 2-59

QBP-Q22

Message sent from the MVI to PSIM, 2-21

QBP-Q22 and the responding RSP-K22 when no match found, 2-22

Query for Patient Matches

Real-time connection query returned from MVI, 2-57

Real-time connection query returned from MVI─batch message example), 2-59

Real-time connection query sent to MVI, 2-56

real-time connection query sent to MVI─batch message example), 2-58

Register a Patient

App ACK sent from MVI to sending system, 2-30

Commit ACK returned to MVI from sending system, 2-31

Commit ACK sent from MVI to sending system, 2-30

Sent to MVI, 2-30

Response

Commit ACK returned from MVI to sending system, 2-21

Commit ACK sent from MVI to sending system, 2-20

From PSIM when the MVI has sent QBP-Q22 to search for match(es), 2-22

Site/DFN pair found on MVI (sent to sending system), 2-18, 2-21

RSP-K22 (Response)—site not found in MVI SITE MONITOR file

sent to the site, 2-20

Unlink Patient Information

App ACK sent to MVI, 2-61

Commit ACK sent from MVI to sending system, 2-61

Commit ACK sent to MVI, 2-61

Sent to MVI, 2-61

Update CMOR

Commit ACK sent to MVI from CMOR, 2-41

Commit ACK sent to MVI from VistA, 2-41

Received at CMOR for approving/disapproving CMOR change request, 2-41

Sent to the MVI requesting CMOR change, 2-40

Update Patient Information

App ACK sent from MVI to receiving system, 2-33

Commit ACK returned to MVI from receiving system, 2-34

Commit ACK sent from MVI to receiving system, 2-33

Sent to MVI, 2-33

SELF ID GENDER, 2-33

Update Person Information

App ACK sent from MVI to VistA, 2-37

App ACK sent to PSIM from MVI, 2-39, 2-46

App ACK sent to VistA from MVI, 2-38, 2-44

Commit ACK returned to MVI from VistA, 2-37

Commit ACK sent from MVI to VistA, 2-36

Commit ACK sent from PSIM with error condition reported, 2-39

Commit ACK sent to PSIM from MVI, 2-38, 2-45

Commit ACK sent to VistA, 2-42

Commit ACK sent to VistA from MVI, 2-37, 2-44

Sent from MVI to PSIM, 2-38, 2-45

Sent from MVI to VistA, 2-37, 2-44

Sent from VistA to MVI, 2-36

Sent requesting CMOR change, 2-40, 2-43

Update Treating Facility

App ACK sent to MVI, 2-49, 2-51

Commit ACK returned from MVI to sending system, 2-49, 2-51

Commit ACK sent to MVI, 2-48, 2-51

Received from MVI, 2-48, 2-51

Execution and delivery time, RCP-4, 3-93

Expected admit date/time, PV2-8, 3-75

F

Field Definitions

BHS, 3-4

BTS, 3-7

DSC, 3-8

ERR, 3-9

EVN, 3-10

MFA, 3-14

MFE, 3-17

MFI, 3-20

MRG, 3-22

MSA, 3-26

MSH, 3-33

NTE, 3-39

PD1, 3-48

PID, 3-53

PV1, 3-72

PV2, 3-75

QAK, 3-77

QPD, 3-80

QRD, 3-84

QRI, 3-89

RDF, 3-95

RDT, 3-98

RPC, 3-91

VTQ, 3-100

ZET, 3-108

ZPD, 3-112

Field Separator, MSH-1, 3-33

Figures and Tables, xx

File-Level Event Code, MFI-3, 3-21

files

ADT/HL7 PIVOT (#391.71), 1-3, 2-32

INSTITUTION (#4), 3-18

PATIENT (#2), 1-3, 1-6

TREATING FACILITY (#391.91), 1-4, 3-11, 3-13

Find Candidates (QBP) and Response (RSP)

QBP-Q22 and RSP-K22, 2-17

Find Candidates query

Commit ACK returned from MVI to sending system, 2-19

Commit ACK sent from MVI to sending system, 2-18

Commit ACK sent to MVI, 2-20, 2-21

msg sent to MVI, 2-18

msg sent to MVI—create site association, 2-20

sending facility unknown to MVI (msg sent to MVI), 2-19

G

Glossary

CSSP and VistA Legacy Web page address, 30

H

Help at Prompts, xxx

Hit count total, QAK-4, 3-78

HL7 Attribute Table—QPD, 3-79

HL7 Commit and Application Level Acknowledgement, 1-2

HL7 Delimiter(s) Included Data in Field Value, 1-2

HL7 Interface Specifications, 1-1

HL7 interface standards, Version 2.4, 1-1

HL7 Optimized (HLO), 1-1

HL7 Standards Documentation

Web page address, xxxi

HL7 tables

0003 EVN—ADT/R Event Type Codes, 3-11

0005—Race, 4-1

0008—Acknowledgement Code, 3-26

0048—What Subject Filter, 3-87

0091—Query priority, 3-91

0091—Query Priority, 3-85

0102─Delayed Acknowledgement type, 3-27

0103—Processing ID, 3-36

0104—Version ID, 3-37

0105—Source of Comment, 3-40

0106—Query/Response Format Code, 3-85

0126—Quantity limited request, 3-92

0126—Quantity Limited Request, 3-86

0136—Yes/no indicator, 3-49

0155—Accept/Application Acknowledgement Conditions, 3-38

0175—Master File Identifier Code, 3-20

0178—File Level Event Code, 3-21

0179—Response Level, 3-21

0180—Record-level Event Code, 3-17

0200—Name type, 3-57

0202—Telecommunication Equipment Type, 3-60

0203—Identifier type, 3-55

0208—Query Response Status, 3-77

0209—Relational operator, 3-103

0210—Relational conjunction, 3-103

0355─Primary key value type, 3-16

0357—Message Error Condition Codes, 3-27

0391—Segment group, 3-94

0394—Response modality, 3-93

0395—Modify indicator, 3-93

0398—Continuation style code, 3-8

0399—Country Code, 3-38

BHS—Batch Header, 3-2

BTS—Batch Trailer, 3-7

DSC—Continuation Pointer, 3-8

ERR—Error, 3-9

EVN—Event Type, 3-10

HL7 field designation numbers and translations, 3-96, 3-98

MFA—Master File Acknowledgement, 3-14

MFE—Master File Entry, 3-17

MFI—Master File Identification, 3-20

MRG—Merge Patient Information, 3-22

MSA—Message Acknowledgement, 3-25

MSH—Message Header, 3-29

NTE—Notes and Comments, 3-39

OBX—Observation/Result, 3-46

PD1—Patient Additional Demographic, 3-47

PID—Patient Identification, 3-50

PV1Patient Visit, 3-69

PV2—Patient Visit Segment – Additional Information, 3-73

QAK—Query Acknowledgement, 3-76

QPD─Query Parameter Definition, 3-79

QRD—Original-Style Query Definition, 3-84

QRI—Query Response Instance Segment, 3-89

RCP—Response Control Parameter, 3-91

RDF—Table Row Definition, 3-95

RDT—Table Row Data, 3-98

VTQ—Virtual Table Query Request, 3-100

HLO (HL7 Optimized), 1-1

How to

Obtain Technical Information Online, xxx

Use this Manual, xxix

I

Identity Unknown Indicator, PID-31, 3-66

Identity Unknown Indicator, PID-32, 3-66

INSTITUTION File (#4), 3-18

Intended Audience/Assumptions, xxxi

K

K22 Event, 2-17

L

Last Update Date/Time, PID-33, 3-67

Last Update Facility, PID-34, 3-67

Legal Disclaimers, xxxi

Link Patient Information

ADT-A24, 2-10

App ACK sent from MVI to sending system, 2-12, 2-15

App ACK sent to MVI, 2-13, 2-14

attempting to Subscribe to ICN, 2-11

Commit ACK returned from MVI to sending system, 2-13, 2-14, 2-15

Commit ACK returned to MVI from sending system, 2-12

Commit ACK sent from MVI to sending system, 2-12

Commit ACK sent to MVI, 2-13, 2-14

msg sent from MVI to PSIM via HLO, 2-16

msg sent from MVI to sending system, 2-13

msg sent from MVI to site, notifying sending system of duplicate record merge, 2-14

msg sent to MVI, 2-11

msg sent to MVI from site to Link PID2 ICN to PID1 ICN, 2-15

notify sending system of change to ICN assignment, 2-13

M

M05 Event, 2-47

Marital status, PID-16, 3-61

Master File Acknowledgment

MFA-1, Record-Level Event Code, 3-14

MFA-2, MFN control ID, 3-15

MFA-3, Completion Date/Time, 3-15

MFA-4, MFN Record Level Error Return, 3-15

MFA-5, Primary Key Value, 3-16

MFA-6, Primary Key Value Type, 3-16

Master File Acknowledgment Segment, 3-14

Master File Entry

MFE-1, Record-level Event Code, 3-17

MFE-2, MFN Control ID, 3-18

MFE-3, Effective Date/Time, 3-18

MFE-4, Primary Key Value, 3-18

MFE-5, Primary Key Value Type, 3-19

Master File Entry Segment, 3-17

Master File Identification

MFI-1, Master File Identifier, 3-20

MFI-3, File-Level Event Code, 3-21

MFI-6, Response Level Code, 3-21

Master File Identification Segment, 3-20

Master File Identifier, MFI-1, 3-20

Master Veteran Index (MVI), 1-1

Match reason code, QRI-2, 3-89

Merge Patient Information

MRG-1, Prior Patient Identifier List, 3-22

MRG-2, Prior Alternate Patient ID, 3-23

MRG-3, Prior Patient Account Number, 3-23

MRG-4, Prior Patient ID, 3-24

MRG-5, Prior Visit Number, 3-24

MRG-6, Prior Alternate Visit ID, 3-24

MRG-7, Prior Patient Name, 3-24

Merge Patient Information Segment, 3-22

Merge Patient—Patient Identifier List

ADT-A40, 2-23

App ACK sent from MVI to sending system, 2-24

Commit ACK returned to MVI from sending system, 2-25

Commit ACK sent from MVI to sending system, 2-24

msg sent to MVI, 2-24

Message Acknowledgment

MSA-1

Acknowledgment Code, 3-26

MSA-2, Message Control ID, 3-26

MSA-3, Text message, 3-27

MSA-5, Delayed Acknowledgment Type, 3-27

MSA-6, Error Condition, 3-27

Message Acknowledgment Segment, 3-25

Message Control ID, MSA-2, 3-26

Message Control ID, MSH-10, 3-36

Message Header

MSH-1, Field Separator, 3-33

MSH-10, Message Control ID, 3-36

MSH-11, Processing ID, 3-36

MSH-12, Version ID, 3-37

MSH-15, Accept Acknowledgment Type, 3-37

MSH-16, Application Acknowledgment Type, 3-37

MSH-17, Country code, 3-38

MSH-2, Encoding Characters, 3-33

MSH-3, Sending Application, 3-33

MSH-4, Sending Facility, 3-34

MSH-5, Receiving Application, 3-35

MSH-6, Receiving Facility, 3-35

MSH-7, Date/Time of Message, 3-35

MSH-9, Message Type, 3-36

Message Header Segment, 3-29

Message query name, 3-76, 3-78

Message query name, QAK-3, 3-78

Message query name, QPD-1, 3-80

Message Type, MSH-9, 3-36

messages

ADT-A28 (Add Person or Patient Information)

Commit ACK sent from MVI to sending system, 2-4

msg sent to MVI, 2-4

ADT-A37 (Unlink Patient Information)

App ACK sent to MVI, 2-61

Commit ACK sent from MVI to sending system, 2-61

Commit ACK sent to MVI, 2-61

sent to MVI, 2-61

Messages

ADT-A01 (Admit/Visit Notification), 2-6

App ACK sent from MVI to sending system, 2-7

Commit ACK returned to MVI from sending system, 2-7

Commit ACK sent from MVI to sending system, 2-7

sent to MVI, 2-7

ADT-A03 (Discharge/End Visit), 2-8, 2-9

App ACK sent from MVI to sending system, 2-9

Commit ACK returned to MVI from sending system, 2-9

Commit ACK sent from MVI to sending system, 2-9

ADT-A04 (Register a Patient), 2-29

App ACK sent from MVI to sending system, 2-30

Commit ACK returned to MVI from sending system, 2-31

Commit ACK sent from MVI to sending system, 2-30

msg sent to MVI, 2-30

ADT-A08 (Update Patient Information), 2-32

App ACK sent from MVI to receiving system, 2-33

Commit ACK returned to MVI from receiving system, 2-34

Commit ACK sent from MVI to receiving system, 2-33

sent to MVI, 2-33

SELF ID GENDER, 2-33

ADT-A24 (Link Patient Information), 2-10

App ACK sent from MVI to sending system, 2-12, 2-15

App ACK sent to MVI, 2-13, 2-14

Commit ACK returned from MVI to sending system, 2-13, 2-14, 2-15

Commit ACK returned to MVI from sending system, 2-12

Commit ACK sent from MVI to sending system, 2-12

Commit ACK sent to MVI, 2-13, 2-14

ADT-A24Link Patient Information)

msg sent from MVI to sending system, 2-13

sent MVI, 2-11

ADT-A28 (Add Person or Patient Information), 2-3

App ACK sent from MVI to sending system, 2-4

Commit ACK returned to MVI from sending system, 2-5

ADT-A31 (Enterprise Update Person Information), 2-43

ADT-A31 (Update CMOR), 2-40

Commit ACK sent to MVI from CMOR, 2-41

Commit ACK sent to MVI from VistA, 2-41

ADT-A31 (Update Person Information), 2-35

App ACK sent from MVI to VistA, 2-37

App ACK sent to PSIM from MVI, 2-39, 2-46

App ACK sent to VistA from MVI, 2-38, 2-44

Commit ACK returned to MVI from VistA, 2-37

Commit ACK sent from MVI to VistA, 2-36

Commit ACK sent from PSIM with error condition reported, 2-39

Commit ACK sent to PSIM from MVI, 2-38, 2-45

Commit ACK sent to VistA, 2-42

Commit ACK sent to VistA from MVI, 2-37, 2-44

ADT-A31 Update Person Information)

sent from MVI to PSIM, 2-38, 2-45

sent from MVI to VistA, 2-37, 2-44

sent from VistA to MVI, 2-36

ADT-A31Update CMOR)

msg sent to the MVI requesting CMOR change, 2-40

received at CMOR for approving/disapproving CMOR change request, 2-41

ADT-A37 (Unlink Patient Information), 2-60

ADT-A40 (Merge Patient—Patient Identifier List), 2-23

App ACK sent from MVI to sending system, 2-24

Commit ACK returned to MVI from sending system, 2-25

Commit ACK sent from MVI to sending system, 2-24

sent to MVI, 2-24

ADT-A43 (Move Patient Information─Patient Identifier List), 2-26

App ACK sent from MVI to PSIM via HLO, 2-28

App ACK sent to MVI, 2-27

Commit ACK returned to MVI from receiving system, 2-28

Commit ACK sent from MVI to PSIM via HLO, 2-28

Commit ACK sent to MVI, 2-27

ADT-A43 Move Patient Information─Patient Identifier List)

sent from MVI to receiving system, 2-27

sent from PSIM via HLO, 2-28

Find Candidates query—create site association

sent to MVI, 2-20

Link Patient Information

attempting to Subscribe to ICN, 2-11

msg sent from MVI to PSIM via HLO, 2-16

notify sending system of change to ICN assignment, 2-13

sent from MVI to site, notifying sending system of duplicate record merge, 2-14

sent to MVI from site to Link PID2 ICN to PID1 ICN, 2-15

MFN-M05 (Update Treating Facility), 2-47

App ACK sent to MVI, 2-49, 2-51

Assigning Authority parsed from MFE, 2-49, 2-50

Commit ACK returned from MVI to sending system, 2-49, 2-51

Commit ACK sent to MVI, 2-48, 2-51

Id Type parsed from MFE, 2-49, 2-50

received from MVI, 2-48, 2-51

QBP-Q22 (Find Candidates query), 2-17

Commit ACK returned from MVI to sending system, 2-19

Commit ACK sent from MVI to sending system, 2-18

Commit ACK sent to MVI, 2-20, 2-21

sending facility unknown to MVI (sent to MVI), 2-19

sent to MVI, 2-18

QBP-Q22 and the responding RSP-K22 when no match found, 2-22

QBP-Q22 message sent from the MVI to PSIM, 2-21

QRY-A19 (Patient Query batch)

Commit ACK sent from MVI, 2-59

QRY-A19 (Patient Query), 2-52

Commit ACK sent from MVI, 2-54, 2-55

Commit ACK sent to MVI, 2-53, 2-55

QRY-A19 Patient Query

patient is known at queried facility, 2-53

patient not known at queried facility, 2-55

sent from MVI, 2-53, 2-55

Query for Patient Matches

real-time connection query returned from MVI (batch message example), 2-59

real-time connection query sent to MVI (batch message example), 2-58

RSP-K22 (Response), 2-17

Commit ACK returned from MVI to sending system, 2-21

Commit ACK sent from MVI to sending system, 2-20

RSP-K22 (Response)─from PSIM when the MVI has sent a QBP-Q22 to search for match(es), 2-22

RSP-K22 (Response)─Site/DFN pair found on MVI sent to sending system, 2-18, 2-21

RSP-K22 (Response)—site not found in MVI SITE MONITOR file

sent to the site, 2-20

segments, 3-2

Update Person Information

sent requesting CMOR change, 2-40, 2-43

VQQ-Q02 (Query for Patient Matches), 2-56

VQQ-Q02 (Query for Patient Matches—Batch format), 2-58

VQQ-Q02 Query for Patient Matches

real-time connection query returned from MVI, 2-57

real-time connection query sent to MVI, 2-56

MFA, 3-14

Field Definitions, 3-14

MFE, 3-17

Field Definitions, 3-17

MFI, 3-20

Field Definitions, 3-20

MFN-M05 (Update Treating Facility), 2-47

App ACK sent to MVI, 2-49, 2-51

Commit ACK returned from MVI to sending system, 2-49, 2-51

Commit ACK sent to MVI, 2-48, 2-51

Modify indicator, RCP-5, 3-93

Mother's identifier, PID-21, 3-64

Mother's maiden name, PID-6, 3-57

Move Patient Information─Patient Identifier List

ADT-A43, 2-26

App ACK sent from MVI to PSIM via HLO, 2-28

App ACK sent to MVI, 2-27

Commit ACK returned to MVI from receiving system, 2-28

Commit ACK sent from MVI to PSIM via HLO, 2-28

Commit ACK sent to MVI, 2-27

msg sent from MVI to PSIM via HLO, 2-28

sent from MVI to receiving system, 2-27

MPI VETERAN/CLIENT File (#985), 2-2, 2

MRG, 3-22

Field Definitions, 3-22

MSA, 3-25

Field Definitions, 3-26

MSH, 3-29

Field Definitions, 3-33

Multiple birth indicator, PID-24, 3-65

N

Nationality, PID-28, 3-66

Notes and Comments

NTE-1, Set ID–NTE-1, 3-39

NTE-2, Source of Comment, 3-39

NTE-3, Comment, 3-40

Notes and Comments Segment, 3-39

NTE, 3-39

Field Definitions, 3-39

Number of Columns Per Row, RDF-1, 3-95

O

Observation/Result Segment, 3-41

Obtain Technical Information Online, How to, xxx

Obtaining Data Dictionary Listings, xxx

OBX

Self Identified Gender, 3-41

Operator ID, EVN-5, 3-12

options

Admit a Patient, 2-6

Appointment Check-in/Check-out, 2-8

DG ADMIT PATIENT, 2-6

DG DISCHARGE PATIENT, 2-8

DG REGISTER A PATIENT, 2-29

Discharge a Patient, 2-8

Display Only Query, 1-4

Register a Patient, 2-29

SDAM APPT CHECK IN/OUT, 2-8

Orientation, xxix

Legal Disclaimers, xxxi

Original-style Query Definition

QRD-1, Query Date/Time, 3-84

QRD-10, What Department Data Code, 3-88

QRD-11, What Data Code Value Qual, 3-88

QRD-12, Query Results Level, 3-88

QRD-2, Query Format Code, 3-85

QRD-3, Query Priority, 3-85

QRD-4, Query ID, 3-85

QRD-5, Deferred Response Type, 3-86

QRD-6, Deferred Response Date/Time, 3-86

QRD-7, Quantity Limited Request, 3-86

QRD-8, Who subject Filter, 3-86

QRD-9, What Subject Filter, 3-87

Original-style Query Definition Segment, 3-84

P

Patch Revisions, xvi

patient & user names

test data, xxix

Patient account number, PID-18, 3-64

Patient Additional Demographic

PD1-3, Patient Primary Facility, 3-48

Patient Additional Demographic Segment, 3-47

Patient address, PID-11, 3-58

Patient alias, 3-58

Patient alias, PID-9, 3-58

Patient Class, PV1-2, 3-72

Patient death date and time, PID-29, 3-66

Patient Death Indicator, PID-30, 3-66

PATIENT File (#2), 1-3, 1-6

Patient ID, PID-2, 3-54

Patient Identification

PID-1, Set ID—PID, 3-53

PID-10, Race, 3-58

PID-11, Patient address, 3-58

PID-12, County code, 3-59

PID-13, Phone number, 3-59

PID-14, Phone number—business, 3-60

PID-15, Primary language, 3-60

PID-16, Marital status, 3-61

PID-17, Religion, 3-61

PID-18, Patient account number, 3-64

PID-19, SSN number—patient, 3-64

PID-2, Patient ID, 3-54

PID-20, SSN number—patient, 3-64

PID-21, Mother's identifier, 3-64

PID-22, Ethnic group, 3-64

PID-23, Birth place (ST), 3-65

PID-24, Multiple birth indicator, 3-65

PID-25, Birth order, 3-65

PID-26, Citizenship, 3-65

PID-27, Veterans military status, 3-65

PID-28, Nationality, 3-66

PID-29, Patient death date and time, 3-66

PID-3, Patient identifier list, 3-54

PID-30, Patient Death Indicator, 3-66

PID-31, Identity Unknown Indicator, 3-66

PID-32, Identity Unknown Indicator, 3-66

PID-33, Last Update Date/Time, 3-67

PID-34, Last Update Facility, 3-67

PID-35, Species Code, 3-67

PID-36, Breed Code, 3-67

PID-37, Strain, 3-68

PID-38, Strain, 3-68

PID-4, Alternate patient ID

Active VHIC number(s), 3-56

PID-5, Patient name, 3-56

PID-6, Mother's maiden name, 3-57

PID-7, Date/time of birth, 3-57

PID-8, Administrative sex, 3-57

PID-9, Patient alias, 3-58

Patient Identification Segment, 3-49

example, 3-50

Patient identifier list, PID-3, 3-54

Patient name, PID-5, 3-56

Patient Primary Facility

ZET-2, 3-108

Patient Primary Facility, PD1-3, 3-48

Patient Query

Commit ACK sent from MVI, 2-54, 2-55

Commit ACK sent to MVI, 2-53, 2-55

patient is known at queried facility, 2-53

patient not known at queried facility, 2-55

QRY-A19, 2-52

sent from MVI, 2-53, 2-55

Patient Status Effective Date, PV2-46, 3-75

Patient Visit

PV1-2, Patient Class, 3-72

PV1-44, Admit Date/Time, 3-72

Patient Visit Segment, 3-69

Patient Visit Segment – Additional Information, 3-73

Patient Visit–Additional Information

PV2

Field Definitions, 3-75

PV2-14, Previous service date, 3-75

PV2-46, Patient Status Effective Date, 3-75

PV2-8, Expected admit date/time, 3-75

PD1, 3-47

Field Definitions, 3-48

Phone number, PID-13, 3-59

Phone number—business, PID-14, 3-60

PID, 3-49

example, 3-50

Field Definitions, 3-53

Previous service date, PV2-14, 3-75

Primary Key Value Type, MFA-6, 3-16

Primary Key Value Type, MFE-5, 3-19

Primary Key Value, MFA-5, 3-16

Primary Key Value, MFE-4, 3-18

Primary language, PID-15, 3-60

Primary View Initialization, 2-1

Prior Alternate patient ID, MRG-2, 3-23

Prior Alternate Visit ID, MRG-6, 3-24

Prior Patient Account Number, MRG-3, 3-23

Prior Patient ID, MRG-4, 3-24

Prior Patient Identifier List, MRG-1, 3-22

Prior Patient Name, MRG-7, 3-24

Prior Visit Number, MRG-5, 3-24

Processing ID, MSH-11, 3-36

PSEUDO SSN REASON, ZPD-34, 3-113

PV1, 3-69

Field Definitions, 3-72

Q

Q02 Event, 2-56, 2-58

Q22 Event, 2-17

QAK, 3-73, 3-76

Field Definitions, 3-77

QBP-Q22 (Find Candidates query), 2-17

Commit ACK returned from MVI to sending system, 2-19

Commit ACK sent from MVI to sending system, 2-18

Commit ACK sent to MVI, 2-20, 2-21

msg sent to MVI, 2-18, 2-19, 2-20

QBP-Q22 and the responding RSP-K22 when no match found, 2-22

QBP-Q22 message sent from the MVI to PSIM, 2-21

QPD, 3-79

Field Definitions, 3-80

QRD, 3-84

Field Definitions, 3-84

QRI, 3-89

Field Definitions, 3-89

QRY-A19 (Patient Query batch)

Commit ACK sent from MVI, 2-59

QRY-A19 (Patient Query), 2-52

Commit ACK sent from MVI, 2-54, 2-55

Commit ACK sent to MVI, 2-53, 2-55

patient is known at queried facility, 2-53

patient not known at queried facility, 2-55

sent from the

MVI, 2-53, 2-55

Quantity Limited Request, QRD-7, 3-86

Quantity limited request, RCP-2, 3-92

Query Acknowledgment

QAK-1, Query Tag, 3-77

QAK-2, Query Response Status, 3-77

QAK-3, Message query name, 3-78

QAK-4, Hit count total, 3-78

Query Acknowledgment Segment, 3-76

Query Date/Time, QRD-1, 3-84

Query for Patient Matches

real-time connection query returned from MVI, 2-57

real-time connection query returned from MVI (batch message example), 2-59

real-time connection query sent to MVI, 2-56

real-time connection query sent to MVI (batch message example), 2-58

VQQ-Q02, 2-56

VQQ-Q02 in Batch Format, 2-58

Query Format Code, QRD-2, 3-85

Query ID, QRD-4, 3-85

Query Parameter Definition

QPD-1, Message query name, 3-80

QPD-2, Query tag, 3-80

QPD-3, User parameters, 3-80

QPD-4, User parameters, 3-82

QPD-5, User parameters, 3-83

QPD-6, User parameters, 3-83

Query Parameter Definition Segment, 3-79

Query Priority, QRD-3, 3-85

Query priority, RCP-1, 3-91

Query Response Instance

QRI-1, Candidate confidence, 3-89

QRI-2, Match reason code, 3-89

QRI-3, Algorithm descriptor, 3-90

Query Response Instance Segment, 3-89

Query Response Status, QAK-2, 3-77

Query Results Level, QRD-12, 3-88

Query Tag, QAK-1, 3-77

Query tag, QPD-2, 3-80

Query Tag, VTQ-1, 3-100

Query/Response Format Code, VTQ-2, 3-100

R

Race, PID-10, 3-58

RCP, 3-91

RDF, 3-95

Field Definitions, 3-95

RDT, 3-98

Field Definitions, 3-98

Real-Time Connection Query batch msg

Commit ACK sent from MVI, 2-59

Receiving Application, MSH-5, 3-35

Receiving Facility, MSH-6, 3-35

Record Level Error Return, MFA-4, 3-15

Recorded Date/Time, EVN-2, 3-11

Record-level Event Code, MFA-1, 3-14

Record-level Event Code, MFE-1, 3-17

Reference Batch Control ID, BHS-12, 3-6

Reference Materials, xxxi

References

VistA, 1-4

Register a Patient

ADT-A04, 2-29

App ACK sent from MVI to sending system, 2-30

Commit ACK returned to MVI from sending system, 2-31

Commit ACK sent from MVI to sending system, 2-30

msg sent to MVI, 2-30

option, 2-29

registration process

Enterprise Search, 21

Religion, PID-17, 3-61

Response

Commit ACK returned from MVI to sending system, 2-21

Commit ACK sent from MVI to sending system, 2-20

RSP-K22 from PSIM when MVI has sent a QBP-Q22 to search for match(es), 2-22

site not found in MVI SITE MONITOR file

message example

sent to the site, 2-20

Site/DFN pair found on MVI (msg sent to sending system), 2-18, 2-21

Response Control Parameter

RCP-1, Query priority, 3-91

RCP-2, Quantity limited request, 3-92

RCP-3, Response modality, 3-92

RCP-4, Execution and delivery time, 3-93

RCP-5, Modify indicator, 3-93

RCP-6, Sort-by field, 3-93

RCP-7, Segment group inclusion, 3-94

Response Control Parameter Segment, 3-91

Response Level Code, MFI-6, 3-21

Response modality, RCP-3, 3-92

Revision History

Patches, xvi

RPC

Field Definitions, 3-91

RSP-K22 (Response), 2-17

Commit ACK returned from MVI to sending system, 2-21

Commit ACK sent from MVI to sending system, 2-20

msg sent to MVI, 2-18, 2-21

msg sent to sending system, 2-20

RSP-K22 (response) from PSIM when MVI sent QBP-Q22 to search for match(es), 2-22

S

SDAM APPT CHECK IN/OUT option, 2-8

Segment group inclusion, RCP-7, 3-94

segments, 3-2

BHS, 3-2

BTS, 3-7

DSC, 3-8

ERR, 3-9

EVN, 3-10

MFA, 3-14

MFE, 3-17

MFI, 3-20

MRG, 3-22

MSA, 3-25

MSH, 3-29

NTE, 3-39

OBX, 3-41

PD1, 3-47

PID, 3-49

example, 3-50

PV1, 3-69

PV2, 3-73

QAK, 3-76

QPD, 3-79

QRD, 3-84

QRI, 3-89

RCP, 3-91

RDF, 3-95

RDT, 3-98

VTQ, 3-100

ZCT, 3-105

ZEL, 3-106

ZEM, 3-107

ZET, 3-108

ZFF, 3-109

ZPD, 3-110

ZSP, 3-114

Selection Criteria, VTQ-5, 3-101

Self Identified Gender, 2-33, 3-41

Sending Application, MSH-3, 3-33

Sending Facility, MSH-4, 3-34

Set ID–NTE, NTE-1, 3-39

Set ID—PID, PID-1, 3-53

Social Security Numbers

test data, xxix

Sort-by field, RCP-6, 3-93

Source of Comment, NTE-2, 3-39

Species Code, PID-35, 3-67

SSN number—patient, PID-19, 3-64

SSN number—patient, PID-20, 3-64

Strain, PID-37, 3-68

Strain, PID-38, 3-68

T

Table Row Data

RDT-1, Column Value, 3-98

Table Row Data Segment, 3-98

Table Row Definition

RDF-1, Number of Columns Per Row, 3-95

RDF-2, Column Description, 3-95

Table Row Definition Segment, 3-95

tables

0002—Marital status, 3-61

0003 EVN—ADT/R Event Type Codes, 3-11

0005—Race, 3-58, 4-1

0008—Acknowledgement Code, 3-26

0048—What Subject Filter, 3-87

0062—Event Reason, 3-12

0091—Query priority, 3-91

0091—Query Priority, 3-85

0102─Delayed Acknowledgement type, 3-27

0103—Processing ID, 3-36

0104—Version ID, 3-37

0105—Source of Comment, 3-40

0106—Query/Response Format Code, 3-85

0126—Quantity limited request, 3-92

0126—Quantity Limited Request, 3-86

0136—Yes/no indicator, 3-49

0155—Accept/Application Acknowledgement Conditions, 3-38

0175—Master File Identifier Code, 3-20

0178—File Level Event Code, 3-21

0179—Response Level, 3-21

0180—Record-level Event Code, 3-17

0181—MFN-4 Record-level Error Return, 3-15

0188─Operator ID, 3-12

0189—Ethnic group, 3-65

0200—Name type, 3-57

0202—Telecommunication Equipment Type, 3-60

0203—Identifier type, 3-55

0208—Query Response Status, 3-77

0209—Relational operator, 3-103

0210—Relational conjunction, 3-103

0355─Primary key value type, 3-16

0357—Message Error Condition Codes, 3-27

0361—Sending/Receiving Application, 3-34

0362—Sending/Receiving Facility, 3-35

0391—Segment group, 3-94

0394—Response modality, 3-93

0395—Modify indicator, 3-93

0398—Continuation style code, 3-8

0399—Country Code, 3-38

0445—Identity Reliability Code, 3-66

BHS—Batch Header, 3-2

BTS—Batch Trailer, 3-7

DSC—Continuation Pointer, 3-8

ERR—Error, 3-9

EVN—Event Type, 3-10

HL7 field designation numbers and translations, 3-96, 3-98

MFA—Master File Acknowledgement, 3-14

MFE—Master File Entry, 3-17

MFI—Master File Identification, 3-20

MRG—Merge Patient Information, 3-22

MSA—Message Acknowledgement, 3-25

MSH—Message Header, 3-29

NPCD 001─National Patient Care Database Error Codes, 4-13

NTE—Notes and Comments, 3-39

OBX—Observation/Result, 3-46

PD1—Patient Additional Demographic, 3-47

PID—Patient Identification, 3-50

PV1—Patient Visit, 3-69

PV2—Patient Visit Segment – Additional Information, 3-73

PV2—Query Response Instance Segment, 3-89

QAK—Query Acknowledgement, 3-76

QPD─Query Parameter Definition, 3-79

QRD—Original-Style Query Definition, 3-84

RCP—Response Control Parameter, 3-91

RDF—Table Row Definition, 3-95

RDT—Table Row Data, 3-98

VA Patient identifiers, 3-87

VA001─Yes/No, 4-1

VA002─Current Means Test Status, 4-1

VA004─Eligibility, 4-2

VA005─Disability Retirement From Military, 4-3

VA006─Eligibility Status, 4-3

VA008─Religion, 4-4

VA010─Means Test Indicator, 4-7

VA011─Period of Service, 4-8

VA012─Type of Insurance, 4-9

VA015─Enrollment Status, 4-10

VA016─Reason Canceled/Declined, 4-11

VA021─Enrollment Priority, 4-11

VA022─Radiation Exposure Method, 4-11

VA023─Prisoner of War Location, 4-12

VA024─Source of Enrollment, 4-12

VA036─MST Status, 4-12

VA046─Agent Orange Exposure Location, 4-13

VTQ—Virtual Table Query Request, 3-100

ZCT―VA Specific Emergency Contact, 3-105

ZEL―VA Specific Patient Eligibility, 3-106

ZEM―VA Specific Employment Information, 3-107

ZET—Event Reason for Date of Last Treatment, 3-108

ZFF―VA Specific File/Field, 3-109

ZPD―VA Specific Patient Information, 3-110

ZSP―VA Specific Service Period, 3-114

test data

patient & user names, xxix

Social Security Numbers, xxix

Text message, MSA-3, 3-27

TREATING FACILITY File (#391.91), 1-4, 3-11, 3-13

U

Unlink Patient Information

ADT-A37, 2-60

App ACK sent to MVI, 2-61

Commit ACK sent from MVI to sending system, 2-61

Commit ACK sent to MVI, 2-61

msg sent to MVI, 2-61

UPDATE BATCH JOB FOR HL7 v2.3, 1-3

Update CMOR

ADT-A31, 2-40

Commit ACK sent to MVI from CMOR, 2-41

Commit ACK sent to MVI from VistA, 2-41

msg sent to the MVI requesting CMOR change, 2-40

received at CMOR for approving/disapproving CMOR change request, 2-41

Update Patient Information

ADT-A08, 2-32

App ACK sent from MVI to receiving system, 2-33

Commit ACK returned to MVI from receiving system, 2-34

Commit ACK sent from MVI to receiving system, 2-33

msg sent to MVI, 2-33

SELF ID GENDER, 2-33

Update Person Information

ADT-A31, 2-35

App ACK sent from MVI to VistA, 2-37

App ACK sent to PSIM from MVI, 2-39, 2-46

App ACK sent to VistA from MVI, 2-38, 2-44

Commit ACK returned to MVI from VistA, 2-37

Commit ACK sent from MVI to VistA, 2-36

Commit ACK sent from PSIM with error condition reported, 2-39

Commit ACK sent to PSIM from MVI, 2-38, 2-45

Commit ACK sent to VistA, 2-42

Commit ACK sent to VistA from MVI, 2-37, 2-44

Event A31, 2-43

message example

sent requesting CMOR change, 2-40, 2-43

sent from MVI to PSIM, 2-38, 2-45

sent from MVI to VistA, 2-37, 2-44

sent from VistA to MVI, 2-36

Update Treating Facility

App ACK sent to MVI, 2-49, 2-51

Assigning Authority parsed from MFE, 2-49, 2-50

Commit ACK returned from MVI to sending system, 2-49, 2-51

Commit ACK sent to MVI, 2-48, 2-51

Id Type parsed from MFE, 2-49, 2-50

MFN-M05, 2-47

Parse MFE more than 245 characters long, 2-50

received from MVI, 2-48, 2-51

URLs

CSSP & VistA Legacy

Acronyms Web page address, 30

Glossary Web page address, 30

User parameters, QPD-3, 3-80

User parameters, QPD-4, 3-82

User parameters, QPD-5, 3-83

User parameters, QPD-6, 3-83

User-defined tables

0002—Marital status, 3-61

0005—Race, 3-58

0062—Event Reason, 3-12

0181—MFN-4 Record-level Error Return, 3-15

0188─Operator ID, 3-12

0189—Ethnic group, 3-65

0200—Name type, 3-57

0361—Sending/Receiving Application, 3-34

0362—Sending/Receiving Facility, 3-35

0445—Identity Reliability Code, 3-66

VA Patient identifiers, 3-87

V

VA HL7 tables

NPCD 001─National Patient Care Database Error Codes, 4-13

VA001─Yes/No, 4-1

VA002─Current Means Test Status, 4-1

VA004─Eligibility, 4-2

VA005─Disability Retirement From Military, 4-3

VA006─Eligibility Status, 4-3

VA008─Religion, 4-4

VA010─Means Test Indicator, 4-7

VA011─Period of Service, 4-8

VA012─Type of Insurance, 4-9

VA015─Enrollment Status, 4-10

VA016─Reason Canceled/Declined, 4-11

VA021─Enrollment Priority, 4-11

VA022─Radiation Exposure Method, 4-11

VA023─Prisoner of War Location, 4-12

VA024─Source of Enrollment, 4-12

VA036─MST Status, 4-12

VA046─Agent Orange Exposure Location, 4-13

ZCT―VA Specific Emergency Contact, 3-105

ZEL―VA Specific Patient Eligibility, 3-106

ZEM―VA Specific Employment Information, 3-107

ZET—Event Reason for Date of Last Treatment, 3-108

ZFF―VA Specific File/Field, 3-109

ZPD―VA Specific Patient Information, 3-110

ZSP―VA Specific Service Period, 3-114

VA Specific Emergency Contact Segment (ZCT), 3-105

VA Specific Employment Information Segment (ZEM), 3-107

VA Specific Event Reason for Date of Last Treatment

ZET-1, VA Specific Event Reason for Date of Last Treatment Segment

Event Reason Code Name, 3-108

ZET-2, Patient Primary Facility, 3-108

VA Specific Event Reason for Date of Last Treatment Segment, 3-108

VA Specific Event Reason for Date of Last Treatment, ZET-1, 3-108

VA Specific File/Field Segment, 3-109

VA Specific Patient Eligibility Segment (ZEL), 3-106

VA Specific Patient Information

VTQ-34, VT Query Name, 3-113

ZET-17, VA Specific Event Reason for Date of Last Treatment Segment

Event Reason Code Name, 3-112

VA Specific Patient Information Segment, 3-110

VA Specific Service Period Segment, 3-114

Version ID, MSH-12, 3-37

Veteran’s Health Identity Card (VHIC), 3-56

Veterans military status, PID-27, 3-65

VHIC, 3-56

VHIC number(s) added to PID-4 segment, 3-56

Virtual Table Name, VTQ-4, 3-101

Virtual Table Query Request

VTQ-1, Query Tag, 3-100

VTQ-2, Query/Response Format Code, 3-100

VTQ-3, VT Query Name, 3-101

VTQ-4, Virtual Table Name, 3-101

VTQ-5, Selection Criteria, 3-101

Virtual Table Query Request Segment, 3-100

VistA References, 1-4

VQQ-Q02 (Query for Patient Matches), 2-56

real-time connection query returned from MVI, 2-57

real-time connection query returned from MVI (batch message example), 2-59

real-time connection query sent to MVI, 2-56

real-time connection query sent to MVI (batch message example), 2-58

VQQ-Q02 (Query for Patient Matches—Batch format), 2-58

VT Query Name, VTQ-3, 3-101

VT Query Name, VTQ-34, 3-113

VTQ, 3-100

Field Definitions, 3-100

W

Web pages

CSSP & VistA Legacy

Acronyms Web Page address, 30

Glossary Web page address, 30

HL7 Standards Documentation Web page address, xxxi

What Data Code Value Qual, QRD-11, 3-88

What Department Data Code, QRD-10, 3-88

What Subject Filter, QRD-9, 3-87

Who subject Filter, QRD-8, 3-86

Z

ZCT―VA Specific Emergency Contact Segment, 3-105

ZEL―VA Specific Patient Eligibility Segment, 3-106

ZEM―VA Specific Employment Information Segment, 3-107

ZET—VA Specific Event Reason for Date of Last Treatment Segment, 3-108

Field Definitions, 3-108

ZFF―VA Specific File/Field Segment, 3-109

ZPD-34

PSEUDO SSN REASON, 3-113

ZPD―VA Specific Patient Information Segment, 3-110

Field Definitions, 3-112

ZSP―VA Specific Service Period Segment, 3-114

[^1]: Available from ISO 1 Rue de Varembe, Case Postale 56, CH 1211, Geneve, Switzerland