---
title: Virtual Patient Record (VPR) Developer's Guide
doc_type: DG
doc_label: Developer Guide
doc_layer: plain
doc_subject: 
app_code: VPR
app_name: Virtual Patient Record
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 17
description: 
audience: 
keywords: 
  - span
  - table
  - class
  - patient
  - optional
  - strong
  - contents
  - date
  - filter
  - anchor
page_count: 0
word_count: 31133
section_count: 54
table_count: 65
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: January 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/virtual_patient_record/vpr_dg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/virtual_patient_record/vpr_dg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=197"
---

---
title: |
  Virtual Patient Record (VPR) 1.0

  Developer’s Guide
---

![](virtual-patient-record-vpr-developer-s-guide/001.png)

January 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Software Product Management (SPM)

<span id="_Toc155864193" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref386466976" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 48%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/24/2024</td>
<td>1.9</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated entries in <u>Table 3</u>, <u>Table 5</u>, <u>Table 11</u>, <u>Table 12</u>, <u>Table 20</u>, <u>Table 21</u>, <u>Table 22</u>, <u>Table 23</u>, <u>Table 26</u>, <u>Table 27</u>, <u>Table 28</u>, <u>Table 29</u>, and <u>Table 36</u>.</p></li>
<li><p>Updated Section <u>5</u>, <u>5.1</u>, <u>5.2</u>, <u>5.2.1</u>, <u>5.2.3</u>, <u>5.2.3.2</u>, <u>5.2.3.3</u>, <u>5.5.1</u>, and <u>5.6</u>.</p></li>
<li><p>Section <u>5.1</u>: Deleted the “VPR Entities” table.</p></li>
<li><p>Deleted the “VPR Subscription File and Indexes” section.</p></li>
<li><p>Added Section <u>5.3</u> and all subsections.</p></li>
</ul></td>
<td>Virtual Patient Record (VPR) Development Team</td>
</tr>
<tr class="even">
<td>10/10/2023</td>
<td>1.8</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>3</u>: Added <strong>DFN</strong> or <strong>patientId</strong> to RPC tables.</p></li>
<li><p>Section <u>3.16</u>:</p></li>
</ul>
<ul>
<li><p>Updated the FILTER input parameter.</p></li>
<li><p><u>Table 27</u>: Added two new properties that are being added in the next VPR patch.</p></li>
</ul>
<ul>
<li><p>Section <u>4</u>: Changed JSON filter names back to lowercase.</p></li>
<li><p>Section <u>5.2</u>: Added new events to tables.</p></li>
<li><p>Section <u>3.18</u>, <u>5.4.2</u>, <u>5.4.3</u>, and <u>5.4.8</u>: Made a few other miscellaneous updates.</p></li>
<li><p><u>Table 60</u>: Added <strong>MDC OBSERVATION UPDATE</strong> event protocol.</p></li>
<li><p><u>Table 61</u>: Added TIU MULTIPLE SIGNATURE (#8925.7) file.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>07/06/2023</td>
<td>1.7</td>
<td><p>Updates for VPR Patches VPR*1*30 and 31:</p>
<ul>
<li><p>Section <u>2.3.1</u> and <u>2.4.1</u>: Added specific prompt references and text regarding results display options.</p></li>
<li><p>Updated <u>Figure 2</u> and <u>Figure 4</u>: Added prompt to continue display.</p></li>
<li><p>Section <u>3.1</u>, <u>3.8</u>, <u>3.8.1</u>, <u>3.8.2</u>, <u>3.11</u>, <u>3.13</u>, <u>3.15</u>, <u>4.4</u>, <u>4.5</u>, and <u>4.12</u>: Updated FILTER parameter.</p></li>
<li><p>Section <u>3.9</u>: Many orders not most.</p></li>
<li><p>Section <u>3.10</u>: In NOTE: “<strong>Visit</strong>” <em>not</em> “<strong>VistA</strong>.”</p></li>
<li><p>Section <u>3.12</u> and <u>3.12.1</u>: Moved text to another section.</p></li>
<li><p>Added Section <u>3.12.5</u>, “<u>Medications by Order</u>.”</p></li>
<li><p>Added Section <u>3.18</u>, “<u>Text Integration Utilities (TIU)</u>.”</p></li>
<li><p><u>Table 29</u>: Updated <strong>category</strong> entry; removed “<strong>RA</strong>” value.</p></li>
<li><p>Added Section <u>3.18.1</u>, “<u>Clinical Procedure/Medicine Reports</u>”; added <u>Table 30</u>.</p></li>
<li><p>Added Section <u>3.18.2</u>, “<u>Laboratory Reports</u>”; added <u>Table 31</u>.</p></li>
<li><p>Added Section <u>3.18.3</u>, “<u>Radiology Reports</u>”; added <u>Table 32</u>.</p></li>
<li><p>Table:</p></li>
</ul>
<ul>
<li><p>Added <strong>VPR DEL INSURANCE</strong>, <strong>VPR INSURANCE EXTENSION</strong>, and <strong>VPR SOCIAL HX EXTENSION</strong> entries.</p></li>
<li><p>Updated <strong>VPR INSURANCE PLAN</strong> entry.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>02/01/2023</td>
<td>1.6</td>
<td><p>Updates for VPR Patch VPR*1*30:</p>
<ul>
<li><p>Table: Added the VPR DEL PTF 601, VPR DOCUMENT CLASS, VPR FAM HX EXTENSION, VPR ICD OP, VPR MAS SPECIALTY, VPR MED SPECIALTY, VPR ORDER DC EVENT, VPR ORDER DIALOG, VPR ORDER EVENT, VPR PATIENT TYPE, VPR PTF 601, VPR PTF 601 EXTENSION, VPR RELEASE EVENT, VPR SERVICE, VPR SURG SPECIALTY, VPR UNITS, VPR VPOV EXTENSION, and VPR VXAM EXTENSION entries.</p></li>
<li><p><u>Table 59</u>: Added the PSO VDEF RDS O13 OP PHARM PPAR VS and PSO VDEF RDS O13 OP PHARM PREF VW entries.</p></li>
<li><p><u>Table 60</u>: Added the DG PTF ICD PROCEDURE NOTIFIER entry.</p></li>
<li><p>Section <u>5.5.2</u>, “<u>Print an Entity Option</u>:” Retitled to match option name.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>07/05/2022</td>
<td>1.5</td>
<td><p>Updates:</p>
<ul>
<li><p>Table: Updated "<strong>Display Name</strong>" and "<strong>Primary Source Sub/File#</strong>" columns for these entries: <strong>VPR DEL FAMILY HX</strong>, <strong>VPR DEL HF VACC REFUSAL</strong>, <strong>VPR DEL ICR</strong> (new), <strong>VPR DEL PTF</strong>, <strong>VPR DEL SOCIAL HX</strong>, <strong>VPR DEL TIU DOCUMENT</strong>, <strong>VPR DEL V CPT</strong>, <strong>VPR DEL V EXAM</strong>, <strong>VPR DEL V POV</strong>, <strong>VPR DEL VACCINATION</strong>, <strong>VPR ELIGIBILITY</strong> (new), <strong>VPR ICR ADMINISTRATION</strong> (new), <strong>VPR ICR CONTRAINDICATION</strong> (new), <strong>VPR ICR EVENT</strong> (new), <strong>VPR ICR EXTENSION</strong> (new), <strong>VPR ICR OBSERVATION</strong> (new), <strong>VPR ICR REFUSAL</strong> (new), and <strong>VPR IMM MANUFACTURER</strong> (new).</p></li>
<li><p>Updated Section <u>5.2.3.2</u>, "<u>Encounters (PCE)</u>:" <strong>XTMP</strong> check times.</p></li>
<li><p>Updated <u>Figure 18</u>: Added VPR ICR EVENT.</p></li>
<li><p>Updated Section <u>5.5.2</u>, "<u>Print an Entity Option</u>:" <u>Figure 19</u>.</p></li>
<li><p>Added Section <u>5.7</u>, "<u>Call To Populate</u>:" Added sub-sections and figures.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>11/03/2021</td>
<td>1.4</td>
<td><p>Updates:</p>
<ul>
<li><p><u>Table 37</u>: Added the <strong>locationName</strong> and <strong>locationUid</strong> entries.</p></li>
<li><p><u>Table 39</u>: Added the <strong>displayOrder</strong> and <strong>vuid</strong> entries.</p></li>
<li><p><u>Table 40</u>: Added the <strong>instructions</strong> and <strong>orderUid</strong> entries.</p></li>
<li><p><u>Table 49</u>: Added the <strong>parent</strong> entry.</p></li>
<li><p>Table 50: Added the <strong>service</strong> entry.</p></li>
<li><p><u>Table 55</u>: Deleted <strong>cpt</strong> entry.</p></li>
<li><p>Table: Added the <strong>VPR DEL FAMILY HX</strong>, <strong>VPR DEL HF VACC REFUSAL</strong>, <strong>VPR DEL PTF</strong>, <strong>VPR DEL SOCIAL HX</strong>, <strong>VPR DEL TIU DOCUMENT</strong>, <strong>VPR DEL V CPT</strong>, <strong>VPR DEL V EXAM</strong>, <strong>VPR DEL V POV</strong>, <strong>VPR DEL VACCINATION</strong>, and <strong>VPR TEXT ONLY</strong> entries.</p></li>
<li><p><u>Table 60</u>: Added the <strong>TIU DOCUMENT ACTION EVENT</strong> entry.</p></li>
<li><p>Added Sections <u>5.2.3</u>, “<u>Tasked Events</u>,” and <u>5.5.1</u>, “<u>VPR CONTAINER (#560.1) File.”</u></p></li>
<li><p>Updated Sections <u>5.2</u>: Added second paragraph, <u>5.2.2</u>: Clarified first sentence, <u>5.3</u>, <u>5.4.1</u>, and <u>5.5.2</u>: Added option names.</p></li>
<li><p>Updated <u>Figure 19</u>.</p></li>
<li><p>Section <u>5.3</u>: Added application programming interface (API) details.</p></li>
<li><p>Updated Section <u>5.5</u>: Intro text.</p></li>
<li><p>Added Section <u>5.6</u>, “<u>Monitoring and Troubleshooting</u>.”</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>03/26/2021</td>
<td>1.3</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated “<a href="#_Toc336755501">How to Use this Manual</a>” section.</p></li>
<li><p>Section <u>5</u>: VPR is currently populating <strong>21</strong> of the <strong>30</strong> SDA containers</p></li>
<li><p>Section: Add intro text.</p></li>
<li><p>Table: Corrected column title, delete some entries and added the following entries: <strong>VPR ADMISSION MOVEMENT</strong>, <strong>VPR EDP CODE</strong>, <strong>VPR EDP EXTENSION</strong>, <strong>VPR EDP LOG</strong>, <strong>VPR LAB FACILITY</strong>, <strong>VPR MAS MOVEMENT TYPE</strong>, <strong>VPR MAS TRANSACTION TYPE</strong>, <strong>VPR MDD PROCEDURE</strong>, <strong>VPR PACKAGE</strong>, <strong>VPR PRF DBRS RECORD</strong>, <strong>VPR PRF HISTORY</strong>, <strong>VPR REFERRING PROVIDER</strong>, <strong>VPR SCH ADM EXTENSION</strong>, <strong>VPR VACC HF ADMIN</strong>, <strong>VPR VACC HF EXT</strong>, <strong>VPR VACC HF REFUSAL</strong>, <strong>VPR VCPT EXTENSION</strong>, <strong>VPR VFILE DELETE</strong>, <strong>VPR VISIT STUB</strong>, and <strong>VPR WARD LOCATION</strong>.</p></li>
<li><p><u>Table 59</u>: Deleted an entry.</p></li>
<li><p><u>Table 60</u>: Added the following entries: <strong>DG PTF ICD DIAGNOSIS NOTIFIER</strong>, <strong>DG SA FILE ENTRY NOTIFIER</strong>, <strong>DGPF PRF EVENT</strong>, <strong>GMRA VERIFY DATA</strong>, and <strong>WV PREGNANCY STATUS CHANGE EVENT</strong>.</p></li>
<li><p>Section: added link to Section <u>5.2</u>.</p></li>
<li><p>Section <u>5.2.4.1</u>: Updated intro text.</p></li>
<li><p>Section <u>5.2.4.2</u>: Updated bulleted list and example.</p></li>
<li><p>Deleted some content and an entry.</p></li>
<li><p>Section <u>5.5</u>, “<u>Generating Online Documentation</u>:” Updated intro text.</p></li>
<li><p>Section <u>5.5.1</u>: Updated title and intro text.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>06/13/2019</td>
<td>1.2</td>
<td><p>Updates for Patch VPR*1.0*10 and VPR*1.0*14:</p>
<ul>
<li><p>Section <u>5</u>, “<u>HealthShare Interface</u>.”</p></li>
<li><p>Renamed/Updated Section <u>5.2</u>, “<u>Data Update Events</u>.”</p></li>
<li><p>Renamed/Updated Section <u>5.3</u>, “<u>Generating SDA Results</u>.”</p></li>
<li><p>Updated <u>VPRHS Utilities</u>.</p></li>
<li><p>Renumbered/Updated Section <u>5.4.1</u>, “<u>$$ON^VPRHS: System Monitoring On/Off</u>.”</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>04/24/2019</td>
<td>1.1</td>
<td><p>Updates for Patch VPR*1.0*8 and VPR*1.0*14:</p>
<ul>
<li><p>Updated stakeholders in the “<a href="#intended_audience">Intended Audience</a>” section.</p></li>
<li><p>Added Section <u>1.1</u>, “<u>Purpose</u>.”</p></li>
<li><p>Updated Section <u>1.2</u>.</p></li>
<li><p>Moved Section <u>1.5</u>, “<u>Formatted Data</u>,” to follow Section <u>1.4</u>.</p></li>
<li><p>Added explanatory text to Section <u>2</u>.</p></li>
<li><p>Updated Sections <u>2.1</u> and <u>2.2</u>.</p></li>
<li><p>Added the following “placeholder” sections for future content:</p></li>
</ul>
<ul>
<li><p>Section 5, “HealthShare Interface.”</p></li>
<li><p>Section 5.1, “Entity (#1.5) File VPR Entries.”</p></li>
<li><p>Section 5.2, “File 560 and AVPR and ANEW Indices.”</p></li>
<li><p>Section 5.3, “Protocol Events.”</p></li>
<li><p>Section 5.4, “Generating Online Documentation.”</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>09/25/2018</td>
<td>1.0</td>
<td><p>Updates for Patch VPR*1.0*8:</p>
<ul>
<li><p>Created a new, separate Developer’s Guide (this manual).</p></li>
<li><p>Moved other content to a new, separate Technical Manual.</p></li>
<li><p>Updated document to follow current documentation standards and style guidelines.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>08/21/2018</td>
<td>0.13</td>
<td><p>Updates for Patch VPR*1.0*7:</p>
<p>Added new data elements to tables.</p>
<p>Pages: 25, 31-32, 51-52, 60, 63-64, 67, 78-80.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>08/03/2015</td>
<td>0.12</td>
<td><p>Updates for Patch VPR*1.0*5:</p>
<p>Moved ICRs to end, and data element lists from Routine section to new Appendix A &amp; B.</p>
<p>Pages: 7, 10, 21-87.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>06/29/2015</td>
<td>0.11</td>
<td><p>Updates for Patch VPR*1.0*5:</p>
<ul>
<li><p>Removed Patch descriptions.</p></li>
<li><p>Updated Data Domains, ICRs, and Checksums.</p></li>
</ul>
<p>Pages: 4-5, 8-9, 11-56.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>01/16/2015</td>
<td>0.10</td>
<td><p>Updates for Patch VPR*1.0*4:</p>
<ul>
<li><p>Updated the VPR*1.0*4 Data Domain section to include Consults.</p></li>
<li><p>Updated Routines section to include VPRDGMRC and VPRDPSO.</p></li>
<li><p>Updated the External Relationships section with changes to the ^USC(8932.1 ICB number</p></li>
<li><p>Updated checksums for VPRDGMRC and VPRDPSO.</p></li>
</ul>
<p>Pages: 6, 12, 43-44.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>01/07/2015</td>
<td>0.09</td>
<td><p>Updates for Patch VPR*1.0*4:</p>
<p>Updated the checksum for VPRDTST to reflect a last-minute change; Page: 45.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>01/02/2015 to 01/06/2015</td>
<td>0.08</td>
<td><p>Updates for Patch VPR*1.0*4:</p>
<ul>
<li><p>Updated dates in page footers and on the cover page; Pages: All.</p></li>
<li><p>Added a prerequisite instruction for installing VPR*1.0*4; Page: 4.</p></li>
<li><p>Added a section describing VPR*1.0*4; Pages: 7-8.</p></li>
<li><p>Added two new ICRs to the External Relationships section; Page: 13.</p></li>
<li><p>Added a new routine (VPRTST) to the routine table; Page 41.</p></li>
<li><p>Updated checksums; Pages: 45-46.</p></li>
<li><p>Added a new option (VPR TEST XML) and new examples for VPR TEST XML and VPR TEST JSON; Pages: 47–50.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>09/11/2013 to 10/11/2013</td>
<td>0.07</td>
<td><p>Updates for Patch VPR*1.0*2:</p>
<ul>
<li><p>Updated Title-page fonts to meet end-user documentation standards.</p></li>
<li><p>Updated revision date.</p></li>
<li><p>Updated footer to include package name (re end-user documentation standards).</p></li>
<li><p>Addressed reviewer suggestions and comments.</p></li>
<li><p>Added an installation and a software-availability section to provide information about how to retrieve software and documentation (re end-user documentation standards).</p></li>
<li><p>Added a legal-disclaimers section (re end-user documentation standards).</p></li>
<li><p>Corrected errors in the routines section; updated checksums.</p></li>
</ul>
<p>Pages: All.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>07/24/2013</td>
<td>0.06</td>
<td><p>Updates for Patch VPR*1.0*2:</p>
<ul>
<li><p>Updated title to reflect new patch.</p></li>
<li><p>Updated Overview to add JSON information.</p></li>
<li><p>Added a new (Formatted Data) section to discuss data formatting.</p></li>
<li><p>Added patch information for VPR*1.0*2.</p></li>
<li><p>Added JSON remote procedure call information.</p></li>
<li><p>Added JSON routines.</p></li>
<li><p>Corrected capitalization in routines table.</p></li>
<li><p>Added a JSON example placeholder.</p></li>
<li><p>Added JSON checksums.</p></li>
<li><p>Updated the glossary section.</p></li>
</ul>
<p>Pages: All.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>07/30/2012</td>
<td>0.05</td>
<td><p>Updates for Patch VPR*1.0*1:</p>
<p>Updated checksum for VPRDPSOR; Page 27.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>06/13/2012</td>
<td>0.04</td>
<td><p>Updates for Patch VPR*1.0*1:</p>
<ul>
<li><p>Updated Clinical Procedures ICRs in Relationships, renumbered the table, increased row height when necessary; Pages 5-7.</p></li>
<li><p>Changed revised date; Pages 5-7.</p></li>
<li><p>Fixed typo; Page 11.</p></li>
</ul></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>05/18/2012</td>
<td>0.03</td>
<td><p>Updates for Patch VPR*1.0*1:</p>
<p>Added a paragraph about the VPR proxy; Page 2.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="even">
<td>05/15/2012</td>
<td>0.02</td>
<td><p>Updates for Patch VPR*1.0*1:</p>
<ul>
<li><p>Changed header colors from blue to black.</p></li>
<li><p>Corrected formatting issues.</p></li>
<li><p>Added hyperlinks to revision history.</p></li>
<li><p>Updated Overview to reflect changes with NwHIN.</p></li>
<li><p>Added new extract routines for Clinical Observations, Clinical Procedures, Insurance, Exams, Skin Tests, Patient Education.</p></li>
<li><p>Renamed Pharmacy Extract Medications.</p></li>
<li><p>Renamed Pharmacy Inpatient extract to Inpatient Meds.</p></li>
<li><p>Renamed Pharmacy Outpatient Extract Outpatient Meds.</p></li>
<li><p>Added Non-VA Meds and IV Fluids/Infusions extracts.</p></li>
<li><p>Added section for Implementation &amp; Maintenance.</p></li>
<li><p>Added section for patch description.</p></li>
<li><p>Modified list of new routines.</p></li>
<li><p>Updated Routines List with new and modified extract routines.</p></li>
<li><p>Added section for Security Keys.</p></li>
<li><p>Updated External relationships table.</p></li>
<li><p>Added section for Files.</p></li>
<li><p>Updated Routine List table with new/changed routines and reordered elements alphabetically.</p></li>
<li><p>Removed elements predecessor, successor, code from <strong>VPRDPL</strong> routine because they were never populated. Added elements acknowledgement [m], provider, and service to VPRDOR routine.</p></li>
<li><p>Added element category to <strong>VPRDPXHF</strong>.</p></li>
<li><p>Added element encounter to <strong>VPRDXIM</strong> routine.</p></li>
<li><p>Added elements <strong>clinicStop</strong>, <strong>provider</strong>, and <strong>type</strong> to <strong>VPRDSDAM</strong> routine (<strong>clinicStop</strong> was inadvertently missed in the previous version of this TM).</p></li>
<li><p>Added elements category, images and parent to <strong>VPRDTIU</strong> routine.</p></li>
<li><p>Updated Checksums table.</p></li>
<li><p>Added Options section.</p></li>
<li><p>Added a Glossary section.</p></li>
</ul>
<p>Pages: All.</p></td>
<td>VPR Development Team</td>
</tr>
<tr class="odd">
<td>08/08/2011</td>
<td>0.01</td>
<td>VPR Version 1.0 Release. Initial document.</td>
<td>VPR Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref386466976" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Table of Contents

<span id="_Toc155864194" class="anchor"></span>List of Figures

<span id="_Toc155864195" class="anchor"></span>List of Tables

<span id="_Ref38421374" class="anchor"></span>Orientation

<span id="_Toc336755501" class="anchor"></span>How to Use this Manual

The *Virtual Patient Record (VPR) Developer’s Guide* provides advice and instruction about the use of the following RPCs:

- <u>VPR GET PATIENT DATA</u>
- <u>VPR GET PATIENT DATA JSON</u>

This manual also describes the VPR interface with HealthShare.

![](virtual-patient-record-vpr-developer-s-guide/002.png) REF: For VPR installation instructions in the VistA environment see the *Virtual Patient Record (VPR) Installation Guide* and any national patch description of the patch being released.

<span id="intended_audience" class="anchor"></span>Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Software Product Management (SPM)—VistA legacy development teams who use the VPR RPCs; specifically, Veterans Health Information Exchange (VHIE) and Joint Legacy Viewer (JLV).
- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](virtual-patient-record-vpr-developer-s-guide/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

Documentation Disclaimer

This manual provides an overall explanation of and the functionality contained in Virtual Patient Record (VPR) 1.0; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet Websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](virtual-patient-record-vpr-developer-s-guide/004.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                                                                                                                                                           | Description                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](virtual-patient-record-vpr-developer-s-guide/005.png)   | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](virtual-patient-record-vpr-developer-s-guide/006.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref525631170" class="anchor"></span>Table 2: VPR Remote Procedure Calls

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<Application Name/Abbreviation/Namespace\>*PATIENT,*\<N\>*
- *\<Application Name/Abbreviation/Namespace\>*USER,*\<N\>*

Where:

- *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.
- *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in Virtual Patient Record (VPR) test patient and user names would be documented as follows:

- VPRPATIENT,ONE; VPRPATIENT,TWO; VPRPATIENT,THREE; … VPRPATIENT,14; etc.
- VPRUSER,ONE; VPRUSER,TWO; VPRUSER,THREE; … VPRUSER,14; etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box:
- User’s responses to online prompts are bold typeface and sometimes highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are sometimes represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](virtual-patient-record-vpr-developer-s-guide/007.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the MUMPS (M) programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, security keys, and RPCs (e.g., VPR GET PATIENT DATA).

![](virtual-patient-record-vpr-developer-s-guide/008.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to your customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](virtual-patient-record-vpr-developer-s-guide/009.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

![](virtual-patient-record-vpr-developer-s-guide/010.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate topic.  
  
REF: For further information, see the *VA FileMan Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](virtual-patient-record-vpr-developer-s-guide/011.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about Virtual Patient Record (VPR) should consult the following:

- *Virtual Patient Record (VPR) Installation Guide*
- *Virtual Patient Record (VPR) Technical Manual*
- *Virtual Patient Record (VPR) Developer’s Guide* (this manual)

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA software documentation can be downloaded from the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/>

![](virtual-patient-record-vpr-developer-s-guide/012.png) REF: VPR manuals are located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=197>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Enhancements](#enhancements)
  - [Background](#background)
  - [Formatted Data](#formatted-data)
- [Remote Procedure Calls](#remote-procedure-calls)
  - [VPR GET CHECKSUM](#vpr-get-checksum)
  - [VPR DATA VERSION](#vpr-data-version)
  - [VPR GET PATIENT DATA](#vpr-get-patient-data)
    - [VPR TEST XML Option](#vpr-test-xml-option)
  - [VPR GET PATIENT DATA JSON](#vpr-get-patient-data-json)
    - [VPR TEST JSON Option](#vpr-test-json-option)
- [XML Tables](#xml-tables)
  - [Allergy/Adverse Reaction Tracking (GMRA)](#allergyadverse-reaction-tracking-gmra)
  - [Clinical Observations (MDC)](#clinical-observations-mdc)
  - [Clinical Procedures (MC)](#clinical-procedures-mc)
  - [Clinical Reminders (PXRM)](#clinical-reminders-pxrm)
  - [Consult/Request Tracking (GMRC)](#consultrequest-tracking-gmrc)
  - [Functional Independence Measurements (RMIM)](#functional-independence-measurements-rmim)
  - [Integrated Billing (IB)](#integrated-billing-ib)
  - [Laboratory (LR)](#laboratory-lr)
    - [Accessions](#accessions)
    - [Panels](#panels)
  - [Orders (OR)](#orders-or)
  - [Patient Care Encounter (PX)](#patient-care-encounter-px)
    - [Exams](#exams)
    - [Education Topics](#education-topics)
    - [Health Factors](#health-factors)
    - [Immunizations](#immunizations)
    - [Skin Tests](#skin-tests)
  - [Patient Record Flags (DGPF)](#patient-record-flags-dgpf)
  - [Pharmacy (PS)](#pharmacy-ps)
    - [Inpatient (Unit Dose) Medications](#inpatient-unit-dose-medications)
    - [IV Fluids (Infusions)](#iv-fluids-infusions)
    - [Outpatient Medications](#outpatient-medications)
    - [Non-VA Medications](#non-va-medications)
    - [Medications by Order](#medications-by-order)
  - [Problem List (GMPL)](#problem-list-gmpl)
  - [Radiology/Nuclear Medicine (RA)](#radiologynuclear-medicine-ra)
  - [Registration (DPT)](#registration-dpt)
  - [Scheduling (SDAM)](#scheduling-sdam)
  - [Surgery (SR)](#surgery-sr)
  - [Text Integration Utilities (TIU)](#text-integration-utilities-tiu)
    - [Clinical Procedure/Medicine Reports](#clinical-proceduremedicine-reports)
    - [Laboratory Reports](#laboratory-reports)
    - [Radiology Reports](#radiology-reports)
  - [Visits/PCE (PX)](#visitspce-px)
  - [Vital Measurements (GMV)](#vital-measurements-gmv)
- [JSON Tables](#json-tables)
  - [Allergy/Adverse Reaction Tracking (GMRA)](#allergyadverse-reaction-tracking-gmra-1)
  - [Clinical Observations (MDC)](#clinical-observations-mdc-1)
  - [Clinical Procedures (MDC)](#clinical-procedures-mdc)
  - [Consult/Request Tracking (GMRC)](#consultrequest-tracking-gmrc-1)
  - [Laboratory (LR)](#laboratory-lr-1)
  - [Orders (OR)](#orders-or-1)
  - [Patient Care Encounter (PX)](#patient-care-encounter-px-1)
    - [CPT Procedures](#cpt-procedures)
    - [Exams](#exams-1)
    - [Education Topics](#education-topics-1)
    - [Health Factors](#health-factors-1)
    - [Immunizations](#immunizations-1)
    - [Purpose of Visit](#purpose-of-visit)
    - [Skin Tests](#skin-tests-1)
  - [Pharmacy (PS)](#pharmacy-ps-1)
    - [Medications](#medications)
    - [Infusions](#infusions)
  - [Problem List (GMPL)](#problem-list-gmpl-1)
  - [PTF (DG)](#ptf-dg)
  - [Radiology/Nuclear Medicine (RA)](#radiologynuclear-medicine-ra-1)
  - [Registration (DPT)](#registration-dpt-1)
  - [Scheduling (SDAM)](#scheduling-sdam-1)
  - [Surgery (SR)](#surgery-sr-1)
  - [Text Integration Utilities (TIU)](#text-integration-utilities-tiu-1)
  - [Visits/PCE (PX)](#visitspce-px-1)
  - [Vital Measurements (GMV)](#vital-measurements-gmv-1)
- [HealthShare Interface](#healthshare-interface)
  - [Process Flow](#process-flow)
  - [Data Update Events](#data-update-events)
    - [Protocol Events](#protocol-events)
    - [MUMPS Index](#mumps-index)
    - [Tasked Events](#tasked-events)
    - [VPR Subscription File](#vpr-subscription-file)
  - [Generating SDA Results](#generating-sda-results)
    - [SDA Containers](#sda-containers)
    - [Reference Files](#reference-files)
    - [Deleting Records](#deleting-records)
    - [Container File](#container-file)
  - [VPRHS Utilities](#vprhs-utilities)
    - [\$\$ON^VPRHS: System Monitoring On/Off](#onvprhs-system-monitoring-onoff)
    - [EN^VPRHS(): Subscribe a Patient](#envprhs-subscribe-a-patient)
    - [UN^VPRHS(): Unsubscribe a Patient](#unvprhs-unsubscribe-a-patient)
    - [\$\$SUBS^VPRHS(): Subscription Status of a Patient](#subsvprhs-subscription-status-of-a-patient)
    - [\$\$VALID^VPRHS(): Validation of a Patient for HealthShare](#validvprhs-validation-of-a-patient-for-healthshare)
    - [POST^VPRHS(): Add Record to AVPR Index for Uploading](#postvprhs-add-record-to-avpr-index-for-uploading)
    - [NEW^VPRHS(): Add Patient to ANEW Index for Subscribing](#newvprhs-add-patient-to-anew-index-for-subscribing)
    - [DEL^VPRHS(): Remove Nodes from ANEW or AVPR Upload Index](#delvprhs-remove-nodes-from-anew-or-avpr-upload-index)
    - [GET^VPRHS(): Retrieve Patient Data for ECR](#getvprhs-retrieve-patient-data-for-ecr)
    - [TEST^VPRHS(): Test SDA Extract](#testvprhs-test-sda-extract)
  - [Generating Online Documentation](#generating-online-documentation)
    - [VPR CONTAINER (#560.1) File](#vpr-container-5601-file)
    - [Print an Entity Option](#print-an-entity-option)
  - [Monitoring and Troubleshooting](#monitoring-and-troubleshooting)
    - [VPR HealthShare Utilities \[VPR HS MENU\] Menu](#vpr-healthshare-utilities-vpr-hs-menu-menu)
    - [Test/Audit VPR Functions \[VPR HS TESTER\] Menu](#testaudit-vpr-functions-vpr-hs-tester-menu)
  - [Call To Populate](#call-to-populate)
    - [VPRZCTP](#vprzctp)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide technical information about the Virtual Patient Record (VPR) 1.0 software, specifically for developer use.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR 1.0 was originally developed as a part of the Health Informatics Initiative’s (hi<sup>2</sup>’s). It has been expanded to support VA’s interfaces to InterSystems’ Health Connect (HC) and HealthShare (HS).

VPR extracts patient data from domains at a local Veterans Health Information Systems and Technology Architecture (VistA) site to provide a cached view of the patient chart. It provides normalized fields with common field names and data structures across domains.

VPR includes four remote procedure calls (RPCs) that do the following:

- Extract data from VistA in Extensible Markup Language (XML) format.
- Extract VistA data in JavaScript Object Notation (JSON) format.
- Calculates checksums for data returned via the XML or JSON RPC.
- Returns the current VPR RPC version number.

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR Patch VPR\*1\*8 extends the Virtual Patient Record (VPR) application, to provide a new method of retrieving patient health data from a VistA database.

VA FileMan Patch DI\*22.2\*9 released a new VA FileMan utility that provides the ability to map VistA files and fields to other data models and extract that data as XML or JSON objects. Patch VPR\*1\*8 populates the ENTITY (#1.5) file to map VistA data elements to InterSystems' Summary Data Architecture (SDA) model and use the supported calls to retrieve the requested data.

Patch VPR\*1\*8 also installs a mechanism to monitor clinical data events in VistA, to enable retrieval of updated information as a patient's data changes. This patch adds new PROTOCOL (#101) file entries and links to appropriate clinical application events; the file and record numbers modified will be collected in the VPR SUBSCRIPTION (#560) file until retrieved and updated.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR RPC for XML-formatted data extraction was initially installed in the Nationwide Health Information Network (NwHIN) namespace, which was called NHIN. The NwHIN client used most of the VPR’s extract routines in production to get and share data. After this initial installation, VPR RPCs were installed in the VPR’s own (VPR) namespace and renumbered as VPR Version 1.0. NwHIN could continue to use the extract routines in its NHIN namespace, but would need to access VPR 1.0, or subsequent versions, to take advantage of future extract routine enhancements.

![](virtual-patient-record-vpr-developer-s-guide/013.png) NOTE: After the VPR package installed its RPCs in its own (VPR) namespace with VPR 1.0, NwHIN began to use VPR 1.0 to take advantage of future extract-routine enhancements. The Virtual Lifetime Electronic Record (VLER) and Joint Legacy Viewer (JLV) are currently the primary users of the RPCs.

## Formatted Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR provides XML- and JSON-formatted data to support web applications that transmit data between themselves, servers, and users’ browsers.

As its name suggests, XML uses markup to structure and serialize data. This human- and machine-readable format enjoys widespread use as a means of exchanging both text-based documents and structured data.

![](virtual-patient-record-vpr-developer-s-guide/014.png) REF: <u>Figure 1</u> contains a snippet of XML-formatted data.

JSON is also a human- and machine-readable data-interchange format; however, its creator focused on making it a vehicle for transmitting structured data, rather than narrative documents. Although it uses several JavaScript notation rules to represent structured data, JSON is programming-language agnostic: JSON parser libraries are available for programming languages that range from ActionScript to Visual Basic.

![](virtual-patient-record-vpr-developer-s-guide/015.png) REF: You can find a comprehensive list of available parser libraries on the [JSON.org](http://www.json.org) website.

JSON supports four primitive and two structured data types:

- Primitive data types:
- Text strings (quotation-mark delimiters)
- Numbers
- Booleans
- Null
- Structured data types:
- Objects
- Arrays

These data types provide a fluid (free-form) way to serialize data transmissions. For example, developers can represent objects that encompass arrays and arrays that encompass objects. They can also include *non*-significant white space around JSON’s structural elements (curly and block brackets, colons, and commas) to enhance human readability.

![](virtual-patient-record-vpr-developer-s-guide/016.png) REF: <u>Figure 3</u> contains a snippet of JSON-formatted data.

Like XML, JSON supports asynchronous JavaScript and XML (Ajax), which allows web applications to send and receive data to and from web pages. As a result, both formats are viable options for data interchanges involving web applications. Two notable cases in point are HMP, which uses JSON-formatted data, and NwHIN, which uses XML-formatted data.

# Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> lists the RPCs released with VPR 1.0:

| Remote Procedure Call                | M Entry Point | Category         |
|--------------------------------------|---------------|------------------|
| <u>VPR GET CHECKSUM</u>          | CHECK^VPRDCRC | Supporting RPC   |
| <u>VPR DATA VERSION</u>          | VERSION^VPRD  | Supporting RPC   |
| <u>VPR GET PATIENT DATA</u>      | GET^VPRD      | Data Extract RPC |
| <u>VPR GET PATIENT DATA JSON</u> | GET^VPRDJ     | Data Extract RPC |

<span id="_Ref155790718" class="anchor"></span>Table 3: VPR GET PATIENT DATA—Allergy/Adverse Reaction Tracking (GMRA): “reactions” Type Elements Returned

The purpose of the VPR application is to serve VistA data to developers for use in GUI or Web applications, formatted as XML or JSON. Because it does *not* store or manage any data of its own, VPR has no direct user interface; its user interface consists of these RPCs. A developer can call either the VPR GET PATIENT DATA or VPR GET PATIENT DATA JSON RPC to retrieve data as XML or JSON respectively, based on the input parameters described below. Specific input values and data returned for each clinical domain and format are described in Sections <u>3</u>, “<u>XML Tables</u>,” and Section <u>4</u>, “<u>JSON Tables</u>.”

## VPR GET CHECKSUM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR GET CHECKSUM is a supporting RPC that retrieves data from VistA via GET^VPRD or GET^VPRDJ and calls the VPRDCRC routine to perform CRC32 calculations. VPRDCRC then returns the calculations as checksum values. Use this RPC to determine if patient data has changed since the last extract was performed.

## VPR DATA VERSION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR DATA VERSION is a supporting RPC that gets the value of the current VPR RPC version and returns it as a string. Any application with the appropriate Integration Control Registration (ICR) can use this RPC to extract the RPC version from VPR software.

## VPR GET PATIENT DATA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR GET PATIENT DATA is a data extract RPC that retrieves data from VistA and returns it as XML in a ^TMP global. Applications with the appropriate ICRs can use this RPC to extract data from VistA. Developers can specify input parameters to determine the types and amounts of data the RPC will extract from VistA. Parameters include:

- Internal entry number (IEN) from PATIENT (#2) file (optionally data file number \[DFN\] or integration control number \[ICN\] for remote calls) \[required parameter\]
- The kinds of data to extract, which can include:
- Allergies and reactions
- Appointments
- Clinical Procedures (medicine and cardiology)
- Consults
- Demographics
- Documents
- Education topics
- Exams
- Flags (Patient Record Flags)
- Functional Independence Measurements
- Health Factors
- Immunizations
- Insurance policies
- Labs (by accession, order or panel, or individual result)
- Medications
- Observations (CLiO)
- Orders
- Problems
- Procedures (includes Radiology, Surgery, and Clinical Procedures)
- Radiology exams
- Skin tests
- Surgical procedures
- Visits and encounters
- Vitals
- Wellness Reminders
- (optional) The date and time from which to begin searching for data.
- (optional) The date and time at which to end searching for data.
- (optional) The maximum number of items to return per data type.
- (optional, but TYPE *must* also be defined when used) The identifier of a single item to return.
- List of name-value pairs, further refining the search.

The output from this RPC is a text array formatted as XML in the temporary global ^TMP(“VPR”,\$J,n).

The text in <u>Figure 1</u> contains a snippet of XML data returned in response to a VPR GET PATIENT DATA RPC call for vitals measurements for VPRTestPatient, One:

<span id="_Ref525552752" class="anchor"></span>Figure 1: VPR GET PATIENT DATA RPC—Sample Returned XML-Formatted Data

\<vital\>

\<entered value='3050316.115625' /\>

\<facility code='998' name='ABILENE (CAA)' /\>

\<location code='158' name='7A GEN MED' /\>

\<measurements\>

\<measurement id='14871' vuid='4500634' name='BLOOD PRESSURE' value='168/68' high='210/110' low='100/60' /\>

\<measurement id='14869' vuid='4500636' name='PULSE' value='72' high='120' low='60' \>

\<qualifiers\>

\<qualifier name='RADIAL' vuid='4688678' /\>

\</qualifiers\>

\</measurement\>

\<measurement id='14872' vuid='4500635' name='PAIN' value='1' /\>

\<measurement id='14870' vuid='4688725' name='RESPIRATION' value='18' high='30' low='8' \>

\<qualifiers\>

\<qualifier name='SPONTANEOUS' vuid='4688706' /\>

\</qualifiers\>

\</measurement\>

\<measurement id='14868' vuid='4500638' name='TEMPERATURE' value='99' units='F' metricValue='37.2' metricUnits='C' high='102' low='95' \>

\<qualifiers\>

\<qualifier name='ORAL' vuid='4500642' /\>

\</qualifiers\>

\</measurement\>

\</measurements

\<taken value='3050316.1' /\>

\</vital\>

![](virtual-patient-record-vpr-developer-s-guide/017.png) REF: To review the lists of data elements returned by the VPR GET PATIENT DATA RPC, see the “<u>XML Tables</u>” section.

### VPR TEST XML Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View XML results \[VPR TEST XML\] option loops around its “Select DOMAIN:” and “Select PATIENT Name:” prompts, making it easy for testers to display data for successive patients and domains. The option asks for a start date, if the data domain supports date filtering; if testers provide a start date, it also asks for a stop date. The option’s start and stop parameters enable testers to limit data displays to a time-bound subset of available data. If testers do not provide a start date, the option does not ask for a stop date and displays all available data for the patient and domain testers specify.

Additional search filters can be entered, for domains that support them. If one of those domains is selected, testers may also see “FILTER” and “VALUE” prompts. An “ID” prompt may also appear, allowing a specific data item to be extracted and displayed. Testers can simply press Enter through any of these filters they do *not* wish to apply, and execution falls through to the extract and display.

Results will be displayed one record at a time, pausing between each to allow the tester to press Enter to continue or enter “^” to exit the results display and return to the “Select DOMAIN:” prompt.

<u>Figure 2</u> is an example of the View XML results \[VPR TEST XML\] option, showing the data it returns (the results are truncated, with extra spaces removed).

<span id="_Ref525555828" class="anchor"></span>Figure 2: VPR TEST XML Option—Sample Returned Output

Select OPTION NAME: <span class="mark">VPR TEST XML \<Enter\></span> View XML results

View XML results

Select PATIENT NAME: <span class="mark">AVIVAPATIENT,TWENTYONE \<Enter\></span> 2-14-34 666000001

YES SC VETERAN PROVIDER,EIGHTEEN PRIMARY CARE TEAM2

Enrollment Priority: GROUP 3 Category: IN PROCESS End Date:

Select DOMAIN: <span class="mark">VITALS</span>

Select START DATE: <span class="mark">11-1-2014 \<Enter\></span> (NOV 01, 2014)

Select STOP DATE: <span class="mark">11-1-2014 \<Enter\></span> (NOV 01, 2014)

Select TOTAL \#items: <span class="mark">\<Enter\></span>

\<results version='1.02' timeZone='-0700' \>

\<vitals total='1' \>

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

\<vital\>

\<entered value='3141103.143428' /\>

\<facility code='500D' name='SLC-FO HMP DEV' /\>

\<location code='23' name='GENERAL MEDICINE' /\>

\<measurements\>

\<measurement id='53157' vuid='4500634' name='BLOOD PRESSURE' value='128/66'

units='mm\[Hg\]' high='210/110' low='100/60' /\>

\<measurement id='53161' vuid='4688724' name='HEIGHT' value='71' units='in'

metricValue='180.34' metricUnits='cm' /\>

\<measurement id='53160' vuid='4500636' name='PULSE' value='92' units='/min'

high='120' low='60' /\>

\<measurement id='53164' vuid='4500635' name='PAIN' value='2' /\>

\<measurement id='53163' vuid='4500637' name='PULSE OXIMETRY' value='95'

units='%' high='100' low='50' /\>

\<measurement id='53159' vuid='4688725' name='RESPIRATION' value='16'

units='/min' high='30' low='8' /\>

\<measurement id='53158' vuid='4500638' name='TEMPERATURE' value='98.5'

units='F' metricValue'53162' vuid='4500639' name='WEIGHT'

## VPR GET PATIENT DATA JSON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR GET PATIENT DATA JSON is a data extract RPC that retrieves data from VistA and returns it as JSON-formatted documents in a ^TMP global. Applications with appropriate ICRs can use this RPC to extract data from VistA. Developers can specify input parameters to determine the types and amounts of data the RPC will extract from VistA by entering the parameters as a list of name-value pairs. Some of the most commonly used parameters include:

- IEN from PATIENT (#2) file (optionally DFN; ICN for remote calls) \[required\]
- The kinds of data to extract, which can include:
- Allergies and reactions
- Appointments
- Clinical Procedures (medicine and cardiology)
- Consults
- CPT procedures
- Demographics
- Documents
- Education topics
- Exams
- Health Factors
- Immunizations
- Lab results
- Medications
- Observations (CLiO)
- Orders
- Problems
- Purpose of visit (POV)
- Radiology exams
- Skin tests
- Surgical procedures
- Visits and admissions
- Vitals
- The date and time from which to begin searching for data \[optional\].
- The date and time at which to stop searching for data \[optional\].
- The maximum number of items to return per data type \[optional\].
- The identifier of a single item to return \[optional, but TYPE *must* also be defined when used\].
- Additional name-value pairs, further refining the search \[optional\].

The RPC’s output is a text array formatted as JSON in the temporary global ^TMP(“VPR”,\$J,n).

<u>Figure 3</u> contains a snippet of data returned in response to a VPR GET PATIENT DATA JSON RPC call for vitals measurements for VPRTestPatient, One—the same patient and data returned in the XML example (<u>Figure 1</u>).

<span id="_Ref525575945" class="anchor"></span>Figure 3: VPR GET PATIENT DATA JSON RPC—Sample Returned JSON-Formatted Data

{"apiVersion":"1.01","params":{"domain":"DEV.HMPDEV.VAINNOVATIONS.US","systemId":"F484"},"data":{"updated":"20130718143517","totalItems":5,"items":\[{"displayName":"BP","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high":"210\\110","kind":"Vital Sign","localId":14871,"locationName":"7 WEST MEDICINE",

"locationUid":"urn:va:location:F484:158","low":"100\\60","observed":200503161000,"result":"168\\68","resulted":20050316115625,"summary":"BLOOD PRESSURE 168\\68mm\[Hg\]","typeCode":"urn:va:vuid:4500634","typeName":"BLOOD PRESSURE","uid":"urn:va:F484:229:vital:14871","units":"mm\[Hg\]"}

,

{"displayName":"P","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high":120,"kind":"Vital sign","localId":14869,"locationName":"7 WEST MEDICINE","locationUid":"urn:va:location:F484:158","low":60,"observed":200503161000,"qualifiers":\[{"name":"RADIAL","vuid":4688678}\],"result":72,"resulted":20050316115625,"summary":"PULSE 72 \\min","typeCode":"urn:va:vuid:4500636","typeName":"PULSE","uid":"urn:va:F484:229:vital:14869","units":"\\min"}

,

{"displayName":"PN","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","kind":"Vital Sign","localId":14872,"locationName":"7 WEST MEDICINE","locationUid":"urn:va:location:F484:158","observed":200503161000,"result":1,"resulted":20050316115625,"summary":"PAIN 1 ","typeCode":"urn:va:vuid:4500635","typeName":"PAIN","uid":"urn:va:F484:229:vital:14872","units":""}

,

{"displayName":"R","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high":30,"kind":"Vital Sign","localId":14870,"locationName":"7 WEST MEDICINE","locationUid":"urn:va:location:F484:158","low":8,"observed":200503161000,"qualifiers":\[{"name":"SPONTANEOUS","vuid":4688706}\],"result":18,"resulted":20050316115625,"summary":"RESPIRATION 18 \\min","typeCode":"urn:va:vuid:4688725","typeName":"RESPIRATION","uid":"urn:va:F484:229:vital:14870","units":"\\min"}

![](virtual-patient-record-vpr-developer-s-guide/018.png) REF: To review the lists of data elements returned by the VPR GET PATIENT DATA JSON RPC, see the “<u>JSON Tables</u>” section.

### VPR TEST JSON Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View JSON results \[VPR TEST JSON\] option loops around its “Select DOMAIN:” and “Select PATIENT Name:” prompts, making it easy for testers to display data for successive patients and domains. The option asks for a start date. If testers provide a start date, it also asks for a stop date. The option’s start and stop parameters enable testers to limit data displays to a time-bound subset of available data. If testers do *not* provide a start date, the option does *not* ask for a stop date and displays all available data for the patient and domain testers specify.

Results are displayed one record at a time, pausing between each to allow the tester to press Enter to continue or enter “^” to exit the results display and return to the “Select DOMAIN:” prompt.

<u>Figure 4</u> is an example of the View JSON results \[VPR TEST JSON\] option, showing the data it returns (the results are truncated, with extra spaces removed).

<span id="_Ref525555662" class="anchor"></span>Figure 4: VPR TEST JSON Option—Sample Returned Output

Select OPTION NAME: <span class="mark">VPR TEST JSON \<Enter\></span> View JSON results

View JSON results

Select PATIENT NAME: <span class="mark">AVIVAPATIENT,TWENTYONE</span>      2-14-34    666000001    YES    SC VETERAN    PROVIDER,EIGHTEEN  PRIMARY CARE TEAM2

Enrollment Priority: GROUP 3 Category: IN PROCESS    End Date:

Select DOMAIN: <span class="mark">VITAL</span>

Select START DATE: <span class="mark">11-1-2014 \<Enter\></span> (NOV 01, 2014)

Select STOP DATE: <span class="mark">11-1-2014 \<Enter\></span> (NOV 01, 2014)

Select TOTAL \#items: <span class="mark">\<Enter\></span>

{"apiVersion":"1.03","params":{"domain":"DEV.HMPDEV.VAINNOVATIONS.US","systemId":"F484"},

"data":{"updated":"20150106112207","totalItems":8,"items":\[

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

{"displayName":"BP","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high"

:"210\\110","kind":"Vital Sign","localId":53157,"locationName":"GENERAL MEDICINE

","locationUid":"urn:va:location:F484:23","low":"100\\60","observed":20141101190

3,"result":"128\\66","resulted":20141103143428,"summary":"BLOOD PRESSURE 128\\66

mm\[Hg\]","typeCode":"urn:va:vuid:4500634","typeName":"BLOOD PRESSURE","uid":"urn

:va:vital:F484:237:53157","units":"mm\[Hg\]"}

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

{"displayName":"HT","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","kind"

:"Vital Sign","localId":53161,"locationName":"GENERAL MEDICINE","locationUid":"u

rn:va:location:F484:23","metricResult":180.34,"metricUnits":"cm","observed":2014

11011903,"result":71,"resulted":20141103143428,"summary":"HEIGHT 71 in","typeCod

e":"urn:va:vuid:4688724","typeName":"HEIGHT","uid":"urn:va:vital:F484:237:53161"

,"units":"in"}

, {"displayName":"P","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high":

120,"kind":"Vital Sign","localId":53160,"locationName":"GENERAL MEDICINE","locationUid":"urn:va:location:F484:23","low":60,"observed"vital:F484:237:53160","units":"\\min"}

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

{"displayName":"PN","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","kind"

:"Vital Sign","localId":53164,"locationName":"GENERAL MEDICINE","locationUid":"u

rn:va:location:F484:23","observed":201411011903,"result":2,"resulted":2014110314

3428,"summary":"PAIN 2 ","typeCode":"urn:va:vuid:4500635","typeName":"PAIN","uid

":"urn:va:vital:F484:237:53164","units":""}

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

{"displayName":"PO2","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high

":100,"kind":"Vital Sign","localId":53163,"locationName":"GENERAL MEDICINE","loc

ationUid":"urn:va:location:F484:23","low":50,"observed":201411011903,"result":95

,"resulted":20141103143428,"summary":"PULSE OXIMETRY 95 %","typeCode":"urn:va:vu

id:4500637","typeName":"PULSE OXIMETRY","uid":"urn:va:vital:F484:237:53163","uni

ts":"%"}

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

{"displayName":"R","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high":

30,"kind":"Vital Sign","localId":53159,"locationName":"GENERAL MEDICINE","locati

onUid":"urn:va:location:F484:23","low":8,"observed":201411011903,"result":16,"re

sulted":20141103143428,"summary":"RESPIRATION 16 \\min","typeCode":"urn:va:vuid:

4688725","typeName":"RESPIRATION","uid":"urn:va:vital:F484:237:53159","units":"\\

/min"}

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

{"displayName":"T","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","high":

102,"kind":"Vital Sign","localId":53158,"locationName":"GENERAL MEDICINE","locat

ionUid":"urn:va:location:F484:23","low":95,"metricResult":36.9,"metricUnits":"C"

,"observed":201411011903,"result":98.5,"resulted":20141103143428,"summary":"TEMP

ERATURE 98.5 F","typeCode":"urn:va:vuid:4500638","typeName":"TEMPERATURE","uid":

"urn:va:vital:F484:237:53158","units":"F"}

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

{"displayName":"WT","facilityCode":"500D","facilityName":"SLC-FO HMP DEV","kind"

:"Vital Sign","localId":53162,"locationName":"GENERAL MEDICINE","locationUid":"u

rn:va:location:F484:23","metricResult":46.36,"metricUnits":"kg","observed":20141

1011903,"result":102,"resulted":20141103143428,"summary":"WEIGHT 102 lb","typeCo

de":"urn:va:vuid:4500639","typeName":"WEIGHT","uid":"urn:va:vital:F484:237:53162

","units":"lb"}

\]}}

# XML Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The tables in this section list the data elements returned by the VPR GET PATIENT DATA RPC. All searches are performed reverse-chronologically to return the most recent data, unless otherwise noted.

All input parameters are optional to refine the extract, except for DFN and TYPE. The Data File Number (DFN) is the internal entry number (IEN) from the PATIENT (#2) file, or alternatively, the Integration Control Number (ICN) for remote calls. This parameter’s value can be provided in any of the following formats:

- DFN
- DFN;ICN
- ;ICN

## Allergy/Adverse Reaction Tracking (GMRA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “reactions”.

START: (optional) VA FileMan date to filter on “entered”.

STOP: (optional) VA FileMan date to filter on “entered”.

MAX: (optional) Use *not recommended*, as reactions are *not* sorted.

ID: (optional) PATIENT ALLERGIES (#120.8) file IEN.

FILTER(“nowrap”):1 or 0, to include breaks between lines in comment text.

Output

| Elements              | Attributes  | Content                                                 |
|-----------------------|-------------|---------------------------------------------------------|
| assessment            | value       | not done or nka (only returned if no reactions) |
| comment \*        | id          | number                                                  |
|                       | enteredBy   | NEW PERSON (#200) Name                                  |
|                       | entered     | VA FileMan date.time                                |
|                       | commentType | O or E (observed or error)                      |
|                       | commentText | string                                                  |
| drugClass \*      | name        | VA DRUG CLASS (#50.605) Classification                  |
|                       | vuid        | VA DRUG CLASS (#50.605) VUID                            |
| drugIngredient \* | name        | DRUG INGREDIENTS (#50.416) Name                         |
|                       | vuid        | DRUG INGREDIENTS (#50.416) VUID                         |
| entered               | value       | VA FileMan date.time                                |
| facility              | code        | INSTITUTION (#4) Station Number                         |
|                       | name        | INSTITUTION (#4) Name                                   |
| id                    | value       | PATIENT ALLERGIES (#120.8) ien                          |
| localCode             | value       | VA FileMan variable pointer                             |
| mechanism             | value       | ALLERGY, PHARMACOLOGIC, or UNKNOWN          |
| name                  | value       | string                                                  |
| reaction \*       | name        | string                                                  |
|                       | vuid        | number                                                  |
| removed               | value       | boolean (1 or 0)                                |
| severity              | value       | MILD, MODERATE, or SEVERE                   |
| source                | value       | O or H (observed or historical)                 |
| type                  | value       | any combination of DFO                                  |
| verified              | value       | any combination of DRUG, FOOD, OTHER                    |
| vuid                  | value       | VUID number                                             |

<span id="_Toc155864387" class="anchor"></span>Table 4: VPR GET PATIENT DATA—Clinical Observations (MDC): “observations” Type Elements Returned

\* = can be multiple

## Clinical Observations (MDC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “observations”.

START: (optional) VA FileMan date to filter on “observed”.

STOP: (optional) VA FileMan date to filter on “observed”.

MAX: (optional) Use with caution, as search is performed chronologically.

ID: (optional) OBS (#704.117) file ID (#.01) value.

FILTER: (optional) None.

Output

| Elements | Attributes | Content                                                                                   |
|----------|------------|-------------------------------------------------------------------------------------------|
| bodySite | code       | VUID number                                                                               |
|          | name       | string                                                                                    |
| comment  | value      | string                                                                                    |
| entered  | value      | VA FileMan date.time                                                                  |
| facility | code       | INSTITUTION (#4) Station Number                                                           |
|          | name       | INSTITUTION (#4) Name                                                                     |
| id       | value      | OBS (#704.117) ID                                                                         |
| location | code       | HOSPITAL LOCATION (#44) ien                                                               |
|          | name       | HOSPITAL LOCATION (#44) Name                                                              |
| method   | code       | VUID number                                                                               |
|          | name       | string                                                                                    |
| name     | value      | string                                                                                    |
| observed | value      | VA FileMan date.time                                                                  |
| position | code       | VUID number                                                                               |
|          | name       | string                                                                                    |
| product  | code       | VUID number                                                                               |
|          | name       | string                                                                                    |
| quality  | code       | VUID number                                                                               |
|          | name       | string                                                                                    |
| range    | value      | Unknown, Normal, Out of Bounds Low, Out of Bounds High, Low, High |
| status   | value      | Verified                                                                                  |
| units    | code       | VUID number                                                                               |
|          | name       | string                                                                                    |
| value    | value      | string                                                                                    |
| vuid     | value      | VUID number                                                                               |

<span id="_Ref155790726" class="anchor"></span>Table 5: VPR GET PATIENT DATA—Clinical Procedures (MC): “clinicalProcedures” Type Elements Returned

## Clinical Procedures (MC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “clinicalProcedures”.

START: (optional) VA FileMan date to filter on “dateTime”.

STOP: (optional) VA FileMan date to filter on “dateTime”.

MAX: (optional) Number of most recent procedures to return.

ID: (optional) Variable pointer to CP data file/item.

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements        | Attributes     | Content                                                                           |
|-----------------|----------------|-----------------------------------------------------------------------------------|
| category        | value          | CP                                                                            |
| consult         | value          | CONSULT (#123) ien                                                                |
| dateTime        | value          | VA FileMan date.time                                                          |
| document \* | id             | TIU DOCUMENT (#8925) ien                                                          |
|                 | localTitle     | TIU DOCUMENT DEFINITION (#8925.1) Name                                            |
|                 | nationalTitle  | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)                                       |
|                 | vuid           | VUID number                                                                       |
|                 | content        | word-processing text                                                              |
| encounter       | value          | VISIT (#9000010) ien                                                              |
| facility        | code           | INSTITUTION (#4) Station Number                                                   |
|                 | name           | INSTITUTION (#4) Name                                                             |
| hasImages       | value          | boolean (1 or 0)                                                          |
| id              | value          | variable pointer                                                                  |
| interpretation  | value          | Normal, Abnormal, Borderline, Incomplete, or Machine Resulted |
| location        | code           | HOSPITAL LOCATION (#44) ien                                                       |
|                 | name           | HOSPITAL LOCATION (#44) Name                                                      |
| name            | value          | string                                                                            |
| order           | code           | ORDER (#100) ien                                                                  |
|                 | name           | string                                                                            |
| provider        | code           | NEW PERSON (#200) ien                                                             |
|                 | name           | NEW PERSON (#200) Name                                                            |
|                 | officePhone    | NEW PERSON (#200) Office Phone                                                    |
|                 | analogPager    | NEW PERSON (#200) Voice Pager                                                     |
|                 | fax            | NEW PERSON (#200) Fax Number                                                      |
|                 | email          | NEW PERSON (#200) Email Address                                                   |
|                 | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                                                   |
|                 | providerType   | PERSON CLASS (#8932.1) Provider Type                                              |
|                 | classification | PERSON CLASS (#8932.1) Classification                                             |
|                 | specialization | PERSON CLASS (#8932.1) Area of Specialization                                     |
|                 | service        | NEW PERSON (#200) Service/Section                                                 |
| requested       | value          | VA FileMan date.time                                                          |
| status          | value          | string                                                                            |

<span id="_Toc155864389" class="anchor"></span>Table 6: VPR GET PATIENT DATA—Clinical Reminders (PXRM): “reminders” Type Elements Returned

\* = can be multiple

## Clinical Reminders (PXRM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not all clinical reminders that may appear in Computerized Patient Record System (CPRS) will be available via this extract. Only the nationally exported “wellness” reminders, those marked for Patient usage and shown in MyHealtheVet, are processed and returned at run time.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “reminders”.

START: (optional) None.

STOP: (optional) None.

MAX: (optional) None.

ID: (optional) REMINDER DEFINITION (#811.9) file ien.

FILTER: (optional) None.

Output

| Elements | Attributes | Content                                                          |
|----------|------------|------------------------------------------------------------------|
| class    | code       | N                                                            |
|          | name       | NATIONAL                                                     |
| detail   |            | word-processing text                                             |
| due      | value      | VA FileMan date.time, DUE NOW, N/A, or CNBD      |
| facility | code       | INSTITUTION (#4) Station Number                                  |
|          | name       | INSTITUTION (#4) Name                                            |
| id       | value      | REMINDER DEFINITION (#811.9) ien                                 |
| lastDone | value      | VA FileMan date.time, or UNKNOWN                         |
| name     | value      | REMINDER DEFINITION (#811.9) Print Name                          |
| status   | value      | DUE NOW, DUE SOON, NOT DUE, RESOLVED, or N/A |
| summary  |            | word-processing text                                             |

<span id="_Toc155864390" class="anchor"></span>Table 7: VPR GET PATIENT DATA—Consult/Request Tracking (GMRC): “consults” Type Elements Returned

## Consult/Request Tracking (GMRC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “consults”.

START: VA FileMan date to filter on “requested”.

STOP: VA FileMan date to filter on “requested”.

MAX: Number of most recent consult requests to return.

ID: REQUEST/CONSULTATION (#123) file IEN.

FILTER(“text”):1 or 0, to include “content” text of report.

Output

| Elements        | Attributes     | Content                                       |
|-----------------|----------------|-----------------------------------------------|
| document \* | id             | TIU DOCUMENT (#8925) ien                      |
|                 | localTitle     | TIU DOCUMENT DEFINITION (#8925.1) Name        |
|                 | nationalTitle  | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)   |
|                 | vuid           | VUID number                                   |
|                 | content        | word-processing text                          |
| facility        | code           | INSTITUTION (#4) Station Number               |
|                 | name           | INSTITUTION (#4) Name                         |
| id              | value          | REQUEST/CONSULTATION (#123) ien               |
| name            | value          | string                                        |
| orderID         | value          | ORDER (#100) ien                              |
| procedure       | value          | GMRC Procedure \#123.3 Name or “Consult”  |
| provider        | code           | NEW PERSON (#200) ien                         |
|                 | name           | NEW PERSON (#200) Name                        |
|                 | officePhone    | NEW PERSON (#200) Office Phone                |
|                 | analogPager    | NEW PERSON (#200) Voice Pager                 |
|                 | fax            | NEW PERSON (#200) Fax Number                  |
|                 | email          | NEW PERSON (#200) Email Address               |
|                 | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code               |
|                 | providerType   | PERSON CLASS (#8932.1) Provider Type          |
|                 | classification | PERSON CLASS (#8932.1)1 Classification        |
|                 | specialization | PERSON CLASS (#8932.1) Area of Specialization |
|                 | service        | NEW PERSON (#200 Service/Section              |
| provDx          | code           | ICD code                                      |
|                 | name           | ICD Description                               |
|                 | system         | ICD or 10D                                    |
| reason          | value          | word-processing text                          |
| requested       | value          | VA FileMan date.time                      |
| result          | value          | string                                        |
| service         | value          | REQUEST SERVICES (#123.5) Name                |
| status          | value          | ORDER STATUS (#100.01) Name                   |
| type            | value          | C or P                                |
| urgency         | value          | string                                        |

<span id="_Toc155864391" class="anchor"></span>Table 8: VPR GET PATIENT DATA—Functional Independence Measurements (RMIM): “functionalMeasurements” Type Elements Returned

\* = can be multiple

## Functional Independence Measurements (RMIM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The assessment scores are often entered by multiple clinicians. The set as a whole is *not* returned until all 18 numeric scores are available. A sub-total for each section of scores will also then be included.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “functionalMeasurements”.

START: (optional) VA FileMan date to filter on “admitted”, chronologically.

STOP: (optional) VA FileMan date to filter on “admitted”, chronologically.

MAX: (optional) Use *not recommended*, as measurements are *not* sorted.

ID: (optional) FUNCTIONAL INDEPENDENCE (#783) file IEN.

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements            | Attributes     |                | Content                                                                |
|---------------------|----------------|----------------|------------------------------------------------------------------------|
| admitClass          | value          |                | 1, 2, or 3                                                 |
| admitted            | value          |                | FileMan                                                                |
| assessment \*   | type           |                | admission, discharge, interim, follow up, or goals |
|                     | cognitiveScore |                | number, 5-35                                                       |
|                     | motorScore     |                | number, 13-91                                                      |
|                     | totalScore     |                | number, 18-126                                                     |
|                     | values         | eat            | number, 1-7                                                        |
|                     |                | groom          | number, 1-7                                                        |
|                     |                | bath           | number, 1-7                                                        |
|                     |                | dressUp        | number, 1-7                                                        |
|                     |                | dressLo        | number, 1-7                                                        |
|                     |                | toilet         | number, 1-7                                                        |
|                     |                | bladder        | number, 1-7                                                        |
|                     |                | bowel          | number, 1-7                                                        |
|                     |                | transChair     | number, 1-7                                                        |
|                     |                | transToilet    | number, 1-7                                                        |
|                     |                | transTub       | number, 1-7                                                        |
|                     |                | locomWalk      | number, 1-7                                                        |
|                     |                | locomStair     | number, 1-7                                                        |
|                     |                | comprehend     | number, 1-7                                                        |
|                     |                | express        | number, 1-7                                                        |
|                     |                | interact       | number, 1-7                                                        |
|                     |                | problem        | number, 1-7                                                        |
|                     |                | memory         | number, 1-7                                                        |
|                     |                | walkMode       | W, C, or B (walk, wheelchair, or both)                     |
|                     |                | comprehendMode | A, V, or B (auditory, visual, or both)                     |
|                     |                | expressMode    | V, N, or B (vocal, non-vocal, or both)                     |
| care                | value          |                | CONTINUUM OF CARE, ACUTE, or SUBACUTE                                  |
| case                | value          |                | number                                                                 |
| discharged          | value          |                | VA FileMan date                                                        |
| document \*     | id             |                | TIU DOCUMENT (#8925) ien                                               |
|                     | localTitle     |                | TIU DOCUMENT DEFINITION (#8925.1) Name                                 |
|                     | nationalTitle  |                | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)                            |
|                     | vuid           |                | VUID number                                                            |
|                     | content        |                | word-processing text                                                   |
| facility            | code           |                | INSTITUTION (#4) Station Number                                        |
|                     | name           |                | INSTITUTION (#4) Name                                                  |
| id                  | value          |                | FUNCTIONAL INDEPENDENCE (#783) ien                                     |
| impairmentGroup     | value          |                | string                                                                 |
| interruption \* | transfer       |                | VA FileMan date                                                        |
|                     | return         |                | VA FileMan date                                                        |
| interruptionCode    | value          |                | string                                                                 |
| name                | value          |                | Functional Independence Measurement                                    |
| onset               | value          |                | VA FileMan date                                                        |

<span id="_Toc155864392" class="anchor"></span>Table 9: VPR GET PATIENT DATA—Integrated Billing (IB): “insurancePolicies” Type Elements Returned

\* = can be multiple

## Integrated Billing (IB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “insurancePolicies”.

START: (optional) None.

STOP: (optional) None.

MAX: (optional) Use *not recommended*, as policies are *not* sorted.

ID: (optional) None.

FILTER(“status”): (optional) Desired status codes, see ^IBBDOC for possible values. Default = “RB”.

Output

| Elements       | Attributes |               | Content                                                                                                                                                                                      |
|----------------|------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| company        | id         |               | INSURANCE COMPANY (#36) ien                                                                                                                                                                  |
|                | name       |               | INSURANCE COMPANY (#36) Name                                                                                                                                                                 |
|                | address    | streetLine1   | INSURANCE COMPANY (#36) Street Address \[1\]                                                                                                                                                 |
|                |            | streetLine2   | INSURANCE COMPANY (#36) Street Address \[2\]                                                                                                                                                 |
|                |            | streetLine3   | INSURANCE COMPANY (#36) Street Address \[3\]                                                                                                                                                 |
|                |            | city          | INSURANCE COMPANY (#36) City                                                                                                                                                                 |
|                |            | stateProvince | INSURANCE COMPANY (#36) State                                                                                                                                                                |
|                |            | postalCode    | INSURANCE COMPANY (#36) Zip                                                                                                                                                                  |
|                | telecom    |               | INSURANCE COMPANY (#36) Phone Number                                                                                                                                                         |
| effectiveDate  | value      |               | VA FileMan date.time                                                                                                                                                                     |
| expirationDate | value      |               | VA FileMan date.time                                                                                                                                                                     |
| facility       | code       |               | INSTITUTION (#4) Station Number                                                                                                                                                              |
|                | name       |               | INSTITUTION (#4) Name                                                                                                                                                                        |
| groupName      | value      |               | GROUP PLAN (#355.3) Group Name                                                                                                                                                               |
| groupNumber    | value      |               | string                                                                                                                                                                                       |
| id             | value      |               | DFN;company id;Group Plan (#355.3) ien                                                                                                                                                       |
| insuranceType  | code       |               | TYPE OF PLAN (#355.1) ien                                                                                                                                                                    |
|                | name       |               | TYPE OF PLAN (#355.1) Name                                                                                                                                                                   |
| relationship   | value      |               | PATIENT, SPOUSE, NATURAL CHILD, EMPLOYEE, ORGAN DONOR, INJURED PLAINTIFF, MOTHER, FATHER, SIGNIFICANT OTHER, LIFE PARTNER, or OTHER RELATIONSHIP |
| subscriber     | id         |               | string                                                                                                                                                                                       |
|                | name       |               | string                                                                                                                                                                                       |

<span id="_Toc155864393" class="anchor"></span>Table 10: VPR GET PATIENT DATA—Laboratory (LR): “labs” Type Elements Returned

## Laboratory (LR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “labs”.

START: (optional) VA FileMan date to filter on “collected”.

STOP: (optional) VA FileMan date to filter on “collected”.

MAX: (optional) Number of most recent accessions to return.

ID: (optional) LAB DATA (#63) file IEN string.

FILTER(“type”): (optional) Desired “type” code(s). Default = “CH”.

FILTER(“nowrap”): (optional) 1 or 0, to include breaks between comment lines.

Output

| Elements       | Attributes     | Content                                       |
|----------------|----------------|-----------------------------------------------|
| collected      | value          | VA FileMan date.time                      |
| comment        | value          | string                                        |
| facility       | code           | INSTITUTION (#4) Station Number               |
|                | name           | INSTITUTION (#4) Name                         |
| groupName      | value          | accession number string                       |
| high           | value          | string                                        |
| id             | value          | LAB DATA (#63) ien string                     |
| interpretation | value          | L, L\*, H, H\*, or NULL   |
| labOrderID     | value          | number                                        |
| localName      | value          | LAB TEST (#60) Print Name                     |
| loinc          | value          | LOINC code                                    |
| low            | value          | string                                        |
| performingLab  | value          | string                                        |
| provider       | code           | NEW PERSON (#200) ien                         |
|                | name           | NEW PERSON (#200) Name                        |
|                | officePhone    | NEW PERSON (#200) Office Phone                |
|                | analogPager    | NEW PERSON (#200) Voice Pager                 |
|                | fax            | NEW PERSON (#200) Fax Number                  |
|                | email          | NEW PERSON (#200) Email Address               |
|                | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code               |
|                | providerType   | PERSON CLASS (#8932.1) Provider Type          |
|                | classification | PERSON CLASS (#8932.1) Classification         |
|                | specialization | PERSON CLASS (#8932.1) Area of Specialization |
|                | service        | NEW PERSON (#200) Service/Section             |
| orderID        | value          | ORDER (#100) ien                              |
| result         | value          | string                                        |
| resulted       | value          | VA FileMan date.time                      |
| sample         | value          | COLLECTION SAMPLE (#62) Name                  |
| specimen       | code           | TOPOGRAPHY (#61) SNOMED Code                  |
|                | name           | TOPOGRAPHY (#61) Name                         |
| status         | value          | completed or incomplete               |
| test           | value          | LAB TEST (#60) Name                           |
| type           | value          | CH or MI                              |
| units          | value          | string                                        |
| vuid           | value          | VUID number                                   |

<span id="_Ref155790731" class="anchor"></span>Table 11: VPR GET PATIENT DATA—Accessions: “accessions” Type Elements Returned

### Accessions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The same results can also be returned grouped by the accessioned specimen; this is the only Lab domain that returns pathology data, and the recommended domain for retrieving microbiology results.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “accessions”.

START: (optional) VA FileMan date to filter on “collected”.

STOP: (optional) VA FileMan date to filter on “collected”.

MAX: (optional) Number of most recent accessions to return.

ID: (optional) LAB DATA (#63) file IEN string.

FILTER(“type”): (optional) Desired “type” codes. Default = all lab types.

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

FILTER(“nowrap”): (optional) 1 or 0, to include breaks between comment lines.

Output

| Elements                                     | Attributes     | Content                                           |
|----------------------------------------------|----------------|---------------------------------------------------|
| collected                                    | value          | VA FileMan date.time                          |
| comment                                      | value          | string                                            |
| document \*                              | id             | TIU DOCUMENT (#8925) ien                          |
| (document only returned for MI and AP types) | localTitle     | TIU DOCUMENT DEFINITION (#8925.1) Name            |
|                                              | nationalTitle  | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)       |
|                                              | vuid           | VUID number                                       |
|                                              | content        | word-processing text                              |
| facility                                     | code           | INSTITUTION (#4) Station Number                   |
|                                              | name           | INSTITUTION (#4) Name                             |
| groupName                                    | value          | accession number string                           |
| id                                           | value          | LAB DATA (#63) ien string                         |
| labOrderID                                   | value          | number                                            |
| name                                         | value          | ACCESSION (#68) Area                              |
| pathologist                                  | code           | NEW PERSON (#200) ien                             |
| (pathologist only returned for AP types)     | name           | NEW PERSON (#200) Name                            |
|                                              | officePhone    | NEW PERSON (#200) Office Phone                    |
|                                              | analogPager    | NEW PERSON (#200) Voice Pager                     |
|                                              | fax            | NEW PERSON (#200) Fax Number                      |
|                                              | email          | NEW PERSON (#200) Email Address                   |
|                                              | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                   |
|                                              | providerType   | PERSON CLASS (#8932.1) Provider Type              |
|                                              | classification | PERSON CLASS (#8932.1) Classification             |
|                                              | specialization | PERSON CLASS (#8932.1) Area of Specialization     |
|                                              | service        | NEW PERSON (#200) Service/Section                 |
| provider                                     | code           | NEW PERSON (#200) ien                             |
|                                              | name           | NEW PERSON (#200) Name                            |
|                                              | officePhone    | NEW PERSON (#200) Office Phone                    |
|                                              | analogPager    | NEW PERSON (#200) Voice Pager                     |
|                                              | fax            | NEW PERSON (#200) Fax Number                      |
|                                              | email          | NEW PERSON (#200) Email Address                   |
|                                              | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                   |
|                                              | providerType   | PERSON CLASS (#8932.1) Provider Type              |
|                                              | classification | PERSON CLASS (#8932.1) Classification             |
|                                              | specialization | PERSON CLASS (#8932.1) Area of Specialization     |
|                                              | service        | NEW PERSON (#200 Service/Section                  |
| resulted                                     | value          | VA FileMan date.time                          |
| sample                                       | value          | COLLECTION SAMPLE (#62) Name                      |
| specimen                                     | code           | TOPOGRAPHY (#61) SNOMED Code                      |
|                                              | name           | TOPOGRAPHY (#61) Name                             |
| status                                       | value          | completed or incomplete                   |
| type                                         | value          | CH, MI, CY, EM, SP, or AU |
| value \*                                 | id             | LAB DATA (#63) file ien string                    |
|                                              | test           | LAB TEST (#60) Name                               |
|                                              | result         | string                                            |
|                                              | interpretation | L, L\*, H, H\*, or NULL       |
|                                              | units          | string                                            |
|                                              | low            | string                                            |
|                                              | high           | string                                            |
|                                              | localName      | LAB TEST (#60) Print Name                         |
|                                              | loinc          | LOINC code                                        |
|                                              | vuid           | VUID number                                       |
|                                              | order          | ORDER (#100) ien                                  |
|                                              | performingLab  | string                                            |

<span id="_Ref155790737" class="anchor"></span>Table 12: VPR GET PATIENT DATA—Panels: “panels” Type Elements Returned

\* = can be multiple

### Panels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Results can also be returned grouped by order or panel within an accession. Because Lab can purge its order information, results are found by first searching the ORDER (#100) file then retrieving the associated results from the LAB DATA (#63) file.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “panels”.

START: (optional) VA FileMan date to filter on date order released.

STOP: (optional) VA FileMan date to filter on date order released.

MAX: (optional) Number of most recent orders to return.

ID: (optional) ORDER (#100) file IEN.

FILTER(“type”): (optional) Desired “type” code. Default = “CH”.

FILTER(“nowrap”): (optional) 1 or 0, to include breaks between comment lines.

Output

| Elements     | Attributes     | Content                                       |
|--------------|----------------|-----------------------------------------------|
| collected    | value          | VA FileMan date.time                      |
| comment      | value          | string                                        |
| facility     | code           | INSTITUTION (#4) Station Number               |
|              | name           | INSTITUTION (#4) Name                         |
| groupName    | value          | accession number string                       |
| id           | value          | ORDER (#100) ien                              |
| labOrderID   | value          | ORDER (#100) Package Reference string         |
| name         | value          | LAB TEST (#60) Name                           |
| order        | code           | ORDER (#100) ien                              |
|              | name           | LAB TEST (#60) Name                           |
| ordered      | value          | VA FileMan date.time                      |
| provider     | code           | NEW PERSON (#200) ien                         |
|              | name           | NEW PERSON (#200) Name                        |
|              | officePhone    | NEW PERSON (#200) Office Phone                |
|              | analogPager    | NEW PERSON (#200) Voice Pager                 |
|              | fax            | NEW PERSON (#200) Fax Number                  |
|              | email          | NEW PERSON (#200) Email Address               |
|              | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code               |
|              | providerType   | PERSON CLASS (#8932.1) Provider Type          |
|              | classification | PERSON CLASS (#8932.1) Classification         |
|              | specialization | PERSON CLASS (#8932.1) Area of Specialization |
|              | service        | NEW PERSON (#200) Service/Section             |
| resulted     | value          | VA FileMan date.time                      |
| sample       | value          | COLLECTION SAMPLE (#62) Name                  |
| specimen     | code           | TOPOGRAPHY (#61) SNOMED Code                  |
|              | name           | TOPOGRAPHY (#61) Name                         |
| status       | value          | completed or incomplete               |
| type         | value          | CH or MI                              |
| value \* | id             | LAB DATA (#63) file ien string                |
|              | test           | LAB TEST (#60) Name                           |
|              | result         | string                                        |
|              | interpretation | L, L\*, H, H\*, or NULL   |
|              | units          | string                                        |
|              | low            | string                                        |
|              | high           | string                                        |
|              | localName      | LAB TEST (#60) Print Name                     |
|              | loinc          | LOINC code                                    |
|              | vuid           | VUID number                                   |
|              | performingLab  | string                                        |

<span id="_Toc155864396" class="anchor"></span>Table 13: VPR GET PATIENT DATA—Orders (OR): “orders” Type Elements Returned

\* = can be multiple

## Orders (OR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many order views in CPRS include actions on orders as separate items; this extract returns only the current snapshot of each order found, unless the view requested is specific to actions (i.e., unsigned).

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “orders”.

START: (optional) VA FileMan date to filter on “released” or “entered”.

STOP: (optional) VA FileMan date to filter on “released” or “entered”.

MAX: (optional) Number of most recent orders to return.

ID: (optional) ORDER (#100) file IEN string.

FILTER(“view”): (optional) Desired “view” code, see ^ORQ1 for possible values. Default = 6 (Released Orders), sorted by “released”.

Output

| Elements               | Attributes     | Content                                                                                                                                                                                                                                    |
|------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| acknowledgement \* | code           | NEW PERSON (#200) ien                                                                                                                                                                                                                      |
|                        | name           | NEW PERSON (#200) Name                                                                                                                                                                                                                     |
|                        | date           | VA FileMan date.time                                                                                                                                                                                                                   |
| codingSystem           | code           | string (national code)                                                                                                                                                                                                                     |
|                        | name           | CPT, NLT, or LNC                                                                                                                                                                                                               |
| content                |                | word-processing text                                                                                                                                                                                                                       |
| discontinued           | date           | VA FileMan date.time                                                                                                                                                                                                                   |
|                        | by             | NEW PERSON (#200) ien                                                                                                                                                                                                                      |
|                        | byName         | NEW PERSON (#200) Name                                                                                                                                                                                                                     |
|                        | reason         | string                                                                                                                                                                                                                                     |
| entered                | value          | VA FileMan date.time                                                                                                                                                                                                                   |
| facility               | code           | INSTITUTION (#4) Station Number                                                                                                                                                                                                            |
|                        | name           | INSTITUTION (#4) Name                                                                                                                                                                                                                      |
| group                  | value          | DISPLAY GROUP (#100.98) Short Name                                                                                                                                                                                                         |
| id                     | value          | ORDER (#100) ien string                                                                                                                                                                                                                    |
| location               | code           | HOSPITAL LOCATION (#44) ien                                                                                                                                                                                                                |
|                        | name           | HOSPITAL LOCATION (#44) Name                                                                                                                                                                                                               |
| name                   | code           | ORDERABLE ITEMS (#101.43) ien                                                                                                                                                                                                              |
|                        | name           | ORDERABLE ITEMS (#101.43) Name                                                                                                                                                                                                             |
| provider               | code           | NEW PERSON (#200) ien                                                                                                                                                                                                                      |
|                        | name           | NEW PERSON (#200) Name                                                                                                                                                                                                                     |
|                        | officePhone    | NEW PERSON (#200) Office Phone                                                                                                                                                                                                             |
|                        | analogPager    | NEW PERSON (#200) Voice Pager                                                                                                                                                                                                              |
|                        | fax            | NEW PERSON (#200) Fax Number                                                                                                                                                                                                               |
|                        | email          | NEW PERSON (#200) Email Address                                                                                                                                                                                                            |
|                        | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                                                                                                                                                                                                            |
|                        | providerType   | PERSON CLASS (#8932.1) Provider Type                                                                                                                                                                                                       |
|                        | classification | PERSON CLASS (#8932.1) Classification                                                                                                                                                                                                      |
|                        | specialization | PERSON CLASS (#8932.1) Area of Specialization                                                                                                                                                                                              |
|                        | service        | NEW PERSON (#200) Service/Section                                                                                                                                                                                                          |
| released               | value          | VA FileMan date.time                                                                                                                                                                                                                   |
| resultID               | value          | string (corresponds to “id” in other domains)                                                                                                                                                                                              |
| service                | value          | PACKAGE (#9.4) Prefix                                                                                                                                                                                                                      |
| signatureStatus        | value          | ON CHART w/written orders, ELECTRONIC, NOT SIGNED, NOT REQUIRED, ON CHART w/printed orders, NOT REQUIRED due to cancel/lapse, SERVICE CORRECTION to signed order, DIGITALLY SIGNED, or ON PARENT order |
| signed                 | value          | VA FileMan date.time                                                                                                                                                                                                                   |
| signer                 | code           | NEW PERSON (#200) ien                                                                                                                                                                                                                      |
|                        | name           | NEW PERSON (#200) Name                                                                                                                                                                                                                     |
|                        | officePhone    | NEW PERSON (#200) Office Phone                                                                                                                                                                                                             |
|                        | analogPager    | NEW PERSON (#200) Voice Pager                                                                                                                                                                                                              |
|                        | fax            | NEW PERSON (#200) Fax Number                                                                                                                                                                                                               |
|                        | email          | NEW PERSON (#200) Email Address                                                                                                                                                                                                            |
|                        | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                                                                                                                                                                                                            |
|                        | providerType   | PERSON CLASS (#8932.1) Provider Type                                                                                                                                                                                                       |
|                        | classification | PERSON CLASS (#8932.1) Classification                                                                                                                                                                                                      |
|                        | specialization | PERSON CLASS (#8932.1) Area of Specialization                                                                                                                                                                                              |
|                        | service        | NEW PERSON (#200) Service/Section                                                                                                                                                                                                          |
| start                  | value          | VA FileMan date.time                                                                                                                                                                                                                   |
| status                 | code           | ORDER STATUS (#100.01) Abbreviation                                                                                                                                                                                                        |
|                        | name           | ORDER STATUS (#100.01) Name                                                                                                                                                                                                                |
|                        | vuid           | ORDER STATUS (#100.01) VUID                                                                                                                                                                                                                |
| stop                   | value          | VA FileMan date.time                                                                                                                                                                                                                   |
| type                   | value          | DISPLAY GROUP (#100.98) Mixed Name                                                                                                                                                                                                         |
| vuid                   | value          | VUID number of ordered item, for labs and meds                                                                                                                                                                                             |

<span id="_Toc155864397" class="anchor"></span>Table 14: VPR GET PATIENT DATA—Exams: “exams” Type Elements Returned

\* = Can be multiple.

## Patient Care Encounter (PX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](virtual-patient-record-vpr-developer-s-guide/019.png) NOTE: All Patient Care Encounter (PCE) patient data file names all start with “V”, which is short for Visit.

### Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “exams”.

START: (optional) VA FileMan date to filter on “dateTime”.

STOP: (optional) VA FileMan date to filter on “dateTime”.

MAX: (optional) Number of most recent exams to return.

ID: (optional) V EXAM (#9000010.13) file IEN.

FILTER: (optional) None.

Output

| Elements  | Attributes | Content                         |
|-----------|------------|---------------------------------|
| comment   | value      | string                          |
| dateTime  | value      | VA FileMan date.time        |
| encounter | value      | VISIT (#9000010) ien            |
| facility  | code       | INSTITUTION (#4) Station Number |
|           | name       | INSTITUTION (#4) Name           |
| id        | value      | V EXAM (#9000010.13) ien        |
| name      | value      | EXAM (#9999999.15) Name         |
| result    | value      | string                          |

<span id="_Toc155864398" class="anchor"></span>Table 15: VPR GET PATIENT DATA—Education Topics: “educationTopics” Type Elements Returned

### Education Topics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “educationTopics”.

START: (optional) VA FileMan date to filter on “dateTime”.

STOP: (optional) VA FileMan date to filter on “dateTime”.

MAX: (optional) Number of most recent education instances to return.

ID: (optional) V PATIENT ED (#9000010.16) file IEN.

FILTER: (optional) None.

Output

| Elements  | Attributes | Content                             |
|-----------|------------|-------------------------------------|
| comment   | value      | string                              |
| dateTime  | value      | VA FileMan date.time            |
| encounter | value      | VISIT (#9000010) ien                |
| facility  | code       | INSTITUTION (#4) Station Number     |
|           | name       | INSTITUTION (#4) Name               |
| id        | value      | V PATIENT ED (#9000010.16) ien      |
| name      | value      | EDUCATION TOPICS (#9999999.09) Name |
| result    | value      | string                              |

<span id="_Toc155864399" class="anchor"></span>Table 16: VPR GET PATIENT DATA—Health Factors: “healthFactors” Type Elements Returned

### Health Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “healthFactors”.

START: (optional) VA FileMan date to filter on “recorded”.

STOP: (optional) VA FileMan date to filter on “recorded”.

MAX: (optional) Number of most recent factors to return.

ID: (optional) V HEALTH FACTORS (#9000010.23) file IEN.

FILTER: (optional) None.

Output

| Elements  | Attributes | Content                                        |
|-----------|------------|------------------------------------------------|
| category  | code       | HEALTH FACTORS (#9999999.64) ien               |
|           | name       | HEALTH FACTORS (#9999999.64) Category          |
| comment   | value      | string                                         |
| encounter | value      | VISIT (#9000010) ien                           |
| facility  | code       | INSTITUTION (#4) Station Number                |
|           | name       | INSTITUTION (#4) Name                          |
| id        | value      | V HEALTH FACTORS (#9000010.23) ien             |
| name      | value      | HEALTH FACTORS (#9999999.64) Factor            |
| recorded  | value      | VA FileMan date.time                       |
| severity  | value      | MINIMAL, MODERATE, or HEAVY/SEVERE |

<span id="_Ref146260436" class="anchor"></span>Table 17: VPR GET PATIENT DATA—Immunizations: “immunizations” Type Elements Returned

### Immunizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “immunizations”.

START: (optional) VA FileMan date to filter on “administered”.

STOP: (optional) VA FileMan date to filter on “administered”.

MAX: (optional) Number of most recent immunizations to return.

ID: (optional) V IMMUNIZATION (#9000010.11) file IEN.

FILTER: (optional) None.

Output

| Elements         | Attributes  | Content                                           |
|------------------|-------------|---------------------------------------------------|
| administered     | value       | VA FileMan date.time                          |
| bodySite         | code        | IMM ADMINISTRATION SITE (#920.3) HL7 Code         |
|                  | name        | IMM ADMINISTRATION SITE (#920.3) Site             |
| comment          | value       | string                                            |
| contraindicated  | value       | boolean (1 or 0)                          |
| cpt              | code        | CPT Code                                          |
|                  | name        | CPT Short Name                                    |
| cvx              | value       | CVX Code                                          |
| documentedBy     | code        | NEW PERSON (#200) ien                             |
|                  | name        | NEW PERSON (#200) Name                            |
| dose             | value       | string                                            |
| encounter        | value       | VISIT (#9000010) ien                              |
| expirationDate   | value       | VA FileMan date.time                          |
| facility         | code        | INSTITUTION (#4) Station Number                   |
|                  | name        | INSTITUTION (#4) Name                             |
| id               | value       | V IMMUNIZATION (#9000010.11) ien                  |
| location         | value       | HOSPITAL LOCATION (#44) Name                      |
| lot              | value       | IMMUNIZATION LOT (#9999999.41) Lot Number         |
| manufacturer     | value       | IMMUNIZATION LOT (#9999999.41) Manufacturer       |
| name             | value       | IMMUNIZATION (#9999999.14) Name                   |
| orderingProvider | code        | NEW PERSON (#200) ien                             |
|                  | name        | NEW PERSON (#200) Name                            |
| provider         | code        | NEW PERSON (#200) ien                             |
|                  | name        | NEW PERSON (#200) Name                            |
| reaction         | value       | string                                            |
| route            | code        | IMM ADMINISTRATION ROUTE (#920.2) HL7 Code        |
|                  | name        | IMM ADMINISTRATION ROUTE (#920.2) Route           |
| series           | value       | PARTIALLY COMPLETE, COMPLETE, BOOSTER, SERIES 1-8 |
| source           | code        | IMMUNIZATION INFO SOURCE (#920) HL7 Code          |
|                  | name        | IMMUNIZATION INFO SOURCE (#920) Source            |
| units            | value       | string                                            |
| vis \[m\]        | date        | VA FileMan date                                   |
|                  | name        | VACCINE INFORMATION STATEMENT (#920) Name         |
|                  | editionDate | VA FileMan date                                   |
|                  | language    | string                                            |

<span id="_Toc155864401" class="anchor"></span>Table 18: VPR GET PATIENT DATA—Skin Tests: “skinTests” Type Elements Returned

### Skin Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “skinTests”.

START: (optional) VA FileMan date to filter on “dateTime”.

STOP: (optional) VA FileMan date to filter on “dateTime”.

MAX: (optional) Number of most recent skin tests to return.

ID: (optional) V SKIN TEST (#9000010.12) file IEN.

FILTER: (optional) None.

Output

| Elements  | Attributes | Content                         |
|-----------|------------|---------------------------------|
| comment   | value      | string                          |
| dateTime  | value      | VA FileMan date.time        |
| encounter | value      | VISIT (#9000010) ien            |
| facility  | code       | INSTITUTION (#4) Station Number |
|           | name       | INSTITUTION (#4) Name           |
| id        | value      | V SKIN TEST (#9000010.12) ien   |
| name      | value      | SKIN TEST (#9999999.28) Name    |
| result    | value      | string                          |

<span id="_Toc155864402" class="anchor"></span>Table 19: VPR GET PATIENT DATA—Patient Record Flags (DGPF): “flags” Type Elements Returned

## Patient Record Flags (DGPF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “flags”.

START: (optional) None.

STOP: (optional) None.

MAX: (optional) None.

ID: (optional) DFN~PRF variable pointer string.

FILTER(“nowrap”): (optional) 1 or 0, to include breaks between content lines.

Output

| Elements   | Attributes | Content                                                    |
|------------|------------|------------------------------------------------------------|
| approvedBy | code       | NEW PERSON (#200) ien                                      |
|            | name       | NEW PERSON (#200) Name                                     |
| assigned   | value      | FileMan date.time                                      |
| category   | value      | I (NATIONAL) or II (LOCAL)                 |
| content    |            | word-processing text                                       |
| document   | code       | TIU DOCUMENT (#8925) ien                                   |
|            | name       | TIU DOCUMENT DEFINITION (#8925.1) Name                     |
| id         | value      | DFN~PRF variable pointer string                            |
| name       | value      | PRF NATIONAL FLAG (#26.15) or PRF LOCAL FLAG (#26.11) Name |
| origSite   | code       | INSTITUTION (#4) Station Number                            |
|            | name       | INSTITUTION (#4) Name                                      |
| ownSite    | code       | INSTITUTION (#4) Station Number                            |
|            | name       | INSTITUTION (#4) Name                                      |
| reviewDue  | value      | VA FileMan date                                            |
| type       | value      | PRF TYPE (#26.16) Name                                     |

<span id="_Ref155790748" class="anchor"></span>Table 20: VPR GET PATIENT DATA—Inpatient (Unit Dose) Medications: “meds” Type Elements Returned

## Pharmacy (PS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All meds can be requested by omitting any filters, but more commonly a single type of medications is pulled at a time, as shown in the following tables. As each type is processed in sequence, use of MAX is discouraged with multiple types.

The PS Application Programming Interface (API) used to get the data sorts meds by expiration date and includes orders that expire on or after the START value but omit those that do *not* begin until after the STOP value.

![](virtual-patient-record-vpr-developer-s-guide/020.png) NOTE: Results can include orders that expire after the STOP value, or that have no expiration date.

### Inpatient (Unit Dose) Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “meds”.

START: (optional) VA FileMan date to filter on “expires”, chronologically.

STOP: (optional) VA FileMan date to filter on “expires”, chronologically.

MAX: (optional) Number of most recent inpatient med orders to return.

ID: (optional) ORDER (#100) file IEN.

FILTER(“vaType”): (optional) “I”.

Output

| Elements         | Attributes     |      | Content                                                                                 |
|------------------|----------------|------|-----------------------------------------------------------------------------------------|
| currentProvider  | code           |      | NEW PERSON (#200) ien                                                                   |
|                  | name           |      | NEW PERSON (#200) Name                                                                  |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                                                          |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                                                           |
|                  | fax            |      | NEW PERSON (#200) Fax Number                                                            |
|                  | email          |      | NEW PERSON (#200) Email Address                                                         |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                                                         |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                                                    |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                                                   |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization                                           |
|                  | service        |      | NEW PERSON (#200) Service/Section                                                       |
| dose \*      | dose           |      | string                                                                                  |
|                  | units          |      | string                                                                                  |
|                  | unitsPerDose   |      | number                                                                                  |
|                  | noun           |      | string                                                                                  |
|                  | route          |      | MEDICATION ROUTES (#51.2) Abbreviation                                                  |
|                  | schedule       |      | ADMINISTRATION SCHEDULE (#51.1) Name                                                    |
|                  | duration       |      | string                                                                                  |
|                  | conjunction    |      | A, T, or E                                                                  |
|                  | doseStart      |      | VA FileMan date.time                                                                |
|                  | doseStop       |      | VA FileMan date.time                                                                |
|                  | order          |      | ORDER (#100) ien                                                                        |
| facility         | code           |      | INSTITUTION (#4) Station Number                                                         |
|                  | name           |      | INSTITUTION (#4) Name                                                                   |
| form             | value          |      | DOSAGE FORM (#50.606) Name                                                              |
| id               | value          |      | ORDER (#100) ien                                                                        |
| IMO              | value          |      | boolean (1 or 0)                                                                |
| indication       | value          |      | string                                                                                  |
| location         | code           |      | HOSPITAL LOCATION (#44) ien                                                             |
|                  | name           |      | HOSPITAL LOCATION (#44) Name                                                            |
| medID            | value          |      | NON-VERIFIED ORDERS (#53.1) ien\_“P;I”, or UNIT DOSE ORDERS (#55.06) subfile ien\_“U;I” |
| name             | value          |      | PHARMACY ORDERABLE ITEM (#50.7) Name, Form                                              |
| ordered          | value          |      | VA FileMan date.time                                                                |
| orderID          | value          |      | ORDER (#100) ien                                                                        |
| orderingProvider | code           |      | NEW PERSON (#200) ien                                                                   |
|                  | name           |      | NEW PERSON (#200) Name                                                                  |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                                                          |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                                                           |
|                  | fax            |      | NEW PERSON (#200) Fax Number                                                            |
|                  | email          |      | NEW PERSON (#200) Email Address                                                         |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                                                         |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                                                    |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                                                   |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization                                           |
|                  | service        |      | NEW PERSON (#200) Service/Section                                                       |
| parent           | value          |      | ORDER (#100) ien                                                                        |
| pharmacist       | code           |      | NEW PERSON (#200) ien                                                                   |
|                  | name           |      | NEW PERSON (#200) Name                                                                  |
| product \*   | code           |      | DRUG (#50) ien                                                                          |
|                  | name           |      | DRUG (#50) Generic Name                                                                 |
|                  | role           |      | D                                                                                   |
|                  | concentration  |      | string                                                                                  |
|                  | order          |      | ORDER (#100) ien                                                                        |
|                  | class          | code | VA DRUG CLASS (#50.605) Code                                                            |
|                  |                | name | VA DRUG CLASS (#50.605) Classification                                                  |
|                  |                | vuid | VA DRUG CLASS (#50.605) VUID                                                            |
|                  | vaGeneric      | code | VA GENERIC (#50.6) ien                                                                  |
|                  |                | name | VA GENERIC (#50.6) Name                                                                 |
|                  |                | vuid | VA GENERIC (#50.6) VUID                                                                 |
|                  | vaProduct      | code | VA PRODUCT (#50.68) ien                                                                 |
|                  |                | name | VA PRODUCT (#50.68) Name                                                                |
|                  |                | vuid | VA PRODUCT (#50.68) VUID                                                                |
| sig              | value          |      | string                                                                                  |
| start            | value          |      | VA FileMan date.time                                                                |
| status           | value          |      | active, hold, historical, or not active                                 |
| stop             | value          |      | VA FileMan date.time                                                                |
| vaStatus         | value          |      | ORDER STATUS (#100.01) Name                                                             |
| vaType           | value          |      | I                                                                                       |

<span id="_Ref155790755" class="anchor"></span>Table 21: VPR GET PATIENT DATA—IV Fluids (Infusions): “meds” Type Elements Returned

\* = Can be multiple.

### IV Fluids (Infusions)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “meds”.

START: (optional) VA FileMan date to filter on “expires”, chronologically.

STOP: (optional) VA FileMan date to filter on “expires”, chronologically.

MAX: (optional) Number of most recent infusion orders to return.

ID: (optional) ORDER (#100) file IEN.

FILTER(“vaType”): (optional) “V”.

Output

| Elements         | Attributes     |      | Content                                                                          |
|------------------|----------------|------|----------------------------------------------------------------------------------|
| currentProvider  | code           |      | NEW PERSON (#200) ien                                                            |
|                  | name           |      | NEW PERSON (#200) Name                                                           |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                                                   |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                                                    |
|                  | fax            |      | NEW PERSON (#200) Fax Number                                                     |
|                  | email          |      | NEW PERSON (#200) Email Address                                                  |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                                                  |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                                             |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                                            |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization                                    |
|                  | service        |      | NEW PERSON (#200) Service/Section                                                |
| dose \*      | route          |      | MEDICATION ROUTES (#51.2) Abbreviation                                           |
|                  | schedule       |      | Administration Schedule \#51.1 Name                                              |
| facility         | code           |      | INSTITUTION (#4) Station Number                                                  |
|                  | name           |      | INSTITUTION (#4) Name                                                            |
| id               | value          |      | ORDER (#100) ien                                                                 |
| IMO              | value          |      | boolean (1 or 0)                                                         |
| indication       | value          |      | string                                                                           |
| ivLimit          | value          |      | string                                                                           |
| location         | code           |      | HOSPITAL LOCATION (#44) ien                                                      |
|                  | name           |      | HOSPITAL LOCATION (#44) Name                                                     |
| medID            | value          |      | NON-VERIFIED ORDERS (#53.1) ien\_“P;I”, or IV ORDERS (#55.01) subfile ien\_“V;I” |
| name             | value          |      | Pharmacy Orderable Item \#50.7 Name, Form                                        |
| ordered          | value          |      | VA FileMan date.time                                                         |
| orderID          | value          |      | ORDER (#100) ien                                                                 |
| orderingProvider | code           |      | NEW PERSON (#200) ien                                                            |
|                  | name           |      | NEW PERSON (#200) Name                                                           |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                                                   |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                                                    |
|                  | fax            |      | NEW PERSON (#200) Fax Number                                                     |
|                  | email          |      | NEW PERSON (#200) Email Address                                                  |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                                                  |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                                             |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                                            |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization                                    |
|                  | service        |      | NEW PERSON (#200) Service/Section                                                |
| pharmacist       | code           |      | NEW PERSON (#200) ien                                                            |
|                  | name           |      | NEW PERSON (#200) Name                                                           |
| product \*   | code           |      | DRUG (#50) ien                                                                   |
|                  | name           |      | DRUG (#50) Generic Name                                                          |
|                  | role           |      | A or B                                                                   |
|                  | concentration  |      | string                                                                           |
|                  | class          | code | VA DRUG CLASS (#50.605) Code                                                     |
|                  |                | name | VA DRUG CLASS (#50.605) Classification                                           |
|                  |                | vuid | VA DRUG CLASS (#50.605) VUID                                                     |
|                  | ordItem        | code | PHARMACY ORDERABLE ITEM (#50.7) ien                                              |
|                  |                | name | PHARMACY ORDERABLE ITEM (#50.7) Name, Form                                       |
|                  | vaGeneric      | code | VA GENERIC (#50.6) ien                                                           |
|                  |                | name | VA GENERIC (#50.6) Name                                                          |
|                  |                | vuid | VA GENERIC (#50.6) VUID                                                          |
|                  | vaProduct      | code | VA PRODUCT (#50.68) ien                                                          |
|                  |                | name | VA PRODUCT (#50.68) Name                                                         |
|                  |                | vuid | VA PRODUCT (#50.68) VUID                                                         |
| rate             | value          |      | string                                                                           |
| start            | value          |      | VA FileMan date.time                                                         |
| status           | value          |      | active, hold, historical, or not active                          |
| stop             | value          |      | VA FileMan date.time                                                         |
| vaStatus         | value          |      | ORDER STATUS (#100.01) Name                                                      |
| vaType           | value          |      | V                                                                            |

<span id="_Ref155790765" class="anchor"></span>Table 22: VPR GET PATIENT DATA—Outpatient Medications: “meds” Type Elements Returned

\* = Can be multiple.

### Outpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “meds”.

START: (optional) VA FileMan date to filter on “expires”, chronologically.

STOP: (optional) VA FileMan date to filter on “expires”, chronologically.

MAX: (optional) Number of most recent outpatient med orders to return.

ID: (optional) ORDER (#100) file IEN.

FILTER(“vaType”): (optional) “O”.

Output

| Elements         | Attributes     |      | Content                                                                              |
|------------------|----------------|------|--------------------------------------------------------------------------------------|
| currentProvider  | code           |      | NEW PERSON (#200) ien                                                                |
|                  | name           |      | NEW PERSON (#200) Name                                                               |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                                                       |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                                                        |
|                  | fax            |      | NEW PERSON (#200) Fax Number                                                         |
|                  | email          |      | NEW PERSON (#200) Email Address                                                      |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                                                      |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                                                 |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                                                |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization                                        |
|                  | service        |      | NEW PERSON (#200) Service/Section                                                    |
| daysSupply       | value          |      | number                                                                               |
| dose \*      | dose           |      | string                                                                               |
|                  | units          |      | string                                                                               |
|                  | unitsPerDose   |      | number                                                                               |
|                  | noun           |      | string                                                                               |
|                  | route          |      | MEDICATION ROUTES (#51.2) Abbreviation                                               |
|                  | schedule       |      | ADMINISTRATION SCHEDULE (#51.1) Name                                                 |
|                  | duration       |      | string                                                                               |
|                  | conjunction    |      | A, T, or E                                                               |
|                  | doseStart      |      | VA FileMan date.time                                                             |
|                  | doseStop       |      | VA FileMan date.time                                                             |
| expires          | value          |      | VA FileMan date                                                                      |
| facility         | code           |      | INSTITUTION (#4) Station Number                                                      |
|                  | name           |      | INSTITUTION (#4) Name                                                                |
| fill \*      | fillDate       |      | VA FileMan date                                                                      |
|                  | fillRouting    |      | W, M, or C                                                               |
|                  | releaseDate    |      | VA FileMan date                                                                      |
|                  | fillQuantity   |      | number                                                                               |
|                  | fillDaysSupply |      | number                                                                               |
|                  | partial        |      | boolean (1 or 0)                                                             |
| fillCost         | value          |      | number                                                                               |
| fillsAllowed     | value          |      | number                                                                               |
| fillsRemaining   | value          |      | number                                                                               |
| form             | value          |      | DOSAGE FORM (#50.606) Name                                                           |
| id               | value          |      | ORDER (#100) ien                                                                     |
| indication       | value          |      | string                                                                               |
| lastFilled       | value          |      | VA FileMan date.time                                                             |
| location         | code           |      | HOSPITAL LOCATION (#44) ien                                                          |
|                  | name           |      | HOSPITAL LOCATION (#44) Name                                                         |
| medID            | value          |      | PENDING OUTPATIENT ORDERS (#52.41) ien\_“P;O”, or PRESCRIPTION (#52) file ien\_“R;O” |
| name             | value          |      | PHARMACY ORDERABLE ITEM (#50.7) Name, Form                                           |
| ordered          | value          |      | VA FileMan date.time                                                             |
| orderID          | value          |      | ORDER (#100) ien                                                                     |
| orderingProvider | code           |      | NEW PERSON (#200) ien                                                                |
|                  | name           |      | NEW PERSON (#200) Name                                                               |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                                                       |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                                                        |
|                  | fax            |      | NEW PERSON (#200) Fax Number                                                         |
|                  | email          |      | NEW PERSON (#200) Email Address                                                      |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                                                      |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                                                 |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                                                |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization                                        |
|                  | service        |      | NEW PERSON (#200) Service/Section                                                    |
| parked           | value          |      | boolean (1 or 0)                                                             |
| pharmacist       | code           |      | NEW PERSON (#200) ien                                                                |
|                  | name           |      | NEW PERSON (#200) Name                                                               |
| prescription     | value          |      | string                                                                               |
| product \*   | code           |      | DRUG (#50) ien                                                                       |
|                  | name           |      | DRUG (#50) Generic Name                                                              |
|                  | role           |      | D                                                                                    |
|                  | concentration  |      | string                                                                               |
|                  | class          | code | VA DRUG CLASS (#50.605) Code                                                         |
|                  |                | name | VA DRUG CLASS (#50.605) Classification                                               |
|                  |                | vuid | VA DRUG CLASS (#50.605) VUID                                                         |
|                  | vaGeneric      | code | VA GENERIC (#50.6) ien                                                               |
|                  |                | name | VA GENERIC (#50.6) Name                                                              |
|                  |                | vuid | VA GENERIC (#50.6) VUID                                                              |
|                  | vaProduct      | code | VA PRODUCT (#50.68) ien                                                              |
|                  |                | name | VA PRODUCT (#50.68) Name                                                             |
|                  |                | vuid | VA PRODUCT (#50.68) VUID                                                             |
| ptInstructions   | value          |      | string                                                                               |
| quantity         | value          |      | number                                                                               |
| routing          | value          |      | W, M, or C                                                               |
| sig              | value          |      | string                                                                               |
| start            | value          |      | VA FileMan date.time                                                             |
| status           | value          |      | active, hold, historical, or not active                              |
| stop             | value          |      | VA FileMan date.time                                                             |
| supply           | value          |      | boolean (1 or 0)                                                             |
| type             | value          |      | Prescription                                                                         |
| vaStatus         | value          |      | ORDER STATUS (#100.01) Name                                                          |
| vaType           | value          |      | O                                                                                |

<span id="_Ref155790770" class="anchor"></span>Table 23: VPR GET PATIENT DATA—Non-VA Medications: “meds” Type Elements Returned

\* = Can be multiple.

### Non-VA Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “meds”.

START: (optional) VA FileMan date to filter on “expires”, chronologically.

STOP: (optional) VA FileMan date to filter on “expires”, chronologically.

MAX: (optional) Number of most recent non-VA med orders to return.

ID: (optional) ORDER (#100) file IEN.

FILTER(“vaType”): (optional) “N”.

Output

| Elements         | Attributes     |      | Content                                                 |
|------------------|----------------|------|---------------------------------------------------------|
| currentProvider  | code           |      | NEW PERSON (#200) ien                                   |
|                  | name           |      | NEW PERSON (#200) Name                                  |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                          |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                           |
|                  | fax            |      | NEW PERSON (#200) Fax Number                            |
|                  | email          |      | NEW PERSON (#200) Email Address                         |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                         |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                    |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                   |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization           |
|                  | service        |      | NEW PERSON (#200) Service/Section                       |
| dose \[m\]       | dose           |      | string                                                  |
|                  | units          |      | string                                                  |
|                  | unitsPerDose   |      | number                                                  |
|                  | noun           |      | string                                                  |
|                  | route          |      | MEDICATION ROUTES (#51.2) Abbreviation                  |
|                  | schedule       |      | ADMINISTRATION SCHEDULE (#51.1) Name                    |
| facility         | code           |      | INSTITUTION (#4) Station Number                         |
|                  | name           |      | INSTITUTION (#4) Name                                   |
| form             | value          |      | DOSAGE FORM (#50.606) Name                              |
| id               | value          |      | ORDER (#100) ien                                        |
| indication       | value          |      | string                                                  |
| location         | code           |      | HOSPITAL LOCATION (#44) ien                             |
|                  | name           |      | HOSPITAL LOCATION (#44) Name                            |
| medID            | value          |      | NON-VA MED ORDERS (#55.05) subfile ien\_“N;O”           |
| name             | value          |      | PHARMACY ORDERABLE ITEM (#50.7) Name, Form              |
| ordered          | value          |      | VA FileMan date.time                                |
| orderID          | value          |      | ORDER (#100) ien                                        |
| orderingProvider | code           |      | NEW PERSON (#200) ien                                   |
|                  | name           |      | NEW PERSON (#200) Name                                  |
|                  | officePhone    |      | NEW PERSON (#200) Office Phone                          |
|                  | analogPager    |      | NEW PERSON (#200) Voice Pager                           |
|                  | fax            |      | NEW PERSON (#200) Fax Number                            |
|                  | email          |      | NEW PERSON (#200) Email Address                         |
|                  | taxonomyCode   |      | PERSON CLASS (#8932.1) X12 Code                         |
|                  | providerType   |      | PERSON CLASS (#8932.1) Provider Type                    |
|                  | classification |      | PERSON CLASS (#8932.1) Classification                   |
|                  | specialization |      | PERSON CLASS (#8932.1) Area of Specialization           |
|                  | service        |      | NEW PERSON (#200) Service/Section                       |
| product \[m\]    | code           |      | DRUG (#50) ien                                          |
|                  | name           |      | DRUG (#50) Generic Name                                 |
|                  | role           |      | D                                                       |
|                  | concentration  |      | string                                                  |
|                  | class          | code | VA DRUG CLASS (#50.605) Code                            |
|                  |                | name | VA DRUG CLASS (#50.605) Classification                  |
|                  |                | vuid | VA DRUG CLASS (#50.605) VUID                            |
|                  | vaGeneric      | code | VA GENERIC (#50.6) ien                                  |
|                  |                | name | VA GENERIC (#50.6) Name                                 |
|                  |                | vuid | VA GENERIC (#50.6) VUID                                 |
|                  | vaProduct      | code | VA PRODUCT (#50.68) ien                                 |
|                  |                | name | VA PRODUCT (#50.68) Name                                |
|                  |                | vuid | VA PRODUCT (#50.68) VUID                                |
| sig              |                |      | string                                                  |
| start            |                |      | VA FileMan date.time                                |
| status           |                |      | active, hold, historical, or not active |
| stop             |                |      | VA FileMan date.time                                |
| type             |                |      | OTC                                                     |
| vaStatus         |                |      | ORDER STATUS (#100.01) Name                             |
| vaType           |                |      | N                                                   |

<span id="_Toc155864407" class="anchor"></span>Table 24: VPR GET PATIENT DATA—Problem List (GMPL): “problems” Type Elements Returned

\* = Can be multiple.

### Medications by Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An alternate domain name is available for each med type that instead runs reverse-chronologically on the ORDER (#100) file, filtering by the “ordered” date *without* regard to medication type; thus, MAX can be safely used and return the most recent set of orders of the desired type(s). Request TYPE of “pharmacy” to use this method instead.

This domain also supports the different order views available in the Orders (OR) domain.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “pharmacy”.

START: (optional) VA FileMan date to filter on “ordered”, chronologically.

STOP: (optional) VA FileMan date to filter on “ordered”, chronologically.

MAX: (optional) Number of most recent med orders to return.

ID: (optional) ORDER (#100) file IEN.

FILTER(“vaType”): (optional) “I”, “V”, “O”, or “N”.

FILTER(“view”): (optional) Desired “view” code from ^ORQ1 (only 1-7, 18, and 23 are supported). Default = 6 (Released Orders).

This domain returns the same data elements as the other Pharmacy domains in Section <u>3.12</u>.

![](virtual-patient-record-vpr-developer-s-guide/021.png) REF: For details on each medication type, see <u>Table 20</u> through <u>Table 23</u>.

## Problem List (GMPL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “problems”.

START: (optional) VA FileMan date to filter on “onset”.

STOP: (optional) VA FileMan date to filter on “onset”.

MAX: (optional) Use *not recommended*, as problems are *not* sorted.

ID: (optional) Problem file \#9000011 IEN.

FILTER(“status”): (optional) Desired “status” code. Default = “” (all).

Output

| Element         | Attributes  | Content                                                       |
|-----------------|-------------|---------------------------------------------------------------|
| acuity          | code        | A or C                                                |
|                 | name        | ACUTE or CHRONIC                                      |
| codingSystem    | value       | ICD or 10D                                                    |
| comment         | id          | number                                                        |
|                 | enteredBy   | NEW PERSON (#200) Name                                        |
|                 | entered     | VA FileMan date                                               |
|                 | commentText | string                                                        |
| entered         | value       | date                                                          |
| exposure \* | value       | AO, IR, PG, HNC, MST, CV, or SHAD |
| facility        | code        | INSTITUTION (#4) Station Number                               |
|                 | name        | INSTITUTION (#4) Name                                         |
| icd             | value       | ICD code                                                      |
| icdd            | value       | ICD Description                                               |
| id              | value       | PROBLEM (#9000011) ien                                        |
| location        | value       | HOSPITAL LOCATION (#44) name                                  |
| name            | value       | PROVIDER NARRATIVE (#9999999.27) Narrative                    |
| onset           | value       | VA FileMan date                                               |
| provider        | code        | NEW PERSON (#200) ien                                         |
|                 | name        | NEW PERSON (#200) Name                                        |
| removed         | value       | boolean (1 or 0)                                      |
| resolved        | value       | VA FileMan date                                               |
| sc              | value       | boolean (1 or 0)                                      |
| sctc            | value       | SNOMED Concept Code                                           |
| sctd            | value       | SNOMED Designation Code                                       |
| sctt            | value       | SNOMED Preferred Text                                         |
| service         | value       | SERVICE (#49) Name                                            |
| status          | code        | A or I                                                |
|                 | name        | ACTIVE or INACTIVE                                            |
| unverified      | value       | boolean (1 or 0)                                      |
| updated         | value       | VA FileMan date                                               |

<span id="_Toc155864408" class="anchor"></span>Table 25: VPR GET PATIENT DATA—Radiology/Nuclear Medicine (RA): “radiologyExams” Type Elements Returned

\* = Can be multiple.

## Radiology/Nuclear Medicine (RA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “radiologyExams”.

START: (optional) VA FileMan date to filter on “dateTime”.

STOP: (optional) VA FileMan date to filter on “dateTime”.

MAX: (optional) Number of most recent exams to return.

ID: EXAMINATIONS (#70.03) subfile IEN string.

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements        | Attributes     | Content                                                             |
|-----------------|----------------|---------------------------------------------------------------------|
| case            | value          | number                                                              |
| category        | value          | RA                                                              |
| dateTime        | value          | VA FileMan date.time                                            |
| document \* | id             | TIU DOCUMENT (#8925) ien                                            |
|                 | localTitle     | TIU DOCUMENT DEFINITION (#8925.1) Name                              |
|                 | nationalTitle  | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)                         |
|                 | vuid           | VUID number                                                         |
|                 | status         | Verified, Released/NotVerified, or Electronically Filed |
|                 | content        | word-processing text                                                |
| encounter       | value          | VISIT (#9000010) ien                                                |
| facility        | code           | INSTITUTION (#4) Station Number                                     |
|                 | name           | INSTITUTION (#4) Name                                               |
| hasImages       | value          | boolean (1 or 0)                                            |
| id              | value          | EXAMINATIONS (#70.03) subfile ien string                            |
| imagingType     | code           | IMAGING TYPE (#79.2) Abbreviation                                   |
|                 | name           | IMAGING TYPE (#79.2) Type of Imaging                                |
| interpretation  | value          | string                                                              |
| location        | code           | HOSPITAL LOCATION (#44) ien                                         |
|                 | name           | HOSPITAL LOCATION (#44) name                                        |
| modifier \* | code           | CPT Modifier                                                        |
|                 | name           | CPT Modifier Name                                                   |
| name            | value          | RAD/NUC MED PROCEDURES (#71) Name                                   |
| order           | code           | ORDER (#100) ien                                                    |
|                 | name           | ORDERABLE ITEMS (#101.43) Name                                      |
| provider        | code           | NEW PERSON (#200) ien                                               |
|                 | name           | NEW PERSON (#200) Name                                              |
|                 | officePhone    | NEW PERSON (#200) Office Phone                                      |
|                 | analogPager    | NEW PERSON (#200) Voice Pager                                       |
|                 | fax            | NEW PERSON (#200) Fax Number                                        |
|                 | email          | NEW PERSON (#200) Email Address                                     |
|                 | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                                     |
|                 | providerType   | PERSON CLASS (#8932.1) Provider Type                                |
|                 | classification | PERSON CLASS (#8932.1) Classification                               |
|                 | specialization | PERSON CLASS (#8932.1) Area of Specialization                       |
|                 | service        | NEW PERSON (#200) Service/Section                                   |
| radOrderID      | value          | RAD/NUC MED ORDERS (#75.1) ien                                      |
| status          | value          | COMPLETE, CANCELLED, EXAMINED, WAITING FOR EXAM, or CALLED FOR EXAM |
| type            | code           | CPT Code                                                            |
|                 | name           | CPT Description                                                     |
| urgency         | value          | STAT, ASAP, or ROUTINE                                  |

<span id="_Ref155790781" class="anchor"></span>Table 26: VPR GET PATIENT DATA—Registration (DPT): “demographics” Type Elements Returned

\* = Can be multiple.

## Registration (DPT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “demographics”.

START: (optional) None.

STOP: (optional) None.

MAX: (optional) None.

ID: (optional) PATIENT (#2) file IEN.

FILTER(“nowrap”): (optional) 1 or 0, to include breaks between lines in flag text.

Output

| Elements                   | Attributes     |               | Content                                                                                                                                                                                  |
|----------------------------|----------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| address                    | streetLine1    |               | string                                                                                                                                                                                   |
|                            | streetLine2    |               | string                                                                                                                                                                                   |
|                            | streetLine3    |               | string                                                                                                                                                                                   |
|                            | city           |               | string                                                                                                                                                                                   |
|                            | stateProvince  |               | STATE (#5) Name                                                                                                                                                                          |
|                            | postalCode     |               | string                                                                                                                                                                                   |
| admitted <sup>†</sup>  | id             |               | PATIENT MOVEMENT (#405) ien                                                                                                                                                              |
|                            | date           |               | PATIENT MOVEMENT (#405) Date/Time                                                                                                                                                        |
| alias \*               | fullName       |               | string                                                                                                                                                                                   |
|                            | familyName     |               | string                                                                                                                                                                                   |
|                            | givenNames     |               | string                                                                                                                                                                                   |
| attending <sup>†</sup> | code           |               | NEW PERSON (#200) ien                                                                                                                                                                    |
|                            | name           |               | NEW PERSON (#200) Name                                                                                                                                                                   |
| bid                        | value          |               | String                                                                                                                                                                                   |
| died                       | value          |               | VA FileMan date                                                                                                                                                                          |
| disability \*          | printName      |               | DISABILITY CONDITION (#31) Name                                                                                                                                                          |
|                            | scPercent      |               | number                                                                                                                                                                                   |
|                            | sc             |               | boolean (1 or 0)                                                                                                                                                                 |
| dob                        | value          |               | VA FileMan date                                                                                                                                                                          |
| eligibility \*         | name           |               | ELIGIBILITY (#8) Name                                                                                                                                                                    |
|                            | primary        |               | boolean (1 or 0)                                                                                                                                                                 |
| eligibilityStatus          | value          |               | PENDING \[RE\]VERIFICATION or VERIFIED                                                                                                                                           |
| ethnicity \*           | value          |               | ETHNICITY (#10.2) HL7 Value                                                                                                                                                              |
| exposure \*            | value          |               | AO, IR, PG, HNC, MST, or CV                                                                                                                                      |
| facility \*            | id             |               | INSTITUTION (#4) Station Number                                                                                                                                                          |
|                            | name           |               | INSTITUTION (#4) Name                                                                                                                                                                    |
|                            | latestDate     |               | VA FileMan date.time                                                                                                                                                                 |
|                            | domain         |               | DOMAIN (#4.2) Name                                                                                                                                                                       |
|                            | homeSite       |               | boolean (1 or 0)                                                                                                                                                                 |
| familyName                 | value          |               | string                                                                                                                                                                                   |
| flag \*                | name           |               | PRF NATIONAL FLAG (#26.15) or PRF LOCAL FLAG (#26.11) Name                                                                                                                               |
|                            | text           |               | string                                                                                                                                                                                   |
| fullName                   | value          |               | string                                                                                                                                                                                   |
| gender                     | value          |               | M, F, or UN                                                                                                                                                                  |
| givenNames                 | value          |               | string                                                                                                                                                                                   |
| Icn                        | value          |               | ICN number                                                                                                                                                                               |
| Id                         | value          |               | PATIENT (#2) ien                                                                                                                                                                         |
| inpatient                  | value          |               | boolean (1 or 0)                                                                                                                                                                 |
| language                   | code           |               | ISO 639 2-character language code                                                                                                                                                        |
|                            | name           |               | string                                                                                                                                                                                   |
| location <sup>†</sup>  | code           |               | HOSPITAL LOCATION (#44) ien                                                                                                                                                              |
|                            | name           |               | HOSPITAL LOCATION (#44) Name                                                                                                                                                             |
| locSvc <sup>†</sup>    | code           |               | M, S, P, NH, NE, I, R, SCI, D, B, or NC                                                                                                      |
|                            | name           |               | MEDICINE, SURGERY, PSYCHIATRY, NHCU, NEUROLOGY, INTERMEDIATE MED, REHAB MEDICINE, SPINAL CORD INJURY, DOMICILIARY, BLIND REHAB, or NON-COUNT |
| lrdfn                      | value          |               | number                                                                                                                                                                                   |
| maritalStatus              | value          |               | D, M, W, S, N, or U                                                                                                                                              |
| meansTest                  | value          |               | MEANS TEST STATUS (#408.32) Name                                                                                                                                                         |
| pcAssigned                 | value          |               | VA FileMan date                                                                                                                                                                          |
| pcProvider                 | code           |               | NEW PERSON (#200) ien                                                                                                                                                                    |
|                            | name           |               | NEW PERSON (#200) Name                                                                                                                                                                   |
|                            | officePhone    |               | NEW PERSON (#200) Office Phone                                                                                                                                                           |
|                            | analogPager    |               | NEW PERSON (#200) Voice Pager                                                                                                                                                            |
|                            | fax            |               | NEW PERSON (#200) Fax Number                                                                                                                                                             |
|                            | email          |               | NEW PERSON (#200) Email Address                                                                                                                                                          |
|                            | taxonomyCode   |               | PERSON CLASS (#8932.1) X12 Code                                                                                                                                                          |
|                            | providerType   |               | PERSON CLASS (#8932.1) Provider Type                                                                                                                                                     |
|                            | classification |               | PERSON CLASS (#8932.1) Classification                                                                                                                                                    |
|                            | specialization |               | PERSON CLASS (#8932.1) Area of Specialization                                                                                                                                            |
|                            | service        |               | NEW PERSON (#200) Service/Section                                                                                                                                                        |
|                            | address        | streetLine1   | string                                                                                                                                                                                   |
|                            |                | streetLine2   | string                                                                                                                                                                                   |
|                            |                | streetLine3   | string                                                                                                                                                                                   |
|                            |                | city          | string                                                                                                                                                                                   |
|                            |                | stateProvince | STATE (#5) Name                                                                                                                                                                          |
|                            |                | postalCode    | string                                                                                                                                                                                   |
| pcTeam                     | code           |               | TEAM (#404.51) ien                                                                                                                                                                       |
|                            | name           |               | TEAM (#404.51) Name                                                                                                                                                                      |
| pcTeamMember               | code           |               | NEW PERSON (#200) ien                                                                                                                                                                    |
|                            | name           |               | NEW PERSON (#200) Name                                                                                                                                                                   |
|                            | officePhone    |               | NEW PERSON (#200) Office Phone                                                                                                                                                           |
|                            | analogPager    |               | NEW PERSON (#200) Voice Pager                                                                                                                                                            |
|                            | fax            |               | NEW PERSON (#200) Fax Number                                                                                                                                                             |
|                            | email          |               | NEW PERSON (#200) Email Address                                                                                                                                                          |
|                            | taxonomyCode   |               | PERSON CLASS (#8932.1) X12 Code                                                                                                                                                          |
|                            | providerType   |               | PERSON CLASS (#8932.1) Provider Type                                                                                                                                                     |
|                            | classification |               | PERSON CLASS (#8932.1) Classification                                                                                                                                                    |
|                            | specialization |               | PERSON CLASS (#8932.1) Area of Specialization                                                                                                                                            |
|                            | service        |               | NEW PERSON (#200) Service/Section                                                                                                                                                        |
| race \*                | value          |               | RACE (#10) HL7 Value                                                                                                                                                                     |
| religion                   | value          |               | RELIGIOUS PREFERENCE (#13) Name                                                                                                                                                          |
| roomBed <sup>†</sup>   | value          |               | string                                                                                                                                                                                   |
| sc                         | value          |               | boolean (1 or 0)                                                                                                                                                                 |
| scPercent                  | value          |               | number                                                                                                                                                                                   |
| sensitive                  | value          |               | boolean (1 or 0)                                                                                                                                                                 |
| servicePeriod              | value          |               | PERIOD OF SERVICE (#21) Name                                                                                                                                                             |
| site <sup>†</sup>      | code           |               | INSTITUTION (#4) Station Number                                                                                                                                                          |
|                            | name           |               | INSTITUTION (#4) Name                                                                                                                                                                    |
| specialty <sup>†</sup> | code           |               | FACILITY TREATING SPECIALTY (#45.7) ien                                                                                                                                                  |
|                            | name           |               | FACILITY TREATING SPECIALTY (#45.7) Name                                                                                                                                                 |
| ssn                        | value          |               | string                                                                                                                                                                                   |
| support \*             | contactType    |               | NOK or ECON                                                                                                                                                                      |
|                            | name           |               | string                                                                                                                                                                                   |
|                            | relationship   |               | string                                                                                                                                                                                   |
|                            | address        | streetLine1   | string                                                                                                                                                                                   |
|                            |                | streetLine2   | string                                                                                                                                                                                   |
|                            |                | streetLine3   | string                                                                                                                                                                                   |
|                            |                | city          | string                                                                                                                                                                                   |
|                            |                | stateProvince | STATE (#5) Name                                                                                                                                                                          |
|                            |                | postalCode    | string                                                                                                                                                                                   |
|                            | telecom        | usageType     | H, MC, or WP                                                                                                                                                                 |
|                            |                | value         | string                                                                                                                                                                                   |
| telecom                    | usageType      |               | H, MC, or WP                                                                                                                                                                 |
|                            | value          |               | string                                                                                                                                                                                   |
| veteran                    | value          |               | boolean (1 or 0)                                                                                                                                                                 |
| ward <sup>†</sup>      | code           |               | WARD LOCATION (#42) ien                                                                                                                                                                  |
|                            | name           |               | WARD LOCATION (#42) Name                                                                                                                                                                 |

<span id="_Ref146260456" class="anchor"></span>Table 27: VPR GET PATIENT DATA—Scheduling (SDAM): “appointments” Type Elements Returned

\* = Can be multiple.

† = Only populated if the patient is currently admitted.

## Scheduling (SDAM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling API sorts appointments by dateTime chronologically; while past appointments are available, the default view is to extract a patient’s future appointments.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “appointments”.

START: (optional) VA FileMan date to filter on “dateTime”. Default = TODAY.

STOP: (optional) VA FileMan date to filter on “dateTime”. Default = all future.

MAX: (optional) Number of (future) appointments to return.

ID: (optional) Inverse visit string (“servCatg;date.time;locationIEN”).

FILTER(“status”): (optional) Desired status code(s). For possible values, see the “Application Programming Interface – SDAPI/Available Data Filters” section in the Patient Information Management System (PIMS) Technical Manual.

Output

| Elements        | Attributes | Content                                                                                                                                                                                     |
|-----------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| apptStatus      | value      | SCHEDULED/KEPT, INPATIENT, NO-SHOW, CANCELLED BY PATIENT, CANCELLED BY CLINIC, RESCHEDULED, NO ACTION TAKEN                                                     |
| cancelled       | value      | VA FileMan date.time                                                                                                                                                                    |
| cancelReason    | value      | CANCELLATION REASONS (#409.2) Name                                                                                                                                                          |
| checkIn         | value      | VA FileMan date.time                                                                                                                                                                    |
| checkOut        | value      | VA FileMan date.time                                                                                                                                                                    |
| clinicStop      | code       | CLINIC STOP (#40.7) AMIS StopCode                                                                                                                                                           |
|                 | name       | CLINIC STOP (#40.7)7 Name                                                                                                                                                                   |
| dateTime        | value      | VA FileMan date.time                                                                                                                                                                    |
| facility        | code       | INSTITUTION (#4) Station Number                                                                                                                                                             |
|                 | name       | INSTITUTION (#4) Name                                                                                                                                                                       |
| id              | value      | serviceCategory code;dateTime;HOSPITAL LOCATION (#44) ien                                                                                                                                   |
| location        | value      | HOSPITAL LOCATION (#44) Name                                                                                                                                                                |
| patientClass    | value      | AMB, IMP, or EMER                                                                                                                                                               |
| provider        | code       | NEW PERSON (#200) ien                                                                                                                                                                       |
|                 | name       | NEW PERSON (#200) Name                                                                                                                                                                      |
| service         | value      | MEDICINE, SURGERY, PSYCHIATRY, NHCU, NEUROLOGY, INTERMEDIATE MED, REHAB MEDICINE, SPINAL CORD INJURY, DOMICILIARY, BLIND REHAB, or RESPITE CARE |
| serviceCategory | code       | A, I, or H                                                                                                                                                                      |
|                 | name       | AMBULATORY, INPATIENT VISIT, or HOSPITALIZATION                                                                                                                                 |
| type            | code       | APPOINTMENT TYPE (#409.1) ien                                                                                                                                                               |
|                 | name       | APPOINTMENT TYPE (#409.1) Name                                                                                                                                                              |
| visit           | value      | VISIT (#9000010) ien                                                                                                                                                                        |
| visitString     | value      | HOSPITAL LOCATION (#44) ien;dateTime; serviceCategory code                                                                                                                                  |

<span id="_Ref155790807" class="anchor"></span>Table 28: VPR GET PATIENT DATA—Surgery (SR): “surgeries” Type Elements Returned

## Surgery (SR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “surgeries”.

START: (optional) VA FileMan date to filter on “dateTime”.

STOP: (optional) VA FileMan date to filter on “dateTime”.

MAX: (optional) Number of most recent surgical procedures to return.

ID: (optional) SURGERY (#130) file IEN.

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements              | Attributes     | Content                                       |
|-----------------------|----------------|-----------------------------------------------|
| category              | value          | SR                                        |
| dateTime              | value          | VA FileMan date                               |
| document \*       | id             | TIU DOCUMENT (#8925) ien                      |
|                       | localTitle     | TIU DOCUMENT DEFINITION (#8925.1) Name        |
|                       | nationalTitle  | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)   |
|                       | vuid           | VUID number                                   |
|                       | content        | word-processing text                          |
| encounter             | value          | VISIT (#9000010) ien                          |
| facility              | code           | INSTITUTION (#4) Station Number               |
|                       | name           | INSTITUTION (#4) Name                         |
| id                    | value          | SURGERY (#130) ien                            |
| modifier \*       | code           | CPT Modifier                                  |
|                       | name           | CPT Modifier Name                             |
| name                  | value          | string                                        |
| opReport              | id             | TIU DOCUMENT (#8925) ien                      |
|                       | localTitle     | TIU DOCUMENT DEFINITION (#8925.1) Name        |
|                       | nationalTitle  | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)   |
|                       | vuid           | VUID number                                   |
| otherProcedure \* | code           | CPT Code                                      |
|                       | name           | CPT Description                               |
| provider              | code           | NEW PERSON (#200) ien                         |
|                       | name           | NEW PERSON (#200) Name                        |
|                       | officePhone    | NEW PERSON (#200) Office Phone                |
|                       | analogPager    | NEW PERSON (#200) Voice Pager                 |
|                       | fax            | NEW PERSON (#200) Fax Number                  |
|                       | email          | NEW PERSON (#200) Email Address               |
|                       | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code               |
|                       | providerType   | PERSON CLASS (#8932.1) Provider Type          |
|                       | classification | PERSON CLASS (#8932.1) Classification         |
|                       | specialization | PERSON CLASS (#8932.1) Area of Specialization |
|                       | service        | NEW PERSON (#200) Service/Section             |
| status                | value          | COMPLETED or ABORTED                  |
| type                  | code           | CPT Code                                      |
|                       | name           | CPT Description                               |

<span id="_Ref139552273" class="anchor"></span>Table 29: VPR GET PATIENT DATA—Text Integration Utilities (TIU): “documents” Type Elements Returned

## Text Integration Utilities (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Completed TIU Documents in the Progress Note and Discharge Summary classes are returned *without* text by default unless otherwise requested. Usually, Clinical Procedure (CP), Lab (LR), and Surgery (SR) reports are in their own classes and *must* be requested separately.

The document extract can also return reports from other sources, in addition to TIU. See the following sub-sections for other supported source files.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “documents”.

START: (optional) VA FileMan date to filter on “referenceDateTime”.

STOP: (optional) VA FileMan date to filter on “referenceDateTime”.

MAX: (optional) Number of most recent documents to return.

ID: (optional) TIU DOCUMENTS (#8925) file IEN.

FILTER(“category”): (optional) Desired “category” code.

FILTER(“status”): (optional) “completed”, “unsigned”, or “all” (for current user).

FILTER(“loinc”): (optional) LOINC code (see [LOINC codes](#LOINC_codes) list following (<u>Table 29</u>).

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements             | Attributes     | Content                                                                       |
|----------------------|----------------|-------------------------------------------------------------------------------|
| category             | value          | PN, DS, CR, CP, SR, LR, C, W, A, or D |
| clinician \[m\]      | code           | NEW PERSON (#200) ien                                                         |
|                      | name           | NEW PERSON (#200) Name                                                        |
|                      | role           | A, S, or C                                                        |
|                      | dateTime       | VA FileMan date.time                                                      |
|                      | signatureBlock | string                                                                        |
|                      | officePhone    | NEW PERSON (#200) Office Phone                                                |
|                      | analogPager    | NEW PERSON (#200) Voice Pager                                                 |
|                      | fax            | NEW PERSON (#200) Fax Number                                                  |
|                      | email          | NEW PERSON (#200) Email Address                                               |
|                      | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                                               |
|                      | providerType   | PERSON CLASS (#8932.1) Provider Type                                          |
|                      | classification | PERSON CLASS (#8932.1) Classification                                         |
|                      | specialization | PERSON CLASS (#8932.1) Area of Specialization                                 |
|                      | service        | NEW PERSON (#200) Service/Section                                             |
| content              |                | word-processing text                                                          |
| documentClass        | value          | TIU DOCUMENT DEFINITION (#8925.1) Name                                        |
| encounter            | value          | VISIT (#9000010) ien                                                          |
| facility             | code           | INSTITUTION (#4) Station Number                                               |
|                      | name           | INSTITUTION (#4) Name                                                         |
| id                   | value          | TIU DOCUMENTS (#8925) ien                                                     |
| images               | value          | number                                                                        |
| localTitle           | value          | TIU DOCUMENT DEFINITION (#8925.1) Name                                        |
| loinc                | value          | LOINC code                                                                    |
| nationalTitle        | code           | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1) VUID                              |
|                      | name           | TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)                                   |
| nationalTitleRole    | code           | TIU LOINC ROLE (#8926.3) VUID                                                 |
|                      | name           | TIU LOINC ROLE (#8926.3) Role                                                 |
| nationalTitleService | code           | TIU LOINC SERVICE (#8926.5) VUID                                              |
|                      | name           | TIU LOINC SERVICE (#8926.5) Service                                           |
| nationalTitleSetting | code           | TIU LOINC SETTING (#8926.4) VUID                                              |
|                      | name           | TIU LOINC SETTING (#8926.4) Setting                                           |
| nationalTitleSubject | code           | TIU LOINC SUBJ MATTER DOMN (#8926.2) VUID                                     |
|                      | name           | TIU LOINC SUBJECT MATTER DOMAIN (#8926.2)                                     |
| nationalTitleType    | code           | TIU LOINC DOCUMENT TYPE (#8926.6) VUID                                        |
|                      | name           | TIU LOINC DOCUMENT TYPE (#8926.6) Doc Type                                    |
| parent               | value          | TIU DOCUMENTS (#8925) ien                                                     |
| referenceDateTime    | value          | VA FileMan date.time                                                      |
| status               | value          | TIU STATUS (#8925.6) Name, in lowercase                                       |
| subject              | value          | string                                                                        |
| type                 | value          | PN, DS, CR, CP, SR, LR, C, W, A, or D |

<span id="_Ref139552463" class="anchor"></span>Table 30: VPR GET PATIENT DATA—Clinical Procedure/Medicine Reports: “documents” Type Elements Returned

<span id="LOINC_codes" class="anchor"></span>LOINC codes currently in use with VLER:

- 11488-4 Consultation Note
- 18726-0 Radiology Studies
- 18842-5 Discharge Summarization Note
- 26441-6 Cardiology Studies
- 27895-2 Gastroenterology Endoscopy Studies
- 27896-0 Pulmonary Studies
- 27897-8 Neuromuscular Electrophysiology Studies
- 27898-6 Pathology Studies
- 28570-0 Procedure Note (unspecified)
- 28619-5 Ophthalmology Studies
- 28634-4 Miscellaneous Studies
- 29752-3 Perioperative Records
- 34117-2 History & Physical Note

Because there was no direct link in VistA between the TIU titles and LOINC codes when this RPC was created, the above list of codes was manually mapped to existing TIU search capabilities. The “loinc” attribute is only returned when a group of documents is requested using the loinc filter and are the same value passed into the extract.

### Clinical Procedure/Medicine Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the CP category to return all Clinical Procedure reports. Those stored in TIU return the data elements listed in <u>Table 29</u>. Older Medicine package reports are *not* stored in TIU and return only the elements shown in <u>Table 30</u>.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “documents”.

FILTER(“category”): (required) “CP”.START: (optional) VA FileMan date to filter on “referenceDateTime”.

STOP: (optional) VA FileMan date to filter on “referenceDateTime”.

MAX: (optional) Number of most recent documents to return.

ID: (optional) Medicine Package (files \#69\*.\*) variable pointer.

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements             | Attributes     | Content                                       |
|----------------------|----------------|-----------------------------------------------|
| category             | value          | CP                                        |
| clinician \[m\]      | code           | NEW PERSON (#200) ien                         |
|                      | name           | NEW PERSON (#200) Name                        |
|                      | role           | A, S, or C                        |
|                      | officePhone    | NEW PERSON (#200) Office Phone                |
|                      | analogPager    | NEW PERSON (#200) Voice Pager                 |
|                      | fax            | NEW PERSON (#200) Fax Number                  |
|                      | email          | NEW PERSON (#200) Email Address               |
|                      | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code               |
|                      | providerType   | PERSON CLASS (#8932.1) Provider Type          |
|                      | classification | PERSON CLASS (#8932.1) Classification         |
|                      | specialization | PERSON CLASS (#8932.1) Area of Specialization |
|                      | service        | NEW PERSON (#200) Service/Section             |
| content              |                | word-processing text                          |
| documentClass        | value          | CLINICAL PROCEDURES                       |
| facility             | code           | INSTITUTION (#4) Station Number               |
|                      | name           | INSTITUTION (#4) Name                         |
| id                   | value          | Medicine package (#69\*.\*) variable pointer  |
| localTitle           | value          | PROCEDURE/SUBSPECIALTY (#697.2) Name          |
| loinc                | value          | LOINC code                                    |
| nationalTitle        | code           | 4696566                                   |
|                      | name           | PROCEDURE REPORT                          |
| nationalTitleService | code           | 4696471                                   |
|                      | name           | PROCEDURE                                 |
| nationalTitleType    | code           | 4696123                                   |
|                      | name           | REPORT                                    |
| referenceDateTime    | value          | VA FileMan date.time                      |
| status               | value          | string                                        |

<span id="_Ref139552561" class="anchor"></span>Table 31: VPR GET PATIENT DATA—Laboratory Reports: “documents” Type Elements Returned

### Laboratory Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the LR category to return all Laboratory reports. Those stored in TIU return the data elements listed in <u>Table 29</u>. Other Lab package reports *not* stored in TIU return only the elements shown in <u>Table 31</u>.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “documents”.

FILTER(“category”): (required) “LR”.START: (optional) VA FileMan date to filter on “referenceDateTime”.

STOP: (optional) VA FileMan date to filter on “referenceDateTime”.

MAX: (optional) Number of most recent documents to return.

ID: (optional) LAB DATA (#63) subfile identifier string (subscript\_“;”\_inverse collection date.time).

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements             | Attributes     | Content                                                     |
|----------------------|----------------|-------------------------------------------------------------|
| clinician \[m\]      | code           | NEW PERSON (#200) ien                                       |
|                      | name           | NEW PERSON (#200) Name                                      |
|                      | role           | A, S, or C                                      |
|                      | officePhone    | NEW PERSON (#200) Office Phone                              |
|                      | analogPager    | NEW PERSON (#200) Voice Pager                               |
|                      | fax            | NEW PERSON (#200) Fax Number                                |
|                      | email          | NEW PERSON (#200) Email Address                             |
|                      | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                             |
|                      | providerType   | PERSON CLASS (#8932.1) Provider Type                        |
|                      | classification | PERSON CLASS (#8932.1) Classification                       |
|                      | specialization | PERSON CLASS (#8932.1) Area of Specialization               |
|                      | service        | NEW PERSON (#200) Service/Section                           |
| content              |                | word-processing text                                        |
| documentClass        | value          | LR LABORATORY REPORTS                                   |
| encounter            | value          | VISIT (#9000010) ien                                        |
| facility             | code           | INSTITUTION (#4) Station Number                             |
|                      | name           | INSTITUTION (#4) Name                                       |
| id                   | value          | LAB DATA (#63) subscript\_”;”\_inverse collection date.time |
| localTitle           | value          | LR \<section\> REPORT                                       |
| loinc                | value          | LOINC code                                                  |
| nationalTitle        | code           | 4697105                                                 |
|                      | name           | LABORATORY NOTE                                         |
| nationalTitleSubject | code           | 4697104                                                 |
|                      | name           | LABORATORY                                              |
| nationalTitleType    | code           | 4696120                                                 |
|                      | name           | NOTE                                                    |
| referenceDateTime    | value          | VA FileMan date.time                                    |
| status               | value          | string                                                      |
| type                 | value          | LR                                                      |

<span id="_Ref139552682" class="anchor"></span>Table 32: VPR GET PATIENT DATA—Radiology Reports: “documents” Type Elements Returned

### Radiology Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the RA category to return all Radiology reports. These are *not* stored in TIU and return only the elements shown in <u>Table 32</u>.

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “documents”.

FILTER(“category”): (required) “RA”.START: (optional) VA FileMan date to filter on “referenceDateTime”.

STOP: (optional) VA FileMan date to filter on “referenceDateTime”.

MAX: (optional) Number of most recent documents to return.

ID: (optional) RAD NUC/MED PATIENT (#70) exam identifier string (inverse exam date.time\_“-“\_case ien).

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

| Elements             | Attributes     | Content                                                         |
|----------------------|----------------|-----------------------------------------------------------------|
| category             | value          | RA                                                          |
| clinician \[m\]      | code           | NEW PERSON (#200) ien                                           |
|                      | name           | NEW PERSON (#200) Name                                          |
|                      | role           | A, S, or C                                          |
|                      | officePhone    | NEW PERSON (#200) Office Phone                                  |
|                      | analogPager    | NEW PERSON (#200) Voice Pager                                   |
|                      | fax            | NEW PERSON (#200) Fax Number                                    |
|                      | email          | NEW PERSON (#200) Email Address                                 |
|                      | taxonomyCode   | PERSON CLASS (#8932.1) X12 Code                                 |
|                      | providerType   | PERSON CLASS (#8932.1) Provider Type                            |
|                      | classification | PERSON CLASS (#8932.1) Classification                           |
|                      | specialization | PERSON CLASS (#8932.1) Area of Specialization                   |
|                      | service        | NEW PERSON (#200) Service/Section                               |
| content              |                | word-processing text                                            |
| encounter            | value          | VISIT (#9000010) ien                                            |
| facility             | code           | INSTITUTION (#4) Station Number                                 |
|                      | name           | INSTITUTION (#4) Name                                           |
| id                   | value          | RAD NUC/MED PATIENT (#70) inverse exam date.time\_“-“\_case ien |
| localTitle           | value          | RAD NUC/MED PROCEDURE (#71) Name                                |
| loinc                | value          | LOINC code                                                      |
| nationalTitle        | code           | 4695068                                                     |
|                      | name           | RADIOLOGY REPORT                                            |
| nationalTitleSubject | code           | 4693357                                                     |
|                      | name           | RADIOLOGY                                                   |
| nationalTitleType    | code           | 4696123                                                     |
|                      | name           | REPORT                                                      |
| referenceDateTime    | value          | VA FileMan date.time                                        |
| status               | value          | string                                                          |

<span id="_Toc155864416" class="anchor"></span>Table 33: VPR GET PATIENT DATA—Visits/PCE (PX): “visits” Type Elements Returned

## Visits/PCE (PX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “visits”.

START: (optional) VA FileMan date to filter on “dateTime”.

STOP: (optional) VA FileMan date to filter on “dateTime”.

MAX: (optional) Number of most recent visits to return.

ID: (optional) VISIT (#9000010) file IEN.

FILTER(“text”): (optional) 1 or 0, to include “content” text of report.

Output

<table>
<caption><p><span id="_Toc155864417" class="anchor"></span>Table 34: VPR GET PATIENT DATA—Vital Measurements (GMV): “vitals” Type Elements Returned</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 24%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>Elements</th>
<th>Attributes</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>cpt <strong>*</strong></td>
<td>code</td>
<td>CPT Code</td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td>CPT Short Name</td>
</tr>
<tr class="odd">
<td>creditStopCode</td>
<td>code</td>
<td>CLINIC STOP (#40.7) AMIS StopCode</td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td>CLINIC STOP (#40.7) Name</td>
</tr>
<tr class="odd">
<td>dateTime</td>
<td>value</td>
<td>VA FileMan <strong>date.time</strong></td>
</tr>
<tr class="even">
<td>document <strong>*</strong></td>
<td>id</td>
<td>TIU DOCUMENT (#8925) ien</td>
</tr>
<tr class="odd">
<td></td>
<td>localTitle</td>
<td>TIU DOCUMENT DEFINITION (#8925.1) Name</td>
</tr>
<tr class="even">
<td></td>
<td>nationalTitle</td>
<td>TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)</td>
</tr>
<tr class="odd">
<td></td>
<td>vuid</td>
<td>VUID number</td>
</tr>
<tr class="even">
<td></td>
<td>content</td>
<td>word-processing text</td>
</tr>
<tr class="odd">
<td>facility</td>
<td>code</td>
<td>INSTITUTION (#4) Station Number</td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td>INSTITUTION (#4) Name</td>
</tr>
<tr class="odd">
<td>icd <strong>*</strong></td>
<td>code</td>
<td>ICD Code</td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td>ICD Description</td>
</tr>
<tr class="odd">
<td></td>
<td>system</td>
<td>ICD or 10D</td>
</tr>
<tr class="even">
<td></td>
<td>narrative</td>
<td>V POV (#9000010.07) Provider Narrative</td>
</tr>
<tr class="odd">
<td></td>
<td>ranking</td>
<td><strong>P</strong> or <strong>S</strong></td>
</tr>
<tr class="even">
<td>id</td>
<td>value</td>
<td>VISIT (#9000010) ien</td>
</tr>
<tr class="odd">
<td>location</td>
<td>value</td>
<td>HOSPITAL LOCATION (#44) Name</td>
</tr>
<tr class="even">
<td>patientClass</td>
<td>value</td>
<td><strong>AMB</strong>, <strong>IMP</strong>, or <strong>EMER</strong></td>
</tr>
<tr class="odd">
<td>provider <strong>*</strong></td>
<td>code</td>
<td>NEW PERSON (#200) ien</td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td>NEW PERSON (#200) Name</td>
</tr>
<tr class="odd">
<td></td>
<td>role</td>
<td><strong>P</strong>, <strong>S</strong>, or <strong>A</strong></td>
</tr>
<tr class="even">
<td></td>
<td>primary</td>
<td>boolean (<strong>1</strong> or <strong>0</strong>)</td>
</tr>
<tr class="odd">
<td></td>
<td>officePhone</td>
<td>NEW PERSON (#200) Office Phone</td>
</tr>
<tr class="even">
<td></td>
<td>analogPager</td>
<td>NEW PERSON (#200) Voice Pager</td>
</tr>
<tr class="odd">
<td></td>
<td>fax</td>
<td>NEW PERSON (#200) Fax Number</td>
</tr>
<tr class="even">
<td></td>
<td>email</td>
<td>NEW PERSON (#200) Email Address</td>
</tr>
<tr class="odd">
<td></td>
<td>taxonomyCode</td>
<td>PERSON CLASS (#8932.1) X12 Code</td>
</tr>
<tr class="even">
<td></td>
<td>providerType</td>
<td>PERSON CLASS (#8932.1) Provider Type</td>
</tr>
<tr class="odd">
<td></td>
<td>classification</td>
<td>PERSON CLASS (#8932.1) Classification</td>
</tr>
<tr class="even">
<td></td>
<td>specialization</td>
<td>PERSON CLASS (#8932.1) Area of Specialization</td>
</tr>
<tr class="odd">
<td></td>
<td>service</td>
<td>NEW PERSON (#200) Service/Section</td>
</tr>
<tr class="even">
<td>reason</td>
<td>code</td>
<td>ICD Code</td>
</tr>
<tr class="odd">
<td></td>
<td>name</td>
<td>ICD Description</td>
</tr>
<tr class="even">
<td></td>
<td>system</td>
<td>ICD or 10D</td>
</tr>
<tr class="odd">
<td></td>
<td>narrative</td>
<td>V POV (#9000010.07) Provider Narrative</td>
</tr>
<tr class="even">
<td>service</td>
<td>value</td>
<td><strong>MEDICINE</strong>, <strong>SURGERY</strong>, <strong>PSYCHIATRY</strong>, <strong>NHCU</strong>, <strong>NEUROLOGY</strong>, <strong>INTERMEDIATE MED</strong>, <strong>REHAB MEDICINE</strong>, <strong>SPINAL CORD INJURY</strong>, <strong>DOMICILIARY</strong>, <strong>BLIND REHAB</strong>, or <strong>RESPITE CARE</strong></td>
</tr>
<tr class="odd">
<td>serviceCategory</td>
<td>code</td>
<td><strong>A</strong>, <strong>H</strong>, <strong>I</strong>, <strong>C</strong>, <strong>N</strong>, <strong>T</strong>, <strong>S</strong>, <strong>O</strong>, <strong>E</strong>, <strong>R</strong>, <strong>D</strong>, or <strong>X</strong></td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td><p><strong>AMBULATORY</strong>, <strong>HOSPITALIZATION</strong>, <strong>IN HOSPITAL</strong>, <strong>CHART REVIEW</strong>, <strong>NOT FOUND</strong>,</p>
<p><strong>TELECOMMUNICATIONS</strong>, <strong>DAY SURGERY</strong>, <strong>OBSERVATION</strong>, <strong>EVENT (HISTORICAL)</strong>, <strong>NURSING HOME</strong>, <strong>DAILY HOSPITALIZATION DATA</strong>, <strong>ANCILLARY PACKAGE DAILY DATA</strong></p></td>
</tr>
<tr class="odd">
<td>stopCode</td>
<td>code</td>
<td>CLINIC STOP (#40.7) AMIS StopCode</td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td>CLINIC STOP (#40.7) Name</td>
</tr>
<tr class="odd">
<td>type</td>
<td>code</td>
<td>CPT Code</td>
</tr>
<tr class="even">
<td></td>
<td>name</td>
<td>CPT Short Name</td>
</tr>
<tr class="odd">
<td>visitString</td>
<td>value</td>
<td>HOSPITAL LOCATION (#44) ien;dateTime; serviceCategory code</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Included with admissions:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>admission</td>
<td></td>
<td>PATIENT MOVEMENT (#405) ien</td>
</tr>
<tr class="odd">
<td>arrivalDateTime</td>
<td></td>
<td>VA FileMan <strong>date.time</strong></td>
</tr>
<tr class="even">
<td>departureDateTime</td>
<td></td>
<td>VA FileMan <strong>date.time</strong></td>
</tr>
<tr class="odd">
<td>ptf</td>
<td></td>
<td>PTF (#45) ien</td>
</tr>
<tr class="even">
<td>roomBed</td>
<td></td>
<td>string</td>
</tr>
<tr class="odd">
<td>specialty</td>
<td></td>
<td>FACILITY TREATING SPECIALTY (#45.7) Name</td>
</tr>
</tbody>
</table>

<span id="_Toc155864417" class="anchor"></span>Table 34: VPR GET PATIENT DATA—Vital Measurements (GMV): “vitals” Type Elements Returned

\* = Can be multiple.

## Vital Measurements (GMV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Parameters

DFN: (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

TYPE: (required) “vitals”.

START: (optional) VA FileMan date to filter on “taken”.

STOP: (optional) VA FileMan date to filter on “taken”.

MAX: (optional) Number of measurement sets to return (by “taken”).

ID: (optional) GMRV VITAL MEASUREMENT (#120.5) file IEN, or VA FileMan date.time to match “taken” and return the set.

FILTER: (optional) None.

Output

| Elements           | Attributes       |      | Content                                                                   |
|--------------------|------------------|------|---------------------------------------------------------------------------|
| entered            | value            |      | VA FileMan date.time                                                  |
| facility           | code             |      | INSTITUTION (#4) Station Number                                           |
|                    | name             |      | INSTITUTION (#4) Name                                                     |
| location           | code             |      | HOSPITAL LOCATION (#44) ien                                               |
|                    | name             |      | HOSPITAL LOCATION (#44) Name                                              |
| measurement \* | id               |      | GMRV VITAL MEASUREMENT (#120.5) ien                                       |
|                    | vuid             |      | VUID number                                                               |
|                    | name             |      | GMRV VITAL TYPE (#120.51) Name                                            |
|                    | value            |      | string                                                                    |
|                    | units            |      | string                                                                    |
|                    | metricValue      |      | number                                                                    |
|                    | metricUnits      |      | C, cm, or kg                                                  |
|                    | high             |      | number                                                                    |
|                    | low              |      | number                                                                    |
|                    | bmi              |      | number                                                                    |
|                    | qualifier \* | name | GMRV VITAL QUALIFIER (#120.52) Qualifier                                  |
|                    |                  | vuid | GMRV VITAL QUALIFIER (#120.52) VUID                                       |
| removed \*     | value            |      | INCORRECT DATE/TIME, INCORRECT READING, INCORRECT PATIENT, INVALID RECORD |
| taken              | value            |      | VA FileMan date.time                                                  |

<span id="_Toc155864418" class="anchor"></span>Table 35: VPR GET PATIENT DATA JSON—Allergy/Adverse Reaction Tracking (GMRA): “allergy” Domain Elements Returned

\* = Can be multiple.

# JSON Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes tables that list the data elements returned by the VPR GET PATIENT DATA JSON RPC. All searches are performed reverse-chronologically to return the most recent data, unless otherwise noted.

This RPC accepts only one input parameter, which is an array passed by reference as a list of name-value pairs \[i.e., FILTER(“name”)=value\]. All input filters are optional to refine the extract, except for domain and patientId.

The <span id="patientId" class="anchor"></span>patientId is the internal entry number (IEN) from the PATIENT (#2) file, or alternatively, the Integration Control Number (ICN) for remote calls. Its value can be provided in any of the following formats:

- IEN
- IEN;ICN
- ;ICN

![](virtual-patient-record-vpr-developer-s-guide/022.png) NOTE: For the PATIENT (#2) file, the IEN is the equivalent of the Data File Number (DFN).

## Allergy/Adverse Reaction Tracking (GMRA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](\l): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “allergy”.

start: (optional) VA FileMan date to filter on “entered”.

stop: (optional) VA FileMan date to filter on “entered”.

max: (optional) Use *not recommended*, as reactions are *not* sorted.

id: (optional) PATIENT ALLERGIES (#120.8) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements         | Attributes |
|------------------|------------|
| entered          |            |
| facilityCode     |            |
| facilityName     |            |
| historical       |            |
| kind             |            |
| localId          |            |
| products         | name       |
|                  | vuid       |
| reactions \* | name       |
|                  | vuid       |
| reference        |            |
| removed          |            |
| summary          |            |
| uid              |            |
| verified         |            |

<span id="_Ref155790827" class="anchor"></span>Table 36: VPR GET PATIENT DATA JSON—Clinical Observations (MDC): “obs” Domain Elements Returned

\* = Can be multiple.

## Clinical Observations (MDC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “obs”.

start: (optional) VA FileMan date to filter on “observed”.

stop: (optional) VA FileMan date to filter on “observed”.

max: (optional) Use with caution, as search is performed chronologically.

id: (optional) OBS (#704.117) file ID (#.01) value.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements           | Attributes |
|--------------------|------------|
| bodySiteCode       |            |
| bodySiteName       |            |
| comment            |            |
| entered            |            |
| facilityCode       |            |
| facilityName       |            |
| interpretationCode |            |
| interpretationName |            |
| localId            |            |
| locationName       |            |
| locationUid        |            |
| methodCode         |            |
| methodName         |            |
| observed           |            |
| qualifiers \*  | code       |
|                    | name       |
|                    | type       |
| result             |            |
| setID              |            |
| setName            |            |
| setStart           |            |
| setStop            |            |
| setType            |            |
| statusCode         |            |
| statusName         |            |
| typeCode           |            |
| typeName           |            |
| typeVuid           |            |
| uid                |            |
| units              |            |

<span id="_Ref139550685" class="anchor"></span>Table 37: VPR GET PATIENT DATA JSON—Clinical Procedures (MDC): “procedure” Domain Elements Returned

\* = Can be multiple.

## Clinical Procedures (MDC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “procedure”.

start: (optional) VA FileMan date to filter on “dateTime”.

stop: (optional) VA FileMan date to filter on “dateTime”.

max: (optional) Number of most recent procedures to return.

id: (optional) Variable pointer to CP data file/item.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements       | Attributes    |
|----------------|---------------|
| category       |               |
| consultUid     |               |
| dateTime       |               |
| encounterUid   |               |
| facilityCode   |               |
| facilityName   |               |
| hasImages      |               |
| interpretation |               |
| kind           |               |
| localId        |               |
| locationName   |               |
| locationUid    |               |
| name           |               |
| orderUid       |               |
| providers      | providerName  |
|                | providerUid   |
| requested      |               |
| results \* | localTitle    |
|                | nationalTitle |
|                | uid           |
| statusName     |               |
| uid            |               |

<span id="_Toc155864421" class="anchor"></span>Table 38: VPR GET PATIENT DATA JSON—Consult/Request Tracking (GMRC): “consult” Domain Elements Returned

\* = Can be multiple.

## Consult/Request Tracking (GMRC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “consult”.

start: (optional) VA FileMan date to filter on “dateTime”.

stop: (optional) VA FileMan date to filter on “dateTime”.

max: (optional) Number of most recent consult requests to return.

id: (optional) REQUEST/CONSULTATION (#123) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

nowrap: (optional) 1 or 0, to include breaks between lines in reason.

Output

| Elements         | Attributes    |
|------------------|---------------|
| category         |               |
| consultProcedure |               |
| dateTime         |               |
| facilityCode     |               |
| facilityName     |               |
| interpretation   |               |
| localId          |               |
| orderName        |               |
| orderUid         |               |
| providerName     |               |
| providerUid      |               |
| provisionalDx    | code          |
|                  | name          |
|                  | system        |
| reason           |               |
| results \*   | localTitle    |
|                  | nationalTitle |
|                  | uid           |
| service          |               |
| statusName       |               |
| typeName         |               |
| uid              |               |
| urgency          |               |

<span id="_Ref139550688" class="anchor"></span>Table 39: VPR GET PATIENT DATA JSON—Laboratory (LR): “lab” Domain Elements Returned

\* = Can be multiple.

## Laboratory (LR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “lab”.

start: (optional) VA FileMan date to filter on “observed”.

stop: (optional) VA FileMan date to filter on “observed”.

max: (optional) Number of most recent accessions to return.

id: (optional) LAB DATA (#63) file IEN string.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

category: (optional) CH, MI, or AP. Default = all.

nowrap: (optional) 1 or 0, to include breaks between comment lines.

Output

| Elements           | Attributes    | Content  |
|--------------------|---------------|----------|
| bactRemarks        |               |          |
| categoryCode       |               |          |
| categoryName       |               |          |
| comment            |               |          |
| displayName        |               |          |
| displayOrder       |               |          |
| facilityCode       |               |          |
| facilityName       |               |          |
| gramStain \*   | result        |          |
| groupName          |               |          |
| groupUid           |               |          |
| high               |               |          |
| interpretationCode |               |          |
| interpretationName |               |          |
| labOrderId         |               |          |
| localId            |               |          |
| low                |               |          |
| observed           |               |          |
| orderUid           |               |          |
| organisms \*   | drugs         | interp   |
|                    |               | name     |
|                    |               | restrict |
|                    |               | result   |
|                    | name          |          |
|                    | qty           |          |
| organizerType      |               |          |
| result             |               |          |
| resulted           |               |          |
| results \*     | localTitle    |          |
|                    | nationalTitle |          |
|                    | resultUid     |          |
|                    | uid           |          |
| sample             |               |          |
| specimen           |               |          |
| statusCode         |               |          |
| statusName         |               |          |
| typeCode           |               |          |
| typeId             |               |          |
| typeName           |               |          |
| uid                |               |          |
| units              |               |          |
| urineScreen        |               |          |
| vuid               |               |          |

<span id="_Ref139550878" class="anchor"></span>Table 40: VPR GET PATIENT DATA JSON—Orders (OR): “order” Domain Elements Returned

\* = Can be multiple.

## Orders (OR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “order”.

start: (optional) VA FileMan date to filter on date released.

stop: (optional) VA FileMan date to filter on date released.

max: (optional) Number of most recent orders to return.

id: (optional) ORDER (#100) file IEN string.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements          | Attributes     |
|-------------------|----------------|
| adminTimes        |                |
| clinicians \* | name           |
|                   | role           |
|                   | signedDateTime |
|                   | uid            |
| content           |                |
| displayGroup      |                |
| entered           |                |
| facilityCode      |                |
| facilityName      |                |
| instructions      |                |
| localId           |                |
| locationName      |                |
| locationUid       |                |
| name              |                |
| oiCode            |                |
| oiName            |                |
| oiPackageRef      |                |
| orderUid          |                |
| predecessor       |                |
| providerName      |                |
| providerUid       |                |
| results \*    | uid            |
| scheduleName      |                |
| service           |                |
| start             |                |
| statusCode        |                |
| statusName        |                |
| statusVuid        |                |
| stop              |                |
| successor         |                |
| uid               |                |

<span id="_Toc155864424" class="anchor"></span>Table 41: VPR GET PATIENT DATA JSON—CPT Procedures: “cpt” Domain Elements Returned

\* = Can be multiple.

## Patient Care Encounter (PX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPT Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “cpt”.

start: (optional) VA FileMan date to filter on “entered”.

stop: (optional) VA FileMan date to filter on “entered”.

max: (optional) Number of most recent procedures to return.

id: (optional) V CPT (#9000010.18) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements      |
|---------------|
| comment       |
| cptCode       |
| encounterName |
| encounterUid  |
| entered       |
| facilityCode  |
| facilityName  |
| localId       |
| locationName  |
| locationUid   |
| name          |
| quantity      |
| type          |
| uid           |

<span id="_Toc155864425" class="anchor"></span>Table 42: VPR GET PATIENT DATA JSON—Exams: “exam” Domain Elements Returned

### Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “exam”.

start: (optional) VA FileMan date to filter on “entered”.

stop: (optional) VA FileMan date to filter on “entered”.

max: (optional) Number of most recent exams to return.

id: (optional) V EXAM (#9000010.13) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements      |
|---------------|
| comment       |
| encounterName |
| encounterUid  |
| entered       |
| facilityCode  |
| facilityName  |
| localId       |
| locationName  |
| locationUid   |
| name          |
| result        |
| uid           |

<span id="_Toc155864426" class="anchor"></span>Table 43: VPR GET PATIENT DATA JSON—Education Topics: “education” Domain Elements Returned

### Education Topics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “education”.

start: (optional) VA FileMan date to filter on “entered”.

stop: (optional) VA FileMan date to filter on “entered”.

max: (optional) Number of most recent education instances to return.

id: (optional) V PATIENT ED (#9000010.16) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements      |
|---------------|
| comment       |
| encounterName |
| encounterUid  |
| entered       |
| facilityCode  |
| facilityName  |
| localId       |
| locationName  |
| locationUid   |
| name          |
| result        |
| uid           |

<span id="_Toc155864427" class="anchor"></span>Table 44: VPR GET PATIENT DATA JSON—Health Factors: “factor” Domain Elements Returned

### Health Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “factor”.

start: (optional) VA FileMan date to filter on “entered”.

stop: (optional) VA FileMan date to filter on “entered”.

max: Number of most recent factors to return.

id: (optional) V HEALTH FACTORS (#9000010.23) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements      |
|---------------|
| categoryName  |
| categoryUid   |
| comment       |
| display       |
| encounterName |
| encounterUid  |
| entered       |
| facilityCode  |
| facilityName  |
| kind          |
| localId       |
| locationName  |
| locationUid   |
| name          |
| severityName  |
| severityUid   |
| summary       |
| uid           |

<span id="_Toc155864428" class="anchor"></span>Table 45: VPR GET PATIENT DATA JSON—Immunizations: “immunization” Domain Elements Returned

### Immunizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “immunization”.

start: (optional) VA FileMan date to filter on “administeredDateTime”.

stop: (optional) VA FileMan date to filter on “administeredDateTime”.

max: (optional) Number of most recent immunizations to return.

id: (optional) V IMMUNIZATION (#9000010.11) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements             |
|----------------------|
| administeredDateTime |
| comment              |
| contraindicated      |
| cptCode              |
| cptName              |
| encounterName        |
| encounterUid         |
| facilityCode         |
| facilityName         |
| localId              |
| locationName         |
| locationUid          |
| name                 |
| performerName        |
| performerUid         |
| reactionCode         |
| reactionName         |
| seriesCode           |
| seriesName           |
| summary              |
| uid                  |

<span id="_Toc155864429" class="anchor"></span>Table 46: VPR GET PATIENT DATA JSON—Purpose of Visit: “pov” Domain Elements Returned

### Purpose of Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “pov”.

start: (optional) VA FileMan date to filter on “entered”.

stop: (optional) VA FileMan date to filter on “entered”.

max: (optional) Number of most recent reasons to return.

id: (optional) V POV (#9000010.07) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements      |
|---------------|
| comment       |
| encounterName |
| encounterUid  |
| entered       |
| facilityCode  |
| facilityName  |
| icdCode       |
| localId       |
| locationName  |
| locationUid   |
| name          |
| type          |
| uid           |

<span id="_Toc155864430" class="anchor"></span>Table 47: VPR GET PATIENT DATA JSON—Skin Tests: “skin” Domain Elements Returned

### Skin Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “skin”.

start: (optional) VA FileMan date to filter on “entered”.

stop: (optional) VA FileMan date to filter on “entered”.

max: (optional) Number of most recent exams to return.

id: (optional) V SKIN TEST (#9000010.12) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements      |
|---------------|
| comment       |
| dateRead      |
| encounterName |
| encounterUid  |
| entered       |
| facilityCode  |
| facilityName  |
| localId       |
| locationName  |
| locationUid   |
| name          |
| reading       |
| result        |
| uid           |

<span id="_Toc155864431" class="anchor"></span>Table 48: VPR GET PATIENT DATA JSON—Medications: “med” Domain Elements Returned

## Pharmacy (PS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “med”.

start: (optional) VA FileMan date to filter on date released.

stop: (optional) VA FileMan date to filter on date released.

max: (optional) Number of most recent med orders to return.

id: (optional) ORDER (#100) file IEN.

vaType: (optional) I, O, or N.

Output

| Elements               | Attributes          |
|------------------------|---------------------|
| administrations \* | dateTime            |
|                        | status              |
| comment                |                     |
| dosages \*         | adminTimes          |
|                        | complexConjunction  |
|                        | complexDuration     |
|                        | dose                |
|                        | relatedOrder        |
|                        | relativeStart       |
|                        | relativeStop        |
|                        | routeName           |
|                        | scheduleFreq        |
|                        | scheduleName        |
|                        | scheduleType        |
|                        | start               |
|                        | stop                |
|                        | units               |
| facilityCode           |                     |
| facilityName           |                     |
| fills \*           | daysSupplyDispensed |
|                        | dispenseDate        |
|                        | partial             |
|                        | releaseDate         |
|                        | routing             |
|                        | quantityDispensed   |
| IMO                    |                     |
| lastFilled             |                     |
| localId                |                     |
| medStatus              |                     |
| medStatusName          |                     |
| medType                |                     |
| name                   |                     |
| orders                 | daysSupply          |
|                        | fillCost            |
|                        | fillsAllowed        |
|                        | fillsRemaining      |
|                        | locationName        |
|                        | locationUid         |
|                        | ordered             |
|                        | orderUid            |
|                        | pharmacistName      |
|                        | pharmacistUid       |
|                        | predecessor         |
|                        | prescriptionId      |
|                        | providerName        |
|                        | providerUid         |
|                        | quantityOrdered     |
|                        | successor           |
|                        | vaRouting           |
| overallStart           |                     |
| overallStop            |                     |
| parent                 |                     |
| patientInstruction     |                     |
| productFormName        |                     |
| products \*        | drugClassCode       |
|                        | drugClassName       |
|                        | ingredientCode      |
|                        | ingredientCodeName  |
|                        | ingredientName      |
|                        | ingredientRole      |
|                        | relatedOrder        |
|                        | strength            |
|                        | suppliedCode        |
|                        | suppliedName        |
| qualifiedName          |                     |
| sig                    |                     |
| stopped                |                     |
| supply                 |                     |
| type                   |                     |
| uid                    |                     |
| vaStatus               |                     |
| vaType                 |                     |

<span id="_Ref139550865" class="anchor"></span>Table 49: VPR GET PATIENT DATA JSON—Infusions: “med” Domain Elements Returned

\* = Can be multiple.

### Infusions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “med”.

start: (optional) VA FileMan date to filter on date released.

stop: (optional) VA FileMan date to filter on date released.

max: (optional) Number of most recent med orders to return.

id: (optional) ORDER (#100) file IEN.

vaType: (optional) “V”.

Output

| Elements               | Attributes         |
|------------------------|--------------------|
| administrations \* | dateTime           |
|                        | status             |
| comment                |                    |
| dosages                | adminTimes         |
|                        | duration           |
|                        | ivRate             |
|                        | restriction        |
|                        | routeName          |
|                        | scheduleFreq       |
|                        | scheduleName       |
|                        | scheduleType       |
| facilityCode           |                    |
| facilityName           |                    |
| IMO                    |                    |
| localId                |                    |
| medStatus              |                    |
| medStatusName          |                    |
| medType                |                    |
| name                   |                    |
| orders                 | locationName       |
|                        | locationUid        |
|                        | ordered            |
|                        | orderUid           |
|                        | pharmacistName     |
|                        | pharmacistUid      |
|                        | predecessor        |
|                        | providerName       |
|                        | providerUid        |
|                        | successor          |
| overallStart           |                    |
| overallStop            |                    |
| parent                 |                    |
| products \*        | drugClassCode      |
|                        | drugClassName      |
|                        | ingredientCode     |
|                        | ingredientCodeName |
|                        | ingredientName     |
|                        | ingredientRole     |
|                        | relatedOrder       |
|                        | strength           |
|                        | suppliedCode       |
|                        | suppliedName       |
|                        | volume             |
| qualifiedName          |                    |
| stopped                |                    |
| type                   |                    |
| uid                    |                    |
| vaStatus               |                    |
| vaType                 |                    |

<span id="_Ref139550851" class="anchor"></span>Table 50: VPR GET PATIENT DATA JSON—Problem List (GMPL): “problem” Domain Elements Returned

\* = Can be multiple.

## Problem List (GMPL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “problem”.

start: (optional) None.

stop: (optional) None.

max: (optional) Use *not recommended*, as problems are *not* sorted.

id: (optional) PROBLEM (#9000011) file IEN.

status: (optional) A or I. Default = A (all).

Output

| Elements         | Attributes    |
|------------------|---------------|
| acuityCode       |               |
| acuityName       |               |
| comments \*  | comment       |
|                  | entered       |
|                  | enteredByCode |
|                  | enteredByName |
| entered          |               |
| facilityCode     |               |
| facilityName     |               |
| icdCode          |               |
| icdName          |               |
| localId          |               |
| locationName     |               |
| locationUid      |               |
| onset            |               |
| problemText      |               |
| providerName     |               |
| providerUid      |               |
| removed          |               |
| resolved         |               |
| service          |               |
| serviceConnected |               |
| statusCode       |               |
| statusName       |               |
| uid              |               |
| unverified       |               |
| updated          |               |

<span id="_Toc155864434" class="anchor"></span>Table 51: VPR GET PATIENT DATA JSON—PTF (DG): “ptf” Domain Elements Returned

\* = Can be multiple.

## PTF (DG)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “ptf”.

start: (optional) VA FileMan date to filter on movement date.

stop: (optional) VA FileMan date to filter on movement date.

max: (optional) Number of most recent treatment codes to return.

id: (optional) PTF (#45) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements          |
|-------------------|
| arrivalDateTime   |
| dischargeDateTime |
| encounterName     |
| encounterUid      |
| facilityCode      |
| facilityName      |
| icdCode           |
| icdName           |
| localId           |
| principalDx       |
| uid               |

<span id="_Toc155864435" class="anchor"></span>Table 52: VPR GET PATIENT DATA JSON—Radiology/Nuclear Medicine (RA): “image” Domain Elements Returned

## Radiology/Nuclear Medicine (RA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “image”.

start: (optional) VA FileMan date to filter on “dateTime”.

stop: (optional) VA FileMan date to filter on “dateTime”.

max: (optional) Number of most recent exams to return.

id: (optional) EXAMINATIONS (#70.03) subfile IEN string.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements         | Attributes   |
|------------------|--------------|
| case             |              |
| category         |              |
| dateTime         |              |
| diagnosis \* | code         |
|                  | lexicon      |
|                  | primary      |
| encounterName    |              |
| encounterUid     |              |
| facilityCode     |              |
| facilityName     |              |
| hasImages        |              |
| imageLocation    |              |
| imagingTypeUid   |              |
| interpretation   |              |
| kind             |              |
| localId          |              |
| locationName     |              |
| locationUid      |              |
| name             |              |
| orderName        |              |
| orderUid         |              |
| providers        | providerName |
|                  | providerUid  |
| results          | localTitle   |
|                  | uid          |
| statusName       |              |
| summary          |              |
| typeName         |              |
| uid              |              |
| verified         |              |

<span id="_Toc155864436" class="anchor"></span>Table 53: VPR GET PATIENT DATA JSON—Registration (DPT): “patient” Domain Elements Returned

\* = Can be multiple.

## Registration (DPT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “patient”.

start: (optional) None.

stop: (optional) None.

max: (optional) None.

id: (optional) PATIENT (#2) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

nowrap: (optional) 1 or 0, to include breaks between lines of flag text.

Output

| Elements             | Attributes               | Content       |
|----------------------|--------------------------|---------------|
| addresses \*     | city                     |               |
|                      | postalCode               |               |
|                      | stateProvince            |               |
|                      | streetLine1              |               |
|                      | streetLine2              |               |
| aliases              | familyName               |               |
|                      | fullName                 |               |
|                      | givenNames               |               |
| briefId              |                          |               |
| dateOfBirth          |                          |               |
| died                 |                          |               |
| disability \*    | disPercent               |               |
|                      | name                     |               |
|                      | sc                       |               |
|                      | vaCode                   |               |
| eligibility \*   | name                     |               |
|                      | primary                  |               |
| eligibilityStatus    |                          |               |
| ethnicities \*   | ethnicity                |               |
| exposures \*     | name                     |               |
|                      | uid                      |               |
| facilities \*    | code                     |               |
|                      | homeSite                 |               |
|                      | latestDate               |               |
|                      | localPatientId           |               |
|                      | name                     |               |
|                      | systemId                 |               |
| familyName           |                          |               |
| flags \*         | name                     |               |
|                      | text                     |               |
| fullName             |                          |               |
| genderCode           |                          |               |
| genderName           |                          |               |
| givenNames           |                          |               |
| icn                  |                          |               |
| inpatient            |                          |               |
| languageCode         |                          |               |
| languageName         |                          |               |
| localId              |                          |               |
| maritalStatuses      | code                     |               |
|                      | name                     |               |
| meansTest            |                          |               |
| pcProviderName       |                          |               |
| pcProviderUid        |                          |               |
| pcTeamMembers \* | name                     |               |
|                      | position                 |               |
|                      | uid                      |               |
| pcTeamName           |                          |               |
| pcTeamUid            |                          |               |
| races \*         | race                     |               |
| religionCode         |                          |               |
| religionName         |                          |               |
| sensitive            |                          |               |
| servicePeriod        |                          |               |
| ssn                  |                          |               |
| supports \*      | addresses \*         | city          |
|                      |                          | postalCode    |
|                      |                          | stateProvince |
|                      |                          | streetLine1   |
|                      |                          | streetLine2   |
|                      | contactTypeCode          |               |
|                      | contactTypeName          |               |
|                      | name                     |               |
|                      | relationship             |               |
|                      | telecomList \*       | telecom       |
|                      |                          | usageCode     |
|                      |                          | usageName     |
| telecoms \*      | telecom                  |               |
|                      | usageCode                |               |
|                      | usageName                |               |
| uid                  |                          |               |
| veteran              | isVet                    |               |
|                      | lrdfn                    |               |
|                      | serviceConnected         |               |
|                      | serviceConnectionPercent |               |

<span id="_Toc155864437" class="anchor"></span>Table 54: VPR GET PATIENT DATA JSON—Scheduling (SDAM): “appointment” Domain Elements Returned

\* = Can be multiple.

## Scheduling (SDAM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling API sorts appointments by dateTime chronologically; while past appointments are available, the default view is to extract a patient’s future appointments.

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “appointment”.

start: (optional) VA FileMan date to filter on “dateTime”. Default = TODAY.

stop: (optional) VA FileMan date to filter on “dateTime”. Default = all future.

max: (optional) Number of \[future\] appointments to return.

id: (optional) Inverse visit string (“servCatg;date.time;locationIEN”).

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements          | Attributes   |
|-------------------|--------------|
| appointmentStatus |              |
| categoryCode      |              |
| categoryName      |              |
| checkIn           |              |
| checkOut          |              |
| comment           |              |
| dateTime          |              |
| facilityCode      |              |
| facilityName      |              |
| localId           |              |
| locationName      |              |
| locationUid       |              |
| patientClassCode  |              |
| patientClassName  |              |
| providers         | providerName |
|                   | providerUid  |
| reasonName        |              |
| service           |              |
| stopCodeName      |              |
| stopCodeUid       |              |
| summary           |              |
| typeCode          |              |
| typeName          |              |
| uid               |              |

<span id="_Ref139550821" class="anchor"></span>Table 55: VPR GET PATIENT DATA JSON—Surgery (SR): “surgery” Domain Elements Returned

\* = Can be multiple.

## Surgery (SR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “surgery”.

start: (optional) VA FileMan date to filter on “dateTime”.

stop: (optional) VA FileMan date to filter on “dateTime”.

max: (optional) Number of most recent surgical procedures to return.

id: (optional) SURGERY (#130) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements         | Attributes    |
|------------------|---------------|
| category         |               |
| dateTime         |               |
| encounterName    |               |
| encounterUid     |               |
| facilityCode     |               |
| facilityName     |               |
| kind             |               |
| localId          |               |
| providers \* | providerName  |
|                  | providerUid   |
| results \*   | localTitle    |
|                  | nationalTitle |
|                  | uid           |
| statusName       |               |
| summary          |               |
| typeCode         |               |
| typeName         |               |
| uid              |               |

<span id="_Toc155864439" class="anchor"></span>Table 56: VPR GET PATIENT DATA JSON—Text Integration Utilities (TIU): “document” Domain Elements Returned

\* = Can be multiple.

## Text Integration Utilities (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “document”.

start: (optional) VA FileMan date to filter on “referenceDateTime”.

stop: (optional) VA FileMan date to filter on “referenceDateTime”.

max: (optional) Number of most recent documents to return.

id: (optional) TIU DOCUMENTS (#8925) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

category: (optional) PN, CR, C, W, A, D, DS, SR, CP, LR, or RA.status: (optional) “completed”, “unsigned”, or “all” (for current user).

text: (optional) 1 or 0, to include “content” text of document.

Output

| Elements             | Attributes        | Content        |
|----------------------|-------------------|----------------|
| attendingName        |                   |                |
| attendingUid         |                   |                |
| documentClass        |                   |                |
| documentTypeCode     |                   |                |
| documentTypeName     |                   |                |
| encounterName        |                   |                |
| encounterUid         |                   |                |
| entered              |                   |                |
| facilityCode         |                   |                |
| facilityName         |                   |                |
| images               |                   |                |
| localId              |                   |                |
| localTitle           |                   |                |
| nationalTitle        | title             |                |
|                      | vuid              |                |
| nationalTitleRole    | role              |                |
|                      | vuid              |                |
| nationalTitleService | service           |                |
|                      | vuid              |                |
| nationalTitleSetting | setting           |                |
|                      | vuid              |                |
| nationalTitleSubject | subject           |                |
|                      | vuid              |                |
| nationalTitleType    | type              |                |
|                      | vuid              |                |
| parent               |                   |                |
| referenceDateTime    |                   |                |
| statusName           |                   |                |
| subject              |                   |                |
| text \*          | clinicians \* | name           |
|                      |                   | role           |
|                      |                   | signature      |
|                      |                   | signedDateTime |
|                      |                   | uid            |
|                      | content           |                |
|                      | dateTime          |                |
|                      | status            |                |
|                      | uid               |                |
| uid                  |                   |                |
| urgency              |                   |                |

<span id="_Toc155864440" class="anchor"></span>Table 57: VPR GET PATIENT DATA JSON—Visits/PCE (PX): “visit” Domain Elements Returned

\* = Can be multiple.

## Visits/PCE (PX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “visit”.

start: (optional) VA FileMan date to filter on “dateTime”.

stop: (optional) VA FileMan date to filter on “dateTime”.

max: (optional) Number of most recent visits to return.

id: (optional) VISIT (#9000010) file IEN.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements         | Attributes        |
|------------------|-------------------|
| categoryCode     |                   |
| categoryName     |                   |
| checkOut         |                   |
| current          |                   |
| dateTime         |                   |
| documents \* | localTitle        |
|                  | nationalTitle     |
|                  | uid               |
| facilityCode     |                   |
| facilityName     |                   |
| localId          |                   |
| locationName     |                   |
| locationUid      |                   |
| movements \* | dateTime          |
|                  | localId           |
|                  | locationName      |
|                  | locationUid       |
|                  | movementType      |
|                  | providerName      |
|                  | providerUid       |
|                  | specialty         |
| patientClassCode |                   |
| patientClassName |                   |
| providers \* | primary           |
|                  | providerName      |
|                  | providerUid       |
|                  | role              |
| reasonName       |                   |
| reasonUid        |                   |
| roomBed          |                   |
| service          |                   |
| specialty        |                   |
| stay             | arrivalDateTime   |
|                  | dischargeDateTime |
| stopCodeName     |                   |
| stopCodeUid      |                   |
| summary          |                   |
| typeName         |                   |
| uid              |                   |

<span id="_Toc155864441" class="anchor"></span>Table 58: VPR GET PATIENT DATA JSON—Vital Measurements (GMV)” “vital” Domain Elements Returned

\* = Can be multiple.

## Vital Measurements (GMV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Input Filters

[patientId](#patientId): (required) PATIENT (#2) file IEN (optionally: DFN;ICN or ;ICN).

domain: (required) “vital”.

start: (optional) VA FileMan date to filter on “observed”.

stop: (optional) VA FileMan date to filter on “observed”.

max: (optional) Number of measurement sets to return (by “taken”).

id: (optional) GMRV VITAL MEASUREMENT (#120.5) file IEN, or VA FileMan date.time to match “taken” and return the set.

uid: (optional) Universal ID for item (urn:va:domain:SYS:DFN:id).

Output

| Elements          | Attributes |
|-------------------|------------|
| displayName       |            |
| facilityCode      |            |
| facilityName      |            |
| high              |            |
| kind              |            |
| localId           |            |
| locationName      |            |
| locationUid       |            |
| low               |            |
| metricResult      |            |
| metricUnits       |            |
| observed          |            |
| qualifiers \* | name       |
|                   | vuid       |
| removed           |            |
| result            |            |
| resulted          |            |
| summary           |            |
| typeCode          |            |
| typeName          |            |
| uid               |            |
| units             |            |

<span id="_Ref11243059" class="anchor"></span>Table 59: VPR HL7 Event Protocols and Associated Listeners

\* = Can be multiple.

# HealthShare Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch VPR\*1\*8 introduced another method of retrieving VistA data to support the HealthShare (HS) interface engine. This patch exported almost 150 entries in the VA FileMan ENTITY (#1.5) file, to map VistA data elements to the SDA model and use the supported VA FileMan DDE[^1] calls to retrieve the requested data as XML. The names and structure of each VPR entity is intended to comply with the SDA model.

Patch VPR\*1\*8 also installed a mechanism to monitor application data events in VistA, to enable retrieval of updated information as a patient's data changes. This patch added new PROTOCOL (#101) file entries and links to other appropriate application events, as well as new utilities in the VPRHS routines to directly support the Regional Health Connect (RHC) servers.

## Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In 2019, all data for active patients was loaded into the Edge Cache Repositories (ECR) on the RHC servers. A patient was considered active at run-time if they:

- Were a current inpatient.
- Had future scheduled appointments or admissions.
- Had a visit within the past three years.

Now, the VPR application performs two primary functions to support HS:

- Monitor patient data events in VistA and notify the RHC of new or modified records.
- Respond to requests from the RHC for an updated copy of those records.

If the patient does *not* currently have data in the ECR, a request for a full new patient load is added to the RHC update list instead.

## Data Update Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR monitors about 40 different patient data events in VistA to be able to notify the RHC that new or updated data is available. The VPR SUBSCRIPTION (#560) file tracks all active patients that have data in the ECR, and it maintains the upload lists used by the RHC to extract updated records.

Patient data is extracted when it is no longer in a draft status, usually electronically signed or in a completed or verified state. Requests for future action, such as orders or appointments, can be removed from the ECR if cancelled before being performed. Records that are retracted or marked as in error are also removed.

### Protocol Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An event in the PROTOCOL (#101) file can be triggered by an application after a record has been added or modified. Other applications add protocol Items to the event to be notified of the changes.

![](virtual-patient-record-vpr-developer-s-guide/023.png) REF: For details about the Kernel Unwinder (XQOR) utility that processes protocols and subscribers, see the Kernel 8.0 and *Kernel Toolkit 7.3 Developer’s Guide* on the [VA Software Document Library (VDL)](https://www.va.gov/vdl/application.asp?appid=10).

VPR added listeners to the HL7 event protocols listed in <u>Table 59</u>:

| Event Protocol                    | Listener            |
|-----------------------------------|---------------------|
| RMIM DRIVER                       | VPR RMIM EVENTS     |
| PSO VDEF RDS O13 OP PHARM PPAR VS | VPR PSO VDEF EVENTS |
| PSO VDEF RDS O13 OP PHARM PREF VW | VPR PSO VDEF EVENTS |
| VAFC ADT-A08 SERVER               | VPR ADT-A08 CLIENT  |

<span id="_Ref11243020" class="anchor"></span>Table 60: VPR *Non*-HL7 Event Protocols and Associated Listeners

VPR also monitors the *non*-HL7 event protocols listed in <u>Table 60</u>:

| Event Protocol                     | Listener               |
|------------------------------------|------------------------|
| DG FIELD MONITOR                   | VPR DG UPDATES         |
| DG PTF ICD DIAGNOSIS NOTIFIER      | VPR PTF EVENTS         |
| DG PTF ICD PROCEDURE NOTIFIER      | VPR PTF OP EVENTS      |
| DG SA FILE ENTRY NOTIFIER          | VPR DGS EVENTS         |
| DGPF PRF EVENT                     | VPR PRF EVENTS         |
| DGPM MOVEMENT EVENTS               | VPR INPT EVENTS        |
| FH EVSEND OR                       | VPR XQOR EVENTS        |
| GMPL EVENT                         | VPR GMPL EVENT         |
| GMRA ASSESSMENT CHANGE             | VPR GMRA ASSESSMENT    |
| GMRA ENTERED IN ERROR              | VPR GMRA ERROR EVENTS  |
| GMRA SIGN-OFF ON DATA              | VPR GMRA EVENTS        |
| GMRA VERIFY DATA                   | VPR GMRA EVENTS        |
| GMRC EVSEND OR                     | VPR XQOR EVENTS        |
| IBCN NEW INSURANCE EVENTS          | VPR IBCN EVENTS        |
| LR7O AP EVSEND OR                  | VPR XQOR EVENTS        |
| LR7O CH EVSEND OR                  | VPR XQOR EVENTS        |
| MDC OBSERVATION UPDATE             | VPR OBSERVATION UPDATE |
| OR EVSEND FH                       | VPR NA EVENTS          |
| OR EVSEND GMRC                     | VPR NA EVENTS          |
| OR EVSEND LRCH                     | VPR NA EVENTS          |
| OR EVSEND ORG                      | VPR XQOR EVENTS        |
| OR EVSEND PS                       | VPR NA EVENTS          |
| OR EVSEND RA                       | VPR NA EVENTS          |
| OR EVSEND VPR                      | VPR XQOR EVENTS        |
| PS EVSEND OR                       | VPR XQOR EVENTS        |
| PSB EVSEND VPR                     | VPR PSB EVENTS         |
| PXK VISIT DATA EVENT               | VPR PCE EVENTS         |
| RA EVSEND OR                       | VPR XQOR EVENTS        |
| SCMC PATIENT TEAM CHANGES          | VPR PCMM TEAM          |
| SCMC PATIENT TEAM POSITION CHANGES | VPR PCMM TEAM POSITION |
| SDAM APPOINTMENT EVENTS            | VPR APPT EVENTS        |
| TIU DOCUMENT ACTION EVENT          | VPR TIU RETRACT        |
| WV PREGNANCY STATUS CHANGE EVENT   | VPR PREGNANCY EVENT    |

<span id="_Ref11243546" class="anchor"></span>Table 61: VPR MUMPS Cross Reference Listeners

### MUMPS Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two VistA files that require data monitoring do *not* have a protocol event, so the MUMPS-type cross references in <u>Table 61</u> were created to call a VPR listener routine on edits:

| File                             | Index |
|----------------------------------|-------|
| TIU DOCUMENT (#8925)             | AEVT  |
| TIU MULTIPLE SIGNATURE (#8925.7) | AVPR  |
| GMRV VITAL MEASUREMENT (#120.5)  | AVPR  |

<span id="_Toc155864445" class="anchor"></span>Table 62: Advance Directive SDA Container

### Tasked Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most events process updates immediately, making changes available to the ECR in near real time. Some event updates need to be tasked but usually run within 5-10 minutes.

#### Patient Demographics

The VistA Registration package fires the DG FIELD MONITOR protocol for every field that is changed in the PATIENT (#2) file, but the entire [Patient](#patient) container is updated all at once. The VPR DG UPDATES listener creates a task the first time it runs, which waits 10 minutes before adding the [Patient](#patient) container to the upload list; the task number is saved in the VPR SUBSCRIPTION (#560) file until it runs. When the DG event fires for another field, the VPR listener simply quits if a task number already exists.

#### Encounters (PCE)

SDA organizes data first by patient but then by encounter, so any record that is linked to a visit must have that pointer defined when the record is created in the ECR; if assigned later, the original record will not be found and a duplicate will be created with the encounter.

When encounters are created or edited in VistA, data is passed to the Patient Care Encounter (PCE) application which fires the PXK VISIT DATA EVENT protocol. This process can happen multiple times during a single user session in some applications, so the VPR PCE EVENTS listener collects the visit number as well as the identifiers of all modified records in ^XTMP in the following format:

^XTMP("VPRPX",0) = descriptor node  
^XTMP("VPRPX",visit~dfn) = NOW ^ visit;9000010 ^ 1 if new

^XTMP("VPRPX",visit~dfn,vFile,ien) = 1 if new

^XTMP("VPRPX","ZTSK") = current task number

It then fires off a task (if one does *not* already exist) to check ^XTMP in 5 minutes; if the encounter has been stable and unchanged for at least 2 minutes, it is moved to the AVPR upload list along with any related PCE records and the ^XTMP entry is removed. If any encounters remain in ^XTMP at the end of the task, it requeues itself to repeat this process until all records have been moved to the upload list.

PCE records can be deleted in VistA, but if the new flag in ^XTMP is true (1). Then, the ^XTMP nodes are simply KILLed, because the record was never sent to the ECR.

![](virtual-patient-record-vpr-developer-s-guide/024.png) REF: For more information on managing deleted records, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

#### Documents (TIU)

The TIU Document event is an index, so it can fire multiple times during a single user session. Documents are also usually linked to a visit, but the visit event is tasked, and thus, is not always executed before the note has been marked as complete and the index is executed. HealthShare requires the encounter to be uploaded to the ECR before any data linked to that encounter.

For these reasons, TIU Documents also use the same process and task as Encounters to populate the upload list. Document identifiers are also saved in ^XTMP in the following format:

^XTMP("VPRPX","DOC",ien) = NOW ^ ien;8925

The encounter task looks for any waiting documents tied to each visit processed, to ensure that a document’s encounter is uploaded first. Any other waiting documents are then also moved to the upload list when stable for at least 2 minutes.

### VPR Subscription File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR SUBSCRIPTION (#560) file tracks the subscription status of patients for inclusion in the ECR. If subscribed, data changes detected for that patient are tracked in the Patients subfile and indexed for fast retrieval by HS in either of the following indexes:

- ^VPR(“ANEW”)
- ^VPR(“AVPR”)

#### ANEW Index

New, or newly active, patients are added to the ANEW index when VistA clinical activity is detected. The RHC monitors this index to register and subscribe to these patients. Once subscribed, the RHC will then automatically upload all of that patient’s current data into HealthShare. The ANEW index is subscripted by a sequence number and patient DFN, and also includes the ICN:

^VPR("ANEW",9,224)="10111V183702"

The RHC removes the ANEW index node when it has registered the patient.

#### AVPR Index

Once a patient is subscribed to, changes to his/her clinical data results in a node added to the AVPR index. Like the ANEW index, the AVPR index is subscripted by a sequence number and the patient DFN. Changes are applied to the ECR in order; AVPR saves more data to know what record has been updated, including:

- Patient ICN
- SDA Container Name
- Record ID, which consists of two semi-colon pieces:
- Internal entry number, or a string that uniquely identifies the record to the Entity
- VistA source file or subfile number
- Action Code:
- U—Update
- D—Delete
- Visit Number (if available)

For example:

^VPR("AVPR",1,229)="10104V248233^Problem^940;9000011^U^"

^VPR("AVPR",2,229)="10104V248233^OtherOrder^33751;100^U^"

^VPR("AVPR",3,229)="10104V248233^Referral^618;123^U^"

^VPR("AVPR",4,229)="10104V248233^Appointment^3190524.1128,229;2.98^U^"

^VPR("AVPR",5,229)="10104V248233^Document^4239;8925^U^7200"

Like ANEW, the RHC removes the AVPR index node when it has uploaded the record.

## Generating SDA Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPR responds to requests for data from the RHC with XML that is formatted according to the Summary Document Architecture (SDA) data model. SDA organizes patient data by classes called “containers,” which correspond to various types of patient data.

VPR uses the VA FileMan ENTITY (#1.5) file to store the mappings between VistA files and fields, and SDA container classes and properties. There is a VPR entity for every file or subfile that feeds a container; some containers have multiple VistA sources, and so multiple VPR entities exist. Entities also exist for subclasses and common or shared data elements, such as providers or locations. The name and structure of each VPR entity is intended to comply with the SDA model.

The initial data set for the VPR Entities was based on the VPR RPCs. Unlike the VPR RPCs that are hard-coded, the DDE (Entity) utility provides a table-driven interface that can be easily updated and searched. SDA supports an aggregated data cache, so national standard codes are used when possible while still preserving VistA values. Some property values are translated to SDA or HL7 table values; see the SDA Class Reference for detailed information on each container.

### SDA Containers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SDA organizes patient data by classes called “containers,” which correspond to various types of clinical data. VPR is currently populating 21 of the 30 SDA containers. There is a VPR entity for every file or subfile that feeds a container; some containers have multiple VistA sources, and so multiple VPR entities exist. The names and structure of each VPR entity is intended to comply with the SDA model.

#### Advance Directives

The Advance Directive (AD) container holds completed TIU Documents with a title that is in the Advance Directives document class.

<table>
<caption><p><span id="_Toc155864446" class="anchor"></span>Table 63: Alert SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 35%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source File</th>
<th>Entity</th>
<th>Events</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th colspan="2"><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TIU Document (#8925)</td>
<td>VPR ADVANCE DIRECTIVE</td>
<td><p>AEVT index on #8925,</p>
<p>TIU DOCUMENT ACTION EVENT protocol</p></td>
<td colspan="2">No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864446" class="anchor"></span>Table 63: Alert SDA Container

A document *must* be complete or amended to be saved in the ECR; retracted documents are removed from the ECR. A patient should have only one active AD at a time per site, but VistA does *not* explicitly track or mark each as active or inactive. The status is set to inactive if the title contains “rescind”.

ADs are not linked to an encounter in SDA, even if the document has a visit pointer in TIU.

#### Alerts

The Alert container holds Patient Record Flags (PRF), and copies of TIU documents with a title in the Crisis Note or Clinical Warning document classes (that populate the “CW” indicator in CPRS).

<table style="width:100%;">
<caption><p><span id="_Toc155864447" class="anchor"></span>Table 64: Allergy SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entities</th>
<th>Events</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRF Assignment (#26.13)</td>
<td>VPR PATIENT RECORD FLAG</td>
<td>DGPF PRF EVENT</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>TIU Document (#8925)</td>
<td>VPR CW NOTES</td>
<td><p>AEVT index on #8925,</p>
<p>TIU DOCUMENT ACTION EVENT protocol</p></td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864447" class="anchor"></span>Table 64: Allergy SDA Container

Only national flag assignments are extracted for the ECR, as local flag assignments have not historically been shared between VistA sites. Flag assignments are *not* deleted from the ECR, but they can be inactivated.

A document *must* be complete or amended to be saved in the ECR; retracted documents are removed from the ECR. Alert documents are *not* linked to an encounter in the ECR, even if the document has a visit pointer in TIU.

#### Allergies

The Allergy container holds all records from the Allergy/Adverse Reaction Tracking application for each patient, or an assessment entry if there are none.

<table>
<caption><p><span id="_Toc155864448" class="anchor"></span>Table 65: Appointment SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 35%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entities</th>
<th>Events</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient Allergies (#120.8)</td>
<td>VPR ALLERGY</td>
<td><p>GMRA SIGN-OFF ON DATA</p>
<p>GMRA VERIFY DATA</p>
<p>GMRA ENTERED IN ERROR</p></td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Adverse Reaction Assessment (#120.86)</td>
<td>VPR ALLERGY ASSESSMENT</td>
<td>GMRA ASSESSMENT CHANGE</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864448" class="anchor"></span>Table 65: Appointment SDA Container

Unlike most other containers, records marked as Entered in Error are retained in SDA at the request of client applications, as this is the only way an allergy can be inactivated in VistA.

If the patient has *not* been assessed for allergies, or has been marked as having No Known Allergies, an Assessment record is sent to the ECR. The creation of an allergy later causes the assessment record to be removed from the ECR. If all reactions are inactivated (marked as Entered in Error), the assessment record will be re-sent to note No Known Allergies.

#### Appointments

The Appointment container is populated primarily from the Appointments subfile of the Patient (#2) file, supplemented with additional data from related entries in the Appointment subfile of the Hospital Location (#44) file and the Outpatient Encounter (#409.68) file. This container also contains entries from the Scheduled Admissions (#41.1) file.

<table>
<caption><p><span id="_Toc155864449" class="anchor"></span>Table 66: Diagnosis SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entities</th>
<th>Events</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Appointment (#2.98) subfile</td>
<td>VPR APPOINTMENT</td>
<td>SDAM APPOINTMENT EVENTS</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Scheduled Admission (#41.1)</td>
<td>VPR SCHEDULED ADMISSION</td>
<td>DG SA FILE ENTRY NOTIFIER</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864449" class="anchor"></span>Table 66: Diagnosis SDA Container

Appointments are *not* usually associated with a visit until checked-in, but SDA organizes data by encounter, and thus, requires the Encounter Number at the time a record is created, if used; populating this property later causes a duplicate entry to be created. For this reason, the visit number is retrieved from the related Outpatient Encounter entry when assigned and stored in an extension property instead of the standard Encounter Number.

Cancelled appointments and admissions are currently filtered out and removed from the ECR.

#### Diagnoses

The Diagnosis container holds ICD code assignments from the V POV (outpatient) and PTF (inpatient) files. The PTF extract pulls codes from the Principal Diagnosis (#79) field, and the Secondary Diagnosis 1-24 (#79.16-79.24915) fields.

<table>
<caption><p><span id="_Toc155864450" class="anchor"></span>Table 67: Document SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entities</th>
<th>Events</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>V POV (#9000010.07)</td>
<td><p>VPR V POV</p>
<p>VPR DEL VPOV</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>PTF (#45)</td>
<td><p>VPR PTF</p>
<p>VPR DEL PTF</p></td>
<td>DG PTF ICD DIAGNOSIS NOTIFIER</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864450" class="anchor"></span>Table 67: Document SDA Container

All diagnoses expect an encounter and are *not* posted without a related VISIT (#9000010) file entry. Each ICD code in the PTF (#45) file creates a separate record in the ECR.

PCE allows V POV records to be deleted, and individual codes can be deleted from PTF. The VPR DEL entities use data saved in ^XTMP to create the delete request.

![](virtual-patient-record-vpr-developer-s-guide/025.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

#### Document

The Document container holds all completed TIU Documents, as well as any Lab or Radiology reports not stored in TIU. All documents must be complete (TIU) or verified (Lab or Rad) to be pulled into the ECR; retracted documents are removed from the ECR.

<table>
<caption><p><span id="_Toc155864451" class="anchor"></span>Table 68: Encounter SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entities</th>
<th>Events</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TIU Document (#8925)</td>
<td><p>VPR DOCUMENT</p>
<p>VPR DEL DOCUMENT</p></td>
<td><p>AEVT index on #8925,</p>
<p>TIU DOCUMENT ACTION EVENT protocol</p></td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Rad/Nuc Med Reports (#74)</td>
<td>VPR RAD REPORT</td>
<td>RA EVSEND OR</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Lab Data (#63)</td>
<td><p>VPR LRMI REPORT</p>
<p>VPR LRAP REPORT</p></td>
<td><p>LR7O CH EVSEND OR</p>
<p>LR7O AP EVSEND OR</p></td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>

<span id="_Toc155864451" class="anchor"></span>Table 68: Encounter SDA Container

Most TIU notes are linked to a visit, though not all. Reports *not* stored in TIU are not tied to an encounter.

Because notes are *not* sent to the ECR until complete, they *cannot* be deleted in VistA afterwards. Some retraction scenarios do, however, remove the Visit pointer from the note which the ECR needs to find and remove the note. The VPR DEL entity uses data saved in ^XTMP to create the delete request.

![](virtual-patient-record-vpr-developer-s-guide/026.png) REF: For more information on building delete messages. see Section 5.3.3, “Deleting Records.”

Any addenda that are added to a note are always included in the original note text. VPR does *not* pull addenda separately for the ECR. Amending a note is a different process that retracts the original and creates a new one. The old note is kept as an audit trail, while the new one can be edited and replaces it. Any user can add an addendum to a note, but users *must* have access to a special TIU menu to be able to amend a note.

If the AP ESIG ON (#619) field in LABORATORY SITE (#69.9) file is set to YES, then pathology reports are stored in TIU and *must* follow all TIU processing rules (signed, complete). For lab reports *not* stored in TIU, including all microbiology reports, results *must* be verified and the report is generated via Lab package APIs.

Radiology reports are *not* stored in TIU at all and *must* have a Report Status of Verified, Released, or Electronically Filed. If a report is part of a set (multiple reports for a single order), all are saved together in the ECR as a single document like TIU addenda.

#### Encounters

The Encounter container is populated from the VISIT (#9000010) file. Supplemental data is pulled from the PATIENT MOVEMENT (#405) and ED LOG (#230) files for admissions and ED visits, respectively. All visits are pulled except for child visits that only store additional StopCodes for the parent visit.

<table>
<caption><p><span id="_Toc155864452" class="anchor"></span>Table 69: Family History SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Visit (#9000010)</td>
<td><p>VPR VISIT</p>
<p>VPR VISIT STUB</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Patient Movement (#405)</td>
<td>VPR ADMISSION</td>
<td>DGPM MOVEMENT EVENTS</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>ED Log (#230)</td>
<td>VPR EDP LOG</td>
<td><p>AVPR index on #230</p>
<p>PXK VISIT DATA EVENT</p></td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864452" class="anchor"></span>Table 69: Family History SDA Container

PCE allows a visit to be deleted if no other records are pointing to it. Deleting an admission or ED log entry in VistA does *not* remove the encounter from the ECR until the related visit is also deleted.

![](virtual-patient-record-vpr-developer-s-guide/027.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

A visit with a Service Category of “Hospitalization” corresponds to an admission in the PATIENT MOVEMENT (#405) file. A PCE item, VSIT PATIENT STATUS, on the DGPM MOVEMENT EVENTS protocol creates a new visit for a new admission. An entire inpatient episode is considered a single visit, so all subsequent movements simply update the admission encounter in the ECR. An admission *must* have a related visit number to be stored in the ECR, but most data is pulled from the movements. Movements can be deleted, but the encounter is *not* removed from the ECR until the related visit is deleted.

Most data in the ED LOG (#230) file that is relevant for the ECR is captured in the VISIT (#9000010) file, and as such is maintained by the PXK VISIT DATA EVENT. The AVPR index on \#230 lets VPR know when an ED Log entry has been closed.

#### Family History

The Family History container is currently populated by the V Health Factors file, with any records that contain some form of ‘Family History’ in its name as there is no Factor Category that contains all history factors.

<table>
<caption><p><span id="_Toc155864453" class="anchor"></span>Table 70: Lab Order SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source File</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>V Health Factor (#9000010.23)</td>
<td><p>VPR FAMILY HISTORY</p>
<p>VPR DEL FAMILY HX</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864453" class="anchor"></span>Table 70: Lab Order SDA Container

Family History entries expect an encounter and are not posted without a related VISIT (#9000010) file entry.

V Health Factor records can also be deleted. The VPR DEL entity uses data saved in ^XTMP to create the delete request.

![](virtual-patient-record-vpr-developer-s-guide/028.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

#### Lab Orders

The Lab Order container is populated from the Orders file, with associated results from the Lab Data file. Orders are added to the ECR when released to the service; cancelled orders that were never acted on are removed from SDA. Orders with a schedule create “child” orders are released to Lab instead of the original “parent” order; only the “child” orders are sent to the ECR.

<table>
<caption><p><span id="_Toc155864454" class="anchor"></span>Table 71: Medication SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Order (#100)</td>
<td>VPR LAB ORDER</td>
<td><p>OR EVSEND LRCH</p>
<p>LR 7O CH EVSEND OR</p></td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Result Subfiles</td>
<td>Entities</td>
<td>Events</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Chem (#63.01)</td>
<td>VPR LRCH RESULT</td>
<td>LR7O CH EVSEND OR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Microbiology (#63.05)</td>
<td>VPR LRMI RESULT</td>
<td>LR7O CH EVSEND OR</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surgical Pathology (#63.08)</td>
<td>VPR LRSP RESULT</td>
<td>LR7O AP EVSEND OR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Cytopathology (#63.09)</td>
<td>VPR LRCY RESULT</td>
<td>LR7O AP EVSEND OR</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>EM (#63.02)</td>
<td>VPR LREM RESULT</td>
<td>LR7O AP EVSEND OR</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc155864454" class="anchor"></span>Table 71: Medication SDA Container

The OR EVSEND protocols are invoked by CPRS when an order is released to the service for action. This usually happens on signature, but an order can be explicitly released without a signature (then signed later). All subsequent updates come from the package events.

![](virtual-patient-record-vpr-developer-s-guide/029.png) REF: For details on these events, see the OE/RR documentation on the [VDL](https://www.va.gov/vdl/section.asp?secid=1).

Until very recently, pathology requests were made directly to the lab; there was no order for them in CPRS. Without an order, the results *cannot* be saved in the [Lab Order](#lab-orders) container; older reports are available in the [Document](#document) container.

Blood Bank requests and results are *not* currently being sent to the ECR.

#### Medications

The Medication container is populated primarily from the Orders file, with additional data coming from the various Pharmacy application files. Orders are sent to the ECR when released to the service; cancelled orders that were never acted on are removed from the ECR. Inpatient orders with a schedule create “child” orders are released to Pharmacy instead of the original “parent” order; only the “child” orders are sent to the ECR.

<table>
<caption><p><span id="_Toc155864455" class="anchor"></span>Table 72: Member Enrollment SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 31%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Order (#100)</td>
<td>VPR MEDICATION</td>
<td><p>OR EVSEND PS</p>
<p>PS EVSEND OR</p></td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Result Sub/files</td>
<td>Entities</td>
<td>Events</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Unit Dose (#55.06)</td>
<td><p>VPR DRUG PRODUCT</p>
<p>VPR DOSAGE STEP</p>
<p>VPR MED ADMINISTRATION</p></td>
<td><p>PS EVSEND OR</p>
<p>PSB EVSEND OR</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>IV (#55.01)</td>
<td><p>VPR IV PRODUCT</p>
<p>VPR MED ADMINISTRATION</p></td>
<td><p>PS EVSEND OR</p>
<p>PSB EVSEND OR</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Non-VA Meds (#55.05)</td>
<td><p>VPR DRUG PRODUCT</p>
<p>VPR DOSAGE STEP</p></td>
<td>PS EVSEND OR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Prescription (#52)</td>
<td><p>VPR DRUG PRODUCT</p>
<p>VPR MED FILL</p></td>
<td><p>PS EVSEND OR</p>
<p>PSO VDEF RDS 013 OP</p>
<p>PHARM PREF VS</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc155864455" class="anchor"></span>Table 72: Member Enrollment SDA Container

The OR EVSEND protocols are invoked by CPRS when an order is released to the service for action. This usually happens on signature, but an order can be explicitly released without a signature (then signed later). All subsequent updates come from the package events.

![](virtual-patient-record-vpr-developer-s-guide/030.png) REF: For details on these events, see the OE/RR documentation on the [VDL](https://www.va.gov/vdl/section.asp?secid=1).

#### Member Enrollment

The Member Enrollment container is populated by the Insurance Type subfile of the PATIENT (#2) file, which is managed by the Integrated Billing (IB) VistA application.

<table>
<caption><p><span id="_Toc155864456" class="anchor"></span>Table 73: Observation SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 31%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Insurance Type (#2.312)</td>
<td><p>VPR INSURANCE</p>
<p>VPR DEL INSURANCE</p></td>
<td>IBCN NEW INSURANCE EVENTS</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864456" class="anchor"></span>Table 73: Observation SDA Container

Integrated Billing allows policy assignments to be deleted. The VPR DEL entity uses data saved in ^XTMP to create the delete requeues.

![](virtual-patient-record-vpr-developer-s-guide/031.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

#### Observations

The Observation container is populated primarily from the GMRV Vital Measurements file but can also include vitals stored in the Clinical Procedures OBS file.

<table>
<caption><p><span id="_Toc155864457" class="anchor"></span>Table 74: Other Order SDA Container</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GMRV Vital Measurement (#120.5)</td>
<td>VPR VITAL MEASUREMENT</td>
<td>AVPR index on #120.5</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>OBS (#704.117)</td>
<td>VPR VITAL MEASUREMENT</td>
<td>MDC OBSERVATION UPDATE</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>

<span id="_Toc155864457" class="anchor"></span>Table 74: Other Order SDA Container

The GMRVUT0 utility returns vitals stored in both files and the GMV APIs support the OBS GUID as well as a \#120.5 IEN, so both files share a single entity. Observations are *not* linked to an encounter or removed from the ECR.

#### Other Orders

The Other Order container is populated by the Orders file and holds any kind of order that was not sent to Lab, Pharmacy, or Radiology. Orders are sent to the ECR when released; cancelled orders that were never acted on are removed from the ECR.

<table>
<caption><p><span id="_Toc155864458" class="anchor"></span>Table 75: Patient SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 31%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Order (#100)</td>
<td>VPR OTHER ORDER</td>
<td><p>OR EVSEND ORG</p>
<p>OR EVSEND FH</p>
<p>FH EVSEND OR</p>
<p>OR EVSEND GMRC</p>
<p>GMRC EVSEND OR</p></td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864458" class="anchor"></span>Table 75: Patient SDA Container

The OR EVSEND protocols are invoked by CPRS when an order is released to the service for action. This usually happens on signature, but an order can be explicitly released without a signature (then signed later). All subsequent updates come from the package events.

![](virtual-patient-record-vpr-developer-s-guide/032.png) REF: For details on these events, see the OE/RR documentation on the [VDL](https://www.va.gov/vdl/section.asp?secid=1).

Orders for the OR package are also called “generic” or text orders, since they only live within CPRS and are *not* sent to any other service for action. As such, they usually go directly to an Active status and users can complete them inside CPRS (which invokes the event).

The Other Orders container also holds Dietetics (FH) and Consult (GMRC) orders. Consult events also cause an entry to be made or updated in the [Referral](#referral) container.

#### Patient

The Patient container is populated primarily from the PATIENT (#2) file and supplemented by various other Registration package files.

<table>
<caption><p><span id="_Toc155864459" class="anchor"></span>Table 76: Physical Exam SDA Container</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 30%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient (#2)</td>
<td>VPR PATIENT</td>
<td><p>DG FIELD MONITOR</p>
<p>VAFC ADT-08 SERVER</p></td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Patient Team Assignment (#404.42)</td>
<td>VPR PATIENT EXTENSION</td>
<td>SCMC PATIENT TEAM CHANGES</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Patient Team Position Assignment (#230)</td>
<td>VPR PATIENT EXTENSION</td>
<td>SCMC PATIENT TEAM POSITION CHANGES</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>

<span id="_Toc155864459" class="anchor"></span>Table 76: Physical Exam SDA Container

Authoritative demographics from Master Veteran Index (MVI) and the HC Registry are saved in the Enterprise Facility (EF) Edge and returned instead of any local value when a request is made to the Access Gateway. Most other properties are returned from the preferred or last treated facility, though some return all values tagged with the source facility.

#### Physical Exams

The Physical Exam container is populated by the V Exam file.

<table>
<caption><p><span id="_Toc155864460" class="anchor"></span>Table 77: Problem SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>V EXAM (#9000010.13)</td>
<td><p>VPR V EXAM</p>
<p>VPR DEL V EXAM</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864460" class="anchor"></span>Table 77: Problem SDA Container

All exams expect an encounter and are *not* posted without a related VISIT (#9000010) file entry.

PCE allows V EXAM records to be deleted. The VPR DEL entity uses data saved in ^XTMP to create the delete request.

![](virtual-patient-record-vpr-developer-s-guide/033.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

#### Problems

The Problem container is populated primarily by the Problem file but also includes Functional Independence Measurements. All problems, active and inactive, are sent to the ECR; “hidden” problems are filtered out or removed.

<table>
<caption><p><span id="_Toc155864461" class="anchor"></span>Table 78: Procedure SDA Container</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 30%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Problem (#9000011)</td>
<td>VPR PROBLEM</td>
<td>GMPL EVENT</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Functional Independence Measurement (#783)</td>
<td>VPR FIM</td>
<td>RMIM DRIVER</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>

<span id="_Toc155864461" class="anchor"></span>Table 78: Procedure SDA Container

The preferred coding system for a problem is SNOMED, but early entries in this file used only ICD. The Problem property is populated by the SNOMED (#80001) field if available; otherwise, the ICD code (field \#.01) is used.

FIM data is returned in the Problem container because previous CDA document specifications looked for it here, and much of SDA used similar structures. Current versions of both models now prefer the [Social History](#social-history) container.

#### Procedures

The primary source for the Procedure container is the V CPT file. Inpatient ICD procedure codes are pulled from the Procedure Code 1-25 (#4-28) fields in the 601 subfile of the PTF (#45) file.

<table>
<caption><p><span id="_Toc155864462" class="anchor"></span>Table 79: Rad Order SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>V CPT (#9000010.18)</td>
<td><p>VPR V CPT</p>
<p>VPR DEL V CPT</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Surgery (#130)</td>
<td>VPR SURGERY</td>
<td>AEVT index on #8925</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="odd">
<td>PTF 601 (#45.05)</td>
<td><p>VPR PTF 601</p>
<p>VPR DEL PTF 601</p></td>
<td>DG PTF ICD PROCEDURE NOTIFIER</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864462" class="anchor"></span>Table 79: Rad Order SDA Container

All procedures expect an encounter and are *not* posted without a related VISIT (#9000010) file entry.

PCE allows V CPT records to be deleted, and individual codes can be deleted from PTF. The VPR DEL entities use data saved in ^XTMP to create the delete request.

![](virtual-patient-record-vpr-developer-s-guide/034.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

Many applications create entries in V CPT for billing and workload tracking, and some of those codes are returned to the ECR elsewhere. Surgery codes are pulled from the Surgery package instead, when a report has been completed in TIU indicating that the procedure has been done. Codes for office visit type are skipped in Procedure and instead returned as a property of the Encounter. Immunization CPT codes are returned in the [Vaccination](#vaccination) container.

#### Rad Order

The Rad Order container is populated from the Orders file, with associated results from the Rad/Nuc Med Patient file. Orders are added to the ECR when released to the service; cancelled orders that were never acted on are removed from SDA.

<table style="width:100%;">
<caption><p><span id="_Toc155864463" class="anchor"></span>Table 80: Referral SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Order (#100)</td>
<td>VPR RAD ORDER</td>
<td>OR EVSEND RA</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Result Sub/file</td>
<td>Entity</td>
<td>Event</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Examinations (#70.03)</td>
<td>VPR RAD RESULT</td>
<td>RA EVSEND OR</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc155864463" class="anchor"></span>Table 80: Referral SDA Container

The OR EVSEND protocols are invoked by CPRS when an order is released to the service for action. This usually happens on signature, but an order can be explicitly released without a signature (then signed later). All subsequent updates come from the package events.

![](virtual-patient-record-vpr-developer-s-guide/035.png) REF: For details on these events, see the OE/RR documentation on the [VDL](https://www.va.gov/vdl/section.asp?secid=1).

#### Referral

The Referral container is populated by the Request/Consultation file, which includes consult and clinical procedure requests. A consult makes an entry in both the Referral and the [Other Order](#other-orders) containers; it can also appear in the [Procedure](#procedures) container if it has a corresponding Clinical Procedure record.

<table style="width:100%;">
<caption><p><span id="_Toc155864464" class="anchor"></span>Table 81: Social History SDA Container</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Request/Consultation (#123)</td>
<td>VPR REFERRAL</td>
<td><p>OR EVSEND GMRC</p>
<p>GMRC EVSEND OR</p></td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>

<span id="_Toc155864464" class="anchor"></span>Table 81: Social History SDA Container

The OR EVSEND protocols are invoked by CPRS when an order is released to the service for action. This usually happens on signature, but an order can be explicitly released without a signature (then signed later). All subsequent updates come from the package events.

![](virtual-patient-record-vpr-developer-s-guide/036.png) REF: For details on these events, see the OE/RR documentation on the [VDL](https://www.va.gov/vdl/section.asp?secid=1).

SDA does *not* support the Delete action for the Referral container, so cancelled consults are *not* removed from the ECR.

The Consult package supports both local and remote requests, via the Inter-Facility Consult (IFC) feature. The Referring Provider has different source fields for local requests (field \#10 - \#200 IEN) vs. remote (field \#.126 – name string only). Remote consults that have only results will have no corresponding order in CPRS.

#### Social History

The Social History container is populated primarily by the V Health Factor file, with entries related to Smoking or Tobacco Use. It also contains a Pregnancy Status entry for female patients using data in the Women’s Health package.

<table>
<caption><p><span id="_Toc155864465" class="anchor"></span>Table 82: Vaccination SDA Container</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 27%" />
<col style="width: 31%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>V Health Factor (#9000010.23)</td>
<td><p>VPR SOCIAL HISTORY</p>
<p>VPR DEL SOCIAL HX</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Pregnancy Status (#790.05) subfile</td>
<td>VPR PREGNANCY</td>
<td>WV PREGNANCY STATUS CHANGE EVENT</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>

<span id="_Toc155864465" class="anchor"></span>Table 82: Vaccination SDA Container

V Health Factors expect an encounter and are *not* posted without a related VISIT (#9000010) file entry, but the Pregnancy Status does not.

PCE allows V Health Factor records to be deleted. The VPR DEL entity uses data saved in ^XTMP to create the delete request.

![](virtual-patient-record-vpr-developer-s-guide/037.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

Only a single entry tracking the pregnancy status of female patients is currently being sent to the ECR, and not every entry in the Pregnancy Status Log.

#### Vaccination

The Vaccination container is populated primarily from the V Immunization file but may also include vaccination refusals in the V Imm Contra/Refusal Event or V Health Factor files.

<table>
<caption><p><span id="_Toc155864466" class="anchor"></span>Table 83: HS.SDA3.CodeTableDetail Data Types</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 28%" />
<col style="width: 28%" />
<col style="width: 7%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Primary Source Files</th>
<th>Entity(ies)</th>
<th>Event(s)</th>
<th><p>Use</p>
<p>Enc?</p></th>
<th><p>Can</p>
<p>Delete</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>V Immunization (#9000010.11)</td>
<td><p>VPR VACCINATION</p>
<p>VPR DEL VACCINATION</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>V Imm Contra/Refusal Events (#9000010.707)</td>
<td><p>VPR ICR EVENT</p>
<p>VPR DEL ICR</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>V Health Factor (#9000010.23)</td>
<td><p>VPR VACC HF REFUSAL</p>
<p>VPR DEL HF VACC</p>
<p>REFUSAL</p></td>
<td>PXK VISIT DATA EVENT</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc155864466" class="anchor"></span>Table 83: HS.SDA3.CodeTableDetail Data Types

All V files expect an encounter and are not posted without a related VISIT (#9000010) file entry.

PCE allows V file records to be deleted. The VPR DEL entities use data saved in ^XTMP to create the delete request

![](virtual-patient-record-vpr-developer-s-guide/038.png) REF: For more information on building delete messages, see Section <u>5.3.3</u>, “<u>Deleting Records</u>.”

### Reference Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference files themselves are *not* stored in the ECR, which is only for patient data. Most patient records point to one or more reference files, however, and SDA properties *must* be able to identify a record in a reference file consistently when needed.

Many VPR entities were created for reference files as coded elements, to be re-useable for consistency. Some have additional data included beyond the standard Code and Description.

| SDA Data Type Class      | Source File                         | Entity                   |
|--------------------------|-------------------------------------|--------------------------|
| ATCCode                  | VA Drug Class (#50.605)             | VPR DRUG CLASS           |
| CareProvider             | New Person (#200)                   | VPR PROVIDER             |
| CareProviderType         | Person Class (#8932.1)              | VPR PERSON CLASS         |
| CareProviderType         | Facility Treating Specialty (#45.7) | VPR SPECIALTY            |
| Country                  | Country Code (#779.004)             | VPR COUNTRY              |
| Diagnosis                | ICD Diagnosis (#80)                 | VPR ICD                  |
| DocumentCompletionStatus | TIU Status (#8925.6)                | VPR DOCUMENT STATUS      |
| DrugProduct              | Drug (#50)                          | VPR DRUG PRODUCT         |
| EthnicGroup              | Ethnicity (#10.2)                   | VPR ETHNICITY            |
| Generic                  | VA Generic (#50.6)                  | VPR DRUG GENERIC         |
| HealthCareFacility       | Hospital Location (#44)             | VPR LOCATION             |
| LabTestItem              | Lab Test (#60)                      | VPR LAB TEST             |
| Language                 | Language (#.85)                     | VPR LANGUAGE             |
| MaritalStatus            | Master Marital Status (#11.99)      | VPR MARITAL STATUS       |
| Observation              | GMRV Vital Type (#120.51)           | VPR VITAL TYPE           |
| ObservationMethod        | GMRV Vital Qualifier (#120.51)      | VPR VITAL QUALIFIER      |
| ObservationValueCode     | Lab LOINC (#95.3)                   | VPR LOINC                |
| OrderCategory            | Display Group (#100.98)             | VPR DISPLAY GROUP        |
| Order                    | Orderable Item (#101.43)            | VPR ORDERABLE ITEM       |
| Organization             | Institution (#4)                    | VPR FACILITY             |
| Priority                 | Order Urgency (#101.42)             | VPR ORDER URGENCY        |
| Procedure                | CPT (#81)                           | VPR CPT                  |
| Race                     | Race Master (#10.99)                | VPR RACE                 |
| Reaction                 | Sign/Symptoms (#120.83)             | VPR ALLERGY SIGN/SYMPTOM |
| Religion                 | Religion (#13)                      | VPR RELIGION             |
| Route                    | Medication Routes (#51.2)           | VPR MED ROUTE            |
| State                    | State (#5)                          | VPR STATE                |
| UoM                      | UCUM Codes (#757.5)                 | VPR UNITS                |
| User                     | New Person (#200)                   | VPR USER                 |

<span id="_Toc155864467" class="anchor"></span>Table 84: HS.Local.VA.SDA3.CodeTableDetail Data Types

| SDA Data Type        | Source File                               | Entity                   |
|----------------------|-------------------------------------------|--------------------------|
| CreditStopCode       | Clinic Stop (#40.7)                       | VPR AMIS                 |
| CPTModifier          | CPT Modifier (#81.3)                      | VPR CPT MODIFIER         |
| DocumentClass        | TIU Document Definition (#8925.1)         | VPR DOCUMENT CLASS       |
| EligibilityCode      | Eligibility Code (#8)                     | VPR ELIGIBILITY          |
| MovementType         | Facility Movement Type (#405.1)           | VPR MAS MOVEMENT TYPE    |
| NationalTitle        | TIU VHA Enterprise Std Title (#8926.1)    | VPR DOCUMENT TITLE       |
| NationalTitleRole    | TIU LOINC Role (#8926.3)                  | VPR DOCUMENT ROLE        |
| NationalTitleService | TIU LOINC Service (#8926.5)               | VPR DOCUMENT SERVICE     |
| NationalTitleSetting | TIU LOINC Setting (#8926.4)               | VPR DOCUMENT SETTING     |
| NationalTitleSubject | TIU LOINC Subject Matter Domain (#8926.2) | VPR DOCUMENT SUBJECT     |
| NationalTitleType    | TIU LOINC Doc Type (#8926.6)              | VPR DOCUMENT TYPE        |
| Package              | Package (#9.4)                            | VPR PACKAGE              |
| Service              | Service/Section (#49)                     | VPR SERVICE              |
| StopCode             | Clinic Stop (#40.7)                       | VPR AMIS                 |
| SurgicalSpecialty    | Specialty (#42.4)                         | VPR MAS SPECIALTY        |
| SurgicalSpecialty    | Medical Specialty (#723)                  | VPR MED SPECIALTY        |
| SurgicalSpecialty    | Surgical Specialty (#45.3)                | VPR SURG SPECIALTY       |
| TransactionType      | MAS Mvt Transaction Type (#405.3)         | VPR MAS TRANSACTION TYPE |
| VAStatus             | Order Status (#100.01)                    | VPR ORDER STATUS         |
| WardLocation         | Ward Location (#42)                       | VPR WARD LOCATION        |

<span id="_Ref84233462" class="anchor"></span>Table 85: VPR HS MGR Menu Options

### Deleting Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Records can be removed from the ECR if they are cancelled or marked in error in VistA. Most records in the ECR are in a complete or verified state so they can no longer be physically deleted from VistA. This preserves data that must be included in the delete request for the RHC to find the record in the ECR and mark it as deleted. Usually the record identifier is sufficient, but some containers require additional properties to match the record. If the record was linked to a visit, then encounter number will also be required.

PCE records can be truly deleted in VistA. A copy of the deleted record’s zero node is saved in ^XTMP by upload sequence number, so the SDA message can still be built when requested from the RHC:

<span id="_Toc155864354" class="anchor"></span>Figure 5: Sample Deleted PCE Record Zero Node Saved in ^XTMP

^XTMP("VPR-seq",0) = descriptor node  
^XTMP("VPR-seq",ien) = DFN ^ Container ^ ien;file# ^ D ^ visit

^XTMP("VPR-seq",ien,0) = zero node of deleted record

Entities can be created for building delete requests that use this data in ^XTMP instead of the application file. Existing delete entities have names that begin with “VPR DEL” to easily identify them.

The ICD codes in the PTF (#45) file create entries in the [Diagnosis](#diagnoses) and [Procedure](#procedures) containers, and when one of those field values is deleted the old data is stored here as well. Some document retractions in TIU remove the visit pointer, so those are also handled by this mechanism.

### Container File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR CONTAINER (#560.1) file contains information about each SDA container class that has been implemented. The SOURCE FILE subfile links each VistA source for that container to one or more Entities used to build SDA messages.

<span id="_Toc155864355" class="anchor"></span>Figure 6: Sample SDA Container Class Entry in the VPR CONTAINER (#560.1) File

NAME: DIAGNOSIS DISPLAY NAME: Diagnosis

SOURCE FILE NUMBER: 9000010.07

UPDATE ENTITY: VPR V POV DELETE ENTITY: VPR DEL V POV

SOURCE FILE NUMBER: 45

UPDATE ENTITY: VPR PTF DELETE ENTITY: VPR DEL PTF

The UPDATE ENTITY is used to build most SDA messages, to send a new or updated record from VistA to the ECR. The DELETE ENTITY is used to build SDA messages for data or records that have been deleted from VistA, using data saved in ^XTMP instead of the regular global.

## VPRHS Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPRHS routine contains the utility functions needed to directly support the RHC servers. These APIs are only used within VPR or by Health Connect (HC). They are documented in this document to help system administrators who support the HC interface.

There are no ICR for these APIs; they are only used within VPR or by Health Connect (HC).

### \$\$ON^VPRHS: System Monitoring On/Off

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The \$\$ON^VPRHS extrinsic function returns the current status of the data monitoring utilities.

The VPR event listeners use this function to verify that data should be passed to HealthShare. If the system has been stopped for any reason, no data will be uploaded and the listener quits.

Format

\$\$ON^VPRHS

Input Parameters

None.

Output

Returns This Boolean function returns the following:

- 1—If system monitoring of data events is active.
- 0—If system monitoring of data events is not active.

#### Example

<span id="_Toc155864356" class="anchor"></span>Figure 7: \$\$ON^VPRHS Extrinsic Function—Example

\>W \$\$ON^VPRHS

1

### EN^VPRHS(): Subscribe a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The EN^VPRHS API adds a patient to the VPR SUBSCRIPTION (#560) file for data monitoring.

The RHC server calls this API during the patient subscription process. Developers working in a system that is *not* linked to an RHC can use this call in programmer mode to replicate the actions of the RHC.

Format

EN^VPRHS(dfn)

Input Parameters

dfn: (Required) Pointer to the PATIENT (#2) file.

Output

None.

#### Example

<span id="_Toc155864357" class="anchor"></span>Figure 8: EN^VPRHS API—Example

\>S DFN=229 D EN^VPRHS(DFN)

### UN^VPRHS(): Unsubscribe a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The UN^VPRHS API removes a patient from the VPR SUBSCRIPTION (#560) file to stop data monitoring for that patient.

The RHC server calls this API when a patient is removed from the data cache and data subscription is stopped. Developers working in a system that is *not* linked to an RHC can use this call in programmer mode to replicate the actions of the RHC.

Format

UN^VPRHS(dfn)

Input Parameters

dfn: (Required) Pointer to the PATIENT (#2) file.

Output

None.

#### Example

<span id="_Toc155864358" class="anchor"></span>Figure 9: UN^VPRHS API—Example

\>S DFN=229 D UN^VPRHS(DFN)

### \$\$SUBS^VPRHS(): Subscription Status of a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The \$\$SUBS^VPRHS extrinsic function returns the current subscription status of a patient.

The [POST^VPRHS](#postvprhs-add-record-to-avpr-index-for-uploading) API uses this function to determine if changes to this patient’s clinical data are currently being tracked in HealthShare.

Format

\$\$SUBS^VPRHS(dfn)

Input Parameters

dfn: (Required) Pointer to the PATIENT (#2) file.

Output

Returns This Boolean function returns the following:

- 1—If the patient is currently subscribed.
- 0—If the patient is *not* currently subscribed.

#### Example

<span id="_Toc155864359" class="anchor"></span>Figure 10: \$\$SUBS^VPRHS Extrinsic Function—Example

\>S DFN=229 W \$\$SUBS^VPRHS(DFN)

0

### \$\$VALID^VPRHS(): Validation of a Patient for HealthShare

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The \$\$VALID^VPRHS extrinsic function evaluates a patient for possible subscription for data monitoring in HealthShare. Patients:

- *Must* have an ICN.
- *Cannot* be deceased or merged.
- *Cannot* be marked as test patients on a Production system.

The [POST^VPRHS](#postvprhs-add-record-to-avpr-index-for-uploading) API uses this function when clinical data is added or modified for a patient that is *not* currently subscribed.

Format

\$\$VALID^VPRHS(dfn)

Input Parameters

dfn: (Required) Pointer to the PATIENT (#2) file.

Output

Returns This Boolean function returns the following:

- 1—If the patient is valid for subscription.
- 0—If the patient is *not* valid for subscription.

#### Example

<span id="_Toc155864360" class="anchor"></span>Figure 11: \$\$VALID^VPRHS Extrinsic Function—Example

\>S DFN=224 W \$\$VALID^VPRHS(DFN)

1

### POST^VPRHS(): Add Record to AVPR Index for Uploading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The POST^VPRHS API adds a node to the AVPR upload index when clinical activity occurs in VistA for a subscribed patient. If the patient is *not* subscribed but is eligible, control is passed to the [NEW^VPRHS](#newvprhs-add-patient-to-anew-index-for-subscribing) API for subscribing. The RHC then automatically uploads all of the patient’s data.

The VPR event listeners use this API when clinical data is added or modified for a patient:

- If the patient is subscribed, an entry is made in the ^VPR(“AVPR”) index.
- If the patient is *not* subscribed but passes the checks in the [\$\$VALID^VPRHS](#validvprhs-validation-of-a-patient-for-healthshare) function, then a request to register the patient in HealthShare is posted in the ^VPR(“ANEW”) index instead.
- If the patient is neither subscribed nor eligible for subscription, nothing is uploaded and the API quits.

Format

POST^VPRHS(dfn,type,id,action,visit\[,.seq\])

Input Parameters

dfn: (Required) Pointer to the PATIENT (#2) file.

type: (Required) Name of the SDA container where the data is to be stored.

id: (Required) Record identifier, in the format:

internal entry number\_“;”\_VistA source file numberaction: (Required) NULL to update the record, or “@” to delete it from HealthShare.

visit: (Required) Pointer to the related VISIT (#9000010) entry, if applicable.

.seq: (Optional) Parameter to return the assigned sequence number in the AVPR or ANEW upload lists, *must* be passed by reference.

Output

This API does *not* directly return any results. If successful, however:

- A node is added to the AVPR or ANEW index.
- The sequence number assigned may optionally be returned in the SEQ parameter.

#### Example

<span id="_Toc155864361" class="anchor"></span>Figure 12: POST^VPRHS API—Example

\>D POST^VPRHS(229,"Problem","644;9000011")

### NEW^VPRHS(): Add Patient to ANEW Index for Subscribing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The NEW^VPRHS API adds a node to the ANEW upload index when clinical activity occurs in VistA for an unsubscribed patient.

The [POST^VPRHS](#postvprhs-add-record-to-avpr-index-for-uploading) API calls this API when a valid patient needs to be registered in HealthShare and subscribed for data monitoring. The RHC server registers and subscribes the patient, and then retrieves all current data for the patient so individual record identifiers do *not* need to be passed here.

Format

NEW^VPRHS(dfn\[,icn\])

Input Parameters

dfn: (Required) Pointer to the PATIENT (#2) file.

icn: (Optional) ICN of patient. If not defined, it retrieves the ICN from the PATIENT (#2) file.

Output

This API does *not* directly return any results. If successful, however, a node is added to the ANEW index.

#### Example

<span id="_Toc155864362" class="anchor"></span>Figure 13: NEW^VPRHS API—Example

\>S DFN=229 D NEW^VPRHS(DFN)

### DEL^VPRHS(): Remove Nodes from ANEW or AVPR Upload Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The DEL^VPRHS API removes a node from the [ANEW](#anew-index) or [AVPR](#avpr-index) upload index after the RHC has processed the patient or record.

The RHC server calls this API to remove nodes from the index after processing. Developers working in a system that is *not* linked to an RHC can use this call in programmer mode to replicate the actions of the RHC.

Format

DEL^VPRHS(list,seq)

Input Parameters

list: (Required) Name of the index, either “[ANEW](#anew-index)” or “[AVPR](#avpr-index)”.

seq: (Required) Sequence number in the index of the node to be removed.

Output

This API does *not* directly return any results. If successful, however, the node disappears from the specified index.

#### Example

<span id="_Toc155864363" class="anchor"></span>Figure 14: DEL^VPRHS API—Example

\>D DEL^VPRHS("AVPR",5873294)

### GET^VPRHS(): Retrieve Patient Data for ECR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The GET^VPRHS API retrieves data from VistA in SDA format for HealthShare. The input parameters are used to call the VA FileMan DDE utility GET^DDE API for the appropriate ENTITY (#1.5) file entries, collecting and returning the results and optionally any errors that may occur.

The RHC server calls this API when data upload requests are put into the [AVPR](#avpr-index) or [ANEW](#anew-index) index. For [AVPR](#avpr-index) nodes, GET is called using the data saved in the index node as the input parameters to request a specific record. For [ANEW](#anew-index), the RHC server requests a whole container at a time to retrieve all current data for the patient.

Format

GET^VPRHS(dfn,type\[,id\]\[,.query\],format,results,errors)

Input Parameters

dfn: (Required) Pointer to the PATIENT (#2) file.

type: (Required) Name of the desired SDA Container.

id: (Optional) Record identifier, in the format:

internal entry number\_“;”\_VistA source file number

If *not* defined, the entire container is returned based on Query.

.query(“name”): (Optional) Array of search conditions as a list of name-value pairs, passed by reference. This parameter is optional and not used if the id parameter is defined.

Commonly used search parameters include:

QUERY(“start”) = VA FileMan formatted date.timeQUERY(“stop”) = VA FileMan formatted date.timeQUERY(“max”) = Maximum number of items to return

Others may be supported by a specific Entity, such as a status One value is used when ID is defined, to retrieve stored data for deleted records:

QUERY(“sequence”) = AVPR list item being processedformat: (Required) Format for results:

- 0=JSON.
- 1=XML (default).

results: (Required) Closed array name for returning results, default is:

^TMP(“VPR GET”,\$J,#)errors: (Required) Closed array name for returning errors, default is:

^TMP(“VPR ERR”,\$J,#)

Output

Returns: This API return results in the specified array or ^TMP global, a single record per list item. The total number of records returned is in the zero node of the array.

#### Examples

#### Example 1

<span id="_Toc155864364" class="anchor"></span>Figure 15: GET^VPRHS API—Example 1

\>D GET^VPRHS(229,"Problem","644;9000011",,1,"VPRESLT") ZW VPRESLT

<span class="mark">VPRESLT(0)</span>=1

<span class="mark">VPRESLT(1)</span>="\<Problem\>\<UpdatedOn\>2007-04-10T00:00:00\</UpdatedOn\>\<Extension\>\<IsExp

osureAO\>false\</IsExposureAO\>\<IsExposureIR\>false\</IsExposureIR\>\<IsExposurePG\>fals

e\</IsExposurePG\>\<IsSc\>false\</IsSc\>\<Service\>MEDICAL\</Service\>\<OnsetDate\>2005-04-0

7\</OnsetDate\>\<LexiconId\>60339\</LexiconId\>\<Priority\>CHRONIC\</Priority\>\</Extension

\>\<ProblemDetails\>Hypertension\</ProblemDetails\>\<Problem\>\<SDACodingStandard\>ICD-9-

CM\</SDACodingStandard\>\<Code\>401.9\</Code\>\<Description\>HYPERTENSION NOS\</Descripti

on\>\</Problem\>\<Clinician\>\<SDACodingStandard\>VA200\</SDACodingStandard\>\<Extension\>\<

Title\>Scholar Extraordinaire\</Title\>\</Extension\>\<Code\>10000000031\</Code\>\<Descrip

tion\>VEHU,ONEHUNDRED\</Description\>\<Name\>\<FamilyName\>VEHU\</FamilyName\>\<GivenName\>

ONEHUNDRED\</GivenName\>\</Name\>\</Clinician\>\<Status\>\<SDACodingStandard\>SNOMED CT\</S

DACodingStandard\>\<Code\>55561003\</Code\>\<Description\>Active\</Description\>\</Status\>

\<EnteredBy\>\<SDACodingStandard\>VA200\</SDACodingStandard\>\<Code\>10000000031\</Code\>\<

Description\>VEHU,ONEHUNDRED\</Description\>\</EnteredBy\>\<EnteredAt\>\<SDACodingStanda

rd\>VA4\</SDACodingStandard\>\<Code\>500\</Code\>\<Description\>CAMP MASTER\</Description\>

\</EnteredAt\>\<EnteredOn\>2007-04-10T00:00:00\</EnteredOn\>\<FromTime\>2005-04-07T00:00

:00\</FromTime\>\<ExternalId\>644;PL\</ExternalId\>\</Problem\>"

#### Example 2

<span id="_Toc155864365" class="anchor"></span>Figure 16: GET^VPRHS API—Example 2

\>S QRY("start")=2991101,QRY("stop")=2991130,QRY("max")=2

\>D GET^VPRHS(129,"Encounter",,.QRY,1,"VPRESLT") ZW VPRESLT

<span class="mark">VPRESLT(0)</span>=2

<span class="mark">VPRESLT(1)</span>="\<Encounter\>\<Extension\>\<StopCode\>\<SDACodingStandard\>AMIS\</SDACodingSt

andard\>\<Code\>328\</Code\>\<Description\>MEDICAL/SURGICAL DAY UNIT MSDU\</Description\>

\</StopCode\>\</Extension\>\<EncounterNumber\>1822\</EncounterNumber\>\<EncounterType\>O\</

EncounterType\>\<EncounterCodedType\>\<Code\>A\</Code\>\<Description\>AMBULATORY\</Descrip

tion\>\</EncounterCodedType\>\<ConsultingClinicians\>\<CareProvider\>\<SDACodingStandard

\>VA200\</SDACodingStandard\>\<Extension\>\<Role\>PRIMARY\</Role\>\<Title\>Scholar Extraord

inaire\</Title\>\</Extension\>\<Code\>11712\</Code\>\<Description\>PROVIDER,TWOHUNDREDNINE

TYSEVEN\</Description\>\<Name\>\<FamilyName\>PROVIDER\</FamilyName\>\<GivenName\>TWOHUNDRE

DNINETYSEVEN\</GivenName\>\</Name\>\<CareProviderTyp: e\>\<SDACodingStandard\>X12\</SDACodi

ngStandard\>\<Extension\>\<Classification\>Physician/Osteopath\</Classification\>\</Exte

nsion\>\<Code\>203B00000N\</Code\>\<Description\>Physicians (M.D. and D.O.)\</Descriptio

n\>\</CareProviderType\>\</CareProvider\>\</ConsultingClinicians\>\<HealthCareFacility\>\<

SDACodingStandard\>VA44\</SDACodingStandard\>\<Extension\>\<StopCode\>\<SDACodingStandar

d\>AMIS\</SDACodingStandard\>\<Code\>328\</Code\>\<Description\>MEDICAL/SURGICAL DAY UNIT

MSDU\</Description\>\</StopCode\>\<CreditStopCode\>\<SDACodingStandard\>AMIS\</SDACoding

Standard\>\<Code\>328\</Code\>\<Description\>MEDICAL/SURGICAL DAY UNIT MSDU\</Descriptio

n\>\</CreditStopCode\>\<Service\>MEDICINE\</Service\>\</Extension\>\<Code\>261\</Code\>\<Descr

iption\>\<\![CDATA\[MIKE'S MEDICAL CLINIC\]\]\>\</Description\>\<LocationType\>OTHER\</Locat

ionType\>\</HealthCareFacility\>\<Priority\>\<Code\>P\</Code\>\<Description\>PRIMARY\</Descr

iption\>\</Priority\>\<EnteredBy\>\<SDACodingStandard\>VA200\</SDACodingStandard\>\<Code\>1

1712\</Code\>\<Description\>PROVIDER,TWOHUNDREDNINETYSEVEN\</Description\>\</EnteredBy\>

\<EnteredAt\>\<SDACodingStandard\>VA4\</SDACodingStandard\>\<Code\>500\</Code\>\<Descriptio

n\>CAMP MASTER\</Description\>\</EnteredAt\>\<EnteredOn\>1999-11-22T11:13:45\</EnteredOn

\>\<FromTime\>1999-11-22T11:13:12\</FromTime\>\<ToTime\>1999-11-22T11:13:00\</ToTime\>\</E

ncounter\>"

<span class="mark">VPRESLT(2)</span>="\<Encounter\>\<Extension\>\<Cpt\>\<SDACodingStandard\>CPT-4\</SDACodingStanda

rd\>\<Code\>99201\</Code\>\<Description\>\<\![CDATA\[OFFICE OR OTHER OUTPATIENT VISIT FOR

THE EVALUATION AND MANAGEMENT OF A NEW PATIENT, WHICH REQUIRES THESE THREE KEY C

OMPONENTS: A PROBLEM FOCUSED HISTORY; A PROBLEM FOCUSED EXAMINATION; AND STRAIGH

TFORWARD MEDICAL DECISION MAKING. COUNSELING AND/OR COORDINATION OF CARE WITH OT

HER PROVIDERS OR AGENCIES ARE PROVIDED CONSISTENT WITH THE NATURE OF THE PROBLEM

\(S\) AND THE PATIENT'S AND/OR FAMILY'S NEEDS. USUALLY, THE PRESENTING PROBLEMS AR

E SELF LIMITED OR MINOR. PHYSICIANS TYPICALLY SPEND 10 MINUTES FACE-TO-FACE WITH

THE PATIENT AND/OR FAMILY.\]\]\>\</Description\>\</Cpt\>\<StopCode\>\<SDACodingStandard\>A

MIS\</SDACodingStandard\>\<Code\>401\</Code\>\<Description\>GENERAL SURGERY\</Description

\>\</StopCode\>\</Extension\>\<EncounterNumber\>1806\</EncounterNumber\>\<EncounterType\>O\<

/EncounterType\>\<EncounterCodedType\>\<Code\>A\</Code\>\<Description\>AMBULATORY\</Descri

ption\>\</EncounterCodedType\>\<ConsultingClinicians\>\<CareProvider\>\<SDACodingStandar

d\>VA200\</SDACodingStandard\>\<Extension\>\<Role\>PRIMARY\</Role\>\<Title\>Scholar Extraor

dinaire\</Title\>\</Extension\>\<Code\>11712\</Code\>\<Description\>PROVIDER,TWOHUNDREDNIN

ETYSEVEN\</Description\>\<Name\>\<FamilyName\>PROVIDER\</FamilyName\>\<GivenName\>TWOHUNDR

EDNINETYSEVEN\</GivenName\>\</Name\>\<CareProviderType\>\<SDACodingStandard\>X12\</SDACod

ingStandard\>\<Extension\>\<Classification\>Physician/Osteopath\</Classification\>\</Ext

ension\>\<Code\>203B00000N\</Code\>\<Description\>Physicians (M.D. and D.O.)\</Descripti

on\>\</CareProviderType\>\</CareProvider\>\</ConsultingClinicians\>\<HealthCareFacility\>

\<SDACodingStandard\>VA44\</SDACodingStandard\>\<Extension\>\<StopCode\>\<SDACodingStanda

rd\>AMIS\</SDACodingStandard\>\<Code\>401\</Code\>\<Description\>GENERAL SURGERY\</Descrip

tion\>\</StopCode\>\<Service\>SURGERY\</Service\>\<Specialty\>\<SDACodingStandard\>VA45.7\</

SDACodingStandard\>\<Code\>18\</Code\>\<Description\>GEM ACUTE MEDICINE\</Description\>\</

Specialty\>\</Extension\>\<Code\>91\</Code\>\<Description\>\<\![CDATA\[SHERYL'S CLINIC\]\]\>\</D

escription\>\<Organization\>\<SDACodingStandard\>VA4\</SDACodingStandard\>\<Code\>998\</Co

de\>\<Description\>ABILENE (CAA)\</Description\>\</Organization\>\<LocationType\>OTHER\</L

ocationType\>\</HealthCareFacility\>\<Priority\>\<Code\>P\</Code\>\<Description\>PRIMARY\</D

escription\>\</Priority\>\<EnteredBy\>\<SDACodingStandard\>VA200\</SDACodingStandard\>\<Co

de\>11712\</Code\>\<Description\>PROVIDER,TWOHUNDREDNINETYSEVEN\</Description\>\</Entere

dBy\>\<EnteredAt\>\<SDACodingStandard\>VA4\</SDACodingStandard\>\<Code\>500\</Code\>\<Descri

ption\>CAMP MASTER\</Description\>\</EnteredAt\>\<EnteredOn\>1999-11-17T11:12:10\</Enter

edOn\>\<FromTime\>1999-11-17T09:00:00\</FromTime\>\<ToTime\>1999-11-17T11:12:00\</ToTime

\>\</Encounter\>"

### TEST^VPRHS(): Test SDA Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The TEST^VPRHS API retrieves data from VistA in SDA format for a single record. The input parameters are used to call the VA FileMan \$\$GET1^DDE utility for the specified ENTITY (#1.5) file entry and display the result or any errors that may occur onscreen.

This API can be used by a developer in programmer mode, for testing and debugging purposes.

Format

TEST^VPRHS(entity,id,dfn\[,seq\])

Input Parameters

entity: (Required) Name of a single entry in, or pointer to, the ENTITY (#1.5) file.

id: (Required) Pointer to the desired record, from the VistA file defined by the Entity’s DEFAULT FILE NUMBER (#.02) field.

dfn: (Required) Pointer to the PATIENT (#2) file.

seq: (Optional) Sequence number of the record in the upload list.

Output

Returns: This API executes the requested entity and displays the results onscreen, as well as any errors that might occur.

#### Example

<span id="_Toc155864366" class="anchor"></span>Figure 17: TEST^VPRHS API—Example

\>D TEST^VPRHS("VPR PROBLEM",644,229)

\<Problem\>

\<UpdatedOn\>2007-04-10T00:00:00\</UpdatedOn\>

\<Extension\>

\<IsExposureAO\>false\</IsExposureAO\>

\<IsExposureIR\>false\</IsExposureIR\>

\<IsExposurePG\>false\</IsExposurePG\>

\<IsSc\>false\</IsSc\>

\<Service\>MEDICAL\</Service\>

\<OnsetDate\>2005-04-07\</OnsetDate\>

\<LexiconId\>60339\</LexiconId\>

\<Priority\>CHRONIC\</Priority\>

\</Extension\>

\<ProblemDetails\>Hypertension\</ProblemDetails\>

\<Problem\>

\<SDACodingStandard\>ICD-9-CM\</SDACodingStandard\>

\<Code\>401.9\</Code\>

\<Description\>HYPERTENSION NOS\</Description\>

\</Problem\>

\<Clinician\>

\<SDACodingStandard\>VA200\</SDACodingStandard\>

\<Extension\>

\<Title\>Scholar Extraordinaire\</Title\>

\</Extension\>

\<Code\>10000000031\</Code\>

\<Description\>VEHU,ONEHUNDRED\</Description\>

\<Name\>

\<FamilyName\>VEHU\</FamilyName\>

\<GivenName\>ONEHUNDRED\</GivenName\>

\</Name\>

\</Clinician\>

\<Status\>

\<SDACodingStandard\>SNOMED CT\</SDACodingStandard\>

\<Code\>55561003\</Code\>

\<Description\>Active\</Description\>

\</Status\>

\<EnteredBy\>

\<SDACodingStandard\>VA200\</SDACodingStandard\>

\<Code\>10000000031\</Code\>

\<Description\>VEHU,ONEHUNDRED\</Description\>

\</EnteredBy\>

\<EnteredAt\>

\<SDACodingStandard\>VA4\</SDACodingStandard\>

\<Code\>500\</Code\>

\<Description\>CAMP MASTER\</Description\>

\</EnteredAt\>

\<EnteredOn\>2007-04-10T00:00:00\</EnteredOn\>

\<FromTime\>2005-04-07T00:00:00\</FromTime\>

\<ExternalId\>644;PL\</ExternalId\>

\</Problem\>

\>

## Generating Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use VA FileMan options to generate and display online documentation to get the most current information about the VPR-SDA interface.

### VPR CONTAINER (#560.1) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Print File Entries option \[DIPRINT\] of VA FileMan to display the contents of the VPR CONTAINER (#560.1) file, as shown in <u>Figure 18</u>. The VPR CONTAINER SOURCES Print template can be used to show the primary Entities for each container and source.

<span id="_Ref83905344" class="anchor"></span>Figure 18: Print File Entries Option—Displaying the VPR CONTAINER (#560.1) File Contents

Select OPTION: <span class="mark">PRINT FILE ENTRIES</span>

Output from what File: VPR CONTAINER// <span class="mark">\<Enter\></span> (24 entries)

Sort by: NAME// <span class="mark">\<Enter\></span>

Start with NAME: FIRST// <span class="mark">\<Enter\></span>

First Print FIELD: <span class="mark">\[VPR CONTAINER SOURCES</span>

(JUL 22, 2021@12:17) User \#11948 File \#560.1

Do you want to edit the 'VPR CONTAINER SOURCES' Template? No// <span class="mark">\<Enter\></span> (No)

Heading (S/C): VPR CONTAINER List// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">0;80;99 \<Enter\></span> Linux Telnet /SSh

VPR CONTAINER List JUL 22, 2021@12:54 PAGE 1

NAME DISPLAY NAME

SOURCE FILE

NUMBER UPDATE ENTITY DELETE ENTITY

--------------------------------------------------------------------------

ADVANCE DIRECTIVE AdvanceDirective

8925 VPR ADVANCE DIRECTIVE

ALERT

26.13 VPR PATIENT RECORD FLAG

8925 VPR CW NOTES

ALLERGY

120.8 VPR ALLERGY

120.86 VPR ALLERGY ASSESSMENT

APPOINTMENT

2.98 VPR APPOINTMENT

41.1 VPR SCHEDULED ADMISSION

DIAGNOSIS

9000010.07 VPR V POV VPR DEL V POV

45 VPR PTF VPR DEL PTF

DOCUMENT

8925 VPR DOCUMENT VPR DEL TIU DOCUMENT

74 VPR RAD REPORT

63.05 VPR LRMI REPORT

63.08 VPR LRAP REPORT

ENCOUNTER

9000010 VPR VISIT VPR VISIT STUB

405 VPR ADMISSION

230 VPR EDP LOG

FAMILY HISTORY FamilyHistory

9000010.23 VPR FAMILY HISTORY VPR DEL FAMILY HX

ILLNESS HISTORY IllnessHistory

LAB ORDER LabOrder

100 VPR LAB ORDER

MEDICAL CLAIM MedicalClaim

MEDICATION

100 VPR MEDICATION

MEMBER ENROLLMENT MemberEnrollment

2.312 VPR INSURANCE

OBSERVATION Observation

120.5 VPR VITAL MEASUREMENT

OTHER ORDER OtherOrder

100 VPR OTHER ORDER

PATIENT Patient

2 VPR PATIENT

PHYSICAL EXAM PhysicalExam

9000010.13 VPR V EXAM VPR DEL V EXAM

PROBLEM Problem

9000011 VPR PROBLEM

783 VPR FIM

PROCEDURE Procedure

130 VPR SURGERY

9000010.18 VPR V CPT VPR DEL V CPT

PROGRAM MEMBERSHIP ProgramMembership

RAD ORDER RadOrder

100 VPR RAD ORDER

REFERRAL Referral

123 VPR REFERRAL

SOCIAL HISTORY SocialHistory

9000010.23 VPR SOCIAL HISTORY VPR DEL SOCIAL HX

790.05 VPR PREGNANCY

VACCINATION Vaccination

9000010.11 VPR VACCINATION VPR DEL VACCINATION

9000010.23 VPR VACC HF REFUSAL VPR DEL HF VACC REFUSAL

9000010.707 VPR ICR EVENT VPR DEL ICR

The UPDATE ENTITY (<u>Figure 18</u>) is used to build most SDA messages, to send a new or updated record from VistA to the ECR. The DELETE ENTITY (<u>Figure 18</u>) is used to build SDA messages for data or records that have been deleted from VistA, using data saved in ^XTMP instead of the regular global.

### Print an Entity Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Mapping \[DDE ENTITY MAPPING\] menu, on the VA FileMan Other Options \[DIOTHER\] menu, contains options that support the creation and management of the ENTITY (#1.5) file entries.

Use the Print an Entity \[DDE ENTITY INQUIRE\] option to display an Entity in a more readable format than the regular VA FileMan Inquire to File Entries option \[DIINQUIRE\]. Basic information about the Entity displays first, followed by a list of the Entity’s Items.

Select the Summary format to see a simple list as shown in <u>Figure 19</u>, or Detailed to view all properties of each item.

<span id="_Ref67809974" class="anchor"></span>Figure 19: Print an Entity Option—Displaying Entities in a Readable Format

Select OPTION: <span class="mark">OTHER OPTIONS</span>

Select OTHER OPTION: <span class="mark">DATA MAPPING</span>

Select DATA MAPPING OPTION: <span class="mark">?</span>

    Answer with DATA MAPPING OPTION NUMBER, or NAME

   Choose from:

   1            ENTER/EDIT AN ENTITY

   <span class="mark">2            PRINT AN ENTITY</span>

   3            GENERATE AN ENTITY FOR A FILE

  

Select DATA MAPPING OPTION: <span class="mark">2 \<Enter\></span> PRINT AN ENTITY

Select ENTITY: <span class="mark">VPR ALLERGY</span>

     1   VPR ALLERGY       SDA

     2   VPR ALLERGY ASSESSMENT       SDA

     3   VPR ALLERGY EXTENSION       SDA

     4   VPR ALLERGY OBSERVATION       SDA

     5   VPR ALLERGY SIGN EXTENSION       SDA

Press \<Enter\> to see more, '^' to exit this list,  OR

CHOOSE 1-5: <span class="mark">1 \<Enter\></span> VPR ALLERGY     SDA

Print item summary or details? Summary

DEVICE: HOME// <span class="mark">0;80;99</span>  NETWORK

ENTITY: VPR ALLERGY (#52)

  FILE: PATIENT ALLERGIES (#120.8)          Jun 07, 2019@09:58:20   PAGE 1

--------------------------------------------------------------------------

DISPLAY NAME: Allergy

      SORT BY:                          DATA MODEL: SDA

    FILTER BY:                           READ ONLY: NO

       SCREEN:

QUERY ROUTINE: ALLERGYS^VPRSDAQ

ENTRY ACTION: S VASITE=+\$\$SITE^VASITE S:VASITE'\>0 VASITE=\$\$KSP^XUPARAM("INST")

    ID ACTION: D ALG1^VPRSDAL(DIEN)

  EXIT ACTION: K GMRAL,GMRAY,VPRALG,VASITE

Seq  Item                        Type Field  Sub/File   Entity

--------------------------------------------------------------------------

2    Extension                     E         120.8      VPR ALLERGY EXTENSION

3    Allergy                       E      1  120.8      VPR CODE TABLE

4    AllergyCategory               E    3.1  120.8      VPR CODE TABLE

5    Clinician                     E     21  120.8      VPR PROVIDER

6    Reaction                      E         120.8      VPR ALLERGY SIGN/SYMPTOM

7    Severity                      E         120.85     VPR CODE TABLE

8    Certainty                     E     19  120.8      VPR CODE TABLE

12   InactiveTime                  S     23  120.8

13   InactiveComments              S         120.8

14   VerifiedTime                  S     20  120.8

17   FreeTextAllergy               S    .02  120.8

19   Status                        S     22  120.8

22   EnteredBy                     E      5  120.8      VPR USER

23   EnteredAt                     E         120.8      VPR FACILITY

24   EnteredOn                     S      4  120.8

25   FromTime                      S         120.85

26   ToTime                        S     23  120.8

27   ExternalId                    I        

Select DATA MAPPING OPTION:

## Monitoring and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If data is not being saved in the ECR, ensure that the application events and tasks are all running, and that the SDA itself is building correctly and as expected.

The HealthShare Interface Manager \[VPR HS MGR\] menu shown in <u>Figure 20</u> contains two sub-menus that can be used for monitoring the system and troubleshooting the SDA messages.

<span id="_Ref84603107" class="anchor"></span>Figure 20: HealthShare Interface Manager \[VPR HS MGR\] Menu

Select OPTION NAME: <span class="mark">VPR HS MGR \<Enter\></span> HealthShare Interface Manager

<span class="mark">HS VPR HealthShare Utilities ...</span>

TEST Test/Audit VPR Functions ...

Select HealthShare Interface Manager Option:

<u>Table 85</u>, describes the two HealthShare Interface Manager \[VPR HS MGR\] sub-menus that contain options that can be used for technical support or testing:

| Option Name                                                  | Option Text               | Description                                                                                                                                           |
|--------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [VPR HS MENU](#vpr-healthshare-utilities-vpr-hs-menu-menu)   | VPR HealthShare Utilities | This menu contains utilities for managing the interface between the VistA Virtual Patient Record (VPR) and the Regional Health Connect (RHC) servers. |
| [VPR HS TESTER](#testaudit-vpr-functions-vpr-hs-tester-menu) | Test/Audit VPR Functions  | This menu contains options to facilitate the audit and testing of the VPR interface with HealthShare.                                                 |

<span id="_Ref84233518" class="anchor"></span>Table 86: VPR HealthShare Utilities Menu Options

### VPR HealthShare Utilities \[VPR HS MENU\] Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR HealthShare Utilities \[VPR HS MENU\] menu shown in <u>Figure 21</u> contains four options used for managing the interface between VistA and the RHC servers:

<span id="_Ref84611724" class="anchor"></span>Figure 21: VPR HealthShare Utilities \[VPR HS MENU\] Menu

Select HealthShare Interface Manager Option: <span class="mark">HS \<Enter\></span> VPR HealthShare Utilities

ENC Encounter Transmission Task Monitor

AVPR SDA Upload List Monitor

UPD Add Records to Upload List

ON Enable Data Monitoring

Select VPR HealthShare Utilities Option:

<u>Table 86</u> and the sub-sections that follow describe the VPR HealthShare Utilities \[VPR HS MENU\] menu options:

| Option Name                                                                            | Option Text                         | Description                                                                                                                           |
|----------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [VPR HS TASK MONITOR](#encounter-transmission-task-monitor-vpr-hs-task-monitor-option) | Encounter Transmission Task Monitor | This option checks the status of the task that collects encounters and related records from PCE and TIU for the AVPR upload list. |
| [VPR HS SDA MONITOR](#sda-upload-list-monitor-vpr-hs-sda-monitor-option)               | SDA Upload List Monitor             | This option monitors the AVPR list of upload requests for the RHC.                                                                |
| [VPR HS PUSH](#add-records-to-upload-list-vpr-hs-push-option)                          | Add Records to Upload List          | This option allows a site to manually add patient record id(s) to the AVPR upload list if needed.                                 |
| [VPR HS ENABLE](#enable-data-monitoring-vpr-hs-enable-option)                          | Enable Data Monitoring              | This option enables or disables the tracking of patient data for the AVPR upload list.                                            |

<span id="_Ref84235694" class="anchor"></span>Table 87: Test/Audit VPR Functions \[VPR HS TESTER\] Menu Options

#### Encounter Transmission Task Monitor \[VPR HS TASK MONITOR\] Option

Updates to the ECR from the Patient Care Encounter (PCE) application are processed and added to the upload list by a background task, to collect multiple edits into a single update per encounter. Documents stored in the Text Integration Utilities (TIU) application also use this process, as they are usually linked to a visit and may also save multiple edits during a single user session.

![](virtual-patient-record-vpr-developer-s-guide/039.png) REF: For details on the event tasks, see Section <u>5.2.3</u>, “<u>Tasked Events</u>.”

HealthShare requires encounters to be uploaded first, before any data linked to that encounter can be saved.

The Encounter Transmission Task Monitor \[VPR HS TASK MONITOR\] option checks the health of this task, displaying the task number and its current status. Any waiting encounters or documents can be viewed here. If the task has stopped for any reason and data is waiting, the task can also be restarted with this option.

<span id="_Toc155864371" class="anchor"></span>Figure 22: Encounter Transmission Task Monitor \[VPR HS TASK MONITOR\] Option—System Prompts and User Entries

Select VPR HealthShare Utilities Option: <span class="mark">ENC \<Enter\></span> Encounter Transmission Task Monitor

Current time: Feb 04, 2021@16:37:10

Data Monitoring System is ON.

Checking TaskMan ...

VPR Encounter task is SCHEDULED.

Task \#8437572 is SCHEDULED for Feb 04, 2021@16:40:33

Checking the Transmission List ...

There are encounters awaiting transmission.

There are no documents awaiting transmission.

Enter monitor action: UPDATE// <span class="mark">?</span>

Enter \<RETURN\> to refresh the monitor display.

<span class="mark">Enter Q to exit the monitor.</span>

Enter T to display the task.

Enter R to re-queue the transmission task.

<span class="mark">Enter E to display the Encounter list.</span>

Enter D to display the Document list.

Enter ? to see this message.

Enter monitor action: UPDATE// <span class="mark">E</span>

Last Updated Visit# DFN Location Feb 04, 2021@16:37:21

--------------------------------------------------------------------------

2/ 4/21@16:33:33 1851 9 GENERAL MEDICINE

Press \<return\> to continue ...<span class="mark">\<Enter\></span>

Current time: Feb 04, 2021@16:37:26

Data Monitoring System is ON.

Checking TaskMan ...

VPR Encounter task is SCHEDULED.

Task \#8437572 is SCHEDULED for Feb 04, 2021@16:40:33

Checking the Transmission List ...

There are encounters awaiting transmission.

There are no documents awaiting transmission.

Enter monitor action: UPDATE// <span class="mark">Q</span>

#### SDA Upload List Monitor \[VPR HS SDA MONITOR\] Option

The SDA Upload List Monitor \[VPR HS SDA MONITOR\] option is a simple monitor of the [AVPR](#avpr-index) index, which the RHC server polls every few seconds for data extracts, optionally filtered by patient and container. If no patient or container is selected, all current entries in the list are displayed. The RHC server removes entries from this index when the data has been uploaded, so this list should turn over every few seconds if the system is running correctly.

The last sequence number used in this list is also displayed at the bottom.

<span id="_Toc155864372" class="anchor"></span>Figure 23: SDA Upload List Monitor \[VPR HS SDA MONITOR\] Option—System Prompts and User Entries

Select VPR HealthShare Utilities Option: <span class="mark">SDA Upload List Monitor</span>

Select PATIENT NAME: <span class="mark">\<Enter\></span>

Select CONTAINER: <span class="mark">\<Enter\></span>

VPR Global Upload Monitor Apr 16, 2021@15:08:30

SEQ DFN All containers for all patients

--------------------------------------------------------------------------

4838 8 5000000049V161696^Medication^16417;100^U^

4839 153 5000000100V704929^Medication^16419;100^U^

4840 153 5000000100V704929^Medication^16420;100^U^

4841 9 5000000098V757329^Observation^525;120.5^U^

4842 9 5000000098V757329^Observation^526;120.5^U^

4843 741 5000000026V032296^Medication^16547;100^U^

4844 741 5000000026V032296^Medication^16546;100^U^

4845 9 5000000098V757329^LabOrder^16578;100^U^

4846 9 5000000098V757329^LabOrder^16577;100^U^

4847 9 5000000098V757329^Medication^16550;100^U^

4848 181 5000000068V971252^Medication^15534;100^U^

4849 300 5000000128V793395^Medication^15556;100^U^

4850 129 5000000129V929287^Medication^15549;100^U^

4851 129 5000000129V929287^Medication^15551;100^U^

4852 300 5000000128V793395^Medication^15553;100^U^

4853 134 5000000046V523900^Medication^15555;100^U^

4854 756 1012856479V033267^Alert^7;26.13^U^

4855 128 5000000126V406128^Medication^16579;100^U^

4856 300 5000000128V793395^Medication^15578;100^U^

Press \<return\> to continue or ^ to exit ... <span class="mark">\<Enter\></span>

VPR Global Upload Monitor Apr 16, 2021@15:09:06

SEQ DFN All containers for all patients

--------------------------------------------------------------------------

4857 9 5000000098V757329^Medication^16892;100^U^

4858 179 5000000115V760984^Medication^16374;100^U^

4859 755 1012856477V526483^Allergy^947;120.8^U^

4860 9 5000000098V757329^Medication^16413;100^U^

Current Sequence#: 4860

Do you wish to continue to monitor the upload global? YES// <span class="mark">NO</span>

#### Add Records to Upload List \[VPR HS PUSH\] Option

The Add Records to Upload List \[VPR HS PUSH\] option allows patient record id(s) to be manually added to the AVPR upload list, if it is suspected that the data cache has gotten out of synch or a record extract has errored.

<span id="_Toc155864373" class="anchor"></span>Figure 24: Add Records to Upload List \[VPR HS PUSH\] Option—System Prompts and User Entries

Select VPR HealthShare Utilities Option: <span class="mark">UPD \<Enter\></span> Add Records to Upload List

Select PATIENT NAME: <span class="mark">VPRPATIENT,ONE \<Enter\></span> 12-1-46 666000004 YES NSC VETERAN \*MULTIPLE BIRTH\* SMB SMB

Select CONTAINER: <span class="mark">PROB \<Enter\></span> Problem

Update the full container? NO// <span class="mark">?</span>

Enter YES to send all available records in this container to the ECR, or

NO to exit.

Update the full container? NO// <span class="mark">\<Enter\></span>

This container has multiple sources; please select one.

Select SOURCE FILE: <span class="mark">?</span>

Select a VistA source file for this container, or press return for all.

Select one of the following:

9000011 PROBLEM

783 FUNCTIONAL INDEPENDENCE MEASUREMENT RECORD

Select SOURCE FILE: <span class="mark">PROBLEM</span>

Available Problems for VPRPATIENT,ONE:

1 JUL 29, 2019 Hearing loss (SCT 15188001)

Select ITEM(S): 1

Problem \#1 added to update queue.

Select CONTAINER:

#### Enable Data Monitoring \[VPR HS ENABLE\] Option

The Enable Data Monitoring \[VPR HS ENABLE\] option enables or disables the tracking of patient data changes in the AVPR upload list, for retrieval by the RHC server. Turning off data monitoring effectively disables the VistA – HealthShare interface entirely, so *this option is for emergency use only and is locked with the VPR HS ENABLE security key*. A timestamp is captured when the system is turned on or off, for use in data recovery.

![](virtual-patient-record-vpr-developer-s-guide/040.png) CAUTION: In a Production system, only use this option at the direction of Health Product Support (HPS) or VPR development staff!

<span id="_Toc155864374" class="anchor"></span>Figure 25: Enable Data Monitoring \[VPR HS ENABLE\] Option—System Prompts and User Entries

Select VPR HealthShare Utilities Option: <span class="mark">ON \<Enter\></span> Enable Data Monitoring

> **WARNING:** Turning off data monitoring will cause the Regional Health Connect

server to become out of synch with VistA!!

\*\*\* Do NOT proceed unless directed to do so by Health Product Support

or VPR development staff!

ARE YOU SURE? NO// <span class="mark">YES</span>

ENABLE MONITORING: YES// <span class="mark">\<Enter\></span>

### Test/Audit VPR Functions \[VPR HS TESTER\] Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Test/Audit VPR Functions \[VPR HS TESTER\] menu shown in <u>Figure 26</u> contains five options for testing and monitoring the VPR data monitoring functions:

<span id="_Ref84612242" class="anchor"></span>Figure 26: Test/Audit VPR Functions \[VPR HS TESTER\] Menu

Select HealthShare Interface Manager Option: <span class="mark">TEST \<Enter\></span> Test/Audit VPR Functions

SDA Test SDA Extracts

AVPR SDA Upload List Monitor

LOG Data Upload List Log

ENC Encounter Transmission Task Monitor

PAT Inquire to Patient Subscriptions

Select Test/Audit VPR Functions Option:

<u>Table 87</u> and the sub-sections that follow describe the Test/Audit VPR Functions \[VPR HS TESTER\] menu options:

| Option Name                                                                            | Option Text                         | Description                                                                                                                           |
|----------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [VPR HS TEST](#test-sda-extracts-vpr-hs-test-option)                                   | Test SDA Extracts                   | This option runs the SDA data extracts for a selected patient and container to view onscreen.                                         |
| [VPR HS SDA MONITOR](#sda-upload-list-monitor-vpr-hs-sda-monitor-option)               | SDA Upload List Monitor             | This option monitors the AVPR list of upload requests for the RHC.                                                                |
| [VPR HS LOG](#data-upload-list-log-vpr-hs-log-option)                                  | Data Upload List Log                | This option enables saving and viewing of the upload list in ^XTMP for testing or debugging purposes, for up to 3 days.       |
| [VPR HS TASK MONITOR](#encounter-transmission-task-monitor-vpr-hs-task-monitor-option) | Encounter Transmission Task Monitor | This option checks the status of the task that collects encounters and related records from PCE and TIU for the AVPR upload list. |
| [VPR HS PATIENTS](#inquire-to-patient-subscriptions-vpr-hs-patients-option)            | Inquire to Patient Subscriptions    | This option displays information about a patient’s subscription status for data monitoring.                                           |

#### Test SDA Extracts \[VPR HS TEST\] Option

The Test SDA Extracts \[VPR HS TEST\] option runs the SDA data extracts for a selected patient and container, to view the records in SDA format as they were sent to the HealthShare. No data is actually sent to the ECR using this option, the results are only displayed on screen for testing and debugging purposes.

<span id="_Toc155864376" class="anchor"></span>Figure 27: Test SDA Extracts \[VPR HS TEST\] Option—System Prompts and User Entries

Select Test/Audit VPR Functions Option: <span class="mark">SDA \<Enter\></span> Test SDA Extracts

Select PATIENT NAME: <span class="mark">VPRPATIENT,ONE \<Enter\></span> 12-1-46 666000004 YES NSC VETERAN \*MULTIPLE BIRTH\* SMB SMB

Select CONTAINER: <span class="mark">PROBLEM</span>

Select SOURCE FILE: <span class="mark">\<Enter\></span>

Select START DATE: <span class="mark">\<Enter\></span>

Select TOTAL \#items: <span class="mark">\<Enter\></span>

DEVICE: HOME// <span class="mark">\<Enter\></span> Linux Telnet /SSh

\#Results: 1

Press \<return\> to continue or ^ to exit results ... <span class="mark">\<Enter\></span>

Result \#1

\<Problem\>

\<UpdatedOn\>2019-07-29T00:00:00\</UpdatedOn\>

\<Extension\>

\<IsExposureAO\>false\</IsExposureAO\>

\<IsExposureIR\>false\</IsExposureIR\>

\<IsExposurePG\>false\</IsExposurePG\>

\<IsExposureCV\>true\</IsExposureCV\>

\<Location\>

\<SDACodingStandard\>VA44\</SDACodingStandard\>

\<Extension\>

\<StopCode\>

\<SDACodingStandard\>AMIS\</SDACodingStandard\>

\<Code\>203\</Code\>

\<Description\>AUDIOLOGY\</Description\>

\</StopCode\>

\<Service\>MEDICINE\</Service\>

\<Specialty\>

\<SDACodingStandard\>VA45.7\</SDACodingStandard\>

\<Code\>11\</Code\>

\<Description\>INTERMEDIATE MED\</Description\>

Press \<return\> to continue or ^ to exit item ... <span class="mark">^</span>

Select CONTAINER: <span class="mark">\<Enter\></span>

Select PATIENT NAME:

#### SDA Upload List Monitor \[VPR HS SDA MONITOR\] Option

The SDA Upload List Monitor \[VPR HS SDA MONITOR\] option is duplicated on the VPR HS TESTER menu for the convenience of users testing VPR patches.

![](virtual-patient-record-vpr-developer-s-guide/041.png) REF: For a description of this option, see Section <u>5.6.1.2</u>, “<u>SDA Upload List Monitor \[VPR HS SDA MONITOR\] Option</u>.”

#### Data Upload List Log \[VPR HS LOG\] Option

The Data Upload List Log \[VPR HS LOG\] option enables VPR to save a copy of the AVPR upload list entries in ^XTMP(“VPRHS”) temporarily, for testing or debugging purposes. Entries are stored by date of activity, so a nightly Kernel job can remove data from the log after 3 days.

The log can also be viewed in this option, by date of activity, and optionally by patient.

<span id="_Toc155864377" class="anchor"></span>Figure 28: Data Upload List Log \[VPR HS LOG\] Option—System Prompts and User Entries

Select Test/Audit VPR Functions Option: <span class="mark">LOG \<Enter\></span> Data Upload List Log

Upload list logging is currently OFF

Would you like to turn it ON? NO// <span class="mark">Y \<Enter\></span> YES

SDA Test SDA Extracts

AVPR SDA Upload List Monitor

<span class="mark">LOG Data Upload List Log</span>

ENC Encounter Transmission Task Monitor

PAT Inquire to Patient Subscriptions

Select Test/Audit VPR Functions Option: <span class="mark">LOG \<Enter\></span> Data Upload List Log

Upload list logging is currently ON

Select log action: VIEW// <span class="mark">\<Enter\></span>

Select a date: Apr 16, 2021// <span class="mark">?</span>

Available date is Apr 16, 2021, or enter ^ to exit.

Select a date: Apr 16, 2021// <span class="mark">\<Enter\></span> (APR 16, 2021)

Starting sequence#: FIRST// <span class="mark">\<Enter\></span>

Select PATIENT NAME: <span class="mark">\<Enter\></span>

SEQ DFN Apr 16, 2021

--------------------------------------------------------------------------

5342 4 5000000103V528688^Problem^187;9000011^U^

Press \<return\> to continue ... <span class="mark">\<Enter\></span>

Select a date: Apr 16, 2021// <span class="mark">^</span>

Select log action: VIEW// <span class="mark">QUIT</span>

#### Encounter Transmission Task Monitor \[VPR HS TASK MONITOR\] Option

The Encounter Transmission Task Monitor \[VPR HS TASK MONITOR\] option is duplicated on the VPR HS TESTER menu for the convenience of users testing VPR patches. However, the action of re-queuing the task, if it has stopped, is *not* available when the option is accessed via the VPR HS TESTER menu.

![](virtual-patient-record-vpr-developer-s-guide/042.png) REF: For a description of this option, see Section <u>5.6.1.1</u>, “<u>Encounter Transmission Task Monitor \[VPR HS TASK MONITOR\] Option</u>.”

#### Inquire to Patient Subscriptions \[VPR HS PATIENTS\] Option

The Inquire to Patient Subscriptions \[VPR HS PATIENTS\] option displays information about a selected patient’s subscription status for HealthShare data monitoring.

<span id="_Toc155864378" class="anchor"></span>Figure 29: Inquire to Patient Subscriptions \[VPR HS PATIENTS\] Option—System Prompts and User Entries

Select Test/Audit VPR Functions Option: <span class="mark">PAT \<Enter\></span> Inquire to Patient Subscriptions

Select PATIENT NAME: <span class="mark">VPRPATIENT,TWO MEANS RD \<Enter\></span> 3-3-30 666000003 NO SC VETERAN ORANGE TEAM

VPRPATIENT,TWO MEANS RD is subscribed in HealthShare

DFN: 3

ICN: 5000000101V983844

\>\> Patient DIED on May 29, 2021@08:00

Select PATIENT NAME: <span class="mark">VPRPATIENT,THREE \<Enter\></span> 0-0-01 102000001P \*\*Pseudo SSN

\*\* YES SC VETERAN \*MULTIPLE BIRTH\* SMB SMB

VPRPATIENT,THREE is subscribed in HealthShare

DFN: 9

ICN: 5000000098V757329

Select PATIENT NAME: <span class="mark">NEWVPRPATIENT,RELEASE \<Enter\></span> 12-30-45 666000015 NO COLLATERAL

\*\*\* Patient Requires a Means Test \*\*\*

\*\*\* Please update \*\*\*

Enter \<RETURN\> to continue. <span class="mark">\<Enter\></span>

MEANS TEST REQUIRED

PATIENT REQUIRES A MEANS TEST

NEWVPRPATIENT,RELEASE is NOT subscribed in HealthShare

DFN: 15

ICN: NO MPI NODE

Select PATIENT NAME:

## Call To Populate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Call To Populate (CTP) is a utility created by the VPR team that can re-pull VistA patient records that already exist on the RHC server. It is used to update data records after national release of a VPR patch, which added extension properties or corrected a data extract problem.

![](virtual-patient-record-vpr-developer-s-guide/043.png) REF: This document describes the VistA CTP Utility, for more information on the Veterans Data Integration and Federation Enterprise Platform (VDIF-EP) CTP Utility, see the [*VDIF-EP Utilities User Guide* (vdif_ug_utilities.pdf)](https://github.com/department-of-veterans-affairs/vdif-ep-product/blob/product/master/env_depl_impl/vdif_ug/vdif_ug_utilities.pdf); located in the VDIF-EP GitHub repository.

### VPRZCTP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The VPRZCTP routine exists on each RHC server to support the CTP utility. It is in the VPRZ namespace as it is only for use by the RHC and is *not* exported to any VistA site. Routine mappings tell the RHC to look for VPRZ routines on its system rather than in VistA. Because the job started on the RHC, the results will accumulate in a global there instead of filling up a ^TMP or ^XTMP global in VistA.

VPRZCTP itself does *not* actually extract any data. It uses the VPR CONTAINER (#560.1) file and existing Entity file definitions to search for affected records, but it only executes the Query Routine. The resulting record identifiers are formatted like the strings used by the AVPR index and returned to the RHC for processing with the real-time updates.

Format

EN^VPRZCTP(start,stop,max,routine,type,id,format,number,dfn,result)

Input Parameters

All input parameters are *optional*; however, if the type input parameter is *not* defined then no data can be returned.

start: Date to start searching for records (default is all records).

stop: Date to stop searching for records (default is all records).

max: Maximum number of items to return per container (default is 9999).

routine: Name of a VPRZ routine to execute for a specialized search.

type: Name of the desired SDA Container(s) and optional source file number, separated by commas, each in the format:

Container name\_\[“;”\_VistA source file number\]id: Record identifier, in the format:

internal entry number\_“;”\_VistA source file numberformat: String indicating the type of results to return, as:

- “OPS”―Individual record identifier strings (default).
- “CNT”―A count of the records found by container.

number: Base number from which to start incrementing the sequence numbers in the results array (default is 0).

dfn: Pointer to the PATIENT (#2) file, or list of pointers as:

“~”\_pointer\_”~”\_pointer\_...\_”~”\_pointerresult: Closed array name for returning results, default is:

^PL.CTP(#) Global that accumulates on the RHC.

Output

This routine returns a list of record identifiers in the specified array, as well as indexes by patient and container. The total number of records returned can be found in the “Tot” node of the array.

Result(#): Record identifier string, formatted for use with AVPR index utility and indexed by:

Result(“DFN”, dfn, \#)Result(“DOMAIN”, dfn, type, \#)Result(“Tot”): Nodes containing counts of the records found by the query, in the form:

Result(“Tot”) total ^ updates ^ deletes ^ last subscript ^

error message, if any

Result(“Tot”, “U”) \# of records to be updated

Result(“Tot”, “D”) \# of records to be deleted

Result(“Tot”, type) \# of records in the container

Result(“Tot”, type, file#) \# of records in the container and source file

#### Examples

The following are some examples of running the VPRZCTP routine utilities to demonstrate how the RHC server calls it and the results returned:

![](virtual-patient-record-vpr-developer-s-guide/044.png) NOTE: This routine exists only on the RHC servers and *not* in any VistA site.

- <u>CTP by Domain</u>
- <u>CTP by Domain: CNT</u>
- <u>CTP by Patient</u>
- <u>CTP by ID</u>
- <u>CTP by Patch</u>

#### CTP by Domain

Running the CTP by Domain utility only truly requires the container name; however, due to the volume of data in VistA other filters, such as a date range, are *strongly recommended*.

![](virtual-patient-record-vpr-developer-s-guide/045.png) NOTE: Dates do *not* need to be passed in VA FileMan format. All input dates are validated using the VA FileMan %DT utility, so any format that passes this check is acceptable.

Any domain that relies on visits will also return any related Encounter records.

<span id="_Toc155864379" class="anchor"></span>Figure 30: CTP by Domain Utility―Sample Results

\><span class="mark">D EN^VPRZCTP(20210701,20211231,,,"Document",,,,,"RESULT") ZW RESULT</span>

RESULT(1)="5000000103V528688^Document^1709;8925^U^1862^4"

RESULT(2)="5000000103V528688^Encounter^1862;9000010^U^^4"

RESULT(3)="5000000098V757329^Document^1716;8925^U^1860^9"

RESULT(4)="5000000098V757329^Document^1706;8925^U^1860^9"

RESULT(5)="5000000098V757329^Encounter^1860;9000010^U^^9"

RESULT(6)="5000000129V929287^Document^1726;8925^U^^129"

RESULT(7)="5000000148V605820^Document^1707;8925^U^1861^229"

RESULT(8)="5000000148V605820^Encounter^1861;9000010^U^^229"

RESULT("DFN",4,1)=""

RESULT("DFN",4,2)=""

RESULT("DFN",9,3)=""

RESULT("DFN",9,4)=""

RESULT("DFN",9,5)=""

RESULT("DFN",129,6)=""

RESULT("DFN",229,7)=""

RESULT("DFN",229,8)=""

RESULT("DOMAIN",4,"Document",1)=""

RESULT("DOMAIN",4,"Encounter",2)=""

RESULT("DOMAIN",9,"Document",3)=""

RESULT("DOMAIN",9,"Document",4)=""

RESULT("DOMAIN",9,"Encounter",5)=""

RESULT("DOMAIN",129,"Document",6)=""

RESULT("DOMAIN",229,"Document",7)=""

RESULT("DOMAIN",229,"Encounter",8)=""

RESULT("Tot")="8^8^0^8^"

RESULT("Tot","D")=0

RESULT("Tot","Document")=5

RESULT("Tot","Document",8925)=5

RESULT("Tot","Encounter")=3

RESULT("Tot","Encounter",9000010)=3

RESULT("Tot","U")=8

\>

#### CTP by Domain: CNT

The “CNT” format of the <u>CTP by Domain</u> utility performs the same query as the regular <u>CTP by Domain</u> utility, but it only returns the index and total nodes to the RHC server. The “CNT” parameter simply tells CTP to only count the number of entries it finds that fit the criteria; it does *not* actually return all of the record ids or do the update. This is sometimes used first to get an estimate of how long it takes the actual <u>CTP by Domain</u> to complete at a given site.

<span id="_Toc155864380" class="anchor"></span>Figure 31: CTP by Domain: CNT Utility―Sample Results

\><span class="mark">D EN^VPRZCTP(20210701,20211231,,,"Document",,"CNT",,,"RESULT") ZW RESULT</span>

RESULT("DFN",4,1)=""

RESULT("DFN",4,2)=""

RESULT("DFN",9,3)=""

RESULT("DFN",9,4)=""

RESULT("DFN",9,5)=""

RESULT("DFN",129,6)=""

RESULT("DFN",229,7)=""

RESULT("DFN",229,8)=""

RESULT("DOMAIN",4,"Document",1)=""

RESULT("DOMAIN",4,"Encounter",2)=""

RESULT("DOMAIN",9,"Document",3)=""

RESULT("DOMAIN",9,"Document",4)=""

RESULT("DOMAIN",9,"Encounter",5)=""

RESULT("DOMAIN",129,"Document",6)=""

RESULT("DOMAIN",229,"Document",7)=""

RESULT("DOMAIN",229,"Encounter",8)=""

RESULT("Tot")="8^8^0^8^"

RESULT("Tot","D")=0

RESULT("Tot","Document")=5

RESULT("Tot","Document",8925)=5

RESULT("Tot","Encounter")=3

RESULT("Tot","Encounter",9000010)=3

RESULT("Tot","U")=8

\>

#### CTP by Patient

The CTP by Patient utility can be run for a single patient by passing the local PATIENT (#2) pointer in the dfn parameter. A finite list of patient DFNs can also be requested by passing in a string whose first character is the delimiter separating each dfn. For example: “~129~231~744”.

<span id="_Toc155864381" class="anchor"></span>Figure 32: CTP by Patient Utility―Sample Results

\><span class="mark">D EN^VPRZCTP(20210701,20211231,,,"Document,Problem",,,,9,"RESULT") ZW RESULT</span>

RESULT(1)="5000000098V757329^Document^1716;8925^U^1860^9"

RESULT(2)="5000000098V757329^Document^1706;8925^U^1860^9"

RESULT(3)="5000000098V757329^Problem^195;9000011^U^^9"

RESULT(4)="5000000098V757329^Problem^155;9000011^U^^9"

RESULT(5)="5000000098V757329^Encounter^1860;9000010^U^^9"

RESULT("DFN",9,1)=""

RESULT("DFN",9,2)=""

RESULT("DFN",9,3)=""

RESULT("DFN",9,4)=""

RESULT("DFN",9,5)=""

RESULT("DOMAIN",9,"Document",1)=""

RESULT("DOMAIN",9,"Document",2)=""

RESULT("DOMAIN",9,"Encounter",5)=""

RESULT("DOMAIN",9,"Problem",3)=""

RESULT("DOMAIN",9,"Problem",4)=""

RESULT("Tot")="5^5^0^5^"

RESULT("Tot","D")=0

RESULT("Tot","Document")=2

RESULT("Tot","Document",8925)=2

RESULT("Tot","Encounter")=1

RESULT("Tot","Encounter",9000010)=1

RESULT("Tot","Problem")=2

RESULT("Tot","Problem",9000011)=2

RESULT("Tot","U")=5

\>

#### CTP by ID

Use the CTP by ID utility to pass in a single record id. It is often used after an error has occurred. If the id parameter is passed, then the type and dfn parameters are also required.

<span id="_Toc155864382" class="anchor"></span>Figure 33: CTP by ID Utility―Sample Results

\><span class="mark">D EN^VPRZCTP(20210701,20211231,,,"Problem","195;9000011",,,9,"RESULT")</span>

\><span class="mark">ZW RESULT</span>

RESULT(1)="5000000098V757329^Problem^195;9000011^U^^9"

RESULT("DFN",9,1)=""

RESULT("DOMAIN",9,"Problem",1)=""

RESULT("Tot")="1^1^0^1^"

RESULT("Tot","D")=0

RESULT("Tot","Problem")=1

RESULT("Tot","Problem",9000011)=1

RESULT("Tot","U")=1

\>

#### CTP by Patch

Some containers, such as Documents, are very intensive to re-load; so, a special lookup routine can be written to target only those records directly affected by a patch. The CTP by Patch utility allows you to pass the CTP patch routine name into VPRZCTP. It should follow these constraints:

- Be named VPRZP##; where \## is the number of the corresponding VistA VPR patch; it will be loaded only on the RHC servers.
- Have a “CTP” line tag, that will be called from inside VPRZCTP.
- Support the search parameters for date range and patient that are available in the variables: VPRBDT, VPREDT, and VPRPT respectively.
- Support the type parameter, if multiple searches are performed; type is available in the VPRTYPE variable and can be whatever domain identifier needed by the routine, such as a container name or a line tag to execute.
- Can call the POST^VPRZCTP API for each record identified, to return the same results array.

<u>Figure 34</u> is an example of the CTP routine from patch VPR\*1\*20, to find documents in the TIU DOCUMENT (#8925) file affected by the patch.

<span id="_Ref107246425" class="anchor"></span>Figure 34: Sample CTP Routine―Finding Documents in the TIU DOCUMENT (#8925) File affected by the Patch

\><span class="mark">D EN^VPRZCTP(20210701,20211231,,"VPRZP20","TIU",,,,,"RESULT") ZW RESULT</span>

RESULT(1)="5000000098V757329^Document^1706;8925^U^1860^9^1706;TIU"

RESULT(2)="5000000098V757329^Document^1716;8925^U^1860^9^1716;TIU"

RESULT(3)="5000000098V757329^Encounter^1860;9000010^U^^9^1860"

RESULT(4)="5000000129V929287^Document^1726;8925^U^^129^1726;TIU"

RESULT(5)="5000000148V605820^Document^1707;8925^U^1861^229^1707;TIU"

RESULT(6)="5000000148V605820^Encounter^1861;9000010^U^^229^1861"

RESULT("DFN",9,1)=""

RESULT("DFN",9,2)=""

RESULT("DFN",9,3)=""

RESULT("DFN",129,4)=""

RESULT("DFN",229,5)=""

RESULT("DFN",229,6)=""

RESULT("DOMAIN",9,"Document",1)=""

RESULT("DOMAIN",9,"Document",2)=""

RESULT("DOMAIN",9,"Encounter",3)=""

RESULT("DOMAIN",129,"Document",4)=""

RESULT("DOMAIN",229,"Document",5)=""

RESULT("DOMAIN",229,"Encounter",6)=""

RESULT("Tot")="6^6^0^6^"

RESULT("Tot","D")=0

RESULT("Tot","TIU")=6

RESULT("Tot","U")=6

\>

[^1]: DDE is the name of the VA FileMan routine that contains the Entity utilities.