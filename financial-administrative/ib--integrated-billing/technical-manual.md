---
title: IB*2 Integrated Billing Version 2 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: archive
pkg_ns: IB
patch_ver: 2
patch_id: IB*2
group_key: "IB:IB:2"
file_numbers: 
  - 2
  - 4
  - 36
  - 49
  - 350
  - 351
  - 355
  - 356
  - 357
  - 365
  - 367
  - 399
security_keys: []
menu_options: 17
description: 
audience: 
keywords: 
  - class
  - even
  - insurance
  - billing
  - report
  - patient
  - claims
  - form
  - edit
  - bill
page_count: 0
word_count: 96325
section_count: 29
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=266"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Integrated Billing

  Version 2.0

  Technical Manual
---

![](ib-2-integrated-billing-version-2-technical-manual/001.png)

March 2023

Office of Information and Technology

Revision History

Initiated on 12/29/2004

<table>
<caption><p><span id="_Toc127633844" class="anchor"></span>Table : Parameters</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 52%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description (Patch # if applicable)</th>
<th><p>Project Manager</p>
<p>Technical Writer</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March 2023</td>
<td><p>Updated for patch IB*2.0*727</p>
<ul>
<li><p>Added IBCEMSRI to Routine List</p></li>
</ul></td>
<td>MCCF EDI TAS eBilling Development Team</td>
</tr>
<tr class="even">
<td>February 2023</td>
<td><p>Updated for patch IB*2.0*716</p>
<ul>
<li><p>Added IBINRPT,IBINUT1 TO Routine list</p></li>
</ul>
<p>Technical Writer QA</p>
<ul>
<li><p>Minor grammatical/formatting changes</p></li>
<li><p>Added SACC to Acronym table</p></li>
</ul></td>
<td>CCDSO IB AR Development Team</td>
</tr>
<tr class="odd">
<td>February 2023</td>
<td><p>Updated for patch IB*2.0*737</p>
<ul>
<li><p>Removed Most Popular Payer from Routines and Options</p></li>
<li><p>Removed Non-Verified Extract from Routines</p></li>
<li><p>Removed SSVI from Acronyms table</p></li>
<li><p>Added multiple entries to the Acronyms table</p></li>
<li><p>Changed references from DBIA to ICR except in actual ICR names</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="even">
<td>September 2022</td>
<td><p>Updated for patch IB*2.0*718</p>
<ul>
<li><p>Added IBCE837N, IBCE837P to Routine list</p></li>
</ul></td>
<td>MCCF EDI TAS eBilling Development Team</td>
</tr>
<tr class="odd">
<td>August 2022</td>
<td><p>Updated for patch IB*2.0*713</p>
<ul>
<li><p>Options: Removed IBCN LIST INACTIVE INS W/PAT</p></li>
<li><p>Routine List: Removed IBCOC</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="even">
<td>May 2022</td>
<td><p>Updated for patch IB*2.0*702</p>
<ul>
<li><p>Added Security key IBCNE EICD REQUEST</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="odd">
<td>January 2022</td>
<td><p>Updated for patch IB*2.0*709</p>
<ul>
<li><p>Added IBOMHC to the Routine List</p></li>
</ul></td>
<td>CCDSO IB AR Development Team</td>
</tr>
<tr class="even">
<td>December 2021</td>
<td><p>Updated for patch IB*2.0*687</p>
<ul>
<li><p>Added to the Callable Routine section (related to IBCNINSL &amp; IBCNINSU)</p></li>
<li><p>Routine List: Removed IBCNERP0; Added/modified IBCNERPB, IBCNERPC, IBCNERPD, IBCNINS, IBCNIUF, IBCNIUH1, IBCNIUHL, IBCNIUK, IBCNIUR1, IBCNIUR2, IBCNES4</p></li>
<li><p>Added file INTERFACILITY INSURANCE UPDATE (#365.19)</p></li>
<li><p>Updated File Flow Chart</p></li>
<li><p>Options: Removed IBCNE IIV BATCH PROCESS, IBCNE IIV PAYER LINK REPORT; Added IBCN EINSURANCE NIGHT PROCESS, IBCNE INS COMPANY LINK REPORT, IBCNE PAYER LINK REPORT, IBCNIU INTERFACILITY INS UPDT</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="odd">
<td>August 2021</td>
<td><p>Updated for patch IB*2.0*650:</p>
<ul>
<li><p>Added IBCE277S, IBCE837S, IBCE837T to Routine list</p></li>
</ul></td>
<td>MCCF EDI TAS eBilling Development Team</td>
</tr>
<tr class="even">
<td>August 2021</td>
<td><p>Updated for patch IB*2.0*706:</p>
<ul>
<li><p>Updated the IB MT NIGHT COMP Option Description</p></li>
</ul></td>
<td>CCDSO IB AR Development Team</td>
</tr>
<tr class="odd">
<td>August 2021</td>
<td><p>Update for patch IB*2.0*701</p>
<ul>
<li><p>Added new option to the Exported Options section on page 178 with Former OTH Patient Eligibility Change Report [IB OTH FSM ELIG. CHANGE REPORT]</p></li>
</ul></td>
<td>LIBERTY ITS</td>
</tr>
<tr class="even">
<td>August 2021</td>
<td><p>Updated for patch IB*2.0*676</p>
<ul>
<li><p>Added new HL7 interface to Cerner</p>
<ul>
<li><blockquote>
<p>HL Logical Link IBARXCVDF</p>
</blockquote></li>
</ul></li>
<li><p>The following routines were added:</p>
<ul>
<li><blockquote>
<p>IBARXCBK</p>
</blockquote></li>
<li><blockquote>
<p>IBARXCSH</p>
</blockquote></li>
<li><blockquote>
<p>IBARXCHL</p>
</blockquote></li>
<li><blockquote>
<p>IBARXCRC</p>
</blockquote></li>
<li><blockquote>
<p>IBARXCR2</p>
</blockquote></li>
<li><blockquote>
<p>IBARXCQR</p>
</blockquote></li>
<li><blockquote>
<p>IBARXCRD</p>
</blockquote></li>
<li><blockquote>
<p>IBARXCFL</p>
</blockquote></li>
</ul></li>
<li><p>The following routines have been modified:</p>
<ul>
<li><blockquote>
<p>IBARX</p>
</blockquote></li>
<li><blockquote>
<p>IBARXMU</p>
</blockquote></li>
<li><blockquote>
<p>IBARXMN</p>
</blockquote></li>
<li><blockquote>
<p>IBARXMA</p>
</blockquote></li>
<li><blockquote>
<p>IBARXMC</p>
</blockquote></li>
<li><blockquote>
<p>IBARXMB</p>
</blockquote></li>
<li><blockquote>
<p>IBARXMP</p>
</blockquote></li>
<li><blockquote>
<p>IBARXMQ</p>
</blockquote></li>
</ul></li>
<li><p>New HLO APPLICATION REGISTRY ENTRIES:</p>
<ul>
<li><blockquote>
<p>IBARXC-QRY</p>
</blockquote></li>
<li><blockquote>
<p>IBARXC-QRYRESP</p>
</blockquote></li>
<li><blockquote>
<p>IBARXC-SEND</p>
</blockquote></li>
<li><blockquote>
<p>IBARXC-RECV</p>
</blockquote></li>
</ul></li>
</ul></td>
<td>Cerner Pharmacy CoPay Team</td>
</tr>
<tr class="odd">
<td>June 2021</td>
<td><p>Updated for patch IB*2.0*703:</p>
<ul>
<li><p>Added routine IBECEAU6</p></li>
</ul></td>
<td>CCDSO IB AR Development Team</td>
</tr>
<tr class="even">
<td>April 2021</td>
<td><p>Updated for patch IB*2.0*688</p>
<ul>
<li><p>Added the routine IBEFSMUT to the list of routines in section “Routine List with Descriptions”</p></li>
</ul></td>
<td>LIBERTY ITS</td>
</tr>
<tr class="odd">
<td>April 2021</td>
<td><p>Updated for patch IB*2.0*668</p>
<ul>
<li><p>Removed references to SSVI routines, files, and options as they were deleted with IB*2.0*668. Specifically, files #366, #366.1, #366.2, and option “IBCN INTERFACILITY INS UPDATE”.</p></li>
<li><p>Added routine IBCNINSU</p></li>
<li><p>Added additional references to ‘VA Directive 6402’</p></li>
<li><p>Removed references to pre / post routines related to IBY432* and IBY528* from the routine sections.</p></li>
<li><p>Updated description for the Payer file #365.12 and for the input template “IBCNE GENERAL PARAMETER EDIT”.</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="even">
<td>December 2020</td>
<td><p>Updated for patch IB*2.0*638</p>
<ul>
<li><p>Added the routine IBTASFAC to the list of routines.</p></li>
</ul></td>
<td>MCCF EDI TAS ePharmacy Development Team</td>
</tr>
<tr class="odd">
<td>November 2020</td>
<td><p>Updated for patch IB*2.0*641:</p>
<ul>
<li><p>Added IBCERPN to Routine list</p></li>
<li><p>Updated List of Options</p></li>
</ul></td>
<td>MCCF EDI TAS eBilling Development Team</td>
</tr>
<tr class="even">
<td>November 2020</td>
<td><p>Updated for patch IB*2.0*664</p>
<ul>
<li><p>Added IBCNERPM, IBCNINSL and IBCNRDV1 to the Routine List</p></li>
<li><p>Two additions were made to the List Templates section of this document: IBCN RDV SELECTOR and IBCN RDV POL SELECTED</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="odd">
<td>August 2020</td>
<td><p>Updated for patch IB*2.0*677</p>
<ul>
<li><p>Updated External Relations, Section 3M to add new Subscribing IA, #7182</p></li>
</ul></td>
<td>CC IBAR Development Team</td>
</tr>
<tr class="even">
<td>June 2020</td>
<td><p>Updated for patch IB*2.0*675</p>
<ul>
<li><p>Updated IBUC VISIT MAINT in the Options List with IBUC VISIT MAINT OVERRIDE</p></li>
</ul></td>
<td>CC IBAR Development Team</td>
</tr>
<tr class="odd">
<td>May 2020</td>
<td><p>Updated for patch IB*2.0*669</p>
<ul>
<li><p>Added IBECEA39 to Routine List</p></li>
</ul></td>
<td>CC IBAR Development Team</td>
</tr>
<tr class="even">
<td>March 2020</td>
<td><p>Updated for patch IB*2.0*671</p>
<ul>
<li><p>Added DBIA #5158 to External Relations</p></li>
</ul></td>
<td>CC IBAR Development Team</td>
</tr>
<tr class="odd">
<td>March 2020</td>
<td><p>Updated for patch IB*2.0*663</p>
<ul>
<li><p>Added IBECEA36 to Routine List</p></li>
<li><p>Added IBECEA37 to Routine List</p></li>
<li><p>Added IBECEA38 to Routine List</p></li>
<li><p>Added IBUCMM to Routine List</p></li>
<li><p>Added IBUCMM1 to Routine List</p></li>
<li><p>Added IBUCSP to Routine List</p></li>
<li><p>Added IBUCSP2 to Routine List</p></li>
<li><p>Added IBUCVM to Routine List</p></li>
<li><p>Added new file 351.82 (IB UC VISIT TRACKING FILE) to the Files and Flow Chart sections</p></li>
<li><p>Added IBUC MAIN MENU to Options List</p></li>
<li><p>Added IBUC MULTI FAC COPAY PULL REQ to Options List</p></li>
<li><p>Added IBUC MULTI FAC COPAY SYNCH to Options without Parents List</p></li>
<li><p>Added IBUC VISIT INQUIRE to Options List</p></li>
<li><p>Added IBUC VISIT MAINT to Options List</p></li>
<li><p>Added IBUC VISIT REPORT to Options List</p></li>
<li><p>Added DBIA #5158 to External Relations</p></li>
</ul></td>
<td>CC IBAR Development Team</td>
</tr>
<tr class="even">
<td>January 2020</td>
<td><p>Updated for patch IB*2.0*623</p>
<ul>
<li><p>Added IBCE837H to Routine List</p></li>
<li><p>Added IBCE837I to Routine List</p></li>
<li><p>Added IBCE837K to Routine List</p></li>
<li><p>Added IBTAS EBILLING RPCS to Options List</p></li>
</ul></td>
<td>MCCF EDI TAS eBilling Development Team</td>
</tr>
<tr class="odd">
<td>December 2019</td>
<td><p>Updated for patch IB*2.0*652.</p>
<ul>
<li><p>Added new security key – ‘IBCN PT POLICY COMNT DELETE’</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="even">
<td>October 2019</td>
<td><p>Updated for patch IB*2.0*631:</p>
<ul>
<li><p>Added IBCNERTU to Routine List.</p></li>
<li><p>Added new file 355.36 (CREATION TO PROCESSING TRACKING) to Files and Flow Chart sections.</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="odd">
<td>August 2019</td>
<td><p>Updated for patch IB*2.0*646:</p>
<ul>
<li><p>Added IBECEA35 to Routine List.</p></li>
<li><p>Updated IBECEA36 in the Routine List.</p></li>
<li><p>Added Community Care to the Glossary.</p></li>
<li><p>Added Urgent Care to the Glossary.</p></li>
</ul></td>
<td>CC IBAR Development Team</td>
</tr>
<tr class="even">
<td>April 2019</td>
<td><p>Updated for patch IB*2.0*608:</p>
<ul>
<li><p>Added IBCU75, IBJPS7 and IBJPS8 to Routine List.</p></li>
<li><p>Added new file 399.6 (CMN FORM TYPES) to Files, File Flow Chart and Security sections.</p></li>
<li><p>Added List Templates ‘IBJP IB NON-MCCF RATE TYPES’ and ‘IBJPS CMN CPTS’.</p></li>
<li><p>Added ‘CMN’, ‘MCCF’ and ‘Non-MCCF’ to Glossary section.</p></li>
</ul></td>
<td>MCCF EDI TAS eBilling Development Team</td>
</tr>
<tr class="odd">
<td>March 2019</td>
<td><p>Updated for patch IB*2.0*602:</p>
<ul>
<li><p>Add “Expire Group Plan” [IBCN EXPIRE GROUP SUBSCRIBERS] option</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="even">
<td>January 2019</td>
<td><p>Updated for patch IB*2.0*621</p>
<ul>
<li><p>Corrected tag FTF^IBCNEUT7 to FTFIC^IBCNEUT7</p></li>
<li><p>Added IBCNEHL6 to Routine List</p></li>
<li><p>Added IBCNEHL7 to Routine List</p></li>
<li><p>Added IBCNEMS1 to Routine List</p></li>
<li><p>Added IBCNERTC to Routine List</p></li>
<li><p>Added IBCNETST to Routine List</p></li>
<li><p>Added EIV EICD TRACKING File to File List</p></li>
<li><p>Updated File Flow Chart</p></li>
</ul></td>
<td>MCCF EDI TAS eInsurance Development Team</td>
</tr>
<tr class="odd">
<td>October 2018</td>
<td><p>Updated for patch IB*2.0*592</p>
<ul>
<li><p>Added IBCEF12 and IBCNSI to routine list</p></li>
<li><p>Added List Templates that were modified for IB*2.0*592, but already existed, IBCE IBSCO ID MAINT, IBCE PRVPRV MAINT, IBCE VIEW PREV TRANS1, IBCE VIEW PREV TRANS2, and IBCNS INSURANCE COMPANY</p></li>
<li><p>Added new List Template, IBCNSC INSURANCE CO ADDRESSES</p></li>
<li><p>Updated File Flow Cart for new pointer field in 399</p></li>
</ul></td>
<td>MCCF EDI TAS eBilling Development Team</td>
</tr>
<tr class="even">
<td>October 2018</td>
<td><p>Updated for patch IB*2.0*614:</p>
<ul>
<li><p>Added new routine IBAMTS3 to the Routine List with Descriptions section on page 21</p></li>
</ul></td>
<td><p>Suicide High Risk Patient Enhancements (SHRPE) Development Team</p>
<p>L. B. (PM)</p>
<p>D. K. (Tech Writer)</p></td>
</tr>
<tr class="odd">
<td>August 2018</td>
<td><p>Updated for patch IB*2.0*591</p>
<ul>
<li><p>Added IBCBB14 to Routine List</p></li>
</ul></td>
<td>MCCF EDI TAS ePharmacy Development Team</td>
</tr>
<tr class="even">
<td>May 2018</td>
<td><p>Updated for patch IB*2*568</p>
<ul>
<li><p>Add new Security Key IB PARAMETER EDIT to several menu options</p></li>
<li><p>Updated list of options</p></li>
</ul></td>
<td><p>A. I. (HAPE EDI Revenue Enhancements)</p>
<p>N. F.</p></td>
</tr>
<tr class="odd">
<td>January 2018</td>
<td><p>Updated for patch IB*2.0*585:</p>
<ul>
<li><p>Updated file #355.1 description on page 67 to include a new pointer field named MASTER TYPE OF PLAN.</p></li>
<li><p>Added a new file #355.99 named MASTER TYPE OF PLAN on page 71 to store relevant coding system data to be associated to terms in the TYPE OF PLAN file #355.1.</p></li>
<li><p>Updated the File Flow Chart with the MASTER TYPE OF PLAN file and pointer on page 127.</p></li>
<li><p>Updated the Options Without Parents section on page 147 with the new Master Type of Plan Association [IBMTOP ASSN] and Master Type of Plan Report [IB MASTER TYPE OF PLAN RPT].</p></li>
</ul></td>
<td>CTT / DM NDS Development Team</td>
</tr>
<tr class="even">
<td>October 2017</td>
<td><p>Updated for patch IB*2.0*577</p>
<ul>
<li><p>Added IBCERP7 to Routine list</p></li>
<li><p>Updated List of Options</p></li>
<li><p>Updated Callable Routines table.</p></li>
<li><p>File List with Descriptions with the 277EDI ID NUMBER Sub-File [#36.017]</p></li>
</ul></td>
<td>FY16 MCCF eBilling Development Team</td>
</tr>
<tr class="odd">
<td>August 2016</td>
<td><p>Updated for patch IB*2.0*549</p>
<ul>
<li><p>Added IBCMDT*, IBCNCH*, IBCNILK, IBCNSU4 to Routine list</p></li>
<li><p>Updated List Templates table</p></li>
<li><p>Updated Exported Options table</p></li>
<li><p>Updated Callable Routines table</p></li>
<li><p>Added Registration integration agreement in the External Relations section</p></li>
</ul></td>
<td>FY15 MCCF eInsurance Development Team</td>
</tr>
<tr class="even">
<td>August 2016</td>
<td><p>Updated for patch IB*2.0*517 (FY15), HCSR Request for Review and Response Transaction (278x217) (278x215):</p>
<ul>
<li><p>Added routines to the Routine List and Descriptions section (p. 34, 48, 49, 53-54)</p></li>
<li><p>Added files to the File List with Descriptions section (72-73, 84)</p></li>
<li><p>Added templates to the List Templates section (p. 99, 101-102)</p></li>
<li><p>File Flow Chart (p. 118, 124-126, 133-134)</p></li>
<li><p>Added new options to the Exported Options section (p. 152, 183)</p></li>
<li><p>Glossary (p. 210)</p></li>
</ul></td>
<td><p>J.S</p>
<p>Harris Team</p></td>
</tr>
<tr class="odd">
<td>August 2016</td>
<td><p>Updated the following sections for patch IB*2.0*547:</p>
<ul>
<li><p>Callable Routines (p.19)</p></li>
<li><p>Routine List Descriptions (pp.27,48,53)</p></li>
<li><p>File List with Descriptions (pp.70,91)</p></li>
<li><p>List Templates (p.101-102)</p></li>
<li><p>File Flow Charts (pp.123,137)</p></li>
<li><p>Exported Options (pp152,181)</p></li>
<li><p>External Relations (p.197)</p></li>
<li><p>Security (p.206)</p></li>
</ul></td>
<td>FY15 MCCF eBilling Development Team.</td>
</tr>
<tr class="even">
<td>August 2016</td>
<td><p>Updated for patch IB*2.0*562</p>
<ul>
<li><p>Add new option IB MT FIX/DISCH SPECIAL CASE (p. 146)</p></li>
</ul></td>
<td><p>T. D.</p>
<p>T. D.</p></td>
</tr>
<tr class="odd">
<td>August 2016</td>
<td><p>Updated for patch IB#2.0*550</p>
<ul>
<li><p>Added new routines IBNCPDRA</p></li>
</ul>
<p>and IBNCPDRB (p.48)</p>
<ul>
<li><p>Added to Menu Diagram IBCNR ROI</p></li>
<li><p>Expiration Report (p.152)</p></li>
<li><p>Added to External Relations</p></li>
<li><p>CMOP; DBIA 6243 &amp; 6244 (p.170)</p></li>
<li><p>ECME; DBIA 6243 &amp; 6244 (p.171)</p></li>
<li><p>O.P.; DBIA 6243, 6244 &amp; 6250 (p.173)</p></li>
</ul></td>
<td><p>T.T.</p>
<p>T.R.</p></td>
</tr>
<tr class="even">
<td>June 2016</td>
<td><p>Updated for patch IB*2.0*529</p>
<ul>
<li><p>Add EDI TRANSMISSION BATCH (#364.1) to the File Protection section</p></li>
</ul>
<p>Updated for patch IB*2.0*530</p>
<ul>
<li><p>Add new routines IBJTAD, IBJTEP, IBJTEP1, and IBJTPE</p></li>
<li><p>Add new List Templates IBJT 835 EEOB PRINT, IBJT ADDITIONAL 835 DATA, and IBJT ERA 835 INFORMATION</p></li>
</ul></td>
<td><p>T.T.</p>
<p>V.D.</p></td>
</tr>
<tr class="odd">
<td>February 2016</td>
<td><p>Updated for patch IB*2.0*525 and IB*2.0*528.</p>
<ul>
<li><p>Added new routines to support SSVI, and screen updates for eIV.</p></li>
<li><p>Add new file definitions:</p>
<ul>
<li><blockquote>
<p>IB SSVI PIN/HL7 PIVOT (#366)</p>
</blockquote></li>
<li><blockquote>
<p>IB INSURANCE INCONSISTENT DATA (#366.1)</p>
</blockquote></li>
<li><blockquote>
<p>IB INSURANCE CONSISTENCY ELEMENTS (#366.2)</p>
</blockquote></li>
</ul></li>
<li><p>Added new reports IBCN GRP PLAN FILES RPT, IBCN HPID CLAIM RPT, IBCN INS RPTS, IBCN INTERFACILITY INS UPDATE, IBCN USER EDIT RPT, and IBCNE HL7 RESPONSE REPORT to Exported Options.</p></li>
</ul></td>
<td><p>T.T.</p>
<p>J.P.</p></td>
</tr>
<tr class="even">
<td>February 2016</td>
<td><p>Updated for patch IB*2.0*534</p>
<ul>
<li><p>Add new routine IBNCPEV3</p></li>
<li><p>Add new database definition IB NCPDP NON-BILLABLE REASONS (#366.17)</p></li>
</ul></td>
<td><p>T.T.</p>
<p>V.D.</p></td>
</tr>
<tr class="odd">
<td>January 2016</td>
<td><p>Updated for patch IB*2.0*560:</p>
<ul>
<li><p>Added note to Global File Description for ^DGRO(391.23 (p. 87).</p></li>
</ul></td>
<td><p>A. S.</p>
<p>T. D.</p></td>
</tr>
<tr class="even">
<td>May 2015</td>
<td><p>Updated for patch IB*2.0*517 (FY13), HCSR Request for Review and Response Transactions (278x217) updates:</p>
<ul>
<li><p>Added routines to the Routine List and Descriptions section</p></li>
<li><p>Added files to the File List with Descriptions section</p></li>
<li><p>Added templates to the List Templates section</p></li>
<li><p>Added templates to the Input Templates section</p></li>
<li><p>Added files to the File Flow Chart section</p></li>
<li><p>Added new options to the Exported Options section</p></li>
<li><p>Added new entries to the Glossary section</p></li>
</ul></td>
<td><p>M.H</p>
<p>FirstView Team</p></td>
</tr>
<tr class="odd">
<td>September 2015</td>
<td><p>Updated for patch IB*2.0*522, ICD-10 PTF Modifications:</p>
<ul>
<li><p>Updated Registration integration agreement in the External Relations section (p.174).</p></li>
</ul></td>
<td><p>T.B.</p>
<p>K.R.</p></td>
</tr>
<tr class="even">
<td>April 2015</td>
<td><p>Updated for patch IB*2.0*516:</p>
<ul>
<li><p>Added IBVCB, IBVCB1, and IBVCB2 to Routine List for View Cancelled Bill Report (p.54).</p></li>
<li><p>Updated List Templates (p.95).</p></li>
<li><p>Added IB VIEW CANCEL BILL to Exported Options (p.142).</p></li>
<li><p>Deleted IBCN INS BILL PROV FLAG RPT from Exported Options (p.148).</p></li>
</ul></td>
<td><p>M.H.</p>
<p>FirstView Team</p></td>
</tr>
<tr class="odd">
<td>November 2014</td>
<td><p>Updated for patch IB*2.0*519:</p>
<ul>
<li><p>Added routines to Routine section (pages 13, 19, 32)</p></li>
<li><p>Updated File List in Files section to include new files (pages 86)</p></li>
<li><p>Updated File Flow Chart in Files section (pages 108, 112, 126)</p></li>
<li><p>Updated Exported Options section to include new option (page 131)</p></li>
<li><p>Updated External Relations with new DBIA (page 170)</p></li>
<li><p>Updated Security section to include new files (pages 182-183)</p></li>
<li><p>Updated Glossary section to include new acronyms (pages 186-187)</p></li>
</ul></td>
<td><p>M.H.</p>
<p>FirstView Team</p></td>
</tr>
<tr class="even">
<td>September 2014</td>
<td><p>Patch IB*2.0*461, ICD-10 Class 1 Remediation updates:</p>
<ul>
<li><p>Updated for ICD-10: p. 179</p></li>
<li><p>Added ICD-10 text to Glossary: p. 213</p></li>
</ul></td>
<td><p>VA PMs: K.T.</p>
<p>HP PM: M.K.</p>
<p>C.H. / B.T. / L.R.</p></td>
</tr>
<tr class="odd">
<td>5/22/2014</td>
<td><p>Updated for patch IB*2.0*506:</p>
<ul>
<li><p>Pages 64, 94, 111, 112, 121-124, and 181</p></li>
</ul></td>
<td><p>M.H.</p>
<p>FirstView Team</p></td>
</tr>
<tr class="even">
<td>1/29/14</td>
<td><p>Updated for patch IB*2.0*497:</p>
<ul>
<li><p>Formatting changes (pages 3, 18, 66,107)</p></li>
<li><p>Updated footer</p></li>
<li><p>Routines added to Routine Section (pages 31-33, 46)</p></li>
<li><p>Files added to Files section (pages 79-82)</p></li>
<li><p>Added Templates Section (page 94)</p></li>
<li><p>Files added to File Flow Chart section (pages 121-124)</p></li>
<li><p>Options added to Exported Options section (pages 149-150)</p></li>
<li><p>DBIA added to External relations section (page 169)</p></li>
</ul></td>
<td><p>M.H.</p>
<p>FirstView Team</p></td>
</tr>
<tr class="odd">
<td>3/26/2013</td>
<td><ul>
<li><p>Updated cover page.</p></li>
<li><p>Added blank page (p.54) for double-sided copying.</p></li>
<li><p>Corrected typo on p. 86.</p></li>
<li><p>Updated for patch IB*2.0*458: Added new routines on pp. 37, 50, and 52/53; new file added to pp. 68 and 113; new options added to pg. 133 and 148.</p></li>
</ul></td>
<td><p>K.N.</p>
<p>K.V.</p></td>
</tr>
<tr class="even">
<td>3/26/2013</td>
<td><p>Updated for patch IB*2.0*457:</p>
<ul>
<li><p>New routines added to p. 32</p></li>
<li><p>New files added to p. 64 and 110</p></li>
<li><p>New input template added to p. 92</p></li>
<li><p>New options added to p. 125 and 146</p></li>
</ul></td>
<td><p>K.N.</p>
<p>K.V.</p></td>
</tr>
<tr class="odd">
<td>July 2012</td>
<td>Updated for patch IB*2.0*476</td>
<td><p>M.R.</p>
<p>S.R.</p></td>
</tr>
<tr class="even">
<td>March 2012</td>
<td>Updated to include ePharmacy Phase 6 (IB*2*452)</td>
<td><p>S.S.</p>
<p>E.G. / B.A.</p></td>
</tr>
<tr class="odd">
<td>March 2012</td>
<td>Updated up to and including eClaims 5010 changes added (IB*2.0*447)</td>
<td><p>S.S.</p>
<p>B.I.</p></td>
</tr>
<tr class="even">
<td>Dec 2011</td>
<td>ePayments 5010 module changes added (IB*2*431 and IB*2*451)</td>
<td><p>S.S.</p>
<p>P.H. / B.A.</p></td>
</tr>
<tr class="odd">
<td>Nov 2011</td>
<td>Updated for Patch IB*2*432</td>
<td><p>S.S.</p>
<p>B.A.</p></td>
</tr>
<tr class="even">
<td>8/19/2011</td>
<td><p>Updated for patch IB*2*449, replaced Menu Diagram with statement.</p>
<ul>
<li><p>Technical writer review—formatting and convert to Section 508 compliant PDF.</p></li>
</ul></td>
<td><p>C.M.</p>
<p>E.Z. / S.S</p></td>
</tr>
<tr class="odd">
<td>June 2009</td>
<td>Updated for patch IB*2.0*399</td>
<td><p>A.S. / T.H.</p>
<p>M.E.G.</p></td>
</tr>
<tr class="even">
<td>June 2008</td>
<td>Updated for patch IB*2.0*389</td>
<td><p>A.S. / T.H.</p>
<p>M.E.G.</p></td>
</tr>
<tr class="odd">
<td>12/29/2004</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td>M.E.G.</td>
</tr>
<tr class="even">
<td>12/29/2004</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td>M.E.G</td>
</tr>
</tbody>
</table>

<span id="_Toc127633844" class="anchor"></span>Table : Parameters

Preface

This is the technical manual for the Integrated Billing (IB) software package. It is designed to assist Information Resources Management (IRM) personnel in operation and maintenance of the package.

For information regarding use of this software, please refer to the Integrated Billing User Manual. For further information on installation and maintenance of this package, Release Notes and an Installation Guide are provided. A Package Security Guide is also provided which addresses security requirements for the package.

Table of Contents

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Orientation](#orientation)
  - [Note to Users with Qume Terminals](#note-to-users-with-qume-terminals)
  - [Symbols](#symbols)
- [General Information](#general-information)
  - [Namespace Conventions](#namespace-conventions)
  - [Integrity Checker](#integrity-checker)
  - [SACC Exemptions / Non-Standard Code](#sacc-exemptions-non-standard-code)
  - [Resource Requirements](#resource-requirements)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementing Claims Tracking](#implementing-claims-tracking)
  - [Implementing Encounter Forms](#implementing-encounter-forms)
  - [Implementing Insurance Data Capture](#implementing-insurance-data-capture)
    - [Prior to installation](#prior-to-installation)
    - [After Installation](#after-installation)
  - [Implementing Patient Billing](#implementing-patient-billing)
  - [Implementing Third Party Billing](#implementing-third-party-billing)
- [Routines](#routines)
  - [Routines to Map](#routines-to-map)
  - [Obsolete Routines](#obsolete-routines)
  - [Callable Routine](#callable-routine)
  - [Routine List with Descriptions](#routine-list-with-descriptions)
  - [DGCR\ to IB\ Namespace Map](#dgcr-to-ib-namespace-map)
- [Files](#files)
  - [Globals to Journal](#globals-to-journal)
  - [File List with Descriptions](#file-list-with-descriptions)
  - [Templates](#templates)
    - [List Templates](#list-templates)
    - [Input Templates](#input-templates)
    - [Sort Templates](#sort-templates)
    - [Print Templates](#print-templates)
  - [File Flow Chart](#file-flow-chart)
- [<span id="Toc129022440" class="anchor"></span>Exported Options](#span-idtoc129022440-classanchorspanexported-options)
  - [Menu Diagram](#menu-diagram)
  - [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
  - [Expected Disk Space Recovery from Purging](#expected-disk-space-recovery-from-purging)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [How to Generate online Documentation](#how-to-generate-online-documentation)
  - [%Index](#index)
  - [Inquire (Option File)](#inquire-option-file)
  - [Print Option File](#print-option-file)
  - [List File Attributes](#list-file-attributes)
- [Security](#security)
  - [File Protection](#file-protection)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
This release of Integrated Billing (IB) version 2.0 introduces fundamental changes to the way Medical Care Cost Recovery (MCCR) related tasks are performed. This software introduces three new modules:
- Claims Tracking
- Encounter Form Utilities
- Insurance Data Capture
There are also significant enhancements to the two previous modules, Patient Billing and Third-Party Billing. IB has moved from a package with the sole purpose of identifying billable episodes of care and creating bills to a package that is responsible for the whole billing process through the passing of charges to Accounts Receivable (AR). IB v2.0 has added functionality to assist in:
- Capturing patient data
- Tracking potentially billable episodes of care
- Completing Utilization Review (UR) tasks
- Capturing more complete insurance information.
IB v2.0 has been targeted for a much wider audience than previous versions.
- The Encounter Form Utilities module is used by Medical Administration Service (MAS) Automated Data Processing Applications Coordinator (ADPAC) or clinic supervisors to create and print clinic-specific forms. Physicians use these forms to consequently provide input into form creation.
- The Claims Tracking module will be used by UR personnel within MCCR and Quality Management (QM) to track episodes of care, do pre-certifications, do continued stay reviews, and complete other UR tasks.
- Insurance verifiers use the Insurance Data Capture module to collect and store patient and insurance carrier-specific data.
- The billing clerks see substantial changes with the enhancements provided in the Patient Billing and Third-Party Billing modules.
- IB version 2.0 is highly integrated with other Decentralized Hospital Computer Program (DHCP) packages.
- Patient Information Management System (PIMS) is a feeder of patient demographic and eligibility data to IB. PIMS also provides information to Claims Tracking, Third Party Billing, and Patient Billing on each billable episode of care, both inpatient and outpatient.
- IB passes bills and / or charges to Accounts Receivable for the purpose of follow-up and collection.
- Prescription information is passed from Outpatient Pharmacy to Patient Billing for the purpose of billing Pharmacy co-payments.
- Prescription refills are passed through Claims Tracking to Third Party Billing to be billed using the Automated Biller.
- The Encounter Form Utilities print data on the forms from the Allergy, PIMS, and Problem List packages. The Print Manager, included with the Encounter Form Utilities, will also print out Health Summaries as well as documents from the Outpatient Pharmacy and PIMS packages.
- Means Test billing data may be transmitted between facilities using the Patient Data Exchange (PDX) v1.5 package. This may assist sites with the preparation of bills for inpatients who transfer between facilities.
- Prosthetics information is passed to Claims Tracking and Third-Party Billing.
The new functionality seen in this software is the direct result of input and feedback received from field users. Task groups made up of representatives from the field were created under the auspices of the MCCR Systems Committee and MCCR EP. These groups had meetings and / or conference calls with the developers and VACO Program Office (MCCR, MAS, and Medical Information Resources Management Office \[MIRMO\]) officials on a regular basis to develop the initial specifications and answer questions that arose during the development cycle. The field representatives in these groups included physicians, UR nurses, MAS ADPACs, MCCR coordinators, and billing clerks. An additional group of users was assembled prior to alpha testing to conduct full usability and functional testing of the software. The input from each of the individuals on these groups was invaluable to the software developers.
IB version 2.0 includes electronic exchange (EDI) of claim information with third party payers and Medicare via Financial Services Center (FSC).
- Claims are transmitted electronically from VistA to insurance providers.
- Remittance advice information for claims transmitted is received as mail messages.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Integrated Billing Technical Manual is divided into major sections for general clarity and simplification of the material being presented. This manual is intended for use as a reference document by technical computer personnel.

The Implementation and Maintenance Section provides information on any aspect of the package that is site configurable. The file Flow Chart found in the Files section shows the relationships between the IB files and files external to the IB package. This section also contains a listing of each IB input, print, and sort template with descriptions. There are also sections on archiving and purging, how to generate online documentation, and package-wide variables.

Information concerning package security may be found in the Integrated Billing v2.0 Package Security Guide.

## Note to Users with Qume Terminals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is very important to set up the Qume terminal properly for this release of Integrated Billing. After the user gains access and verifies codes, the following will appear:

Select TERMINAL TYPE NAME:{type}//

Please make sure that \<C-QUME\> is entered here. This entry will become the default. Press \<RET\> at this prompt for all subsequent log-ins. If any other terminal type configuration is set, options using the List Manager utility (such as the Insurance Company Entry/Edit option under the Patient Insurance Menu or the Clinic Setup/Edit Forms option under the Edit Encounter Forms Menu) will neither display nor function properly on the terminal.

## Symbols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are explanations of the symbols used throughout this manual:

- \<RET\>: Press the RETURN or ENTER key.
- \<SP\>: Press the spacebar.
- \<^\>: Up-arrow, press the SHIFT key and the numeric 6 key simultaneously.
- \<?\> \<??\>: Enter single, double, or triple question marks to activate online help,
- \<???\>: Depending on the level of help needed.

# General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Namespace Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespaces and file ranges assigned to the Integrated Billing package are DIC, File \#36; IB, Files \# 350 - 389; DGCR, Files \# 399 - 399.5. Files \#409.95 and 409.96, under namespace SD, are exported with version 2.0 of IB.

## Integrity Checker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IBNTEG routine checks integrity for other IB and DGCR routines. This was built using the KERNEL utility routine, XTSUMBLD.

## SACC Exemptions / Non-Standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One Standards and Conventions Committee (SACC) exemption was granted for one time killing of the following DD nodes for IB v2.0.

- ^DD(399,.01,21)
- ^DD(399,2,21)
- ^DD(399,205,21)
- ^DD(399,213,23)
- ^DD(399,303,21)

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resource requirements for Integrated Billing version 1.0 were measured in detail, and VA Medical Centers were distributed equipment for this package. The resource consumption of existing modules of Integrated Billing version 2.0 has not changed significantly. The three new modules in Integrated Billing have some additional resource requirements.

The installation of IB version 2.0 may require approximately 5-15 megabytes of additional disk capacity. This includes up to 2.5 megabytes in the global DPT, up to 2.5 megabytes in the global DGCR, up to 5 megabytes in the global IBA, and up to 5 megabytes in the new global IBT.

The Encounter Form Utilities require a small amount of additional capacity to edit and store the format of the encounter forms.

1.  The standard partition size has been increased to 40K. Increase the partition size to the new standard in order to run the utilities. The printing of encounter forms will require at least one dedicated printer that most sites have already received. The printing will require additional CPU capacity; however, this job may be scheduled during non-peak workload hours.

The Insurance Data Capture module has been highly used during testing. This module will increase the disk utilization in the DPT global by approximately 1k per every 10 insurance policies and in the IBA global by 1k per every three insurance policies.

Based on the experience of our test sites, the Claims Tracking module will use approximately 5k of disk space for every pre-admission entry (one for every insurance case plus 5 per week for UR). In addition, approximately 1k of disk space for every 3 outpatient visits or prescription refills will be used.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Integrated Billing package may be tailored specifically to meet the needs of the various sites. Instructions may be found in the Integrated Billing User Manual under the MCCR System Definition Menu, which includes the MCCR Site Parameter Display/Edit option and others that may be used by each site to define configuration.

The Ambulatory Surgery Maintenance Menu contains all the options necessary to transfer Billable Ambulatory Surgical Code (BASC) procedures into the BASC file (#350.4) annually, when new BASC procedures are provided. It also contains options to build and manage the use of CPT Check-off Sheets and an option to enter or edit locality modifiers. This functionality is currently obsolete but has been left in IB 2.0 pending possible future requirements.

There are other options in the MCCR System Definition Menu to enter or edit billing rates, update rate types, activate revenue codes, enter/edit automated billing parameters, and edit insurance company information. The Enter/Edit IB Site Parameters option in the System Manager's Integrated Billing Menu is used to modify the parameters controlling the Integrated Billing background filer. All configurations may be modified at any time as the site's needs change.

## Implementing Claims Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installing IB v2.0, sites should review the Claims Tracking site parameters and determine how to use this module. The recommended settings are shown in the User Manual. The Claims Tracking module can use a great deal of disk space and capacity if turned on to track all episodes.

Because this part of the package contains the data entry portion of the QM national roll up of data, and will determine the random sample cases for review, most sites will be compelled to run this part of the inpatient tracking. If using the Automated Biller to do bill preparation for outpatient and prescription refill billing, turn on tracking in the Claims Tracking module. There are ways to automatically back load cases into Claims Tracking, if not currently capacity exists, or to delay the implementation. The site can still take advantage of this module later.

The option Claims Tracking Parameter Edit has several features that affect the operation of the software. There are parameters that may greatly affect the kind and frequency of records that are added to Claims Tracking and the amount of disk space utilized. Claims Tracking also contains a random sample generator for UR to randomly select which admissions are to be reviewed. Setting the parameters concerning the number of weekly admissions by service affects which cases, if any, are selected as the random case. If the numbers in these fields are set lower than the number of admissions per week, the random sample case will be selected early in the week. If the numbers in these fields are set higher than the number of admissions per week, depending on the random number selected for that week, there is a risk that no random sample will be selected.

## Implementing Encounter Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are steps that the local site should take before encounter forms can be used.

First, forms must be designed and assigned to the clinics. Forms can be shared between clinics, but it is important to control who has responsibility for editing the shared forms. One important aspect of designing encounter forms is determining what codes should go on the form. Many encounter forms will have lists of CPT codes, diagnosis codes, or problems. Because space on an encounter form is at a premium, careful analysis is required to determine the codes most used by the clinic before entering codes on the form. For CPT codes, the option Most Commonly Used Outpatient CPT Codes can be used to determine a clinic's most used codes.

Procedures for printing the encounter forms must be determined. The following are some of the questions that must be answered.

- What printers to use?
- Can the printers be loaded with enough paper?
- How many days in advance should the forms be printed?
- What time of day to run the print job?
- Should the printers be watched?
- What to do if there are printer problems?

It is expected that most printing of forms will be done in batch at night for entire divisions, and that forms will be printed several days in advance with only the additions printed the night before.

Then there are questions concerning what to do with the encounter forms.

- How will the completed encounter forms be routed?
- Who will input the data?

It is expected that much of the collected data will be input through checkout which is part of PIMS 5.3.

The Print Manager that comes with the Encounter Form Utilities is expected to be very useful to the local sites. Sites must decide which reports should be printed. The Print Manager allows these reports to be specified along with the encounter forms. The fastest way to define the reports is at the division level, rather than at the clinic level. Individual clinics can override reports defined to print at the division level.

## Implementing Insurance Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several tools in the Insurance module to identify duplicate insurance company file (#36) entries and to resolve these problems. It may also be helpful to review the process of how insurance information is collected at the facility. This module was designed so that as little information as possible would be collected during registration and that more complete information would be collected by a separate employee who would contact the insurance company.

### Prior to installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review how the Group Number and Group Name fields in the Insurance Type multiple of the PATIENT file (#2) are entered. These will be used to create the new GROUP INSURANCE PLAN file (#355.3). A new group plan will be created for every unique group plan entry for each insurance company. If possible, consolidate similar but unique names.

Print a list of all active and inactive insurance companies along with the addresses. There are several new insurance company address fields. Determine which insurance company entries can be inactivated and merged into another (active) insurance company entry.

2.  Do not delete the old entries. Inactivate them currently.

Determine which users should have access to the new Insurance options. There are options that allow for view-only access to both the insurance company information and patient insurance information as well as options for data entry. Limiting the ability of certain individuals to add / edit / delete information may improve the quality of insurance information. Having accurate and detailed insurance information can improve collections by focusing efforts on cases that are potentially reimbursable.

Many sites enter Medicare and Medicaid policy information as an insurance policy. If the entry in the insurance company file (#36) for Medicare and Medicaid exist, we recommend that the field Will Reimburse? be answered "NO". This will prevent the software from treating this as a billable insurance company entry. If this is answered other than "no", this could have a significant impact on the Claims Tracking module.

### After Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

First, run the option List Inactive Ins. Co. Covering Patients. This option will list companies that are currently covering patients who are non-billable due to the insurance company being inactive. In the Insurance Company Entry/Edit option, there is an action to activate and inactivate an insurance company. Use this action for the inactive insurance companies and it allows the user to print a list of the patients covered under these companies. To merge the patients to another company, do so at this or a later time.

If the user found a list of insurance companies that have many similar entries to handle different inpatient, outpatient, or prescription address information, combine these entries into one. Choose the entry to update and enter the complete information. Go back and inactivate the companies no longer used and utilize this feature to merge (re-point) the patients to the updated company entry. If many similar entries are found with the same name, but entered slightly differently, enter those names as synonyms for the updated company.

The option List New not Verified Policies can be run periodically to list new policies that have been added since a specific date and have not been verified by the insurance staff. Updating this information can help maintain the patient insurance information and allow the MCCR staff to concentrate on billing for covered care. This may foster good communication with the insurance carriers and ultimately improve rates of collection.

## Implementing Patient Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no preparation required by the facility to use the Patient Billing module of Integrated Billing version 2.0. However, the following guidelines are suggested.

Make a list of all stop codes, dispositions, and clinics where the billing of the Means Test outpatient co-payment is not desired. These values may easily be entered into the system (utilizing the option Flag Stop Codes / Dispositions / Clinics) from the list.

Decide whether to suppress the generation of mail messages for insured patients who have been billed Means Test co-payments. Update the parameter Suppress MT Ins Bulletin using the MCCR Site Parameter Display/Edit option.

## Implementing Third Party Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the site wishes to use the Automated Biller, enter the appropriate values to control the execution of the Automated Biller. Use the Enter/Edit Automated Billing Parameters \[IB AUTO BILLER PARAMS\] option. Starting with IB patch IB\*2\*568, this option is locked with security key IB PARAMETER EDIT.

<table>
<caption><p><span id="_Toc127633845" class="anchor"></span>Table : Parameters</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AUTO BILLER FREQUENCY</td>
<td><p>Enter the number of days between each execution of the Automated Biller.</p>
<p>For example, enter "7" to create bills once a week.</p></td>
</tr>
<tr class="even">
<td>INPATIENT STATUS (AB)</td>
<td>Enter the status in which the PTF record should be before the Auto Biller can create a bill. No auto bill will be created unless the PTF status is at least closed, regardless of how this parameter is set.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633845" class="anchor"></span>Table : Parameters

The following parameters may be entered for inpatient admissions, outpatient visits, and prescription refills.

| Parameter        | Definition                                                                                                                                                                                                                                                                             |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AUTOMATE BILLING | Enter "Yes" if bills should be automatically created for possible billable events with no user interaction. Leave this blank if the site prefers each event to be manually checked before a bill is created by the Auto Biller.                                                        |
| BILLING CYCLE    | For each type of event, enter the maximum date range of a bill. If this is left blank, the date range will default to the event date through the end of the month in which the event took place. For inpatient interim bills, this will be the next month after the last interim bill. |
| DAYS DELAY       | Enter the number of days after the end of the BILLING CYCLE that the bill should be created.                                                                                                                                                                                           |

<span id="_Toc127633846" class="anchor"></span>Table : Parameters

The following parameters may be used by sites to control prescription refill billing data and charge calculation. If the site plans to implement prescription refill billing, enter the appropriate values using the MCCR Site Parameter Display/Edit option \[IBJ MCCR SITE PARAMETERS\]. Starting with IB patch IB\*2\*568, this option is locked with security key IB PARAMETER EDIT.

| Parameter                  | Definition                                                                                                                                                                                                                                                                                                                                             |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEFAULT RX REFILL REV CODE | Enter the revenue code that should be used for most prescription refill bills. If this revenue code is defined, charges for every prescription refill will automatically be added to the bill with this Revenue Code. This site parameter may be overridden by the Insurance Company file (#36) parameter PRESCRIPTION REFILL REV. CODE if left blank. |
| DEFAULT RX REFILL DX       | If applicable, enter a diagnosis code that should be added to every prescription refill bill.                                                                                                                                                                                                                                                          |
| DEFAULT RX REFILL CPT      | If applicable, enter a CPT code that should be added to every prescription refill bill.                                                                                                                                                                                                                                                                |

<span id="_Toc127633847" class="anchor"></span>Table : Parameters

The following are other new site parameters that may need to be set using the MCCR Site Parameter Enter/Edit option \[IB MCCR PARAMETER EDIT\].

| Parameter                | Definition                                                                                                                                                                                                                        |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HCFA-1500 ADDRESS COLUMN | For the Health Care Finance Administration (HCFA)-1500, enter the column number in which the mailing address should begin printing for it to show in the envelope window (if it does not already print in the appropriate place). |
| UB-92 ADDRESS COLUMN     | For the UB-92, enter the column number in which the mailing address should begin printing for it to show in the envelope window (if it does not already print in the appropriate place).                                          |

<span id="_Toc127633848" class="anchor"></span>Table : Callable Routine

If the Bill Addendum Sheet should automatically print for every HCFA-1500 with prescription refills or prosthetic items, set the DEFAULT PRINTER (BILLING) field for the BILL ADDENDUM form type to the appropriate device. (Use the Select Default Device for Forms option \[IB SITE DEVICE SETUP\].)

If certain insurance companies require a specific Revenue Code to be used for Rx refills that is different than the DEFAULT RX REFILL REV CODE field, use the option Insurance Company Entry/Edit \[IBCN INSURANCE CO EDIT\] to enter the required Revenue Code in the PRESCRIPTION REFILL REV. CODE field.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per VA Directive 6402 (Aug 28, 2013) regarding security of software that affects financial systems, most of the IB routines may not be modified. The third line of routines that may not be modified will be so noted. The following routines are exempt from this requirement:

- IBD\* - Encounter Form Utilities
- IBO\*, IBCO\*, IBTO\* – Non-critical Reports

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that the following routines be mapped:

- IBA\*
- IBCNS
- IBCNS1
- IBCNSC\*
- IBCNSM\*
- IBCNSP\*
- IBCNSU\*
- IBEF\*
- IBR\*
- IBTRKR\*
- IBUTL\*
- IBX\*
- IBCNH\*

## Obsolete Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are obsolete for IB in version 2.0 and may be deleted.

- IBACKIN
- IBEHCF1
- IBOHCP
- IBEHCFA
- IBOHCTP
- IBEP
3.  The only routines in the DGCR namespace that are exported with IB 2.0 are DGCRAMS, DGCRNS, and DGCRP3. All other routines in the DGCR namespace may be deleted.

## Callable Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633849" class="anchor"></span>Table : Routine List</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Tag^Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>INST^IBCNINSL</td>
<td><p>Institution/Facility Lookup – Returns only VAMCs</p>
<p>The user will be prompted for either a full or partial institution name and be presented with a list of possible matches. The user will be able to select ALL for all institutions. The user will be able to select multiple institutions.</p>
<p>Input:</p>
<blockquote>
<p>ARRAY – Passed by Reference</p>
<p>PROMPT – The prompt to be displayed by the user</p>
</blockquote>
<p>Output:</p>
<blockquote>
<p>ARRAY – List of Institutions/Facilities</p>
</blockquote></td>
</tr>
<tr class="even">
<td>INSCO^IBCNINSL</td>
<td><p>Insurance Company Lookup</p>
<p>User will be prompted to enter a full or partial insurance company name and be presented with a list of possible matches. The user may select multiple insurance companies.</p>
<p>Input:</p>
<blockquote>
<p>ARRAY – Passed by Reference</p>
</blockquote>
<p>Output:</p>
<blockquote>
<p>ARRAY – List of Insurance Companies selected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PAYER^IBCNINSL</td>
<td><p>Payer Lookup</p>
<p>The user will be prompted to enter the full or partial payer name and will be presented with a list of possible matches. The user may select multiple payers.</p>
<p>Input:</p>
<blockquote>
<p>APP – Payer Application (EIV or IIU)</p>
<p>NOPYR – pass 1 to exclude the “~No Payer” payer or 0 to include</p>
<p>ARRAY – Pass by reference</p>
</blockquote>
<p>Output:</p>
<blockquote>
<p>ARRAY – Array of Payers selected</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PAYER^IBCNINSU</td>
<td><p>This function will return the requested information about a payer from file #365.12:</p>
<p>Input:</p>
<blockquote>
<p>Review the code for the current list of required and optional inputs as it is not easy to be documented in this small cell in a meaningful manner.</p>
</blockquote>
<p>Output:</p>
<blockquote>
<p>ARRAY - Data requested is returned in the array that was passed by reference</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PYRDEACT^IBCNINSU</td>
<td><p>This function will return whether that payer has a DEACTIVATE status or not.</p>
<blockquote>
<p>Input:</p>
<p>PIEN - Payer IEN</p>
<p>Output</p>
<p>DEACTIVATE - Payer Deactivated (Internal Format)</p>
<p>0 - No</p>
<p>1 - Yes</p>
<p>DATE/TIME DEACTIVATE - Date and Time the Payer was deactivated (Internal FileMan format)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>$$INSURED^IBCNS1(DFN, DATE)</td>
<td><p>This extrinsic function will return a "1" if the patient is insured for the specified date or a "0" if the patient is not insured. Input of the date is optional. The default is "today". No other data is returned. For billing purposes, a patient is only considered insured if he has an entry in the INSURANCE TYPE sub-file that meets the following four conditions.</p>
<ol type="1">
<li><blockquote>
<p>The insurance company is active.</p>
</blockquote></li>
<li><blockquote>
<p>The insurance company will reimburse the government. (If the site tracks Medicare coverage of patients, the entry in the INSURANCE COMPANY file (#36) should be set to not reimburse.)</p>
</blockquote></li>
<li><blockquote>
<p>The effective date is before the date of care.</p>
</blockquote></li>
<li><blockquote>
<p>The expiration date is after the date of care. (Treat no entry in the EFFECTIVE DATE and EXPIRATION DATE fields as from the beginning of time to the end of time.)</p>
</blockquote></li>
</ol>
<p>The user might find something like the following reference:</p>
<p>I $$INSURED^IBCNS1(DFN,+$G(^DGPM(+DGPMCA,0))) D BILL.</p></td>
</tr>
<tr class="odd">
<td>ALL^IBCNS1(dfn, variable, active, date)</td>
<td><p>This function will return all insurance data in the array of choice. Input the patient internal entry number and the variable the data is to be returned. Optionally, ask for active insurance information by putting a "1" or "2" in the third parameter and a date for the insurance to be active on in the fourth parameter (the default is "today"). If the value of the third parameter is "2", then insurance companies that do not reimburse VA will be included. This is primarily to retrieve Medicare policies when it is desirable to include these in active policies, e.g., when printing insurance information on encounter forms.</p>
<p>It will return the 0, 1, and 2 nodes for each entry in the INSURANCE TYPE sub-file and the 0 node from the GROUP INSURANCE PLAN file (#355.3) in a 2-dimensional array, Array (x, node). The array element Array (0) will be defined to the count of entries. In Array (x, node) x will be the internal entry in the INSURANCE TYPE sub-file and node will be 0, 1, 2 or 355.3. The GROUP NAME and NUMBER fields have been moved to the GROUP INSURANCE PLAN file (#355.3), but since many programmers are used to looking for this data on the 0th node from the INSURANCE TYPE sub-file, the current value from 355.3 is put back into the respective pieces of the 0th node. The code for this call looks something like the following:</p>
<p>K IBINS</p>
<p>D ALL^IBCNS1(DFN,"IBINS",1,IBDT) I $G(IBINS(0)) D LIST</p></td>
</tr>
<tr class="even">
<td>DGCRAMS</td>
<td>Supported call for AR to determine Automated Management Information System (AMIS) segments for insurance bills.</td>
</tr>
<tr class="odd">
<td>DGCRNS</td>
<td>IB v1.5 insurance retrieval call, to be replaced by ALL^IBCNS1.</td>
</tr>
<tr class="even">
<td>DGCRP3</td>
<td>This call, available to Accounts Receivable, will print second and third notice UB-82s, UB-92s, and HCFA-1500s.</td>
</tr>
<tr class="odd">
<td>DISP^IBAPDX1(in, sptr, out, off)</td>
<td>This extrinsic function is also used by the PDX package. This call will transform the data in the array generated by the EXTR^IBAPDX call into an array which is in a display-ready format.</td>
</tr>
<tr class="even">
<td>DISP^IBCNS</td>
<td>This tag can be called to do the standard insurance display. This display is used extensively in registration and billing. The variable DFN must be defined to the current patient. Using this tag will keep the displays current when the package developers update these or make other data dictionary changes.</td>
</tr>
<tr class="odd">
<td>DISP^IBARXEU(dfn, date, number of lines, unknown action)</td>
<td>This is a supported call for all developers. It will print the standard display of exemption status for the patient's current exemption on or before the specified date. If no date is specified, "today" is the default. It will print a maximum of three lines of text; the current exemption status, the exemption reason, and the date of the last exemption. All parameters are optional except for DFN. The display can be limited to a specified number of lines. In addition, if a medication co-payment exemption status has never been determined for a patient, the display can be set to not display or display the unknown information.</td>
</tr>
<tr class="even">
<td>EPFBAPI^ IBCEP8C(SrcArray, RetArray)</td>
<td>Integration agreement 5806. This private agreement between FB and IB will allow Fee Basis to file Fee Vendor and 5010 Providers to the IB NON/OTHER VA BILLING PROVIDER (#355.93) file for paid Fee claims that are potentially billable by IB (For Future Use). The call is made during a nightly process (option FB PAID TO IB) within FB.</td>
</tr>
<tr class="odd">
<td>EXTR^IBAPDX(tran, dfn, arr)</td>
<td>This extrinsic function is used by the Patient Data Exchange (PDX) version 1.5 package to transport Means Test billing data between facilities. For a given patient, this routine will build a global array containing Continuous Patient, Active Billing Clock, and Means Test Charge information from the transmitting facility.</td>
</tr>
<tr class="even">
<td>IB^IBRUTL</td>
<td>This call, available to Accounts Receivable, will determine if there are Means Test charges on hold associated with a given bill number. An optional parameter will return the held charges in an array.</td>
</tr>
<tr class="odd">
<td>IBAMTD</td>
<td>This routine is invoked by the MAS Movement Event Driver. It processes final Means Test charges for Category C veterans who are discharged.</td>
</tr>
<tr class="even">
<td>IBAMTED</td>
<td>This routine is invoked by the MAS Means Test Event Driver. It sends a mail message to the IB CAT C mail group if a patient's Means Test "billable" status changes (i.e., from Category C to Category A or vice versa).</td>
</tr>
<tr class="odd">
<td>IBAMTS</td>
<td>This routine is invoked by the Scheduling Check-In Event Driver. It bills the Means Test outpatient co-payment charge to Category C veterans who are checked in for a clinic visit.</td>
</tr>
<tr class="even">
<td>IBARX</td>
<td>This routine has 4 calls supported for Outpatient Pharmacy only: XTYPE^IBARX (eligibility determination), NEW^IBARX (file new RX co-payments), CANCEL^IBARX (cancel), and UPDATE^IBARX (update).</td>
</tr>
<tr class="odd">
<td>IBOLK</td>
<td>This routine has two supported entry points for the Accounts Receivable package to print a profile of an AR Transaction. The entry point ENF is used to print a full profile. The entry point ENB is used to print a brief profile.</td>
</tr>
<tr class="even">
<td>IBRFN</td>
<td>This routine has supported calls to return the text of an error message.</td>
</tr>
<tr class="odd">
<td>IBRREL</td>
<td>This routine has one supported call, AR^IBRREL, for the Accounts Receivable package. If there are Means Test charges on hold that are associated with the input bill number, these charges will be displayed and available for selection to be "released" to AR.</td>
</tr>
<tr class="even">
<td>IBCAPP</td>
<td>CLAIMS AUTO PROCESSING MAIN PROCESSER. This routine is called by IBCNSBL2 (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCAPP1</td>
<td>CLAIMS AUTO PROCESSING UTILITIES. This routine is called by IBCAPP (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCAPP2</td>
<td>CLAIMS AUTO PROCESSING. This routine is called by IBCECOB1 (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCAPR</td>
<td>PRINT EOB/MRA. This routine is called by IBCAPR1 and IBCAPR2 (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCAPR1</td>
<td>CAPR PRINT FUNCTIONS. This routine is called by IBCAPP (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCAPR2</td>
<td>PRINT EOB/MRA (IB*2.0*432)</td>
</tr>
<tr class="even">
<td>IBCAPU</td>
<td>CLAIMS AUTO PROCESSING UTILITIES (IB*2.0*432)</td>
</tr>
<tr class="odd">
<td>LNNDCCK^IBCBB11</td>
<td>Validate Line Level for NDC – The Units and Units/Basis of Measurement fields are required if the NDC field is populated (IB*2.0*577).</td>
</tr>
<tr class="even">
<td>IBCBB12</td>
<td>PROCEDURE AND LINE LEVEL PROVIDER EDITS. This routine is called by IBCBB1 (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCEF80</td>
<td>PROVIDER ID FUNCTIONS. This routine is called by IBCEF7 and IBCEFPL (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCEF81</td>
<td>PROVIDER ADJUSTMENTS. This routine is called by IBCEF80, IBCEFP, and IBCEFPL (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCEF82</td>
<td>PROVIDER ADJUSTMENTS. This routine is called by IBCEF81 (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCEF83</td>
<td>GET PROVIDER FUNCTIONS. CALLED BY OUTPUT FORMATTER (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCEF84</td>
<td>GET PROVIDER FUNCTIONS. CALLED FROM DICT 399, FIELDS .21 &amp; 101 TRIGGERS FOR FIELD 27. (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCEFP</td>
<td>PROVIDER ID FUNCTIONS. This routine is called by IBCEF11, IBCEF74, IBCEF76, IBCEF79, and IBCEF83 IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCEFP1</td>
<td>OUTPUT FORMATTER PROVIDER UTILITIES. This routine is called by IBCEF76 and IBCEFP (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCEU7</td>
<td>EDI UTILITIES. This routine is called by IBXS3, IBXS6, IBXS7, IBXSC3, IBXSC6, IBXSC7, and IBXX17 (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>FTFIC^IBCNEUT7</td>
<td>Returns an Insurance Company’s formatted Filing Time Frame</td>
</tr>
<tr class="even">
<td>FTFGP^IBCNEUT7</td>
<td>Returns a Group Plan’s formatted Filing Time Frame</td>
</tr>
<tr class="odd">
<td>IBCSC10</td>
<td>MCCR SCREEN 10 (UB-82 BILL SPECIFIC INFO). This routine is called by BILLING SCREEN 10 (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCSC102</td>
<td>MCCR SCREEN 10 (UB-04 BILL SPECIFIC INFO). This routine is called by BILLING SCREEN 10 (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCSC10A</td>
<td>ADD/ENTER CHIROPRACTIC DATA. This routine is called by BILLING SCREEN 10 (IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCSC10B</td>
<td>ADD/ENTER PATIENT REASON FOR VISIT DATA. This routine is called by BILLING SCREEN 10 (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>IBCSC10H</td>
<td>MCCR SCREEN 10 (BILL SPECIFIC INFO) CMS-1500 .This routine is called by BILLING SCREEN 10 IB*2.0*432).</td>
</tr>
<tr class="even">
<td>IBCU7B</td>
<td>LINE LEVEL PROVIDER USER INPUT. This routine is called by IBCCPT (IB*2.0*432).</td>
</tr>
<tr class="odd">
<td>MENU^IBECK</td>
<td>This routine may be used on menu entry actions to display warnings.</td>
</tr>
<tr class="even">
<td>RXST^IBARXEU(dfn, date)</td>
<td>This is a supported extrinsic variable for all developers that returns the current exemption on or before the specified date. If no date is specified, "today" is the default. This variable returns the following data in the respective piece position: exemption status, exemption status text, the exemption reason code, the exemption reason text, and the date of prior test.</td>
</tr>
<tr class="odd">
<td>STMT^IBRFN1(tran)</td>
<td>This routine call is used by the Accounts Receivable package during the printing of the patient statements. The input to this routine is the AR transaction number. The output is a global array that contains the pharmacy, inpatient, or outpatient clinical data, which is incorporated into the patient statement.</td>
</tr>
<tr class="even">
<td>THRES^IBARXEU1(date, type, dependents)</td>
<td>This supported call will return the threshold amount that a patient's income must not exceed to be exempt from the medication co-payment requirement. Inputs are date of test, type of threshold (currently on type=2 is supported), and the number of dependents. The data is retrieved from the BILLING THRESHOLDS file (#354.3).</td>
</tr>
<tr class="odd">
<td>ADD3611^IBCEOB</td>
<td>Create EOB stub. Used by Accounts Receivable package, EDI Lockbox module – Integration Agreement 4042.</td>
</tr>
<tr class="even">
<td>DUP^IBCEOB</td>
<td>Check for duplicate EOB. Used by Accounts Receivable package, EDI Lockbox module – Integration Agreement 4042.</td>
</tr>
<tr class="odd">
<td>ERRUPD^IBCEOB</td>
<td>Update EOB for error. Used by Accounts Receivable package, EDI Lockbox module – Integration Agreement 4042.</td>
</tr>
<tr class="even">
<td>UPD3611^IBCEOB</td>
<td>Update EOB detail. Used by Accounts Receivable package, EDI Lockbox module – Integration Agreement 4042.</td>
</tr>
<tr class="odd">
<td>SPL1^IBCEOBAR</td>
<td>Allows AR AMOUNTS multiple on an EOB to be changed. Used by Accounts Receivable package, EDI Lockbox module when an ERA line is split. Integration Agreement 4050.</td>
</tr>
<tr class="even">
<td>COPY^IBCEOB4</td>
<td>Allows an EOB to be copied. Used by Accounts Receivable package, EDI Lockbox module – Integration Agreement 5671.</td>
</tr>
<tr class="odd">
<td>UNLOCK^IBCEOB4</td>
<td>Allows an EOB to be LOCKED. User by Accounts Receivable package, EDI Lockbox module – Integration Agreement 5671.</td>
</tr>
<tr class="even">
<td>MOVE^IBCEOB4</td>
<td>Allows claim number on an EOB to be changed. Used by Accounts Receivable package, EDI Lockbox module – Integration Agreement 5671.</td>
</tr>
<tr class="odd">
<td>UNLOCK^IBCEOB4</td>
<td>Allows an EOB to be UNLOCKED. Used by Accounts Receivable package, EDI Lockbox module – Integration Agreement 5671.</td>
</tr>
<tr class="even">
<td>IBDSP^IBJTU6</td>
<td>Build IB List Manager display array scratch globals. Used by Accounts Receivable and by Electronic Claims Management Engine (ECME) – Integration Agreement 5713.</td>
</tr>
<tr class="odd">
<td>RX^IBNCPDP</td>
<td>IB Billing Determination. Used by ECME to determine billing information for ePharmacy. Integration Agreement 4299.</td>
</tr>
<tr class="even">
<td>STORESP^IBNCPDP</td>
<td>Create ePharmacy bills. Used by ECME to send the results of the ePharmacy response from the payers into billing to create bills. Integration Agreement 4299.</td>
</tr>
<tr class="odd">
<td>PRINT^IBNCPEV</td>
<td><p>Print the IB NCPDP Billing Events Report. Used by ECME.</p>
<p>Integration Agreement 5712.</p></td>
</tr>
<tr class="even">
<td>COLLECT^IPNCPEV3</td>
<td>Entry point to extract report data from the IB NCPDP EVENT LOG based on the incoming criteria. Used by the BPS RPT NON-BILLABLE REPORT in the ECME application. Integration Agreement 6131.</td>
</tr>
<tr class="odd">
<td>RT^IBNCPDPU</td>
<td>Used internally by the billing system to determine the proper rate type for ePharmacy billing situations.</td>
</tr>
<tr class="even">
<td>RXINS^IBNCPDPU</td>
<td>Return an array of pharmacy insurance policies in Coordination of Benefits order. Used by ECME. IA 5714.</td>
</tr>
<tr class="odd">
<td>HPD^IBCNHUT1(INS,V)</td>
<td><p>This function returns the Health Plan Identifier (HPID) / Other Entity Identifier (OEID) for an insurance company. The user must pass in the Insurance Company ien in file 36 (INS). If the user passes the second variable as V=1, validation checks will also be run on the HPID. If the HPID does not pass the validation checks (10 numeric characters, 1<sup>st</sup> character is a 6 or 7 and the 10th character is the Luhn check-digit), the function will append a ‘*’ to the end of the HPID to indicate it is not valid.</p>
<p>Reference something like the following:</p>
<p>W !,"HPID/OEID: ",$$HPD^IBCNHUT1(INS,1)</p></td>
</tr>
<tr class="even">
<td>IBRFIHLU</td>
<td>RFAI HL7 Utilities – Utilities used for the handling of Request For Additional Information (RFAI) HL7 messages.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633849" class="anchor"></span>Table : Routine List

## Routine List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633850" class="anchor"></span>Table : DGCR Routines</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DGCRAMS</td>
<td>Bridge routine to IBCAMS routine that determines Accounts Receivable AMIS category for insurance bills.</td>
</tr>
<tr class="even">
<td>DGCRNS</td>
<td>Utility routine to determine if patient has active insurance and to do standard displays.</td>
</tr>
<tr class="odd">
<td>DGCRP3</td>
<td>Bridge routine to IBCF13 routine that is the call for Accounts Receivable to print bills.</td>
</tr>
<tr class="even">
<td>IB20428P, IB20P*, IB20R244, IB2P167C</td>
<td>IB Individual Patch POST-INIT Routines</td>
</tr>
<tr class="odd">
<td>IB20E253, IB20E295, IB20E362, IB20E379, IB20E410, IB20E425, IB20E441</td>
<td>IB Individual Patch Environment Check Routines</td>
</tr>
<tr class="even">
<td>IB20IN</td>
<td>IB version 2.0 initialization routine</td>
</tr>
<tr class="odd">
<td>IB20PRE</td>
<td>IB version 2.0 pre-initialization routine</td>
</tr>
<tr class="even">
<td>IB20PT*</td>
<td>IB version 2.0 post initialization routines</td>
</tr>
<tr class="odd">
<td>IB3PSOU</td>
<td>Outpatient Pharmacy Administrative Fee Change Update</td>
</tr>
<tr class="even">
<td>IBACSV</td>
<td>CODE SET VERSIONING IB UTILITIES</td>
</tr>
<tr class="odd">
<td>IBACUS</td>
<td>TRICARE BILLING UTILITIES</td>
</tr>
<tr class="even">
<td>IBACUS1</td>
<td>TRICARE PATIENT RX CO-PAY CHARGES</td>
</tr>
<tr class="odd">
<td>IBACUS2</td>
<td>TRICARE FISCAL INTERMEDIARY RX CLAIMS</td>
</tr>
<tr class="even">
<td>IBACV</td>
<td>COMBAT VET UTILITIES</td>
</tr>
<tr class="odd">
<td>IBACVA, IBACVA1, IBACVA2</td>
<td>Routines for the mail message generation and automatic charge creation for the CHAMPVA subsistence charge.</td>
</tr>
<tr class="even">
<td>IBAECB</td>
<td>LTC BILLING CLOCK INQUIRY</td>
</tr>
<tr class="odd">
<td>IBAECB1</td>
<td>LTC BILLING CLOCK INQUIRY</td>
</tr>
<tr class="even">
<td>IBAECC</td>
<td>LONG TERM CARE CLOCK MAINTANCE</td>
</tr>
<tr class="odd">
<td>IBAECI</td>
<td>LONG TERM CARE INPATIENT TRACKER</td>
</tr>
<tr class="even">
<td>IBAECM1</td>
<td>LTC PHASE 2 MONTHLY JOB</td>
</tr>
<tr class="odd">
<td>IBAECM2</td>
<td>LTC PHASE 2 MONTHLY JOB</td>
</tr>
<tr class="even">
<td>IBAECM3</td>
<td>LTC PHASE 2 MONTHLY JOB PART 3</td>
</tr>
<tr class="odd">
<td>IBAECN1</td>
<td>LTC PHASE 2 NIGHTLY JOB</td>
</tr>
<tr class="even">
<td>IBAECO</td>
<td>LONG TERM CARE OUTPATIENT TRACKER</td>
</tr>
<tr class="odd">
<td>IBAECP</td>
<td>LTC SINGLE PATIENT PROFILE</td>
</tr>
<tr class="even">
<td>IBAECP1</td>
<td>LTC SINGLE PATIENT PROFILE</td>
</tr>
<tr class="odd">
<td>IBAECU</td>
<td>LTC UTILITIES DETERMINE LTC ELIG</td>
</tr>
<tr class="even">
<td>IBAECU1</td>
<td>LONG TERM IDENTIFICATION UTILITIES</td>
</tr>
<tr class="odd">
<td>IBAECU2</td>
<td>LTC PHASE 2 UTILITIES</td>
</tr>
<tr class="even">
<td>IBAECU3</td>
<td>LTC PHASE 2 UTILITIES</td>
</tr>
<tr class="odd">
<td>IBAECU4</td>
<td>LTC PHASE 2 UTILITIES</td>
</tr>
<tr class="even">
<td>IBAECU5</td>
<td>LTC PHASE 2 UTILITIES</td>
</tr>
<tr class="odd">
<td>IBAERR</td>
<td>Converts pharmacy co-pay error codes to text and sends a mail message if error occurs in a tasked job.</td>
</tr>
<tr class="even">
<td>IBAERR1</td>
<td>Creates mail messages when errors occur during the compilation of Means Test charges.</td>
</tr>
<tr class="odd">
<td>IBAERR2</td>
<td>Processes error messages and sends mail messages for the Medication Co-payment Exemption process.</td>
</tr>
<tr class="even">
<td>IBAERR3</td>
<td>Sends and processes alerts for the Medication Co-payment Exemption process if the site chooses to use alerts rather than mail messages for electronic notification.</td>
</tr>
<tr class="odd">
<td>IBAFIL</td>
<td>Posts tasks to the background filer. Starts filer if it is not running.</td>
</tr>
<tr class="even">
<td>IBAGMM</td>
<td>GMT MONTHLY TOTALS REPORT</td>
</tr>
<tr class="odd">
<td>IBAGMM1</td>
<td>GMT MONTHLY TOTALS REPORT</td>
</tr>
<tr class="even">
<td>IBAGMR</td>
<td>GMT SINGLE PATIENT REPORT</td>
</tr>
<tr class="odd">
<td>IBAGMR1</td>
<td>GMT SINGLE PATIENT REPORT</td>
</tr>
<tr class="even">
<td>IBAGMT</td>
<td>GEOGRAPHIC MEANS TEST UTILITIES</td>
</tr>
<tr class="odd">
<td>IBAHVE3</td>
<td>CV EXPIRATION REPORT</td>
</tr>
<tr class="even">
<td>IBAKAT</td>
<td>CANCEL CO-PAY CHARGES FOR KATRINA VETS</td>
</tr>
<tr class="odd">
<td>IBAMTBU</td>
<td>Creates mail messages when Category C patient movements change, and when continuous patients are discharged.</td>
</tr>
<tr class="even">
<td>IBAMTBU1</td>
<td>Creates a mail message when charges are created in error for patients admitted for observation and examination.</td>
</tr>
<tr class="odd">
<td>IBAMTBU2</td>
<td>Generates a mail message if a change in the Means Test affects the patient's Means Test charges.</td>
</tr>
<tr class="even">
<td>IBAMTC</td>
<td>Means Test Billing Nightly Compilation Job. Creates charges and updates billing clocks for all Category C inpatients.</td>
</tr>
<tr class="odd">
<td>IBAMTC1</td>
<td>Sends mail message when the Nightly Compilation Job has completed.</td>
</tr>
<tr class="even">
<td>IBAMTC2, IBAMTC3</td>
<td>Ensures inpatient events are closed on discharge and Category C charges are passed. Sends mail message if not accomplished.</td>
</tr>
<tr class="odd">
<td>IBAMTD</td>
<td>Means Test Billing Discharge Compilation Job. Calculates final Means Test charges when a Category C patient is discharged. Invoked by the MAS Movement Event Driver. The bundling and unbundling of Means Test billing data that is transmitted, received, and displayed by the PDX package.</td>
</tr>
<tr class="even">
<td>IBAMTD1</td>
<td>Computes Means Test charges for single day admissions.</td>
</tr>
<tr class="odd">
<td>IBAMTD2</td>
<td>Determines whether a change in patient movements will affect a patient's Means Test charges.</td>
</tr>
<tr class="even">
<td>IBAMTED</td>
<td>Invoked by the MAS Means Test Event Driver. Determines whether a change in the Means Test should result in the generation of a mail message.</td>
</tr>
<tr class="odd">
<td>IBAMTED1</td>
<td>Creates new or updated exemptions whenever a change occurs in a patient's demographic data, eligibility, Means Test, or Co-pay Test that would affect his/her exemption status.</td>
</tr>
<tr class="even">
<td>IBAMTED2</td>
<td>RX CO-PAY TEST EVENT DRIVER, Z06 EXEMPTION PROCESSING</td>
</tr>
<tr class="odd">
<td>IBAMTEDU</td>
<td>Determines whether a change in the Means Test will affect patient’s Means Test charges. Creates a list of charges or patient care episodes that would be included in the mail message.</td>
</tr>
<tr class="even">
<td>IBAMTEL</td>
<td>Contains the various locations where an error may occur in the processing of Means Test charges for inpatients.</td>
</tr>
<tr class="odd">
<td>IBAMTI, IBAMTI1, IBAMTI2</td>
<td>These routines handle all mail message generation, processing, and outputs for special inpatient billing cases.</td>
</tr>
<tr class="even">
<td>IBAMTS, IBAMTS1, IBAMTS2</td>
<td>Bills / Credits Category C outpatient co-payments via Scheduling Event Driver.</td>
</tr>
<tr class="odd">
<td>IBAMTS3</td>
<td>APIs are added to support High Risk for Suicide (HRfS) claims proration and exclusions. A bulletin generator for a patient who has the HRfS flag activated or inactivated during the previous day (run through the Means Test Nightly process) was added.</td>
</tr>
<tr class="even">
<td>IBAMTV</td>
<td>BACK-BILLING SUPPORT FOR IVM</td>
</tr>
<tr class="odd">
<td>IBAMTV1</td>
<td>BUILD ARRAY OF BILLABLE EPISODES</td>
</tr>
<tr class="even">
<td>IBAMTV2</td>
<td>CREATE CHARGES FOR BILLABLE EPISODES</td>
</tr>
<tr class="odd">
<td>IBAMTV3</td>
<td>RELEASE CHARGES PENDING REVIEW</td>
</tr>
<tr class="even">
<td>IBAMTV31</td>
<td>LIST CHARGES PENDING REVIEW</td>
</tr>
<tr class="odd">
<td>IBAMTV32</td>
<td>RELEASE PENDING CHARGES ACTIONS</td>
</tr>
<tr class="even">
<td>IBAMTV4</td>
<td>FIND CHARGES FOR IVM PATIENTS</td>
</tr>
<tr class="odd">
<td>IBAPDX, IBAPDX0, IBAPDX1</td>
<td>These routines are invoked by the PDX package and handle the bundling and unbundling of Means Test billing data that is transmitted, received, and displayed by the PDX package.</td>
</tr>
<tr class="even">
<td>IBAREP</td>
<td>Routine to repost IB Actions to Accounts Receivable.</td>
</tr>
<tr class="odd">
<td>IBARX, IBARX1</td>
<td>Routine has supported calls for Pharmacy Co-pay for eligibility, new charges, cancelled charges, and updated charges.</td>
</tr>
<tr class="even">
<td>IBARXCBK</td>
<td>Routine that does the message building and sending to Cerner when a BackBilling event occurs</td>
</tr>
<tr class="odd">
<td>IBARXCFL</td>
<td>Routine that contains utility used to process the VAFCTFU1 and VAFCTFU2 Treating Facility lists into the proper content and format (used the content of the VAFCTFU2 routine, but the format of the VAFCTFU1 routine)</td>
</tr>
<tr class="even">
<td>IBARXCR2</td>
<td>Routine that receives from Cerner either a Query or a Query Response and sends to the proper routine to build the appropriate response. Looks for either a QRY (for Query) or DSR (for Query Response)</td>
</tr>
<tr class="odd">
<td>IBARXCRD</td>
<td>Routine Files a Query Response (DSR) from Cerner</td>
</tr>
<tr class="even">
<td>IBARXCRC</td>
<td>Routine receives and files a new Transaction (DFT) from Cerner</td>
</tr>
<tr class="odd">
<td>IBARXCQR</td>
<td>Routine sends out a Seeding Query to Cerner</td>
</tr>
<tr class="even">
<td>IBARXCSH</td>
<td>Routine will send out a Query Response (DSR) to Cerner</td>
</tr>
<tr class="odd">
<td>IBARXCHL</td>
<td>Routine will send out a new Transaction (DFT) to Cerner</td>
</tr>
<tr class="even">
<td>IBARXDOC</td>
<td>Documentation of variable passing for IBARX.</td>
</tr>
<tr class="odd">
<td>IBARXEB</td>
<td>Sends electronic notification of changes in the patient's exemption status that require notification. Specifically, each time a patient either receives or loses a hardship exemption, a mail message or alert is generated.</td>
</tr>
<tr class="even">
<td>IBARXEC, IBARXEC0, IBARXEC2, IBARXEC3</td>
<td>These routines are the main components of the Medication Co-payment Exemption Conversion routines.</td>
</tr>
<tr class="odd">
<td>IBARXEC1, IBARXEC4, IBARXEC5</td>
<td>Print the report from the Medication Co-payment Exemption Conversion and the related option.</td>
</tr>
<tr class="even">
<td>IBARXECA</td>
<td>Contains the logic to cancel charges during the Medication Co-payment Exemption process.</td>
</tr>
<tr class="odd">
<td>IBARXEI</td>
<td>Produces the full and brief inquiry options for the Medication Co-payment Exemption process.</td>
</tr>
<tr class="even">
<td>IBARXEL</td>
<td>RX CO-PAY EXEMPTION INCOME TEST REMINDERS</td>
</tr>
<tr class="odd">
<td>IBARXEL1</td>
<td>RX CO-PAY EXEMPTION REMINDER REPRINT</td>
</tr>
<tr class="even">
<td>IBARXEP</td>
<td>Produces reports from the BILLING PATIENT file (#354) on the number and kinds of exemptions currently held by patients.</td>
</tr>
<tr class="odd">
<td>IBARXEPE</td>
<td>Edit pharmacy co-pay exemption letter.</td>
</tr>
<tr class="even">
<td>IBARXEPL</td>
<td>Print pharmacy co-pay exemption letters.</td>
</tr>
<tr class="odd">
<td>IBARXEPS</td>
<td>ALB/RM/PHH,EG - RX CO-PAY EXEMPTION UPDATE STATUS</td>
</tr>
<tr class="even">
<td>IBARXEPV</td>
<td>Has the ability to test the accuracy of patient exemptions for a date range and to update the exemptions of incorrect entries.</td>
</tr>
<tr class="odd">
<td>IBARXET</td>
<td>Allows adding and editing of Billing Thresholds.</td>
</tr>
<tr class="even">
<td>IBARXEU</td>
<td>Contains two supported calls to retrieve a patient's Medication Co-payment Exemption status.</td>
</tr>
<tr class="odd">
<td>IBARXEU0</td>
<td>Routine used to retrieve and / or update a patient's Medication Co-payment Exemption status. This routine should not be used by applications outside of IB.</td>
</tr>
<tr class="even">
<td>IBARXEU1</td>
<td>Contains the logic to calculate a patient's Medication Co-payment Exemption status.</td>
</tr>
<tr class="odd">
<td>IBARXEU3, IBARXEU4</td>
<td>Contain the logic to cancel past Medication Co-payment charges in both IB and AR.</td>
</tr>
<tr class="even">
<td>IBARXEU5</td>
<td>Contains the logic for dealing with net worth as part of income.</td>
</tr>
<tr class="odd">
<td>IBARXEVT</td>
<td>Medication Co-payment Exemption event driver. Invoked each time a Medication Co-payment Exemption is created.</td>
</tr>
<tr class="even">
<td>IBARXEX, IBARXEX1</td>
<td>Contain the logic for adding hardship exemptions for patients.</td>
</tr>
<tr class="odd">
<td>IBARXMA</td>
<td>PHARMACY CO-PAY BACKGROUND PROCESSES – IB*2.0*676 modified to check if Treating Facility is Cerner and send transaction with an HL7 message to Cerner.</td>
</tr>
<tr class="even">
<td>IBARXMB</td>
<td>PHARMACY CO-PAY CAP BILLING FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBARXMC</td>
<td>PHARMACY CO-PAY CAP FUNCTIONS – IB*2.0*676 modified to check if Treating Facility is Cerner and send transaction with an HL7 message to Cerner.</td>
</tr>
<tr class="even">
<td>IBARXMI</td>
<td>HL7 RECEIVER FOR PFSS WORKING ROUTINE</td>
</tr>
<tr class="odd">
<td>IBARXMN</td>
<td>PHARMCAY CO-PAY CAP RX PROCESSING – IB*2.0*676 modified to check if Treating Facility is Cerner and send transaction with an HL7 message to Cerner.</td>
</tr>
<tr class="even">
<td>IBARXMO</td>
<td>PHARMACY CO-PAY CAP REPORTS</td>
</tr>
<tr class="odd">
<td>IBARXMO1</td>
<td>PHARMACY CO-PAY CAP</td>
</tr>
<tr class="even">
<td>IBARXMP</td>
<td>PHARMCAY CO-PAY CAP PUSH TRANSACTION</td>
</tr>
<tr class="odd">
<td>IBARXMQ</td>
<td>RX CO-PAY RPC QUERY ROUTINE (MILL BILL)</td>
</tr>
<tr class="even">
<td>IBARXMR</td>
<td>PHARMCAY CO-PAY CAP RPC STUFF</td>
</tr>
<tr class="odd">
<td>IBARXMU</td>
<td>PHARMACY CO-PAY CAP UTILITIES</td>
</tr>
<tr class="even">
<td>IBARXPFS</td>
<td>PFSS ROUTINE FOR INTER-FACILITY RX CO-PAY</td>
</tr>
<tr class="odd">
<td>IBATCM</td>
<td>TRANSFER PRICING TRANSACTION CHARGES</td>
</tr>
<tr class="even">
<td>IBATEI</td>
<td>TRANSFER PRICING INPATIENT TRACKER</td>
</tr>
<tr class="odd">
<td>IBATEI1</td>
<td>TRANSFER PRICING BACKGROUND JOB</td>
</tr>
<tr class="even">
<td>IBATEO</td>
<td>TRANSFER PRICING OUTPATIENT TRACKER</td>
</tr>
<tr class="odd">
<td>IBATEP</td>
<td>TRANSFER PRICING RX TRACKER</td>
</tr>
<tr class="even">
<td>IBATER</td>
<td>Background job routine that searches for Transfer Pricing transactions in the Prosthetics file (#660).</td>
</tr>
<tr class="odd">
<td>IBATFILE</td>
<td>Utility calls for filing Transfer Pricing transactions.</td>
</tr>
<tr class="even">
<td>IBATLM0</td>
<td>TRANSFER PRICING PT LIST MANAGER</td>
</tr>
<tr class="odd">
<td>IBATLM0A</td>
<td>TRANSFER PRICING PT LIST MANAGER</td>
</tr>
<tr class="even">
<td>IBATLM1, IBATLM1A, IBATLM1B</td>
<td>Routines used to create a listing of Transfer Pricing transactions.</td>
</tr>
<tr class="odd">
<td>IBATLM2, IBATLM2A, IBATLM2B</td>
<td>Routines used to display Transfer Pricing patient transactions.</td>
</tr>
<tr class="even">
<td>IBATLM3</td>
<td>TRANSFER PRICING PATIENT INFO SCREEN</td>
</tr>
<tr class="odd">
<td>IBATLM3A</td>
<td>TRANSFER PRICING PT INFO SCREEN BUILD</td>
</tr>
<tr class="even">
<td>IBATO, IBATO1</td>
<td>Routines used to produce various Transfer Pricing reports.</td>
</tr>
<tr class="odd">
<td>IBATOP</td>
<td>TRANSFER PRICING PATIENT LISTING</td>
</tr>
<tr class="even">
<td>IBATRX</td>
<td>TRANSFER PRICING RX ROUTINE</td>
</tr>
<tr class="odd">
<td>IBATUTL</td>
<td>Utility calls for various Transfer Pricing functions.</td>
</tr>
<tr class="even">
<td>IBAUTL</td>
<td>Utility calls for IB application interface routines.</td>
</tr>
<tr class="odd">
<td>IBAUTL1</td>
<td>Utility routine to determine BASC billing rates.</td>
</tr>
<tr class="even">
<td>IBAUTL2</td>
<td>Means Test billing utilities - retrieve billing rates; add / edit charges for a patient.</td>
</tr>
<tr class="odd">
<td>IBAUTL3</td>
<td>Means Test billing utilities - retrieve / update billing event and billing clock data.</td>
</tr>
<tr class="even">
<td>IBAUTL4</td>
<td>Means Test billing utilities - calculate inpatient charges.</td>
</tr>
<tr class="odd">
<td>IBAUTL5</td>
<td>Means Test billing utilities - pass charges to Accounts Receivable; miscellaneous functions.</td>
</tr>
<tr class="even">
<td>IBAUTL6, IBAUTL7</td>
<td>Contain the logic used to add entries to the BILLING PATIENT file (#354) and the BILLING EXEMPTIONS file (#354.1).</td>
</tr>
<tr class="odd">
<td>IBAXDR</td>
<td>ROUTINE TO MERGE ENTRIES IN IB FILE FOR PATIENT MERGE</td>
</tr>
<tr class="even">
<td>IBBAACCT</td>
<td>PFSS ACCOUNT API</td>
</tr>
<tr class="odd">
<td>IBBAADD</td>
<td>PFSS FILE INDEXING</td>
</tr>
<tr class="even">
<td>IBBAADTI</td>
<td>PFSS INBOUND FILER</td>
</tr>
<tr class="odd">
<td>IBBACDM</td>
<td>PFSS SERVICE MASTER API</td>
</tr>
<tr class="even">
<td>IBBACHRG</td>
<td>PFSS CHARGE API</td>
</tr>
<tr class="odd">
<td>IBBADFTO</td>
<td>PFSS DFT BATCH MESSAGING</td>
</tr>
<tr class="even">
<td>IBBAPI</td>
<td>APIS FOR OTHER PACKAGES FOR PFSS</td>
</tr>
<tr class="odd">
<td>IBBASCI</td>
<td>CIDC SWITCH UTILITIES</td>
</tr>
<tr class="even">
<td>IBBASWCH</td>
<td>PFSS MASTER SWITCH FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBBDOC</td>
<td>APIS FOR OTHER PACKAGES FOR PFSS - DOCUMENT</td>
</tr>
<tr class="even">
<td>IBBFAPI</td>
<td>FOR OTHER PACKAGES TO QUERY INSURANCE INFO</td>
</tr>
<tr class="odd">
<td>IBBSHDWN</td>
<td>IB Sunset for PFSS</td>
</tr>
<tr class="even">
<td>IBCA, IBCA0, IBCA1, IBCA2</td>
<td>MCCR add new billing record. (Routines formerly named DGCRA, DGCRA0, DGCRA1, DGCRA2.)</td>
</tr>
<tr class="odd">
<td>IBCA3</td>
<td>Displays all bills for episode of care. (Formerly named DGCRA3.)</td>
</tr>
<tr class="even">
<td>IBCAMS</td>
<td>Determines Accounts Receivable AMIS category for insurance bills. (Routine formerly named DGCRAMS.)</td>
</tr>
<tr class="odd">
<td>IBCAPP</td>
<td>CLAIMS AUTO PROCESSING MAIN PROCESSER</td>
</tr>
<tr class="even">
<td>IBCAPP1</td>
<td>CLAIMS AUTO PROCESSING UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCAPP2</td>
<td>CLAIMS AUTO PROCESSING</td>
</tr>
<tr class="even">
<td>IBCAPR</td>
<td>PRINT EOB/MRA</td>
</tr>
<tr class="odd">
<td>IBCAPR1</td>
<td>CAPR PRINT FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCAPR2</td>
<td>PRINT EOB / MRA</td>
</tr>
<tr class="odd">
<td>IBCAPU</td>
<td>CLAIMS AUTO PROCESSING UTILITIES</td>
</tr>
<tr class="even">
<td>IBCB, IBCB1, IBCB2</td>
<td>MCCR bill processing. (Routines formerly named DGCRB, DGCRB1, and DGCRB2.)</td>
</tr>
<tr class="odd">
<td>IBCB11</td>
<td>Process bill after enter / edited</td>
</tr>
<tr class="even">
<td>IBCBB, IBCBB1, IBCBB2</td>
<td>Checks bills for completeness. (Routines formerly named DGCRBB, DGCRBB1, and DGCRBB2.)</td>
</tr>
<tr class="odd">
<td>IBCBB0</td>
<td>IB edit check routine continuation</td>
</tr>
<tr class="even">
<td>IBCBB11</td>
<td>CONTINUATION OF EDIT CHECK ROUTINE</td>
</tr>
<tr class="odd">
<td>IBCBB12</td>
<td>PROCEDURE AND LINE LEVEL PROVIDER EDITS</td>
</tr>
<tr class="even">
<td>IBCBB13</td>
<td>PROCEDURE AND LINE LEVEL PROVIDER EDITS</td>
</tr>
<tr class="odd">
<td>IBCBB14</td>
<td>CONTINUATION OF EDIT CHECK ROUTINE FOR EPHARM</td>
</tr>
<tr class="even">
<td>IBCBB21</td>
<td>CONTINUATION OF EDIT CHECK ROUTINE FOR UB</td>
</tr>
<tr class="odd">
<td>IBCBB3</td>
<td>CONTINUATION OF EDIT CHECKS ROUTINE (MEDICARE)</td>
</tr>
<tr class="even">
<td>IBCBB4</td>
<td>CONT OF MEDICARE EDIT CHECKS</td>
</tr>
<tr class="odd">
<td>IBCBB5</td>
<td>CONT OF MEDICARE EDIT CHECKS</td>
</tr>
<tr class="even">
<td>IBCBB6</td>
<td>CONT. OF MEDICARE EDIT CHECKS</td>
</tr>
<tr class="odd">
<td>IBCBB7</td>
<td>CONT. OF MEDICARE EDIT CHECKS</td>
</tr>
<tr class="even">
<td>IBCBB7A</td>
<td>CON'T MEDICARE EDIT CHECKS</td>
</tr>
<tr class="odd">
<td>IBCBB8</td>
<td>CON'T MEDICARE EDIT CHECKS</td>
</tr>
<tr class="even">
<td>IBCBB9</td>
<td>MEDICARE PART B EDIT CHECKS</td>
</tr>
<tr class="odd">
<td>IBCBR</td>
<td>Enter/Edit Billing Rates. (Routine formerly named DGCRBR.)</td>
</tr>
<tr class="even">
<td>IBCBULL</td>
<td>MCCR mail messages. (Routine formerly named DGCRBULL.)</td>
</tr>
<tr class="odd">
<td>IBCC, IBCC1</td>
<td>Cancel a Third-Party Bill. (Routine formerly named DGCRC.)</td>
</tr>
<tr class="even">
<td>IBCCC, IBCCC1, IBCCC2</td>
<td>Cancel and copy bill. (Routines formerly named DGCRCC, DGCRCC1, and DGCRCC2.)</td>
</tr>
<tr class="odd">
<td>IBCCC3</td>
<td>Continuation of Copy and Cancel.</td>
</tr>
<tr class="even">
<td>IBCCCB</td>
<td>COPY BILL FOR COB</td>
</tr>
<tr class="odd">
<td>IBCCCB0</td>
<td>COPY BILL FOR COB (OVERFLOW)</td>
</tr>
<tr class="even">
<td>IBCCPT</td>
<td>Display CPT codes from Ambulatory Surgeries screen. (Routine formerly named DGCRCPT)</td>
</tr>
<tr class="odd">
<td>IBCCPT1</td>
<td>MCCR OUTPATIENT VISITS LISTING CONT.(2)</td>
</tr>
<tr class="even">
<td>IBCCR</td>
<td>CLAIM CANCEL AND RESUBMIT INFORMATION</td>
</tr>
<tr class="odd">
<td>IBCD, IBCD1, IBCD2, IBCD3, IBCD4, IBCD5</td>
<td>Automated Biller background job</td>
</tr>
<tr class="even">
<td>IBCDC</td>
<td>Automated Biller utility routine</td>
</tr>
<tr class="odd">
<td>IBCDE</td>
<td>Automated Biller comments file management</td>
</tr>
<tr class="even">
<td>IBCDP</td>
<td>AUTOMATED BILLER PRINT</td>
</tr>
<tr class="odd">
<td>IBCE</td>
<td>837 EDI TRANSMISSION UTILITIES/NIGHTLY JOB</td>
</tr>
<tr class="even">
<td>IBCE277</td>
<td>277 EDI CLAIM STATUS MESSAGE PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCE277S</td>
<td>Create MailMan message from 277STAT data array</td>
</tr>
<tr class="even">
<td>IBCE835</td>
<td>835 EDI EXPLANATION OF BENEFITS MSG PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCE835A</td>
<td>835 EDI EOB PROCESSING CONTINUED</td>
</tr>
<tr class="even">
<td>IBCE837</td>
<td>OUTPUT FOR 837 TRANSMISSION</td>
</tr>
<tr class="odd">
<td>IBCE837A</td>
<td>OUTPUT FOR 837 TRANSMISSION - CONTINUED</td>
</tr>
<tr class="even">
<td>IBCE837B</td>
<td>OUTPUT FOR 837 TRANSMISSION (cont.)</td>
</tr>
<tr class="odd">
<td>IBCE837H</td>
<td>837 RPC ROUTINE for CLAIM DATA extract for FHIR transaction</td>
</tr>
<tr class="even">
<td>IBCE837I</td>
<td>837 RPC ROUTINE for CLAIM LIST extract for FHIR transaction, Continuation of IBCE837H, additional functions</td>
</tr>
<tr class="odd">
<td>IBCE837K</td>
<td>837 RPC ROUTINE for CLAIM ACKNOWLEDGEMENT for FHIR transaction</td>
</tr>
<tr class="even">
<td>IBCE837L</td>
<td>837 RPC ROUTINE for CLAIM DATA extract for FHIR transaction continued</td>
</tr>
<tr class="odd">
<td>IBCE837N</td>
<td>RPC TO RETURN EXTERNAL CLAIM NUMBER FOR IEN</td>
</tr>
<tr class="even">
<td>IBCE837P</td>
<td>OUTPUT FOR 837 TRANSMISSION - CONTINUED</td>
</tr>
<tr class="odd">
<td>IBCE837S</td>
<td>RPC to change 837 FHIR Transmit Yes / No in IB SITE PARAMETERS</td>
</tr>
<tr class="even">
<td>IBCE837T</td>
<td>RPC to setup test claims for non-production sites</td>
</tr>
<tr class="odd">
<td>IBCEBUL</td>
<td>837 EDI SPECIAL BULLETINS PROCESSING</td>
</tr>
<tr class="even">
<td>IBCECOB</td>
<td>IB COB MANAGEMENT SCREEN</td>
</tr>
<tr class="odd">
<td>IBCECOB1</td>
<td>IB COB MANAGEMENT SCREEN/REPORT</td>
</tr>
<tr class="even">
<td>IBCECOB2</td>
<td>IB COB MANAGEMENT SCREEN</td>
</tr>
<tr class="odd">
<td>IBCECOB3</td>
<td>COB MANAGEMENT REPORT</td>
</tr>
<tr class="even">
<td>IBCECOB4</td>
<td>IB EM MANAGEMENT - REVIEW STATUS SCREEN</td>
</tr>
<tr class="odd">
<td>IBCECOB5</td>
<td>IB COB MANAGEMENT SCREEN</td>
</tr>
<tr class="even">
<td>IBCECOB6</td>
<td>IB COB MANAGEMENT SCREEN</td>
</tr>
<tr class="odd">
<td>IBCECSA</td>
<td>IB CLAIMS STATUS AWAITING RESOLUTION SCREEN</td>
</tr>
<tr class="even">
<td>IBCECSA1</td>
<td>IB STATUS AWAITING RESOLUTION SCREEN</td>
</tr>
<tr class="odd">
<td>IBCECSA2</td>
<td>IB CLAIMS STATUS AWAITING RESOLUTION SCREEN</td>
</tr>
<tr class="even">
<td>IBCECSA3</td>
<td>CLAIMS STATUS AWAITING RESOLUTION REPORT</td>
</tr>
<tr class="odd">
<td>IBCECSA4</td>
<td>IB CLAIMS STATUS AWAITING RESOLUTION SCREEN</td>
</tr>
<tr class="even">
<td>IBCECSA5</td>
<td>VIEW EOB SCREEN</td>
</tr>
<tr class="odd">
<td>IBCECSA6</td>
<td>VIEW EOB SCREEN</td>
</tr>
<tr class="even">
<td>IBCECSA6</td>
<td>VIEW EOB SCREEN</td>
</tr>
<tr class="odd">
<td>IBCECSA7</td>
<td>VIEW EOB SCREEN CONTINUED</td>
</tr>
<tr class="even">
<td>IBCEDC</td>
<td>EDI CLAIM STATUS REPORT COMPILE</td>
</tr>
<tr class="odd">
<td>IBCEDP</td>
<td>EDI CLAIM STATUS REPORT PRINT</td>
</tr>
<tr class="even">
<td>IBCEDS</td>
<td>EDI CLAIM STATUS REPORT - SELECTION</td>
</tr>
<tr class="odd">
<td>IBCEDS1</td>
<td>EDI CLAIM STATUS REPORT - SELECTION CONT</td>
</tr>
<tr class="even">
<td>IBCEF, IBCEF1, IBCEF11, IBCEF12, IBCEF2, IBCEF21, IBCEF22, IBCEF3, IBCEF31</td>
<td>Routines used for formatting UB-92/HCFA 1500 forms, and Dental 835D transaction</td>
</tr>
<tr class="odd">
<td>IBCEF4</td>
<td>MRA / EDI ACTIVATED UTILITIES</td>
</tr>
<tr class="even">
<td>IBCEF5</td>
<td>MRA / EDI ACTIVATED UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEF51</td>
<td>MRA/ EDI ACTIVATED UTILITIES CONTINUED</td>
</tr>
<tr class="even">
<td>IBCEF6</td>
<td>EDI TRANSMISSION RULES DISPLAY</td>
</tr>
<tr class="odd">
<td>IBCEF61</td>
<td>EDI TRANSMISSION RULES DEFINITION</td>
</tr>
<tr class="even">
<td>IBCEF62</td>
<td>EDI TRANSMISSION RULES BT RESTRICTIONS DISPLAY</td>
</tr>
<tr class="odd">
<td>IBCEF7</td>
<td>FORMATTER AND EXTRACTOR SPECIFIC BILL FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCEF71</td>
<td>FORMATTER AND EXTRACTOR SPECIFIC BILL FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBCEF72</td>
<td>FORMATTER AND EXTRACTOR SPECIFIC BILL FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCEF73</td>
<td>FORMATTER AND EXTRACTOR SPECIFIC BILL FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBCEF73A</td>
<td>FORMATTER AND EXTRACTOR SPECIFIC (NPI) BILL FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCEF74</td>
<td>FORMATTER/EXTRACT BILL FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBCEF74A</td>
<td>PROVIDER ID MAINT ?ID CONTINUATION</td>
</tr>
<tr class="even">
<td>IBCEF75</td>
<td>PROVIDER ID FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBCEF76</td>
<td>PROVIDER ID FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCEF77</td>
<td>FORMATTER / EXTRACT BILL FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBCEF78</td>
<td>Provider ID functions</td>
</tr>
<tr class="even">
<td>IBCEF79</td>
<td>BILLING PROVIDER FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBCEF80</td>
<td>PROVIDER ID FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCEF81</td>
<td>PROVIDER ADJUSTMENTS</td>
</tr>
<tr class="odd">
<td>IBCEF82</td>
<td>PROVIDER ADJUSTMENTS</td>
</tr>
<tr class="even">
<td>IBCEF83</td>
<td>GET PROVIDER FUNCTIONS</td>
</tr>
<tr class="odd">
<td>IBCEF84</td>
<td>GET PROVIDER FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCEFG</td>
<td>OUTPUT FORMATTER EXTRACT</td>
</tr>
<tr class="odd">
<td>IBCEFG0</td>
<td>FORMS GENERATOR EXTRACT (CONT)</td>
</tr>
<tr class="even">
<td>IBCEFG1</td>
<td>OUTPUT FORMATTER DATA DEFINITION UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEFG3</td>
<td>OUTPUT FORMATTER MAINT - SCREEN BLD UTILITIES</td>
</tr>
<tr class="even">
<td>IBCEFG4</td>
<td>OUTPUT FORMATTER MAINTENANCE - FORM ACTION PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCEFG41</td>
<td>OUTPUT FORMATTER MAINT - ACT PROC (CONT)</td>
</tr>
<tr class="even">
<td>IBCEFG5</td>
<td>OUTPUT FORMATTER MAINT -FLD SCREEN BLD UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEFG6</td>
<td>OUTPUT FORMATTER MAINT-FORM FLD ACTION PROCESSING</td>
</tr>
<tr class="even">
<td>IBCEFG60</td>
<td>OUTPUT FORMATTER-FORM FLD ACTION PROCESSING (CONT)</td>
</tr>
<tr class="odd">
<td>IBCEFG61</td>
<td>OUTPUT FORMATTER MAINT-FORM FLD ACTION PROCESSING (CONT)</td>
</tr>
<tr class="even">
<td>IBCEFG7</td>
<td>OUTPUT FORMATTER GENERIC FORM PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCEFG70</td>
<td>OUTPUT FORMATTER GENERIC SCREEN PROCESSING</td>
</tr>
<tr class="even">
<td>IBCEFG8</td>
<td>OUTPUT FORMATTER GENERIC FORM TEST PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCEFP</td>
<td>PROVIDER ID FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCEFP1</td>
<td>OUTPUT FORMATTER PROVIDER UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEM</td>
<td>837 EDI RETURN MESSAGE PROCESSING</td>
</tr>
<tr class="even">
<td>IBCEM01</td>
<td>BATCH BILLS LIST TEMPLATE</td>
</tr>
<tr class="odd">
<td>IBCEM02</td>
<td>837 EDI RESUBMIT BATCH PROCESSING</td>
</tr>
<tr class="even">
<td>IBCEM03</td>
<td>837 EDI RESUBMIT INDIVIDUAL BILL PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCEM1</td>
<td>837 EDI RETURN MESSAGE MAIN LIST TEMPLATE</td>
</tr>
<tr class="even">
<td>IBCEM2</td>
<td>837 EDI RETURN MSG EXTRACT MAIN LIST TEMPLATE</td>
</tr>
<tr class="odd">
<td>IBCEM3</td>
<td>IB ELECTRONIC MESSAGE MGMNT ACTIONS</td>
</tr>
<tr class="even">
<td>IBCEM4</td>
<td>IB ELECTRONIC MESSAGE SCREEN TEXT MAINT</td>
</tr>
<tr class="odd">
<td>IBCEMCA</td>
<td>Multiple CSA Message Management</td>
</tr>
<tr class="even">
<td>IBCEMCA1</td>
<td>Multiple CSA Message Management - Actions</td>
</tr>
<tr class="odd">
<td>IBCEMCA2</td>
<td>Multiple CSA Message Management - Actions</td>
</tr>
<tr class="even">
<td>IBCEMCA3</td>
<td>Multiple CSA Message Management - Actions</td>
</tr>
<tr class="odd">
<td>IBCEMCL</td>
<td>Multiple CSA Message Management</td>
</tr>
<tr class="even">
<td>IBCEMMR</td>
<td>IB MRA Report of Patients w/o Medicare WNR</td>
</tr>
<tr class="odd">
<td>IBCEMPRG</td>
<td>Purge Status Messages</td>
</tr>
<tr class="even">
<td>IBCEMQA</td>
<td>MRA QUIET BILL AUTHORIZATION</td>
</tr>
<tr class="odd">
<td>IBCEMQC</td>
<td>MRA EOB CRITERIA FOR AUTO-AUTHORIZE</td>
</tr>
<tr class="even">
<td>IBCEMRA</td>
<td>837 MEDICARE MRA UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEMRAA</td>
<td>MEDICARE REMITTANCE ADVICE DETAIL-PART A</td>
</tr>
<tr class="even">
<td>IBCEMRAB</td>
<td>MEDICARE REMITTANCE ADVICE DETAIL-PART B</td>
</tr>
<tr class="odd">
<td>IBCEMRAX</td>
<td>MEDICARE REMITTANCE ADVICE DETAIL-PART A Cont’d</td>
</tr>
<tr class="even">
<td>IBCEMSG</td>
<td>EDI PURGE STATUS MESSAGES</td>
</tr>
<tr class="odd">
<td>IBCEMSG1</td>
<td>EDI PURGE STATUS MESSAGES CONT.</td>
</tr>
<tr class="even">
<td>IBCEMSG2</td>
<td>EDI PURGE STATUS MESSAGES CONT.</td>
</tr>
<tr class="odd">
<td>IBCEMSR</td>
<td>MRA STATISTICS REPORT</td>
</tr>
<tr class="even">
<td>IBCEMSR1</td>
<td>MRA STATISTICS REPORT CONT.</td>
</tr>
<tr class="odd">
<td>IBCEMSR2</td>
<td>non-MRA PRODUCTIVITY REPORT</td>
</tr>
<tr class="even">
<td>IBCEMSR3</td>
<td>non-MRA PRODUCTIVITY REPORT</td>
</tr>
<tr class="odd">
<td>IBCEMSR6</td>
<td>IB PRINTED CLAIMS REPORT - Sort</td>
</tr>
<tr class="even">
<td>IBCEMSR7</td>
<td>IB PRINTED CLAIMS REPORT - Print</td>
</tr>
<tr class="odd">
<td>IBCEMSRI</td>
<td>RPC FOR IENS LIST AND CLAIM DATA FOR TAS PRINTED CLAIMS REPORT</td>
</tr>
<tr class="even">
<td>IBCEMSRP</td>
<td>IB PRINTED CLAIMS REPORT</td>
</tr>
<tr class="odd">
<td>IBCEMU1</td>
<td>IB MRA UTILITY</td>
</tr>
<tr class="even">
<td>IBCEMU2</td>
<td>IB MRA Utility</td>
</tr>
<tr class="odd">
<td>IBCEMU3</td>
<td>MRA UTILITY - INS CO CHECKER</td>
</tr>
<tr class="even">
<td>IBCEMU4</td>
<td>MRA UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEMVU</td>
<td>STAND-ALONE VIEW MRA EOB</td>
</tr>
<tr class="even">
<td>IBCEOB</td>
<td>835 EDI EOB MESSAGE PROCESSING (record types 5,6,10, 12, 13, and 17)</td>
</tr>
<tr class="odd">
<td>IBCEOB</td>
<td>835 EDI EOB MESSAGE PROCESSING</td>
</tr>
<tr class="even">
<td>IBCEOB0</td>
<td>835 EDI EOB MESSAGE PROCESSING (record types 30, 40, 41, 42, 45, and 46)</td>
</tr>
<tr class="odd">
<td>IBCEOB00</td>
<td>835 EDI EOB MESSAGE PROCESSING (record types 15, 20, 35, 37)</td>
</tr>
<tr class="even">
<td>IBCEOB01</td>
<td>835 EDI EOB MESSAGE PROCESSING (patient and insurance information)</td>
</tr>
<tr class="odd">
<td>IBCEOB1</td>
<td>835 EDI EOB MESSAGE PROCESSING (record type HDR)</td>
</tr>
<tr class="even">
<td>IBCEOB2</td>
<td>EOB LIST FOR MANUAL MAINTENANCE</td>
</tr>
<tr class="odd">
<td>IBCEOB21</td>
<td>EOB MAINTENANCE ACTIONS</td>
</tr>
<tr class="even">
<td>IBCEOB3</td>
<td>835 EDI EOB BULLETINS</td>
</tr>
<tr class="odd">
<td>IBCEOB4</td>
<td>EPAYMENTS MOVE / COPY EEOB TO NEW CLAIM</td>
</tr>
<tr class="even">
<td>IBCEOBAR</td>
<td>EOB FUNCTIONS FOR A/R</td>
</tr>
<tr class="odd">
<td>IBCEP</td>
<td>Functions for PROVIDER ID MAINT - INS CO PARAMS</td>
</tr>
<tr class="even">
<td>IBCEP0</td>
<td>Functions for PROVIDER ID MAINTENANCE</td>
</tr>
<tr class="odd">
<td>IBCEP0A</td>
<td>EDI UTILITIES for insurance assigned provider ID</td>
</tr>
<tr class="even">
<td>IBCEP0B</td>
<td>Functions for PROVIDER ID MAINTENANCE</td>
</tr>
<tr class="odd">
<td>IBCEP1</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="even">
<td>IBCEP2</td>
<td>EDI UTILITIES FOR PROVIDER ID</td>
</tr>
<tr class="odd">
<td>IBCEP2A</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="even">
<td>IBCEP2B</td>
<td>EDI UTILITIES FOR PROVIDER ID</td>
</tr>
<tr class="odd">
<td>IBCEP3</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="even">
<td>IBCEP4</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="odd">
<td>IBCEP4A</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="even">
<td>IBCEP5</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="odd">
<td>IBCEP5A</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="even">
<td>IBCEP5B</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="odd">
<td>IBCEP5C</td>
<td>EDI UTILITIES for provider ID</td>
</tr>
<tr class="even">
<td>IBCEP5D</td>
<td>EDI UTILITIES - for State License</td>
</tr>
<tr class="odd">
<td>IBCEP6</td>
<td>PROVIDER ID MAINT menu and INS CO EDIT hook</td>
</tr>
<tr class="even">
<td>IBCEP7</td>
<td>Functions for facility level PROVIDER ID MAINT</td>
</tr>
<tr class="odd">
<td>IBCEP7A</td>
<td>Functions for facility level PROVIDER ID MAINT</td>
</tr>
<tr class="even">
<td>IBCEP7B</td>
<td>Functions for PROVIDER ID</td>
</tr>
<tr class="odd">
<td>IBCEP7C</td>
<td>Functions for facility level PROVIDER ID MAINT</td>
</tr>
<tr class="even">
<td>IBCEP8</td>
<td>FUNCTIONS FOR NON-VA PROVIDER</td>
</tr>
<tr class="odd">
<td>IBCEP81</td>
<td>NPI and Taxonomy Functions</td>
</tr>
<tr class="even">
<td>IBCEP82</td>
<td>Special cross references and data entry for fields in file 355.93</td>
</tr>
<tr class="odd">
<td>IBCEP8A</td>
<td>Functions for provider ID maintenance</td>
</tr>
<tr class="even">
<td>IBCEP8B</td>
<td>FUNCTIONS FOR NON-VA PROVIDER cont’d</td>
</tr>
<tr class="odd">
<td>IBCEP8C</td>
<td>Functions for IB SILENT INTERFACE FROM FB</td>
</tr>
<tr class="even">
<td>IBCEP8C1</td>
<td>Functions for IB SILENT INTERFACE FROM FB</td>
</tr>
<tr class="odd">
<td>IBCEP9</td>
<td>MASS UPDATE OF PROVIDER ID FROM FILE OR MANUAL</td>
</tr>
<tr class="even">
<td>IBCEP9A</td>
<td>PROVIDER EXTRACT</td>
</tr>
<tr class="odd">
<td>IBCEP9B</td>
<td>UPDATE OF PROVIDER ID FROM FILE UTILITIES</td>
</tr>
<tr class="even">
<td>IBCEPA</td>
<td>Provider ID functions - Care Units</td>
</tr>
<tr class="odd">
<td>IBCEPB</td>
<td>Insurance company ID parameters</td>
</tr>
<tr class="even">
<td>IBCEPC</td>
<td>Insurance company plan type list</td>
</tr>
<tr class="odd">
<td>IBCEPCID</td>
<td>Provider ID functions</td>
</tr>
<tr class="even">
<td>IBCEPTC</td>
<td>EDI PREVIOUSLY TRANSMITTED CLAIMS</td>
</tr>
<tr class="odd">
<td>IBCEPTC0</td>
<td>EDI PREVIOUSLY TRANSMITTED CLAIMS CONT</td>
</tr>
<tr class="even">
<td>IBCEPTC1</td>
<td>EDI PREV TRANSMITTED CLAIMS REPORT OUTPUT</td>
</tr>
<tr class="odd">
<td>IBCEPTC2</td>
<td>EDI PREVIOUSLY TRANSMITTED CLAIMS LIST MGR</td>
</tr>
<tr class="even">
<td>IBCEPTC3</td>
<td>EDI PREVIOUSLY TRANSMITTED CLAIMS ACTIONS</td>
</tr>
<tr class="odd">
<td>IBCEPTM</td>
<td>FILE EDI CLAIMS TEST MESSAGES</td>
</tr>
<tr class="even">
<td>IBCEPTR</td>
<td>Test Claim Messages Report</td>
</tr>
<tr class="odd">
<td>IBCEPTU</td>
<td>TEST TRANSMIT CLAIMS UTILITIES</td>
</tr>
<tr class="even">
<td>IBCEPU</td>
<td>Functions for PROVIDER ID MAINTENANCE</td>
</tr>
<tr class="odd">
<td>IBCEQ1</td>
<td>BSL,PROVIDER ID QUERY</td>
</tr>
<tr class="even">
<td>IBCEQ1A</td>
<td>PROVIDER ID QUERY REPORT</td>
</tr>
<tr class="odd">
<td>IBCEQ2</td>
<td>PROVIDER / BILLING ID WORKSHEET</td>
</tr>
<tr class="even">
<td>IBCEQ2A</td>
<td>PROVIDER / BILLING ID WORKSHEET SOLUTIONS</td>
</tr>
<tr class="odd">
<td>IBCEQBS</td>
<td>837 EDI QUERY BATCH STATUS REPORTS</td>
</tr>
<tr class="even">
<td>IBCERP1</td>
<td>BILL AWAITING RESUBMISSION REPORT</td>
</tr>
<tr class="odd">
<td>IBCERP2</td>
<td>ELECTRONIC ERROR REPORT</td>
</tr>
<tr class="even">
<td>IBCERP3</td>
<td>EDI BATCHES WAITING MORE THAN 1 DAY REPORT</td>
</tr>
<tr class="odd">
<td>IBCERP4</td>
<td>EDI RECEIPT / REJECTION MSGS STILL PENDING / UPDATNG</td>
</tr>
<tr class="even">
<td>IBCERP5</td>
<td>BATCH LIST</td>
</tr>
<tr class="odd">
<td>IBCERP6</td>
<td>MRA / EDI CLAIMS READY FOR EXTRACT</td>
</tr>
<tr class="even">
<td>IBCERP6A</td>
<td>READY FOR EXTRACT LIST MANAGER REPORT</td>
</tr>
<tr class="odd">
<td>IBCERP7</td>
<td>HCCH PAYER ID REPORT (IB*2.0*577)</td>
</tr>
<tr class="even">
<td>IBCERPN</td>
<td>RPN Resubmission/Printing Claims No Changes CSA Report</td>
</tr>
<tr class="odd">
<td>IBCERPT</td>
<td>277 EDI ENVOY REPORT MESSAGE PROCESSING</td>
</tr>
<tr class="even">
<td>IBCERPT1</td>
<td>ELECTRONIC REPORT DISPOSITION</td>
</tr>
<tr class="odd">
<td>IBCESRV</td>
<td>Server interface to IB from Austin</td>
</tr>
<tr class="even">
<td>IBCESRV1</td>
<td>Server interface to IB from Austin</td>
</tr>
<tr class="odd">
<td>IBCESRV2</td>
<td>Server based Auto-update utilities - IB EDI</td>
</tr>
<tr class="even">
<td>IBCESRV3</td>
<td>Server based Auto-update utilities - IB EDI</td>
</tr>
<tr class="odd">
<td>IBCEST</td>
<td>837 EDI STATUS MESSAGE PROCESSING</td>
</tr>
<tr class="even">
<td>IBCEST1</td>
<td>IB 837 EDI Status Message Processing Cont.</td>
</tr>
<tr class="odd">
<td>IBCEU</td>
<td>EDI UTILITIES</td>
</tr>
<tr class="even">
<td>IBCEU0</td>
<td>EDI UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEU1</td>
<td>EDI UTILITIES FOR EOB PROCESSING</td>
</tr>
<tr class="even">
<td>IBCEU2</td>
<td>EDI UTILITIES FOR AUTO ADD OF CODES ON BILL</td>
</tr>
<tr class="odd">
<td>IBCEU3</td>
<td>EDI UTILITIES FOR 1500 CLAIM FORM</td>
</tr>
<tr class="even">
<td>IBCEU4</td>
<td>EDI UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCEU5</td>
<td>EDI UTILITIES (CONTINUED) FOR CMS-1500</td>
</tr>
<tr class="even">
<td>IBCEU6</td>
<td>EDI UTILITIES FOR EOB PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCEU7</td>
<td>EDI UTILITIES</td>
</tr>
<tr class="even">
<td>IBCEXTR</td>
<td>CLAIMS READY FOR EXTRACT MANAGEMENT SCREEN</td>
</tr>
<tr class="odd">
<td>IBCEXTR1</td>
<td>IB READY FOR EXTRACT STATUS SCREEN</td>
</tr>
<tr class="even">
<td>IBCEXTR2</td>
<td>IB EXTRACT STATUS MANAGEMENT</td>
</tr>
<tr class="odd">
<td>IBCEXTRP</td>
<td>VIEW / PRINT EDI EXTRACT DATA</td>
</tr>
<tr class="even">
<td>IBCF</td>
<td>Dispatch to print claim forms.</td>
</tr>
<tr class="odd">
<td>IBCF1, IBCF10, IBCF11, IBCF12, IBCF14</td>
<td>Print UB-82. (Routines formerly named DGCRP, DGCRP0, DGCRP1, DGCRP2, and DGCRP4.)</td>
</tr>
<tr class="even">
<td>IBCF13</td>
<td>Call for Accounts Receivable to print bills. (Routine formerly named DGCRP3.)</td>
</tr>
<tr class="odd">
<td>IBCF1TP</td>
<td>UB-82 Test Pattern Print. (Routine formerly named DGCRTP.)</td>
</tr>
<tr class="even">
<td>IBCF2, IBCF21, IBCF22, IBCF23, IBCF2P</td>
<td>Print HCFA 1500.</td>
</tr>
<tr class="odd">
<td>IBCF23A</td>
<td>HCFA 1500 19-90 DATA - SPLIT FROM IBCF23</td>
</tr>
<tr class="even">
<td>IBCF2TP</td>
<td>Print HCFA 1500 Test Pattern Print</td>
</tr>
<tr class="odd">
<td>IBCF3, IBCF31, IBCF32, IBCF33, IBCF331, IBCF34, IBCF3P</td>
<td>Print UB-92</td>
</tr>
<tr class="even">
<td>IBCF3TP</td>
<td>UB-92 Test Pattern Print</td>
</tr>
<tr class="odd">
<td>IBCF4</td>
<td>Print Bill Addendum</td>
</tr>
<tr class="even">
<td>IBCFP</td>
<td>Print all authorized bills in order</td>
</tr>
<tr class="odd">
<td>IBCFP1</td>
<td>PRINT AUTHORIZED BILLS IN ORDER</td>
</tr>
<tr class="even">
<td>IBCIADD1</td>
<td>ADD ENTRY TO FILE 351.9</td>
</tr>
<tr class="odd">
<td>IBCIASN</td>
<td>STANDALONE OPTION TO RE-ASSIGN CLAIMS</td>
</tr>
<tr class="even">
<td>IBCIBW</td>
<td>IBCI CLAIMS MANAGER MGR WORKSHEET</td>
</tr>
<tr class="odd">
<td>IBCICL</td>
<td>IBCI CLAIMS MANAGER CLERK WORKSHEET</td>
</tr>
<tr class="even">
<td>IBCICME</td>
<td>IBCI CLAIMSMANAGER ERROR REPORT</td>
</tr>
<tr class="odd">
<td>IBCICME1</td>
<td>IBCI CLAIMSMANAGER ERROR REPORT</td>
</tr>
<tr class="even">
<td>IBCICMEP</td>
<td>ClaimsManager ERROR REPORT</td>
</tr>
<tr class="odd">
<td>IBCICMS</td>
<td>IBCI CLAIMSMANAGER STATUS REPORT</td>
</tr>
<tr class="even">
<td>IBCICMSP</td>
<td>ClaimsManager STATUS REPORT</td>
</tr>
<tr class="odd">
<td>IBCICMW</td>
<td>CLAIMSMANAGER WORKSHEET REPORT</td>
</tr>
<tr class="even">
<td>IBCIL0</td>
<td>CLAIMSMANAGER SKIP LIST</td>
</tr>
<tr class="odd">
<td>IBCIMG</td>
<td>IBCI CLAIMS MANAGER MGR WORKSHEET</td>
</tr>
<tr class="even">
<td>IBCIMSG</td>
<td>BUILD MESSAGE FOR CLAIMSMANAGER</td>
</tr>
<tr class="odd">
<td>IBCIMSG1</td>
<td>BUILD MESSAGE FOR CLAIMSMANAGER CONT'D</td>
</tr>
<tr class="even">
<td>IBCINPT</td>
<td>Extract data and create NPT file</td>
</tr>
<tr class="odd">
<td>IBCIPAY</td>
<td>Extract data and create Ingenix Payer File</td>
</tr>
<tr class="even">
<td>IBCIPOST</td>
<td>CLAIMSMANAGER POST INSTALL</td>
</tr>
<tr class="odd">
<td>IBCISC</td>
<td>IB EDIT SCREENS ?CLA FUNCTIONALITY</td>
</tr>
<tr class="even">
<td>IBCIST</td>
<td>ENTRY POINTS FOR CLAIMSMANAGER INTERFACE</td>
</tr>
<tr class="odd">
<td>IBCIUDF</td>
<td>CLAIMSMANAGER USER DEFINED FIELDS</td>
</tr>
<tr class="even">
<td>IBCIUT1</td>
<td>MISC UTILITIES FOR CLAIMSMANAGER INTERFACE</td>
</tr>
<tr class="odd">
<td>IBCIUT2</td>
<td>CLAIMSMANAGER MESSAGE UTILITIES</td>
</tr>
<tr class="even">
<td>IBCIUT3</td>
<td>TCP/IP UTILITIES FOR CLAIMSMANAGER INTERFACE</td>
</tr>
<tr class="odd">
<td>IBCIUT4</td>
<td>MISC UTILITIES</td>
</tr>
<tr class="even">
<td>IBCIUT5</td>
<td>UTILITIES FOR CLAIMSMANAGER INTERFACE</td>
</tr>
<tr class="odd">
<td>IBCIUT6</td>
<td>MAILMAN UTILITIES</td>
</tr>
<tr class="even">
<td>IBCIUT7</td>
<td>COMMENTS FIELD UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCIWK</td>
<td>WORKSHEET UTILITY</td>
</tr>
<tr class="even">
<td>IBCMENU</td>
<td>Main menu driver. (Routine formerly named DGCRMENU.)</td>
</tr>
<tr class="odd">
<td>IBCMDT</td>
<td>IBCN INS PLANS MISSING DATA Insurance Missing Data Report (Driver)</td>
</tr>
<tr class="even">
<td>IBCMDT1</td>
<td>IBCN INS PLANS MISSING DATA Insurance Missing Data Report (Driver 1)</td>
</tr>
<tr class="odd">
<td>IBCMDT2</td>
<td>IBCN INS PLANS MISSING DATA Insurance Missing Data Report (Compile)</td>
</tr>
<tr class="even">
<td>IBCMDT3</td>
<td>IBCN INS PLANS MISSING DATA Insurance Missing Data Report (Print)</td>
</tr>
<tr class="odd">
<td>IBCN118</td>
<td>Data Dictionary trigger logic for comments</td>
</tr>
<tr class="even">
<td>IBCNADD</td>
<td>Address Retrieval Engine for BILL/CLAIMS file (#399).</td>
</tr>
<tr class="odd">
<td>IBCNAU</td>
<td>User Edit Report</td>
</tr>
<tr class="even">
<td>IBCNAU1</td>
<td>User Edit Report</td>
</tr>
<tr class="odd">
<td>IBCNAU2</td>
<td>User Edit Report</td>
</tr>
<tr class="even">
<td>IBCNAU3</td>
<td>User Edit Report</td>
</tr>
<tr class="odd">
<td>IBCNBAA</td>
<td>This program displays subscriber registration information from the Insurance Buffer, IIV Response Report file, and Annual Benefits file (#355.4).</td>
</tr>
<tr class="even">
<td>IBCNBAC</td>
<td>Ins Buffer: Individually Accept Insurance Buffer Fields</td>
</tr>
<tr class="odd">
<td>IBCNBAR</td>
<td>Ins Buffer: process Accept and Reject</td>
</tr>
<tr class="even">
<td>IBCNBCD</td>
<td>Ins Buffer: display / compare buffer and existing ins</td>
</tr>
<tr class="odd">
<td>IBCNBCD1</td>
<td>This program edits subscriber information in the Patient Insurance subfile (File #2.312).</td>
</tr>
<tr class="even">
<td>IBCNBCD2</td>
<td>This program sets up the Insurance Buffer to process Accepts.</td>
</tr>
<tr class="odd">
<td>IBCNBCD3</td>
<td>This program displays IB Annual Benefits / Coverage Limitations Display Screens.</td>
</tr>
<tr class="even">
<td>IBCNBCD4</td>
<td>This program is part of Subscriber Display Screens.</td>
</tr>
<tr class="odd">
<td>IBCNBCD5</td>
<td>This program is part of Subscriber Display Screens.</td>
</tr>
<tr class="even">
<td>IBCNBCD6</td>
<td>This program is part of Subscriber Display Screens.</td>
</tr>
<tr class="odd">
<td>IBCNBCD7</td>
<td>This program is part of Subscriber Display Screens.</td>
</tr>
<tr class="even">
<td>IBCNBCD8</td>
<td>This program is part of Subscriber Display Screen Fields.</td>
</tr>
<tr class="odd">
<td>IBCNBED</td>
<td>Ins Buffer: delete existing entries in buffer</td>
</tr>
<tr class="even">
<td>IBCNBEE</td>
<td>Ins Buffer: add / edit existing entries in buffer</td>
</tr>
<tr class="odd">
<td>IBCNBES</td>
<td>Ins Buffer: stuff new entries / data into buffer</td>
</tr>
<tr class="even">
<td>IBCNBES1</td>
<td>Ins Buffer: stuff new entries / data into buffer</td>
</tr>
<tr class="odd">
<td>IBCNBLA</td>
<td>Ins Buffer: LM action calls</td>
</tr>
<tr class="even">
<td>IBCNBLA1</td>
<td>Ins Buffer: LM action calls (cont.)</td>
</tr>
<tr class="odd">
<td>IBCNBLA2</td>
<td>Ins Buffer, Multiple Selection</td>
</tr>
<tr class="even">
<td>IBCNBLB</td>
<td>Ins Buffer: Eligibility / Benefit screen</td>
</tr>
<tr class="odd">
<td>IBCNBLE</td>
<td>Ins Buffer: LM buffer entry screen</td>
</tr>
<tr class="even">
<td>IBCNBLE1</td>
<td>Ins Buffer, Expand Entry, continued</td>
</tr>
<tr class="odd">
<td>IBCNBLL</td>
<td>Ins Buffer: LM main screen, list buffer entries</td>
</tr>
<tr class="even">
<td>IBCNBLP</td>
<td>Ins Buffer: LM buffer process screen</td>
</tr>
<tr class="odd">
<td>IBCNBLP1</td>
<td>Ins Buffer: LM buffer process build</td>
</tr>
<tr class="even">
<td>IBCNBME</td>
<td>Ins Buffer: external entry points, add / edit buffer</td>
</tr>
<tr class="odd">
<td>IBCNBMI</td>
<td>Ins Buffer: move buffer data to insurance files</td>
</tr>
<tr class="even">
<td>IBCNBMN</td>
<td>Ins Buffer: add new insurance file entries</td>
</tr>
<tr class="odd">
<td>IBCNBOA</td>
<td>Ins Buffer: Activity Report</td>
</tr>
<tr class="even">
<td>IBCNBOE</td>
<td>Ins Buffer: Employee Report</td>
</tr>
<tr class="odd">
<td>IBCNBOF</td>
<td>Ins Buffer: Employee Report (Entered)</td>
</tr>
<tr class="even">
<td>IBCNBPG</td>
<td>Ins Buffer: Option Purge stub entries</td>
</tr>
<tr class="odd">
<td>IBCNBU1</td>
<td>Ins Buffer: Utilities</td>
</tr>
<tr class="even">
<td>IBCNBUH</td>
<td>Ins Buffer: Help Text</td>
</tr>
<tr class="odd">
<td>IBCNCH</td>
<td>Patient Policy Subscriber Comments (Driver)</td>
</tr>
<tr class="even">
<td>IBCNCH2</td>
<td>Patient Policy Subscriber Comments (Driver 1, Comment Search)</td>
</tr>
<tr class="odd">
<td>IBCNCH3</td>
<td>Patient Policy Subscriber Comments (Comment Search)</td>
</tr>
<tr class="even">
<td>IBCNEAMC</td>
<td>IIV AUTO MATCH BUFFER LISTING</td>
</tr>
<tr class="odd">
<td>IBCNEAME</td>
<td>IIV AUTO MATCH ENTRY / EDIT</td>
</tr>
<tr class="even">
<td>IBCNEAMI</td>
<td>IIV AUTO MATCH INPUT TRANSFORM</td>
</tr>
<tr class="odd">
<td>IBCNEBF</td>
<td>Create an Entry in the Buffer File</td>
</tr>
<tr class="even">
<td>IBCNEDE</td>
<td>eIV DATA EXTRACTS (main driver for eIV processing at night)</td>
</tr>
<tr class="odd">
<td>IBCNEDE1</td>
<td>eIV INSURANCE BUFFER EXTRACT</td>
</tr>
<tr class="even">
<td>IBCNEDE2</td>
<td>eIV PRE REG EXTRACT (APPTS)</td>
</tr>
<tr class="odd">
<td>IBCNEDE4</td>
<td>eIV Electronic Insurance Coverage Discovery (EICD)</td>
</tr>
<tr class="even">
<td>IBCNEDE5</td>
<td>eIV DATA EXTRACTS</td>
</tr>
<tr class="odd">
<td>IBCNEDE6</td>
<td>eIV DATA EXTRACTS</td>
</tr>
<tr class="even">
<td>IBCNEDE7</td>
<td>eIV DATA EXTRACTS</td>
</tr>
<tr class="odd">
<td>IBCNEDEP</td>
<td>Process Transaction Records</td>
</tr>
<tr class="even">
<td>IBCNEDEQ</td>
<td>Process eIV Transactions continued</td>
</tr>
<tr class="odd">
<td>IBCNEDST</td>
<td>HL7 Registration Message Statistics</td>
</tr>
<tr class="even">
<td>IBCNEHL1</td>
<td>HL7 Process Incoming RPI Messages</td>
</tr>
<tr class="odd">
<td>IBCNEHL2</td>
<td>HL7 Process Incoming RPI Messages (cont.)</td>
</tr>
<tr class="even">
<td>IBCNEHL3</td>
<td>HL7 Process Incoming RPI Continued</td>
</tr>
<tr class="odd">
<td>IBCNEHL4</td>
<td>HL7 Process Incoming RPI Messages (cont.)</td>
</tr>
<tr class="even">
<td>IBCNEHL5</td>
<td>HL7 Process Incoming RPI Messages</td>
</tr>
<tr class="odd">
<td>IBCNEHL6</td>
<td>HL7 Process Incoming RPI Continued</td>
</tr>
<tr class="even">
<td>IBCNEHL7</td>
<td>HL7 Process Incoming 271 Messages Continued</td>
</tr>
<tr class="odd">
<td>IBCNEHLD</td>
<td>IIV Deactivate MFN Message</td>
</tr>
<tr class="even">
<td>IBCNEHLI</td>
<td>Incoming HL7 messages</td>
</tr>
<tr class="odd">
<td>IBCNEHLK</td>
<td>HL7 Acknowledgement Messages</td>
</tr>
<tr class="even">
<td>IBCNEHLM</td>
<td>HL7 Registration MFN Message</td>
</tr>
<tr class="odd">
<td>IBCNEHLO</td>
<td>Outgoing HL7 messages</td>
</tr>
<tr class="even">
<td>IBCNEHLQ</td>
<td>HL7 RQI Message</td>
</tr>
<tr class="odd">
<td>IBCNEHLT</td>
<td>HL7 Process Incoming MFN Messages</td>
</tr>
<tr class="even">
<td>IBCNEHLU</td>
<td>HL7 Utilities</td>
</tr>
<tr class="odd">
<td>IBCNEKI2</td>
<td>PURGE eIV DATA FILES CONT'D</td>
</tr>
<tr class="even">
<td>IBCNEKIT</td>
<td>PURGE eIV DATA FILES</td>
</tr>
<tr class="odd">
<td>IBCNEML</td>
<td>MAILMAN NOTIFICATION TO LINK PAYERS</td>
</tr>
<tr class="even">
<td>IBCNEMS1</td>
<td>Consolidated Mailman messages</td>
</tr>
<tr class="odd">
<td>IBCNEPM</td>
<td>PAYER MAINTENANCE PAYER LIST SCREEN</td>
</tr>
<tr class="even">
<td>IBCNEPM1</td>
<td>PAYER MAINT / INS COMPANY LIST FOR PAYER</td>
</tr>
<tr class="odd">
<td>IBCNEPM2</td>
<td>PAYER MAINTENANCE ENTRY POINT</td>
</tr>
<tr class="even">
<td>IBCNEPY</td>
<td>eIV PAYER EDIT OPTION</td>
</tr>
<tr class="odd">
<td>IBCNEQU</td>
<td>eIV REQUEST ELECTRONIC INSURANCE INQUIRY</td>
</tr>
<tr class="even">
<td>IBCNEQU1</td>
<td>Continuation of IBCNEQU</td>
</tr>
<tr class="odd">
<td>IBCNERP0</td>
<td>IBCNE eIV STATISTICAL REPORT (cont’d)</td>
</tr>
<tr class="even">
<td>IBCNERP1</td>
<td>IBCNE USER IF eIV RESPONSE REPORT</td>
</tr>
<tr class="odd">
<td>IBCNERP2</td>
<td>IBCNE eIV RESPONSE REPORT COMPILE</td>
</tr>
<tr class="even">
<td>IBCNERP3</td>
<td>IBCNE eIV RESPONSE REPORT PRINT</td>
</tr>
<tr class="odd">
<td>IBCNERP4</td>
<td>IBCNE USER INTERFACE eIV PAYER REPORT</td>
</tr>
<tr class="even">
<td>IBCNERP5</td>
<td>IBCNE eIV PAYER REPORT COMPILE</td>
</tr>
<tr class="odd">
<td>IBCNERP6</td>
<td>eIV PAYER REPORT PRINT</td>
</tr>
<tr class="even">
<td>IBCNERP7</td>
<td>eIV STATISTICAL REPORT</td>
</tr>
<tr class="odd">
<td>IBCNERP8</td>
<td>IBCNE eIV STATISTICAL REPORT COMPILE</td>
</tr>
<tr class="even">
<td>IBCNERP9</td>
<td>eIV STATISTICAL REPORT PRINT</td>
</tr>
<tr class="odd">
<td>IBCNERPA</td>
<td>IBCNE eIV RESPONSE REPORT (cont'd)</td>
</tr>
<tr class="even">
<td>IBCNERPB</td>
<td>PAYER LINK REPORT</td>
</tr>
<tr class="odd">
<td>IBCNERPC</td>
<td>PAYER LINK REPORT continued</td>
</tr>
<tr class="even">
<td>IBCNERPD</td>
<td>INSURANCE COMPANY LINK REPORT</td>
</tr>
<tr class="odd">
<td>IBCNERPE</td>
<td>IBCNE eIV RESPONSE REPORT (cont'd)</td>
</tr>
<tr class="even">
<td>IBCNERPF</td>
<td>IBCNE USER INTERFACE EIV INSURANCE UPDATE REPORT</td>
</tr>
<tr class="odd">
<td>IBCNERPG</td>
<td>IBCNE EIV INSURANCE UPDATE REPORT COMPILE</td>
</tr>
<tr class="even">
<td>IBCNERPH</td>
<td>IBCNE EIV INSURANCE UPDATE REPORT PRINT</td>
</tr>
<tr class="odd">
<td>IBCNERPI</td>
<td>IBCNE eIV Secondary Insurance Report Print</td>
</tr>
<tr class="even">
<td>IBCNERPJ</td>
<td>HL7 Response Report</td>
</tr>
<tr class="odd">
<td>IBCNERPK</td>
<td>HL7 Response Report</td>
</tr>
<tr class="even">
<td>IBCNERPL</td>
<td>HL7 Response Report</td>
</tr>
<tr class="odd">
<td>IBCNERPM</td>
<td>IBCNE EIV PAYER DOD REPORT</td>
</tr>
<tr class="even">
<td>IBCNERTC</td>
<td>Covered by Health Insurance</td>
</tr>
<tr class="odd">
<td>IBCNERTQ</td>
<td>Real-time Insurance Verification</td>
</tr>
<tr class="even">
<td>IBCNERTU</td>
<td>eIV Processing Real-Time Inquiries</td>
</tr>
<tr class="odd">
<td>IBCNES</td>
<td>eIV eligibility / Benefit screen</td>
</tr>
<tr class="even">
<td>IBCNES1</td>
<td>eIV eligibility / Benefit utilities</td>
</tr>
<tr class="odd">
<td>IBCNES2</td>
<td>eIV eligibility / Benefit action protocols</td>
</tr>
<tr class="even">
<td>IBCNES3</td>
<td>Eligibility / Benefits screen action protocols, cont.</td>
</tr>
<tr class="odd">
<td>IBCNES4</td>
<td>eIV elig/Benefit screen</td>
</tr>
<tr class="even">
<td>IBCNESI</td>
<td>Potential Medicare COB Prompts</td>
</tr>
<tr class="odd">
<td>IBCNESI1</td>
<td>MEDICARE POTENTIAL COB Patient Selection</td>
</tr>
<tr class="even">
<td>IBCNESI2</td>
<td>MEDICARE PATIENTS WITH SUBSEQUENT INSURANCE</td>
</tr>
<tr class="odd">
<td>IBCNETST</td>
<td>eIV Gate-keeper test scenarios</td>
</tr>
<tr class="even">
<td>IBCNEUT1</td>
<td>IIV MISC. UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCNEUT2</td>
<td>eIV MISC. UTILITIES</td>
</tr>
<tr class="even">
<td>IBCNEUT3</td>
<td>eIV MISC. UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCNEUT4</td>
<td>eIV MISC. UTILITIES</td>
</tr>
<tr class="even">
<td>IBCNEUT5</td>
<td>eIV MISC. UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCNEUT6</td>
<td>IIV MISC. UTILITIES</td>
</tr>
<tr class="even">
<td>IBCNEUT7</td>
<td>IIV MISC. UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCNEUT8</td>
<td>eIV MISC. UTILITIES</td>
</tr>
<tr class="even">
<td>IBCNFCON</td>
<td>This routine is called for eII Configuration Edit option to change eII configuration parameters.</td>
</tr>
<tr class="odd">
<td>IBCNFRD</td>
<td>Gets the Result file messages and Extract file’s confirmation messages from AITC DMI Queue, and then it creates the Result file.</td>
</tr>
<tr class="even">
<td>IBCNFRD2</td>
<td>Builds the XML file from Result file messages.</td>
</tr>
<tr class="odd">
<td>IBCNFSND</td>
<td>Sends Extract files as MailMan messages to AITC DMI Queue. Notifies IBCNF EII IRM mail group if confirmation messages are not received from AITC DMI queue for given Extract file messages within given time frame and re-sends those messages to AITC DMI Queue. Checks to make sure the Extract files and Result files are created on time; if not, sends warning message to IBCNF EII IRM mail group. Also purges the Activity logs of HMS EXTRACT FILE STATUS and HMS RESULT FILE STATUS that are older than 180 days.</td>
</tr>
<tr class="even">
<td>IBCNGP</td>
<td>Report of Coverage Limitations (Main Driver, Prompts)</td>
</tr>
<tr class="odd">
<td>IBCNGP1</td>
<td>Report of Coverage Limitations (Compile and Print)</td>
</tr>
<tr class="even">
<td>IBCNGPF</td>
<td>List Group Plans without Annual Benefits Report</td>
</tr>
<tr class="odd">
<td>IBCNGPF1</td>
<td>List Group Plans without Annual Benefits Report</td>
</tr>
<tr class="even">
<td>IBCNGPF2</td>
<td>List Group Plans without Annual Benefits Report</td>
</tr>
<tr class="odd">
<td>IBCNGPF3</td>
<td>List Group Plans without Annual Benefits Report</td>
</tr>
<tr class="even">
<td>IBCNHHLI</td>
<td>Processes incoming HL7 messages from the National Insurance File (NIF).</td>
</tr>
<tr class="odd">
<td>IBCNHHLO</td>
<td>Generates outgoing HL7 message to the National Insurance File (NIF).</td>
</tr>
<tr class="even">
<td>IBCNHSRV</td>
<td>Used by the IBCNH HPID NIF BATCH QUERY menu option (triggered by the NIFQRY mail group) to enable HL7 communication with the National Insurance File (NIF) and send a batch query to catch the system up to the data in the NIF.</td>
</tr>
<tr class="odd">
<td>IBCNHUT1</td>
<td>Utility functions for working with Health Plan Identifiers (HPID) and Other Entity Identifiers (OEID).</td>
</tr>
<tr class="even">
<td>IBCNHUT2</td>
<td>Utility functions for working with Health Plan Identifiers (HPID) and Other Entity Identifiers (OEID).</td>
</tr>
<tr class="odd">
<td>IBCNHPR</td>
<td>This program is part of the Manually Added HPIDs to Billing Claim Report.</td>
</tr>
<tr class="even">
<td>IBCNHPR1</td>
<td>This program is part of the Manually Added HPIDs to Billing Claim Report.</td>
</tr>
<tr class="odd">
<td>IBCNHPR2</td>
<td>This program is part of the Manually Added HPIDs to Billing Claim Report.</td>
</tr>
<tr class="even">
<td>IBCNICB</td>
<td>Update utilities for the ICB interface</td>
</tr>
<tr class="odd">
<td>IBCNILK</td>
<td>This routine contains the new Insurance Company Look-up Utility that is invoked from many points within the Insurance Data Capture module.</td>
</tr>
<tr class="even">
<td>IBCNINS</td>
<td>This routine is run each night via TaskMan. It controls the different processes that the eBusiness eInsurance team wants to execute after hours on a daily basis.</td>
</tr>
<tr class="odd">
<td>IBCNINSL</td>
<td>Centralized insurance look-up routine</td>
</tr>
<tr class="even">
<td>IBCNINSU</td>
<td>General insurance utilities</td>
</tr>
<tr class="odd">
<td>IBCNIUF</td>
<td>Interfacility Insurance Update (IIU) Filer. – Identifies and tracks recently verified active policies that are to be share to other VAMCs.</td>
</tr>
<tr class="even">
<td>IBCNIUH1</td>
<td>IIU RECEIVE AND PROCESS INSURANCE TRANSMISSIONS</td>
</tr>
<tr class="odd">
<td>IBCNIUHL</td>
<td>Interfacility Insurance Update (IIU) – Creates and transmits an HL7 message that contains recently verified active insurance policies to other VAMCs. Associated with the INTERFACILITY INSURANCE UPDATE file #365.19.</td>
</tr>
<tr class="even">
<td>IBCNIUK</td>
<td>Interfacility Insurance Update (IIU) – Purging of transmissions that were sent and received to / from other VAMCs. Maintains the INTERFACILITY INSURANCE UPDATE file #365.19.</td>
</tr>
<tr class="odd">
<td>IBCNIUR1</td>
<td>Interfacility Insurance Update (IIU) – Interfacility Insurance Update report.</td>
</tr>
<tr class="even">
<td>IBCNIUR2</td>
<td>Interfacility Insurance Update (IIU) – Interfacility Insurance Update report (continued).</td>
</tr>
<tr class="odd">
<td>IBCNQ</td>
<td>Patient Billing Inquiry. (Routine formerly named DGCRNQ.)</td>
</tr>
<tr class="even">
<td>IBCNQ1</td>
<td>Outpatient Visit Date Inquiry. (Routine formerly named DGCRNQ1.)</td>
</tr>
<tr class="odd">
<td>IBCNRDV</td>
<td>INSURANCE INFORMATION EXCHANGE VIA RDV</td>
</tr>
<tr class="even">
<td>IBCNRDV1</td>
<td>Select policies for interactive INSURANCE INFORMATION EXCHANGE VIA RDV</td>
</tr>
<tr class="odd">
<td>IBCNRE1</td>
<td>Edit PAYER APPLICATION Sub-file</td>
</tr>
<tr class="even">
<td>IBCNRE2</td>
<td>Edit NCPDP PROCESSOR APPLICATION Sub-file</td>
</tr>
<tr class="odd">
<td>IBCNRE3</td>
<td>Edit PHARMACY BENEFITS MANAGER (PBM) APPLICATION Sub-file</td>
</tr>
<tr class="even">
<td>IBCNRE4</td>
<td>Edit PLAN APPLICATION Sub-file</td>
</tr>
<tr class="odd">
<td>IBCNRE5</td>
<td>Edit HIPAA NCPDP ACTIVE FLAG</td>
</tr>
<tr class="even">
<td>IBCNRFM1</td>
<td>Perform FileMan API Calls</td>
</tr>
<tr class="odd">
<td>IBCNRHLT</td>
<td>Receive HL7 e-Pharmacy MFN Message</td>
</tr>
<tr class="even">
<td>IBCNRHLU</td>
<td>e-Pharmacy HL7 Utilities</td>
</tr>
<tr class="odd">
<td>IBCNRMFE</td>
<td>Receive HL7 e-Pharmacy MFE Segment</td>
</tr>
<tr class="even">
<td>IBCNRMFK</td>
<td>Send HL7 e-Pharmacy MFK Message</td>
</tr>
<tr class="odd">
<td>IBCNRP</td>
<td>Plan Match ListMan</td>
</tr>
<tr class="even">
<td>IBCNRP5</td>
<td>Group Plan Status Report</td>
</tr>
<tr class="odd">
<td>IBCNRP5P</td>
<td>Group Plan Status Report</td>
</tr>
<tr class="even">
<td>IBCNRPM1</td>
<td>Match Multiple Group Plans to a Pharmacy Plan</td>
</tr>
<tr class="odd">
<td>IBCNRPM2</td>
<td>Match Multiple Group Plans to a Pharmacy Plan</td>
</tr>
<tr class="even">
<td>IBCNRPMT</td>
<td>Match Group Plan to Pharmacy Plan</td>
</tr>
<tr class="odd">
<td>IBCNRPS</td>
<td>Match Test Payer Sheet to a Pharmacy Plan</td>
</tr>
<tr class="even">
<td>IBCNRPS2</td>
<td>Plan Match ListMan</td>
</tr>
<tr class="odd">
<td>IBCNRPSI</td>
<td>Group Plan Status Inquiry</td>
</tr>
<tr class="even">
<td>IBCNRPSM</td>
<td>Match Test Payer Sheet to a Pharmacy Plan</td>
</tr>
<tr class="odd">
<td>IBCNRRP1</td>
<td>Group Plan Worksheet Report</td>
</tr>
<tr class="even">
<td>IBCNRRP2</td>
<td>IBCNR GROUP PLAN WORKSHEET COMPILE</td>
</tr>
<tr class="odd">
<td>IBCNRRP3</td>
<td>GROUP PLAN WORKSHEET REPORT PRINT</td>
</tr>
<tr class="even">
<td>IBCNRRP4</td>
<td>Pharmacy Plan Report</td>
</tr>
<tr class="odd">
<td>IBCNRSM</td>
<td>Shared Plan Matches Report</td>
</tr>
<tr class="even">
<td>IBCNRU1</td>
<td>IB Utilities</td>
</tr>
<tr class="odd">
<td>IBCNRXI1</td>
<td>Post-Installation procedure</td>
</tr>
<tr class="even">
<td>IBCNRXI2</td>
<td>BHAM ISC/DMB - Post-Installation procedure</td>
</tr>
<tr class="odd">
<td>IBCNRZCM</td>
<td>Receive HL7 e-Pharmacy ZCM Segment</td>
</tr>
<tr class="even">
<td>IBCNRZP0</td>
<td>Receive HL7 e-Pharmacy ZP0 Segment</td>
</tr>
<tr class="odd">
<td>IBCNRZPB</td>
<td>Receive HL7 e-Pharmacy ZPB Segment</td>
</tr>
<tr class="even">
<td>IBCNRZPL</td>
<td>Receive HL7 e-Pharmacy ZPL Segment</td>
</tr>
<tr class="odd">
<td>IBCNRZPT</td>
<td>Receive HL7 e-Pharmacy ZPT Segment</td>
</tr>
<tr class="even">
<td>IBCNRZRX</td>
<td>Receive HL7 e-Pharmacy ZRX Segment</td>
</tr>
<tr class="odd">
<td>IBCNS, IBCNS1</td>
<td>These routines contain the supported calls to determine if a patient has any insurance or active insurance, to retrieve the data, and to do standard displays.</td>
</tr>
<tr class="even">
<td>IBCNS2</td>
<td>This routine contains several utilities called by data dictionary for the BILL/CLAIMS file (#399).</td>
</tr>
<tr class="odd">
<td>IBCNS3</td>
<td>DISPLAY EXTENDED INSURANCE</td>
</tr>
<tr class="even">
<td>IBCNS4</td>
<td>This routine contains the trigger logic to obtain the authorization number / referral number from the 278-transaction file (#356.22).</td>
</tr>
<tr class="odd">
<td>IBCNSA, IBCNSA0, IBCNSA1, IBCNSA2</td>
<td>These routines allow for the display and editing of the Annual Benefits available for an insurance plan.</td>
</tr>
<tr class="even">
<td>IBCNSBL, IBCNSBL1</td>
<td>This routine creates the new insurance policy mail message. It is called by the event driver whenever a new insurance policy is added.</td>
</tr>
<tr class="odd">
<td>IBCNSBL2</td>
<td>'BILL NEXT PAYOR' BULLETIN</td>
</tr>
<tr class="even">
<td>IBCNSC, IBCNSC0, IBCNSC01, IBCNSC1</td>
<td>These routines allow for the display and editing of insurance company data.</td>
</tr>
<tr class="odd">
<td>IBCNSC02</td>
<td>Insurance Company parent / child management</td>
</tr>
<tr class="even">
<td>IBCNSC2</td>
<td>INACTIVATE AND REPOINT INS STUFF</td>
</tr>
<tr class="odd">
<td>IBCNSC3</td>
<td>INACTIVATE AND REPOINT INS STUFF1</td>
</tr>
<tr class="even">
<td>IBCNSC4</td>
<td>INSURANCE PLAN DETAIL SCREEN UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCNSC41</td>
<td>INSURANCE PLAN SCREEN UTILITIES (CONT)</td>
</tr>
<tr class="even">
<td>IBCNSCD</td>
<td>DELETE INSURANCE COMPANY</td>
</tr>
<tr class="odd">
<td>IBCNSCD1</td>
<td>DELETE INSURANCE COMPANY (CON'T)</td>
</tr>
<tr class="even">
<td>IBCNSCD2</td>
<td>DELETE INSURANCE COMPANY (CON'T)</td>
</tr>
<tr class="odd">
<td>IBCNSCD3</td>
<td>DELETE INSURANCE COMPANY (CON'T)</td>
</tr>
<tr class="even">
<td>IBCNSD, IBCNSD1</td>
<td>These routines allow for the display and editing of the benefits a patient has used for a year for a specific plan.</td>
</tr>
<tr class="odd">
<td>IBCNSEH</td>
<td>This routine prints the extended help for insurance policy and plan information.</td>
</tr>
<tr class="even">
<td>IBCNSEVT</td>
<td>This routine invokes the New Insurance Policy Added Event Driver every time a new insurance policy is added.</td>
</tr>
<tr class="odd">
<td>IBCNSGE</td>
<td>Insurance Company EDI Parameter Report</td>
</tr>
<tr class="even">
<td>IBCNSGM</td>
<td>Insurance Company Billing Provider Flag Report / Message</td>
</tr>
<tr class="odd">
<td>IBCNSI</td>
<td>INSURANCE COMPANY BILLING ADDRESSES</td>
</tr>
<tr class="even">
<td>IBCNSJ</td>
<td>INSURANCE PLAN UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCNSJ1</td>
<td>INACTIVATE AN INSURANCE PLAN</td>
</tr>
<tr class="even">
<td>IBCNSJ11</td>
<td>INACTIVATE AN INSURANCE PLAN (CON'T)</td>
</tr>
<tr class="odd">
<td>IBCNSJ12</td>
<td>INACTIVATE AN INSURANCE PLAN (CON'T)</td>
</tr>
<tr class="even">
<td>IBCNSJ13</td>
<td>INACTIVATE AN INSURANCE PLAN (CON'T)</td>
</tr>
<tr class="odd">
<td>IBCNSJ14</td>
<td>INACTIVATE AN INSURANCE PLAN (CON'T)</td>
</tr>
<tr class="even">
<td>IBCNSJ2</td>
<td>CHANGE POLICY PLAN</td>
</tr>
<tr class="odd">
<td>IBCNSJ21</td>
<td>CHANGE POLICY PLAN (CON'T)</td>
</tr>
<tr class="even">
<td>IBCNSJ3</td>
<td>ADD NEW INSURANCE PLAN</td>
</tr>
<tr class="odd">
<td>IBCNSJ4</td>
<td>INACTIVATE MULTIPLE INSURANCE PLANS</td>
</tr>
<tr class="even">
<td>IBCNSJ5</td>
<td>INSURANCE PLAN MAINTENANCE ACTION PROCESSING</td>
</tr>
<tr class="odd">
<td>IBCNSJ51</td>
<td>INSURANCE PLAN MAINTENANCE ACTION PROCESSING (continued)</td>
</tr>
<tr class="even">
<td>IBCNSJ52</td>
<td>INSURANCE PLAN MAINTENANCE ACTION PROCESSING (continued)</td>
</tr>
<tr class="odd">
<td>IBCNSM, IBCNSM1, IBCNSM2, IBCNSM31, IBCNSM32, IBCNSM4</td>
<td>These routines display in list format one patient's policies and allow for editing of these policies.</td>
</tr>
<tr class="even">
<td>IBCNSM3</td>
<td>INSURANCE MANAGEMENT - OUTPUTS</td>
</tr>
<tr class="odd">
<td>IBCNSM5, IBCNSM6, IBCNSM7, IBCNSM8, IBCNSM9</td>
<td>These routines print the insurance plan worksheets and policy coverage reports.</td>
</tr>
<tr class="even">
<td>IBCNSMM</td>
<td>MEDICARE INSURANCE INTAKE</td>
</tr>
<tr class="odd">
<td>IBCNSMM1</td>
<td>MEDICARE INSURANCE INTAKE (CONT)</td>
</tr>
<tr class="even">
<td>IBCNSMM2</td>
<td>MEDICARE INSURANCE INTAKE (CONT)</td>
</tr>
<tr class="odd">
<td>IBCNSMR</td>
<td>MEDICARE BILLS</td>
</tr>
<tr class="even">
<td>IBCNSMR0</td>
<td>MEDICARE BILLS</td>
</tr>
<tr class="odd">
<td>IBCNSMR1</td>
<td>MEDICARE BILLS</td>
</tr>
<tr class="even">
<td>IBCNSMR6</td>
<td>MRA EXTRACT</td>
</tr>
<tr class="odd">
<td>IBCNSMR7</td>
<td>MRA EXTRACT</td>
</tr>
<tr class="even">
<td>IBCNSMR8</td>
<td>MRA EXTRACT</td>
</tr>
<tr class="odd">
<td>IBCNSMRA</td>
<td>MEDICARE BILLS</td>
</tr>
<tr class="even">
<td>IBCNSMRE</td>
<td>MRA EXTRACT</td>
</tr>
<tr class="odd">
<td>IBCNSOK, IBCNSOK1</td>
<td>These routines check, fix, and print reports on integrity of group plans in the PATIENT file [#2].</td>
</tr>
<tr class="even">
<td>IBCNSP, IBCNSP0, IBCNSP01, IBCNSP11, IBCNSP3, IBCNSV</td>
<td>These routines display policy data for a patient in expanded format and allow for editing of the data.</td>
</tr>
<tr class="odd">
<td>IBCNSP02</td>
<td>INSURANCE MANAGEMENT - EXPANDED POLICY</td>
</tr>
<tr class="even">
<td>IBCNSP1</td>
<td>INSURANCE MANAGEMENT - policy actions</td>
</tr>
<tr class="odd">
<td>IBCNSP2</td>
<td>This routine is the supported call to allow for editing of a patient's insurance policy and plan information from registration and billing.</td>
</tr>
<tr class="even">
<td>IBCNSU, IBCNSU1</td>
<td>Insurance utility routines to add entries to the GROUP INSURANCE PLAN (#355.3), ANNUAL BENEFITS (#355.4), and INSURANCE CLAIMS YEAR TO DATE (#355.5) files.</td>
</tr>
<tr class="odd">
<td>IBCNSU2</td>
<td>This routine contains the new Plan Look-up Utility that is invoked from many points within the Insurance Data Capture module.</td>
</tr>
<tr class="even">
<td>IBCNSU21</td>
<td>Insurance Plan Selector Utility</td>
</tr>
<tr class="odd">
<td>IBCNSU3</td>
<td>Functions for billing decisions to determine plan coverage limitations.</td>
</tr>
<tr class="even">
<td>IBCNSU31</td>
<td>Functions for billing decisions to determine Insurance Filing Timeframe.</td>
</tr>
<tr class="odd">
<td>IBCNSU4</td>
<td>SPONSOR UTILITIES</td>
</tr>
<tr class="even">
<td>IBCNSU41</td>
<td>SPONSOR UTILITIES (CON'T)</td>
</tr>
<tr class="odd">
<td>IBCNSUR</td>
<td>MOVE SUBSCRIBERS TO DIFFERENT PLAN</td>
</tr>
<tr class="even">
<td>IBCNSUR1</td>
<td>MOVE SUBSCRIBERS TO DIFFERENT PLAN (CON'T)</td>
</tr>
<tr class="odd">
<td>IBCNSUR2</td>
<td>MOVE SUBSCRIBERS TO DIFFERENT PLAN (CON'T)</td>
</tr>
<tr class="even">
<td>IBCNSUR3</td>
<td>MOVE SUBSCRIBERS (BULLETIN)</td>
</tr>
<tr class="odd">
<td>IBCNSUR4</td>
<td>This routine contains the new Subscriber Look-up Utility that is invoked from the IBCN MOVE SUBSCRIBER TO PLAN option within the Integrated Billing Module.</td>
</tr>
<tr class="even">
<td>IBCNSUX</td>
<td>SPLIT MEDICARE COMBINATION PLANS</td>
</tr>
<tr class="odd">
<td>IBCNSUX1</td>
<td>SPLIT COMBINATION PLANS CONT.</td>
</tr>
<tr class="even">
<td>IBCNUPD</td>
<td>UPDATE SUBCRIBER INFO FOR SELECTED PATIENTS</td>
</tr>
<tr class="odd">
<td>IBCOC1</td>
<td>Prints a list of new but not verified insurance.</td>
</tr>
<tr class="even">
<td>IBCOIVM</td>
<td>IVM BILLING ACTIVITY</td>
</tr>
<tr class="odd">
<td>IBCOIVM1</td>
<td>IB BILLING ACTIVITY (COMPILE/PRINT)</td>
</tr>
<tr class="even">
<td>IBCOIVM2</td>
<td>IB BILLING ACTIVITY (BULLETIN)</td>
</tr>
<tr class="odd">
<td>IBCOMA</td>
<td>IDENTIFY ACTIVE POLICIES W/NO EFFECTIVE DATE</td>
</tr>
<tr class="even">
<td>IBCOMA1</td>
<td>IDENTIFY ACTIVE POLICIES W/NO EFFECTIVE DATE (CON'T)</td>
</tr>
<tr class="odd">
<td>IBCOMC</td>
<td>IDENTIFY PT BY AGE WITH OR WITHOUT INSURANCE</td>
</tr>
<tr class="even">
<td>IBCOMC1</td>
<td>ALB/CMS-IDENTIFY PT BY AGE WITH OR WITHOUT INSURANCE (CON'T)</td>
</tr>
<tr class="odd">
<td>IBCOMC2</td>
<td>IDENTIFY PT BY AGE WITH OR WITHOUT INSURANCE (CON'T)</td>
</tr>
<tr class="even">
<td>IBCOMD</td>
<td>GENERATE INSURANCE COMPANY LISTINGS</td>
</tr>
<tr class="odd">
<td>IBCOMD1</td>
<td>GENERATE INSURANCE COMPANY LISTINGS</td>
</tr>
<tr class="even">
<td>IBCOMN</td>
<td>PATIENTS NO COVERAGE VERIFIED REPORT</td>
</tr>
<tr class="odd">
<td>IBCOMN1</td>
<td>PATIENTS NO COVERAGE VERIFIED REPORT (CON'T)</td>
</tr>
<tr class="even">
<td>IBCONS1, IBCONS2, IBCONSC</td>
<td>Veterans with insurance outputs. (Routines formerly named DGCRONS1, DGCRONS2, DGCRONSC.)</td>
</tr>
<tr class="odd">
<td>IBCONS3</td>
<td>Veterans with insurance outputs interface with Claims Tracking.</td>
</tr>
<tr class="even">
<td>IBCONS4</td>
<td>NSC W/INSURANCE OUTPUT (SETUP)</td>
</tr>
<tr class="odd">
<td>IBCOPP</td>
<td>LIST INS. PLANS BY CO. (DRIVER)</td>
</tr>
<tr class="even">
<td>IBCOPP1</td>
<td>LIST INS. PLANS BY CO. (DRIVER 1)</td>
</tr>
<tr class="odd">
<td>IBCOPP2</td>
<td>LIST INS. PLANS BY CO. (COMPILE)</td>
</tr>
<tr class="even">
<td>IBCOPP3</td>
<td>LIST INS. PLANS BY CO. (PRINT)</td>
</tr>
<tr class="odd">
<td>IBCOPR</td>
<td>Print dollar amts for pre-registration</td>
</tr>
<tr class="even">
<td>IBCOPR1</td>
<td>Print dollar amts for pre-registration</td>
</tr>
<tr class="odd">
<td>IBCOPV, IBCOPV1, IBCOPV2</td>
<td>Display outpatient visits screen. (Routines formerly named DGCROPV, DGCROPV1, DGCROPV2.)</td>
</tr>
<tr class="even">
<td>IBCORC, IBCORC1, IBCORC2</td>
<td>Rank Insurance Carriers.</td>
</tr>
<tr class="odd">
<td>IBCORC3</td>
<td>RANK INSURANCE CARRIERS (NEW BULLETIN)</td>
</tr>
<tr class="even">
<td>IBCRBC</td>
<td>RATES: BILL CALCULATION OF CHARGES</td>
</tr>
<tr class="odd">
<td>IBCRBC1</td>
<td>RATES: BILL CALCULATION BILLABLE EVENTS</td>
</tr>
<tr class="even">
<td>IBCRBC11</td>
<td>RATES: BILL CALCULATION BILLABLE EVENTS</td>
</tr>
<tr class="odd">
<td>IBCRBC2</td>
<td>RATES: BILL CALCULATION OF ITEM CHARGE</td>
</tr>
<tr class="even">
<td>IBCRBC3</td>
<td>RATES: BILL CALCULATION SORT/STORE</td>
</tr>
<tr class="odd">
<td>IBCRBE</td>
<td>RATES: BILL ENTER/EDIT (RS/CS) SCREEN</td>
</tr>
<tr class="even">
<td>IBCRBEI</td>
<td>RATES: BILL ENTER/EDIT (RS/CS) SCREEN - BI</td>
</tr>
<tr class="odd">
<td>IBCRBF</td>
<td>RATES: BILL FILE CHARGES</td>
</tr>
<tr class="even">
<td>IBCRBG, IBCRBG1, IBCRBG2</td>
<td>Contains utility calls for various inpatient / PTF / outpatient / CPT functions.</td>
</tr>
<tr class="odd">
<td>IBCRBH1</td>
<td>RATES: BILL HELP DISPLAYS - CHARGES</td>
</tr>
<tr class="even">
<td>IBCRBH2</td>
<td>RATES: BILL HELP DISPLAYS - CPT CHARGES</td>
</tr>
<tr class="odd">
<td>IBCRCC</td>
<td>RATES: CALCULATION OF ITEM CHARGE</td>
</tr>
<tr class="even">
<td>IBCRCI</td>
<td>RATES: CALCULATION ITEM / EVENT COST FNCTNS</td>
</tr>
<tr class="odd">
<td>IBCRCU1</td>
<td>RATES: CALCULATION UTILITIES</td>
</tr>
<tr class="even">
<td>IBCREC</td>
<td>RATES: CM INACTIVATE CPT CHARGE OPTION</td>
</tr>
<tr class="odd">
<td>IBCRED</td>
<td>RATES: CM DELETE CHARGE ITEMS OPTION</td>
</tr>
<tr class="even">
<td>IBCREE</td>
<td>RATES: CM ENTER / EDIT</td>
</tr>
<tr class="odd">
<td>IBCREE1</td>
<td>RATES: CM ENTER / EDIT (CI)</td>
</tr>
<tr class="even">
<td>IBCREE2</td>
<td>RATES: CM ENTER / EDIT (SG,RL,PD,DV)</td>
</tr>
<tr class="odd">
<td>IBCREF</td>
<td>RATES: CM FILE ENTRIES (CI,BI)</td>
</tr>
<tr class="even">
<td>IBCREQ</td>
<td>RATES: CM FAST ENTER / EDIT OPTION</td>
</tr>
<tr class="odd">
<td>IBCRER</td>
<td>RATES: CM RC NATIONAL ENTER / EDIT OPTION</td>
</tr>
<tr class="even">
<td>IBCRER1</td>
<td>RATES: CM RC NATIONAL ENTER / EDIT OPTION (CONT)</td>
</tr>
<tr class="odd">
<td>IBCRETP</td>
<td>RATES: TRANSFER PRICING CM FAST ENTER/EDIT</td>
</tr>
<tr class="even">
<td>IBCREU1</td>
<td>RATES: CM ENTER / EDIT UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCRHBA</td>
<td>RATES: UPLOAD HOST FILES (AWP)</td>
</tr>
<tr class="even">
<td>IBCRHBC</td>
<td>RATES: UPLOAD HOST FILES (CMAC DRIVER)</td>
</tr>
<tr class="odd">
<td>IBCRHBC1</td>
<td>RATES: UPLOAD HOST FILES (CMAC &lt;2000)</td>
</tr>
<tr class="even">
<td>IBCRHBC2</td>
<td>RATES: UPLOAD HOST FILES (CMAC 2000+)</td>
</tr>
<tr class="odd">
<td>IBCRHBC3</td>
<td>RATES: UPLOAD HOST FILES (CMAC 2005+)</td>
</tr>
<tr class="even">
<td>IBCRHBR</td>
<td>RATES: UPLOAD HOST FILES (RC) DRIVER</td>
</tr>
<tr class="odd">
<td>IBCRHBR1</td>
<td>RATES: UPLOAD HOST FILES (RC) SETUP</td>
</tr>
<tr class="even">
<td>IBCRHBR2</td>
<td>RATES: UPLOAD HOST FILES (RC) READ</td>
</tr>
<tr class="odd">
<td>IBCRHBR3</td>
<td>RATES: UPLOAD HOST FILES (RC) PARSE</td>
</tr>
<tr class="even">
<td>IBCRHBR4</td>
<td>RATES: UPLOAD (RC) SELECT SITES</td>
</tr>
<tr class="odd">
<td>IBCRHBR5</td>
<td>RATES: UPLOAD (RC) CALCULATIONS SETUP</td>
</tr>
<tr class="even">
<td>IBCRHBR6</td>
<td>RATES: UPLOAD (RC) SITE CALCULATIONS</td>
</tr>
<tr class="odd">
<td>IBCRHBRA</td>
<td>RATES: UPLOAD RC V1 CPT 2000 CHARGES</td>
</tr>
<tr class="even">
<td>IBCRHBRB</td>
<td>RATES: UPLOAD RC V1.4 MOVE LAB CODES</td>
</tr>
<tr class="odd">
<td>IBCRHBRV</td>
<td>RATES: UPLOAD (RC) VERSION FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCRHBS</td>
<td>RATES: UPLOAD HOST FILES (RC 2+) DRIVER</td>
</tr>
<tr class="odd">
<td>IBCRHBS1</td>
<td>RATES: UPLOAD HOST FILES (RC 2+) SETUP</td>
</tr>
<tr class="even">
<td>IBCRHBS2</td>
<td>RATES: UPLOAD HOST FILES (RC 2+) READ</td>
</tr>
<tr class="odd">
<td>IBCRHBS3</td>
<td>RATES: UPLOAD HOST FILES (RC 2+) PARSE</td>
</tr>
<tr class="even">
<td>IBCRHBS4</td>
<td>RATES: UPLOAD (RC 2+) SELECT SITES</td>
</tr>
<tr class="odd">
<td>IBCRHBS5</td>
<td>RATES: UPLOAD (RC 2+) CALCULATIONS DRIVER</td>
</tr>
<tr class="even">
<td>IBCRHBS6</td>
<td>RATES: UPLOAD (RC 2+) CALCULATIONS SETUP</td>
</tr>
<tr class="odd">
<td>IBCRHBS7</td>
<td>RATES: UPLOAD (RC 2+) CALCULATIONS SITE</td>
</tr>
<tr class="even">
<td>IBCRHBS8</td>
<td>RATES: UPLOAD (RC 2+) CALCULATIONS CHARGE</td>
</tr>
<tr class="odd">
<td>IBCRHBSZ</td>
<td>RATES: UPLOAD (RC 2+) DIVISION FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBCRHBT</td>
<td>RATES: UPLOAD HOST FILES (TP)</td>
</tr>
<tr class="odd">
<td>IBCRHD</td>
<td>RATES: UPLOAD ASSIGN &amp; DELETE</td>
</tr>
<tr class="even">
<td>IBCRHL</td>
<td>RATES: UPLOAD CHECK &amp; ADD TO CM SEARCH</td>
</tr>
<tr class="odd">
<td>IBCRHO</td>
<td>RATES: UPLOAD CHECK &amp; ADD TO CM REPORT</td>
</tr>
<tr class="even">
<td>IBCRHRS</td>
<td>RATES: UPLOAD (RC) CHANGE SITE TYPE OPTION</td>
</tr>
<tr class="odd">
<td>IBCRHU1</td>
<td>RATES: UPLOAD UTILITIES</td>
</tr>
<tr class="even">
<td>IBCRHU2</td>
<td>RATES: UPLOAD UTILITIES (ADD CM ELEMENTS)</td>
</tr>
<tr class="odd">
<td>IBCRLA1</td>
<td>RATES: DISPLAY ACTION PROTOCOLS</td>
</tr>
<tr class="even">
<td>IBCRLC</td>
<td>RATES: DISPLAY CHARGE SETS</td>
</tr>
<tr class="odd">
<td>IBCRLD</td>
<td>RATES: DISPLAY INTRO</td>
</tr>
<tr class="even">
<td>IBCRLG</td>
<td>RATES: DISPLAY BILLING REGIONS</td>
</tr>
<tr class="odd">
<td>IBCRLI</td>
<td>RATES: DISPLAY CHARGE ITEMS</td>
</tr>
<tr class="even">
<td>IBCRLL</td>
<td>RATES: DISPLAY SPECIAL GROUPS</td>
</tr>
<tr class="odd">
<td>IBCRLM</td>
<td>RATES: DISPLAY REVENUE CODE LINKS</td>
</tr>
<tr class="even">
<td>IBCRLN</td>
<td>RATES: DISPLAY PROVIDER DISCOUNT</td>
</tr>
<tr class="odd">
<td>IBCRLR</td>
<td>RATES: DISPLAY BILLING RATES</td>
</tr>
<tr class="even">
<td>IBCRLS</td>
<td>RATES: DISPLAY SCHEDULES</td>
</tr>
<tr class="odd">
<td>IBCRLT</td>
<td>RATES: DISPLAY RATE TYPES</td>
</tr>
<tr class="even">
<td>IBCROE</td>
<td>CHARGE MASTER TO EXCEL OUTPUT</td>
</tr>
<tr class="odd">
<td>IBCROI</td>
<td>RATES: REPORTS CHARGE ITEM</td>
</tr>
<tr class="even">
<td>IBCROI1</td>
<td>RATES: REPORTS CHARGE ITEM (SRCH)</td>
</tr>
<tr class="odd">
<td>IBCROIP</td>
<td>RATES: REPORTS CHARGE ITEM: PROCEDURES</td>
</tr>
<tr class="even">
<td>IBCRON</td>
<td>RATES: REPORTS PROVIDER DISCOUNT</td>
</tr>
<tr class="odd">
<td>IBCROR</td>
<td>RATES: REPORTS</td>
</tr>
<tr class="even">
<td>IBCRTN</td>
<td>Edit bills returned from Accounts Receivable. (Routine formerly named DGCRTN.)</td>
</tr>
<tr class="odd">
<td>IBCRU1</td>
<td>RATES: UTILITIES</td>
</tr>
<tr class="even">
<td>IBCRU2</td>
<td>RATES: UTILITIES (CI DEFINITIONS)</td>
</tr>
<tr class="odd">
<td>IBCRU3</td>
<td>RATES: UTILITIES (CS / BR)</td>
</tr>
<tr class="even">
<td>IBCRU4</td>
<td>RATES: UTILITIES (RG / BILL / CI)</td>
</tr>
<tr class="odd">
<td>IBCRU5</td>
<td>RATES: UTILITIES (DISPLAYS)</td>
</tr>
<tr class="even">
<td>IBCRU6</td>
<td>RATES: UTILITIES (SPECIAL GROUPS)</td>
</tr>
<tr class="odd">
<td>IBCRU7</td>
<td>TRANSFER PRICING CHARGE MASTER UTILITIES</td>
</tr>
<tr class="even">
<td>IBCRU8</td>
<td>RATES: UTILITIES (RC)</td>
</tr>
<tr class="odd">
<td>IBCSC1</td>
<td>Enter / Edit a Bill Screen 1 (Demographics). (Routine formerly named DGCRSC1.)</td>
</tr>
<tr class="even">
<td>IBCSC10</td>
<td>MCCR SCREEN 10 (UB-82 BILL SPECIFIC INFO)</td>
</tr>
<tr class="odd">
<td>IBCSC102</td>
<td>MCCR SCREEN 10 (UB-04 BILL SPECIFIC INFO)</td>
</tr>
<tr class="even">
<td>IBCSC10A</td>
<td>ADD/ENTER CHIROPRACTIC DATA</td>
</tr>
<tr class="odd">
<td>IBCSC10B</td>
<td>ADD/ENTER PATIENT REASON FOR VISIT DATA</td>
</tr>
<tr class="even">
<td>IBCSC10H</td>
<td>MCCR SCREEN 10 (BILL SPECIFIC INFO) CMS-1500</td>
</tr>
<tr class="odd">
<td>IBCSC11</td>
<td>MCCR SCREEN 11 (LOCAL SCREEN 11 SPECIFIC INFO)</td>
</tr>
<tr class="even">
<td>IBCSC2</td>
<td>Enter / Edit a Bill Screen 2 (Employment). (Routine formerly named DGCRSC2.)</td>
</tr>
<tr class="odd">
<td>IBCSC3</td>
<td>Enter / Edit a Bill Screen 3 (Payer / Mailing Address). (Routine formerly named DGCRSC3.)</td>
</tr>
<tr class="even">
<td>IBCSC4</td>
<td>Enter / Edit a Bill Screen 4 (Inpatient EOC). (Routine formerly named DGCRSC4.)</td>
</tr>
<tr class="odd">
<td>IBCSC4A, IBCSC4B, IBCSC4C</td>
<td>Enter / Edit a Bill PTF Screens. (Routines formerly named DGCRSC4A, DGCRSC4B, and DGCRSC4C.)</td>
</tr>
<tr class="even">
<td>IBCSC4D, IBCSC4E</td>
<td>Enter / Edit a bill's diagnoses.</td>
</tr>
<tr class="odd">
<td>IBCSC4F</td>
<td>GET PTF DIAGNOSIS</td>
</tr>
<tr class="even">
<td>IBCSC5</td>
<td>Enter / Edit a Bill Screen 5 (Opt. EOC). (Routine formerly named DGCRSC5.)</td>
</tr>
<tr class="odd">
<td>IBCSC5A, IBCSC5C</td>
<td>Enter / Edit a bill's prescription refills.</td>
</tr>
<tr class="even">
<td>IBCSC5B</td>
<td>Enter / Edit a bill's prosthetic items.</td>
</tr>
<tr class="odd">
<td>IBCSC6</td>
<td>Enter / Edit a Bill Screen 6 (Inpatient Billing Info). (Routine formerly named DGCRSC6.)</td>
</tr>
<tr class="even">
<td>IBCSC61</td>
<td>Enter / Edit a Bill screen utility. (Routine formerly named DGCRSC61.)</td>
</tr>
<tr class="odd">
<td>IBCSC7</td>
<td>Enter / Edit a Bill Screen 7 (Opt. Billing Info). (Routine formerly named DGCRSC7.)</td>
</tr>
<tr class="even">
<td>IBCSC8</td>
<td>Enter / Edit a Bill Screen 8 (Bill Specific Info). (Routine formerly named DGCRSC8.)</td>
</tr>
<tr class="odd">
<td>IBCSC82</td>
<td>Enter / Edit a Bill Screen 8 for UB-92.</td>
</tr>
<tr class="even">
<td>IBCSC8H</td>
<td>Enter / Edit a Bill Screen 8, if HCFA-1500. (Routine formerly named DGCRSC8H.)</td>
</tr>
<tr class="odd">
<td>IBCSC9</td>
<td>MCCR SCREEN 9 (AMBULANCE INFO)</td>
</tr>
<tr class="even">
<td>IBCSCE, IBCSCE1</td>
<td>Enter / Edit a Bill screen edits. (Routines formerly named DGCRSCE, DGCRSCE1.)</td>
</tr>
<tr class="odd">
<td>IBCSCH, IBCSCH1</td>
<td>Enter / Edit a Bill help screens. (Routines formerly named DGCRSCH, DGCRSCH1.)</td>
</tr>
<tr class="even">
<td>IBCSCH2</td>
<td>ALB / DLS - Continuation of routine IBCSCH</td>
</tr>
<tr class="odd">
<td>IBCSCP</td>
<td>Enter / Edit a Bill screen processor. (Routine formerly named DGCRSCP.)</td>
</tr>
<tr class="even">
<td>IBCSCU</td>
<td>Enter / Edit a Bill screen utility. (Routine formerly named DGCRSCU.)</td>
</tr>
<tr class="odd">
<td>IBCU, IBCU1, IBCU2, IBCU3, IBCU4, IBCU5</td>
<td>Enter / Edit a Bill billing utility. (Routines formerly named DGCRU, DGCRU1, DGCRU2, DGCRU3, DGCRU4, DGCRU5.)</td>
</tr>
<tr class="even">
<td>IBCU41, IBCU64</td>
<td>Third Party billing utilities</td>
</tr>
<tr class="odd">
<td>IBCU6, IBCU61, IBCU62, IBCU63</td>
<td>Automatic calculation of charges utility routines. (Routines formerly named DGCRU6, DGCRU61, DGCRU62, and DGCRU63.)</td>
</tr>
<tr class="even">
<td>IBCU65</td>
<td>BILL CHARGE UTILITY: COMBINE E&amp;M</td>
</tr>
<tr class="odd">
<td>IBCU7, IBCU7</td>
<td>Procedures enter / edit utility routines. (Routines formerly named DGCRU7, DGCRU71.)</td>
</tr>
<tr class="even">
<td>IBCU71</td>
<td>INTERCEPT SCREEN INPUT OF PROCEDURE CODES</td>
</tr>
<tr class="odd">
<td>IBCU72</td>
<td>ADD / EDIT / DELETE PROCEDURE DIAGNOSES</td>
</tr>
<tr class="even">
<td>IBCU73</td>
<td>ADD / DELETE MODIFIER 26 TO SPECIFIED CPTS</td>
</tr>
<tr class="odd">
<td>IBCU74</td>
<td>INTERCEPT SCREEN INPUT OF PROCEDURE CODES (CONT)</td>
</tr>
<tr class="even">
<td>IBCU75</td>
<td>INTERCEPT SCREEN INPUT OF PROCEDURE CODES (ENTER CMN INFO)</td>
</tr>
<tr class="odd">
<td>IBCU7A</td>
<td>BILL PROCEDURE MANIPULATIONS</td>
</tr>
<tr class="even">
<td>IBCU7A1</td>
<td>BILL PROCEDURE MANIPULATIONS (BUNDLED)</td>
</tr>
<tr class="odd">
<td>IBCU7B</td>
<td>LINE LEVEL PROVIDER USER INPUT</td>
</tr>
<tr class="even">
<td>IBCU7U</td>
<td>BILL PROCEDURE UTILITIES</td>
</tr>
<tr class="odd">
<td>IBCU8, IBCU81, IBCU82</td>
<td>Third Party Billing Utilities</td>
</tr>
<tr class="even">
<td>IBCU83</td>
<td>THIRD PARTY BILLING UTILITES (BILL-CT)</td>
</tr>
<tr class="odd">
<td>IBCU9</td>
<td>BILLING UTILITY ROUTINE (CONTINUED)</td>
</tr>
<tr class="even">
<td>IBCVA, IBCVA0, IBCVA1</td>
<td>Third Party Billing set variables. (Routines formerly named DGCRVA, DGCRVA0, and DGCRVA1.)</td>
</tr>
<tr class="odd">
<td>IBCVC</td>
<td>VALUE CODE FUNCTIONALITY</td>
</tr>
<tr class="even">
<td>IBD21P4</td>
<td>POST INIT - 6/11/96</td>
</tr>
<tr class="odd">
<td>IBD3KENV</td>
<td>AICS 3.0 Environment Checker</td>
</tr>
<tr class="even">
<td>IBD3KPT</td>
<td>Post Init routine for AICS v 3.0 - 11 NOV 96</td>
</tr>
<tr class="odd">
<td>IBDE, IBDE1, IBDE1A, IBDE1B, IBDE2, IBDE3, IBDEHELP</td>
<td>The import / export utility for the encounter form.</td>
</tr>
<tr class="even">
<td>IBDE4</td>
<td>PUT FORMS AND BLOCKS INTO IMPORT / EXPORT UTILTIY</td>
</tr>
<tr class="odd">
<td>IBDECLN</td>
<td>Clean up Data Qualifiers and Package interfaces</td>
</tr>
<tr class="even">
<td>IBDECLN1</td>
<td>Clean up Data Qualifiers and Package interfaces</td>
</tr>
<tr class="odd">
<td>IBDECLN2</td>
<td>Clean up Data Qualifiers and Package interfaces</td>
</tr>
<tr class="even">
<td>IBDEI*</td>
<td>IB ENCOUNTER FORM IMP/EXP Routines</td>
</tr>
<tr class="odd">
<td>IBDEPRE</td>
<td>PREINIT FOR USE BY IMP/EXP UTILITY</td>
</tr>
<tr class="even">
<td>IBDEPT</td>
<td>ENCOUNTER FORM - installation routine for AICS 2.1</td>
</tr>
<tr class="odd">
<td>IBDF10, IBDF10A, IBDF10B</td>
<td>Shifting blocks and the contents of blocks.</td>
</tr>
<tr class="even">
<td>IBDF10C</td>
<td>ENCOUNTER FORM - (shift block contents - continued)</td>
</tr>
<tr class="odd">
<td>IBDF11, IBDF11A</td>
<td>Print Manager setup for the encounter form.</td>
</tr>
<tr class="even">
<td>IBDF12</td>
<td>Editing Tool Kit forms.</td>
</tr>
<tr class="odd">
<td>IBDF13</td>
<td>Editing Tool Kit blocks.</td>
</tr>
<tr class="even">
<td>IBDF14</td>
<td>Clinic Setups Report</td>
</tr>
<tr class="odd">
<td>IBDF14A</td>
<td>AICS LIST CLINIC SETUP</td>
</tr>
<tr class="even">
<td>IBDF15</td>
<td>List Clinics Using Forms Report.</td>
</tr>
<tr class="odd">
<td>IBDF15A</td>
<td>AICS FORM USE BY DIVISION / CLINIC</td>
</tr>
<tr class="even">
<td>IBDF16</td>
<td>Edit package interfaces, marking areas.</td>
</tr>
<tr class="odd">
<td>IBDF17</td>
<td>Copy Check-off Sheets to encounter forms.</td>
</tr>
<tr class="even">
<td>IBDF18</td>
<td>Utility for providing the Problem List package with a list of clinic common problems from an encounter form.</td>
</tr>
<tr class="odd">
<td>IBDF18A</td>
<td>ENCOUNTER FORM - utilities for PCE</td>
</tr>
<tr class="even">
<td>IBDF18A1</td>
<td>ENCOUNTER FORM - utilities for PCE</td>
</tr>
<tr class="odd">
<td>IBDF18A2</td>
<td>WISC / TN - ENCOUNTER FORM - utilities for PCE</td>
</tr>
<tr class="even">
<td>IBDF18B</td>
<td>ENCOUNTER FORM - utilities for PCE</td>
</tr>
<tr class="odd">
<td>IBDF18C</td>
<td>ENCOUNTER FORM - form ID utilities</td>
</tr>
<tr class="even">
<td>IBDF18D</td>
<td>ENCOUNTER FORM - form type utilities</td>
</tr>
<tr class="odd">
<td>IBDF18E</td>
<td>ENCOUNTER FORM - PCE DEVICE INTERFACE utilities</td>
</tr>
<tr class="even">
<td>IBDF18E0</td>
<td>ENCOUNTER FORM - PCE DEVICE INTERFACE utilities</td>
</tr>
<tr class="odd">
<td>IBDF18E1</td>
<td>ENCOUNTER FORM - PCE DEVICE INTERFACE utilities</td>
</tr>
<tr class="even">
<td>IBDF18E2</td>
<td>AICS Error Logging Routine</td>
</tr>
<tr class="odd">
<td>IBDF18E3</td>
<td>ENCOUNTER FORM - PCE DEVICE INTERFACE utilities</td>
</tr>
<tr class="even">
<td>IBDF18E4</td>
<td>ENCOUNTER FORM - MISC INTERFACES utilities</td>
</tr>
<tr class="odd">
<td>IBDF19</td>
<td>Routine for deleting garbage, compiling forms.</td>
</tr>
<tr class="even">
<td>IBDF1A</td>
<td>Printing a single encounter form, along with other reports defined via the Print Manager.</td>
</tr>
<tr class="odd">
<td>IBDF1B, IBDF1B1, IBDF1B1A, IBDF1B1B, IBDF1B2, IBDF1B3, IBDF1B5, IBDF1BA</td>
<td>Printing batches of encounter forms for appointments, along with other reports defined via the Print Manager.</td>
</tr>
<tr class="even">
<td>IBDF1C</td>
<td>Print a blank encounter form within the List Manager.</td>
</tr>
<tr class="odd">
<td>IBDF2A</td>
<td>Prints a form - device must be open, variables defined.</td>
</tr>
<tr class="even">
<td>IBDF2A1</td>
<td>ENCOUNTER FORM (IBDF2A continued)</td>
</tr>
<tr class="odd">
<td>IBDF2A2</td>
<td>ENCOUNTER FORM (IBDF2A continued)</td>
</tr>
<tr class="even">
<td>IBDF2B, IBDF2B1</td>
<td>Writes a data field to the form.</td>
</tr>
<tr class="odd">
<td>IBDF2D, IBDF2D1</td>
<td>Writes a selection list to the form.</td>
</tr>
<tr class="even">
<td>IBDF2D2</td>
<td>ENCOUNTER FORM - PRINT SELECTION LIST (cont'd)</td>
</tr>
<tr class="odd">
<td>IBDF2D3</td>
<td>ENCOUNTER FORM - WRITE SELECTION LIST (cont'd)</td>
</tr>
<tr class="even">
<td>IBDF2E</td>
<td>Writes lines and text areas to the form.</td>
</tr>
<tr class="odd">
<td>IBDF2F</td>
<td>Prints the form - the form image must be in an array.</td>
</tr>
<tr class="even">
<td>IBDF2F1</td>
<td>ENCOUNTER FORM - PRINT FORM (sends to printer)</td>
</tr>
<tr class="odd">
<td>IBDF2F2</td>
<td>PRINT VA LOGO AS ANCHORS ON ENCOUNTER FORMS</td>
</tr>
<tr class="even">
<td>IBDF2G</td>
<td>ENCOUNTER FORM (prints input field)</td>
</tr>
<tr class="odd">
<td>IBDF2H</td>
<td>ENCOUNTER FORM (prints hand print field)</td>
</tr>
<tr class="even">
<td>IBDF3</td>
<td>Edit selection groups</td>
</tr>
<tr class="odd">
<td>IBDF4, IBDF4A</td>
<td>Edit selections</td>
</tr>
<tr class="even">
<td>IBDF4C</td>
<td>CPT MODIFIER SELECTION</td>
</tr>
<tr class="odd">
<td>IBDF5, IBDF5A, IBDF5B, IBDF5C</td>
<td>Creating an array that contains the form for display via the List Manager; editing the form; creating new blocks on the form; moving and re-sizing blocks.</td>
</tr>
<tr class="even">
<td>IBDF5D</td>
<td>ENCOUNTER FORM (copy page)</td>
</tr>
<tr class="odd">
<td>IBDF6, IBDF6A, IBDFC</td>
<td>Adding and deleting forms to a clinic setup; creating and deleting forms.</td>
</tr>
<tr class="even">
<td>IBDF7</td>
<td>Creating a list of Tool Kit blocks for the List Manager; creating a new Tool Kit block.</td>
</tr>
<tr class="odd">
<td>IBDF8</td>
<td>Displaying a Tool Kit block.</td>
</tr>
<tr class="even">
<td>IBDF9, IBDF9A, IBDF9A1, IBDF9B, IBDF9B1, IBDF9C, IBDF9D, IBDF9E</td>
<td>Displaying a block, resizing it, editing its attributes and contents.</td>
</tr>
<tr class="odd">
<td>IBDF9A3</td>
<td>ENCOUNTER FORM (create, edit, delete selection list - continued)</td>
</tr>
<tr class="even">
<td>IBDF9B2</td>
<td>ENCOUNTER FORM (edit, delete, add multiple choice fields)</td>
</tr>
<tr class="odd">
<td>IBDF9B3</td>
<td>ENCOUNTER FORM (edit, delete, add data fields)</td>
</tr>
<tr class="even">
<td>IBDF9B4</td>
<td>ENCOUNTER FORM (edit, delete, add Hand Print fields)</td>
</tr>
<tr class="odd">
<td>IBDFBK1</td>
<td>AICS broker Utilities</td>
</tr>
<tr class="even">
<td>IBDFBK2</td>
<td>AICS broker Utilities</td>
</tr>
<tr class="odd">
<td>IBDFBK3</td>
<td>AICS broker Utilities</td>
</tr>
<tr class="even">
<td>IBDFBKR</td>
<td>EF utility, receive and format data for PCE</td>
</tr>
<tr class="odd">
<td>IBDFBKS</td>
<td>Create form spec file for scanning</td>
</tr>
<tr class="even">
<td>IBDFBKS1</td>
<td>ENCOUNTER FORM - create form spec for scanning (Broker Version CONTINUATION)</td>
</tr>
<tr class="odd">
<td>IBDFBKS2</td>
<td>Create form spec for scanning</td>
</tr>
<tr class="even">
<td>IBDFBKS3</td>
<td>ENCOUNTER FORM - create form spec for scanning (Broker Version)</td>
</tr>
<tr class="odd">
<td>IBDFBKS4</td>
<td>Create form spec file for scanning</td>
</tr>
<tr class="even">
<td>IBDFC</td>
<td>ENCOUNTER FORM - CONVERSION UTILTY</td>
</tr>
<tr class="odd">
<td>IBDFC1</td>
<td>ENCOUNTER FORM - CONVERTED FORMS LIST</td>
</tr>
<tr class="even">
<td>IBDFC2</td>
<td>ENCOUNTER FORM - converts a form for scanning</td>
</tr>
<tr class="odd">
<td>IBDFC2A</td>
<td>ENCOUNTER FORM - converts a form for scanning (cont'd)</td>
</tr>
<tr class="even">
<td>IBDFC2B</td>
<td>ENCOUNTER FORM - converts a form for scanning</td>
</tr>
<tr class="odd">
<td>IBDFC3</td>
<td>ENCOUNTER FORM - replace original form with converted form</td>
</tr>
<tr class="even">
<td>IBDFC4</td>
<td>ENCOUNTER FORM - print scanning form definition</td>
</tr>
<tr class="odd">
<td>IBDFCG</td>
<td>CLINIC GROUP FORMS SCREEN</td>
</tr>
<tr class="even">
<td>IBDFCG1</td>
<td>CONT. of Clinic Group Enter Edit Screen - 1 1 95</td>
</tr>
<tr class="odd">
<td>IBDFCMP</td>
<td>AICS list of components on a form</td>
</tr>
<tr class="even">
<td>IBDFCMP1</td>
<td>AICS list of components on a form (cont.)</td>
</tr>
<tr class="odd">
<td>IBDFCNOF</td>
<td>AICS clinics with no forms</td>
</tr>
<tr class="even">
<td>IBDFDBS</td>
<td>Database Server Utilities</td>
</tr>
<tr class="odd">
<td>IBDFDE</td>
<td>AICS Data Entry, Entry point by form</td>
</tr>
<tr class="even">
<td>IBDFDE0</td>
<td>AICS Data Entry, Check out interview</td>
</tr>
<tr class="odd">
<td>IBDFDE1</td>
<td>AICS Data Entry, Final check</td>
</tr>
<tr class="even">
<td>IBDFDE10</td>
<td>AICS Data entry utility</td>
</tr>
<tr class="odd">
<td>IBDFDE2</td>
<td>AICS Data Entry, process selection lists</td>
</tr>
<tr class="even">
<td>IBDFDE21</td>
<td>AICS Data Entry, process selection lists</td>
</tr>
<tr class="odd">
<td>IBDFDE22</td>
<td>AICS Data Entry, check selection rules</td>
</tr>
<tr class="even">
<td>IBDFDE23</td>
<td>Select CPT Modifiers during Manual Data Entry</td>
</tr>
<tr class="odd">
<td>IBDFDE3</td>
<td>AICS Manual Data Entry, process handprint fields</td>
</tr>
<tr class="even">
<td>IBDFDE4</td>
<td>AICS Manual Data Entry, process multiple choice fields</td>
</tr>
<tr class="odd">
<td>IBDFDE41</td>
<td>AICS Data Entry, process selection lists</td>
</tr>
<tr class="even">
<td>IBDFDE42</td>
<td>AICS Data Entry, check selection rules</td>
</tr>
<tr class="odd">
<td>IBDFDE5</td>
<td>AICS Manual Data Entry, Loader routine for 357.6</td>
</tr>
<tr class="even">
<td>IBDFDE6</td>
<td>AICS Manual Data Entry, Entry point by clinic</td>
</tr>
<tr class="odd">
<td>IBDFDE61</td>
<td>AICS Manual Data Entry, process selection lists</td>
</tr>
<tr class="even">
<td>IBDFDE7</td>
<td>AICS Manual Data Entry, Entry point for Group Clinics</td>
</tr>
<tr class="odd">
<td>IBDFDE8</td>
<td>AICS Manual Data Entry, Entry for no form no appt</td>
</tr>
<tr class="even">
<td>IBDFDE9</td>
<td>AICS Manual Data Entry, Report of inputs by form</td>
</tr>
<tr class="odd">
<td>IBDFDEA</td>
<td>AICS Data Entry API</td>
</tr>
<tr class="even">
<td>IBDFDVE</td>
<td>AICS edit printers file</td>
</tr>
<tr class="odd">
<td>IBDFESP</td>
<td>AICS EDIT SITE PARAMS</td>
</tr>
<tr class="even">
<td>IBDFFRFT</td>
<td>AICS Free Forms Tracking Entry</td>
</tr>
<tr class="odd">
<td>IBDFFSMP</td>
<td>Print a sample of all encounter forms. - Dec 12, 1995@800</td>
</tr>
<tr class="even">
<td>IBDFFT</td>
<td>FORMS TRACKING</td>
</tr>
<tr class="odd">
<td>IBDFFT1</td>
<td>FORMS TRACKING CONTINUED - JUL 6 1995</td>
</tr>
<tr class="even">
<td>IBDFFT2</td>
<td>FORMS TRACKING</td>
</tr>
<tr class="odd">
<td>IBDFFT3</td>
<td>ROUTINE TO QUEUE FORMS TRACKING REPORT - 13 NOV 96</td>
</tr>
<tr class="even">
<td>IBDFFT4</td>
<td>FORMS TRACKING</td>
</tr>
<tr class="odd">
<td>IBDFFV</td>
<td>AICS FORM VALIDATION</td>
</tr>
<tr class="even">
<td>IBDFFV1</td>
<td>AICS FORM VALIDATION</td>
</tr>
<tr class="odd">
<td>IBDFFV2</td>
<td>AICS FORM VALIDATION</td>
</tr>
<tr class="even">
<td>IBDFFV3</td>
<td>AICS FORM VALIDATION</td>
</tr>
<tr class="odd">
<td>IBDFGRP</td>
<td>GROUP COPY - 7/25/95</td>
</tr>
<tr class="even">
<td>IBDFHLP</td>
<td>HELP CODE FOR SPECIAL INSTRUCTIONS</td>
</tr>
<tr class="odd">
<td>IBDFLST</td>
<td>Maintenance Utility Invalid Codes List - MAY 17, 1995</td>
</tr>
<tr class="even">
<td>IBDFLST1</td>
<td>Maintenance Utility Invalid Codes List - MAY 17, 1995</td>
</tr>
<tr class="odd">
<td>IBDFM1</td>
<td>Compiling bubbles and hand print fields</td>
</tr>
<tr class="even">
<td>IBDFN, IBDFN1, IBDFN2, IBDFN3, IBDFN4, IBDFN5, IBDFN6</td>
<td>Entry points used by the PACKAGE INTERFACE file #357.6) for interfacing with other packages.</td>
</tr>
<tr class="odd">
<td>IBDFN10</td>
<td>ENCOUNTER FORM (selection routines - mostly for PCE files)</td>
</tr>
<tr class="even">
<td>IBDFN11</td>
<td>ENCOUNTER FORM (entry points for reprint of dynamic data)</td>
</tr>
<tr class="odd">
<td>IBDFN12</td>
<td>ENCOUNTER FORM - SELECTORS</td>
</tr>
<tr class="even">
<td>IBDFN13</td>
<td>ENCOUNTER FORM (input transforms for AICS Data Types)</td>
</tr>
<tr class="odd">
<td>IBDFN14</td>
<td>ENCOUNTER FORM - OUTPUTS</td>
</tr>
<tr class="even">
<td>IBDFN15</td>
<td>ENCOUNTER FORM - OUTPUTS</td>
</tr>
<tr class="odd">
<td>IBDFN16</td>
<td>ENCOUNTER FORM (entry points for gaf project)</td>
</tr>
<tr class="even">
<td>IBDFN7</td>
<td>ENCOUNTER FORM - validate logic for data</td>
</tr>
<tr class="odd">
<td>IBDFN8</td>
<td>ENCOUNTER FORM - PCE GDI INPUT TRANSFORMS</td>
</tr>
<tr class="even">
<td>IBDFN9</td>
<td>ENCOUNTER FORM - output transforms for data</td>
</tr>
<tr class="odd">
<td>IBDFOSG</td>
<td>SCANNED EF FOR OUTPATIENTS WITH BILLS GENERATED REPORT</td>
</tr>
<tr class="even">
<td>IBDFOSG1</td>
<td>SCANNED ENCOUNTERS WITH BILLING DATA CONT.</td>
</tr>
<tr class="odd">
<td>IBDFOSG2</td>
<td>ENCOUNTERS WITH BILLING DATA CONT. - SEP 11, 1995</td>
</tr>
<tr class="even">
<td>IBDFPCE</td>
<td>AICS UPDATE FROM PCE</td>
</tr>
<tr class="odd">
<td>IBDFPE</td>
<td>ENCOUNTER FORMS QUEUEING PARAMETERS DISPLAY 1 31 94</td>
</tr>
<tr class="even">
<td>IBDFPE1</td>
<td>ENCOUNTER FORMS QUEUEING PARAMETERS DISPLAY CONT.</td>
</tr>
<tr class="odd">
<td>IBDFPRG</td>
<td>AICS PURGE UTILITY</td>
</tr>
<tr class="even">
<td>IBDFPRG1</td>
<td>AICS PURGE UTILITY</td>
</tr>
<tr class="odd">
<td>IBDFQB</td>
<td>MAIN QUEUE JOB FOR ENCOUNTER FORM PRINTING - FEB 2, 1995</td>
</tr>
<tr class="even">
<td>IBDFQEA</td>
<td>ENCOUNTER FORM - BUILD FORM (editing action for group's selections list)</td>
</tr>
<tr class="odd">
<td>IBDFQEA1</td>
<td>ENCOUNTER FORM - BUILD FORM (editing action for group's selections list) cont.</td>
</tr>
<tr class="even">
<td>IBDFQS</td>
<td>REQUEUE OF PRINT JOB FOR A SINGLE PARAMETER GROUP - FEB 9, 1995</td>
</tr>
<tr class="odd">
<td>IBDFQSL</td>
<td>ENCOUNTER FORM - Quick selection edit</td>
</tr>
<tr class="even">
<td>IBDFQSL1</td>
<td>ENCOUNTER FORM - Quick selection edit (cont.)</td>
</tr>
<tr class="odd">
<td>IBDFQSL2</td>
<td>ENCOUNTER FORM - Quick selection edit (cont.)</td>
</tr>
<tr class="even">
<td>IBDFREG</td>
<td>ENCOUNTER FORM (prints for a single patient)</td>
</tr>
<tr class="odd">
<td>IBDFRPC</td>
<td>AICS Return list of interfaces</td>
</tr>
<tr class="even">
<td>IBDFRPC1</td>
<td>Return list of selections</td>
</tr>
<tr class="odd">
<td>IBDFRPC2</td>
<td>Return list of selections, broker call</td>
</tr>
<tr class="even">
<td>IBDFRPC3</td>
<td>AICS Identify patient form id</td>
</tr>
<tr class="odd">
<td>IBDFRPC4</td>
<td>AICS Pass data to PCE, Broker Call</td>
</tr>
<tr class="even">
<td>IBDFRPC5</td>
<td>AICS Pass data to PCE, Broker Call</td>
</tr>
<tr class="odd">
<td>IBDFRPC6</td>
<td>AICS Pass data to PCE, Broker Call</td>
</tr>
<tr class="even">
<td>IBDFSS</td>
<td>STATUS SELECT ROUTINE (FORMS TRACKING)</td>
</tr>
<tr class="odd">
<td>IBDFSS1</td>
<td>FORMS TRACKING SELECTED STATUS - JUL 6, 1995</td>
</tr>
<tr class="even">
<td>IBDFST</td>
<td>FORMS TRACKING STATISTICS - JUL 6, 1995</td>
</tr>
<tr class="odd">
<td>IBDFST1</td>
<td>FORMS TRACKING STATISTICS - JUL 6, 1995</td>
</tr>
<tr class="even">
<td>IBDFU, IBDFU1, IBDFU10, IBDFU1A, IBDFU1B, IBDFU2, IBDFU2A, IBDFU2B, IBDFU2C, IBDFU3, IBDFU4, IBDFU5, IBDFU5A, IBDFU6, IBDFU7, IBDFU8, IBDFU9, IBDFUA</td>
<td>Utilities used for encounter forms.</td>
</tr>
<tr class="odd">
<td>IBDFU1C</td>
<td>ENCOUNTER FORM (sets various parameters)</td>
</tr>
<tr class="even">
<td>IBDFU91</td>
<td>ENCOUNTER FORM - transforms needed to validate, display, and pass data</td>
</tr>
<tr class="odd">
<td>IBDFUTI</td>
<td>Installation utilities Re-Compile Templates / x-refs</td>
</tr>
<tr class="even">
<td>IBDFUTL</td>
<td>Maintenance Utility Routine - APR 20, 1995</td>
</tr>
<tr class="odd">
<td>IBDFUTL1</td>
<td>Maintenance Utility cont. - 4 20 95</td>
</tr>
<tr class="even">
<td>IBDFUTL2</td>
<td>MAINTENANCE UTILITY CONT. - 4/24/95</td>
</tr>
<tr class="odd">
<td>IBDFUTL3</td>
<td>MAINTENANCE UTILITY CONT. - 4/24/95</td>
</tr>
<tr class="even">
<td>IBDNTEG</td>
<td>ISC / XTSUMBLD KERNEL - Package checksum checker</td>
</tr>
<tr class="odd">
<td>IBDNTEG0</td>
<td>ISC / XTSUMBLD KERNEL - Package checksum checker</td>
</tr>
<tr class="even">
<td>IBDX*</td>
<td>Generated or Compiled Routines for XREFS, PRINT TEMPLATES, INPUT TEMPLATES</td>
</tr>
<tr class="odd">
<td>IBDY*</td>
<td>Mixed Post-Init, Pre-Init, and Environment Routines for released patches.</td>
</tr>
<tr class="even">
<td>IBEBR</td>
<td>Enter / Edit Billing Rates.</td>
</tr>
<tr class="odd">
<td>IBEBRH</td>
<td>Help routine for Enter / Edit Billing Rates.</td>
</tr>
<tr class="even">
<td>IBECEA, IBECEA0</td>
<td>Cancel / Edit / Add Charges - build charges array for list processor.</td>
</tr>
<tr class="odd">
<td>IBECEA1</td>
<td>Cancel / Edit / Add Charges - logic for the Pass a Charge action.</td>
</tr>
<tr class="even">
<td>IBECEA2, IBECEA21, IBECEA22</td>
<td>Cancel / Edit / Add Charges - logic for the Edit a Charge action.</td>
</tr>
<tr class="odd">
<td>IBECEA3, IBECEA31, IBECEA32, IBECEA33</td>
<td>Cancel / Edit / Add Charges - logic for the Add a Charge action.</td>
</tr>
<tr class="even">
<td>IBECEA34</td>
<td>Cancel / Edit / Add... Fee Support</td>
</tr>
<tr class="odd">
<td>IBECEA35</td>
<td>Cancel / Edit / Add... TRICARE Support</td>
</tr>
<tr class="even">
<td>IBECEA36</td>
<td>Cancel / Edit / Add... Community Care (CC) Urgent Care Support</td>
</tr>
<tr class="odd">
<td>IBECEA37</td>
<td>Cancel / Edit / Add... Community Care (CC) Urgent Care Visit Tracking Support – Remote APIs</td>
</tr>
<tr class="even">
<td>IBECEA38</td>
<td>Cancel / Edit / Add... Community Care (CC) Urgent Care Visit Tracking Support</td>
</tr>
<tr class="odd">
<td>IBECEA39</td>
<td>Multi-site maintains UC VISIT TRACKING FILE (#351.82) - PULL</td>
</tr>
<tr class="even">
<td>IBECEA4</td>
<td>Cancel / Edit / Add Charges - logic for the Cancel a Charge action.</td>
</tr>
<tr class="odd">
<td>IBECEA5, IBECEA51</td>
<td>Cancel / Edit / Add Charges - logic for the Update Events action, and subsequent actions on the Update Events list.</td>
</tr>
<tr class="even">
<td>IBECEAU, IBECEAU1, IBECEAU2, IBECEAU3, IBECEAU4</td>
<td>Cancel / Edit / Add Charges - utilities used by all actions.</td>
</tr>
<tr class="odd">
<td>IBECEAU5</td>
<td>Cancel / Edit / Add CALC Observation CO-PAY</td>
</tr>
<tr class="even">
<td>IBECEAU6</td>
<td>Cancel a copay charge API (for COVID-19 period cancellations)</td>
</tr>
<tr class="odd">
<td>IBECK</td>
<td>Checks status of filer</td>
</tr>
<tr class="even">
<td>IBECPF</td>
<td>Continuous Patient flag / un-flag</td>
</tr>
<tr class="odd">
<td>IBECPTE</td>
<td>Enter and / or edit BASC table reference data</td>
</tr>
<tr class="even">
<td>IBECPTT</td>
<td>Transfers BASC rate group and status updates from the UPDATE BILLABLE AMBULATORY SURGICAL CODE file (#350.41) to the BILLABLE AMBULATORY SURGICAL CODE file (#350.4).</td>
</tr>
<tr class="odd">
<td>IBECPTT</td>
<td>TRANSFERS CPT RATE UPDATES TO 350.4</td>
</tr>
<tr class="even">
<td>IBECPTZ</td>
<td>BASC transfer utility</td>
</tr>
<tr class="odd">
<td>IBECUS</td>
<td>TRICARE PHARMACY ENGINE OPTIONS</td>
</tr>
<tr class="even">
<td>IBECUS1</td>
<td>TRICARE PHARMACY BILLING ENGINES</td>
</tr>
<tr class="odd">
<td>IBECUS2</td>
<td>TRICARE PHARMACY BILL TRANSACTION</td>
</tr>
<tr class="even">
<td>IBECUS21</td>
<td>FILE TRICARE PHARMACY TRANSACTIONS</td>
</tr>
<tr class="odd">
<td>IBECUS22</td>
<td>TRICARE PHARMACY BILLING UTILITIES</td>
</tr>
<tr class="even">
<td>IBECUS3</td>
<td>CANCEL TRICARE PHARMACY TRANSACTION</td>
</tr>
<tr class="odd">
<td>IBECUSM</td>
<td>TRICARE PHARMACY BILLING OPTIONS</td>
</tr>
<tr class="even">
<td>IBECUSMU</td>
<td>PHARMACY BILLING OPTION UTILITIES</td>
</tr>
<tr class="odd">
<td>IBECUSO</td>
<td>TRICARE PHARMACY BILLING OUTPUTS</td>
</tr>
<tr class="even">
<td>IBEF</td>
<td>Integrated Billing background filer</td>
</tr>
<tr class="odd">
<td>IBEFCOP</td>
<td>Background filer, Rx co-payment processor</td>
</tr>
<tr class="even">
<td>IBEFSMUT</td>
<td>Gather and return individual patient billing information from either File #350 or File #399</td>
</tr>
<tr class="odd">
<td>IBEFUNC</td>
<td>Set of extrinsic functions</td>
</tr>
<tr class="even">
<td>IBEFUNC1, IBEFUNC2</td>
<td>Set of extrinsic functions used in BASC billing</td>
</tr>
<tr class="odd">
<td>IBEFUNC3</td>
<td>EXTRINSIC FUNCTIONS</td>
</tr>
<tr class="even">
<td>IBEFUR</td>
<td>UTILITY: FIND RELATED FIRST AND THIRD PARTY BILLS</td>
</tr>
<tr class="odd">
<td>IBEFURF</td>
<td>UTILITY: FIND RELATED FIRST PARTY BILLS</td>
</tr>
<tr class="even">
<td>IBEFURT</td>
<td>UTILITY: FIND RELATED THIRD PARTY BILLS</td>
</tr>
<tr class="odd">
<td>IBEFUTL</td>
<td>Utility program for filer options</td>
</tr>
<tr class="even">
<td>IBEFUTL1</td>
<td>Recompiles and cross references all IB templates.</td>
</tr>
<tr class="odd">
<td>IBEMTBC</td>
<td>Category C billing clock maintenance</td>
</tr>
<tr class="even">
<td>IBEMTF, IBEMTF1</td>
<td>Flag Stop Codes / Dispositions / Clinics</td>
</tr>
<tr class="odd">
<td>IBEMTF2</td>
<td>List Non-Billable Stop Codes / Dispositions / Clinics</td>
</tr>
<tr class="even">
<td>IBEMTO</td>
<td>Bills all Means Test Outpatient co-payment charges that are on hold awaiting the new co-pay rate.</td>
</tr>
<tr class="odd">
<td>IBEMTO1</td>
<td>Lists all Means Test Outpatient co-payment charges that are on hold awaiting the new co-pay rate.</td>
</tr>
<tr class="even">
<td>IBEMTSCR</td>
<td>Print billable types for visit co-pay</td>
</tr>
<tr class="odd">
<td>IBEMTSCU</td>
<td>Print billable types for visit co-pay</td>
</tr>
<tr class="even">
<td>IBEPAR, IBEPAR1</td>
<td>IB Site Parameter entry and edit. (Routines formerly named DGCRPAR, DGCRPAR1.)</td>
</tr>
<tr class="odd">
<td>IBEPTC</td>
<td>TP FLAG STOP CODES AND CLINICS</td>
</tr>
<tr class="even">
<td>IBEPTC1</td>
<td>TP FLAG STOP CODES AND CLINICS (CON'T.)</td>
</tr>
<tr class="odd">
<td>IBEPTC2</td>
<td>TP LIST NON-BILLABLE STOP CODES AND CLINICS</td>
</tr>
<tr class="even">
<td>IBEPTC3</td>
<td>TP FLAG ALL CLINICS</td>
</tr>
<tr class="odd">
<td>IBERS</td>
<td>User interface for the Appointment Check-off Sheet.</td>
</tr>
<tr class="even">
<td>IBERS1</td>
<td>Search, sort, and print Appointment Check-off Sheets chosen by the user.</td>
</tr>
<tr class="odd">
<td>IBERS2</td>
<td>Gather and store individual patient data for a Check-off Sheet.</td>
</tr>
<tr class="even">
<td>IBERS3</td>
<td>Gather and store individual patient PTF and billing diagnoses for a Check-off Sheet.</td>
</tr>
<tr class="odd">
<td>IBERSE</td>
<td>Build and edit the CPT lists for the Check-off Sheets.</td>
</tr>
<tr class="even">
<td>IBERSI</td>
<td>List and / or delete procedures on Check-off Sheets that are AMA inactive and / or nationally, locally, and billing inactive.</td>
</tr>
<tr class="odd">
<td>IBERSP</td>
<td>Prints the formatted CPT list for the Check-off Sheets.</td>
</tr>
<tr class="even">
<td>IBERSP1</td>
<td>Creates the formatted CPT list for the Check-off Sheets.</td>
</tr>
<tr class="odd">
<td>IBESTAT</td>
<td>Status display of IB site parameters and filer status</td>
</tr>
<tr class="even">
<td>IBETIME</td>
<td>Capacity management utility</td>
</tr>
<tr class="odd">
<td>IBINRPT</td>
<td>Indian Attestation Copay Exemption Report</td>
</tr>
<tr class="even">
<td>IBINUT1</td>
<td>Indian Attestation Copay Exemption Report Utilities</td>
</tr>
<tr class="odd">
<td>IBJD</td>
<td>DIAGNOSTIC MEASURES UTILITIES</td>
</tr>
<tr class="even">
<td>IBJD1</td>
<td>DIAGNOSTIC MEASURES UTILITIES</td>
</tr>
<tr class="odd">
<td>IBJDB1</td>
<td>BILLING LAG TIME REPORT</td>
</tr>
<tr class="even">
<td>IBJDB11</td>
<td>BILLING LAG TIME REPORT (COMPILE)</td>
</tr>
<tr class="odd">
<td>IBJDB12</td>
<td>BILLING LAG TIME REPORT (OPT PRINT / SUMMARIES)</td>
</tr>
<tr class="even">
<td>IBJDB13</td>
<td>BILLING LAG TIME REPORT (INPT PRINT)</td>
</tr>
<tr class="odd">
<td>IBJDB2</td>
<td>REASONS NOT BILLABLE REPORT (INPUT)</td>
</tr>
<tr class="even">
<td>IBJDB21</td>
<td>REASONS NOT BILLABLE REPORT (COMPILE)</td>
</tr>
<tr class="odd">
<td>IBJDB22</td>
<td>REASONS NOT BILLABLE REPORT (PRINT)</td>
</tr>
<tr class="even">
<td>IBJDE</td>
<td>DM DATA EXTRACTION (MAIN ROUTINE)</td>
</tr>
<tr class="odd">
<td>IBJDE1</td>
<td>DM DATA EXTRACTION (MENU OPTIONS / TRANSMIT E-MAIL)</td>
</tr>
<tr class="even">
<td>IBJDF1</td>
<td>THIRD PARTY FOLLOW-UP REPORT</td>
</tr>
<tr class="odd">
<td>IBJDF11</td>
<td>THIRD PARTY FOLLOW-UP REPORT (COMPILE)</td>
</tr>
<tr class="even">
<td>IBJDF12</td>
<td>THIRD PARTY FOLLOW-UP REPORT (PRINT)</td>
</tr>
<tr class="odd">
<td>IBJDF1H</td>
<td>THIRD PARTY FOLLOW-UP REPORT (HELP)</td>
</tr>
<tr class="even">
<td>IBJDF2</td>
<td>THIRD PARTY FOLLOW-UP SUMMARY REPORT</td>
</tr>
<tr class="odd">
<td>IBJDF4</td>
<td>FIRST PARTY FOLLOW-UP REPORT</td>
</tr>
<tr class="even">
<td>IBJDF41</td>
<td>FIRST PARTY FOLLOW-UP REPORT (COMPILE)</td>
</tr>
<tr class="odd">
<td>IBJDF42</td>
<td>FIRST PARTY FOLLOW-UP REPORT (PRINT)</td>
</tr>
<tr class="even">
<td>IBJDF43</td>
<td>FIRST PARTY FOLLOW-UP REPORT (COMPILE/PRINT SUMMARY)</td>
</tr>
<tr class="odd">
<td>IBJDF4H</td>
<td>FIRST PARTY FOLLOW-UP REPORT (HELP)</td>
</tr>
<tr class="even">
<td>IBJDF5</td>
<td>CHAMPVA / TRICARE FOLLOW-UP REPORT</td>
</tr>
<tr class="odd">
<td>IBJDF51</td>
<td>CHAMPVA / TRICARE FOLLOW-UP REPORT (COMPILE)</td>
</tr>
<tr class="even">
<td>IBJDF52</td>
<td>CHAMPVA / TRICARE FOLLOW-UP REPORT (PRINT)</td>
</tr>
<tr class="odd">
<td>IBJDF53</td>
<td>CHAMPVA / TRICARE FOLLOW-UP REPORT (SUMMARY)</td>
</tr>
<tr class="even">
<td>IBJDF5H</td>
<td>CHAMPVA / TRICARE FOLLOW-UP REPORT (HELP)</td>
</tr>
<tr class="odd">
<td>IBJDF6</td>
<td>MISCELLANEOUS BILLS FOLLOW-UP REPORT</td>
</tr>
<tr class="even">
<td>IBJDF61</td>
<td>MISC. BILLS FOLLOW-UP REPORT (COMPILE)</td>
</tr>
<tr class="odd">
<td>IBJDF62</td>
<td>MISC. BILLS FOLLOW-UP REPORT (PRINT)</td>
</tr>
<tr class="even">
<td>IBJDF63</td>
<td>MISC. BILLS FOLLOW-UP REPORT (COMPILE/PRINT SUMMARY)</td>
</tr>
<tr class="odd">
<td>IBJDF6H</td>
<td>MISCELLANEOUS BILLS FOLLOW-UP REPORT (HELP)</td>
</tr>
<tr class="even">
<td>IBJDF7</td>
<td>REPAYMENT PLAN REPORT</td>
</tr>
<tr class="odd">
<td>IBJDF71</td>
<td>REPAYMENT PLAN REPORT (COMPILE)</td>
</tr>
<tr class="even">
<td>IBJDF72</td>
<td>REPAYMENT PLAN REPORT (PRINT)</td>
</tr>
<tr class="odd">
<td>IBJDF7H</td>
<td>REPAYMENT PLAN REPORT (HELP)</td>
</tr>
<tr class="even">
<td>IBJDF8</td>
<td>AR PRODUCTIVITY REPORT</td>
</tr>
<tr class="odd">
<td>IBJDF81</td>
<td>AR PRODUCTIVITY REPORT (COMPILE)</td>
</tr>
<tr class="even">
<td>IBJDF811</td>
<td>AR PRODUCTIVITY REPORT (COMPILE-cont.)</td>
</tr>
<tr class="odd">
<td>IBJDF82</td>
<td>AR PRODUCTIVITY REPORT (PRINT)</td>
</tr>
<tr class="even">
<td>IBJDF8H</td>
<td>AR PRODUCTIVITY REPORT (HELP)</td>
</tr>
<tr class="odd">
<td>IBJDF8I</td>
<td>ADD / EDIT IB DM WORKLOAD PARAMETERS</td>
</tr>
<tr class="even">
<td>IBJDF8I1</td>
<td>ADD / EDIT IB DM WORKLOAD PARAMETERS-(CONT.)</td>
</tr>
<tr class="odd">
<td>IBJDF8R</td>
<td>AR WORKLOAD ASSIGNMENTS (PRINT)</td>
</tr>
<tr class="even">
<td>IBJDI1</td>
<td>PERCENTAGE OF COMPLETED REGISTRATIONS</td>
</tr>
<tr class="odd">
<td>IBJDI11</td>
<td>PERCENTAGE OF COMPLETED REGISTRATIONS (CONT'D)</td>
</tr>
<tr class="even">
<td>IBJDI2</td>
<td>VETERANS WITH UNVERIFIED ELIGIBILITY</td>
</tr>
<tr class="odd">
<td>IBJDI21</td>
<td>VETERANS WITH UNVERIFIED ELIGIBILITY (CONT'D)</td>
</tr>
<tr class="even">
<td>IBJDI3</td>
<td>NO EMPLOYER LISTING</td>
</tr>
<tr class="odd">
<td>IBJDI4</td>
<td>PATIENTS WITH UNIDENTIFIED INSURANCE</td>
</tr>
<tr class="even">
<td>IBJDI41</td>
<td>PATIENTS WITH UNIDENTIFIED INSURANCE (CONT'D)</td>
</tr>
<tr class="odd">
<td>IBJDI5</td>
<td>INSURANCE POLICIES NOT VERIFIED</td>
</tr>
<tr class="even">
<td>IBJDI6</td>
<td>SC VETS W/ NSC EPISODES OF INPT CARE</td>
</tr>
<tr class="odd">
<td>IBJDI7</td>
<td>OUTPATIENT WORKLOAD REPORT</td>
</tr>
<tr class="even">
<td>IBJDIPR</td>
<td>PERCENTAGE OF PATIENTS PREREGISTERED REPORT</td>
</tr>
<tr class="odd">
<td>IBJDNTEG</td>
<td>ISC / XTSUMBLD KERNEL - Package checksum checker</td>
</tr>
<tr class="even">
<td>IBJDU1</td>
<td>UTILIZATION WORKLOAD REPORT</td>
</tr>
<tr class="odd">
<td>IBJPB</td>
<td>IBSP AUTOMATED BILLING SCREEN</td>
</tr>
<tr class="even">
<td>IBJPC</td>
<td>IBSP CLAIMS TRACKING PARAMETER SCREEN</td>
</tr>
<tr class="odd">
<td>IBJPC1</td>
<td>Routine for Site Parameter Health Care Service Review (HCSR) screen (nodes 63-66)</td>
</tr>
<tr class="even">
<td>IBJPC2</td>
<td>Routine for HCSR Ward Parameter screen</td>
</tr>
<tr class="odd">
<td>IBJPC3</td>
<td>Clinic and Ward Inclusion list by payer for Site Parameter HCSR screen</td>
</tr>
<tr class="even">
<td>IBJPI</td>
<td>IBJP eIV SITE PARAMETERS SCREEN</td>
</tr>
<tr class="odd">
<td>IBJPI2</td>
<td>eIV SITE PARAMETERS SCREEN ACTIONS</td>
</tr>
<tr class="even">
<td>IBJPI5</td>
<td>eIV SITE PARAMETERS SCREEN</td>
</tr>
<tr class="odd">
<td>IBJPM</td>
<td>IBSP MCCR PARAMETERS SCREEN</td>
</tr>
<tr class="even">
<td>IBJPS</td>
<td>IBSP IB SITE PARAMETER SCREEN</td>
</tr>
<tr class="odd">
<td>IBJPS1</td>
<td>IBSP IB SITE PARAMETER BUILD</td>
</tr>
<tr class="even">
<td>IBJPS2</td>
<td>IBSP IB SITE PARAMETER BUILD (CONT.)</td>
</tr>
<tr class="odd">
<td>IBJPS3</td>
<td>IB SITE PARAMETERS, PAY-TO PROVIDER</td>
</tr>
<tr class="even">
<td>IBJPS4</td>
<td>IB Site Parameters, Pay-To Provider Associations</td>
</tr>
<tr class="odd">
<td>IBJPS5</td>
<td>IB Site Parameters, Revenue Codes</td>
</tr>
<tr class="even">
<td>IBJPS6</td>
<td>IB Site Parameters, Administrative Contractors</td>
</tr>
<tr class="odd">
<td>IBJPS7</td>
<td>IB Site Parameters, Pay-To Provider Rate Types</td>
</tr>
<tr class="even">
<td>IBJPS8</td>
<td>IB Site Parameters, CMN CPT Inclusions CPT Codes</td>
</tr>
<tr class="odd">
<td>IBJTA1</td>
<td>TPI ACTIONS</td>
</tr>
<tr class="even">
<td>IBJTAD</td>
<td>Third Party Joint Inquiry (TPJI) Electronic Remittance Advice (ERA) / 835 ADDITIONAL INFORMATION SCREEN</td>
</tr>
<tr class="odd">
<td>IBJTBA, IBJTBA1</td>
<td>Used to display TPJI bill charge information.</td>
</tr>
<tr class="even">
<td>IBJTBB</td>
<td>TPI BILL DIAGNOSIS SCREEN</td>
</tr>
<tr class="odd">
<td>IBJTBC</td>
<td>TPI BILL PROCEDURES SCREEN</td>
</tr>
<tr class="even">
<td>IBJTCA</td>
<td>TPI CLAIMS INFO BUILD</td>
</tr>
<tr class="odd">
<td>IBJTCA1</td>
<td>TPI CLAIMS INFO BUILD</td>
</tr>
<tr class="even">
<td>IBJTCA2</td>
<td>TPI CLAIMS INFO BUILD (CONT)</td>
</tr>
<tr class="odd">
<td>IBJTEA</td>
<td>TPI PATIENT ELIGIBLITY SCREEN</td>
</tr>
<tr class="even">
<td>IBJTED</td>
<td>TPJI EDI STATUS SCREEN</td>
</tr>
<tr class="odd">
<td>IBJTEP</td>
<td>TPJI ERA / 835 INFORMATION SCREEN</td>
</tr>
<tr class="even">
<td>IBJTEP1</td>
<td>TPJI utility Routine for the IBJTEP and IBJTPE routines</td>
</tr>
<tr class="odd">
<td>IBJTLA</td>
<td>TPI ACTIVE BILLS LIST SCREEN</td>
</tr>
<tr class="even">
<td>IBJTLA1</td>
<td>TPI ACTIVE BILLS LIST BUILD</td>
</tr>
<tr class="odd">
<td>IBJTLB</td>
<td>TPI INACTIVE LIST SCREEN</td>
</tr>
<tr class="even">
<td>IBJTLB1</td>
<td>TPI INACTIVE LIST BUILD</td>
</tr>
<tr class="odd">
<td>IBJTNA</td>
<td>TPI INSURANCE SCREENS / ACTIONS</td>
</tr>
<tr class="even">
<td>IBJTNB</td>
<td>TPI INSURANCE POLICY / AB SCREENS / ACTIONS</td>
</tr>
<tr class="odd">
<td>IBJTPE</td>
<td>TPJI ERA / 835 PRINT EEOB INFORMATION SCREEN</td>
</tr>
<tr class="even">
<td>IBJTNC</td>
<td>TPI INSURANCE PATIENT POLICIES</td>
</tr>
<tr class="odd">
<td>IBJTRA, IBJTRA1</td>
<td>Used to display Claims Tracking insurance communications.</td>
</tr>
<tr class="even">
<td>IBJTRX</td>
<td>TPJI screen for ECME response information</td>
</tr>
<tr class="odd">
<td>IBJTTA</td>
<td>TPI AR ACCOUNT / CLAIM PROFILE</td>
</tr>
<tr class="even">
<td>IBJTTA1</td>
<td>TPI AR ACCOUNT / CLAIM PROFILE BUILD</td>
</tr>
<tr class="odd">
<td>IBJTTB</td>
<td>TPI AR TRANSACTION PROFILE</td>
</tr>
<tr class="even">
<td>IBJTTB1</td>
<td>TPI AR TRANSACTION PROFILE BUILD</td>
</tr>
<tr class="odd">
<td>IBJTTB2</td>
<td>TPI AR TRANSACTION PROFILE (CONT)</td>
</tr>
<tr class="even">
<td>IBJTTC</td>
<td>TPI AR COMMENT HISTORY</td>
</tr>
<tr class="odd">
<td>IBJTU1</td>
<td>TPI UTILITIES</td>
</tr>
<tr class="even">
<td>IBJTU2</td>
<td>TPI UTILITIES</td>
</tr>
<tr class="odd">
<td>IBJTU3</td>
<td>TPI UTILITIES – INS ADDRESS</td>
</tr>
<tr class="even">
<td>IBJTU31</td>
<td>TPI UTILITIES – INS</td>
</tr>
<tr class="odd">
<td>IBJTU4</td>
<td>TPI UTILITIES – AR CALLS</td>
</tr>
<tr class="even">
<td>IBJTU5</td>
<td>TPI UTILITIES – BILLS / CLAIMS TRACKING</td>
</tr>
<tr class="odd">
<td>IBJTU6</td>
<td>IB List Manager API. See Integration Agreement 5713</td>
</tr>
<tr class="even">
<td>IBJU1</td>
<td>JBI UTILITIES</td>
</tr>
<tr class="odd">
<td>IBJVDEQ</td>
<td>CBO Data Extract Queue Trigger</td>
</tr>
<tr class="even">
<td>IBJYL</td>
<td>List Template Exporter</td>
</tr>
<tr class="odd">
<td>IBJYL1</td>
<td>List Template Exporter</td>
</tr>
<tr class="even">
<td>IBJYL2</td>
<td>List Template Exporter</td>
</tr>
<tr class="odd">
<td>IBJYL3</td>
<td>List Template Exporter</td>
</tr>
<tr class="even">
<td>IBJYL4</td>
<td>List Template Exporter</td>
</tr>
<tr class="odd">
<td>IBJYPT</td>
<td>IBJ V2.0 POST-INITIALIZATION ROUTINE</td>
</tr>
<tr class="even">
<td>IBMFNHLI</td>
<td>Process incoming MFN Messages for table updates related to X12 278 messages.</td>
</tr>
<tr class="odd">
<td>IBNCDNC</td>
<td>DRUGS NON COVERED</td>
</tr>
<tr class="even">
<td>IBNCDNC1</td>
<td>DRUGS NON COVERED</td>
</tr>
<tr class="odd">
<td>IBNCP*</td>
<td>IB routines related to ePharmacy / ECME processing and billing of electronic real-time prescriptions.</td>
</tr>
<tr class="even">
<td>IBNCPBB</td>
<td>ECME BACKBILLING</td>
</tr>
<tr class="odd">
<td>IBNCPBB1</td>
<td>CONTINUATION OF ECME BACKBILLING</td>
</tr>
<tr class="even">
<td>IBNCPDP</td>
<td>APIS FOR NCPCP / ECME</td>
</tr>
<tr class="odd">
<td>IBNCPDP1</td>
<td>PROCESSING FOR NEW RX REQUESTS</td>
</tr>
<tr class="even">
<td>IBNCPDP2</td>
<td>PROCESSING FOR ECME RESP</td>
</tr>
<tr class="odd">
<td>IBNCPDP3</td>
<td>STORES NDC / AWP UPDATES</td>
</tr>
<tr class="even">
<td>IBNCPDP4</td>
<td>HANDLE ECME EVENTS</td>
</tr>
<tr class="odd">
<td>IBNCPDP5</td>
<td>PROCESSING FOR ECME RESP FOR SECONDARY</td>
</tr>
<tr class="even">
<td>IBNCPDP6</td>
<td>TRICARE NCPDP TOOLS</td>
</tr>
<tr class="odd">
<td>IBNCPDPC</td>
<td>CLAIMS TRACKING EDITOR for ECME</td>
</tr>
<tr class="even">
<td>IBNCPDPE</td>
<td>NCPDP BILLING EVENTS REPORT</td>
</tr>
<tr class="odd">
<td>IBNCPDPH</td>
<td>ECME REPORT OF ON HOLD CHARGES FOR A PATIENT</td>
</tr>
<tr class="even">
<td>IBNCPDPI</td>
<td>ECME SCREEN INSURANCE VIEW AND UTILITIES</td>
</tr>
<tr class="odd">
<td>IBNCPDPL</td>
<td>for ECME RESEARCH SCREEN ELIGIBILITY VIEW</td>
</tr>
<tr class="even">
<td>IBNCPDPR</td>
<td>ECME RELEASE CHARGES ON HOLD</td>
</tr>
<tr class="odd">
<td>IBNCPDPU</td>
<td>UTILITIES FOR NCPCP</td>
</tr>
<tr class="even">
<td>IBNCPDPV</td>
<td>for ECME SCREEN VIEW PATIENT INSURANCE</td>
</tr>
<tr class="odd">
<td>IBNCPDR</td>
<td>ROI MANAGEMENT, LIST MANAGER</td>
</tr>
<tr class="even">
<td>IBNCPDR1</td>
<td>ROI MANAGEMENT</td>
</tr>
<tr class="odd">
<td>IBNCPDR2</td>
<td>ROI MANAGEMENT, ADD ROI</td>
</tr>
<tr class="even">
<td>IBNCPDR4</td>
<td>ROI MANAGEMENT, ROI CHECK</td>
</tr>
<tr class="odd">
<td>IBNCPDR5</td>
<td>ROI MANAGEMENT, EXPAND ROI</td>
</tr>
<tr class="even">
<td>IBNCPDRA</td>
<td>ROI EXPIRATION REPORT USER SELECTION CRITERIA</td>
</tr>
<tr class="odd">
<td>IBNCPDRB</td>
<td>ROI EXPIRATION REPORT DISPLAY</td>
</tr>
<tr class="even">
<td>IBNCPDS1</td>
<td>DISPLAY RX COB DETERMINATION</td>
</tr>
<tr class="odd">
<td>IBNCPEB</td>
<td>BULLETINS FOR NCPDP</td>
</tr>
<tr class="even">
<td>IBNCPEV</td>
<td>NCPDP BILLING EVENTS REPORT</td>
</tr>
<tr class="odd">
<td>IBNCPEV1</td>
<td>NCPDP BILLING EVENTS REPORT</td>
</tr>
<tr class="even">
<td>IBNCPEV3</td>
<td>NCPDP BILLING EVENTS REPORT-APIs for new BPS RPT NON-BILLABLE REPORT in the ECME application.</td>
</tr>
<tr class="odd">
<td>IBNCPLOG</td>
<td>IB ECME EVNT REPORT</td>
</tr>
<tr class="even">
<td>IBNCPNB</td>
<td>UTILITIES FOR NCPCP</td>
</tr>
<tr class="odd">
<td>IBNCPRR</td>
<td>Prescription Report for 3rd Party Billing cross check</td>
</tr>
<tr class="even">
<td>IBNCPRR1</td>
<td>Prescription Report for 3rd Party Billing (Extrinsic Functions)</td>
</tr>
<tr class="odd">
<td>IBNCPUT1</td>
<td>IB NCPDP UTILITIES</td>
</tr>
<tr class="even">
<td>IBNCPUT2</td>
<td>IB NCPDP UTILITIES</td>
</tr>
<tr class="odd">
<td>IBNCPUT3</td>
<td>ePharmacy secondary billing</td>
</tr>
<tr class="even">
<td>IBNTEG*</td>
<td>IB integrity routines.</td>
</tr>
<tr class="odd">
<td>IBOA31</td>
<td>List All Bills For a Patient Report. (Routine formerly named DGCRA31.)</td>
</tr>
<tr class="even">
<td>IBOA32</td>
<td>Continuation of List All Bills For a Patient Report. Retrieves and displays Integrated Billing Actions. (Routine formerly named DGCRA32.)</td>
</tr>
<tr class="odd">
<td>IBOAMS</td>
<td>Revenue Code Totals by Rate Type Report. (Routine formerly named DGCRAMS1.)</td>
</tr>
<tr class="even">
<td>IBOBCC, IBOBCC1</td>
<td>Search, sort, and print the Unbilled BASC for Insured Patient Appointment Report.</td>
</tr>
<tr class="odd">
<td>IBOBCR6</td>
<td>Continuous Pt. Report - displays a listing of patients who have been continuously hospitalized since July 1, 1986.</td>
</tr>
<tr class="even">
<td>IBOBCRT</td>
<td>Billing Cycle Inquiry - displays 90 day billing clocks, primary eligibility code, status, etc.</td>
</tr>
<tr class="odd">
<td>IBOBL</td>
<td>List bills for an episode of care. (Routine formerly named DGCROBL.)</td>
</tr>
<tr class="even">
<td>IBOCDRPT</td>
<td>Lists charges that may need to be cancelled because the patient is identified as Catastrophically Disabled.</td>
</tr>
<tr class="odd">
<td>IBOCHK</td>
<td>Verifies links from IB to Pharmacy.</td>
</tr>
<tr class="even">
<td>IBOCNC</td>
<td>Determine Clinic CPT Usage Report search parameters from user input.</td>
</tr>
<tr class="odd">
<td>IBOCNC1</td>
<td>Search and sort the Clinic CPT Usage Report.</td>
</tr>
<tr class="even">
<td>IBOCNC2</td>
<td>Print the Clinic CPT Usage Report.</td>
</tr>
<tr class="odd">
<td>IBOCOSI</td>
<td>Search, sort, and print the inactive CPT codes on Check-off Sheets Report.</td>
</tr>
<tr class="even">
<td>IBOCPD</td>
<td>Option for printing the full or summary Clerk Productivity Report.</td>
</tr>
<tr class="odd">
<td>IBOCPDS</td>
<td>Search, sort, and print the Clerk Productivity Summary Report.</td>
</tr>
<tr class="even">
<td>IBODISP</td>
<td>Brief and full inquiry to Integrated Billing Actions.</td>
</tr>
<tr class="odd">
<td>IBODIV</td>
<td>Select division or clinic.</td>
</tr>
<tr class="even">
<td>IBOEMP, IBOEMP1, IBOEMP2</td>
<td>List of employed patients with no insurance coverage.</td>
</tr>
<tr class="odd">
<td>IBOHCK</td>
<td>CHECK FOR IB CHARGES ON HOLD</td>
</tr>
<tr class="even">
<td>IBOHCR</td>
<td>RELEASE / UPDATE A PATIENTS CHARGES ON HOLD</td>
</tr>
<tr class="odd">
<td>IBOHCT</td>
<td>CHECK FOR IB CHARGES ON HOLD</td>
</tr>
<tr class="even">
<td>IBOHDT*</td>
<td>REPORT OF CHARGES ON HOLD &gt; 60 DAYS</td>
</tr>
<tr class="odd">
<td>IBOHDT1</td>
<td>REPORT OF CHARGES ON HOLD &gt; 60 DAYS-CONT</td>
</tr>
<tr class="even">
<td>IBOHFIX</td>
<td>CLEAN UP ROUTINE FOR PATCH IB*2*95</td>
</tr>
<tr class="odd">
<td>IBOHIST</td>
<td>HISTORY OF CHARGES ON HOLD REPORT</td>
</tr>
<tr class="even">
<td>IBOHLD1, IBOHLD2</td>
<td>Report of Category C Charges On Hold</td>
</tr>
<tr class="odd">
<td>IBOHPT*</td>
<td>Report of Charges On Hold for a Patient</td>
</tr>
<tr class="even">
<td>IBOHPT1</td>
<td>REPORT OF ON HOLD CHARGES FOR A PATIENT</td>
</tr>
<tr class="odd">
<td>IBOHPT2</td>
<td>ON HOLD CHARGE INFO / PT CONT.</td>
</tr>
<tr class="even">
<td>IBOHRAR</td>
<td>RELEASED CHARGES REPORT</td>
</tr>
<tr class="odd">
<td>IBOHRL</td>
<td>AUTO-RELEASE CHARGES ON HOLD &gt; 90 DAYS</td>
</tr>
<tr class="even">
<td>IBOHTOT</td>
<td>COUNT / AMT OF CHARGES ON HOLD REPORT</td>
</tr>
<tr class="odd">
<td>IBOLK</td>
<td>Patient Billing Inquiry - user interface, prints IB Actions.</td>
</tr>
<tr class="even">
<td>IBOLK1</td>
<td>Address Inquiry</td>
</tr>
<tr class="odd">
<td>IBOMBL</td>
<td>MCCR MAS Billing Log. (Routine formerly named DGCROMBL.)</td>
</tr>
<tr class="even">
<td>IBOMHC</td>
<td>COMPACT Act Copay Review Report</td>
</tr>
<tr class="odd">
<td>IBOMTC</td>
<td>Category C Activity Listing - user interface</td>
</tr>
<tr class="even">
<td>IBOMTC1</td>
<td>Category C Activity Listing - compilation and output</td>
</tr>
<tr class="odd">
<td>IBOMTE</td>
<td>Estimate Category C Charges - user interface</td>
</tr>
<tr class="even">
<td>IBOMTE1</td>
<td>Estimate Category C Charges - output</td>
</tr>
<tr class="odd">
<td>IBOMTE2</td>
<td>Estimate Category C Charges - compile charges</td>
</tr>
<tr class="even">
<td>IBOMTLTC</td>
<td>MT / LTC CO-PAY REMOTE QUERY</td>
</tr>
<tr class="odd">
<td>IBOMTP</td>
<td>Single Patient Cat C Profile - user interface</td>
</tr>
<tr class="even">
<td>IBOMTP1</td>
<td>Single Patient Cat C Profile - compilation and output</td>
</tr>
<tr class="odd">
<td>IBORAT</td>
<td>Top level routine for Billing Rates Listing</td>
</tr>
<tr class="even">
<td>IBORAT1A</td>
<td>Builds a temp file of data from the IB ACTION CHARGE file (#350.2).</td>
</tr>
<tr class="odd">
<td>IBORAT1B</td>
<td>Parses the temp file built by IBORAT1A and calculates effective dates for IB ACTION CHARGES.</td>
</tr>
<tr class="even">
<td>IBORAT1C</td>
<td>Writes the IB ACTION CHARGES to the selected device.</td>
</tr>
<tr class="odd">
<td>IBORAT2A</td>
<td>Filters the BILLING RATES file (#399.5) to build a temp file of billing rates.</td>
</tr>
<tr class="even">
<td>IBORAT2B</td>
<td>Parses the temp file built by IBORAT2A and calculates effective dates for BILLING RATES.</td>
</tr>
<tr class="odd">
<td>IBORAT2C</td>
<td>Writes the BILLING RATES to the selected device.</td>
</tr>
<tr class="even">
<td>IBORT, IBORT1</td>
<td>MCCR MAS Billing Totals Report. (Routines formerly named DGCRORT, DGCRORT1.)</td>
</tr>
<tr class="odd">
<td>IBOSCDC</td>
<td>SERVICE CONNECTED DETERMINATION CHANGE REPORT</td>
</tr>
<tr class="even">
<td>IBOSCDC1</td>
<td>SERVICE CONNECTED DETERMINATION CHANGE REPORT UTILITIES</td>
</tr>
<tr class="odd">
<td>IBOSRX</td>
<td>POTENTIAL SECONDARY RX CLAIMS REPORT</td>
</tr>
<tr class="even">
<td>IBOST</td>
<td>Statistics report routine</td>
</tr>
<tr class="odd">
<td>IBOSTUS, IBOSTUS1</td>
<td>Bill Status Report. (Routines formerly named DGCROST, DGCROST1.)</td>
</tr>
<tr class="even">
<td>IBOTR, IBOTR1, IBOTR11</td>
<td>Insurance Payment Trend Report user interface. (Routines IBOTR and IBOTR1 were formerly named DGCROTR, DGCROTR1.)</td>
</tr>
<tr class="odd">
<td>IBOTR2</td>
<td>Insurance Payment Trend Report data compilation. (Routine formerly named DGCROTR2.)</td>
</tr>
<tr class="even">
<td>IBOTR3, IBOTR4</td>
<td>Insurance Payment Trend Report output. (Routines formerly named DGCROTR3, DGCROTR4.)</td>
</tr>
<tr class="odd">
<td>IBOTRR</td>
<td>ROI Expired Consent Report</td>
</tr>
<tr class="even">
<td>IBOUNP1, IBOUNP2, IBOUNP3</td>
<td>Inpatients w/Unknown or Expired Insurance Report</td>
</tr>
<tr class="odd">
<td>IBOUNP4, IBOUNP5, IBOUNP6</td>
<td>Outpatients’ w/Unknown or Expired Insurance Report</td>
</tr>
<tr class="even">
<td>IBOUTL</td>
<td>Utility program for output reports</td>
</tr>
<tr class="odd">
<td>IBOVOP, IBOVOP1, IBOVOP2</td>
<td>Category C Outpatient / Events Report</td>
</tr>
<tr class="even">
<td>IBP</td>
<td>Archive / Purge - option driver</td>
</tr>
<tr class="odd">
<td>IBP431</td>
<td><p>POST INSTALL FOR IB*2.0*431</p>
<p>Reformats data in ^IBM(361.1 for HIPA 5010 changes.</p></td>
</tr>
<tr class="even">
<td>IBPA</td>
<td>Archive / Purge - Archive billing data</td>
</tr>
<tr class="odd">
<td>IBPEX</td>
<td>Contains the logic to purge entries from the BILLING EXEMPTIONS file (#354.1). This routine will not purge entries for approximately two years from its release date.</td>
</tr>
<tr class="even">
<td>IBPF, IBPF1</td>
<td>Archive / Purge - Find Billing Data to Archive</td>
</tr>
<tr class="odd">
<td>IBPFU</td>
<td>Archive / Purge - Find Billing Data to Archive utilities</td>
</tr>
<tr class="even">
<td>IBPO</td>
<td>Archive / Purge - Outputs - List Archive / Purge Log Entries; Archive / Purge Log Inquiry; List Search Template Entries.</td>
</tr>
<tr class="odd">
<td>IBPP</td>
<td>Archive / Purge - purge billing data</td>
</tr>
<tr class="even">
<td>IBPU, IBPU1, IBPU2</td>
<td>Archive / Purge - general utilities</td>
</tr>
<tr class="odd">
<td>IBPUBUL</td>
<td>Archive / Purge - generate mail message after archive / purge operation</td>
</tr>
<tr class="even">
<td>IBPUDEL</td>
<td>Archive / Purge - delete entries from a search template</td>
</tr>
<tr class="odd">
<td>IBQL356</td>
<td>UM ROLLUP - IBT DATA EXTRACTS</td>
</tr>
<tr class="even">
<td>IBQL356A</td>
<td>UM ROLLUP - IBT DATA EXTRACTS CONT.</td>
</tr>
<tr class="odd">
<td>IBQL538</td>
<td>IBQ EXTRACT DATA</td>
</tr>
<tr class="even">
<td>IBQLCHK</td>
<td>UM ROLLUP - CHECK INFO. IN IB(array)</td>
</tr>
<tr class="odd">
<td>IBQLD1</td>
<td>ACUTE / NON-ACUTE DOWNLOAD</td>
</tr>
<tr class="even">
<td>IBQLD1A</td>
<td>ACUTE / NON-ACUTE DOWNLOAD</td>
</tr>
<tr class="odd">
<td>IBQLD2</td>
<td>PATIENT DOWNLOAD TO SPREADSHEET</td>
</tr>
<tr class="even">
<td>IBQLD2A</td>
<td>PATIENT DOWNLOAD TO SPREADSHEET</td>
</tr>
<tr class="odd">
<td>IBQLD3</td>
<td>PATIENT / PROVIDER REVIEW DOWNLOAD</td>
</tr>
<tr class="even">
<td>IBQLD3A</td>
<td>PROVIDER / PATIENT DOWNLOAD</td>
</tr>
<tr class="odd">
<td>IBQLD4</td>
<td>ACUTE / NON-ACUTE REPORT</td>
</tr>
<tr class="even">
<td>IBQLD4A</td>
<td>ACUTE / NON-ACUTE DOWNLOAD</td>
</tr>
<tr class="odd">
<td>IBQLLD</td>
<td>LOAD UMR FILE</td>
</tr>
<tr class="even">
<td>IBQLLD1</td>
<td>LOAD UMR FILE</td>
</tr>
<tr class="odd">
<td>IBQLLD2</td>
<td>LOAD UMR FILE / EDIT CHECK ORDER</td>
</tr>
<tr class="even">
<td>IBQLPL</td>
<td>PATIENTS QUALIFY / MISSING INFO LIST</td>
</tr>
<tr class="odd">
<td>IBQLPL1</td>
<td>PATIENTS QUALIFY / MISSING INFO LIST</td>
</tr>
<tr class="even">
<td>IBQLPL2</td>
<td>PRINT PATIENTS QUALIFY / MISSING LIST</td>
</tr>
<tr class="odd">
<td>IBQLPL3</td>
<td>PATIENTS QUALIFY / MISSING LIST</td>
</tr>
<tr class="even">
<td>IBQLPOST</td>
<td>CREATE IBQ ROLLUP MAILGROUP POST INT</td>
</tr>
<tr class="odd">
<td>IBQLPRE</td>
<td>PRE INSTALL INIT</td>
</tr>
<tr class="even">
<td>IBQLPRG</td>
<td>PURGE UMR FILE AFTER ROLLUP</td>
</tr>
<tr class="odd">
<td>IBQLR1</td>
<td>ACUTE / NON-ACUTE REPORT</td>
</tr>
<tr class="even">
<td>IBQLR1A</td>
<td>ACUTE / NON-ACUTE REPORT</td>
</tr>
<tr class="odd">
<td>IBQLR1B</td>
<td>ACUTE / NON-ACUTE REPORT</td>
</tr>
<tr class="even">
<td>IBQLR2</td>
<td>PATIENT REPORT</td>
</tr>
<tr class="odd">
<td>IBQLR2A</td>
<td>PATIENT REPORT</td>
</tr>
<tr class="even">
<td>IBQLR3</td>
<td>PATIENT / PROVIDER REVIEW REPORT</td>
</tr>
<tr class="odd">
<td>IBQLR3A</td>
<td>PROVIDER / PATIENT REPORT</td>
</tr>
<tr class="even">
<td>IBQLR4</td>
<td>ACUTE / NON-ACUTE REPORT</td>
</tr>
<tr class="odd">
<td>IBQLR4A</td>
<td>ACUTE / NON-ACUTE REPORT</td>
</tr>
<tr class="even">
<td>IBQLSCR</td>
<td>SCREEN DUMP OF RAW DATA FOR DOWNLOAD SPREADSHEET</td>
</tr>
<tr class="odd">
<td>IBQLT</td>
<td>TRANSMIT DATA</td>
</tr>
<tr class="even">
<td>IBQLT5</td>
<td>TRANSMIT PREVIOUS ROLLUPS</td>
</tr>
<tr class="odd">
<td>IBQLT5A</td>
<td>TRANSMIT PREVIOUS ROLLUPS</td>
</tr>
<tr class="even">
<td>IBQYIN</td>
<td>INITIALIZATION ROUTINE FOR PATCH IBQ*1*1</td>
</tr>
<tr class="odd">
<td>IBQYPT</td>
<td>POST-INITIALIZATION FOR PATCH IBQ*1*1</td>
</tr>
<tr class="even">
<td>IBR</td>
<td>Totals charges, passes to Accounts Receivable, and subsequently updates IB actions.</td>
</tr>
<tr class="odd">
<td>IBRBUL</td>
<td>Sends a mail message to the IB Category C mail group informing it that Category C charges have been determined for a veteran with insurance.</td>
</tr>
<tr class="even">
<td>IBRCON1</td>
<td>Allows the user to do a lookup on a cross-reference of patients with converted charges and then select one for processing.</td>
</tr>
<tr class="odd">
<td>IBRCON2</td>
<td>Passes all outpatient converted charges prior to a user-selected date to Accounts Receivable by calling routine ^IBR.</td>
</tr>
<tr class="even">
<td>IBRCON3</td>
<td>Top level routine for the IBRCON1 and IBRCON2.</td>
</tr>
<tr class="odd">
<td>IBRFIHL1</td>
<td>HL7 Process Incoming EHC_E12 Messages</td>
</tr>
<tr class="even">
<td>IBRFIHL2</td>
<td>HL7 Process Incoming EHC_E12 Messages (cont.)</td>
</tr>
<tr class="odd">
<td>IBRFIHLI</td>
<td>Incoming HL7 messages</td>
</tr>
<tr class="even">
<td>IBRFIHLU</td>
<td>HL7 Utilities</td>
</tr>
<tr class="odd">
<td>IBRFIN</td>
<td>RFAI Message Detail Worklist</td>
</tr>
<tr class="even">
<td>IBRFIWL</td>
<td>LIST OF Request For Additional Information (RFAI) SCREEN</td>
</tr>
<tr class="odd">
<td>IBRFIWL1</td>
<td>RFAI Message Detail Worklist</td>
</tr>
<tr class="even">
<td>IBRFIWLA</td>
<td>LIST OF Request For Additional Information (RFAI) SCREEN</td>
</tr>
<tr class="odd">
<td>IBRFN, IBRFN1, IBRFN2</td>
<td>Routine contains supported calls for Accounts Receivable</td>
</tr>
<tr class="even">
<td>IBRFN3</td>
<td>Passes bill / claims info to Accounts Receivable</td>
</tr>
<tr class="odd">
<td>IBRFN4</td>
<td>Contains utility calls for IB / AR Extract</td>
</tr>
<tr class="even">
<td>IBRREL</td>
<td>Release Means Test charges placed on hold</td>
</tr>
<tr class="odd">
<td>IBRSUTL</td>
<td>ASCD INTERFACE UTILITIES</td>
</tr>
<tr class="even">
<td>IBRUTL</td>
<td>Utilities for the IB / Accounts Receivable interface</td>
</tr>
<tr class="odd">
<td>IBRXUTL</td>
<td>PHARMACY API CALLS</td>
</tr>
<tr class="even">
<td>IBRXUTL1</td>
<td>BP / BDM - PHARMACY API CALLS</td>
</tr>
<tr class="odd">
<td>IBSDU</td>
<td>ACRP API UTILITIES</td>
</tr>
<tr class="even">
<td>IBTASFAC</td>
<td>Facilities RPC, used by the TAS application</td>
</tr>
<tr class="odd">
<td>IBTASHLT</td>
<td>HEALTH CHECK RPC</td>
</tr>
<tr class="even">
<td>IBTOAT, IBTOAT1, IBTOAT2</td>
<td>These routines print the Admission Sheet.</td>
</tr>
<tr class="odd">
<td>IBTOBI, IBTOBI1, IBTOBI2, IBTOBI3, IBTOBI4</td>
<td>These routines print the Claims Tracking summary for billing.</td>
</tr>
<tr class="even">
<td>IBTODD, IBTODD1</td>
<td>These routines print the Days Denied Report for Claims Tracking.</td>
</tr>
<tr class="odd">
<td>IBTODD2</td>
<td>CLAIMS TRACKING DENIED DAYS REPORT</td>
</tr>
<tr class="even">
<td>IBTOECT</td>
<td>ENHANCED CLAIMS TRACKING REPORTS</td>
</tr>
<tr class="odd">
<td>IBTOLR</td>
<td>This routine prints the list of cases in Claims Tracking requiring Random Sample.</td>
</tr>
<tr class="even">
<td>IBTONB</td>
<td>This routine prints unbilled care that is billable in Claims Tracking.</td>
</tr>
<tr class="odd">
<td>IBTOPW</td>
<td>This routine prints the Pending Reviews Report.</td>
</tr>
<tr class="even">
<td>IBTOSA</td>
<td>This routine prints the Scheduled Admissions with Insurance Report.</td>
</tr>
<tr class="odd">
<td>IBTOSUM, IBTOSUM1, IBTOSUM2</td>
<td>These routines print the MCCR / UR Summary Report.</td>
</tr>
<tr class="even">
<td>IBTOTR</td>
<td>This routine prints the Claims Tracking Inquiry.</td>
</tr>
<tr class="odd">
<td>IBTOUA</td>
<td>This routine prints the Unscheduled Admissions with Insurance Report.</td>
</tr>
<tr class="even">
<td>IBTOUR, IBTOUR1, IBTOUR2, IBTOUR3, IBTOUR4, IBTOUR5</td>
<td>These routines print the Claims Tracking UR Activity Report.</td>
</tr>
<tr class="odd">
<td>IBTOVS</td>
<td>This routine prints a list of billable visits from Claims Tracking by visit type.</td>
</tr>
<tr class="even">
<td>IBTRC, IBTRC1, IBTRC2, IBTRC3, IBTRC4</td>
<td>These routines display the list of Insurance Reviews for a visit and allow for editing of the data on one or more reviews, as well as adding or deleting reviews.</td>
</tr>
<tr class="odd">
<td>IBTRCD, IBTRCD0, IBTRCD1</td>
<td>These routines create the expanded display of a single Insurance Review and allow for editing of the review.</td>
</tr>
<tr class="even">
<td>IBTRD, IBTRD1</td>
<td>These routines display the list of denials and appeals and allow for adding, editing, and deleting of the data on one or more of the listed items.</td>
</tr>
<tr class="odd">
<td>IBTRDD, IBTRDD1</td>
<td>These routines create the expanded display of a single denial or appeal and for editing of the entry.</td>
</tr>
<tr class="even">
<td>IBTRE, IBTRE0, IBTRE1, IBTRE2, IBTRE20, IBTRE3</td>
<td>These routines display the list of Claims Tracking entries (inpatient visits, outpatient visits, prescription refills) for a patient, and allow for adding, editing, and deleting of visits on the list.</td>
</tr>
<tr class="odd">
<td>IBTRE4</td>
<td>This routine allows for editing of inpatient procedures in Claims Tracking.</td>
</tr>
<tr class="even">
<td>IBTRE5</td>
<td>This routine allows for the editing of inpatient providers in Claims Tracking.</td>
</tr>
<tr class="odd">
<td>IBTRE6</td>
<td>This routine allows for the editing of inpatient procedures in Claims Tracking.</td>
</tr>
<tr class="even">
<td>IBTRED, IBTRED0, IBTRED01, BTRED1, IBTRED2</td>
<td>These routines create the expanded display of a single entry in Claims Tracking and editing on the displayed data.</td>
</tr>
<tr class="odd">
<td>IBTRH1</td>
<td>Contains the main Entry Points for the HCSR Worklist.</td>
</tr>
<tr class="even">
<td>IBTRH1A</td>
<td>Contains Entry Points and Functions used in filtering / displaying the HCSR Worklist.</td>
</tr>
<tr class="odd">
<td>IBTRH1B</td>
<td>Contains Entry Points and Functions used in filtering / displaying the HCSR Worklist.</td>
</tr>
<tr class="even">
<td>IBTRH2</td>
<td>HCSR Worklist Expand Entry</td>
</tr>
<tr class="odd">
<td>IBTRH2A</td>
<td>HCSR Worklist Expand Entry continued</td>
</tr>
<tr class="even">
<td>IBTRH2B</td>
<td>HCSR Worklist Expand Entry - Send</td>
</tr>
<tr class="odd">
<td>IBTRH3</td>
<td>IBT HCSR Response View</td>
</tr>
<tr class="even">
<td>IBTRH3A</td>
<td>IBT HCSR Response View – Display set up</td>
</tr>
<tr class="odd">
<td>IBTRH3B</td>
<td>IBT HCSR Response View – Display set up</td>
</tr>
<tr class="even">
<td>IBTRH5</td>
<td>HCSR Response Worklist</td>
</tr>
<tr class="odd">
<td>IBTRH5A</td>
<td>HCSR Create 278 Request</td>
</tr>
<tr class="even">
<td>IBTRH5B</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="odd">
<td>IBTRH5C</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="even">
<td>IBTRH5D</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="odd">
<td>IBTRH5E</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="even">
<td>IBTRH5F</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="odd">
<td>IBTRH5G</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="even">
<td>IBTRH5H</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="odd">
<td>IBTRH5I</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="even">
<td>IBTRH5J</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="odd">
<td>IBTRH5K</td>
<td>Contains Entry Points and Functions used in creating a 278 request from a selected entry in the HCSR Response Worklist.</td>
</tr>
<tr class="even">
<td>IBTRH6</td>
<td>HCSR Send 278 Short Worklist</td>
</tr>
<tr class="odd">
<td>IBTRH7</td>
<td>Entry Point for IBT HCSR MANUAL 278 ADD Protocol</td>
</tr>
<tr class="even">
<td>IBTRH8</td>
<td>Entry Point to display X12 278 message in X12 format.</td>
</tr>
<tr class="odd">
<td>IBTRH8A</td>
<td>Additional routine to display X12 278 message in X12 format</td>
</tr>
<tr class="even">
<td>IBTRHDE</td>
<td>HCSR Patient Events Search</td>
</tr>
<tr class="odd">
<td>IBTRHDE1</td>
<td>HCSR Auto Trigger of 278X215 Inquiry</td>
</tr>
<tr class="even">
<td>IBTRHLI</td>
<td>Receive and store 278 Response message</td>
</tr>
<tr class="odd">
<td>IBTRHLI1</td>
<td>Receive and store 278 Response message</td>
</tr>
<tr class="even">
<td>IBTRHLI2</td>
<td>Receive and store 278 Response message</td>
</tr>
<tr class="odd">
<td>IBTRHLI3</td>
<td>Receive and store 278 Response message</td>
</tr>
<tr class="even">
<td>IBTRHLO</td>
<td>Create and send 278 Inquiry</td>
</tr>
<tr class="odd">
<td>IBTRHLO1</td>
<td>Create and send 278 Inquiry cont.</td>
</tr>
<tr class="even">
<td>IBTRHLO2</td>
<td>Create and send 278 Inquiry cont.</td>
</tr>
<tr class="odd">
<td>IBTRHLU</td>
<td>Utilities used to receive and store 278 Response message</td>
</tr>
<tr class="even">
<td>IBTRHRC</td>
<td>CLAIMS TRACKING 278 CERTIFICATION REPORT</td>
</tr>
<tr class="odd">
<td>IBTRHRD</td>
<td>CLAIMS TRACKING 278 DELETION DISPOSITION REPORT</td>
</tr>
<tr class="even">
<td>IBTRHRS</td>
<td>CLAIMS TRACKING 278 STATISTICAL VOLUME REPORT</td>
</tr>
<tr class="odd">
<td>IBTRKR</td>
<td>Invoked by the inpatient event driver and automatically creates an inpatient Claims Tracking entry for specific admissions.</td>
</tr>
<tr class="even">
<td>IBTRKR0</td>
<td>CLAIMS TRACKING - RANDOM SELECTION BULLETIN</td>
</tr>
<tr class="odd">
<td>IBTRKR1</td>
<td>The random sample generator for determining which admissions will be part of the QM mandated random sample.</td>
</tr>
<tr class="even">
<td>IBTRKR2</td>
<td>This routine is invoked by the nightly background job and adds scheduled admissions to Claims Tracking.</td>
</tr>
<tr class="odd">
<td>IBTRKR3, IBTRKR31</td>
<td>Adds prescription refill information to Claims Tracking.</td>
</tr>
<tr class="even">
<td>IBTRKR4, IBTRKR41</td>
<td>Add outpatient encounters to Claims Tracking.</td>
</tr>
<tr class="odd">
<td>IBTRKR5</td>
<td>This routine adds prosthetics to Claims Tracking.</td>
</tr>
<tr class="even">
<td>IBTRKRBA</td>
<td>Claims tracking - random selection bulletin</td>
</tr>
<tr class="odd">
<td>IBTRKRBD</td>
<td>Claims tracking - deleted admission bulletin</td>
</tr>
<tr class="even">
<td>IBTRKRBR</td>
<td>Claims tracking - relinker bulletin</td>
</tr>
<tr class="odd">
<td>IBTRKRU</td>
<td>Claims tracking file utilities</td>
</tr>
<tr class="even">
<td>IBTRP</td>
<td>Displays and allows editing of Claims Tracking parameters.</td>
</tr>
<tr class="odd">
<td>IBTRPR, IBTRPR0, IBTRPR01, IBTRPR1, IBTRPR2</td>
<td>These routines display pending hospital insurance reviews and perform necessary actions on these reviews.</td>
</tr>
<tr class="even">
<td>IBTRR</td>
<td>ROI consent records display and editing in Claims Tracking</td>
</tr>
<tr class="odd">
<td>IBTRR1</td>
<td>ROI consent records display and editing in Claims Tracking</td>
</tr>
<tr class="even">
<td>IBTRV, IBTRV1, IBTRV2, IBTRV3, IBTRV31</td>
<td>These routines display the list of hospital reviews for a visit and allow for adding, editing, and deleting of the entries listed.</td>
</tr>
<tr class="odd">
<td>IBTRVD, IBTRVD0, IBTRVD1</td>
<td>These routines create the expanded display of a single hospital review and allow editing of the displayed data.</td>
</tr>
<tr class="even">
<td>IBTUB</td>
<td>UNBILLED AMOUNTS MENU</td>
</tr>
<tr class="odd">
<td>IBTUBAV</td>
<td>UNBILLED AMOUNTS - AVERAGE BILL AMOUNT LOGIC</td>
</tr>
<tr class="even">
<td>IBTUBAV1</td>
<td>UNBILLED AMOUNTS - AVERAGE BILL AMOUNT LOGIC</td>
</tr>
<tr class="odd">
<td>IBTUBO</td>
<td>UNBILLED AMOUNTS - GENERATE UNBILLED REPORTS</td>
</tr>
<tr class="even">
<td>IBTUBO1</td>
<td>UNBILLED AMOUNTS - GENERATE UNBILLED REPORTS</td>
</tr>
<tr class="odd">
<td>IBTUBO2</td>
<td>UNBILLED AMOUNTS - GENERATE UNBILLED REPORTS</td>
</tr>
<tr class="even">
<td>IBTUBO3</td>
<td>UNBILLED AMOUNTS - GENERATE UNBILLED REPORTS</td>
</tr>
<tr class="odd">
<td>IBTUBOA</td>
<td>UNBILLED AMOUNTS - GENERATE UNBILLED REPORTS</td>
</tr>
<tr class="even">
<td>IBTUBOU</td>
<td>UNBILLED AMOUNTS (UTILITIES)</td>
</tr>
<tr class="odd">
<td>IBTUBUL</td>
<td>UNBILLED AMOUNTS</td>
</tr>
<tr class="even">
<td>IBTUBV</td>
<td>UNBILLED AMOUNTS - VIEW UNBILLED DATA</td>
</tr>
<tr class="odd">
<td>IBTUTL, IBTUTL1, IBTUTL2, IBTUTL3, IBTUTL4, IBTUTL5</td>
<td>These utility routines perform the creation of new entries in Claims Tracking, insurance reviews, and hospital reviews.</td>
</tr>
<tr class="even">
<td>IBVCB, IBVCB1, IBVCB2</td>
<td>View Cancelled Bill Report</td>
</tr>
<tr class="odd">
<td>IBUCMM,IBUCMM1</td>
<td>Urgent Care Visit Summary / Detail Report</td>
</tr>
<tr class="even">
<td>IBUCSP,IBUCSP1</td>
<td>Urgent Care Visit Tracking Inquiry Report</td>
</tr>
<tr class="odd">
<td>IBUCMM</td>
<td>Urgent Care Visit Maintenance Utility</td>
</tr>
<tr class="even">
<td>IBX*</td>
<td>Generated or Compiled Routines for XREFS, PRINT TEMPLATES, INPUT TEMPLATES</td>
</tr>
<tr class="odd">
<td>IBY*EN</td>
<td>ENVIRONMENT CHECKS FOR IB PATCH</td>
</tr>
<tr class="even">
<td>IBY*PO</td>
<td>POST-INSTALLATION FOR IB PATCH</td>
</tr>
<tr class="odd">
<td>IBY*PR</td>
<td>PRE- INSTALLATION FOR IB PATCH</td>
</tr>
</tbody>
</table>

<span id="_Toc127633850" class="anchor"></span>Table : DGCR Routines

## DGCR\* to IB\* Namespace Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of DGCR routines that changed to the IB namespace in this version.

| DGCR Name | IB Name  | DGCR Name | IB Name |
|-----------|----------|-----------|---------|
| DGCRA     | IBCA     | DGCRP0    | IBCF10  |
| DGCRA0    | IBCA0    | DGCRP1    | IBCF11  |
| DGCRA1    | IBCA1    | DGCRP2    | IBCF12  |
| DGCRA2    | IBCA2    | DGCRP4    | IBCF14  |
| DGCRA3    | IBCA3    | DGCRPAR   | IBEPAR  |
| DGCRA31   | IBOA31   | DGCRPAR1  | IBEPAR1 |
| DGCRA32   | IBOA32   | DGCRSC1   | IBCSC1  |
| DGCRAMS1  | IBOAMS   | DGCRSC2   | IBCSC2  |
| DGCRAMS2  | OBSOLETE | DGCRSC3   | IBCSC3  |
| DGCRB     | IBCB     | DGCRSC4   | IBCSC4  |
| DGCRB1    | IBCB1    | DGCRSC4A  | IBCSC4A |
| DGCRB2    | IBCB2    | DGCRSC4B  | IBCSC4B |
| DGCRBB    | IBCBB    | DGCRSC4C  | IBCSC4C |
| DGCRBB1   | IBCBB1   | DGCRSC5   | IBCSC5  |
| DGCRBB2   | IBCBB2   | DGCRSC6   | IBCSC6  |
| DGCRBR    | IBCBR    | DGCRSC61  | IBCSC61 |
| DGCRBULL  | IBCBULL  | DGCRSC7   | IBCSC7  |
| DGCRC     | IBCC     | DGCRSC8   | IBCSC8  |
| DGCRCC    | IBCCC    | DGCRSC8H  | IBCSC8H |
| DGCRCC1   | IBCCC1   | DGCRSCE   | IBCSCE  |
| DGCRCC2   | IBCCC2   | DGCRSCE1  | IBCSCE1 |
| DGCRCPT   | IBCCPT   | DGCRSCH   | IBCSCH  |
| DGCRMENU  | IBCMENU  | DGCRSCH1  | IBCSCH1 |
| DGCRNQ    | IBCNQ    | DGCRSCP   | IBCSCP  |
| DGCRNQ1   | IBCNQ1   | DGCRSCU   | IBCSCU  |
| DGCROBL   | IBOBL    | DGCRTN    | IBCRTN  |
| DGCROMBL  | IBOMBL   | DGCRTP    | IBCF1TP |
| DGCRONS1  | IBCONS1  | DGCRU     | IBCU    |
| DGCRONS2  | IBCONS2  | DGCRU1    | IBCU1   |
| DGCRONSC  | IBCONSC  | DGCRU2    | IBCU2   |
| DGCROPV   | IBCOPV   | DGCRU3    | IBCU3   |
| DGCROPV1  | IBCOPV1  | DGCRU4    | IBCU4   |
| DGCROPV2  | IBCOPV2  | DGCRU5    | IBCU5   |
| DGCRORT   | IBORT    | DGCRU6    | IBCU6   |
| DGCRORT1  | IBORT1   | DGCRU61   | IBCU61  |
| DGCROST   | IBOSTUS  | DGCRU62   | IBCU62  |
| DGCROST1  | IBOSTUS1 | DGCRU63   | IBCU63  |
| DGCROTR   | IBOTR    | DGCRU7    | IBCU7   |
| DGCROTR1  | IBOTR1   | DGCRU71   | IBCU71  |
| DGCROTR2  | IBOTR2   | DGCRVA    | IBCVA   |
| DGCROTR3  | IBOTR3   | DGCRVA0   | IBCVA0  |
| DGCROTR4  | IBOTR4   | DGCRVA1   | IBCVA1  |
| DGCRP     | IBCF1    |           |         |

<span id="_Toc127633851" class="anchor"></span>Table : File List

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per VHA Directive 10-93-142 regarding security of software that affects financial systems, most of the IB Data Dictionaries may not be modified. The file descriptions of these files will be so noted. The files that may be modified are Encounter Form files \#357 through \#358.91.

VA Directive 6402 (Aug 28, 2013) is a more recent directive than VHA Directive 10-93-142 and rescinds VHA 2004-038, Modifications to VHA Modifications to Class I Software dated July 23, 2004. Per VA Directive 6402, regarding security of software that affects financial systems, most of the IB Data Dictionaries may not be modified. The file descriptions of these files should be updated over time to reflect the current directive.

## Globals to Journal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB, IBA, IBAM, IBE, and IBT globals must be journaled. In a future release, we intend to move all dynamic files from IBE to IBA so that it will not be necessary to journal IBE. Journaling of the IBAT global is optional.

## File List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633852" class="anchor"></span>Table : Templates List</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>File # / File Name</th>
<th>Global / File Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>36</p>
<p>INSURANCE COMPANY</p></td>
<td><p>^DIC(36,</p>
<p>This file contains the names and addresses of insurance companies as needed by the local facility. <strong>The data in this file is not editable using VA File Manager.</strong></p></td>
</tr>
<tr class="even">
<td>335.93 IB NON/OTHER VA BILLING PROVIDER FILE</td>
<td><p>^IBA(355.93,</p>
<p>This file contains data for non-VA facilities that provide services for VA patients who have reimbursable insurance for these services. VA pays for the services and in turn submits the charges to the insurance company for reimbursement.</p></td>
</tr>
<tr class="odd">
<td><p>350</p>
<p>INTEGRATED BILLING ACTION</p></td>
<td><p>^IB(350,</p>
<p>Entries in this file are created by other applications calling approved interface routines.</p></td>
</tr>
<tr class="even">
<td><p>350.1</p>
<p>IB ACTION TYPE</p></td>
<td><p>^IBE(350.1,</p>
<p>This file contains the types of actions that a service can use with Integrated Billing and the related logic to tell IB how this entry is to be processed.</p></td>
</tr>
<tr class="odd">
<td><p>350.2</p>
<p>IB ACTION CHARGE</p></td>
<td><p>^IBE(350.2,</p>
<p>This file contains the charge information for an IB ACTION TYPE by effective date of the charge.</p></td>
</tr>
<tr class="even">
<td><p>350.21</p>
<p>IB ACTION STATUS</p></td>
<td><p>^IBE(350.21,</p>
<p>The file holds new statuses that are introduced in v2.0, display and abbreviated names for the statuses, and classification-type fields for each status that are used for processing in the Integrated Billing module.</p></td>
</tr>
<tr class="odd">
<td><p>350.3</p>
<p>IB CHARGE REMOVAL REASONS</p></td>
<td><p>^IBE(350.3,</p>
<p>Data in this file comes pre-loaded with reasons why a charge may be cancelled or removed. <strong>Sites are asked not to edit or add entries to this file.</strong></p></td>
</tr>
<tr class="even">
<td><p>350.4</p>
<p>BILLABLE AMBULATORY SURGICAL CODES</p></td>
<td><p>^IBE(350.4,</p>
<p>This file contains the CPT procedure and the associated HCFA rate groups for ambulatory surgeries that may be billed.</p></td>
</tr>
<tr class="odd">
<td><p>350.41</p>
<p>UPDATE BILLABLE AMBULATORY SURGICAL CODE</p></td>
<td><p>^IBE(350.41,</p>
<p>This file contains updates to the ambulatory surgery procedures that can be billed.</p></td>
</tr>
<tr class="even">
<td><p>350.5</p>
<p>BASC LOCALITY MODIFIER</p></td>
<td><p>^IBE(350.5,</p>
<p>This file is used in the calculation of the charge for an ambulatory surgery performed on any given date.</p></td>
</tr>
<tr class="odd">
<td><p>350.6</p>
<p>IB ARCHIVE/PURGE LOG</p></td>
<td><p>^IBE(350.6,</p>
<p>This file is used to track the archiving and purging operations of the following files used in Integrated Billing List Archive/Purge Log entries: INTEGRATED BILLING ACTION file (#350), CATEGORY C BILLING CLOCK file (#351), and BILL/CLAIMS file (#399).</p></td>
</tr>
<tr class="even">
<td><p>350.7</p>
<p>AMBULATORY CHECK-OFF SHEET</p></td>
<td><p>^IBE(350.7,</p>
<p>This file defines the Ambulatory Surgery Check-off Sheets used by outpatient clinics. It contains the CPT print format to be used on the Ambulatory Surgeries Check-off List.</p></td>
</tr>
<tr class="odd">
<td><p>350.71</p>
<p>AMBULATORY SURGERY CHECK-OFF SHEET PRINT FIELDS</p></td>
<td><p>^IBE(350.71,</p>
<p>This file contains the sub-headers and procedures associated with each check-off sheet defined for the CPT clinic list.</p></td>
</tr>
<tr class="even">
<td><p>350.8*</p>
<p>IB ERROR</p></td>
<td><p>^IBE(350.8,</p>
<p>If a potential error is detected during a billing process, the full text description of the error will be reported from this file.</p></td>
</tr>
<tr class="odd">
<td><p>350.9</p>
<p>IB SITE PARAMETERS</p></td>
<td><p>^IBE(350.9,</p>
<p>This file contains the necessary site-specific data to run and manage the Integrated Billing package and the IB Background Filer. Only one entry per facility is allowed.</p></td>
</tr>
<tr class="even">
<td><p>351</p>
<p>CATEGORY C BILLING CLOCK</p></td>
<td><p>^IBE(351,</p>
<p>This file is used to create and maintain billing clocks in which Category C patients may be charged for co-payment and per diem charges for hospital or nursing home care, as well as outpatient visits. It will initially be populated by the Means Test data conversion and subsequently created and updated by Integrated Billing. Entries in this file should not be deleted or edited through VA FileMan.</p></td>
</tr>
<tr class="odd">
<td><p>351.1</p>
<p>IB CONTINUOUS PATIENT</p></td>
<td><p>^IBE(351.1,</p>
<p>This file contains a list of all hospital or nursing home care patients receiving continuous institutional care from prior to 7/1/86 who may be subject to Category C billing.</p></td>
</tr>
<tr class="even">
<td><p>351.2</p>
<p>SPECIAL INPATIENT BILLING CASES</p></td>
<td><p>^IBE(351.2,</p>
<p>This file is used to track inpatient episodes for Category C veterans who have claimed exposure to Agent Orange, Ionizing Radiation, and Environmental Contaminants.</p></td>
</tr>
<tr class="odd">
<td><p>351.5</p>
<p>TRICARE PHARMACY TRANSACTIONS</p></td>
<td><p>^IBA(351.5,</p>
<p>This file is used to store data related to each Pharmacy billing transaction with the Tricare fiscal intermediary. Each transaction is submitted to the RNA/Triad Pharmacy ClaimGuard System, which is a commercial point of sale pharmacy billing software package, where it is forwarded to the intermediary through an electronic switch company. All of the information that is returned from the intermediary is stored in this file.</p></td>
</tr>
<tr class="even">
<td><p>351.51</p>
<p>TRICARE PHARMACY ERRORS</p></td>
<td><p>^IBE(351.51,</p>
<p>This table file is used to store the various errors that may occur when TRICARE prescriptions are billed using the commercial point-of-sale pharmacy billing software package.</p></td>
</tr>
<tr class="odd">
<td><p>351.52</p>
<p>TRICARE PHARMACY REJECTS</p></td>
<td><p>^IBA(351.52,</p>
<p>This file is used to store all the reasons that were used by the Tricare fiscal intermediary to reject a pharmacy billing transaction. Entries in this file are automatically deleted if a prescription is re-submitted a subsequently accepted. The option Delete Reject Entry [IB TRICARE DEL REJECT] may be used to delete entries from this file.</p></td>
</tr>
<tr class="even">
<td><p>351.53</p>
<p>PRODUCT SELECTION REASON</p></td>
<td>^IBA(351.53,</td>
</tr>
<tr class="odd">
<td><p>351.6</p>
<p>TRANSFER PRICING PATIENT</p></td>
<td><p>^IBAT(351.6,</p>
<p>This file is used to store Transfer Pricing patient specific information.</p></td>
</tr>
<tr class="even">
<td><p>351.61</p>
<p>TRANSFER PRICING TRANSACTIONS</p></td>
<td><p>^IBAT(351.61,</p>
<p>This file holds all transfer pricing transactions.</p></td>
</tr>
<tr class="odd">
<td><p>351.62</p>
<p>TRANSFER PRICING FIELD DEFINITION</p></td>
<td><p>^IBAT(351.62,</p>
<p>This file comes populated with national entries. These entries should never be deleted or edited. It is not recommended that facilities add entries to this file. The entries are used to extract and format data for all the transfer pricing reports. <strong>DO NOT delete entries in this file. DO NOT edit data in this file with VA File Manager.</strong></p></td>
</tr>
<tr class="even">
<td><p>351.67</p>
<p>TRANSFER PRICING INPT PROSTHETIC ITEMS</p></td>
<td><p>^IBAT(351.67,</p>
<p>This file stores the prosthetic devices that should be automatically billed for inpatient devices issued. Unless a device is in this file, it will only be billed for outpatient services (automatically).</p></td>
</tr>
<tr class="odd">
<td><p>351.7</p>
<p>IB DM EXTRACT REPORTS</p></td>
<td><p>^IBE(351.7,</p>
<p>This file contains the necessary DM reports that will have summary data collected via the Diagnostic Measures Extraction process.</p></td>
</tr>
<tr class="even">
<td><p>351.701</p>
<p>IB DM EXTRACT DATA ELEMENTS</p></td>
<td><p>^IBE(351.701,</p>
<p>This file contains various report data elements / line items. One or more of these file entries is related to a corresponding entry in the IB DM EXTRACT REPORTS file (#351.7).</p></td>
</tr>
<tr class="odd">
<td><p>351.71</p>
<p>IB DM EXTRACT DATA</p></td>
<td><p>^IBE(351.71,</p>
<p>This file contains data collected via the Diagnostic Measures Extraction process. Within each entry is a series of DM reports from which summary data has been collected on a monthly basis.</p></td>
</tr>
<tr class="even">
<td><p>351.73</p>
<p>IB DM WORKLOAD PARAMETERS</p></td>
<td><p>^IBE(351.73,</p>
<p>This file contains Input parameters used to produce AR Workload To-Do Lists. It also contains the flag that determines if a clerk is to ONLY be included on productivity reports. The Workload To-Do lists are mailman messages sent to the supervisors and clerks. The Productivity reports are sent to a printer.</p></td>
</tr>
<tr class="odd">
<td><p>351.81</p>
<p>LTC CO-PAY CLOCK</p></td>
<td><p>^IBA(351.81,</p>
<p><strong>DO NOT delete entries in this file. DO NOT edit data in this file with VA File Manager.</strong></p>
<p>Entries in this file will be added and updated my menu options, event triggers, and a nightly background job. Entries in this file will not be deleted.</p>
<p>This file stores Long Term Care billing information that is used to make a billing determination for LTC rates.</p></td>
</tr>
<tr class="even">
<td><p>351.82</p>
<p>IB UC VISIT TRACKING FILE</p></td>
<td><p>^IBUC(351.82,</p>
<p><strong>DO NOT delete entries in this file. DO NOT edit data in this file with VA File Manager.</strong></p>
<p>Entries in this file will be added and updated by menu options and a nightly background job. Entries in this file will not be deleted.</p>
<p>This file stores Community Care Urgent Care Visit information that is used to determine what copay, if any, a veteran must pay for an Urgent Care visit within the community.</p></td>
</tr>
<tr class="odd">
<td><p>351.9</p>
<p>CLAIMSMANAGER BILLS</p></td>
<td><p>^IBA(351.9,</p>
<p>This file contains information on bills that have been sent to the Ingenix ClaimsManager.</p>
<p>The entries in this file have matching entries in the BILL/CLAIMS file (399). The internal number in file 399 is the same as the internal number in the CLAIMSMANAGER BILLS file.</p></td>
</tr>
<tr class="even">
<td><p>351.91</p>
<p>CLAIMSMANAGER STATUS</p></td>
<td><p>^IBA(351.91,</p>
<p>This file contains the status entries that are utilized by the ClaimsManager interface.</p></td>
</tr>
<tr class="odd">
<td><p>352.1</p>
<p>BILLABLE APPOINTMENT TYPE</p></td>
<td><p>^IBE(352.1,</p>
<p>This is a time-sensitive file that maintains records for each appointment type with indicators for IGNORE MEANS TEST, PRINT ON INSURANCE REPORT, and DISPLAY ON INPUT SCREEN.</p></td>
</tr>
<tr class="even">
<td><p>352.2</p>
<p>NON-BILLABLE DISPOSITIONS</p></td>
<td><p>^IBE(352.2,</p>
<p>This file is used to flag dispositions in the DISPOSITION file (#37) as either billable or non-billable for Means Test billing.</p></td>
</tr>
<tr class="odd">
<td><p>352.3</p>
<p>NON-BILLABLE CLINIC STOP CODES</p></td>
<td><p>^IBE(352.3,</p>
<p>This file is used to flag clinic stop codes in the CLINIC STOP file (#40.7) as either billable or non-billable for Means Test billing.</p></td>
</tr>
<tr class="even">
<td><p>352.4</p>
<p>NON-BILLABLE CLINICS</p></td>
<td><p>^IBE(352.4,</p>
<p>This file is used to flag clinics in the HOSPITAL LOCATION file (#44) as either billable or non-billable for Means Test billing.</p></td>
</tr>
<tr class="odd">
<td><p>352.5</p>
<p>IB CLINIC STOP CODE BILLABLE TYPES</p></td>
<td><p>^IBE(352.5,</p>
<p>This file is used to store the outpatient clinic stop code and billable type based on an effective date. An internal lookup on the AEFFDT cross reference for a clinic stop code and visit date will provide the billable type. The billable type determines the billable rate for each outpatient visit.</p></td>
</tr>
<tr class="even">
<td><p>353</p>
<p>BILL FORM TYPE</p></td>
<td><p>^IBE(353,</p>
<p>This is a reference file containing the types of health insurance claim forms used in billing. Sites may add local forms to this file; however, the internal entry number for locally added forms should be in the stations number range of station number times 1000.</p></td>
</tr>
<tr class="odd">
<td><p>353.1*</p>
<p>PLACE OF SERVICE</p></td>
<td><p>^IBE(353.1,</p>
<p>This file contains the Place of Service codes that may be associated with a procedure on the HCFA-1500. These codes were developed specifically for the HCFA-1500 and should not be changed by the site.</p></td>
</tr>
<tr class="even">
<td><p>353.2*</p>
<p>TYPE OF SERVICE</p></td>
<td><p>^IBE(353.2,</p>
<p>This file contains the Type of Service codes that may be associated with a procedure on the HCFA-1500. These codes were developed specifically for the HCFA-1500 and should not be changed by the site.</p></td>
</tr>
<tr class="odd">
<td><p>353.3</p>
<p>IB ATTACHMENT REPORT TYPE</p></td>
<td><p>^IBE(353.3,</p>
<p>This file contains entries that describe the type of supplemental information available to support a claim for reimbursement for health care services. Attachment Report Type Code is at both the claim level and line level.</p></td>
</tr>
<tr class="even">
<td><p>353.4</p>
<p>TRANSPORT REASON CODE</p></td>
<td><p>^IBE(353.4,</p>
<p>This file contains Ambulance Transport Reason Codes and Ambulance Transport Reasons used to identify why ambulance transportation was required. This file comes pre-populated and should not be edited.</p></td>
</tr>
<tr class="odd">
<td><p>353.5</p>
<p>AMBULANCE CONDITION INDICATORS</p></td>
<td><p>^IBE(353.5,</p>
<p>This file contains patient conditions in relation (pickup, during, and drop-off) to ambulance transportation. This file comes pre-populated and should not be edited.</p></td>
</tr>
<tr class="even">
<td><p>354</p>
<p>BILLING PATIENT</p></td>
<td><p>^IBA(354,</p>
<p>Do not edit this file. Under normal operation, it is not necessary to edit the fields in this file directly. The option Manual Change Co-pay Exemption (Hardships) can be used to update and correct this entry by creating a new exemption. If many patient records have problems, the option Print/Verify Patient Exemption Status can be used to correct the entries. The data in this file is updated each time a new (current) exemption is created for a patient. Exemptions are automatically created when changes in patient information change the exemption status or when an expired (older than one year) exemption is encountered when determining the exemption status for Pharmacy. This file will contain specific information related to billing about individual patients. Current status of the Medication Co-payment Exemption will be kept in this file. Conceptually, this is different than the BILLING EXEMPTIONS file (#354.1), which maintains the audit log and historical data related to billing exemptions.</p></td>
</tr>
<tr class="odd">
<td><p>354.1</p>
<p>BILLING EXEMPTIONS</p></td>
<td><p>^IBA(354.1,</p>
<p>Do not edit this file. Under normal operation, it is not necessary to edit the fields in this file directly. The option Manual Change Co-pay Exemption (Hardships) can be used to update and correct entries by creating a new exemption. If many patient records have problems, the option Print / Verify Patient Exemption Status can be used to correct the entries.</p></td>
</tr>
<tr class="even">
<td><p>354.2</p>
<p>EXEMPTION REASON</p></td>
<td><p>^IBE(354.2,</p>
<p>This file contains the reasons that exemptions can be given with associated status and description.</p></td>
</tr>
<tr class="odd">
<td><p>354.3</p>
<p>BILLING THRESHOLDS</p></td>
<td><p>^IBE(354.3,</p>
<p>This file contains the income threshold amounts used by the Medication Co-payment Exemption process.</p></td>
</tr>
<tr class="even">
<td><p>354.4</p>
<p>BILLING ALERTS</p></td>
<td><p>^IBA(354.4,</p>
<p>This file will only be populated if a site chooses to use the "Alert" functionality available in Kernel v7 instead of receiving mail messages. This is determined by the field USE ALERTS (#.14) in the IB SITE PARAMETERS file (#350.9).</p></td>
</tr>
<tr class="odd">
<td><p>354.5</p>
<p>BILLING ALERT DEFINITION</p></td>
<td><p>^IBE(354.5,</p>
<p>This file contains the necessary information to process electronic notifications sent by the Medication Co-payment Exemption process.</p></td>
</tr>
<tr class="even">
<td><p>354.6</p>
<p>IB FORM LETTER</p></td>
<td><p>^IBE(354.6,</p>
<p>This file contains the header and main body of letters that are generated by the IB package. Each site should edit the header of the letter to reflect its own address. Sites may edit the main body of the letter to change the signer of the letter or add contact persons and phone numbers. The text of the letters has been approved by MCCR VACO.</p></td>
</tr>
<tr class="odd">
<td><p>354.7</p>
<p>IB PATIENT CO-PAY ACCOUNT</p></td>
<td><p>^IBAM(354.7,</p>
<p>This file stores summary information about a patient's co-pay account. The information will be used to determine if a patient has reached his co-pay cap for the month or year.</p></td>
</tr>
<tr class="even">
<td><p>354.71</p>
<p>IB CO-PAY TRANSACTIONS</p></td>
<td><p>^IBAM(354.71,</p>
<p>This file stores individual transactions for outpatient medication co-payments. The transactions in this file will be used to store detailed information about a patient's prescription co-payments, including amounts billed and not billed. There should be transactions stored in this file for both this facility and other treating facilities throughout the VA system.</p></td>
</tr>
<tr class="odd">
<td><p>354.75</p>
<p>IB CO-PAY CAPS</p></td>
<td><p>^IBAM(354.75,</p>
<p>This file comes populated with data. The data in this file should not be edited, added, or deleted locally. The information stored here is the cap amounts for outpatient medication co-payment. Once a patient has reached his cap, billing will stop for the remainder of the period indicated.</p></td>
</tr>
<tr class="even">
<td><p>355.1*</p>
<p>TYPE OF PLAN</p></td>
<td><p>^IBE(355.1,</p>
<p>This file contains the standard types of plans that an insurance company may provide. The type of plan may be dependent on the type of coverage provided by the insurance company and may affect the type of benefits that are available for the plan. The file is capable of being standardized, via the MASTER TYPE OF PLAN field, to provide industry-wide interoperability.</p></td>
</tr>
<tr class="odd">
<td><p>355.12</p>
<p>SOURCE OF INFORMATION</p></td>
<td><p>^IBE(355.12,</p>
<p>This file contains a list of valid Source of Information codes. These codes can be used to track where the insurance information originated from.</p></td>
</tr>
<tr class="even">
<td><p>355.13</p>
<p>INSURANCE FILING TIME FRAME</p></td>
<td><p>^IBE(355.13,</p>
<p>This file contains the list of valid Standard Insurance Filing Time Frames that may be automatically applied. This file comes populated with the standard entries and should not be modified locally.</p></td>
</tr>
<tr class="odd">
<td><p>355.2*</p>
<p>TYPE OF INSURANCE COVERAGE</p></td>
<td><p>^IBE(355.2,</p>
<p>This file contains the types of coverage with which an insurance company is generally associated. If an insurer is identified with more than one type of coverage, it should be identified as HEALTH INSURANCE as this encompasses all.</p></td>
</tr>
<tr class="even">
<td><p>355.3</p>
<p>GROUP INSURANCE PLAN</p></td>
<td><p>^IBA(355.3,</p>
<p>This file contains the relevant data for group insurance plans. The data in this file is specific to the plan itself. This is in contrast to the PATIENT file (#2) that contains data about patients' policies and where the policy may be for a group or health insurance plan.</p></td>
</tr>
<tr class="odd">
<td><p>355.31</p>
<p>PLAN LIMITATION CATEGORY</p></td>
<td><p>^IBE(355.31,</p>
<p>This table file contains elements that can be checked for an insurance company policy to determine if third party billing is valid. For example, the general categories of coverage the policy may exclude.</p></td>
</tr>
<tr class="even">
<td><p>355.32</p>
<p>PLAN COVERAGE LIMITATIONS</p></td>
<td><p>^IBA(355.32,</p>
<p>This file contains the detail by plan and effective date of the categories that may be restricted for insurance coverage.</p></td>
</tr>
<tr class="odd">
<td><p>355.33</p>
<p>INSURANCE VERIFICATION PROCESSOR</p></td>
<td><p>^IBA(355.33,</p>
<p>This file contains insurance information accumulated by various sources. The data is held in this file until an authorized person processes the information by either rejecting it or moving it to the Insurance files.</p>
<p>Once an entry is processed, most of the data is deleted leaving a stub entry in this file that can be used for reporting and tracking purposes.</p></td>
</tr>
<tr class="even">
<td><p>355.34</p>
<p>INSURANCE REMOTE QUERY RESULTS</p></td>
<td><p>^IBA(355.34,</p>
<p>This is a log file for the insurance queries that were done during a given month / year. There will be one entry for each month / year with summary results only stored in the file.</p></td>
</tr>
<tr class="odd">
<td><p>355.35</p>
<p>HMS EXTRACT FILE STATUS FILE</p></td>
<td>This file keeps track of the Extract files messages sent to AITC DMI Queue and the confirmation messages that are received from AITC.</td>
</tr>
<tr class="even">
<td><p>355.351</p>
<p>HMS RESULT FILE STATUS FILE</p></td>
<td>This file keeps track of the Result file messages received from AITC.</td>
</tr>
<tr class="odd">
<td><p>355.36</p>
<p>CREATION TO PROCESSING TRACKING</p></td>
<td><p>^IBA(355.36,</p>
<p>This file tracks transactions from creation until final processing. This file tracks insurance records that are processed through the INSURANCE VERIFICATION PROCESSOR (#355.33), in addition to records that are processed by eIV via auto update.</p></td>
</tr>
<tr class="even">
<td><p>355.4</p>
<p>ANNUAL BENEFITS</p></td>
<td><p>^IBA(355.4,</p>
<p>This file contains the fields to maintain the annual benefits by year for an insurance policy.</p></td>
</tr>
<tr class="odd">
<td><p>355.5</p>
<p>INSURANCE CLAIMS YEAR TO DATE</p></td>
<td><p>^IBA(355.5,</p>
<p>This file contains the CLAIM TO DATE information about a patient's health insurance claims to a specific carrier for a specific year. This will allow estimate receivables based on whether claims exceed deductibles or other maximum benefits.</p></td>
</tr>
<tr class="even">
<td><p>355.6</p>
<p>INSURANCE RIDERS</p></td>
<td><p>^IBE(355.6,</p>
<p>This file contains a listing of insurance riders that can be purchased as add-on coverage to a group plan. The software does nothing special with these riders. The listing may be added to locally and be assigned to patients as policy riders. This information is strictly for display and tracking purposes only.</p></td>
</tr>
<tr class="odd">
<td><p>355.7</p>
<p>PERSONAL POLICY</p></td>
<td><p>^IBA(355.7,</p>
<p>This file contains the insurance riders that have been purchased as add-on coverage to a group plan. This information is used internally for display purposes only.</p></td>
</tr>
<tr class="even">
<td><p>355.8</p>
<p>SPONSOR</p></td>
<td><p>^IBA(355.8,</p>
<p>The SPONSOR file contains a list of people who are the sponsors for patients who have Tricare insurance coverage. These people, who are typically active duty personnel or military retirees, are stored as either patients (in file #2) or non-patients in the SPONSOR PERSON (#355.82) file. A variable pointer is used to point to the person in either of those two files.</p>
<p>This file is used as a list of sponsors who may be the sponsor of more than one patient. The SPONSOR RELATIONSHIP (#355.81) file relates a sponsor to a specific patient.</p></td>
</tr>
<tr class="odd">
<td><p>355.81</p>
<p>SPONSOR RELATIONSHIP</p></td>
<td><p>^IBA(355.81,</p>
<p>The Sponsor Relationship file is used to associate a sponsor in file #355.8 with a patient. The attributes associated with that sponsor/patient relationship are stored in this file.</p></td>
</tr>
<tr class="even">
<td><p>355.82</p>
<p>SPONSOR PERSON</p></td>
<td><p>^IBA(355.82,</p>
<p>This file is pointed to by the SPONSOR (#355.8) and contains all sponsors who are not patients. This file contains the non-patient sponsor's name, date of birth, and social security number, all of which are retrieved from the PATIENT (#2) file for sponsors who are patients. Other pertinent sponsor information is stored in the SPONSOR (#355.8) file.</p></td>
</tr>
<tr class="odd">
<td><p>355.9</p>
<p>IB BILLING PRACTITIONER ID</p></td>
<td><p>^IBA(355.9,</p>
<p>This file contains one record for each unique billing provider id number that an individual provider (practitioner) is assigned by an insurance company or by a licensing or government entity. Entries without an insurance company indicate the number is assigned to the practitioner by a licensing or government entity and will apply to all insurance companies.</p></td>
</tr>
<tr class="even">
<td><p>355.91</p>
<p>IB INSURANCE CO LEVEL BILLING PROV ID</p></td>
<td><p>^IBA(355.91,</p>
<p>This file contains one record for each provider id that an insurance company assigns to a facility for ALL billing providers at the facility. Each record can be for an insurance company and any combination of the patient status, form type and care unit. There must be only one record for each combination.</p></td>
</tr>
<tr class="odd">
<td><p>355.92</p>
<p>FACILITY BILLING ID</p></td>
<td><p>^IBA(355.92,</p>
<p>This file contains one record for each facility id that an insurance company assigns to a facility. Each record can be for an insurance company and any combination of the patient status and form type. There must be only one record for each combination.</p></td>
</tr>
<tr class="even">
<td><p>355.93</p>
<p>IB NON/OTHER VA BILLING PROVIDER</p></td>
<td><p>^IBA(355.93,</p>
<p>This file contains data for non-VA facilities that provide services for VA patients who have reimbursable insurance for these services.</p></td>
</tr>
<tr class="odd">
<td><p>355.95</p>
<p>IB PROVIDER ID CARE UNIT</p></td>
<td><p>^IBA(355.95,</p>
<p>This file contains the data values (referred to as care units) to be used to match a provider on a claim to the correct provider id #. The entries in this file are specific to an insurance company.</p></td>
</tr>
<tr class="even">
<td><p>355.96</p>
<p>IB INS CO PROVIDER ID CARE UNIT</p></td>
<td><p>^IBA(355.96,</p>
<p>This file defines the 'list' of care units that an insurance company uses to assign provider ids. Each record must have an insurance company, a provider type, and a care unit entry. The total of all the records in this file for a given insurance company comprises the complete list of care units the insurance company requires the V.A. to use when determining provider ids for any claims sent.</p></td>
</tr>
<tr class="odd">
<td><p>355.97</p>
<p>IB PROVIDER ID # TYPE</p></td>
<td><p>^IBE(355.97,</p>
<p>There can be many kinds of provider id numbers that may need to be reported when billing for hospital and professional services. This file contains entries that will be used to classify or identify the valid kinds of provider ids that the V.A. will use. This is needed specifically for the transmission of bills so the proper interpretation of the ID's can be made electronically.</p></td>
</tr>
<tr class="even">
<td><p>355.98</p>
<p>IB ALTERNATE PRIMARY ID TYPES</p></td>
<td><p>^IBA(355.98,</p>
<p>This file contains the Alternate Primary Payer ID Types, which are used to identify an Alternate Primary Payer ID for a payer to be sent on the outgoing electronic claim (837).</p></td>
</tr>
<tr class="odd">
<td><p>355.99</p>
<p>MASTER TYPE OF PLAN</p></td>
<td><p>^IBEMTOP(355.99,</p>
<p>This file contains coding system and code data used for association to the MASTER TYPE OF PLAN field within the TYPE OF PLAN file #355.1 for the purposes of native standardization between the VA and the users of its data.</p></td>
</tr>
<tr class="even">
<td><p>356</p>
<p>CLAIMS TRACKING</p></td>
<td><p>^IBT(356,</p>
<p>This file may contain entries of all types of billable events that need to be tracked by MCCR. The information in this file is used for MCCR and / or UR purposes. It is information about the event itself not otherwise stored or pertinent for MCCR purposes.</p></td>
</tr>
<tr class="odd">
<td><p>356.001</p>
<p>X12 278 REQUEST CATEGORY</p></td>
<td><p>^IBT(356.001,</p>
<p>This file contains all the corresponding X.12 codes for request categories.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.002</p>
<p>X12 278 CERTIFICATION TYPE CODE</p></td>
<td><p>^IBT(356.002,</p>
<p>This file contains all the corresponding X.12 codes for certification type codes.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.003</p>
<p>X12 278 CURRENT HEALTH CONDITION CODE</p></td>
<td><p>^IBT(356.003,</p>
<p>This file contains all the corresponding X.12 codes for current health condition.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.004</p>
<p>X12 278 PROGNOSIS CODE</p></td>
<td><p>^IBT(356.004,</p>
<p>This file contains all the corresponding X.12 codes for prognosis.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.005</p>
<p>X12 278 DELAY REASON CODE</p></td>
<td><p>^IBT(356.005,</p>
<p>This file contains all the corresponding X.12 codes for delay reasons.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.006</p>
<p>X12 278 DIAGNOSIS TYPE</p></td>
<td><p>^IBT(356.006,</p>
<p>This file contains all the corresponding X.12 codes for diagnosis types.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.007</p>
<p>X12 278 DELIVERY PATTERN TIME CODE</p></td>
<td><p>^IBT(356.007,</p>
<p>This file contains all the corresponding X.12 codes for delivery time pattern.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.008</p>
<p>X12 278 CONDITION CODE</p></td>
<td><p>^IBT(356.008,</p>
<p>This file contains all the corresponding X.12 codes for condition.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.009</p>
<p>X12 278 ADMISSION SOURCE</p></td>
<td><p>^IBT(356.009,</p>
<p>This file contains all the corresponding X.12 codes for admission source.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.01</p>
<p>X12 278 PATIENT STATUS</p></td>
<td><p>^IBT(356.01,</p>
<p>This file contains all the corresponding X.12 codes for patient status.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.011</p>
<p>X12 278 NURSING HOME RESIDENTIAL STATUS</p></td>
<td><p>^IBT(356.011,</p>
<p>This file contains all the corresponding X.12 codes for nursing home residential status.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.012</p>
<p>X12 278 SUBLUXATION LEVEL CODE</p></td>
<td><p>^IBT(356.012,</p>
<p>This file contains all the corresponding X.12 codes for subluxation level.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.013</p>
<p>X12 278 OXYGEN EQUIPMENT TYPE</p></td>
<td><p>^IBT(356.013,</p>
<p>This file contains all the corresponding X.12 codes for oxygen equipment types.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.014</p>
<p>X12 278 OXYGEN TEST CONDITION</p></td>
<td><p>^IBT(356.014,</p>
<p>This file contains all the corresponding X.12 codes for oxygen test conditions.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.015</p>
<p>X12 278 OXYGEN TEST FINDINGS</p></td>
<td><p>^IBT(356.015,</p>
<p>This file contains all the corresponding X.12 codes for oxygen test findings.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.016</p>
<p>X12 278 OXYGEN DELIVERY SYSTEM CODE</p></td>
<td><p>^IBT(356.016,</p>
<p>This file contains all the corresponding X.12 codes for oxygen delivery systems.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.017</p>
<p>X12 278 PATIENT LOCATION</p></td>
<td><p>^IBT(356.017,</p>
<p>This file contains all the corresponding X.12 codes for patient locations.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.018</p>
<p>X12 278 REPORT TYPE CODE</p></td>
<td><p>^IBT(356.018,</p>
<p>This file contains all the corresponding X.12 codes for report types.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.019</p>
<p>X12 278 NURSING HOME LEVEL OF CARE</p></td>
<td><p>^IBT(356.019,</p>
<p>This file contains all the corresponding X.12 codes for nursing home level of care.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td><p>356.02</p>
<p>X12 278 CERTIFICATION ACTION CODES</p></td>
<td><p>^IBT(356.02,</p>
<p>This file contains all of the corresponding X.12 codes for the Certification Action Codes.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>356.021</p>
<p>X12 278 HCS DECISION REASON CODES</p></td>
<td><p>^IBT(356.021,</p>
<p>This file contains all the corresponding X.12 codes for the Health Care Services Decision Reason Codes according to the ASC X12 External Code Source 886.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="even">
<td>356.022 UNIVERSAL DENTAL NUMBERING SYSTEM</td>
<td><p>^IBT(356.022,</p>
<p>This file contains all of the corresponding X.12 Tooth codes - External Code Source 135: American Dental Association.</p>
<p>Per VHA Directive 10-93-142, this file definition should not be modified.</p></td>
</tr>
<tr class="odd">
<td>356.023 HCSR WORKLIST DELETE REASON CODE</td>
<td><p>^IBT(356.023,</p>
<p>This file contains all the Delete Reason Codes that can be added to an HCSR 278 Worklist entry when removing the entry from the worklist.</p></td>
</tr>
<tr class="even">
<td><p>356.1</p>
<p>HOSPITAL REVIEW</p></td>
<td><p>^IBT(356.1,</p>
<p>This file contains Utilization Review information about appropriateness of admission and continued stay in an acute medical setting. It uses the Integral criteria for appropriateness. An entry for each day of care for cases being tracked is required by the QM office in VACO. The information in this file will be rolled up into a national database. Only reviews that have a status of COMPLETE should be rolled up. The information in this file is clinical in nature and should be treated with the same confidentiality as required of all clinical data.</p></td>
</tr>
<tr class="odd">
<td><p>356.11</p>
<p>CLAIMS TRACKING REVIEW TYPE</p></td>
<td><p>^IBE(356.11,</p>
<p>This is the type of review that is being performed by MCCR or UR. This file may contain the logic to determine which questions and / or screens can be presented to the user in the future. <strong>Do not add, edit, or delete entries in this file without instructions from the ISC.</strong></p></td>
</tr>
<tr class="even">
<td><p>356.19</p>
<p>CLAIMS TRACKING UNBILLED AMOUNTS DATA</p></td>
<td><p>^IBE(356.19,</p>
<p>This file contains the data used in the compilation of the average inpatient bill totals and the monthly unbilled amounts bulletin and report.</p></td>
</tr>
<tr class="odd">
<td><p>356.2</p>
<p>INSURANCE REVIEW</p></td>
<td><p>^IBT(356.2,</p>
<p>This file contains information about the MCCR / UR portion of Utilization Review and the associated contacts with insurance carriers. Appropriateness of care is inferred from the approval and denial of billing days by the insurance carriers UR section. While this information appears to be primarily administrative in nature, it may contain sensitive clinical information and should be treated with the same confidentiality as required of all clinical data.</p></td>
</tr>
<tr class="even">
<td><p>356.21</p>
<p>CLAIMS TRACKING DENIAL REASONS</p></td>
<td><p>^IBE(356.21,</p>
<p>This file is a list of the standard reasons for denial of a claim. Editing this file may have significant impact on the results of the MCCR NDB roll up of Claims Tracking information. <strong>Do not add, edit, or delete entries in this file without instructions from the site ISC.</strong></p></td>
</tr>
<tr class="odd">
<td><p>356.22</p>
<p>HCS REVIEW TRANSMISSION FILE</p></td>
<td><p>^IBT(356.22,</p>
<p>This file contains information related to Healthcare Services Review worklist and corresponding HL7 messages (message type 278).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>356.25</p>
<p>CLAIMS TRACKING ROI</p></td>
<td><p>^IBT(356.25,</p>
<p>This file stores Release of Information (ROI) data collected that relates to a specific patient/drug/insurance combination for the effective dates. A claim that includes a sensitive drug is checked against this file for a billing determination. Claims that do not pass the check are determined to be not ECME billable. Bills that do not pass the check cannot be authorized.</p>
<p><strong>Per VHA Directive 2004-038, this file should not be modified or edited with VA FileMan.</strong></p></td>
</tr>
<tr class="odd">
<td><p>356.26</p>
<p>CLAIMS TRACKING ROI CONSENT</p></td>
<td><p>^IBT(356.26,</p>
<p>This file stores Release of Information (ROI) data obtained from a patient. Each sensitive</p>
<p>condition will have its own record. Data includes patient, sensitive condition, effective date of consent, expiration date when the consent ends, a revoked flag, and comments intended for entry of the Insurance the release consent covers.</p>
<p><strong>This file should not be modified or edited with VA FileMan</strong></p></td>
</tr>
<tr class="even">
<td><p>356.3</p>
<p>CLAIMS TRACKING SI/IS CATEGORIES</p></td>
<td><p>^IBE(356.3,</p>
<p>This file contains the major categories that are used to address the severity of illness and intensity of service. Specific criteria for each category must be met to address appropriateness of admission to continued stay in and discharge from specialized units and general units. Editing this file may have significant impact on the QM national roll up of Utilization Review information. The contents of this file are the general categories for Intensity of Service and Severity of Illness from InterQual. <strong>Do not add, edit, or delete entries in this file without instructions from the ISC.</strong></p></td>
</tr>
<tr class="odd">
<td><p>356.399</p>
<p>CLAIMS TRACKING/BILL</p></td>
<td><p>^IBT(356.399,</p>
<p>This file serves as a bridge between Claims Tracking and the Bill/Claims file (#399). An entry is created automatically by the billing module to link the events being billed to the Claims Tracking entry. It serves as a cross-reference in a many to many relationship for the entries in these two files. It should be maintained by the Billing module.</p></td>
</tr>
<tr class="even">
<td><p>356.4</p>
<p>CLAIMS TRACKING NON-ACUTE CLASSIFICATIONS</p></td>
<td><p>^IBE(356.4,</p>
<p>This file contains the list of approved non-acute classifications provided by the UM office in VACO. The codes are used in roll up of national data. <strong>Do not add, edit, or delete entries in this file without instructions from the ISC.</strong></p></td>
</tr>
<tr class="odd">
<td><p>356.5</p>
<p>CLAIMS TRACKING ALOS</p></td>
<td><p>^IBE(356.5,</p>
<p>This file contains the DRGs and average length of stays (ALOS) year that is the most common ALOS approved by insurance companies. This generally is much shorter than the ALOS for VA.</p></td>
</tr>
<tr class="even">
<td><p>356.6</p>
<p>CLAIMS TRACKING TYPE</p></td>
<td><p>^IBE(356.6,</p>
<p>This file contains the types of events that can be stored in Claims Tracking. It also contains data on how the Automated Biller is to handle each type of event. <strong>Do not add, edit, or delete entries in this file without instructions from the ISC.</strong></p></td>
</tr>
<tr class="odd">
<td><p>356.7</p>
<p>CLAIMS TRACKING ACTION</p></td>
<td><p>^IBE(356.7,</p>
<p>This file contains a list of the types of actions that may be taken on a review or a contact by an insurance company. <strong>Do not add, edit, or delete entries in this file without instructions from the ISC.</strong></p></td>
</tr>
<tr class="even">
<td><p>356.8</p>
<p>CLAIMS TRACKING NON-BILLABLE REASONS</p></td>
<td><p>^IBE(356.8,</p>
<p>This is a file of reasons that may be entered into the Claims Tracking module to specify why a potential claim is not billable<strong>. Do not add, edit, or delete entries in this file without instructions from the ISC</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>356.85</p>
<p>CLAIMS TRACKING BILLABLE FINDINGS</p></td>
<td><p>^IBT(356.85,</p>
<p>This file stores the Billable Findings codes for the Claims Tracking module of IB. Entries in this file are nationally distributed and should not be changed locally.</p></td>
</tr>
<tr class="even">
<td><p>356.9</p>
<p>INPATIENT DIAGNOSIS</p></td>
<td><p>^IBT(356.9,</p>
<p>This file is designed to hold all inpatient diagnoses.</p></td>
</tr>
<tr class="odd">
<td><p>356.91</p>
<p>INPATIENT PROCEDURE</p></td>
<td><p>^IBT(356.91,</p>
<p>This file is designed to hold all inpatient procedures.</p></td>
</tr>
<tr class="even">
<td><p>356.93</p>
<p>INPATIENT INTERIM DRG</p></td>
<td><p>^IBT(356.93,</p>
<p>This file holds interim DRGs computed by the Claims Tracking module for display in Claims Tracking and on reports. The computed ALOS is based upon 1992 HCFA average lengths of stay (ALOS), not VA averages. The purpose is to help utilization review personnel determine if the ALOS approved by an insurance company is within industry standards.</p></td>
</tr>
<tr class="odd">
<td><p>356.94</p>
<p>INPATIENT PROVIDERS</p></td>
<td><p>^IBT(356.94,</p>
<p>This file allows the Claims Tracking module to store the admitting physician. In addition, the attending and resident providers can be identified in this file. If attending and resident providers are entered, it is assumed to be entered completely for an episode of care being tracked. If no provider other than admitting physician is entered, the providers and attending from MAS will be the correct providers. Because QM data may be extracting this data on the national roll up, it is necessary to correctly identify the attending physician.</p></td>
</tr>
<tr class="even">
<td><p>357</p>
<p>ENCOUNTER FORM</p></td>
<td><p>^IBE(357,</p>
<p>This file contains encounter form descriptions used by the Encounter Form utilities to print encounter forms.</p></td>
</tr>
<tr class="odd">
<td><p>357.08</p>
<p>AICS PURGE LOG</p></td>
<td><p>^IBD(357.08,</p>
<p>This file will contain one entry for each time the AICS purge options are run. Both the automatic and manual options cause entries. The purpose of this file is to provide a historical log of the number of entries that are purged at each site.</p></td>
</tr>
<tr class="even">
<td><p>357.09</p>
<p>ENCOUNTER FORM PARAMETERS</p></td>
<td><p>^IBD(357.09,</p>
<p>This file contains the AICS parameters that control the operation of the package. Included are parameters to manage the automatic purge and those necessary to create print manager jobs that automatically queue encounter forms to print.</p></td>
</tr>
<tr class="odd">
<td><p>357.1</p>
<p>ENCOUNTER FORM BLOCK</p></td>
<td><p>^IBE(357.1,</p>
<p>This file contains descriptions of blocks, which are rectangular areas on an encounter form.</p></td>
</tr>
<tr class="even">
<td><p>357.2</p>
<p>SELECTION LIST</p></td>
<td><p>^IBE(357.2,</p>
<p>A selection list is composed of one or more rectangular area(s) in a block, called columns, which contain a list. The column(s) will have one or more sub columns, each sub column containing either text or an input symbol. The input symbols are for the user to mark to indicate a choice from the list.</p></td>
</tr>
<tr class="odd">
<td><p>357.3</p>
<p>SELECTION</p></td>
<td><p>^IBE(357.3,</p>
<p>This file contains the items appearing on the SELECTION LISTS. A selection can be composed of several fields; therefore, it can occupy several sub columns. Only the text is stored here, not the MARKING SYMBOLS.</p></td>
</tr>
<tr class="even">
<td><p>357.4</p>
<p>SELECTION GROUP</p></td>
<td><p>^IBE(357.4,</p>
<p>A Selection Group is a set of items on a list and the header under which those items should appear.</p></td>
</tr>
<tr class="odd">
<td><p>357.5</p>
<p>DATA FIELD</p></td>
<td><p>^IBE(357.5,</p>
<p>A data field can be composed of a label (determined at the time the form description is created) and data, coming from the DHCP database (determined at the time the form prints). The label and data are printed to the encounter form. A data field can be composed of subfields, each subfield containing possibly its own label and data.</p></td>
</tr>
<tr class="even">
<td><p>357.6*</p>
<p>PACKAGE INTERFACE</p></td>
<td><p>^IBE(357.6,</p>
<p>This file is used in the form design process and to print data to the form. It contains a description of all the interfaces with other packages.</p></td>
</tr>
<tr class="odd">
<td><p>357.69</p>
<p>TYPE OF VISIT</p></td>
<td><p>^IBE(357.69,</p>
<p>This file contains the Evaluation and Management codes. It consists of a subset of CPT codes used to describe the level of care for an outpatient visit.</p></td>
</tr>
<tr class="even">
<td><p>357.7</p>
<p>FORM LINE</p></td>
<td><p>^IBE(357.7,</p>
<p>This file contains either a horizontal or vertical line appearing on the form.</p></td>
</tr>
<tr class="odd">
<td><p>357.8</p>
<p>TEXT AREA</p></td>
<td><p>^IBE(357.8,</p>
<p>A TEXT AREA is a rectangular area on the form that displays a word processing field. The text is automatically formatted to fit within this area.</p></td>
</tr>
<tr class="even">
<td><p>357.91</p>
<p>MARKING AREA TYPE</p></td>
<td><p>^IBE(357.91,</p>
<p>This file contains the different types of marking areas in which the user can write that can be printed to a form. The following are examples: ( ), __,. These are for the person completing the form to enter a mark to indicate a choice.</p></td>
</tr>
<tr class="odd">
<td><p>357.92</p>
<p>PRINT CONDITIONS</p></td>
<td><p>^IBE(357.92,</p>
<p>This file contains a table containing a list of conditions recognized by the Print Manager; it is used to specify the conditions under which reports should be printed. The Print Manager is a program that scans the appointments for selected clinics for a selected date and prints specified reports under specified conditions.</p></td>
</tr>
<tr class="even">
<td><p>357.93</p>
<p>MULTIPLE CHOICE FIELD</p></td>
<td><p>^IBE(357.93,</p>
<p>This file allows multiple choice fields to be defined for forms.</p></td>
</tr>
<tr class="odd">
<td><p>357.94</p>
<p>ENCOUNTER FORM PRINTERS</p></td>
<td><p>^IBE(357.94,</p>
<p>This file contains a list of terminal types that can support either duplex printing or the printer control language PCL5. Entering the correct information in this file will allow encounter forms printed to these terminal types to utilize these features.</p></td>
</tr>
<tr class="even">
<td><p>357.95</p>
<p>FORM DEFINITION</p></td>
<td><p>^IBD(357.95,</p>
<p>Contains information about the form needed to process the input.</p></td>
</tr>
<tr class="odd">
<td><p>357.96</p>
<p>ENCOUNTER FORM TRACKING</p></td>
<td><p>^IBD(357.96,</p>
<p>This file is used to track the data capture efforts associated with each appointment.</p></td>
</tr>
<tr class="even">
<td><p>357.97</p>
<p>ENCOUNTER FORM COUNTERS</p></td>
<td><p>^IBD(357.97,</p>
<p>This file contains the counters needed by the encounter form utilities.</p></td>
</tr>
<tr class="odd">
<td><p>357.98</p>
<p>AICS DATA QUALIFIERS</p></td>
<td><p>^IBD(357.98,</p>
<p>A table of qualifiers used by the PCE Generic Device Interface.</p></td>
</tr>
<tr class="even">
<td><p>357.99</p>
<p>PRINT MANAGER CLINIC GROUPS</p></td>
<td><p>^IBD(357.99,</p>
<p>This file is used to create groups of clinics for use by the Print Manager.</p></td>
</tr>
<tr class="odd">
<td><p>358</p>
<p>IMP/EXP ENCOUNTER FORM</p></td>
<td><p>^IBE(358,</p>
<p>This file is nearly identical to File #357. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="even">
<td><p>358.1</p>
<p>IMP/EXP ENCOUNTER FORM BLOCK</p></td>
<td><p>^IBE(358.1,</p>
<p>This file is nearly identical to File #357.1. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="odd">
<td><p>358.2</p>
<p>IMP/EXP SELECTION LIST</p></td>
<td><p>^IBE(358.2,</p>
<p>This file is nearly identical to File #357.2. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="even">
<td><p>358.3</p>
<p>IMP/EXP SELECTION</p></td>
<td><p>^IBE(358.3,</p>
<p>This file is nearly identical to File #357.3. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="odd">
<td><p>358.4</p>
<p>IMP/EXP SELECTION GROUP</p></td>
<td><p>^IBE(358.4,</p>
<p>Nearly identical to File #357.4. It is used by the Import/ Export Utility as a workspace to Import / Export forms.</p></td>
</tr>
<tr class="even">
<td><p>358.5</p>
<p>IMP/EXP DATA FIELD</p></td>
<td><p>^IBE(358.5,</p>
<p>This file is nearly identical to File #357.5. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="odd">
<td><p>358.6</p>
<p>IMP/EXP PACKAGE INTERFACE</p></td>
<td><p>^IBE(358.6,</p>
<p>This file is nearly identical to File #357.6. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="even">
<td><p>358.7</p>
<p>IMP/EXP FORM LINE</p></td>
<td><p>^IBE(358.7,</p>
<p>This file is nearly identical to File #357.7. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="odd">
<td><p>358.8</p>
<p>IMP/EXP TEXT AREA</p></td>
<td><p>^IBE(358.8,</p>
<p>This file is nearly identical to File #357.8. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="even">
<td><p>358.91</p>
<p>IMP/EXP MARKING AREA</p></td>
<td><p>^IBE(358.91,</p>
<p>This file is nearly identical to File #357.91. It is used by the Import / Export Utility as a workspace for importing or exporting forms.</p></td>
</tr>
<tr class="odd">
<td><p>358.93</p>
<p>IMP/EXP MULTIPLE CHOICE FIELD</p></td>
<td><p>^IBE(358.93,</p>
<p>This file is used as a work space for the Import / Export utility of the encounter form utilities.</p></td>
</tr>
<tr class="even">
<td><p>358.94</p>
<p>IMP/EXP HAND PRINT FIELD</p></td>
<td><p>^IBE(358.94,</p>
<p>Used by the Import / Export utility as a workspace.</p></td>
</tr>
<tr class="odd">
<td><p>358.98</p>
<p>IMP/EXP AICS DATA QUALIFIERS</p></td>
<td><p>^IBD(358.98,</p>
<p>Used by the Import / Export utility of the encounter forms as a workspace.</p></td>
</tr>
<tr class="even">
<td><p>358.99</p>
<p>IMP/EXP AICS DATA ELEMENTS</p></td>
<td><p>^IBE(358.99,</p>
<p>Used as a workspace for the Import / Export utility.</p></td>
</tr>
<tr class="odd">
<td><p>359</p>
<p>CONVERTED FORMS</p></td>
<td><p>^IBD(359,</p>
<p>This file contains a list of forms created with the IB 2.0 version of the encounter form utilities that have been converted under AICS for scanning.</p></td>
</tr>
<tr class="even">
<td><p>359.1</p>
<p>AICS DATA ELEMENTS</p></td>
<td><p>^IBE(359.1,</p>
<p>Used to describe a simple data element, one that would appear as a single field on a form. The description includes instructions on how to print the field and how the scanning software should recognize it.</p></td>
</tr>
<tr class="odd">
<td><p>359.2</p>
<p>FORM SPECS</p></td>
<td><p>^IBD(359.2,</p>
<p>This file contains the description of the form used by the scanning software. The description, for example, must contain the locations of all the fields to be read.</p></td>
</tr>
<tr class="even">
<td><p>359.3</p>
<p>AICS ERROR AND WARNING LOG</p></td>
<td><p>^IBD(359.3,</p>
<p>This file is used to log errors that occur in the DHCP Server side of AICS.</p>
<p>Currently this occurs while rolling up the data from the scanner in a format that is then passed to the PCE Device Interface. Under normal circumstances, very few errors should occur. However, if an error does occur, the workstation software (client side) will be notified and the error can be found in this file and if possible, resolved. Normally each error represents one piece of data that was ignored by the server software and can easily be entered into PCE using one of the data entry methodologies.</p>
<p>Entries in this file may be deleted after any corrective action that needs to be taken is complete.</p></td>
</tr>
<tr class="odd">
<td><p>359.94</p>
<p>HAND PRINT FIELD</p></td>
<td><p>^IBE(359.94,</p>
<p>This file allows fields to be defined to print on forms for hand print.</p></td>
</tr>
<tr class="even">
<td><p>361</p>
<p>BILL STATUS MESSAGE</p></td>
<td><p>^IBM(361,</p>
<p>This file contains the data from the return status messages for IB bills returned via EDI from Austin FSC and AAC.</p></td>
</tr>
<tr class="odd">
<td><p>361.1</p>
<p>EXPLANATION OF BENEFITS</p></td>
<td><p>^IBM(361.1</p>
<p>This file contains the explanation of benefits results (EOB) for bills as well as MEDICARE remittance advice data. The data in this file may be appended to any subsequent claims in the COB process.</p>
<p>This file is also used by the Accounts Receivable package EDI LOCKBOX module to store 3rd Party remittance advice information.</p>
<p>Write access by EDI LOCKBOX is allowed only through API – see Integration Agreement - 4042</p>
<p>Read access by EDI LOCKBOX is allowed – see Integration Agreement - 4051</p></td>
</tr>
<tr class="even">
<td><p>361.2</p>
<p>IB ELECTRONIC REPORT DISPOSITION</p></td>
<td><p>^IBE(361.2,</p>
<p>This file contains a record for each electronic report that can be returned to the site by the V.A's clearinghouse. The purpose of the file is to allow the sites to determine which of these reports should be forwarded to the appropriate mail group and which ones should be ignored.</p></td>
</tr>
<tr class="odd">
<td><p>361.3</p>
<p>IB MESSAGE SCREEN TEXT</p></td>
<td><p>^IBE(361.3,</p>
<p>This file contains a list of words or phrases that, if found in the text of an electronic returned message for billing, will cause the message to be handled in one of two ways, based on a flag on each entry:</p>
<p>If the text is present, always file the message without requiring a review or if the text is found in the message, regardless of any text found in the rest of the message, always force it to be reviewed.</p></td>
</tr>
<tr class="even">
<td><p>361.4</p>
<p>EDI TEST CLAIM STATUS MESSAGE</p></td>
<td><p>^IBM(361.4,</p>
<p>This file contains the transmission history and return messages that were received via the test queue for claims that were sent initially as EDI claims and have been retransmitted as test claims.</p></td>
</tr>
<tr class="odd">
<td><p>362.1</p>
<p>IB AUTOMATED BILLING COMMENTS</p></td>
<td><p>^IBA(362.1,</p>
<p>This file contains entries created by the Third Party Automated Biller. As the Auto Biller attempts to create bills based on events in Claims Tracking, it sets entries in this file indicating the action taken by the Auto Biller for the event. The only way entries are added to this file is by the Auto Biller. There is no user entry.</p></td>
</tr>
<tr class="even">
<td><p>362.3</p>
<p>IB BILL/CLAIMS DIAGNOSIS</p></td>
<td><p>^IBA(362.3,</p>
<p>This file contains all diagnoses for bills in the Bill/Claims file (#399).</p></td>
</tr>
<tr class="odd">
<td><p>362.4</p>
<p>IB BILL/CLAIMS PRESCRIPTION REFILL</p></td>
<td><p>^IBA(362.4,</p>
<p>This file contains all prescription refills for bills in the BILL/CLAIMS file (#399).</p></td>
</tr>
<tr class="even">
<td><p>362.5</p>
<p>IB BILL/CLAIMS PROSTHETICS</p></td>
<td><p>^IBA(362.5,</p>
<p>This file contains all prosthetic items associated with bills in the BILL/CLAIMS file (#399).</p></td>
</tr>
<tr class="odd">
<td><p>363</p>
<p>RATE SCHEDULE</p></td>
<td><p>^IBE(363,</p>
<p>A Rate Schedule defines a specific type of service that may be billed to a specific payer. This links all elements necessary to define exactly what events are billed (Charge Set) to which payers (Rate Type).</p>
<p>There should be a unique Rate Schedule for each type of service billable to a payer.</p></td>
</tr>
<tr class="even">
<td><p>363.1</p>
<p>CHARGE SET</p></td>
<td><p>^IBE(363.1,</p>
<p>This file contains the definitions of all Charge Sets. A Charge Set defines a charge rate for a single type of billable event.</p>
<p><strong>DO NOT edit data in this file with VA File Manager.</strong></p></td>
</tr>
<tr class="odd">
<td><p>363.2</p>
<p>CHARGE ITEM</p></td>
<td><p>^IBA(363.2,</p>
<p>Individual billable items and charges. Each item that may be billed should have an entry. For the item to be automatically charged it must be an item defined on a bill.</p>
<p>The items are grouped into Charge Sets that correspond to rates.</p></td>
</tr>
<tr class="even">
<td><p>363.21</p>
<p>BILLING ITEMS</p></td>
<td><p>^IBA(363.21,</p>
<p>This file is part of the Rates process and contains billable items that may be found on a bill but do not have a source file.</p>
<p>Entries should only be added or deleted through the option provided.</p></td>
</tr>
<tr class="odd">
<td><p>363.3</p>
<p>BILLING RATE</p></td>
<td><p>^IBE(363.3,</p>
<p>This file defines the types of rates available to bill third parties for reimbursement.</p>
<p>Nationally distributed Billing Rates should not be modified. <strong>DO NOT edit data in this file with VA File Manager.</strong></p></td>
</tr>
<tr class="even">
<td><p>363.31</p>
<p>BILLING REGION</p></td>
<td><p>^IBE(363.31,</p>
<p>A Billing Region is an area defined by a Billing Rate as having a unique set of charges. This may correspond to one or more divisions.</p>
<p>Each Billing Rate may have multiple regions and each region may cover one or more divisions.</p></td>
</tr>
<tr class="odd">
<td><p>363.32</p>
<p>BILLING SPECIAL GROUPS</p></td>
<td><p>^IBE(363.32,</p>
<p>This file contains the names of special cases that should be applied to certain bill types. This includes the Revenue Code Link group names and the Provider Discount group names.</p></td>
</tr>
<tr class="even">
<td><p>363.33</p>
<p>BILLING REVENUE CODE LINKS</p></td>
<td><p>^IBE(363.33,</p>
<p>Certain types of bills require specific revenue codes to be used to bill certain types of care. This file allows the linking of revenue codes and the care provided.</p></td>
</tr>
<tr class="odd">
<td><p>363.34</p>
<p>BILLING PROVIDER DISCOUNT</p></td>
<td><p>^IBE(363.34,</p>
<p>This file contains a discount associated with a provider person class. This discount is generally used to adjust physician based provider charges for a non-physician provider. The discount will be applied to care billed to a Billing Rate for providers of the listed person class's.</p></td>
</tr>
<tr class="even">
<td><p>364</p>
<p>EDI TRANSMIT BILL</p></td>
<td><p>^IBA(364,</p>
<p>This file contains a record for each bill for each time it is included in a batch for EDI transmissions. This file allows a bill to be tracked throughout its transmission life and gives the bill's current EDI status.</p></td>
</tr>
<tr class="odd">
<td><p>364.1</p>
<p>EDI TRANSMISSION BATCH</p></td>
<td><p>^IBA(364.1,</p>
<p>This file contains a record for each 'batch' created for EDI transmission. It is used to track batch activity and to record statistics on number of bills in a batch that were rejected and accepted and to record the message number in Mailman that the batch is stored in for inquiry access.</p></td>
</tr>
<tr class="even">
<td><p>364.2</p>
<p>EDI MESSAGES</p></td>
<td><p>^IBA(364.2,</p>
<p>This file contains the messages that are sent electronically back to the site relating to EDI processing. These include, but are not limited to, status messages, error and warning messages found in the EDI transmission cycle, insurance company updates, batch summaries and statistics. These messages are stored by message type and options exist that scan this file and display the messages to the appropriate users and allow each one to be dealt with and resolved if necessary.</p></td>
</tr>
<tr class="odd">
<td><p>364.3</p>
<p>IB MESSAGE ROUTER</p></td>
<td><p>^IBE(364.3,</p>
<p>This file contains a listing of the transactions that can be handled by the IB message server. This file also contains the mail group that will receive any transaction processing error message and the entry point (TAG^ROUTINE) for each different transaction processing.</p></td>
</tr>
<tr class="even">
<td><p>364.4</p>
<p>IB EDI TRANSMISSION RULE</p></td>
<td><p>^IBE(364.4,</p>
<p>This file contains the rules to be applied to a bill to determine if it is eligible for transmission via national EDI.</p></td>
</tr>
<tr class="odd">
<td><p>364.5</p>
<p>IB DATA ELEMENT DEFINITION</p></td>
<td><p>^IBA(364.5,</p>
<p>This file contains the definition of all data elements that are needed for various forms throughout the MCCR DHCP system. It contains the 'blueprint' for how to extract the data for each data element entry.</p></td>
</tr>
<tr class="even">
<td><p>364.6</p>
<p>IB FORM SKELETON DEFINITION</p></td>
<td><p>^IBA(364.6,</p>
<p>This file contains records that define the skeleton makeup of forms for the IB system. This definition includes the absolute position of every field that can be output on the form, the length each field must be limited to, and some descriptive information. This includes printed forms, transmittable output files, and special local billing screens.</p></td>
</tr>
<tr class="odd">
<td><p>364.7</p>
<p>IB FORM FIELD CONTENT</p></td>
<td><p>^IBA(364.7,</p>
<p>This is the file that contains the specific fields to be used to produce the associated form or screen. If there is no insurance company or bill type specified for an entry, this is assumed to be the default definition of the field.</p></td>
</tr>
<tr class="even">
<td><p>365</p>
<p>IIV RESPONSE</p></td>
<td><p>^IBCN(365,</p>
<p>This file holds all responses to HL7 messages generated from the IIV Transmission Queue File for Insurance Identification and Verification.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.011</p>
<p>X12 271 ELIGIBILITY/BENEFIT</p></td>
<td><p>^IBE(365.011,</p>
<p>This file contains all the corresponding X.12 271 EB01 codes (Eligibility/Benefits).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.012</p>
<p>X12 271 COVERAGE LEVEL</p></td>
<td><p>^IBE(365.012,</p>
<p>This file contains all the corresponding X.12 271 EB02 codes (Coverage Level).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.013</p>
<p>X12 271 SERVICE TYPE</p></td>
<td><p>^IBE(365.013,</p>
<p>This file contains all the corresponding X.12 271 EB03 codes (Service Type).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.014</p>
<p>X12 271 INSURANCE TYPE</p></td>
<td><p>^IBE(365.014,</p>
<p>This file contains all the corresponding X.12 271 EB04 codes (Insurance Type).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.015</p>
<p>X12 271 TIME PERIOD QUALIFIER</p></td>
<td><p>^IBE(365.015,</p>
<p>This file contains all the corresponding X.12 271 EB06 codes (Time Period Qualifier).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.016</p>
<p>X12 271 QUANTITY QUALIFIER</p></td>
<td><p>^IBE(365.016,</p>
<p>This file contains all the corresponding X.12 271 EB09 codes (Quantity Qualifier).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.017</p>
<p>X12 271 ERROR CONDITION</p></td>
<td><p>^IBE(365.017,</p>
<p>This file contains all the corresponding X.12 271 AAA03 codes (Error Conditions). These values are returned because of an error in processing.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.018</p>
<p>X12 271 ERROR ACTION</p></td>
<td><p>^IBE(365.018,</p>
<p>This file contains all the corresponding X.12 271 AAA04 codes (Error Actions). Certain retry actions are programmed based upon the current values in this table.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.021</p>
<p>X12 271 CONTACT QUALIFIER</p></td>
<td><p>^IBE(365.021,</p>
<p>This file contains all the corresponding X.12 codes that identify a method for contact.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.022</p>
<p>X12 271 ENTITY IDENTIFIER CODE</p></td>
<td><p>^IBE(365.022,</p>
<p>This file contains all the corresponding X.12 codes that identify an eligibility / benefit entity.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.023</p>
<p>X12 271 IDENTIFICATION QUALIFIER</p></td>
<td><p>^IBE(365.023,</p>
<p>This file contains all the corresponding X.12 codes for identification qualifiers.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.024</p>
<p>X12 271 PROVIDER CODE</p></td>
<td><p>^IBE(365.024,</p>
<p>This file contains all the corresponding X.12 codes that identify a provider.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.025</p>
<p>X12 271 DELIVERY FREQUENCY CODE</p></td>
<td><p>^IBE(365.025,</p>
<p>This file contains all the corresponding X.12 codes for delivery frequency.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.026</p>
<p>X12 271 DATE QUALIFIER</p></td>
<td><p>^IBE(365.026,</p>
<p>This file contains all the corresponding X.12 codes for date / time qualifiers.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.027</p>
<p>X12 271 LOOP ID</p></td>
<td><p>^IBE(365.027,</p>
<p>This file contains all the corresponding X.12 codes for loop IDs. It is a dictionary to map X12 codes to corresponding values. The codes are used to parse inbound type 271 messages, among others. HIPAA loop IDs come from FSC as part of 271 response message.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.028</p>
<p>X12 271 REFERENCE IDENTIFICATION</p></td>
<td><p>^IBE(365.028,</p>
<p>This file contains all the corresponding X.12 codes for reference identification codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.029</p>
<p>X12 271 UNITS OF MEASUREMENT</p></td>
<td><p>^IBE(365.029,</p>
<p>This file contains all the corresponding X.12 271 Units of measurement.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.031</p>
<p>X12 271 ENTITY RELATIONSHIP CODE</p></td>
<td><p>^IBE(365.031,</p>
<p>This file contains all the corresponding X.12 271 Entity Relationship codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.032</p>
<p>X12 271 DATE FORMAT QUALIFIER</p></td>
<td><p>^IBE(365.032,</p>
<p>This file contains all the corresponding X.12 271 date format qualifiers.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.033</p>
<p>X12 271 YES/NO RESPONSE CODE</p></td>
<td><p>^IBE(365.033,</p>
<p>This file contains the corresponding X.12 271 YES / NO condition or Response codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.034</p>
<p>X12 271 LOCATION QUALIFER</p></td>
<td><p>^IBE(365.034,</p>
<p>This file contains all the corresponding X.12 271 Location Qualifiers.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.035</p>
<p>X12 271 PROCEDURE CODING METHOD</p></td>
<td><p>^IBE(365.035,</p>
<p>This file contains all the corresponding X.12 271 procedure coding methods.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.036</p>
<p>X12 271 DELIVERY PATTERN</p></td>
<td><p>^IBE(365.036,</p>
<p>This file contains all the corresponding X12 271 Delivery Pattern codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.037</p>
<p>X12 271 PATIENT RELATIONSHIP</p></td>
<td><p>^IBE(365.037,</p>
<p>This file contains all the corresponding X.12 271 patient relationship codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.038</p>
<p>X12 271 INJURY CATEGORY</p></td>
<td><p>^IBE(365.038,</p>
<p>This file contains all the corresponding X.12 271 Nature of Injury Category codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.039</p>
<p>X12 271 MILITARY PERSONNEL INFO STATUS CODE</p></td>
<td><p>^IBE(365.039,</p>
<p>This file contains all the corresponding X.12 271 military personnel information status codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.041</p>
<p>X12 271 MILITARY GOVT SERVICE AFFILIATION</p></td>
<td><p>^IBE(365.041,</p>
<p>This file contains all the corresponding X.12 271 military personnel information government service affiliation codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.042</p>
<p>X12 271 MILITARY SERVICE RANK</p></td>
<td><p>^IBE(365.042,</p>
<p>This file contains all the corresponding X.12 271 military personnel information rank codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.043</p>
<p>X12 271 ENTITY TYPE QUALIFIER</p></td>
<td><p>^IBE(365.043,</p>
<p>This file contains all the corresponding X.12 271 Entity Type Qualifiers.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.044</p>
<p>X12 271 CODE LIST QUALIFIER</p></td>
<td><p>^IBE(365.044,</p>
<p>This file contains all the corresponding X.12 271 code list qualifiers.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.045</p>
<p>X12 271 NATURE OF INJURY CODES</p></td>
<td><p>^IBE(365.045,</p>
<p>This file contains all the corresponding X.12 271 NATURE OF INJURY CODES.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.046</p>
<p>X12 271 MILITARY EMPLOYMENT STATUS CODE</p></td>
<td><p>^IBE(365.046,</p>
<p>This file contains all the corresponding X.12 271 MPI employment status codes.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.1</p>
<p>IIV TRANSMISSION QUEUE</p></td>
<td><p>^IBCN(365.1,</p>
<p>This file contains records that have been selected based on specific criteria to generate an HL7 message. These messages will be sent to the Eligibility Communicator for processing.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.11</p>
<p>IIV AUTO MATCH</p></td>
<td><p>^IBCN(365.11,</p>
<p>The Auto Match file is a VistA facility to help IIV match user-entered insurance company names to the correct insurance company names in the insurance company file. This file links together an Auto Match Value with a valid insurance company name. The Auto Match Value may contain common spelling mistakes and wildcard characters to aid in the selection of a valid insurance company name.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.12</p>
<p>PAYER</p></td>
<td><p>^IBE(365.12,</p>
<p>This is a standard file exported by the IB package. It contains insurance payers for the VA. The Payers included are used for electronically verifying insurance and authorization/referral requests. Do not add, edit, or delete these entries except through the provided edit options.</p>
<p><strong>Per VA Directive 6402, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.13</p>
<p>PAYER APPLICATION</p></td>
<td><p>^IBE(365.13,</p>
<p>This file contains all the different applications that a payer could be contacted electronically for.</p>
<p>Initially there will only be electronic insurance verification (eIV) as an application.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.14</p>
<p>IIV TRANSMISSION STATUS</p></td>
<td><p>^IBE(365.14,</p>
<p>This file contains all the statuses that an electronic insurance verification transmission or receiving record can have.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.15</p>
<p>IIV STATUS TABLE</p></td>
<td><p>^IBE(365.15,</p>
<p>This file contains the various IIV statuses for entries in the Insurance Verification Processor. Also included are the symbols that should appear in the eIV status column in the Insurance Verification Processor list, and a more detailed description of the status that is used in the Expand Entry action.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.18</p>
<p>EIV EICD TRACKING</p></td>
<td><p>^IBCN(365.18,</p>
<p>This file allows VistA to track data associated with the Electronic Insurance</p>
<p>Coverage Discovery (EICD) extract process. Both Identification and Verification EICD transactions (inquiries and responses) are detailed and tracked in this file.</p>
<p><strong>Per VHA Directive 6402, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>365.19</p>
<p>INTERFACILITY INSURANCE UPDATE</p></td>
<td><p>^IBCN(365.19,</p>
<p>This file contains records that have been selected based on specific criteria to generate an HL7 message in order to share recently verified active insurance policies to other VAMCs via the Interfacility Insurance Update (IIU) process. This file also contains all recently verified policies that were received from other VAMCs via IIU.</p>
<p><strong>Per VA Directive 6402, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>365.2</p>
<p>IIV RESPONSE REVIEW</p></td>
<td><p>^IBCN(365.2,</p>
<p>This file holds the outcome of the reviews of MEDICARE (WNR) messages contained in the IIV RESPONSE file (#365). The file is populated when the user enters comments and statuses against selected messages using the Medicare Potential COB Worklist [IBCNE POTENTIAL COB LIST] option.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>366.01</p>
<p>NCPDP PROCESSOR</p></td>
<td><p>^IBCNR(366.01,</p>
<p>This Integrated Billing (IB) file was created for the e-Pharmacy Project. It is maintained centrally, via real time HL7 Table Update Messages, using the WebMD database. Never maintain locally, except via a designated and secured option that edits selected APPLICATION Sub-file fields, such as LOCAL ACTIVE. A NCPDP Processor receives NCPDP transmissions and adjudicates NCPDP claims. A NCPDP Processor is uniquely identified by its' name.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>366.02</p>
<p>PHARMACY BENEFITS MANAGER (PBM)</p></td>
<td><p>^IBCNR(366.02,</p>
<p>This Integrated Billing (IB) file was created for the e-Pharmacy Project. It is maintained centrally, via real time HL7 Table Update Messages, using the WebMD database. Never maintain locally, except via a designated and secured option that edits selected APPLICATION Sub-file fields, such as LOCAL ACTIVE. A Pharmacy Benefits Manager (PBM) administers a plan on behalf of the insurance company payer. A PBM is typically a separate, contracted entity, but it may be the insurance company payer. A PBM is uniquely identified by its' name.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>366.03</p>
<p>PLAN</p></td>
<td><p>^IBCNR(366.03,</p>
<p>This Integrated Billing (IB) file was created for the e-Pharmacy Project. It is maintained centrally, via real time HL7 Table Update Messages, using the WebMD database. Never maintain locally, except via a designated and secured option that edits selected APPLICATION Sub-file fields, such as LOCAL ACTIVE. A Plan is a Payer's medical health care insurance product that defines benefits and delivery to organizations and individuals that enroll in the Plan. A Plan is uniquely identified by its' identifier (VA National Plan ID).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>366.11</p>
<p>NCPDP PROCESSOR APPLICATION</p></td>
<td><p>^IBCNR(366.11,</p>
<p>This Integrated Billing (IB) file was created for the e-Pharmacy Project. It is maintained centrally. Never maintain locally. A NCPDP Processor Application identifies an electronic interface application associated with the NCPDP PROCESSOR File (366.01). A NCPDP Processor Application is uniquely identified by its' name.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>366.12</p>
<p>PHARMACY BENEFITS MANAGER (PBM) APPLICATION</p></td>
<td><p>^IBCNR(366.12,</p>
<p>This Integrated Billing (IB) file was created for the e-Pharmacy Project. It is maintained centrally. Never maintain locally. A Pharmacy Benefits Manager (PB) Application identifies an electronic interface application associated with the PHARMACY BENEFITS MANAGER (PBM) File (366.02). A PBM Application is uniquely identified by its' name.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>366.13</p>
<p>PLAN APPLICATION</p></td>
<td><p>^IBCNR(366.13,</p>
<p>This Integrated Billing (IB) file was created for the e-Pharmacy Project. It is maintained centrally. Never maintain locally.</p>
<p>A Plan Application identifies an electronic interface application associated with the PLAN File (366.03). A Plan Application is uniquely identified by its' name.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>366.14</p>
<p>IB NCPDP EVENT LOG</p></td>
<td><p>^IBCNR(366.14,</p>
<p>This file contains data that are passed into IB NCPDP APIs by outside applications - E CLAIMS MGMT ENGINE and OUTPATIENT PHARMACY (see IA # 4299). Data stored in this file are used for IB ECME EVENT report to provide details about E-Pharmacy claims processing and about communication details between IB and the applications listed above. The data in this file is populated internally by the IB application (data not directly entered by the user).</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>366.15</p>
<p>IB NCPDP PRESCRIPTION</p></td>
<td><p>^IBCNR(366.15,</p>
<p><strong>DO NOT delete entries in this file. DO NOT edit data in this file with VA File Manager.</strong></p>
<p>This file is used to support NCPDP billing for multiple Rate Types. Entries are created in this file based on the prescription and fill/refill number. The Rate Type determined at time of Billing Determination is stored in this file so it can be utilized when bill creation occurs. This file is also used to store the associated co-payment reference number if a non-veteran co-payment charge is created to allow easy lookup if the co-payment charge needs to be cancelled.</p>
<p><strong>Per VHA Directive 2004-038, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>366.16</p>
<p>IB NDC NON COVERED BY PLAN</p></td>
<td><p>^IBCNR(366.16,</p>
<p>This file is used to store drug's NDC rejected by payers as non-covered by pharmacy plan. The drug's NDC, Group Insurance Plan and the last date the drug was rejected are used by Integrated Billing and ECME packages to prevent sending e-claims for non-covered drugs.</p>
<p><strong>Per VHA Directive 2004-038, this file should not be modified or edited with VA FileMan.</strong></p></td>
</tr>
<tr class="odd">
<td><p>366.17</p>
<p>IB NCPDP NON-BILLABLE STATUS REASONS</p></td>
<td><p>This file contains the non-billable status reasons used by the IB NCPDP Billing Event Log and that are returned by the IB Billable Status Check for ePharmacy claims.</p>
<p><strong>Per VHA Directive 2004-038, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td>367<br />
HPID/OEID RESPONSE</td>
<td><p>^IBCNH(367,</p>
<p>This file contains responses associated with inquiries from the HPID / OEID TRANSMISSION QUEUE file (file #367.1)</p></td>
</tr>
<tr class="odd">
<td>367.1<br />
HPID/OEID TRANSMISSION QUEUE</td>
<td><p>^IBCNH(367.1,</p>
<p>This file contains records that have been selected based on specific criteria to generate an HL7 message. These messages will be sent to the National Insurance File (NIF) for processing.</p></td>
</tr>
<tr class="even">
<td>367.11<br />
INSURANCE COMPANY ID TYPE</td>
<td><p>^IBE(367.11,</p>
<p>This file contains the possible ID types that could be received from the National Insurance file (NIF) for an Insurance Company entry.</p></td>
</tr>
<tr class="odd">
<td><p>368</p>
<p>HEALTH CARE CLAIM RFAI (277)</p></td>
<td><p>^IBA(368</p>
<p>This file contains all records received from the FSC ASC X12N health Care Claim Request For Additional Information (277) HL7 message.</p></td>
</tr>
<tr class="even">
<td><p>368.001</p>
<p>X12 277 CLAIM STATUS CATEGORY</p></td>
<td><p>^IBE(368.001</p>
<p>This file contains Health Care Claim Status Codes - limited to the R codes of X12 code source 507.</p></td>
</tr>
<tr class="odd">
<td><p>368.002</p>
<p>X12 277 PRODUCT OR SERVICE ID QUAL</p></td>
<td><p>^IBE(368.002</p>
<p>This file contains Code identifying the type / source of the descriptive number used in Product / Service ID.</p></td>
</tr>
<tr class="even">
<td><p>372</p>
<p>PFSS SITE PARAMETERS</p></td>
<td><p>^IBBAS(372,</p>
<p>The PFSS SITE PARAMETERS file holds data required for proper function of the IBB software, which provides common utilities and procedures for PFSS.</p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>373</p>
<p>PFSS CHARGE CACHE</p></td>
<td><p>^IBBAD(373,</p>
<p>This file is used to store charge data from various VistA applications so that a background process can create an HL7 P03 message from each record. The messages are batched and sent to the external medical billing system.</p>
<p><strong>Under no circumstances may records be created or modified directly via FileMan or other methods. Record creation and data update is allowed only through CHARGE^IBBAPI.</strong></p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="even">
<td><p>375</p>
<p>PFSS ACCOUNT</p></td>
<td><p>^IBBAA(375,</p>
<p>This file is used to store visit/encounter data from various VistA applications, so that a background process can create HL7 ADT messages that are sent to the external medical billing system.</p>
<p><strong>Under no circumstances may records be created or modified directly via FileMan or other methods. Record creation and data update is allowed only through GETACCT^IBBAPI.</strong></p>
<p><strong>Per VHA Directive 10-93-142, this file definition should not be modified.</strong></p></td>
</tr>
<tr class="odd">
<td><p>389.9</p>
<p>STATION NUMBER (TIME SENSITIVE)</p></td>
<td><p>^VA(389.9,</p>
<p>The purpose of this file is to allow DHCP software flexibility and reliability when the station number of a medical center changes or when one or more stations have merged into one station.</p>
<p>Adding or modifying entries in this file may affect many DHCP applications. Control of entry into this file should be carefully controlled by the IRM Service Chief.</p></td>
</tr>
<tr class="even">
<td><p>390</p>
<p>ENROLLMENT RATED DISABILITY UPLOAD AUDIT</p></td>
<td><p>^DGRDUA(390,</p>
<p>This file tracks new/modified Rated Disability changes received from the Health Eligibility Center via ORU / ORF Z11 messages. The purpose of this file is for History only and cannot be considered current. Data will be purged from this file after it is over 365 days old.</p></td>
</tr>
<tr class="odd">
<td><p>391</p>
<p>TYPE OF PATIENT</p></td>
<td><p>^DG(391,</p>
<p>This file contains the various types of patient that might be seen at a VA facility. The file is pointed to by the TYPE field of the PATIENT file and every patient added to the system must have a TYPE specified. Using the 'Patient Type Update' option of ADT the user should specify the parameters concerning which screens should be displayed during the registration process for these patient types and what data elements on those screens are editable.</p></td>
</tr>
<tr class="even">
<td><p>391.1</p>
<p>AMIS SEGMENT</p></td>
<td><p>^DG(391.1,</p>
<p>This file contains the various AMIS segments. The .001 (Number) field should be defined as the segment number.</p></td>
</tr>
<tr class="odd">
<td><p>391.23</p>
<p>DG REGISTER ONCE FIELD DEFINITION</p></td>
<td><p>^DGRO(391.23,</p>
<p>This file is used to define the fields that are collected at a Last Site Treated and loaded into a Querying Site via Register Once Messaging.</p>
<ol start="4">
<li><p>Register Once is being removed from the Register A Patient option by patch DG*5.3*915.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><p>391.31</p>
<p>HOME TELEHEALTH PATIENT</p></td>
<td>^DGHT(391.31,</td>
</tr>
<tr class="odd">
<td><p>391.71</p>
<p>ADT/HL7 PIVOT</p></td>
<td><p>^VAT(391.71,</p>
<p>This file serves as a funnel for all of the ADT events that need to be broadcast to any system. The VISIT file may replace this file in the future. The entries in this file will contain information on how to get back to its parent event in PIMS. There are no parent child relationships stored here.</p></td>
</tr>
<tr class="even">
<td><p>391.72</p>
<p>ADT/HL7 EVENT REASON</p></td>
<td><p>^VAT(391.72,</p>
<p>This file contains the event reason codes for admission, discharge, and transfer (ADT) Health Level Seven (HL7) events.</p></td>
</tr>
<tr class="odd">
<td><p>391.91</p>
<p>TREATING FACILITY LIST</p></td>
<td><p>^DGCN(391.91,</p>
<p>This file holds the Treating Facility List, a list of institutions where the patient has had treatment.</p>
<p>- IB*2.0*676 the TFL will contain Cerner as a treating facility. (Not part of this patch) IB*676 will allow transactions that need to go to Cerner an HL7 process to send and receive transactions, Query’s, and Query Response</p></td>
</tr>
<tr class="even">
<td><p>391.92</p>
<p>VAFC ASSIGNING AUTHORITY</p></td>
<td><p>^DGCN(391.92,</p>
<p>The VAFC ASSIGNING AUTHORITY (#391.92) file expands the capability of VA Identity Management Service (IdM) to support future initiatives, (e.g., National Health Information Network (NHIN) and non-Patient Identity Management, etc.). This file stores a portion of the data used to assemble fully qualified identifiers used for either the Health Level Seven v2.4 or v3.0 standard.</p></td>
</tr>
<tr class="odd">
<td><p>391.98</p>
<p>PATIENT DATA EXCEPTION</p></td>
<td><p>^DGCN(391.98,</p>
<p>This file is currently used to log exceptions encountered and status. This file should not be limited to demographic exceptions as it is a place holder. It is tied to a patient.</p></td>
</tr>
<tr class="even">
<td><p>391.984</p>
<p>EXCEPTION STATUS</p></td>
<td><p>^DGCN(391.984,</p>
<p>This file contains the status name and code (abbreviation) associated with the exceptions processed by the Patient Data Review [VAFC EXCEPTION HANDLER] option.</p></td>
</tr>
<tr class="odd">
<td><p>391.99</p>
<p>PATIENT DATA ELEMENT</p></td>
<td><p>^DGCN(391.99,</p>
<p>This file is used to store each individual data element and its location for the exception that is logged.</p></td>
</tr>
<tr class="even">
<td><p>392</p>
<p>BENEFICIARY TRAVEL CLAIM</p></td>
<td><p>^DGBT(392,</p>
<p>This file contains the completed travel claim entries for patients showing departure/destination data, as well as specific claim data.</p></td>
</tr>
<tr class="odd">
<td><p>392.1</p>
<p>BENEFICIARY TRAVEL DISTANCE</p></td>
<td><p>^DGBT(392.1,</p>
<p>This file contains the mileage data between departure cities and medical center divisions. Each departure city can have multiple divisions entered, each with its own associated mileage, most economical cost, and remarks field.</p></td>
</tr>
<tr class="even">
<td><p>392.2</p>
<p>BENEFICIARY TRAVEL CERTIFICATION</p></td>
<td><p>^DGBT(392.2,</p>
<p>This file contains the income certification data for patients for Beneficiary Travel claims, including amount certified, eligibility for Benefit Travel, and means test status.</p></td>
</tr>
<tr class="odd">
<td><p>392.3</p>
<p>BENEFICIARY TRAVEL ACCOUNT</p></td>
<td><p>^DGBT(392.3,</p>
<p>Although this file has been decentralized, changes and additions should be made with extreme care.</p></td>
</tr>
<tr class="even">
<td><p>392.31</p>
<p>LOCAL VENDOR</p></td>
<td><p>^DGBT(392.31,</p>
<p>This file contains vendors of the Core Financial Logistics System (coreFLS) used by the local system. Entries should only be added and updated through the applications interfaced with coreFLS. Entries SHOULD NOT be added, edited, or deleted through File Manager.</p></td>
</tr>
<tr class="odd">
<td><p>392.4</p>
<p>BENEFICIARY TRAVEL MODE OF TRANSPORTATION</p></td>
<td><p>^DGBT(392.4,</p>
<p>This file contains the data on the different modes of transportation available in Benefit Travel claims.</p></td>
</tr>
<tr class="even">
<td><p>393</p>
<p>INCOMPLETE RECORDS</p></td>
<td><p>^VAS(393,</p>
<p>This file is the main file for the Incomplete Records Tracking package IRT This is where all the data is stored that will be displayed for each deficiency on the enter / edit screens and on all the reports.</p></td>
</tr>
<tr class="odd">
<td><p>393.1</p>
<p>MAS SERVICE</p></td>
<td><p>^DG(393.1,</p>
<p>This file stores all the possible services for both wards and clinics.</p></td>
</tr>
<tr class="even">
<td><p>393.2</p>
<p>IRT STATUS</p></td>
<td><p>^DG(393.2,</p>
<p>This is the file that contains the names of the statuses that an IRT record must go thru to its completion.</p></td>
</tr>
<tr class="odd">
<td><p>393.3</p>
<p>IRT TYPE OF DEFICIENCY</p></td>
<td><p>^VAS(393.3,</p>
<p>This file contains the names of the types of deficiencies that are tracked in the IRT package.</p></td>
</tr>
<tr class="even">
<td><p>393.41</p>
<p>TYPE OF CATEGORY</p></td>
<td><p>^VAS(393.41,</p>
<p>This is the file that stores the name of the category and all data elements related to the category, that a deficiency falls under. There are thirteen categories.</p></td>
</tr>
<tr class="odd">
<td><p>394</p>
<p>*PDX TRANSACTION</p></td>
<td><p>^VAT(394,</p>
<p>This file has been replaced with the VAQ - TRANSACTION file (#394.61).</p>
<p>Version 1.0 of PDX used this file to store administrative information concerning all PDX transmissions. Version 1.5 of PDX has marked it for deletion and version 2.0 will delete it.</p></td>
</tr>
<tr class="even">
<td><p>394.1</p>
<p>*PDX DATA</p></td>
<td><p>^VAT(394.1,</p>
<p>This file has been replaced with the VAQ - DATA file (#394.62).</p>
<p>Version 1.0 of PDX used this file to store patient information that was transmitted using PDX. Version 1.5 of PDX has marked it for deletion and version 2.0 will delete it.</p></td>
</tr>
<tr class="odd">
<td><p>394.2</p>
<p>*PDX PARAMETER</p></td>
<td><p>^VAT(394.2,</p>
<p>This file has been replaced with the VAQ - PARAMETER file (#394.81).</p>
<p>Version 1.0 of PDX used this file to store site specific information concerning the use of PDX. Version 1.5 of PDX has marked it for deletion and version 2.0 will delete it.</p></td>
</tr>
<tr class="even">
<td><p>394.3</p>
<p>*PDX STATUS</p></td>
<td><p>^VAT(394.3,</p>
<p>This file has been replaced with the VAQ - STATUS file (#394.85).</p>
<p>Version 1.0 of PDX used this file to store all possible phases of a PDX transmission. Version 1.5 of PDX has marked it for deletion and version 2.0 will delete it.</p></td>
</tr>
<tr class="odd">
<td><p>394.4</p>
<p>*PDX STATISTICS</p></td>
<td><p>^VAT(394.4,</p>
<p>This file has been replaced with the VAQ - WORKLOAD file (#394.87).</p>
<p>Version 1.0 of PDX used this file to store workload statistics concerning use of PDX. Version 1.5 of PDX has marked it for deletion and version 2.0 will delete it.</p></td>
</tr>
<tr class="even">
<td><p>394.61</p>
<p>VAQ - TRANSACTION</p></td>
<td><p>^VAT(394.61,</p>
<p>This file holds information describing each PDX transaction. A PDX transaction is created when one of the following events occur.</p></td>
</tr>
<tr class="odd">
<td><p>394.62</p>
<p>VAQ - DATA</p></td>
<td><p>^VAT(394.62,</p>
<p>This file holds any patient information that was transmitted using PDX.</p></td>
</tr>
<tr class="even">
<td><p>394.71</p>
<p>VAQ - DATA SEGMENT</p></td>
<td><p>^VAT(394.71,</p>
<p>This file defines each data segment currently supported by PDX.</p></td>
</tr>
<tr class="odd">
<td><p>394.72</p>
<p>VAQ - ENCRYPTION METHOD</p></td>
<td><p>^VAT(394.72,</p>
<p>This file defines each encryption method currently supported by PDX.</p></td>
</tr>
<tr class="even">
<td><p>394.73</p>
<p>VAQ - ENCRYPTED FIELDS</p></td>
<td><p>^VAT(394.73,</p>
<p>This file contains all fields that should be encrypted in PDX Requests and Unsolicited PDXs transmitted by the facility. This file is only relevant when encryption has been turned on.</p></td>
</tr>
<tr class="odd">
<td><p>394.81</p>
<p>VAQ - PARAMETER</p></td>
<td><p>^VAT(394.81,</p>
<p>This file contains site specific information concerning the use of PDX. Only one entry may be made in this file.</p></td>
</tr>
<tr class="even">
<td><p>394.82</p>
<p>VAQ - RELEASE GROUP</p></td>
<td><p>^VAT(394.82,</p>
<p>This file contains the facilities that have been granted 'Automatic Processing'. In order for a request to be automatically processed, the requesting facility must have an entry in this file.</p></td>
</tr>
<tr class="odd">
<td><p>394.83</p>
<p>VAQ - OUTGOING GROUP</p></td>
<td><p>^VAT(394.83,</p>
<p>This file contains groups of facilities commonly accessed using PDX.</p></td>
</tr>
<tr class="even">
<td><p>394.84</p>
<p>VAQ - SEGMENT GROUP</p></td>
<td><p>^VAT(394.84,</p>
<p>This file contains groups of data segments commonly referenced by the facility. Groups marked as 'Public' may be referenced by all users of PDX. Groups marked as 'Private' may only be referenced by the individual that created the group.</p></td>
</tr>
<tr class="odd">
<td><p>394.85</p>
<p>VAQ - STATUS</p></td>
<td><p>^VAT(394.85,</p>
<p>This file defines all possible statuses of a PDX transaction.</p>
<p>Codes must be in the form XXXX-YYYYY where XXXX is the namespace of the package (1-4 upper case characters) and YYYYY is 1-5 characters (upper or lower case) of the package's choosing. [Must pattern match 1.4U1"-"1.5A]</p></td>
</tr>
<tr class="even">
<td><p>394.86</p>
<p>VAQ - AUTO-NUMBERING</p></td>
<td><p>^VAT(394.86,</p>
<p>This file is used to implement auto-numbering in the PDX files. Fields with auto-numbering capability will have an entry in this file</p></td>
</tr>
<tr class="odd">
<td><p>394.87</p>
<p>VAQ - WORKLOAD</p></td>
<td><p>^VAT(394.87,</p>
<p>This file contains statistics concerning the workload done using PDX. PDX workload is considered to be requesting patient information from another facility, manually processing requests from another facility, and uploading PDX data to the Patient File. Work done by the PDX Server is also stored in this file.</p></td>
</tr>
<tr class="even">
<td><p>394.88</p>
<p>VAQ - WORK</p></td>
<td><p>^VAT(394.88,</p>
<p>This file contains the type of work being tracked by the VAQ - WORKLOAD file (#394.87).</p></td>
</tr>
<tr class="odd">
<td><p>395</p>
<p>DVB PARAMETERS</p></td>
<td>^DVB(395,</td>
</tr>
<tr class="even">
<td><p>395.1</p>
<p>ENTITLEMENT CODES</p></td>
<td>^DVB(395.1,</td>
</tr>
<tr class="odd">
<td><p>395.2</p>
<p>ANATOMICAL-LOSS CODES</p></td>
<td>^DVB(395.2,</td>
</tr>
<tr class="even">
<td><p>395.3</p>
<p>MONTHLY COMPENSATION</p></td>
<td>^DVB(395.3,</td>
</tr>
<tr class="odd">
<td><p>395.4</p>
<p>DIARY DEFINITIONS</p></td>
<td>^DVB(395.4,</td>
</tr>
<tr class="even">
<td><p>395.5</p>
<p>HINQ SUSPENSE</p></td>
<td>^DVB(395.5,</td>
</tr>
<tr class="odd">
<td><p>395.7</p>
<p>HINQ AUDIT</p></td>
<td>^DVB(395.7,</td>
</tr>
<tr class="even">
<td><p>396</p>
<p>FORM 7131</p></td>
<td><p>^DVB(396,</p>
<p>Holds all requests for 7131 information. This is the information that was requested on the old paper 7131 forms.</p>
<p>Node 6 was added with Version 2.7 of AMIE. This node contains the divisions a selected report on a 7131 has been transferred to. Node 7 was added with Version 2.7 of AMIE. This node contains the dates a report on a 7131 was transferred to another division. These nodes are used only by Multidivisional facilities that transfer reports on a 7131. The decimal portion of the field numbers for the fields on nodes 6 and 7 indicates the node the field exists on. The piece position for each field on nodes 6 and 7 corresponds to the piece position of its respective report status field on that report's node.</p>
<ol start="5">
<li><p>The 'AE' and 'AF' cross-references are specialized MUMPS cross- references used to implement the Divisional Transfer of reports on a 7131 request. Please follow the technical descriptions of the above cross-references when re-indexing.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><p>396.1</p>
<p>AMIE SITE PARAMETER</p></td>
<td><p>^DVB(396.1,</p>
<p>Holds the package specific parameters for the AMIE site.</p></td>
</tr>
<tr class="even">
<td><p>396.15</p>
<p>CAPRI DIVISION EXAM LIST</p></td>
<td><p>^DVB(396.15,</p>
<p>This file is used by the CAPRI GUI to maintain a list of AMIE C&amp;P examinations that are assigned to a specific medical center division. It is also possible to set a flag in this file to disable the division from appearing in the listing of selectable divisions in the GUI.</p></td>
</tr>
<tr class="odd">
<td><p>396.17</p>
<p>CAPRI TEMPLATES</p></td>
<td><p>^DVB(396.17,</p>
<p>This file holds the definitions generated by users of the CAPRI C&amp;P Worksheet Module (CPWM) that are used to re-generate GUI screens. CPWM allows point-n-click entry of C&amp;P examinations and will store ASCII reports in AMIE and TIU when the user has finished the documentation process. This file serves to track documents in progress as well as documents that have been already completed and sent to TIU and AMIE.</p></td>
</tr>
<tr class="even">
<td><p>396.18</p>
<p>CAPRI TEMPLATE DEFINITIONS</p></td>
<td><p>^DVB(396.18,</p>
<p>This file maintains a list of definitions used to generate examination templates in the CAPRI GUI interface. These definitions will be used by providers to document C&amp;P examinations in point-n-click format. The definitions will not be used in the roll-n-scroll AMIE-II application and are specific to the GUI environment. As old definitions are retired, it will be retained in the file for historical purposes. This file should remain standardized between all sites and entries not be modified, removed, or added except through patch installation.</p></td>
</tr>
<tr class="odd">
<td><p>396.2</p>
<p>AMIE REPORT</p></td>
<td><p>^DVB(396.2,</p>
<p>File to hold various parameters for specialized reporting in the A.M.I.E. package. Information is deleted as soon as possible.</p>
<p>(This file is used specifically when generating and printing Notices of Discharge).</p></td>
</tr>
<tr class="even">
<td><p>396.3</p>
<p>2507 REQUEST</p></td>
<td><p>^DVB(396.3,</p>
<p>Holds all 2507 requests generated from Regional Office users.</p></td>
</tr>
<tr class="odd">
<td><p>396.4</p>
<p>2507 EXAM</p></td>
<td><p>^DVB(396.4,</p>
<p>This file contains all the exams that are associated with the various 2507 requests.</p></td>
</tr>
<tr class="even">
<td><p>396.5</p>
<p>2507 CANCELLATION REASON</p></td>
<td><p>^DVB(396.5,</p>
<p>This file has all current reasons that a 2507 exam may be cancelled.</p></td>
</tr>
<tr class="odd">
<td><p>396.6</p>
<p>AMIE EXAM</p></td>
<td><p>^DVB(396.6,</p>
<p>Current listing of all valid 2507 exams that may be requested. The exams may be inactivated by the setting of the active/inactive flag. Only the Regional Office may determine if an exam is active or inactive.</p></td>
</tr>
<tr class="even">
<td><p>396.7</p>
<p>2507 BODY SYSTEM</p></td>
<td><p>^DVB(396.7,</p>
<p>Contains all body system names to which the 2507 exams are related.</p></td>
</tr>
<tr class="odd">
<td><p>396.94</p>
<p>2507 INSUFFICIENT REASONS</p></td>
<td><p>^DVB(396.94,</p>
<p>This file has been added for use by the 2507 EXAM File (396.4). It contains the reason an exam is returned by the Regional Office to the Medical Center as 'Insufficient'.</p>
<p>The reasons contained in this file were developed and agreed upon by the AMIE Sub-group of the PII-EP. This information should not be modified by the site.</p></td>
</tr>
<tr class="even">
<td><p>396.95</p>
<p>AMIE C&amp;P EXAM TRACKING</p></td>
<td><p>^DVB(396.95,</p>
<p>This file has been added for use by the 2507 REQUEST File (396.3). It contains information about C&amp;P appointments linked to 2507 Requests.</p>
<p>This file should not be edited via FileMan. The information in this file is crucial to proper calculation of the Average Processing Time on the AMIE AMIS 290.</p></td>
</tr>
<tr class="odd">
<td><p>399</p>
<p>BILLS/CLAIMS</p></td>
<td><p>^DGCR(399,</p>
<p>This file contains all the information necessary to complete a Third Party billing claim form.</p></td>
</tr>
<tr class="even">
<td><p>399.1</p>
<p>MCCR UTILITY</p></td>
<td><p>^DGCR(399.1,</p>
<p>This file contains all of the Occurrence Codes, Discharge Statuses, Discharge Bed sections, and Value Codes that may be used on a Third Party Claim form.</p></td>
</tr>
<tr class="odd">
<td><p>399.2</p>
<p>REVENUE CODE</p></td>
<td><p>^DGCR(399.2,</p>
<p>This file contains all the Revenue Codes that may be used on the Third-Party Claim forms.</p></td>
</tr>
<tr class="even">
<td><p>399.3</p>
<p>RATE TYPE</p></td>
<td><p>^DGCR(399.3,</p>
<p>This file contains all the Rate Types that may be used on the Third-Party Claim forms.</p></td>
</tr>
<tr class="odd">
<td><p>399.4</p>
<p>MCCR INCONSISTENT DATA ELEMENTS</p></td>
<td><p>^DGCR(399.4,</p>
<p>Contains a list of all possible reasons a bill may be disapproved during the authorization phase of the billing process.</p></td>
</tr>
<tr class="even">
<td><p>399.5</p>
<p>BILLING RATES</p></td>
<td><p>^DGCR(399.5,</p>
<p>Contains the historical billing rates associated with revenue codes and specialties for which the DVA has legislative authority to bill third parties for reimbursement. It is used to automatically associate revenue codes, bed sections, and amounts on bills.</p></td>
</tr>
<tr class="odd">
<td><p>399.6</p>
<p>CMN FORM TYPES</p></td>
<td><p>^IBE(399.6,</p>
<p>This file contains the various Certificate of Medical Necessity (CMN) form types and is used in Enter/Edit Billing when the user specifies CMN information for an eligible procedure.</p></td>
</tr>
<tr class="even">
<td><p>409.95</p>
<p>PRINT MANAGER CLINIC SETUP</p></td>
<td><p>^SD(409.95,</p>
<p>This file defines which encounter forms to use for a clinic. It can also be used to define other forms or reports to print, along with the new encounter forms. For each appointment, a packet of forms can be printed, saving the effort of collating the forms manually.</p></td>
</tr>
<tr class="odd">
<td><p>409.96</p>
<p>PRINT MANAGER DIVISION SETUP</p></td>
<td><p>^SD(409.96,</p>
<p>This file allows the user to specify reports or forms that should print in addition to the encounter forms for the entire division. Only reports contained in the PACKAGE INTERFACE file (#357.6) can be specified. The user can ALOS specify the conditions under which the report should print. The intent is to print packets of forms as not to be manually collated.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc127633852" class="anchor"></span>Table : Templates List

\*File contains data that will overwrite existing data.

\*\*File contains data that will merge with existing data.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Template                       | Description                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBCE INSCO ID MAINT            | IB Provider ID Maintenance screen, sets default values for Secondary Provider IDs for CMS-1500 and UB-04 forms. Accessed through Insurance Company Editor.                                                                                                                                                                                                       |
| IBCE PRVPRV MAINT              | Performing Provider IDs in the Insurance Company Editor                                                                                                                                                                                                                                                                                                          |
| IBCE VIEW PREV TRANS1          | Previously transmitted claims list                                                                                                                                                                                                                                                                                                                               |
| IBCE VIEW PREV TRANS2          | Previously transmitted claims list                                                                                                                                                                                                                                                                                                                               |
| IBCE VIEW LOC PRINT            | Protocol List Type. Generates the previously printed claims screen.                                                                                                                                                                                                                                                                                              |
| IBCN INS CO SELECTED           | Protocol List Type. Displays Insurance Companies selected by template IBCN INS CO SELECTOR. Allows users to deselect an Insurance Company.                                                                                                                                                                                                                       |
| IBCN INS CO SELECTOR           | Protocol List Type. Displays Insurance Companies using a variety of user selected filters. Allows user to select and deselect Insurance Companies. It allows filter criteria to be reset and for users to see a complete list of currently selected Insurance Companies.                                                                                         |
| IBCN SUBSCRIBER SELECTED       | Protocol List Type. Displays Subscribers selected by template IBCN SUBSCRIBER SELECTOR. Allows user to deselect a Subscriber.                                                                                                                                                                                                                                    |
| IBCN SUBSCRIBER SELECTOR       | Protocol List Type. Displays a list of Subscribers for a specified group plan using user defined filter. Allows user to select and deselect Subscribers, sort the listed Subscribers and see a complete list of currently selected Subscribers.                                                                                                                  |
| IBCNB INSURANCE BUFFER PAYER   | Protocol List Type. Displays the Payer Summary information for Eligibility Benefits.                                                                                                                                                                                                                                                                             |
| IBCNCH POL COMMENT EXPAND VIEW | Protocol List Type. Displays all the fields of the selected Patient Policy Subscriber comment.                                                                                                                                                                                                                                                                   |
| IBCNCH POLICY COMMENT EXPAND   | Protocol List Type. Displays all the fields of the selected Patient Policy Subscriber comment. Allows the user to edit or delete the comment under specified conditions. New security key ‘IBCN PT POLICY COMNT DELETE’ provides supervisors additional delete capabilities regarding comments.                                                                  |
| IBCNCH POLICY COMMENT HISTORY  | Protocol List Type. Displays all the Patient Policy Comments for a specified patient and policy. Allows the user to add a new comment, expand a comment, search all comments for a specified string, edit a comment and delete a comment. New security key ‘IBCN PT POLICY COMNT DELETE’ provides supervisors additional delete capabilities regarding comments. |
| IBCN POLICY COMMENT SEARCH     | Protocol List Type. Displays Patient Policy Comments for a specified patient and policy that contain a specified string. Allows user to scroll through all comments that contain the string using Next Comment and Previous Comment actions.                                                                                                                     |
| IBCN POLICY COMMENT VIEW       | Protocol List Type. Displays Patient Policy Comments for a specified patient and policy. Allows the user to search all comments for a specified string.                                                                                                                                                                                                          |
| IBCN RDV POL SELECTED          | Protocol List Type. Displays list of selected policies and allows user to deselect policies. Used by the Remote Insurance Inquiry \[IBCN REMOTE INSURANCE QUERY\] option.                                                                                                                                                                                        |
| IBCN RDV SELECTOR              | Protocol List Type. Displays a list of policies from Remote sites. The user can select/deselect policies to be imported. Used by the Remote Insurance Inquiry \[IBCN REMOTE INSURANCE QUERY\] option.                                                                                                                                                            |
| IBCNE ELIGIBILITY/BENEFIT INFO | Protocol List Type. Generates the eIV Elig / Benefit Information screen.                                                                                                                                                                                                                                                                                         |
| IBCNE MEDICARE COB DISPLAY     | Protocol List Type. Generates list of Medicare patients with subsequent insurance.                                                                                                                                                                                                                                                                               |
| IBCNE MEDICARE COB LIST        | Protocol List Type. Generates list of Medicare patients with subsequent insurance and enables patient selection.                                                                                                                                                                                                                                                 |
| IBCNS INSURANCE COMPANY        | Insurance Company Editor                                                                                                                                                                                                                                                                                                                                         |
| IBCNS PLAN SELECTOR            | Insurance Plan Lookup                                                                                                                                                                                                                                                                                                                                            |
| IBCNS POLICIES SELECTED        | Selected Policies                                                                                                                                                                                                                                                                                                                                                |
| IBCNSC INSURANCE CO ADDRESSES  | Insurance Company Editor claims mailing addresses                                                                                                                                                                                                                                                                                                                |
| IBJP ADMIN CONTRACTOR COM      | Protocol List Type. Generates the Commercial Alt Primary Payer ID Types screen.                                                                                                                                                                                                                                                                                  |
| IBJP ADMIN CONTRACTOR MED      | Protocol List Type. Generates the Medicare Alt Primary Payer ID Types screen.                                                                                                                                                                                                                                                                                    |
| IBJP IB REVENUE CODES          | Protocol List Type. Generates the Excluded Revenue Codes screen.                                                                                                                                                                                                                                                                                                 |
| IBJP CLAIMS TRACKING           | Protocol List Type. Generates the Claims Tracking Parameter screen.                                                                                                                                                                                                                                                                                              |
| IBJP HCSR ADM INSCO            | Protocol List Type. Generates the HCSR Insurance Exclusions screen.                                                                                                                                                                                                                                                                                              |
| IBJP HCSR APPT INSCO           | Protocol List Type. Generates the HCSR Insurance Exclusions screen.                                                                                                                                                                                                                                                                                              |
| IBJP HCSR CLINICS              | Protocol List Type. Generates the HCSR Clinics Inclusions screen.                                                                                                                                                                                                                                                                                                |
| IBJP HCSR PARAMETERS           | Protocol List Type. Generates the HCSR Parameters screen.                                                                                                                                                                                                                                                                                                        |
| IBJP HCSR WARDS                | Protocol List Type. Generates the HCSR Wards Exclusions screen.                                                                                                                                                                                                                                                                                                  |
| IBJP IB NON-MCCF RATE TYPES    | Protocol List Type. Allows user to define what a NON-MCCF RATE TYPE is in the IB Site Parameters.                                                                                                                                                                                                                                                                |
| IBJP IB PAY-TO PROVIDERS       | Protocol List Type. Displays list of Pay-to Providers defined under IB Site Parameters; allows user to add, edit, and delete Pay-to Providers; allows user to go to Pay-to Associations.                                                                                                                                                                         |
| IBJP IB PAY-TO ASSOCIATIONS    | Protocol List Type. Displays Divisions associated with each Pay-to Provider; allows user to add, edit, and delete associations.                                                                                                                                                                                                                                  |
| IBJP IB TRICARE PAY-TO PROVS   | Protocol List Type. Displays list of TRICARE-specific Pay-to Providers defined under IB Site Parameters; allows user to add, edit, delete TRICARE-specific Pay-to Providers; allows user to go to TRICARE-specific Pay-to Associations.                                                                                                                          |
| IBJP IB TRICARE PAY-TO ASSOCS  | Protocol List Type. Displays Divisions associated with each TRICARE-specific Pay-to Provider; allows user to add, edit, and delete associations.                                                                                                                                                                                                                 |
| IBJP IIV SITE PARAMETERS       | Protocol List Type. Displays the IV Site Parameters.                                                                                                                                                                                                                                                                                                             |
| IBJPS CMN CPTS                 | Protocol List Type. Displays a list of CPT codes / descriptions under “IB Site Parameters” for which the user should be prompted for Certificate of Medical Necessity (CMN) info and allows user to add additional CPTs.                                                                                                                                         |
| IBJT ACTIVE LIST               | Third Party Joint inquiry – active bills                                                                                                                                                                                                                                                                                                                         |
| IBJT INACTIVE LIST             | Third Party Joint inquiry – inactive bills                                                                                                                                                                                                                                                                                                                       |
| IBRFI 277 DETAIL WL            | Protocol List Type. Generates the RFAI Message Detail screen.                                                                                                                                                                                                                                                                                                    |
| IBRFI 277 WL                   | Protocol List Type. Displays the RFAI Management Worklist.                                                                                                                                                                                                                                                                                                       |
| IBRFI COMMENTS                 | Protocol List Type. Displays the RFAI Claim Comment History.                                                                                                                                                                                                                                                                                                     |
| IBT CLAIMS TRACKING EDITOR     | Protocol List Type. Generates the Claims Tracking Editor screen.                                                                                                                                                                                                                                                                                                 |
| IBT COMMUNICATIONS EDITOR      | Protocol List Type. Generates the Insurance Reviews / Contacts screen.                                                                                                                                                                                                                                                                                           |
| IBT HCSR ENTRY                 | Protocol List Type. Generates the HCSR Expanded Entry screen.                                                                                                                                                                                                                                                                                                    |
| IBT HCSR RESPONSE VIEW         | Display List Type. Generates the HCSR Response View screen.                                                                                                                                                                                                                                                                                                      |
| IBT HCSR RESPONSE WORKLIST     | Protocol List Type. Generates the HCSR Response Worklist screen.                                                                                                                                                                                                                                                                                                 |
| IBT HCSR SEND 278 SHORT        | Protocol List Type. Generates the HCSR 278 Send screen.                                                                                                                                                                                                                                                                                                          |
| IBT HCSR WORKLIST              | Protocol List Type. Generates the HCSR Worklist screen.                                                                                                                                                                                                                                                                                                          |
| IBJT 835 EEOB PRINT            | Protocol List Type. Generates the TPJI ERA /835 Print EEOB Information Screen, which displays detailed EEOB data.                                                                                                                                                                                                                                                |
| IBJT ADDITIONAL 835 DATA       | Protocol List Type. Generates the TPJI ERA / 835 Additional Information Screen, which display additional payer and contact information in the 835 transaction.                                                                                                                                                                                                   |
| IBJT ERA 835 INFORMATION       | Protocol List Type. Generates the TPJI ERA/835 Information Screen, which display Electronic Remittance Advice / 835 information.                                                                                                                                                                                                                                 |

<span id="_Toc127633853" class="anchor"></span>Table : Input Templates

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633854" class="anchor"></span>Table : Sort Templates</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE#</th>
<th>TEMPLATE</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td>IBCN PATIENT INSURANCE</td>
<td>New input template to handle the input/edit of fields in the patient insurance multiple (2.312) in the patient file.</td>
</tr>
<tr class="even">
<td>36</td>
<td>IBEDIT INS CO1</td>
<td>Edits INSURANCE COMPANY file from Insurance Company Edit option.</td>
</tr>
<tr class="odd">
<td>350.9</td>
<td>IB EDIT CLEAR</td>
<td>Clear Integrated Billing Filer Parameters.</td>
</tr>
<tr class="even">
<td>350.9</td>
<td>IB EDIT MCCR PARM</td>
<td>Enter / edit MCCR Site Parameters.</td>
</tr>
<tr class="odd">
<td>350.9</td>
<td>IB EDIT SITE PARAM</td>
<td>Enter / edit Integrated Billing Site Parameters.</td>
</tr>
<tr class="even">
<td>350.9</td>
<td>IBCNE GENERAL PARAMETER EDIT</td>
<td>Enter / edit the editable General Parameters related to the Ins. Verification Site Parameters.</td>
</tr>
<tr class="odd">
<td>350.9</td>
<td>IBCNF EDIT CONFIGURATION</td>
<td>Edits the eII configuration parameter fields in IB SITE PARAMETERS (#350.9); it is called from IBCNFCON routine.</td>
</tr>
<tr class="even">
<td>351</td>
<td>IB BILLING CYCLE ADD</td>
<td>Patient Billing Clock Maintenance, new entry.</td>
</tr>
<tr class="odd">
<td>351</td>
<td>IB BILLING CYCLE ADJUST</td>
<td>Patient Billing Clock Maintenance, edit existing entry.</td>
</tr>
<tr class="even">
<td>351.61</td>
<td>IBAT OUT PRICING EDIT</td>
<td><p>PROCEDURES</p>
<ul>
<li><blockquote>
<p>PROCEDURES</p>
</blockquote></li>
<li><blockquote>
<p>D CPTDSP^IBATLM2B(X)</p>
</blockquote></li>
<li><blockquote>
<p>QUANTITY</p>
</blockquote></li>
<li><blockquote>
<p>PROCEDURE COST</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>353</td>
<td>IB DEVICE</td>
<td>Bill Form Print Device Setup</td>
</tr>
<tr class="even">
<td>353</td>
<td>IBCE ADD/EDIT LOCAL FORM</td>
<td><p>NAME</p>
<p>FORM LENGTH</p>
<p>ENTRY PRE-PROCESSOR</p>
<p>ENTRY POST-PROCESSOR</p>
<p>EXTRACT CODE</p>
<p>OUTPUT CODE</p>
<p>FORM PRE-PROCESSOR</p>
<p>FORM POST-PROCESSOR</p>
<p>FIELD DELIMITER</p>
<p>SHORT DESCRIPTION</p></td>
</tr>
<tr class="odd">
<td>354</td>
<td>IB CURRENT STATUS</td>
<td>Updates the current status in the BILLING PATIENT file whenever a new exemption is created.</td>
</tr>
<tr class="even">
<td>354.1</td>
<td>IB INACTIVATE EXEMPTION</td>
<td>Inactivates actives exemptions. Only one exemption for a date may be active.</td>
</tr>
<tr class="odd">
<td>354.1</td>
<td>IB NEW EXEMPTION</td>
<td>Updates new exemptions in the BILLING Exemptions file.</td>
</tr>
<tr class="even">
<td>354.3</td>
<td>IB ENTER THRESHOLD</td>
<td>Enter new income thresholds.</td>
</tr>
<tr class="odd">
<td>355.4</td>
<td>IBCN AB ADD COM</td>
<td>Allows editing of Annual Benefits comments.</td>
</tr>
<tr class="even">
<td>355.4</td>
<td>IBCN AB EDIT ALL</td>
<td>Allows editing of all Annual Benefits fields.</td>
</tr>
<tr class="odd">
<td>355.4</td>
<td>IBCN AB HOME HEA</td>
<td>Allows editing of the Home Health section of ANNUAL BENEFITS.</td>
</tr>
<tr class="even">
<td>355.4</td>
<td>IBCN AB HOSPC</td>
<td>Allows editing of the Hospice section of ANNUAL BENEFITS.</td>
</tr>
<tr class="odd">
<td>355.4</td>
<td>IBCN AB INPT</td>
<td>Allows editing of the Inpatient section of ANNUAL BENEFITS.</td>
</tr>
<tr class="even">
<td>355.4</td>
<td>IBCN AB IV MGMT</td>
<td>Allows editing of the IV Mgmt section of ANNUAL BENEFITS.</td>
</tr>
<tr class="odd">
<td>355.4</td>
<td>IBCN AB MEN H</td>
<td>Allows editing of the Mental Health section of ANNUAL BENEFITS.</td>
</tr>
<tr class="even">
<td>355.4</td>
<td>IBCN AB OPT</td>
<td>Allows editing of the Outpatient section of ANNUAL BENEFITS.</td>
</tr>
<tr class="odd">
<td>355.4</td>
<td>IBCN AB POL INF</td>
<td>Allows editing of the Policy Information section of ANNUAL BENEFITS.</td>
</tr>
<tr class="even">
<td>355.4</td>
<td>IBCN AB REHAB</td>
<td>Allows editing of the Rehab section of ANNUAL BENEFITS.</td>
</tr>
<tr class="odd">
<td>355.5</td>
<td>IBCN BU ADD COM</td>
<td>Allows editing of the Comments in BENEFITS USED.</td>
</tr>
<tr class="even">
<td>355.5</td>
<td>IBCN BU ED AL</td>
<td>Allows editing of all BENEFITS USED fields.</td>
</tr>
<tr class="odd">
<td>355.5</td>
<td>IBCN BU INPT</td>
<td>Allows editing of the Inpatient section of BENEFITS USED.</td>
</tr>
<tr class="even">
<td>355.5</td>
<td>IBCN BU OPT</td>
<td>Allows editing of the Outpatient section of BENEFITS USED.</td>
</tr>
<tr class="odd">
<td>355.5</td>
<td>IBCN BU POL</td>
<td>Allows editing of the Policy section of BENEFITS USED.</td>
</tr>
<tr class="even">
<td>356</td>
<td>IBT ASSIGN CASE</td>
<td>Allows assigning a case to a reviewer.</td>
</tr>
<tr class="odd">
<td>356</td>
<td>IBT BILLLING INFO</td>
<td>Allows editing of billing information in Claims Tracking.</td>
</tr>
<tr class="even">
<td>356</td>
<td>IBT PRECERT INFO</td>
<td>Allows editing of pre-certification information in Claims Tracking.</td>
</tr>
<tr class="odd">
<td>356</td>
<td>IBT QUICK EDIT</td>
<td>Allows editing of necessary fields for a visit in Claims Tracking.</td>
</tr>
<tr class="even">
<td>356</td>
<td>IBT STATUS CHANGE</td>
<td>Allows changing status of a visit in Claims Tracking.</td>
</tr>
<tr class="odd">
<td>356</td>
<td>IBT UR INFO</td>
<td>Edit field used to determine which cases require which types of reviews.</td>
</tr>
<tr class="even">
<td>356.1</td>
<td>IBT ADD COMMENTS</td>
<td>Edits COMMENTS field of HOSPITAL REVIEW file (#356.1).</td>
</tr>
<tr class="odd">
<td>356.1</td>
<td>IBT REMOVE NEXT REVIEW</td>
<td>Deletes next review date.</td>
</tr>
<tr class="even">
<td>356.1</td>
<td>IBT REVIEW INFO</td>
<td>Edits REVIEW INFORMATION field.</td>
</tr>
<tr class="odd">
<td>356.1</td>
<td>IBT SPECIAL UNIT</td>
<td>Edits Special Units si / is fields.</td>
</tr>
<tr class="even">
<td>356.1</td>
<td>IBT STATUS CHANGE</td>
<td>Edits STATUS field.</td>
</tr>
<tr class="odd">
<td>356.19</td>
<td>IBT AVERAGE BILL AMOUNTS (12M)</td>
<td><p>NO. INPT INST. CLAIMS (12M)</p>
<p>AMT INPT INST. CLAIMS (12M)</p>
<p>NO. INPT EPISODES/INST. (12M)</p>
<p>NO. INPT PROF. CLAIMS (12M)</p>
<p>AMT INPT PROF. CLAIMS (12M)</p>
<p>NO. INPT EPISODES/PROF. (12M)</p>
<p>DATE UPDATED (12M)</p></td>
</tr>
<tr class="even">
<td>356.19</td>
<td>IBT AVERAGE BILL AMOUNTS (MON)</td>
<td><p>NO. INPT INST. CLAIMS (MON)</p>
<p>AMT INPT INST. CLAIMS (MON)</p>
<p>NO. INPT EPISODES/INST. (MON)</p>
<p>NO. INPT PROF. CLAIMS (MON)</p>
<p>AMT INPT PROF. CLAIMS (MON)</p>
<p>NO. INPT EPISODES/PROF. (MON)</p>
<p>DATE UPDATED (MON)</p></td>
</tr>
<tr class="odd">
<td>356.19</td>
<td>IBT UNBILLED AMOUNTS</td>
<td><p>EPISODES MISSING INST CLAIMS</p>
<p>EPISODES MISSING PROF CLAIMS</p>
<p>ENCOUNTERS MISSING CLAIMS</p>
<p>CPT CODES MISSING INST CLAIMS</p>
<p>CPT CODES MISSING PROF CLAIMS</p>
<p>NUMBER OF UNBILLED RX'S</p>
<p>UNBILLED INPATIENT AMOUNT</p>
<p>UNBILLED OUTPATIENT AMOUNT</p>
<p>UNBILLED RX AMOUNT</p>
<p>TOTAL UNBILLED AMOUNT</p>
<p>NO. MRA INPT INST CLAIMS</p>
<p>NO. MRA INPT PROF CLAIMS</p>
<p>MRA CPT CODES ON INST CLAIMS</p>
<p>MRA CPT CODES ON PROF CLAIMS</p>
<p>NUMBER OF MRA UNBILLED RX'S</p>
<p>MRA UNBILLED INPATIENT AMOUNT</p>
<p>MRA UNBILLED OUTPATIENT AMOUNT</p>
<p>MRA UNBILLED PRESCRIPTION AMT</p>
<p>TOTAL MRA UNBILLED AMOUNT</p>
<p>2.11</p></td>
</tr>
<tr class="even">
<td>356.2</td>
<td>IBT ACTION INFO</td>
<td>Allows editing of specific field relative to an Action.</td>
</tr>
<tr class="odd">
<td>356.2</td>
<td>IBT ADD APPEAL</td>
<td>Edits Appeal information.</td>
</tr>
<tr class="even">
<td>356.2</td>
<td>IBT APPEAL INFO</td>
<td>Allows editing of Appeal Address in File #36.</td>
</tr>
<tr class="odd">
<td>356.2</td>
<td>IBT COMMENT INFO</td>
<td>Edits COMMENTS fields.</td>
</tr>
<tr class="even">
<td>356.2</td>
<td>IBT CONTACT INFO</td>
<td>Edits Contact information.</td>
</tr>
<tr class="odd">
<td>356.2</td>
<td>IBT FINAL OUTCOME</td>
<td>Allows specifying outcome of an appeal.</td>
</tr>
<tr class="even">
<td>356.2</td>
<td>IBT INS VERIFICATION</td>
<td>Allows insurance verifiers to edit specific contact information from Insurance Mgmt.</td>
</tr>
<tr class="odd">
<td>356.2</td>
<td>IBT INSURANCE INFO</td>
<td>Edits the Appeals Address in the INSURANCE COMPANY file (#36).</td>
</tr>
<tr class="even">
<td>356.2</td>
<td>IBT QUICK EDIT</td>
<td>Used to add/edit a new review.</td>
</tr>
<tr class="odd">
<td>356.2</td>
<td>IBT REMOVE NEXT REVIEW</td>
<td>Deletes next review data.</td>
</tr>
<tr class="even">
<td>356.2</td>
<td>IBT STATUS CHANGE</td>
<td>Edits INSURANCE REVIEW STATUS field.</td>
</tr>
<tr class="odd">
<td>356.22</td>
<td>IB ADD/EDIT 278</td>
<td>Used to create / Edit a 278 request for a selected HCSR Worklist event.</td>
</tr>
<tr class="even">
<td>356.22</td>
<td>IB CREATE 278 REQUEST</td>
<td>Used to create / Edit a 278 request for a selected HCSR Worklist event.</td>
</tr>
<tr class="odd">
<td>356.22</td>
<td>IB CREATE 278 REQUEST SHORT</td>
<td>Used to create / Edit a 278 request for a selected HCSR Worklist event.</td>
</tr>
<tr class="even">
<td>357</td>
<td>IBDF EDIT NEW FORM</td>
<td>Used to edit a new form.</td>
</tr>
<tr class="odd">
<td>357</td>
<td>IBDF EDIT OLD OR COPIED FORM</td>
<td>Used to edit an existing form.</td>
</tr>
<tr class="even">
<td>357.1</td>
<td>IBDF EDIT HEADER &amp; OUTLINE</td>
<td>Used to edit a block's header and outline.</td>
</tr>
<tr class="odd">
<td>357.1</td>
<td>IBDF EDIT HEADER BLOCK</td>
<td>Used to edit the header block of a form.</td>
</tr>
<tr class="even">
<td>357.1</td>
<td>IBDF NEW EMPTY BLOCK</td>
<td>Used to edit the header, position, outline, and other characteristics of a new block.</td>
</tr>
<tr class="odd">
<td>357.1</td>
<td>IBDF POSITION COPIED BLOCK</td>
<td>Used to position a copied block onto a form.</td>
</tr>
<tr class="even">
<td>357.2</td>
<td>IBDF EDIT SELECTION LIST</td>
<td>Used to edit a selection list, except for the position and size of the columns.</td>
</tr>
<tr class="odd">
<td>357.2</td>
<td>IBDF POSITION/SIZE COLUMNS</td>
<td>Used to edit the size and position of a selection list's columns.</td>
</tr>
<tr class="even">
<td>357.3</td>
<td>IBDF CPT MODIFIER</td>
<td><p>CPT MODIFIER</p>
<ul>
<li><blockquote>
<p>ALL</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>357.3</td>
<td>IBDF EDIT PLACE HOLDER</td>
<td><p>PRINT ORDER WITHIN GROUP</p>
<p>PLACE HOLDER TEXT</p>
<p>USE AS SUBHEADER?</p></td>
</tr>
<tr class="even">
<td>357.3</td>
<td>IBDF EDIT SELECTION</td>
<td>Used to edit a selection.</td>
</tr>
<tr class="odd">
<td>357.5</td>
<td>IBDF EDIT DATA FIELD</td>
<td>Used to edit a data field.</td>
</tr>
<tr class="even">
<td>357.5</td>
<td>IBDF EDIT FORM HEADER</td>
<td>Used to edit the form header data field.</td>
</tr>
<tr class="odd">
<td>357.5</td>
<td>IBDF EDIT LABEL FIELD</td>
<td><p>NAME</p>
<p>BLOCK</p>
<p>TYPE OF DATA</p>
<p>SUBFIELD</p>
<ul>
<li><blockquote>
<p>SUBFIELD LABEL</p>
</blockquote></li>
<li><blockquote>
<p>STARTING ROW FOR LABEL</p>
</blockquote></li>
<li><blockquote>
<p>STARTING COLUMN FOR LABEL</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>357.6</td>
<td>IBDF EDIT AVAILABLE HLTH SMRY</td>
<td>Used to define a package interface that prints a Health Summary.</td>
</tr>
<tr class="odd">
<td>357.6</td>
<td>IBDF EDIT AVAILABLE REPORT</td>
<td>Used to define a package interface that prints a report other than a Health Summary.</td>
</tr>
<tr class="even">
<td>357.6</td>
<td>IBDF EDIT OUTPUT/SELECTION RTN</td>
<td>Used to define a package interface of the type output routine or selection routine.</td>
</tr>
<tr class="odd">
<td>357.69</td>
<td>IB EDIT E&amp;M QUANTITY</td>
<td>Allow quantity greater than 1</td>
</tr>
<tr class="even">
<td>357.7</td>
<td>IBDF FORM LINE</td>
<td>Used to edit a line.</td>
</tr>
<tr class="odd">
<td>357.8</td>
<td>IBDF EDIT TEXT AREA</td>
<td>Used to edit a text area.</td>
</tr>
<tr class="even">
<td>357.91</td>
<td>IBDF EDIT MARKING AREA</td>
<td>Used to edit a marking area.</td>
</tr>
<tr class="odd">
<td>357.93</td>
<td>IBDF EDIT MULT CHOICE FIELD</td>
<td><p>NAME</p>
<p>BLOCK</p>
<p>SELECTION RULE</p>
<p>CHOICE</p>
<ul>
<li><blockquote>
<p>ID</p>
</blockquote></li>
<li><blockquote>
<p>DATA QUALIFIER</p>
</blockquote></li>
<li><blockquote>
<p>CHOICE LABEL</p>
</blockquote></li>
<li><blockquote>
<p>STARTING COLUMN FOR LABEL</p>
</blockquote></li>
<li><blockquote>
<p>STARTING ROW FOR LABEL</p>
</blockquote></li>
<li><blockquote>
<p>BUBBLE COLUMN</p>
</blockquote></li>
<li><blockquote>
<p>BUBBLE ROW</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>357.94</td>
<td>IBDF EDIT PRINTER</td>
<td><p>TERMINAL TYPE</p>
<p>PRINTER LANGUAGE TYPE</p>
<p>SIMPLEX</p>
<p>DUPLEX, LONG-EDGE BINDING</p>
<p>DUPLEX, SHORT-EDGE BINDING</p>
<p>TCP PRINTER</p></td>
</tr>
<tr class="odd">
<td>357.96</td>
<td>IBD CREATE FORM TRACKING</td>
<td><p>PATIENT</p>
<p>APPOINTMENT</p>
<p>FORM TYPE</p>
<p>DATE/TIME PRINTED</p>
<p>SOURCE OF FORM ID</p>
<p>FORM TYPE ID (EXTERNAL SOURCE) EXTERNAL PRINTED FORM ID</p>
<p>CLINIC</p>
<p>PROCESSING STATUS</p>
<p>NO APPOINTMENT ENTRY</p></td>
</tr>
<tr class="even">
<td>357.96</td>
<td>IBD EDIT FORM TRACKING STATUS</td>
<td><p>DATE/TIME RECEIVED IN DHCP</p>
<p>PROCESSING STATUS</p>
<p>ERROR</p></td>
</tr>
<tr class="odd">
<td>359.94</td>
<td>IBDF EDIT HAND PRINT FIELD</td>
<td><p>NAME</p>
<p>BLOCK</p>
<p>DHCP DATA ELEMENT</p>
<p>LABEL</p>
<p>LABEL APPEARANCE</p></td>
</tr>
<tr class="even">
<td>364.5</td>
<td>IBCE DEFINE LOCAL ELEMENT</td>
<td><p>NAME</p>
<p>SECURITY LEVEL</p>
<p>BASE FILE</p>
<p>TYPE OF ELEMENT</p>
<p>ELEMENT CATEGORY</p>
<p>ELEMENT CATEGORY</p>
<p>FILEMAN FIELD REFERENCE</p>
<p>FILEMAN RETURN FORMAT</p>
<p>CONSTANT VALUE</p>
<p>EXTRACT CODE</p>
<p>ARRAY ROOT</p>
<p>DESCRIPTION</p></td>
</tr>
<tr class="odd">
<td>364.6</td>
<td>IBCE ADD/EDIT LOCAL FORM FIELD</td>
<td><p>CALCULATE ONLY OR OUTPUT</p>
<p>PAGE OR SEQUENCE</p>
<p>FIRST LINE NUMBER</p>
<p>STARTING COLUMN OR PIECE</p>
<p>MAX NUMBER LINES</p>
<p>LENGTH</p>
<p>LOCAL OVERRIDE ALLOWED</p>
<p>SHORT DESCRIPTION</p>
<p>CALCULATE ONLY OR OUTPUT</p></td>
</tr>
<tr class="even">
<td>364.7</td>
<td>IBCE EDIT FIELD CONTENT</td>
<td><p>SECURITY LEVEL</p>
<p>DATA ELEMENT</p>
<p>EDIT STATUS</p>
<p>EDIT GROUP NUMBER</p>
<p>SCREEN PROMPT</p>
<p>FORMAT CODE</p>
<p>INSURANCE COMPANY</p>
<p>BILL TYPE</p>
<p>PAD CHARACTER</p>
<p>FORMAT CODE DESCRIPTION</p></td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB MAIL</td>
<td>Enter / edit a bill's mailing address.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB REVCODE EDIT</td>
<td>Enter / Edit a bill's revenue code information.</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB SCREEN1</td>
<td>Enter / Edit billing screen 1, demographic information.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB SCREEN10</td>
<td>Enter / edit billing screen 10</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB SCREEN102</td>
<td>Enter / edit billing screen 10</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB SCREEN10H</td>
<td>Enter / edit billing screen 10</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB SCREEN2</td>
<td>Enter / edit billing screen 2, employment information.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB SCREEN3</td>
<td>Enter / edit billing screen 3, payer information.</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB SCREEN4</td>
<td>Enter / edit billing screen 4, inpatient event information.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB SCREEN5</td>
<td>Enter / edit billing screen 5, outpatient event information.</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB SCREEN6</td>
<td>Enter / Edit billing screen 6, inpatient general billing information.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB SCREEN7</td>
<td>Enter / edit billing screen 7, outpatient general billing information.</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB SCREEN8</td>
<td>Enter / Edit UB-82 billing screen 8, billing specific information.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB SCREEN82</td>
<td>Enter / edit UB-92 billing screen 8, bill specific information.</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB SCREEN8H</td>
<td>Enter / Edit HCFA 1500 billing screen 8, billing specific information.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB SCREEN9</td>
<td>Ambulance Information.</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB STATUS</td>
<td>Edit a bill's status.</td>
</tr>
<tr class="even">
<td>399.2</td>
<td>IB ACTIVATE</td>
<td>Activate / inactivate revenue codes.</td>
</tr>
<tr class="odd">
<td>399.3</td>
<td>IB RATE EDIT</td>
<td>Update RATE TYPE file (#399.3).</td>
</tr>
<tr class="even">
<td>409.95</td>
<td>IBDF PRINT MANAGER</td>
<td>Defines reports and encounter forms to clinic.</td>
</tr>
<tr class="odd">
<td>409.96</td>
<td>IBDF PRINT MANAGER</td>
<td>Defines reports and encounter forms to division.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633854" class="anchor"></span>Table : Sort Templates

### Sort Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633855" class="anchor"></span>Table : Print Templates</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE#</th>
<th>TEMPLATE</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td>IBNOTVER, IBNOTVER1</td>
<td>Lists new, not verified insurance entries.</td>
</tr>
<tr class="even">
<td>36</td>
<td>IB INACTIVE INS CO</td>
<td>List of inactive insurance companies covering patients.</td>
</tr>
<tr class="odd">
<td>335.93</td>
<td>IB PROVIDERS FROM FB</td>
<td>List of records that have been affected by FB PAID TO IB automatic interface (For Future Use to Validate Testing).</td>
</tr>
<tr class="even">
<td>350</td>
<td>IB INCOMPLETE</td>
<td>Integrated Billing Action List of entries with a status of INCOMPLETE.</td>
</tr>
<tr class="odd">
<td>351.71</td>
<td>IBJD DM REPT SORT</td>
<td><p>SORT BY: MONTH</p>
<p>From: OCT 2003</p>
<p>To: OCT 2003</p>
<p>ASK range of values</p>
<ul>
<li><blockquote>
<p>WITHIN MONTH, SORT BY: REPORT</p>
</blockquote></li>
<li><blockquote>
<p>REPORT SUB-FIELD: STATUS</p>
</blockquote></li>
<li><blockquote>
<p>From: 1</p>
</blockquote></li>
<li><blockquote>
<p>To: 2</p>
</blockquote></li>
<li><blockquote>
<p>ASK range of values</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>354</td>
<td>IB BILLING PAT W/INCOME</td>
<td>List of patients with a "No Income Data" exemption.</td>
</tr>
<tr class="odd">
<td>354</td>
<td>IB BILLING PATIENT BY REASON</td>
<td>List of currently exempt patients by reason.</td>
</tr>
<tr class="even">
<td>354</td>
<td>IB BILLING PATIENT BY STATUS</td>
<td>List of currently exempt patients by status.</td>
</tr>
<tr class="odd">
<td>354</td>
<td>IB EXEMPT PATIENTS</td>
<td>List of exempt patients.</td>
</tr>
<tr class="even">
<td>354</td>
<td>IB EXEMPTION LETTER</td>
<td>Stores results of search when printing exemption letters.</td>
</tr>
<tr class="odd">
<td>354.3</td>
<td>IB PRINT THRESHOLD</td>
<td>List of thresholds.</td>
</tr>
<tr class="even">
<td>356</td>
<td>IBT LIST VISITS</td>
<td>Lists visits in Claims Tracking by date and type. Primarily list random sample cases.</td>
</tr>
<tr class="odd">
<td>357.6</td>
<td>IBD PRIM CARE SEARCH</td>
<td>List of new primary care interfaces for patch.</td>
</tr>
<tr class="even">
<td>357.96</td>
<td>IBD NO APPOINTMENT LIST</td>
<td>This template with list patients for a date range that have had encounter forms printed that are not related to appointments.</td>
</tr>
<tr class="odd">
<td>359.3</td>
<td>IBD LIST ERRORS</td>
<td><p>SORT BY: '@ERROR DATE/TIME</p>
<p>From:</p>
<p>To:</p>
<p>WITHIN ERROR DATE/TIME, SORT BY: #USER</p>
<p>From:</p>
<p>To:</p>
<p>WITHIN USER, SORT BY: PATIENT</p>
<p>From: @</p>
<p>To:</p>
<p>Do NOT ask range of values</p>
<p>WITHIN PATIENT, SORT BY:</p>
<p>ENCOUNTER DATE/TIME;S1</p>
<p>From: @</p>
<p>To:</p>
<p>Do NOT ask range of values</p></td>
</tr>
<tr class="even">
<td>362.1</td>
<td>IB AB COMMENTS</td>
<td>Automated Biller Error / Comments Report.</td>
</tr>
<tr class="odd">
<td>364.6</td>
<td>IBCE LOCAL DATA ELEMENTS</td>
<td>This sort template will allow for the printing of local form override data.</td>
</tr>
<tr class="even">
<td>399</td>
<td>IB CLK PROD</td>
<td>Clerk Productivity Report.</td>
</tr>
<tr class="odd">
<td>399.5</td>
<td>IB BILLING RATES</td>
<td>Billing Rates List.</td>
</tr>
<tr class="even">
<td>8994</td>
<td>IBD RPC LIST</td>
<td>AICS Remote Procedure List.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633855" class="anchor"></span>Table : Print Templates

### Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633856" class="anchor"></span>Table : File Flow</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 35%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE#</th>
<th>TEMPLATE</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td>IB NOTVER</td>
<td>Lists new, not verified insurance entries.</td>
</tr>
<tr class="even">
<td>36</td>
<td>IB INACTIVE INS CO</td>
<td>List of inactive insurance companies shown in the system as still providing patient coverage.</td>
</tr>
<tr class="odd">
<td>40.8</td>
<td>IB DIVISION DISPLAY</td>
<td>Displays wage rates and locality modifier data for a division.</td>
</tr>
<tr class="even">
<td>350</td>
<td>IB INCOMPLETE</td>
<td>Integrated Billing Action List of entries with status of INCOMPLETE.</td>
</tr>
<tr class="odd">
<td>350</td>
<td>IB LIST</td>
<td>Integrated Billing Action List.</td>
</tr>
<tr class="even">
<td>350.41</td>
<td>IB CPT UPDATE ERROR</td>
<td>Update Billable Ambulance Surgery Transfer Error List Report.</td>
</tr>
<tr class="odd">
<td>350.6</td>
<td>IB PURGE LIST LOG ENTRIES</td>
<td>Displays log entries from the IB Archive Purge Log.</td>
</tr>
<tr class="even">
<td>350.7</td>
<td>IB CPT PG DISPLAY</td>
<td>Displays a Check-off Sheet's line format and associated sub headers.</td>
</tr>
<tr class="odd">
<td>350.71</td>
<td>IB CPT CP DISPLAY</td>
<td>Displays procedures associated with a particular Check-off Sheet sub header.</td>
</tr>
<tr class="even">
<td>351</td>
<td>IB BILLING CLOCK HEADER</td>
<td>Displays the header for the Patient Billing Clock Inquiry.</td>
</tr>
<tr class="odd">
<td>351</td>
<td>IB BILLING CLOCK INQ</td>
<td>Displays the Patient Billing Clock Inquiry data.</td>
</tr>
<tr class="even">
<td>351.71</td>
<td>IBJD DM REPT PRINT</td>
<td></td>
</tr>
<tr class="odd">
<td>351.71</td>
<td>IBJD DM V/P EXTRACTS</td>
<td></td>
</tr>
<tr class="even">
<td>352.1</td>
<td>IB APPOINTMENT TYPE</td>
<td>Billable Appointment Type List.</td>
</tr>
<tr class="odd">
<td>354</td>
<td>IB BILLING PAT W/INCOME</td>
<td>Used when producing a list of nonexempt patients with no income data.</td>
</tr>
<tr class="even">
<td>354</td>
<td>IB BILLING PATIENT</td>
<td>Prints the exemption reason reports with the detailed patient listing.</td>
</tr>
<tr class="odd">
<td>354</td>
<td>IB BILLING PATIENT SUMMARY</td>
<td>Prints the exemption reason reports that do not include the detailed patient listing.</td>
</tr>
<tr class="even">
<td>354</td>
<td>IB DO NOT USE</td>
<td>Creates results of IB EXEMPTION LETTER sort template.</td>
</tr>
<tr class="odd">
<td>354</td>
<td>IB PATIENT ADDRESSES</td>
<td>For local use, contains patient names and addresses.</td>
</tr>
<tr class="even">
<td>354.3</td>
<td>IB PRINT THRESHOLD</td>
<td>Prints a list of entries from the BILLING THRESHOLDS file (#354.3).</td>
</tr>
<tr class="odd">
<td>356</td>
<td>IB LIST VISITS</td>
<td>Lists visits in Claims Tracking. Primarily to list random sample cases.</td>
</tr>
<tr class="even">
<td>356</td>
<td>IBT LIST VISITS</td>
<td><p>PATIENT;L20</p>
<p>PATIENT:</p>
<ul>
<li><blockquote>
<p>PRIMARY LONG ID;"PT. ID";L13</p>
</blockquote></li>
<li><blockquote>
<p>WARD LOCATION;L10;"WARD"</p>
</blockquote></li>
</ul>
<p>EVENT TYPE:</p>
<ul>
<li><blockquote>
<p>ABBREVIATION;"VISIT TYPE"</p>
</blockquote></li>
</ul>
<p>DATE(EPISODE DATE);"DATE";L11</p>
<p>TRACKED AS INSURANCE CLAIM?;"INS. CASE";L4</p>
<p>TRACKED AS RANDOM SAMPLE?;"RANDOM CASE"</p>
<p>TRACKED AS SPECIAL CONDITION;"SPECIAL COND."</p>
<p>TRACKED AS A LOCAL ADDITION?;"LOCAL CASE"</p>
<p>HOSPITAL REVIEWS ASSIGNED TO;L12;"HOSP REVIEWER"</p>
<p>INS. REVIEWS ASSIGNED TO;L12;"INS REVIEWER"</p></td>
</tr>
<tr class="odd">
<td>356</td>
<td>IBT QUICK REV CODING STAT</td>
<td><p>PATIENT</p>
<p>PATIENT:SSN;"SSN"</p>
<p>OUTPATIENT ENCOUNTER:LOCATION;"LOCATION";C1;L15</p>
<p>OUTPATIENT ENCOUNTER;"DATE/TIME";C18;L20</p>
<p>REASON NOT BILLABLE;C1</p>
<p>BILLABLE FINDINGS TYPE</p>
<ul>
<li><blockquote>
<p>BILLABLE FINDINGS TYPE</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>357.96</td>
<td>IBD NO APPOINTMENT LIST</td>
<td><p>PATIENT;L25!</p>
<p>PATIENT:</p>
<ul>
<li><blockquote>
<p>PRIMARY LONG ID;"SSN";L12</p>
</blockquote></li>
</ul>
<p>CLINIC;L25</p>
<p>DATE/TIME PRINTED;L20</p>
<p>PROCESSING STATUS;L18</p></td>
</tr>
<tr class="odd">
<td>359.3</td>
<td>IBD LIST ERRORS</td>
<td><p>PATIENT;L20</p>
<p>PATIENT:</p>
<ul>
<li><blockquote>
<p>PRIMARY LONG ID;"ID";L12</p>
</blockquote></li>
</ul>
<p>ENCOUNTER DATE/TIME;"APPOINTMENT DATE";L16</p>
<p>FORM TRACKING NUMBER;"FORM TRACKING ID";R9</p>
<p>ERROR SOURCE</p>
<p>USER;L20</p>
<p>ERROR MESSAGE;W35</p></td>
</tr>
<tr class="even">
<td>362.1</td>
<td>IB AB COMMENTS</td>
<td>Automated Biller Error / Comments Report.</td>
</tr>
<tr class="odd">
<td>364.2</td>
<td>IBCEM MESSAGE LIST</td>
<td><p>"MESSAGE #: "_#.01;X;C1</p>
<p>"MESSAGE TYPE: "_MESSAGE TYPE;C40;X</p>
<p>"DATE RECORDED: "_NUMDATE(DATE RECORDED)_"@"_TIME(DATE RECORDED);C3;X</p>
<p>"BATCH NUMBER: "_BATCH NUMBER;C40;X</p>
<p>"BILL #: "_TRANSMIT BILL;C3;X</p>
<p>"STATUS: "_STATUS;C40;X</p>
<p>"MESSAGE DATE: "_NUMDATE(MESSAGE DATE)_"@"_TIME(MESSAGE DATE);C3;X</p>
<p>"UPDATE TASK: "_UPDATE TASK;C40;X</p>
<p>"STATUS CHANGED DATE: "_NUMDATE(STATUS CHANGED DATE)_"@"_TIME(STATUS CHANGED DAT</p>
<p>"STATUS CHANGED BY: "_STATUS CHANGED BY;C3;X</p>
<p>"SOURCE LEVEL: "_SOURCE LEVEL;C3;X</p>
<p>"SOURCE: "_SOURCE;C40;X</p>
<p>"MESSAGE:";C1;X</p>
<p>MESSAGE;C1;X;m</p>
<p>"BILL NUMBERS:";C7;S;""</p>
<p>"TRANSMISSION STATUS:";C29;""</p>
<p>"-------------";C7;""</p>
<p>"--------------------";C29;""</p>
<p>BATCH NUMBER:</p>
<p>EDI TRANSMIT BILL:</p>
<p>BILL NUMBER;"";C7</p>
<p>TRANSMISSION STATUS;"";C29</p></td>
</tr>
<tr class="even">
<td>364.2</td>
<td>IBCEM MESSAGE LIST HDR</td>
<td><p>"EDI RETURN MESSAGE DETAIL";C0;""</p>
<p>DATE(TODAY);C45;L18;"";d</p>
<p>TIME(NOW);C59;""</p>
<p>"PAGE: "_PAGE;C69;""</p>
<p>DUP("-",80);C0;L80;S;""</p></td>
</tr>
<tr class="odd">
<td>364.4</td>
<td>IBCE RULE DISPLAY</td>
<td>TOO MUCH INFORMATION TO DISPLAY</td>
</tr>
<tr class="even">
<td>364.4</td>
<td>IBCE RULE DISPLAY HEADER</td>
<td><p>"TRANSMISSION RULE DETAIL";C1</p>
<p>NOW;C36;X;L18</p>
<p>"PAGE: "_PAGE;C70;X</p>
<p>DUP("=",80);C1;X</p>
<p>" ";C1;X</p></td>
</tr>
<tr class="odd">
<td>364.6</td>
<td>IBCE LOCAL DATA ELEMENTS</td>
<td><p>ASSOCIATED FORM DEFINITION:</p>
<p>"LINE: "_LINE_"/COL: "_COL_" ";X;L18</p>
<p>SHORT DESCRIPTION_$J("",20);C19;"DESCRIPTION";L20</p>
<p>IB FORM FIELD CONTENT:</p>
<p>DATA ELEMENT;L28</p>
<p>"CODE: ";C10;X</p>
<p>FORMAT CODE;C16;W50;"FORMAT CODE"</p>
<p>"DESC: ";C10;X</p>
<p>FORMAT CODE DESCRIPTION;C16;W50;m;w</p>
<p>"INSURANCE COMPANY: "_$S(INSURANCE COMPANY="":"ALL",1:INSURANCE COMPANY);C10;</p>
<p>"BILL TYPE: "_$S(BILL TYPE="":"ALL",1:BILL TYPE);"";C10</p>
<p>" ";C1;""</p></td>
</tr>
<tr class="even">
<td>399</td>
<td>IB CLK PROD</td>
<td>Clerk Productivity Report</td>
</tr>
<tr class="odd">
<td>399</td>
<td>IB CLK PROD HDR</td>
<td>Clerk Productivity Report</td>
</tr>
<tr class="even">
<td>399.5</td>
<td>IB BILLING RATES</td>
<td>List billing rates</td>
</tr>
<tr class="odd">
<td>409.71</td>
<td>IB CPT RG DISPLAY</td>
<td>Displays billing Medicare rate group data for a procedure.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633856" class="anchor"></span>Table : File Flow

## File Flow Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633857" class="anchor"></span>Table : Options without Parents</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 38%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>FILE#</p>
<p>AND NAME</p></th>
<th>POINTS TO</th>
<th>POINTED TO BY</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>36</p>
<p>INSURANCE COMPANY</p></td>
<td><p>5 - STATE</p>
<p>36 - INSURANCE COMPANY</p>
<p>355.13 - INSURANCE FILING TIME FRAME</p>
<p>355.2 - TYPE OF INSURANCE COVERAGE</p>
<p>355.97 - IB PROVIDER ID # TYPE</p>
<p>365.12 - PAYER</p>
<p>399.2 - REVENUE CODE</p></td>
<td><p>2 - PATIENT</p>
<p>36 - INSURANCE COMPANY</p>
<p>340 - AR DEBTOR</p>
<p>344.4 - ELECTRONIC REMITTANCE ADVICE</p>
<p>350.9 - IB SITE PARAMETERS</p>
<p>355.3 - GROUP INSURANCE PLAN</p>
<p>355.9 - IB BILLING PRACTITIONER ID</p>
<p>355.91 - IB INSURANCE CO LEVEL BILLING PROV ID</p>
<p>355.92 - FACILITY BILLING ID</p>
<p>355.95 -IB PROVIDER ID CARE UNIT</p>
<p>355.96 - IB INS CO PROVIDER ID CARE UNIT</p>
<p>356.2 - INSURANCE REVIEW</p>
<p>356.25 = CLAIMS TRACKING ROI</p>
<p>361.1 - EXPLANATION OF BENEFITS</p>
<p>364.1 - EDI TRANSMISSION BATCH</p>
<p>364.4 - IB EDI TRANSMISSION RULE</p>
<p>364.7 - IB FORM FIELD CONTENT</p>
<p>367.1 - HPID/OEID TRANSMISSION QUEUE</p>
<p>399 - BILL/CLAIMS</p>
<p>412 - AR DEBTOR</p>
<p>430 - ACCOUNTS RECEIVABLE</p>
<p>453 - APPLICANT</p>
<p>19625 - DSIV ICB AUDIT</p>
<p>594004 - INSURANCE PATIENT BILL</p>
<p>9002313.57 - BPS LOG OF TRANSACTIONS</p>
<p>9002313.59 - BPS TRANSACTION</p>
<p>9002313.78 - BPS INSURER DATA</p></td>
</tr>
<tr class="even">
<td><p>355.93</p>
<p>IB NON/OTHER VA BILLING PROVIDER FILE</p></td>
<td><p>x - IB PROVIDER ID # TYPE</p>
<p>200 - NEW PERSON</p>
<p>8932.1 - PERSON CLASS</p>
<p>5 - STATE</p></td>
<td><p>161.9 - FEE BASIS PAID TO IB</p>
<p>355.9 - IB BILLING PRACTITIONER ID</p>
<p>399 - BILL/CLAIMS</p></td>
</tr>
<tr class="odd">
<td><p>350</p>
<p>INTEGRATED BILLING ACTION FILE</p></td>
<td><p>2 - PATIENT</p>
<p>4 - INSTITUTION</p>
<p>200 - NEW PERSON</p>
<p>350 - INTEGRATED BILLING ACTION</p>
<p>350.1 - IB ACTION TYPE</p>
<p>350.21 - IB ACTION STATUS</p>
<p>350.3 - IB CHARGE REMOVE REASONS</p>
<p>352.5 - IB CLINIC STOP CODE BILLABLE TYPES</p>
<p>354.71 - IB CO-PAY TRANSACTIONS</p>
<p>375 - PFSS ACCOUNT</p></td>
<td><p>52 - PRESCRIPTION</p>
<p>350 - INTEGRATED BILLING ACTION</p>
<p>351.2 - SPECIAL INPATIENT BILLING CASES</p>
<p>351.5 - TRICARE PHARMACY TRANSACTIONS</p>
<p>354.71 - IB CO-PAY TRANSACTIONS</p>
<p>366.15 - IB NCPDP PRESCRIPTION</p></td>
</tr>
<tr class="even">
<td><p>350.1</p>
<p>IB ACTION TYPE FILE</p></td>
<td><p>49 - SERVICE/SECTION</p>
<p>350.1 - IB ACTION TYPE</p>
<p>430.2 - ACCOUNTS RECEIVABLE CATEGORY</p></td>
<td><p>52 - PRESCRIPTION</p>
<p>350 - INTEGRATED BILLING ACTION</p>
<p>350.1 - IB ACTION TYPE</p>
<p>350.2 - IB ACTION CHARGE</p>
<p>350.4 - BILLABLE AMBULATORY SURGICAL CODE</p>
<p>350.41 - UPDATE BILLABLE AMBULATORY SURGICAL CODE</p>
<p>354.71 - IB CO-PAY TRANSACTIONS</p>
<p>399.1 - MCCR UTILITY</p></td>
</tr>
<tr class="odd">
<td><p>350.2</p>
<p>IB ACTION CHARGE FILE</p></td>
<td>350.1 - IB ACTION TYPE</td>
<td></td>
</tr>
<tr class="even">
<td><p>350.21</p>
<p>IB ACTION STATUS FILE</p></td>
<td></td>
<td>350 - INTEGRATED BILLING ACTION</td>
</tr>
<tr class="odd">
<td><p>350.3</p>
<p>IB CHARGE REMOVE REASONS FILE</p></td>
<td></td>
<td><p>350 - INTEGRATED BILLING ACTION</p>
<p>354.71 - IB CO-PAY TRANSACTIONS</p></td>
</tr>
<tr class="even">
<td><p>350.4</p>
<p>BILLABLE AMBULATORY SURGICAL CODE FILE</p></td>
<td><p>81 - CPT</p>
<p>350.1 - IB ACTION TYPE</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>350.41</p>
<p>UPDATE BILLABLE AMBULATORY SURGICAL CODE FILE</p></td>
<td><p>81 - CPT</p>
<p>350.1 - IB ACTION TYPE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>350.5</p>
<p>BASC LOCALITY MODIFIER FILE</p></td>
<td>40.8 - MEDICAL CENTER DIVISION</td>
<td></td>
</tr>
<tr class="odd">
<td><p>350.6</p>
<p>IB ARCHIVE/PURGE LOG FILE</p></td>
<td><p>1 - FILE</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>350.7</p>
<p>AMBULATORY CHECK-OFF SHEET FILE</p></td>
<td></td>
<td><p>44 - HOSPITAL LOCATION</p>
<p>350.71 - AMBULATORY SURG. CHECK-OFF SHEET PRINT FIELDS</p></td>
</tr>
<tr class="odd">
<td><p>350.71</p>
<p>AMBULATORY SURG. CHECK-OFF SHEET PRINT FIELDS FILE</p></td>
<td><p>350.7 - AMBULATORY CHECK-OFF SHEET</p>
<p>350.71 - AMBULATORY SURG. CHECK-OFF SHEET PRINT FIELDS</p>
<p>81 - CPT</p></td>
<td>350.71 - AMBULATORY SURG. CHECK-OFF SHEET PRINT FIELDS</td>
</tr>
<tr class="even">
<td><p>350.8</p>
<p>IB ERROR</p></td>
<td>354.5 - BILLING ALERT DEFINITION</td>
<td>399 - BILL/CLAIMS</td>
</tr>
<tr class="odd">
<td><p>350.9</p>
<p>IB SITE PARAMETERS</p></td>
<td><p>9002313.93 - BPS NCPDP REJECT CODES</p>
<p>363.1 - CHARGE SET</p>
<p>81 - CPT</p>
<p>3.5 - DEVICE</p>
<p>4.1 - FACILITY TYPE</p>
<p>142 - HEALTH SUMMARY TYPE</p>
<p>80 - ICD DIAGNOSIS</p>
<p>4 - INSTITUTION</p>
<p>36 - INSURANCE COMPANY</p>
<p>3.8 - MAIL GROUP</p>
<p>40.8 - MEDICAL CENTER DIVISION</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>365.12 - PAYER</p>
<p>399.2 - REVENUE CODE</p>
<p>49 - SERVICE/SECTION</p>
<p>5 - STATE</p>
<p>351.6 - TRANSFER PRICING PATIENT</p>
<p>350.963 - HCSR CLINIC LIST</p>
<p>350.964 - HCSR WARD LIST</p>
<p>350.965 - HCSR INSCO APPT LIST</p>
<p>350.966 - HCSR INSCO ADM LIST</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>350.963</p>
<p>HCSR CLINIC LIST</p></td>
<td></td>
<td>350.9 - IB SITE PARAMETERS</td>
</tr>
<tr class="odd">
<td><p>350.964</p>
<p>HCSR WARD LIST</p></td>
<td></td>
<td>350.9 - IB SITE PARAMETERS</td>
</tr>
<tr class="even">
<td><p>350.965</p>
<p>HCSR INSCO APPT LIST</p></td>
<td></td>
<td>350.9 - IB SITE PARAMETERS</td>
</tr>
<tr class="odd">
<td><p>350.966</p>
<p>HCSR INSCO ADM LIST</p></td>
<td></td>
<td>350.9 - IB SITE PARAMETERS</td>
</tr>
<tr class="even">
<td><p>351</p>
<p>MEANS TEST BILLING CLOCK FILE</p></td>
<td><p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>351.1</p>
<p>IB CONTINUOUS PATIENT FILE</p></td>
<td><p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>351.2</p>
<p>SPECIAL INPATIENT BILLING CASES FILE</p></td>
<td><p>350 - INTEGRATED BILLING ACTION</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>405 - PATIENT MOVEMENT</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>351.5</p>
<p>TRICARE PHARMACY TRANSACTIONS FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>350 - INTEGRATED BILLING ACTION</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>351.53 - PRODUCT SELECTION REASON</p></td>
<td>351.52 - TRICARE PHARMACY REJECTS</td>
</tr>
<tr class="even">
<td><p>351.52</p>
<p>TRICARE PHARMACY REJECTS FILE</p></td>
<td>351.5 - TRICARE PHARMACY TRANSACTIONS</td>
<td></td>
</tr>
<tr class="odd">
<td><p>351.53</p>
<p>PRODUCT SELECTION REASON FILE</p></td>
<td></td>
<td>351.5 - TRICARE PHARMACY TRANSACTIONS</td>
</tr>
<tr class="even">
<td><p>351.6</p>
<p>TRANSFER PRICING PATIENT FILE</p></td>
<td><p>4 - INSTITUTION</p>
<p>2 - PATIENT</p></td>
<td><p>350.9 - IB SITE PARAMETERS</p>
<p>351.61 - TRANSFER PRICING TRANSACTIONS</p></td>
</tr>
<tr class="odd">
<td><p>351.61</p>
<p>TRANSFER PRICING TRANSACTIONS FILE</p></td>
<td><p>81 - CPT</p>
<p>80.2 - DRG</p>
<p>50 - DRUG</p>
<p>80 - ICD DIAGNOSIS</p>
<p>4 - INSTITUTION</p>
<p>405 - PATIENT MOVEMENT</p>
<p>45 - PTF</p>
<p>351.6 - TRANSFER PRICING PATIENT</p>
<p>351.61 - TRANSFER PRICING TRANSACTIONS</p></td>
<td>351.61 - TRANSFER PRICING TRANSACTIONS</td>
</tr>
<tr class="even">
<td><p>351.67</p>
<p>TRANSFER PRICING INPT PROSTHETIC ITEMS FILE</p></td>
<td>661.1 - PROSTHETIC HCPCS</td>
<td></td>
</tr>
<tr class="odd">
<td>351.7 IB DM EXTRACT REPORTS FILE</td>
<td>351.701 - IB DM EXTRACT DATA ELEMENTS</td>
<td></td>
</tr>
<tr class="even">
<td>351.701 IB DM EXTRACT DATA ELEMENTS FILE</td>
<td>351.7 - IB DM EXTRACT REPORTS</td>
<td>351.71 - IB DM EXTRACT DATA</td>
</tr>
<tr class="odd">
<td>351.71 IB DM EXTRACT DATA FILE</td>
<td><p>351.701 - IB DM EXTRACT DATA ELEMENTS</p>
<p>351.7 - IB DM EXTRACT REPORTS</p></td>
<td></td>
</tr>
<tr class="even">
<td>351.73 IB DM WORKLOAD PARAMETERS FILE</td>
<td><p>430.2 - ACCOUNTS RECEIVABLE CATEGORY</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="odd">
<td>351.81 LTC CO-PAY CLOCK FILE</td>
<td><p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="even">
<td>351.82 IB UC VISIT TRACKING FILE</td>
<td><p>2 - PATIENT</p>
<p>4 - INSTITUTION</p></td>
<td></td>
</tr>
<tr class="odd">
<td>351.9 CLAIMSMANAGER BILLS FILE</td>
<td><p>399 - BILL/CLAIMS</p>
<p>351.91 - CLAIMSMANAGER STATUS</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="even">
<td>351.91 CLAIMSMANAGER STATUS FILE</td>
<td></td>
<td>351.9 - CLAIMSMANAGER BILLS</td>
</tr>
<tr class="odd">
<td><p>352.1</p>
<p>BILLABLE APPOINTMENT TYPE FILE</p></td>
<td>409.1 - APPOINTMENT TYPE</td>
<td></td>
</tr>
<tr class="even">
<td><p>352.2</p>
<p>NON-BILLABLE DISPOSITIONS FILE</p></td>
<td>37 - DISPOSITION</td>
<td></td>
</tr>
<tr class="odd">
<td><p>352.3</p>
<p>NON-BILLABLE CLINIC STOP CODES FILE</p></td>
<td>40.7 - CLINIC STOP</td>
<td></td>
</tr>
<tr class="even">
<td><p>352.4</p>
<p>NON-BILLABLE CLINICS FILE</p></td>
<td>44 - HOSPITAL LOCATION</td>
<td></td>
</tr>
<tr class="odd">
<td><p>352.5</p>
<p>IB CLINIC STOP CODE BILLABLE TYPES FILE</p></td>
<td></td>
<td>350 - INTEGRATED BILLING ACTION</td>
</tr>
<tr class="even">
<td><p>353</p>
<p>BILL FORM TYPE FILE</p></td>
<td><p>353 - BILL FORM TYPE</p>
<p>1 - FILE</p></td>
<td><p>353 - BILL FORM TYPE</p>
<p>364.6 - IB FORM SKELETON DEFINITION</p>
<p>399 - BILL/CLAIMS</p></td>
</tr>
<tr class="odd">
<td><p>353.1</p>
<p>PLACE OF SERVICE FILE</p></td>
<td></td>
<td>399 - BILL/CLAIMS</td>
</tr>
<tr class="even">
<td><p>353.2</p>
<p>TYPE OF SERVICE FILE</p></td>
<td></td>
<td><p>399 - BILL/CLAIMS</p>
<p>162 - FEE BASIS PAYMENT</p></td>
</tr>
<tr class="odd">
<td><p>354</p>
<p>BILLING PATIENT FILE</p></td>
<td><p>354.2 - EXEMPTION REASON</p>
<p>2 - PATIENT</p></td>
<td>354.1 - BILLING EXEMPTIONS</td>
</tr>
<tr class="even">
<td><p>354.1</p>
<p>BILLING EXEMPTIONS FILE</p></td>
<td><p>354.4 - BILLING ALERTS</p>
<p>354 - BILLING PATIENT</p>
<p>354.2 - EXEMPTION REASON</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>354.2</p>
<p>EXEMPTION REASON FILE</p></td>
<td></td>
<td><p>354 - BILLING PATIENT</p>
<p>354.1 - BILLING EXEMPTIONS</p></td>
</tr>
<tr class="even">
<td><p>354.4</p>
<p>BILLING ALERTS FILE</p></td>
<td><p>354.5 - BILLING ALERT DEFINITION</p>
<p>200 - NEW PERSON</p></td>
<td>354.1 - BILLING EXEMPTIONS</td>
</tr>
<tr class="odd">
<td><p>354.5</p>
<p>BILLING ALERT DEFINITION FILE</p></td>
<td><p>3.8 - MAIL GROUP</p>
<p>200 - NEW PERSON</p></td>
<td><p>350.8 - IB ERROR</p>
<p>354.4 - BILLING ALERTS</p></td>
</tr>
<tr class="even">
<td><p>354.7</p>
<p>IB PATIENT CO-PAY ACCOUNT FILE</p></td>
<td>2 - PATIENT</td>
<td>354.71 - IB CO-PAY TRANSACTIONS</td>
</tr>
<tr class="odd">
<td><p>354.71</p>
<p>IB CO-PAY TRANSACTIONS FILE</p></td>
<td><p>350.1 - IB ACTION TYPE</p>
<p>350.3 - IB CHARGE REMOVE REASONS</p>
<p>354.71 - IB CO-PAY TRANSACTIONS</p>
<p>354.7 - IB PATIENT CO-PAY ACCOUNT</p>
<p>4 - INSTITUTION</p>
<p>350 - INTEGRATED BILLING ACTION</p>
<p>200 - NEW PERSON</p></td>
<td><p>52 - PRESCRIPTION</p>
<p>350 - INTEGRATED BILLING ACTION</p>
<p>354.71 - IB CO-PAY TRANSACTIONS</p></td>
</tr>
<tr class="even">
<td><p>355.1</p>
<p>TYPE OF PLAN FILE</p></td>
<td></td>
<td><p>355.3 - GROUP INSURANCE PLAN</p>
<p>355.33 - INSURANCE VERIFICATION PROCESSOR</p></td>
</tr>
<tr class="odd">
<td><p>355.12</p>
<p>SOURCE OF INFORMATION FILE</p></td>
<td></td>
<td><p>2 – PATIENT</p>
<p>355.33 - INSURANCE VERIFICATION PROCESSOR</p>
<p>355.36 - CREATION TO PROCESSING TRACKING</p>
<p>365.1 IIV TRANSMISSION QUEUE</p></td>
</tr>
<tr class="even">
<td><p>355.13</p>
<p>INSURANCE FILING TIME FRAME FILE</p></td>
<td></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>355.3 - GROUP INSURANCE PLAN</p></td>
</tr>
<tr class="odd">
<td><p>355.2</p>
<p>TYPE OF INSURANCE COVERAGE FILE</p></td>
<td></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>367.1 - HPID/OEID TRANSMISSION QUEUE FILE</p></td>
</tr>
<tr class="even">
<td><p>355.3</p>
<p>GROUP INSURANCE PLAN FILE</p></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>355.13 - INSURANCE FILING TIME FRAME</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>366.03 - PLAN</p>
<p>355.1 - TYPE OF PLAN</p></td>
<td><p>2 – PATIENT</p>
<p>355.32 - PLAN COVERAGE LIMITATIONS</p>
<p>355.4 - ANNUAL BENEFITS</p>
<p>355.5 - INSURANCE CLAIMS YEAR TO DATE</p>
<p>366.14 – IB NCPDP EVENT LOG</p>
<p>366.16 - IB NDC NON COVERED BY PLAN</p>
<p>19625 - DSIV ICB AUDIT</p>
<p>9002313.02 - BPS CLAIMS</p>
<p>9002313.15 - BPS ASLEEP PAYERS</p>
<p>9002313.57 - BPS LOG OF TRANSACTIONS</p>
<p>9002313.59 - BPS TRANSACTION</p>
<p>9002313.78 - BPS INSURER DATA</p></td>
</tr>
<tr class="odd">
<td><p>355.31</p>
<p>PLAN LIMITATION CATEGORY FILE</p></td>
<td>355.6 - INSURANCE RIDERS</td>
<td>355.32 - PLAN COVERAGE LIMITATIONS</td>
</tr>
<tr class="even">
<td><p>355.32</p>
<p>PLAN COVERAGE LIMITATIONS FILE</p></td>
<td><p>355.3 - GROUP INSURANCE PLAN</p>
<p>200 - NEW PERSON</p>
<p>355.31 - PLAN LIMITATION CATEGORY</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.33</p>
<p>INSURANCE VERIFICATION PROCESSOR FILE</p></td>
<td><p>365.15 - IIV STATUS TABLE</p>
<p>4 - INSTITUTION</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>355.12 - SOURCE OF INFORMATION</p>
<p>5 - STATE</p>
<p>355.1 - TYPE OF PLAN</p></td>
<td><p>365 - IIV RESPONSE</p>
<p>365.1 - IIV TRANSMISSION QUEUE</p></td>
</tr>
<tr class="even">
<td><p>355.35</p>
<p>HMS EXTRACT FILE STATUS FILE</p></td>
<td><p>(#.03) MESSAGES subfile</p>
<p>MESSAGE ID(#.01) points to MESSAGE(#3.9) file NUMBER(#.001) field</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.351</p>
<p>HMS RESULT FILE STATUS FILE</p></td>
<td><p>(#.03) MESSAGES subfile</p>
<p>MESSAGE ID(#.01) points to MESSAGE(#3.9) file NUMBER(#.001) field</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>355.36</p>
<p>CREATION TO PROCESSING TRACKING</p></td>
<td>(#.03) SOURCE OF INFORMATION points to SOI file (#355.12)</td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.4</p>
<p>ANNUAL BENEFITS FILE</p></td>
<td><p>355.3 - GROUP INSURANCE PLAN</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>355.5</p>
<p>INSURANCE CLAIMS YEAR TO DATE FILE</p></td>
<td><p>355.3 - GROUP INSURANCE PLAN</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.6</p>
<p>INSURANCE RIDERS FILE</p></td>
<td></td>
<td><p>355.31 - PLAN LIMITATION CATEGORY</p>
<p>355.7 - PERSONAL POLICY</p></td>
</tr>
<tr class="even">
<td><p>355.7</p>
<p>PERSONAL POLICY FILE</p></td>
<td><p>355.6 - INSURANCE RIDERS</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.8</p>
<p>SPONSOR FILE</p></td>
<td><p>23 - BRANCE OF SERVICE</p>
<p>2 - PATIENT</p>
<p>355.82 - SPONSOR PERSON</p></td>
<td>355.81 - SPONSOR RELATIONSHIP</td>
</tr>
<tr class="even">
<td><p>355.81</p>
<p>SPONSOR RELATIONSHIP FILE</p></td>
<td><p>2 - PATIENT</p>
<p>355.8 - SPONSOR</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.82</p>
<p>SPONSOR PERSON FILE</p></td>
<td></td>
<td>355.8 - SPONSOR</td>
</tr>
<tr class="even">
<td><p>355.9</p>
<p>IB BILLING PRACTITIONER ID FILE</p></td>
<td><p>355.96 - IB INS CO PROVIDER ID CARE UNIT</p>
<p>355.93 - IB NON/OTHER VA BILLING PROVIDER</p>
<p>355.97 - IB PROVIDER ID</p>
<p>36 - INSURANCE COMPANY</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.91</p>
<p>IB INSURANCE CO LEVEL BILLING PROV ID FILE</p></td>
<td><p>355.96 - IB INS CO PROVIDER ID CARE UNIT</p>
<p>355.97 - IB PROVIDER ID # TYPE</p>
<p>36 - INSURANCE COMPANY</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>355.92</p>
<p>FACILITY BILLING ID FILE</p></td>
<td><p>355.97 - IB PROVIDER ID # TYPE</p>
<p>355.95 - IB PROVIDER ID CARE UNIT</p>
<p>36 - INSURANCE COMPANY</p>
<p>40.8 - MEDICAL CENTER DIVISION</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>355.93</p>
<p>IB NON/OTHER VA BILLING PROVIDER FILE</p></td>
<td><p>355.97 - IB PROVIDER ID # TYPE</p>
<p>200 - NEW PERSON</p>
<p>8932.1 - PERSON CLASS</p>
<p>5 - STATE</p></td>
<td><p>355.9 - IB BILLING PRACTITIONER ID</p>
<p>399 - BILL/CLAIMS</p></td>
</tr>
<tr class="even">
<td><p>355.95</p>
<p>IB PROVIDER ID CARE UNIT FILE</p></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>40.8 - MEDICAL CENTER DIVISION</p></td>
<td><p>355.92 - FACILITY BILLING ID</p>
<p>355.96 - IB INS CO PROVIDER ID CARE UNIT</p></td>
</tr>
<tr class="odd">
<td><p>355.96</p>
<p>IB INS CO PROVIDER ID CARE UNIT FILE</p></td>
<td><p>355.97 - IB PROVIDER ID # TYPE</p>
<p>355.95 - IB PROVIDER ID CARE UNIT</p>
<p>36 - INSURANCE COMPANY</p></td>
<td><p>355.9 - IB BILLING PRACTITIONER ID</p>
<p>355.91 - IB INSURANCE CO LEVEL BILLING PROV ID</p></td>
</tr>
<tr class="even">
<td><p>355.97</p>
<p>IB PROVIDER ID # TYPE FILE</p></td>
<td></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>355.9 - IB BILLING PRACTITIONER ID</p>
<p>355.91 - IB INSURANCE CO LEVEL BILLING PROV ID</p>
<p>355.92 - FACILITY BILLING ID</p>
<p>355.93 - IB NON/OTHER VA BILLING PROVIDER</p>
<p>355.96 - IB INS CO PROVIDER ID CARE UNIT</p>
<p>399 - BILL/CLAIMS</p></td>
</tr>
<tr class="odd">
<td><p>355.98</p>
<p>IB ALTERNATE PRIMARY ID TYPE</p></td>
<td></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>350.9 - IB SITE PARAMETERS</p>
<p>399 - BILL/CLAIMS</p></td>
</tr>
<tr class="even">
<td><p>355.99</p>
<p>MASTER TYPE OF PLAN FILE</p></td>
<td></td>
<td>355.1 - TYPE OF PLAN</td>
</tr>
<tr class="odd">
<td><p>356</p>
<p>CLAIMS TRACKING FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>356.85 - CLAIMS TRACKING BILLABLE FINDINGS</p>
<p>356.8 - CLAIMS TRACKING NON-BILLABLE REASONS</p>
<p>356.6 - CLAIMS TRACKING TYPE</p>
<p>356.9 - INPATIENT DIAGNOSIS</p>
<p>200 - NEW PERSON</p>
<p>409.68 - OUTPATIENT ENCOUNTER</p>
<p>2 - PATIENT</p>
<p>405 - PATIENT MOVEMENT</p>
<p>52 - PRESCRIPTION</p>
<p>660 - RECORD OF PROS APPLIANCE/REPAIR</p>
<p>41.1 - SCHEDULED ADMISSION</p>
<p>9000010 - VISIT</p></td>
<td><p>356.1 - HOSPITAL REVIEW</p>
<p>356.2 - INSURANCE REVIEW</p>
<p>356.399 - CLAIMS TRACKING/BILL</p>
<p>362.1 - IB AUTOMATED BILLING COMMENTS</p></td>
</tr>
<tr class="even">
<td><p>356.001</p>
<p>X12 278 REQUEST CATEGORY FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.002</p>
<p>X12 278 CERTIFICATION TYPE CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.003</p>
<p>X12 278 CURRENT HEALTH CONDITION CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.004</p>
<p>X12 278 PROGNOSIS CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.005</p>
<p>X12 278 DELAY REASON CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.006</p>
<p>X12 278 DIAGNOSISY TYPE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.007</p>
<p>X12 278 DELIVERY PATTERN TIME CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.008</p>
<p>X12 278 CONDITION CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.009</p>
<p>X12 278 ADMISSION SOURCE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.01</p>
<p>X12 278 PATIENT STATUS FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.011</p>
<p>X12 278 NURSING HOME RESIDENTIAL STATUS FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.012</p>
<p>X12 278 SUBLUXATION LEVEL CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.013</p>
<p>X12 278 OXYGEN EQUIPMENT TYPE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.014</p>
<p>X12 278 OXYGEN TEST CONDITION FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.015</p>
<p>X12 278 OXYGEN TEST FINDINGS FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.016</p>
<p>X12 278 OXYGEN DELIVERY SYSTEM CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.017</p>
<p>X12 278 PATIENT LOCATION FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.018</p>
<p>X12 278 REPORT TYPE CODE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.019</p>
<p>X12 278 NURSING HOME LEVEL OF CARE FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.02</p>
<p>X12 278 CERTIFICATION ACTION CODES FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="even">
<td><p>356.021</p>
<p>X12 278 DCS DECISION REASON CODES FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.022</p>
<p>UNIVERSAL DENTAL NUMBERING SYSTEM</p></td>
<td></td>
<td><p>356.22 - HCS REVIEW TRANSMISSION</p>
<p>399 - BILL/CLAIMS</p></td>
</tr>
<tr class="even">
<td>356.023 HCSR WORKLIST DELETE REASON CODE</td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>356.1</p>
<p>HOSPITAL REVIEW FILE</p></td>
<td><p>356 - CLAIMS TRACKING</p>
<p>356.4 - CLAIMS TRACKING NON-ACUTE CLASSIFICATIONS</p>
<p>356.11 - CLAIMS TRACKING REVIEW TYPE</p>
<p>356.3 - CLAIMS TRACKING SI/IS CATEGORIES</p>
<p>45.7 - FACILITY TREATING SPECIALTY</p>
<p>356.1 - HOSPITAL REVIEW</p>
<p>200 - NEW PERSON</p></td>
<td><p>356.1 - HOSPITAL REVIEW</p>
<p>356.2 - INSURANCE REVIEW</p></td>
</tr>
<tr class="even">
<td><p>356.11</p>
<p>CLAIMS TRACKING REVIEW TYPE FILE</p></td>
<td></td>
<td><p>356.1 - HOSPITAL REVIEW</p>
<p>356.2 - INSURANCE REVIEW</p></td>
</tr>
<tr class="odd">
<td><p>356.2</p>
<p>INSURANCE REVIEW FILE</p></td>
<td><p>356 - CLAIMS TRACKING</p>
<p>356.7 - CLAIMS TRACKING ACTION</p>
<p>356.21 - CLAIMS TRACKING DENIAL REASONS</p>
<p>356.11 - CLAIMS TRACKING REVIEW TYPE</p>
<p>356.1 - HOSPITAL REVIEW</p>
<p>80 - ICD DIAGNOSIS</p>
<p>36 - INSURANCE COMPANY</p>
<p>356.2 - INSURANCE REVIEW</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td>356.2 - INSURANCE REVIEW</td>
</tr>
<tr class="even">
<td><p>356.21</p>
<p>CLAIMS TRACKING</p>
<p>DENIAL REASONS</p></td>
<td>356.2 - INSURANCE REVIEW</td>
<td></td>
</tr>
<tr class="odd">
<td><p>356.22</p>
<p>HCS REVIEW TRANSMISSION FILE</p></td>
<td><p>2 - PATIENT</p>
<p>42 - WARD LOCATION</p>
<p>44 - HOSPITAL LOCATION</p>
<p>200 - NEW PERSON</p>
<p>356.001 - X12 278 REQUEST CATEGORY</p>
<p>356.002 - X12 278 CERTIFICATION TYPE CODE</p>
<p>365.013 - X12 271 SERVICE TYPE</p>
<p>353.1 - PLACE OF SERVICE</p>
<p>5 - STATE</p>
<p>779.004 - COUNTRY CODE</p>
<p>356.003 - X12 278 CURRENT HEALTH CONDITION CODE</p>
<p>356.004 - X12 278 PROGNOSIS CODE</p>
<p>356.005 - X12 278 DELAY REASON CODE</p>
<p>356.006 - X12 278 DIAGNOSIS TYPE</p>
<p>365.016 - X12 271 QUANTITY QUALIFIER</p>
<p>365.015 - X12 271 TIME PERIOD QUALIFIER</p>
<p>365.025 - X12 271 DELIVERY FREQUENCY CODE</p>
<p>356.007 - X12 278 DELIVERY PATTERN TIME CODE</p>
<p>356.008 - X12 278 CONDITION CODE</p>
<p>356.009 - X12 278 ADMISSION SOURCE</p>
<p>356.01 - X12 278 PATIENT STATUS</p>
<p>356.011 - X12 278 NURSING HOME RESIDENTIAL STATUS</p>
<p>356.012 - X12 278 SUBLUXATION LEVEL CODE</p>
<p>356.013 - X12 278 OXYGEN EQUIPMENT TYPE</p>
<p>356.014 - X12 278 OXYGEN TEST CONDITION</p>
<p>356.015 - X12 278 OXYGEN TEST FINDINGS</p>
<p>356.016 - X12 278 OXYGEN DELIVERY SYSTEM CODE</p>
<p>356.017 - X12 278 PATIENT LOCATION</p>
<p>356.018 - X12 278 REPORT TYPE</p>
<p>356.023 - HCSR WORKLIST DELETE REASON CODE</p>
<p>365.022 - X12 271 ENTITY IDENTIFIER CODE</p>
<p>365.027 - X12 271 LOOP ID</p>
<p>365.023 - X12 271 IDENTIFICATION QUALIFIER</p>
<p>36 - INSURANCE COMPANY</p>
<p>81.3 - CPT MODIFIER</p>
<p>399.2 - REVENUE CODE</p>
<p>356.019 - X12 278 NURSING HOME LEVEL OF CARE</p>
<p>81 - CPT</p>
<p>365.017 - X12 271 ERROR CONDITION</p>
<p>365.018 - X12 271 ERROR ACTION</p>
<p>356.022 - UNIVERSAL SENTAL NUMBERING SYSTEM</p>
<p>356.021 - X12 278 HCS DECISION REASON CO</p>
<p>356.02 - X12 278 CERTIFICATION ACTION C</p>
<p>356.22 - HCS REVIEW TRANSMISSION</p>
<p>80.1 - ICD OPERATION/PROCEDURE</p></td>
<td>356.22 - HCS REVIEW TRANSMISSION FILE</td>
</tr>
<tr class="even">
<td><p>356.25</p>
<p>CLAIMS TRACKING ROI FILE</p></td>
<td><p>50 - DRUG</p>
<p>36 - INSURANCE COMPANY</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>356.26</p>
<p>CLAIMS TRACKING ROI CONSENT</p></td>
<td><p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>356.3</p>
<p>CLAIMS TRACKING SI/IS CATEGORIES FILE</p></td>
<td></td>
<td>356.1 - HOSPITAL REVIEW</td>
</tr>
<tr class="odd">
<td><p>356.399</p>
<p>CLAIMS TRACKING/BILL FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>356 - CLAIMS TRACKING</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>356.5</p>
<p>CLAIMS TRACKING ALOS FILE</p></td>
<td>80.2 - DRG</td>
<td></td>
</tr>
<tr class="odd">
<td><p>356.6</p>
<p>CLAIMS TRACKING TYPE FILE</p></td>
<td></td>
<td>356 - CLAIMS TRACKING</td>
</tr>
<tr class="even">
<td><p>356.7</p>
<p>CLAIMS TRACKING ACTION FILE</p></td>
<td></td>
<td>356.2 - INSURANCE REVIEW</td>
</tr>
<tr class="odd">
<td><p>356.8</p>
<p>CLAIMS TRACKING NON-BILLABLE REASONS FILE</p></td>
<td></td>
<td><p>356 - CLAIMS TRACKING</p>
<p>9002313.02 - BPS CLAIMS</p>
<p>9002313.77 - BPS REQUESTS</p></td>
</tr>
<tr class="even">
<td><p>356.9</p>
<p>INPATIENT DIAGNOSIS FILE</p></td>
<td><p>80 - ICD DIAGNOSIS</p>
<p>405 - PATIENT MOVEMENT</p></td>
<td>356 - CLAIMS TRACKING</td>
</tr>
<tr class="odd">
<td><p>356.91</p>
<p>INPATIENT PROCEDURE FILE</p></td>
<td><p>80.1 - ICD OPERATION / PROCEDURE</p>
<p>405 - PATIENT MOVEMENT</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>356.93</p>
<p>INPATIENT INTERIM DRG FILE</p></td>
<td><p>80.2 - DRG</p>
<p>405 - PATIENT MOVEMENT</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>356.94</p>
<p>INPATIENT PROVIDERS FILE</p></td>
<td><p>200 - NEW PERSON</p>
<p>405 - PATIENT MOVEMENT</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>357</p>
<p>ENCOUNTER FORM FILE</p></td>
<td></td>
<td><p>357.09 - ENCOUNTER FORM PARAMETERS</p>
<p>357.1 - ENCOUNTER FORM BLOCK</p>
<p>357.95 - FORM DEFINITION</p>
<p>359 - CONVERTED FORMS</p>
<p>359.3 - AICS ERROR AND WARNING LOG</p>
<p>409.95 - PRINT MANAGER CLINIC SETUP</p></td>
</tr>
<tr class="odd">
<td><p>357.08</p>
<p>AICS PURGE LOG FILE</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>357.09</p>
<p>ENCOUNTER FORM PARAMETERS FILE</p></td>
<td><p>357 - ENCOUNTER FORM</p>
<p>3.8 - MAIL GROUP</p>
<p>357.99 - PRINT MANAGER CLINIC GROUPS</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>357.1</p>
<p>ENCOUNTER FORM BLOCK FILE</p></td>
<td><p>359.1 - AICS DATA ELEMENTS</p>
<p>357.98 - AICS DATA QUALIFIERS</p>
<p>357 - ENCOUNTER FORM</p>
<p>357.6 - PACKAGE INTERFACE</p></td>
<td><p>357.2 - SELECTION LIST</p>
<p>357.5 - DATA FIELD</p>
<p>357.7 - FORM LINE</p>
<p>357.8 - TEXT AREA</p>
<p>357.93 - MULTIPLE CHOICE FIELD</p>
<p>358.94 - IMP/EXP HAND PRINT FIELD</p>
<p>359.94 - HAND PRINT FIELD</p></td>
</tr>
<tr class="even">
<td><p>357.2</p>
<p>SELECTION LIST FILE</p></td>
<td><p>357.98 - AICS DATA QUALIFIERS</p>
<p>357.1 - ENCOUNTER FORM BLOCK</p>
<p>357.91 - MARKING AREA TYPE</p>
<p>357.6 - PACKAGE INTERFACE</p></td>
<td><p>357.3 - SELECTION</p>
<p>357.4 - SELECTION GROUP</p></td>
</tr>
<tr class="odd">
<td><p>357.3</p>
<p>SELECTION FILE</p></td>
<td><p>757.01 - EXPRESSIONS</p>
<p>357.4 - SELECTION GROUP</p>
<p>357.2 - SELECTION LIST</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>357.4</p>
<p>SELECTION GROUP FILE</p></td>
<td>357.2 - SELECTION LIST</td>
<td>357.3 - SELECTION</td>
</tr>
<tr class="odd">
<td><p>357.5</p>
<p>DATA FIELD FILE</p></td>
<td><p>357.1 - ENCOUNTER FROM BLOCK</p>
<p>357.6 - PACKAGE INTERFACE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>357.6</p>
<p>PACKAGE INTERFACE FILE</p></td>
<td><p>359.1 - AICS DATA ELEMENTS</p>
<p>142 - HEALTH SUMMARY TYPE</p>
<p>357.6 - PACKAGE INTERFACE</p></td>
<td><p>357.2 - SELECTION LIST</p>
<p>357.5 - DATA FIELD</p>
<p>357.6 - PACKAGE INTERFACE</p>
<p>357.93 - MULTIPLE CHOICE FIELD</p>
<p>358.94 - IMP/EXP HAND PRINT FIELD</p>
<p>359.3 - AICS ERROR AND WARNING LOG</p>
<p>359.94 - HAND PRINT FIELD</p></td>
</tr>
<tr class="odd">
<td><p>357.69</p>
<p>TYPE OF VISIT FILE</p></td>
<td>81 - CPT</td>
<td></td>
</tr>
<tr class="even">
<td><p>357.7</p>
<p>FORM LINE FILE</p></td>
<td>357.1 - ENCOUNTER FORM BLOCK</td>
<td></td>
</tr>
<tr class="odd">
<td><p>357.8</p>
<p>TEXT AREA FILE</p></td>
<td>357.1 - ENCOUNTER FORM BLOCK</td>
<td></td>
</tr>
<tr class="even">
<td><p>357.93</p>
<p>MULTIPLE CHOICE FIELD FILE</p></td>
<td><p>357.98 - AICS DATA QUALIFIERS</p>
<p>357.1 - ENCOUNTER FORM BLOCK</p>
<p>357.6 - PACKAGE INTERFACE</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>357.94</p>
<p>ENCOUNTER FORM PRINTERS FILE</p></td>
<td>3.2 - TERMINAL TYPE</td>
<td></td>
</tr>
<tr class="even">
<td><p>357.95</p>
<p>FORM DEFINITION FILE</p></td>
<td><p>359.1 - AICS DATA ELEMENTS</p>
<p>357.98 - AICS DATA QUALIFIERS</p>
<p>357 - ENCOUNTER FORM</p>
<p>757.01 - EXPRESSIONS</p>
<p>44 - HOSPITAL LOCATION</p>
<p>357.6 - PACKAGE INTERFACE</p>
<p>357.3 - SELECTION</p></td>
<td>357.96 - ENCOUNTER FORM TRACKING</td>
</tr>
<tr class="odd">
<td><p>357.96</p>
<p>ENCOUNTER FORM TRACKING FILE</p></td>
<td><p>357.98 - AICS DATA QUALIFIERS</p>
<p>357.95 - FORM DEFINITION</p>
<p>44 - HOSPITAL LOCATION</p>
<p>200 - NEW PERSON</p>
<p>357.6 - PACKAGE INTERFACE</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>357.98</p>
<p>AICS DATA QUALIFIERS FILE</p></td>
<td></td>
<td>357.6 - PACKAGE INTERFACE</td>
</tr>
<tr class="odd">
<td><p>357.99</p>
<p>PRINT MANAGER CLINIC GROUPS FILE</p></td>
<td><p>44 - HOSPITAL LOCATION</p>
<p>40.8 - MEDICAL CENTER DIVISION</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>358</p>
<p>IMP/EXP ENCOUNTER FORM FILE</p></td>
<td></td>
<td>358.1 - IMP/EXP ENCOUNTER FORM BLOCK</td>
</tr>
<tr class="odd">
<td><p>358.1</p>
<p>IMP/EXP ENCOUNTER FORM BLOCK FILE</p></td>
<td>358 - IMP/EXP ENCOUNTER FORM</td>
<td><p>358.2 - IMP/EXP SELECTION LIST</p>
<p>358.5 - IMP/EXP DATA FIELD</p>
<p>358.7 - IMP/EXP FORM LINE</p>
<p>358.8 - IMP/EXP TEXT AREA</p>
<p>358.93 - IMP/EXP MULTIPLE CHOICE FIELD</p></td>
</tr>
<tr class="even">
<td><p>358.2</p>
<p>IMP/EXP SELECTION LIST FILE</p></td>
<td><p>358.98 - IMP/EXP AICS DATA QUALIFIERS</p>
<p>358.1 - IMP/EXP ENCOUNTER FORM BLOCK</p>
<p>358.91 - IMP/EXP MARKING AREA</p>
<p>358.6 - IMP/EXP PACKAGE INTERFACE</p></td>
<td><p>358.3 - IMP/EXP SELECTION</p>
<p>358.4 - IMP/EXP SELECTION GROUP</p></td>
</tr>
<tr class="odd">
<td><p>358.3</p>
<p>IMP/EXP SELECTION FILE</p></td>
<td><p>757.01 - EXPRESSIONS</p>
<p>358.4 - IMP/EXP SELECTION GROUP</p>
<p>358.2 - IMP/EXP SELECTION LIST</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>358.4</p>
<p>IMP/EXP SELECTION GROUP FILE</p></td>
<td>358.2 - IMP/EXP SELECTION LIST</td>
<td>358.3 - IMP/EXP SELECTION</td>
</tr>
<tr class="odd">
<td><p>358.5</p>
<p>IMP/EXP DATA FIELD FILE</p></td>
<td><p>358.1 - IMP/EXP ENCOUNTER FORM BLOCK</p>
<p>358.6 - IMP/EXP PACKAGE INTERFACE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>358.6</p>
<p>IMP/EXP PACKAGE INTERFACE FILE</p></td>
<td><p>142 - HEALTH SUMMARY TYPE</p>
<p>358.99 - IMP/EXP AICS DATA ELEMENTS</p>
<p>358.6 - IMP/EXP PACKAGE INTERFACE</p></td>
<td><p>358.2 - IMP/EXP SELECTION LIST</p>
<p>358.5 - IMP/EXP DATA FIELD</p>
<p>358.6 - IMP/EXP PACKAGE INTERFACE</p>
<p>358.93 - IMP/EXP MULTIPLE CHOICE FIELD</p></td>
</tr>
<tr class="odd">
<td><p>358.7</p>
<p>IMP/EXP FORM LINE FILE</p></td>
<td>358.1 - IMP/EXP ENCOUNTER FORM BLOCK</td>
<td></td>
</tr>
<tr class="even">
<td><p>358.8</p>
<p>IMP/EXP TEXT AREA FILE</p></td>
<td>358.1 - IMP/EXP ENCOUNTER FORM BLOCK</td>
<td></td>
</tr>
<tr class="odd">
<td><p>358.93</p>
<p>IMP/EXP MULTIPLE CHOICE FIELD FILE</p></td>
<td><p>358.98 - IMP/EXP AICS DATA QUALIFIERS</p>
<p>358.1 - IMP/EXP ENCOUNTER FORM BLOCK</p>
<p>358.6 - IMP/EXP PACKAGE INTERFACE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>358.94</p>
<p>IMP/EXP HAND PRINT FIELD FILE</p></td>
<td><p>359.1 - AICS DATA ELEMENTS</p>
<p>357.1 - ENOCUNTER FORM BLOCK</p>
<p>357.6 - PACKAGE INTERFACE</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>358.98</p>
<p>IMP/EXP AICS DATA QUALIFIERS FILE</p></td>
<td></td>
<td><p>357.6 - PACKAGE INTERFACE</p>
<p>358.6 - IMP/EXP PACKAGE INTERFACE</p></td>
</tr>
<tr class="even">
<td><p>359</p>
<p>CONVERTED FORMS FILE</p></td>
<td>357 - ENCOUNTER FORM</td>
<td></td>
</tr>
<tr class="odd">
<td><p>359.1</p>
<p>AICS DATA ELEMENTS FILE</p></td>
<td></td>
<td><p>357.6 - PACKAGE INTERFACE</p>
<p>358.94 - IMP/EXP HAND PRINT FIELD</p>
<p>359.94 - HAND PRINT FIELD</p></td>
</tr>
<tr class="even">
<td><p>359.3</p>
<p>AICS ERROR AND WARNING LOG FILE</p></td>
<td><p>357 - ENCOUNTER FORM</p>
<p>200 - NEW PERSON</p>
<p>357.6 - PACKAGE INTERFACE</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>359.94</p>
<p>HAND PRINT FIELD FILE</p></td>
<td><p>359.1 - AICS DATA ELEMENTS</p>
<p>357.1 - ENCOUNTER FORM BLOCK</p>
<p>357.6 - PACKAGE INTERFACE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>361</p>
<p>BILL STATUS MESSAGE FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>364.1 - EDI TRANSMISSION BATCH</p>
<p>364 - EDI TRANSMIT BILL</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>361.1</p>
<p>EXPLANATION OF BENEFITS FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>364.1 - EDI TRANSMISSION BATCH</p>
<p>364 - EDI TRANSMIT BILL</p>
<p>36 - INSURANCE COMPANY</p>
<p>200 - NEW PERSON</p>
<p>399.2 - REVENUE CODE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>361.3</p>
<p>IB MESSAGE SCREEN TEXT FILE</p></td>
<td>200 - NEW PERSON</td>
<td></td>
</tr>
<tr class="odd">
<td><p>361.4</p>
<p>EDI TEST CLAIM STATUS MESSAGE FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>361.4 - EDI TEST CLAIM STATUS MESSAGE</p>
<p>364.1 - EDI TRANSMISSION BATCH</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>362.1</p>
<p>IB AUTOMATED BILLING COMMENTS FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>356 - CLAIMS TRACKING</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>362.3</p>
<p>IB BILL/CLAIMS DIAGNOSIS FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>80 - ICD DIAGNOSIS</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>362.4</p>
<p>IB BILL/CLAIMS PRESCRIPTION REFILL FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>50 - DRUG</p>
<p>52 - PRESCRIPTION</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>362.5</p>
<p>IB BILL/CLAIMS PROSTHETICS FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>660 - RECORD OF PROS APPLIANCE / REPAIR</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>363</p>
<p>RATE SCHEDULE FILE</p></td>
<td><p>363.1 - CHARGE SET</p>
<p>399.1 - MCCR UTILITY</p>
<p>399.3 - RATE TYPE</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>363.1</p>
<p>CHARGE SET FILE</p></td>
<td><p>363.3 - BILLING RATE</p>
<p>363.31 - BILLING REGION</p>
<p>399.1 - MCCR UTILITY</p>
<p>399.2 - REVENUE CODE</p></td>
<td><p>350.9 - IB SITE PARAMETERS</p>
<p>363.2 - CHARGE ITEM</p></td>
</tr>
<tr class="even">
<td><p>363.2</p>
<p>CHARGE ITEM FILE</p></td>
<td><p>363.21 - BILLING ITEMS</p>
<p>363.1 - CHARGE SET</p>
<p>81 - CPT</p>
<p>81.3 - CPT MODIFIER</p>
<p>80.2 - DRG</p>
<p>399.1 - MCCR UTILITY</p>
<p>399.2 - REVENUE CODE</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>363.21</p>
<p>BILLING ITEMS FILE</p></td>
<td></td>
<td>363.2 - CHARGE ITEM</td>
</tr>
<tr class="even">
<td><p>363.3</p>
<p>BILLING RATE FILE</p></td>
<td></td>
<td>363.1 - CHARGE SET</td>
</tr>
<tr class="odd">
<td><p>363.31</p>
<p>BILLING REGION FILE</p></td>
<td><p>4 - INSTITUTION</p>
<p>40.8 - MEDICAL CENTER DIVISION</p></td>
<td>363.1 - CHARGE SET</td>
</tr>
<tr class="even">
<td><p>363.32</p>
<p>BILLING SPECIAL GROUPS FILE</p></td>
<td><p>363.3 - BILLING RATE</p>
<p>363.1 - CHARGE SET</p></td>
<td><p>363.33 - BILLING REVENUE CODE LINKS</p>
<p>363.34 - BILLING PROVIDER DISCOUNT</p></td>
</tr>
<tr class="odd">
<td><p>363.33</p>
<p>BILLING REVENUE CODE LINKS FILE</p></td>
<td><p>363.32 - BILLING SPECIAL GROUPS</p>
<p>81 - CPT</p>
<p>399.2 - REVENUE CODE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>363.34</p>
<p>BILLING PROVIDER DISCOUNT FILE</p></td>
<td><p>363.32 - BILLING SPECIAL GROUPS</p>
<p>8932.1 - PERSON CLASS</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>364</p>
<p>EDI TRANSMIT BILL FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>364.1 - EDI TRANSMISSION BATCH</p></td>
<td><p>361 - BILL STATUS MESSAGE</p>
<p>361.1 - EXPLANATION OF BENEFITS</p>
<p>364.2 - EDI MESSAGES</p></td>
</tr>
<tr class="even">
<td><p>364.1</p>
<p>EDI TRANSMISSION BATCH FILE</p></td>
<td><p>364.2 - EDI MESSAGES</p>
<p>364.1 - EDI TRANSMISSION BATCH</p>
<p>36 - INSURANCE COMPANY</p>
<p>200 - NEW PERSON</p></td>
<td><p>361 - BILL STATUS MESSAGE</p>
<p>361.1 - EXPLANATION OF BENEFITS</p>
<p>364 - EDI TRANSMIT BILL</p>
<p>364.1 - EDI TRANSMISSION BATCH</p>
<p>364.2 - EDI MESSAGES</p></td>
</tr>
<tr class="odd">
<td><p>364.2</p>
<p>EDI MESSAGES FILE</p></td>
<td><p>364.1 - EDI TRANSMISSION BATCH</p>
<p>364 - EDI TRANSMIT BILL</p>
<p>364.3 - IB MESSAGE ROUTER</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p></td>
<td>364.1 - EDI TRANSMISSION BATCH</td>
</tr>
<tr class="even">
<td><p>364.3</p>
<p>IB MESSAGE ROUTER FILE</p></td>
<td>3.8 - MAIL GROUP</td>
<td>364.2 - EDI MESSAGES</td>
</tr>
<tr class="odd">
<td><p>364.4</p>
<p>IB EDI TRANSMISSION RULE FILE</p></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>364.5</p>
<p>IB DATA ELEMENT DEFINITION FILE</p></td>
<td>1 - FILE</td>
<td>364.7 - IB FORM FIELD CONTENT</td>
</tr>
<tr class="odd">
<td><p>364.6</p>
<p>IB FORM SKELETON DEFINITION FILE</p></td>
<td><p>353 - BILL FORM TYPE</p>
<p>364.6 - IB FORM SKELETON DEFINITION</p></td>
<td><p>364.6 - IB FORM SKELETON DEFINITION</p>
<p>364.7 - IB FORM FIELD CONTENT</p></td>
</tr>
<tr class="even">
<td><p>364.7</p>
<p>IB FORM FIELD CONTENT FILE</p></td>
<td><p>364.5 - IB DATA ELEMENT DEFINITION</p>
<p>364.6 - IB FORM SKELETON DEFINITION</p>
<p>36 - INSURANCE COMPANY</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>365</p>
<p>IIV RESPONSE FILE</p></td>
<td><p>80 - ICD DIAGNOSIS</p>
<p>365.1 - IIV TRANSMISSION QUEUE</p>
<p>365.14 - IIV TRANSMISSION STATUS</p>
<p>355.33 - INSURANCE VERIFICATION PROCESSOR</p>
<p>2 - PATIENT</p>
<p>365.12 - PAYER</p>
<p>353.1 - PLACE OF SERVICE</p>
<p>5 - STATE</p>
<p>365.021 - X12 271 CONTACT QUALIFIER</p>
<p>365.012 - X12 271 COVERAGE LEVEL</p>
<p>365.026 - X12 271 DATE QUALIFIER</p>
<p>365.025 - X12 271 DELIVERY FREQUENCY CODE</p>
<p>365.011 - X12 271 ELIGIBILITY / BENEFIT</p>
<p>365.022 - X12 271 ENTITY IDENTIFIER CODE</p>
<p>365.018 - X12 271 ERROR ACTION</p>
<p>365.017 - X12 271 ERROR CONDITION</p>
<p>365.023 - X12 271 IDENTIFICATION QUALIFIER</p>
<p>365.014 - X12 271 INSURANCE TYPE</p>
<p>365.024 - X12 271 PROVIDER CODE</p>
<p>365.016 - X12 271 QUANTITY QUALIFIER</p>
<p>365.028 - X12 271 REFERENCE IDENTIFICATION</p>
<p>365.013 - X12 271 SERVICE TYPE</p>
<p>365.015 - X12 271 TIME PERIOD QUALIFIER</p>
<p>365.027 - X12 271 LOOP ID</p>
<p>365.036 - X12 271 DELIVERY PATTERN</p>
<p>365.044 - X12 271 CODE LIST QUALIFIER</p>
<p>365.032 - X12 271 DATE FORMAT QUALIFIER</p>
<p>365.031 - X12 271 ENTITY RELATIONSHIP CODE</p>
<p>365.043 - X12 271 ENTITY TYPE QUALIFIER</p>
<p>365.038 - X12 271 INJURY CATEGORY</p>
<p>365.034 - X12 271 LOCATION QUALIFER</p>
<p>365.046 - X12 271 MILITARY EMPLOYMENT STATUS CODE</p>
<p>365.041 - X12 271 MILITARY GOVT SERVICE</p>
<p>365.039 - X12 271 MILITARY PERSONNEL INFO STATUS CODE:</p>
<p>365.042 - X12 271 MILITARY SERVICE RANK</p>
<p>365.045 - X12 271 NATURE OF INJURY CODES</p>
<p>365.037 - X12 271 PATIENT RELATIONSHIP</p>
<p>365.035 - X12 271 PROCEDURE CODING METHOD</p>
<p>365.029 - X12 271 UNITS OF MEASUREMENT</p>
<p>365.033 - X12 271 YES/NO RESPONSE CODE</p></td>
<td><p>365.1 - IIV TRANSMISSION QUEUE</p>
<p>2.312 - INSURANCE TYPE subfile within the PATIENT file (#2)</p>
<p>365.18 - EIV EICD TRACKING</p>
<p>365.2 - IIV RESPONSE REVIEW</p></td>
</tr>
<tr class="even">
<td><p>365.011</p>
<p>X12 271 ELIGIBILITY/BENEFIT FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.012</p>
<p>X12 271 COVERAGE LEVEL FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.013</p>
<p>X12 271 SERVICE TYPE FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.014</p>
<p>X12 271 INSURANCE TYPE FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.015</p>
<p>X12 271 TIME PERIOD QUALIFIER FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.016</p>
<p>X12 271 QUANTITY QUALIFIER FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.017</p>
<p>X12 271 ERROR CONDITION FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>356.22 - HCS REVIEW TRANSMISSION FILE</p></td>
</tr>
<tr class="odd">
<td><p>365.018</p>
<p>X12 271 ERROR ACTION FILE</p></td>
<td></td>
<td>365 - IIV RESPONSE</td>
</tr>
<tr class="even">
<td><p>365.021</p>
<p>X12 271 CONTACT QUALIFIER FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.022</p>
<p>X12 271 ENTITY IDENTIFIER CODE FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p>
<p>356.22 - HCS REVIEW TRANSMISSION FILE</p></td>
</tr>
<tr class="even">
<td><p>365.023</p>
<p>X12 271 IDENTIFICATION QUALIFIER FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.024</p>
<p>X12 271 PROVIDER CODE FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.025</p>
<p>X12 271 DELIVERY FREQUENCY CODE FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p>
<p>356.22 - HCS REVIEW TRANSMISSION FILE</p></td>
</tr>
<tr class="odd">
<td><p>365.026</p>
<p>X12 271 DATE QUALIFIER FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.027</p>
<p>X12 271 LOOP ID FILE</p></td>
<td></td>
<td>356.22 - HCS REVIEW TRANSMISSION</td>
</tr>
<tr class="odd">
<td><p>365.028</p>
<p>X12 271 REFERENCE IDENTIFICATION FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.029</p>
<p>X12 271 UNITS OF MEASUREMENT</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.031</p>
<p>X12 271 ENTITY RELATIONSHIP CODE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.032</p>
<p>X12 271 DATE FORMAT QUALIFIER</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.033</p>
<p>X12 271 YES/NO RESPONSE CODE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.034</p>
<p>X12 271 LOCATION QUALIFER</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.034</p>
<p>X12 271 LOCATION QUALIFER</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.036</p>
<p>X12 271 DELIVERY PATTERN</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.037</p>
<p>X12 271 PATIENT RELATIONSHIP</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.038</p>
<p>X12 271 INJURY CATEGORY</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.039</p>
<p>X12 271 MILITARY PERSONNEL INFO STATUS CODE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.041</p>
<p>X12 271 MILITARY GOVT SERVICE AFFILIATION</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.042</p>
<p>X12 271 MILITARY SERVICE RANK</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.043</p>
<p>X12 271 ENTITY TYPE QUALIFIER</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.044</p>
<p>X12 271 CODE LIST QUALIFIER</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.045</p>
<p>X12 271 NATURE OF INJURY CODES</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="odd">
<td><p>365.046</p>
<p>X12 271 MILITARY EMPLOYMENT STATUS CODE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>2.312 - INSURANCE TYPE sub-file</p></td>
</tr>
<tr class="even">
<td><p>365.1</p>
<p>IIV TRANSMISSION QUEUE FILE</p></td>
<td><p>365 - IIV RESPONSE</p>
<p>365.14 - IIV TRANSMISSION STATUS</p>
<p>355.33 - INSURANCE VERIFICATION PROCESSOR</p>
<p>2 - PATIENT</p>
<p>365.12 - PAYER</p></td>
<td><p>365 - IIV RESPONSE</p>
<p>365.18 - EIV EICD TRACKING</p></td>
</tr>
<tr class="odd">
<td><p>365.11</p>
<p>IIV AUTO MATCH FILE</p></td>
<td>200 - NEW PERSON</td>
<td></td>
</tr>
<tr class="even">
<td><p>365.12</p>
<p>PAYER FILE</p></td>
<td><p>200 - NEW PERSON</p>
<p>365.13 - PAYER APPLICATION</p></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>350.9 - IB SITE PARAMETERS</p>
<p>365 - IIV RESPONSE</p>
<p>365.1 - IIV TRANSMISSION QUEUE</p>
<p>366.03 - PLAN</p></td>
</tr>
<tr class="odd">
<td><p>365.13</p>
<p>PAYER APPLICATION FILE</p></td>
<td></td>
<td>365.12 - PAYER</td>
</tr>
<tr class="even">
<td><p>365.14</p>
<p>IIV TRANSMISSION STATUS FILE</p></td>
<td></td>
<td><p>365 - IIV RESPONSE</p>
<p>365.1 - IIV TRANSMISSION QUEUE</p></td>
</tr>
<tr class="odd">
<td><p>365.15</p>
<p>IIV STATUS TABLE FILE</p></td>
<td></td>
<td>355.33 - INSURANCE VERIFICATION PROCESSOR</td>
</tr>
<tr class="even">
<td><p>365.18</p>
<p>EIV EICD TRACKING</p></td>
<td><p>2 - PATIENT</p>
<p>5 - STATE</p>
<p>365 - IIV RESPONSE</p>
<p>365.1 - IIV TRANSMISSION QUEUE</p>
<p>365.12 - PAYER</p></td>
<td>365.1 - IIV TRANSMISSION QUEUE</td>
</tr>
<tr class="odd">
<td><p>365.2</p>
<p>IIV RESPONSE REVIEW FILE</p></td>
<td><p>365 - IIV RESPONSE</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>366.01</p>
<p>NCPDP PROCESSOR FILE</p></td>
<td><p>366.11 - NCPDP PROCESSOR APPLICATION</p>
<p>200 - NEW PERSON</p></td>
<td>366.03 - PLAN</td>
</tr>
<tr class="odd">
<td><p>366.02</p>
<p>PHARMACY BENEFITS MANAGER (PBM) FILE</p></td>
<td><p>200 - NEW PERSON</p>
<p>366.12 - PHARMACY BENEFITS MANAGER (PBM) APPLICATION</p></td>
<td>366.03 - PLAN</td>
</tr>
<tr class="even">
<td><p>366.03</p>
<p>PLAN FILE</p></td>
<td><p>9002313.92 - BPS NCPDP FORMATS</p>
<p>366.01 - MCPDP PROCESSOR</p>
<p>200 - NEW PERSON</p>
<p>365.12 - PAYER</p>
<p>366.02 - PHARMACY BENEFITS MANAGER (PBM)</p>
<p>366.13 - PLAN APPLICATION</p></td>
<td>355.3 - GROUP INSURANCE PLAN</td>
</tr>
<tr class="odd">
<td><p>366.11</p>
<p>NCPDP PROCESSOR APPLICATION FILE</p></td>
<td></td>
<td>366.01 - NCPDP PROCESSOR</td>
</tr>
<tr class="even">
<td><p>366.12</p>
<p>PHARMACY BENEFITS MANAGER (PBM) APPLICATION FILE</p></td>
<td></td>
<td>366.02 - PHARMACY BENEFITS MANAGER (PBM)</td>
</tr>
<tr class="odd">
<td><p>366.13</p>
<p>PLAN APPLICATION FILE</p></td>
<td></td>
<td>366.03 - PLAN</td>
</tr>
<tr class="even">
<td><p>366.14</p>
<p>IB NCPDP EVENT LOG FILE</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>9002313.56 - BPS PHARMACIES</p>
<p>356.8 - CLAIMS TRACKING NON-BILLABLE REASONS</p>
<p>355.3 - GROUP INSURANCE PLAN</p>
<p>40.8 - MEDICAL CENTER DIVISION</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>52 - PRESCRIPTION</p>
<p>399.3 - RATE TYPE</p>
<p>5 - STATE</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>366.15</p>
<p>IB NCPDP PRESCRIPTION FILE</p></td>
<td><p>350 - INTEGRATED BILLING ACTION</p>
<p>399.3 - RATE TYPE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>366.16</p>
<p>IB NDC NON COVERED BY PLAN FILE</p></td>
<td><p>9002313.93 - BPS NCPDP REJECT CODES</p>
<p>355.3 - GROUP INSURANCE PLAN</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>366.17</p>
<p>IB NCPDP NON-BILLABLE REASONS</p></td>
<td></td>
<td>366.14 - IB NCPDP EVENT LOG</td>
</tr>
<tr class="even">
<td><p>367</p>
<p>HPID/OEID RESPONSE</p></td>
<td><p>367.1 - HPID/OEID TRANSMISSION QUEUE</p>
<p>367.11 - INSURANCE COMPANY ID TYPE</p></td>
<td>367.1 - HPID/OEID TRANSMISSION QUEUE</td>
</tr>
<tr class="odd">
<td><p>367.1</p>
<p>HPID/OEID TRANSMISSION QUEUE</p></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>367 - HPID/OEID RESPONSE</p>
<p>367.11 - INSURANCE COMPANY ID TYPE</p>
<p>5 - STATE</p>
<p>355.2 - TYPE OF COVERAGE</p></td>
<td>367 - HPID/OEID RESPONSE</td>
</tr>
<tr class="even">
<td><p>367.11</p>
<p>INSURANCE COMPANY ID TYPE</p></td>
<td></td>
<td><p>367 - HPID/OEID RESPONSE</p>
<p>367.1 - HPID/OEID TRANSMISSION QUEUE</p></td>
</tr>
<tr class="odd">
<td><p>368</p>
<p>HEALTH CARE CLAIM RFAI (277)</p></td>
<td><p>399 - BILL/CLAIMS</p>
<p>779.004 - COUNTRY CODE</p>
<p>81.3 - CPT MODIFIER</p>
<p>36 - INSURANCE COMPANY</p>
<p>95.3 - LAB LOINC</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>399.2 - REVENUE CODE</p>
<p>5 - STATE</p>
<p>365.021 - X12 271 CONTACT QUALIFIER</p>
<p>368.001 - X12 277 CLAIM STATUS CATEGORY</p>
<p>368.002 - X12 277 PRODUCT OR SERVICE ID</p>
<p>5.11 - ZIP CODE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>368.001</p>
<p>X12 277 CLAIM STATUS CATEGORY FILE</p></td>
<td></td>
<td>368 - HEALTH CARE CLAIM RFAI (277)</td>
</tr>
<tr class="odd">
<td><p>368.002</p>
<p>X12 277 PRODUCT OR SERVICE ID QUAL</p></td>
<td></td>
<td>368 - HEALTH CARE CLAIM RFAI (277)</td>
</tr>
<tr class="even">
<td><p>372</p>
<p>PFSS SITE PARAMETERS FILE</p></td>
<td><p>4 - INSTITUTION</p>
<p>3.8 - MAIL GROUP</p>
<p>200 - NEW PERSON</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>373</p>
<p>PFSS CHARGE CACHE FILE</p></td>
<td><p>81 - CPT</p>
<p>44 - HOSPITAL LOCATION</p>
<p>80 - ICD DIAGNOSIS</p>
<p>200 - NEW PERSON</p>
<p>100 - ORDER</p>
<p>2 - PATIENT</p>
<p>375 - PFSS ACCOUNT</p>
<p>440 - VENDOR</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>375</p>
<p>PFSS ACCOUNT FILE</p></td>
<td><p>409.1 - APPOINTMENT TYPE</p>
<p>40.7 - CLINIC STOP</p>
<p>81 - CPT</p>
<p>772 - HL7 MESSAGE TEXT</p>
<p>44 - HOSPITAL LOCATION</p>
<p>80 - ICD DIAGNOSIS</p>
<p>8.1 - MAS ELIGIBILITY CODE</p>
<p>40.8 - MEDICAL CENTER DIVISION</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>75.1 - RAD/NUC MED ORDERS</p>
<p>130 - SURGERY</p>
<p>45.3 - SURGICAL SPECIALTY</p></td>
<td><p>52 - PRESCRIPTION</p>
<p>75.1 - RAD/NUC MED ORDERS</p>
<p>100 - ORDER</p>
<p>130 - SURGERY</p>
<p>350 - INTEGRATED BILLING ACTION</p>
<p>373 - PFSS CHARGE CACHE</p>
<p>409.55 - APPOINTMENT PFSS ACCOUNT REFERENCE</p>
<p>660 - RECORD OF PROS APPLIANCE/REPAIR</p>
<p>9000010 - VISIT</p></td>
</tr>
<tr class="odd">
<td><p>390</p>
<p>ENROLLMENT RATED DISABILITY UPLOAD AUDIT FILE</p></td>
<td><p>31 - DISABILITY CONDITION</p>
<p>2 - PATIENT</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>391</p>
<p>TYPE OF PATIENT FILE</p></td>
<td>8.2 - IDENTIFICATION FORMAT</td>
<td>2 - PATIENT</td>
</tr>
<tr class="odd">
<td><p>391.1</p>
<p>AMIS SEGMENT FILE</p></td>
<td><p>40.8 - MEDICAL CENTER DIVISION</p>
<p>200 - NEW PERSON</p></td>
<td>2 - PATIENT</td>
</tr>
<tr class="even">
<td><p>391.31</p>
<p>HOME TELEHEALTH PATIENT FILE</p></td>
<td><p>4 - INSTITUTION</p>
<p>200 - NEW PERSON</p>
<p>2 - PATIENT</p>
<p>123 - REQUEST / CONSULTATION</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>399</p>
<p>BILL/CLAIMS FILE</p></td>
<td><p>353.5 - AMBULANCE CONDITION INDICATORS</p>
<p>353 - BILL FORM TYPE</p>
<p>399 - BILL/CLAIMS</p>
<p>81 - CPT</p>
<p>81.3 - CPT MODIFIER</p>
<p>80.2 - DRG</p>
<p>44 - HOSPITAL LOCATION</p>
<p>353.3 - IB ATTACHMENT REPORT TYPE</p>
<p>362.3 - IB BILL/CLAIMS DIAGNOSIS</p>
<p>350.8 - IB ERROR</p>
<p>355.96 - IB INS CO PROVIDER ID CARE UNIT</p>
<p>355.93 - IB NON/OTHER VA BILLING PROVIDER</p>
<p>355.97 - IB PROVIDER ID # TYPE</p>
<p>80 - ICD DIAGNOSIS</p>
<p>80.1 - ICD OPERATION / PROCEDURE</p>
<p>4 - INSTITUTION</p>
<p>36 - INSURANCE COMPANY</p>
<p>399.4 - MCCR INCONSISTEND DATA ELEMENT</p>
<p>399.1 - MCCR UTILITY</p>
<p>40.8 - MEDICAL CENTER DIVISION</p>
<p>200 - NEW PERSON</p>
<p>409.68 - OUTPATIENT ENCOUNTER</p>
<p>2 - PATIENT</p>
<p>8932.1 - PERSON CLASS</p>
<p>353.1 - PLACE OF SERVICE</p>
<p>45 - PTF</p>
<p>399.3 - RATE TYPE</p>
<p>399.2 - REVENUE CODE</p>
<p>5 - STATE</p>
<p>353.4 - TRANSPORT REASON CODE</p>
<p>353.2 - TYPE OF SERVICE</p>
<p>356.022 - X12 278 DENTAL NUMBERING SYSTEM</p>
<p>399.6 - CMN FORM TYPES</p></td>
<td><p>351.5 - TRICARE PHARMACY TRANSACTIONS</p>
<p>351.9 - CLAIMSMANAGER BILLS</p>
<p>356 - CLAIMS TRACKING</p>
<p>356.399 - CLAIMS TRACKING/BILL</p>
<p>361 - BILL STATUS MESSAGE</p>
<p>361.1 - EXPLANATION OF BENEFITS</p>
<p>361.4 - EDI TEST CLAIM STATUS MESSAGE</p>
<p>362.1 - IB AUTOMATED BILLING COMMENTS</p>
<p>362.3 - IB BILL/CLAIMS DIAGNOSIS</p>
<p>362.4 - IB BILL/CLAIMS PRESCRIPTION REFILL</p>
<p>362.5 - IB BILL/CLAIMS PROSTHETICS</p>
<p>364 - EDI TRANSMIT BILL</p>
<p>399 - BILL/CLAIMS</p>
<p>9002313.77 - BPS REQUESTS</p></td>
</tr>
<tr class="even">
<td><p>399.1</p>
<p>MCCR UTILITY FILE</p></td>
<td><p>350.1 - IB ACTION TYPE</p>
<p>399.1 - MCCR UTILITY</p></td>
<td><p>42.4 - SPECIALTY</p>
<p>363 - RATE SCHEDULE</p>
<p>363.1 - CHARGE SET</p>
<p>363.2 - CHARGE ITEM</p>
<p>399 - BILL/CLAIMS</p>
<p>399.1 - MCCR UTILITY</p>
<p>399.5 - BILLING RATES</p>
<p>487.81 - ODS DOD RATES</p>
<p>11500.61 - ODS BILLING SPECIALTY</p></td>
</tr>
<tr class="odd">
<td><p>399.2</p>
<p>REVENUE CODE FILE</p></td>
<td></td>
<td><p>36 - INSURANCE COMPANY</p>
<p>350.9 - IB SITE PARAMETERS</p>
<p>363.1 - CHARGE SET</p>
<p>363.2 - CHARGE ITEM</p>
<p>363.33 - BILLING REVENUE CODE LINKS</p>
<p>399.5 - BILLING RATES</p></td>
</tr>
<tr class="even">
<td><p>399.3</p>
<p>RATE TYPE FILE</p></td>
<td><p>430.2 - ACCOUNTS RECEIVABLE CATEGORY</p>
<p>430.6 - AR DEBT LIST</p></td>
<td><p>363 - RATE SCHEDULE</p>
<p>366.15 - IB NCPDP PRESCRIPTION</p>
<p>399 - BILL/CLAIMS</p>
<p>9002313.77 - BPS REQUESTS</p></td>
</tr>
<tr class="odd">
<td><p>399.5</p>
<p>BILLING RATES FILE</p></td>
<td><p>399.1 - MCCR UTILITY</p>
<p>399.2 - REVENUE CODE</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>399.6</p>
<p>CMN FORM TYPES</p></td>
<td></td>
<td>399 - BILL/CLAIMS</td>
</tr>
</tbody>
</table>

<span id="_Toc127633857" class="anchor"></span>Table : Options without Parents

# [<span id="_Toc129022440" class="anchor"></span>Exported Options](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Diagram Menu Options feature of the Kernel package may be used to generate printouts of full menus provided by IB.

<table>
<caption><p><span id="_Toc127633858" class="anchor"></span>Table : Exported Options</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Background Vet. Patients with Discharges and Ins</p>
<p>[IB BACKGRND VET DISCHS W/INS] Background Vet. Patients with Admissions and Ins</p>
<p>[IB BACKGRND VETS INPT W/INS]</p>
<p>Background Vet. Patients with Opt. Visits and Ins</p>
<p>[IB BACKGRND VETS OPT W/INS]</p></td>
<td>These report options may be queued to run regularly at the discretion of the facility.</td>
</tr>
<tr class="even">
<td><p>Clear Integrated Billing Filer Parameters</p>
<p>[IB FILER CLEAR PARAMETERS]</p></td>
<td>This option clears the IB site parameters that control the IB Background Filer. It is set up as a Start Up job that is executed when the CPU is rebooted.</td>
</tr>
<tr class="odd">
<td><p>Queue Means Test/Category C Compilation of Charges</p>
<p>[IB MT NIGHT COMP]</p></td>
<td>This option executes jobs for Claims Tracking, the Auto Biller, and Means Test billing. It should be queued to run each evening after the G&amp;L recalculation has been completed.</td>
</tr>
<tr class="even">
<td><p>Output IB Menu</p>
<p>[IB OUTPUT MENU]</p></td>
<td>This menu option is designed to be assigned to users outside of IB.</td>
</tr>
<tr class="odd">
<td><p>Return Messages Server</p>
<p>[IBCE MESSAGES SERVER]</p></td>
<td>This option controls the reading and storing of return messages generated as a result of the processing of Integrated Billing electronic transmissions with the Austin translator.</td>
</tr>
<tr class="even">
<td><p>View Insurance Management Menu</p>
<p>[IBCN VIEW INSURANCE DATA]</p></td>
<td>This menu contains view options to patient insurance and insurance company information. It was designed to be assigned to users outside of IB.</td>
</tr>
<tr class="odd">
<td>[IBCNF EII GET SERVER]</td>
<td>This is a server type option (not used by any user) that runs the GAITCMSG^IBCNFRD routine. Members of the IBN, IBX, IBK and IBH mail groups will receive the AITC DMI Queue confirmation messages for the four types of Extract files. The IBN mail group will also receive the results file messages.</td>
</tr>
<tr class="even">
<td>Send HPID/OEID Batch Queries<br />
[IBCNH HPID NIF BATCH QUERY]</td>
<td><p>This option does not appear on any VistA user menu and is for a one-time use with IB*2.0*519. It is *not* to be executed by a VistA user. Once this option is run once, it will be marked as ‘OUT OF ORDER’.</p>
<p>When the eInsurance staff is informed by FSC that the National Insurance File (NIF) is ready to exchange HL7 messages for a given VistA site, this option will be remotely executed at the specified VistA site. The receipt of a MailMan message by the VistA mail group “NIFQRY” with the subject line of “TRIGGER BATCH QUERY” will result in the execution of this option.</p>
<p>The purpose of this option is to retrieve the NIF ID's and HPID / OEID data from the NIF and load it into the VistA system. This option will kick off one HL7 message per insurance company. Running this option will set the HPID / OEID Active? flag in the IB SITE PARAMETERS file (#350.9) to 1 for Active that will indicate to VistA that the NIF is ready to send and receive Insurance Company HL7 updates to and from the site.</p></td>
</tr>
<tr class="odd">
<td><p>Auto-Build Average Bill Amounts</p>
<p>[IBT MONTHLY AUTO GEN AVE BILL]</p></td>
<td>This option should be scheduled to run automatically once a month. No device is necessary. It will build and store the number of inpatient and outpatient bills authorized and the total dollar amounts of the bills. A mail message is generated when the job has successfully completed.</td>
</tr>
<tr class="even">
<td><p>Auto-Generate Unbilled Amounts Report</p>
<p>[IBT MONTHLY AUTO GEN UNBILLED]</p></td>
<td>This option should be scheduled to run automatically once a month on or about the first of the month. No device is necessary. It will build and store the unbilled amounts data and send a mail message with the necessary results. The new site parameter, AUTO PRINT UNBILLED LIST, will allow for sites to pre-determine if a detailed listing should be printed each month.</td>
</tr>
<tr class="odd">
<td>Master Type of Plan Association [IBMTOP ASSN]</td>
<td>This option enables users to associate TYPE OF PLAN file (#355.1) entries with the MASTER TYPE OF PLAN file (#355.99).</td>
</tr>
<tr class="even">
<td>Master Type of Plan Report [IB MASTER TYPE OF PLAN RPT]</td>
<td>This report prints the Plan Types from the TYPE OF PLAN (#355.1) file and each Plan Type's mapping relationship to the MASTER TYPE OF PLAN (#355.99) file.</td>
</tr>
<tr class="odd">
<td>Urgent Care synch copay file across facilities [IBUC MULTI FAC COPAY SYNCH]</td>
<td>This option should not be placed on any menu or run by any user. It is designed to be scheduled in TaskMan to be executed once a day during off-peak hours. This option is a nightly task that updates COPAY data across a user's treating facilities.</td>
</tr>
<tr class="even">
<td><p>Background Vet. Patients with Discharges and Ins</p>
<p>[IB BACKGRND VET DISCHS W/INS] Background Vet. Patients with Admissions and Ins</p>
<p>[IB BACKGRND VETS INPT W/INS]</p>
<p>Background Vet. Patients with Opt. Visits and Ins</p>
<p>[IB BACKGRND VETS OPT W/INS]</p></td>
<td>These report options may be queued to run regularly at the discretion of the facility.</td>
</tr>
<tr class="odd">
<td><p>Clear Integrated Billing Filer Parameters</p>
<p>[IB FILER CLEAR PARAMETERS]</p></td>
<td>This option clears the IB site parameters that control the IB Background Filer. It is set up as a Start Up job that is executed when the CPU is rebooted.</td>
</tr>
<tr class="even">
<td><p>Queue Means Test/Category C Compilation of Charges</p>
<p>[IB MT NIGHT COMP]</p></td>
<td>This option executes jobs for Claims Tracking, the Auto Biller, and Means Test billing. It should be queued to run each evening after the G&amp;L recalculation has been completed.</td>
</tr>
<tr class="odd">
<td><p>Output IB Menu</p>
<p>[IB OUTPUT MENU]</p></td>
<td>This menu option is designed to be assigned to users outside of IB.</td>
</tr>
<tr class="even">
<td><p>Return Messages Server</p>
<p>[IBCE MESSAGES SERVER]</p></td>
<td>This option controls the reading and storing of return messages generated as a result of the processing of Integrated Billing electronic transmissions with the Austin translator.</td>
</tr>
<tr class="odd">
<td><p>eInsurance Night Process</p>
<p>[IBCN EINSURANCE NIGHT PROCESS]</p></td>
<td>This option is not to be placed on any menu nor run by any user. This option is specifically designed to be scheduled in TaskMan to be executed once a day during off-peak hours. Running this more than once a day may cause unexpected results. This option controls jobs for the eBusiness eInsurance team. (It is used mostly for, but not limited to, the eIV and the IIU interfaces.)</td>
</tr>
<tr class="even">
<td><p>View Insurance Management Menu</p>
<p>[IBCN VIEW INSURANCE DATA]</p></td>
<td>This menu contains view options to patient insurance and insurance company information. It was designed to be assigned to users outside of IB.</td>
</tr>
<tr class="odd">
<td>[IBCNF EII GET SERVER]</td>
<td>This is a server type option (not used by any user) that runs the GAITCMSG^IBCNFRD routine. Members of the IBN, IBX, IBK and IBH mail groups will receive the AITC DMI Queue confirmation messages for the four types of Extract files. The IBN mail group will also receive the results file messages.</td>
</tr>
<tr class="even">
<td>Send HPID/OEID Batch Queries<br />
[IBCNH HPID NIF BATCH QUERY]</td>
<td><p>This option does not appear on any VistA user menu and is for a one-time use with IB*2.0*519. It is *not* to be executed by a VistA user. Once this option is run once, it will be marked as ‘OUT OF ORDER’.</p>
<p>When the eInsurance staff is informed by FSC that the National Insurance File (NIF) is ready to exchange HL7 messages for a given VistA site, this option will be remotely executed at the specified VistA site. The receipt of a MailMan message by the VistA mail group “NIFQRY” with the subject line of “TRIGGER BATCH QUERY” will result in the execution of this option.</p>
<p>The purpose of this option is to retrieve the NIF ID's and HPID / OEID data from the NIF and load it into the VistA system. This option will kick off one HL7 message per insurance company. Running this option will set the HPID / OEID Active? flag in the IB SITE PARAMETERS file (#350.9) to 1 for Active that will indicate to VistA that the NIF is ready to send and receive Insurance Company HL7 updates to and from the site.</p></td>
</tr>
<tr class="odd">
<td><p>Auto-Build Average Bill Amounts</p>
<p>[IBT MONTHLY AUTO GEN AVE BILL]</p></td>
<td>This option should be scheduled to run automatically once a month. No device is necessary. It will build and store the number of inpatient and outpatient bills authorized and the total dollar amounts of the bills. A mail message is generated when the job has successfully completed.</td>
</tr>
<tr class="even">
<td><p>Auto-Generate Unbilled Amounts Report</p>
<p>[IBT MONTHLY AUTO GEN UNBILLED]</p></td>
<td>This option should be scheduled to run automatically once a month on or about the first of the month. No device is necessary. It will build and store the unbilled amounts data and send a mail message with the necessary results. The new site parameter, AUTO PRINT UNBILLED LIST, will allow for sites to pre-determine if a detailed listing should be printed each month.</td>
</tr>
<tr class="odd">
<td>Master Type of Plan Association [IBMTOP ASSN]</td>
<td>This option enables users to associate TYPE OF PLAN file (#355.1) entries with the MASTER TYPE OF PLAN file (#355.99).</td>
</tr>
<tr class="even">
<td>Master Type of Plan Report [IB MASTER TYPE OF PLAN RPT]</td>
<td>This report prints the Plan Types from the TYPE OF PLAN (#355.1) file and each Plan Type's mapping relationship to the MASTER TYPE OF PLAN (#355.99) file.</td>
</tr>
<tr class="odd">
<td>Urgent Care synch copay file across facilities [IBUC MULTI FAC COPAY SYNCH]</td>
<td>This option should not be placed on any menu or run by any user. It is designed to be scheduled in TaskMan to be executed once a day during off-peak hours. This option is a nightly task that updates COPAY data across a user's treating facilities.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633858" class="anchor"></span>Table : Exported Options

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc127633859" class="anchor"></span>Table : Criteria be met to Purge Billing Data</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IB ACTIVATE REVENUE CODES</td>
<td>This option allows the user to activate the revenue codes which that site has chosen to use for its third-party billing.</td>
</tr>
<tr class="even">
<td>IB AUTHORIZE BILL GENERATION</td>
<td>This option allows the user to perform final review of information contained in a billing record. The user is then able to authorize the generation of the bill and the release of the information to Fiscal.</td>
</tr>
<tr class="odd">
<td>IB AUTO BILLER PARAMS</td>
<td>Enter and edit the parameters controlling Automated Billing. Security key IB PARAMETER EDIT required.</td>
</tr>
<tr class="even">
<td>IB BACKGRND VET DISCHS W/INS</td>
<td>This option may be set to be queued once per week to run and generate a list of Veterans with Insurance and Discharges.</td>
</tr>
<tr class="odd">
<td>IB BACKGRND VETS INPT W/INS</td>
<td>This option may be set to be queued once per week to run and generate a list of Veterans with Insurance and Admissions.</td>
</tr>
<tr class="even">
<td>IB BACKGRND VETS OPT W/INS</td>
<td>This option may be set to be queued once per week to run and generate a list of Veterans with Insurance and Outpatient Visits.</td>
</tr>
<tr class="odd">
<td>IB BATCH PRINT BILLS</td>
<td>Queues all authorized bills that have not been flagged for transmission to print in user specified order.</td>
</tr>
<tr class="even">
<td>IB BILL STATUS REPORT</td>
<td>This option generates a summary (count and amount) of bill rate types and statuses.</td>
</tr>
<tr class="odd">
<td>IB BILLING CLERK MENU</td>
<td>This menu contains the basic Medical Care Cost Recovery Billing Module options. Through this option, a user may inquire to billing records, generate a limited number of reports, and with the proper security keys, may also establish and review billing records.</td>
</tr>
<tr class="even">
<td>IB BILLING RATES FILE</td>
<td>This option allows enter/edit of Billing Rates that will be used in the automatic calculation of costs when preparing a third-party bill.</td>
</tr>
<tr class="odd">
<td>IB BILLING SUPERVISOR MENU</td>
<td>This menu contains all the Medical Care Cost Recovery Billing Module options. Through this option, a user may accomplish every phase of the billing process and access all billing reports.</td>
</tr>
<tr class="even">
<td>IB BILLING TOTALS REPORT</td>
<td>This report is sorted by rate type and prints all billing totals for each rate type.</td>
</tr>
<tr class="odd">
<td>IB CANCEL BILL</td>
<td>This option allows the user to cancel a bill. A mandatory comment field exists to document the reason for cancellation, and a log is maintained to audit responsible user and date/time bill is cancelled. A bulletin is sent to the billing supervisor each time a bill is cancelled.</td>
</tr>
<tr class="even">
<td>IB CANCEL/EDIT/ADD CHARGES</td>
<td>This option will allow the user to directly cancel, edit, or add to patient charges.</td>
</tr>
<tr class="odd">
<td>IB CIDC INSURANCE SWITCH</td>
<td>This option allows editing of the CIDC Insurance Switch. This switch should be changed with great caution as it can affect multiple packages and users.</td>
</tr>
<tr class="even">
<td>IB CLEAN AUTO BILLER LIST</td>
<td>Deletes all entries from the auto biller results list before a certain date.</td>
</tr>
<tr class="odd">
<td>IB COPY AND CANCEL</td>
<td>This option will allow cancelling a bill and then will create an exact duplicate bill except its status will be ENTERED / NOT REVIEWED.</td>
</tr>
<tr class="even">
<td>IB COPY SECOND/THIRD</td>
<td>This option is used to create Secondary and Tertiary bills. The Primary bill is copied to create the bill to the Secondary payer. The Secondary bill is copied to create the bill to the Tertiary payer. The bill being copied is not cancelled.</td>
</tr>
<tr class="odd">
<td>IB CORRECT REJECTED/DENIED</td>
<td>This option will allow correcting a rejected or denied bill that has not had any payments posted to it.</td>
</tr>
<tr class="even">
<td>IB DRUGS NON COVERED REPORT</td>
<td>This option will print non covered drugs, plans and dates.</td>
</tr>
<tr class="odd">
<td>IB ECME BILLING EVENTS</td>
<td>This option prints the ECME Billing Events Report.</td>
</tr>
<tr class="even">
<td>IB EDIT BILLING INFO</td>
<td>This option allows the user to enter the information required to generate a third-party bill and to edit existing billing information.</td>
</tr>
<tr class="odd">
<td>IB EDIT E&amp;M CODE QUANTITY FLAG</td>
<td>Runs the input template IB EDIT E&amp;M QUANTITY to set the value for the E&amp;M CODE QUANTITY FLAG. (Field .06 of file 357.69).</td>
</tr>
<tr class="even">
<td>IB EDIT RETURNED BILL</td>
<td>This option will allow users to edit a bill that has been returned from AR to MCCR and return it back to A/R.</td>
</tr>
<tr class="odd">
<td>IB EDIT SITE PARAMETERS</td>
<td>This option allows entering and editing of Integrated Billing Site Parameter file. Modifying the site parameters can affect the performance of Integrated Billing's background filer. Security key IB PARAMETER EDIT required.</td>
</tr>
<tr class="even">
<td>IB FILER CLEAR PARAMETERS</td>
<td>This option will clear the IB site parameters to allow the IB filer to start on its own whenever it needs to. It will not edit the field, FILE IN BACKGROUND. It will only let the filer start when called if this field is set to yes. This option will be called as a startup job when the CPU is rebooted. It will clear the two IB parameters that prevent the IB filer from restarting if the CPU crashed while the filer was running.</td>
</tr>
<tr class="odd">
<td>IB FILER START</td>
<td>This option will task the IB background filer to run whether a filer is currently running. This option can be used when a filer job has terminated unexpectedly and won't restart itself. This will force a filer to start running.</td>
</tr>
<tr class="even">
<td>IB FILER STOP</td>
<td>This option will cause the IB background filer to cease when it has finished processing all its known transactions. Processing with Accounts Receivable will then be accomplished in the foreground.</td>
</tr>
<tr class="odd">
<td>IB FLAG CONTINUOUS PATIENTS</td>
<td>This option can be used to add or edit entries in the file of patient continuously hospitalized since 1986. These patients are exempt from the co-payment portion of the means test but may still be charged the per diem. The automated category C billing software will exempt these patients from the co-payments. In order to be considered continuously hospitalized the patient must not have changed levels of care, i.e., gone from a NHCU to the hospital.</td>
</tr>
<tr class="even">
<td>IB GENERATE ECME RX BILLS</td>
<td>This option is for Back-Billing purposes. It allows resending a single or multiple prescription through ECME for electronic billing.</td>
</tr>
<tr class="odd">
<td>IB GMT MONTHLY TOTALS</td>
<td></td>
</tr>
<tr class="even">
<td>IB GMT SINGLE PATIENT REPORT</td>
<td>The option calls the GMT Single Patient Report.</td>
</tr>
<tr class="odd">
<td>IB HCCH PAYER ID REPORT</td>
<td>The option calls the HCCH Payer ID Report. (IB*2.0*577).</td>
</tr>
<tr class="even">
<td>IB INPATIENT VET REPORT</td>
<td>This option prints a list of all patients with non-service-connected disabilities who have insurance and who had inpatient admissions during a user-specified date range. Eligibility status is provided for each patient on list.</td>
</tr>
<tr class="odd">
<td>IB LIST ALL BILLS FOR PAT.</td>
<td>This option will print a list of all bills for one patient.</td>
</tr>
<tr class="even">
<td>IB LIST BILLS FOR EPISODE</td>
<td>This option will list all bills related to an episode of care.</td>
</tr>
<tr class="odd">
<td>IB LIST OF BILLING RATES</td>
<td>This option will print a list of Billing Rates by Effective date.</td>
</tr>
<tr class="even">
<td>IB MANAGER MENU</td>
<td>This is the master IB menu that will contain all the IB options.</td>
</tr>
<tr class="odd">
<td>IB MEANS TEST MENU</td>
<td>This menu contains the options to manage the automated charges that are generated for Category C veterans.</td>
</tr>
<tr class="even">
<td>IB MRA BACKBILLING REPORT</td>
<td>This option is to be used to produce a report and / or send data on the potential recoveries of old claims to carriers that have consistently refused to reimburse the VA for Medicare supplemental policies.</td>
</tr>
<tr class="odd">
<td>IB MRA EDIT INS CO LIST</td>
<td>Use this option to create a list of Insurance Companies that are primarily Medicare supplemental carriers. These carriers have consistently been denied payments to the VA due to the VA's inability to produce an EOB from Medicare showing the Medicare allowable charges and the patient’s responsibility for the claim, for example, USAA.</td>
</tr>
<tr class="even">
<td>IB MRA EXTRACT</td>
<td>This option is used to queue the MRA extract.</td>
</tr>
<tr class="odd">
<td>IB MT BILLABLE STOPS</td>
<td>This option will print the billable types (stop codes) for co-pay visits. There is an option to deliver the report to the user in mailman or print the report to a printer or on the screen.</td>
</tr>
<tr class="even">
<td>IB MT BILLING REPORT</td>
<td>This report is used to list all Means Test and LTC charges within a user-specified date range.</td>
</tr>
<tr class="odd">
<td>IB MT CLOCK INQUIRY</td>
<td>Allows inquiry to the Means Test co-pay patient’s number of inpatient days and amounts billed.</td>
</tr>
<tr class="even">
<td>IB MT CLOCK MAINTENANCE</td>
<td>This option will allow adding or editing of Patient Billing Clocks.</td>
</tr>
<tr class="odd">
<td>IB MT DISP SPECIAL CASES</td>
<td>This option is used to enter the reason for not billing special inpatient billing cases.</td>
</tr>
<tr class="even">
<td>IB MT ESTIMATOR</td>
<td>This report is used to estimate the Means Test charges for an episode of Hospital or Nursing Home Care, given a proposed length of stay. The report may also be used to determine the remaining charges that will be billed to a current inpatient.</td>
</tr>
<tr class="odd">
<td>IB MT FIX/DISCH SPECIAL CASE</td>
<td>This option will update records in the Special Inpatient Billing Cases File (#351.2) with discharge dates, if any exist in the Patient Movement File (#405).</td>
</tr>
<tr class="even">
<td>IB MT FLAG OPT PARAMS</td>
<td>This option is used to flag stop codes, dispositions, and clinics that the site has determined to be exempt from the Means Test outpatient co-payment charge. These parameters are all flagged by date and may be inactivated and re-activated.</td>
</tr>
<tr class="odd">
<td>IB MT LIST FLAGGED PARAMS</td>
<td>This output is used to generate a list of all stop codes, dispositions, and clinics that are inactive as of a user-specified date.</td>
</tr>
<tr class="even">
<td>IB MT LIST HELD (RATE) CHARGES</td>
<td>This option is used to generate a list of all Means Test outpatient co-payment charges that have been placed on hold in Integrated Billing because the outpatient co-pay rate is over one year old.</td>
</tr>
<tr class="odd">
<td>IB MT LIST SPECIAL CASES</td>
<td>This option is used to list all special inpatient billing cases. After a case has been disposed, the output will include either the reason for non-billing, or all the charges that have been billed for the admission.</td>
</tr>
<tr class="even">
<td>IB MT LTC REMOTE QUERY</td>
<td>This option will allow the user to perform a remote query on a patient for both MT and LTC billing information.</td>
</tr>
<tr class="odd">
<td>IB MT NIGHT COMP</td>
<td><p>This job creates Means Test bills for all current inpatients through the previous day. The job should be queued to run each evening after the G&amp;L Recalculation has been completed.</p>
<p>In order to ensure that Pandemic period copays are properly cancelled and don't appear on patient statements, as required by the American Rescue Plan Act (ARPA) of 2021, the IB MT NIGHT COMP VistA TaskMan job will need to follow the scheduling criteria listed below:</p>
<ul>
<li><p>Starts shortly after midnight local time.</p></li>
<li><p>Starts after the DG G&amp;L RECALCULATION AUTO nightly process.</p></li>
<li><p>Starts at least 30 minutes prior to the start of the PRCA NIGHTLY PROCESS.</p></li>
</ul>
<p>You may need to reschedule the PRCA NIGHTLY PROCESS TaskMan job as well to ensure that it starts at least 30 minutes after the start of the IB MT NIGHT COMP TaskMan job.</p></td>
</tr>
<tr class="even">
<td>IB MT ON HOLD FIX</td>
<td><p>This option should be assigned to the person responsible for insuring IB Actions are processed correctly. This option should be deleted once the clean-up process is complete. Select this option to perform one of three actions:</p>
<ol type="1">
<li><blockquote>
<p>List all INTEGRATED BILLING ACTIONS with a status of INCOMPLETE.</p>
</blockquote></li>
<li><blockquote>
<p>List all INTEGRATED BILLING ACTIONS with a status of COMPLETE / PENDING AR.</p>
</blockquote></li>
<li><blockquote>
<p>Repost INTEGRATED BILLING ACTIONS with a status of COMPLETE / PENDING AR and pass these charges to AR.</p>
</blockquote></li>
</ol>
<p>When selecting item #3, the software will attempt to process the IB actions with a status of COMPLETE.</p>
<p>Some of these IB Actions will be placed ON HOLD with the ON HOLD DATE set to TODAY, while other IB Actions will be passed to AR and patients will be billed IMMEDIATELY.</p></td>
</tr>
<tr class="odd">
<td>IB MT ON HOLD MENU</td>
<td>This menu is used to group all options that are used to manage Integrated Billing actions that are placed on hold because the patient has insurance coverage or because the outpatient co-pay rate is over one year old.</td>
</tr>
<tr class="even">
<td>IB MT PASS CONV CHARGES</td>
<td>This option sends converted charges to accounts receivable. User can use Patient name or a Cutoff date as selection criteria.</td>
</tr>
<tr class="odd">
<td>IB MT PROFILE</td>
<td>The Means Test Billing Profile may be used to list, for a single patient, all Means Test charges that fall within a user-specified date range.</td>
</tr>
<tr class="even">
<td>IB MT REL HELD (RATE) CHARGES</td>
<td>This option is used to release charges that have been placed on hold in Integrated Billing because the outpatient co-pay rate is over one year old. If the new (less than one year old) rate has been entered into the Billing table, the option will prompt the user to task off a job that will automatically update the dollar amount and bill all such charges. The user will receive a bulletin when the tasked job has completed.</td>
</tr>
<tr class="odd">
<td>IB MT RELEASE CHARGES</td>
<td>This option is used to release Means Test charges that are 'on hold' awaiting claim disposition from the patient's insurance company. Any held up charges for a patient (that is specified by the user) may be selected and passed to Accounts Receivable. This option will also be accessed from the 'Enter a Payment' option in the Accounts Receivable package. If the user posts a payment from an insurance company for a bill that has any 'held' charges associated with it, the user may opt to select any of the charges to pass to Accounts Receivable in order to post a portion of the insurance company's payment to the patient's bill.</td>
</tr>
<tr class="even">
<td>IB MT REV PEND CHARGES</td>
<td>This new option is introduced with IVM v2.0 to support the IVM process. When an IVM-verified Means Test is transmitted from the IVM Center to the field facility, Means Tests charges will be created, if necessary, for patients whose MT status has changed from NO to YES. These charges are not passed to Accounts Receivable but held in Billing in a new 'hold' (HOLD - REVIEW) status to await a manual review. This option is used to review all charges that are pending a review before being billed to the patient. Once reviewed, the charge may either be cancelled or passed to AR. If the charge is passed, billing information is passed to the IVM package to initiate the transmission of billing information back to the IVM Center.</td>
</tr>
<tr class="odd">
<td>IB OUTPATIENT VET REPORT</td>
<td>This option prints a list of all patients with non-service-connected disabilities who have insurance and who had outpatient visits during a user-specified date range. Eligibility status is provided for each patient on list.</td>
</tr>
<tr class="even">
<td>IB OUTPT VISIT DATE INQUIRY</td>
<td>This option displays a billing record that covers a specified outpatient visit. The user may select any patient with billed outpatient visits, and then the visit date in question. The option displays the same information as found in the Patient Billing Inquiry.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT AUTO BILLER</td>
<td>Prints the list of bills and comments resulting from the Automated Biller.</td>
</tr>
<tr class="even">
<td>IB OUTPUT CLK PROD</td>
<td>Lists number and type of bills entered by selected clerks, over a date range.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT CNT/AMT RPT</td>
<td>This option produces the Count and Dollar Amount of Charges on Hold Report. The report provides a subtotal and sub-count, by action type, of each patient charge with the status of ON HOLD. These charges have not been passed to Accounts Receivable. Accounting is responsible for supplying these figures to FMS on a monthly basis.</td>
</tr>
<tr class="even">
<td>IB OUTPUT CONTINUOUS PATIENTS</td>
<td>This option is a list of current inpatients continuously hospitalized at the same level of care since 1986.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT DAYS ON HOLD</td>
<td>This option produces the Days on Hold Report. The report lists all Integrated Billing charges that have been in the ON HOLD status for an extended period. Use the default to list charges that have been on hold for longer than 60 days.</td>
</tr>
<tr class="even">
<td>IB OUTPUT EMPLOYER REPORT</td>
<td>For patients without active insurance, this report will list the patients and / or the spouse’s employer.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT EVENTS REPORT</td>
<td>Report of clinic check-ins, stop codes, registrations, and charges for Category C patients.</td>
</tr>
<tr class="even">
<td>IB OUTPUT FULL INQ BY BILL NO</td>
<td>This option will display information about a bill. The bill may either be a third-party bill, a pharmacy co-pay bill, or a means test charge. If a full inquiry is selected for non-third-party bills, then additional information about the care or services is displayed when available.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT HELD CHARGES</td>
<td>This option produces the Held Charges Report. The report lists all charges having the status of ON HOLD. With each charge is listed bills that are for the same outpatient visit or the same inpatient admission with an overlap in the period covered. Users have the option of printing the report with or without Insurance information.</td>
</tr>
<tr class="even">
<td>IB OUTPUT HELD CHARGES/PT</td>
<td><p>This option lists all IB Actions for a patient that is currently on hold or was on hold for a user specified date range. The report lists IB Action ID, Rate Type, Bill #, AR status, IB Status, and information related to corresponding Third-Party Claims.</p>
<ol start="6">
<li><p>Only those charges placed on hold since the installation of patch IB*2*70 will appear on this report.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>IB OUTPUT HISTORY OF HELD CHGS</td>
<td>This option provides a count and dollar total of charges that have been on hold for a date range. The report sorts charges by current status. Sites will be able to keep track of how many charges were cancelled, released (billed), or remain on hold. This report only counts charges with an ON HOLD DATE defined.</td>
</tr>
<tr class="even">
<td>IB OUTPUT IB INQ</td>
<td>This option will display a captioned inquiry of one IB Action.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT INPTS WITHOUT INS</td>
<td>This option will produce a list of either current inpatients or admissions for a date range where the patient has either unknown insurance or the insurance is expired.</td>
</tr>
<tr class="even">
<td>IB OUTPUT INQ BY PATIENT</td>
<td>This inquiry will provide a brief display of IB actions for select patients for a selected date range.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT IVM BILLING ACTIVITY</td>
<td>This option is used to generate a list of bills that have been generated against insurance policies that were identified by the IVM Center. The user has the option of electronically transmitting the report to the IVM Center when the option is executed in the Production account.</td>
</tr>
<tr class="even">
<td>IB OUTPUT LIST ACTIONS</td>
<td>This option will print the IB actions by a user selected date range. The user may also select an additional field to sort by, such as status.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT MANAGEMENT REPORTS</td>
<td>This menu contains reports that provide statistics or lists of bills that can be used in managing the Billing program.</td>
</tr>
<tr class="even">
<td>IB OUTPUT MENU</td>
<td>This menu contains Inquiry and report options for Integrated Billing</td>
</tr>
<tr class="odd">
<td>IB OUTPUT MOST COMMON OPT CPT</td>
<td>This option will list the most common Ambulatory Procedures and Ambulatory Surgeries performed in a date range for a given set of clinics. This can be used to help build the CPT Check-off Sheets.</td>
</tr>
<tr class="even">
<td>IB OUTPUT OPTS WITHOUT INS</td>
<td>This report will produce a list of patients for clinic appointments that have unknown or expired insurance.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT PATIENT REPORT MENU</td>
<td>This menu contains the Billing reports that deal with one or a group of patients. This includes all billing lists of patients and billing inquiries.</td>
</tr>
<tr class="even">
<td>IB OUTPUT PRE-REG SOURCE REPT</td>
<td>This report will print bills and payments within the user selected date range that are associated to an insurance policy with a source of information equal to the user selected criteria.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT RANK CARRIERS</td>
<td>This option is used to generate a listing of insurance carriers ranked by the total amount billed. The user may specify a date range from which bills should be selected, as well as the number of carriers to be ranked. This output must be transmitted to the MCCR Program Office after the beginning of the fiscal year. The selected date range should be the entire fiscal year (i.e., 10/1/92 through 9/30/93) and 30 carriers should be ranked. First run the report without transmitting in order to first review the results. When the report is being run in the Production account, the user will always transmit the report centrally. The central mail group is G.MCCR DATA@FORUM.VA.GOV, which is stored as a parameter in field #4.05 in the IB SITE PARAMETERS (#350.9) file.</td>
</tr>
<tr class="even">
<td>IB OUTPUT RELEASED CHARGES RPT</td>
<td>This report lists all charges identified as once being ON HOLD or on HOLD-REVIEW status that currently have a status of BILLED and the DATE LAST UPDATED falls within the date range the user specifies.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT ROI EXPIRED</td>
<td>This report lists the ROI Special Consents that will expire within a user-specified date range.</td>
</tr>
<tr class="even">
<td>IB OUTPUT STATISTICAL REPORT</td>
<td>This report lists the total number of Integrated Billing actions by Action type along with the total charge by type for a date range. The net totals are also printed. The net totals are derived by looking at the last update for a parent even though the update may not be within the date range. The net total within a date range can be derived by the formula "new-update-cancel" for any associated action types.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT TREND REPORT</td>
<td>This option allows the user to analyze payment trends among insurance companies. In addition, it may be used to track receivables that are due the Medical Center. Many different criteria may be specified to limit the selection of bills, such as Rate Type, Impatient/Outpatient, Treatment Dates, Bill Printed Dates, and Insurance Company. Any additional field may also be selected and analyzed depending upon its content.</td>
</tr>
<tr class="even">
<td>IB OUTPUT VERIFY RX LINKS</td>
<td>This option will compare the soft link stored in Integrated Billing with the pointer in the prescription file pointing back to Integrated Billing. A report will print out of all IB Actions that do not verify.</td>
</tr>
<tr class="odd">
<td>IB OUTPUT VETS BY DISCH</td>
<td>List of Veteran discharges by division that is billable.</td>
</tr>
<tr class="even">
<td>IB PATIENT BILLING INQUIRY</td>
<td>This option displays all the actions that have been performed on a specified billing record. The user may select by patient name or bill number a record, and is shown bill status, total charges, statement covers period, and all previous actions of that billing record.</td>
</tr>
<tr class="odd">
<td>IB PROVIDER FROM FB DETAIL</td>
<td>This option prints all records modified by the FB PAID TO IB background process for a date range (For Future Use to Validate Testing).</td>
</tr>
<tr class="even">
<td>IB PROVIDER FROM FB RPTS MENU</td>
<td>This menu option allows users to run reports about records in the IB NON/OTHER BILLING PROVIDER (#355.93) file that have been affected by the FB PAID TO IB background job (For Future Use to Validate Testing).</td>
</tr>
<tr class="odd">
<td>IB PROVIDER FROM FB SUMMARY</td>
<td>This option identifies and reports on entries in the IB NON/OTHER VA BILLING PROVIDER (#355.93) file that were added or changed by the FEE BASIS PAID TO IB interface for a date range (For Future Use to Validate Testing).</td>
</tr>
<tr class="even">
<td>IB PRINT BILL</td>
<td>This option allows the user to print a third-party bill after all required information has been input, and after the billing information has been reviewed and authorized. A reimbursable insurance bill that has been flagged for transmission cannot be printed before it has been transmitted at least once.</td>
</tr>
<tr class="odd">
<td>IB PRINT BILL ADDENDUM</td>
<td>Prints the Addendum sheets that may accompany CMS-1500 Rx Refill or Prosthetics bills. The addendum contains information that could not fit on the bill form.</td>
</tr>
<tr class="even">
<td>IB PRINTED CLAIMS REPORT</td>
<td>This option will generate a report of claims for a specified timeframe that were locally printed but had the potential to be transmitted electronically.</td>
</tr>
<tr class="odd">
<td>IB PURGE BILLING DATA</td>
<td>This option may be used to purge data from the following files: #350 INTEGRATED BILLING ACTION #351 CATEGORY C BILLING CLOCK #399 BILL/CLAIMS Entries from these files must be archived before purged.</td>
</tr>
<tr class="even">
<td>IB PURGE DELETE TEMPLATE ENTRY</td>
<td>This option may be used to prevent a record from being purged from the database. The user will be prompted for an established Search Template based on one of the following three files: 350 INTEGRATED BILLING ACTION 351 CATEGORY C BILLING CLOCK 399 BILL/CLAIMS The records stored in this template will be listed, and the user may select a record to be deleted from the template.</td>
</tr>
<tr class="odd">
<td>IB PURGE LIST LOG ENTRIES</td>
<td>This option may be used to list all the log entries in the IB ARCHIVE/PURGE LOG file, #350.6. All entries in the file are listed, in the order added to the file.</td>
</tr>
<tr class="even">
<td>IB PURGE LIST TEMPLATE ENTRIES</td>
<td>This option may be used to list all entries in a Search Template that are scheduled to be archived and purged.</td>
</tr>
<tr class="odd">
<td>IB PURGE LOG INQUIRY</td>
<td>This option may be used to provide a full inquiry of any entry in the IB ARCHIVE/PURGE LOG, file #350.6.</td>
</tr>
<tr class="even">
<td>IB PURGE MENU</td>
<td>This menu contains all the Integrated billing purge options</td>
</tr>
<tr class="odd">
<td>IB PURGE/ARCHIVE BILLING DATA</td>
<td>This option may be used to archive data from the following files: #350 INTEGRATED BILLING ACTION #351 CATEGORY C BILLING CLOCK #399 BILL/CLAIMS Entries from these files must be found and placed in the appropriate Search (Sort) template, before archived.</td>
</tr>
<tr class="even">
<td>IB PURGE/BASC TRANSFER CLEANUP</td>
<td>Delete all CPT entries in the temporary file that have been transferred to the permanent billing file.</td>
</tr>
<tr class="odd">
<td>IB PURGE/FIND BILLING DATA</td>
<td>This option may be used to identify records to be archived and purged from the following files: #350 INTEGRATED BILLING ACTION #351 CATEGORY C BILLING CLOCK #399 BILL/CLAIMS Entries that are selected to be archived and then purged are placed into a Search (Sort) template.</td>
</tr>
<tr class="even">
<td>IB OTH FSM ELIG. CHANGE REPORT</td>
<td>This option assists users in reviewing past encounters of Former Service Member for potential back-billing charges. This report provides data for all Former OTH Service Members whose primary eligibility changed from EXPANDED MH CARE NON-ENROLLEE to their verified/determined (via Veterans Benefits Administration (VBA)) primary eligibility within a user specified date range.</td>
</tr>
<tr class="odd">
<td>IB REPOST</td>
<td>Option allows passing of IB action entries that did not successfully pass to AR to be reposted to the IB filer.</td>
</tr>
<tr class="even">
<td>IB RETURN BILL</td>
<td>This option will allow users to return a bill from MCCR to AR if it had previously been returned to MCCR from AR.</td>
</tr>
<tr class="odd">
<td>IB RETURN BILL LIST</td>
<td>This option will generate a list of bills returned by Accounts Receivable to MCCR. The output should be directed to a printer as this report may take a few minutes to print.</td>
</tr>
<tr class="even">
<td>IB RETURN BILL MENU</td>
<td>Menu to access options related to editing bills returned by A/R to MCCR and returning these to A/R.</td>
</tr>
<tr class="odd">
<td>IB REV CODE TOTALS</td>
<td>Print totals of Revenue Code amounts by Rate Type. To collect data for AMIS Segments 295 and 296.</td>
</tr>
<tr class="even">
<td>IB RX ADD THRESHOLDS</td>
<td>This option is used to add the Income Thresholds used in the Medication Co-payment Income Exemption.</td>
</tr>
<tr class="odd">
<td>IB RX EDIT LETTER</td>
<td>This option will allow editing of the header, or station name and address, and the main body of a letter. The letter IB NOW EXEMPT is the letter that was written to be sent to patients who become exempt during the conversion; it informs patients that there is no longer a need to send in a co-payment with Rx refill requests. The first six lines of the header field will be centered at the top of each letter. Do not center these lines. The patient address will print beginning on line 17. The main body will print after the patient address section. Do not include functions in either word processing field as VA FileMan utilities are not used at this time to output the letters.</td>
</tr>
<tr class="even">
<td>IB RX EXEMPTION MENU</td>
<td>This is the primary menu in IB for the options to manage and print reports on the Medication Co-payment Income Exclusion functionality.</td>
</tr>
<tr class="odd">
<td>IB RX HARDSHIP</td>
<td>This option can be used to give a hardship waiver from the Medication Co-payment. If a hardship is granted it will be good for one year from the date of the hardship. This option can also be used to update a single patient's exemption to the correct status as computed from his patient record, if the current exemption does not match what is computed.</td>
</tr>
<tr class="even">
<td>IB RX INQUIRE</td>
<td>This option will allow a brief inquiry to active exemptions or a full inquiry to the history of all exemptions for a patient.</td>
</tr>
<tr class="odd">
<td>IB RX PRINT EX LETERS</td>
<td>This option will print the form letter IB NOW EXEMPT for all currently exempt patients. The following patients will not be included: Deceased Patients Non-Veterans Patients who are rated SC greater than 50% The user will be allowed to sort by Exemption Status Date, and by Patient name. Optionally, the user can store the results of the search in a template named IB EXEMPTION LIST for local printing purposes.</td>
</tr>
<tr class="even">
<td>IB RX PRINT PAT. EXEMP.</td>
<td>This option can print a list of patients by exemption status or exemption reason. This will enable a facility to print a list of patients who are either exempt or non-exempt. Optionally the report can print only sub totals without printing the detailed patient listing.</td>
</tr>
<tr class="odd">
<td>IB RX PRINT RETRO CHARGES</td>
<td>This report will print a list of patients and Medication Co-payment charges that have been canceled due to the income exclusion. Initially this report will print a list of charges canceled during the installation / conversion process. The software may cancel other charges after installation and this report can be used to list those charges.</td>
</tr>
<tr class="even">
<td>IB RX PRINT THRESHOLDS</td>
<td>This option will print a listing of the Income Thresholds used in the Medication Co-payment Income Exemption process. The output is sorted by type of Threshold and Effective Date.</td>
</tr>
<tr class="odd">
<td>IB RX PRINT VERIFY EXEMP</td>
<td>This option can be used to search through the BILLING EXEMPTIONS file and compare the currently stored active exemption for each patient against what it calculates to be the correct exemption status for the patient based on current data in the MAS files. This report can be run to just print a list of discrepancies or it can be run to automatically update each incorrect exemption status. Initially the report should be run without updating the exemptions. The option Manually Change Co-pay Exemptions (Hardship) can be used to update exemptions to the correct status one patient at a time if desired.</td>
</tr>
<tr class="even">
<td>IB RX REPRINT REMINDER</td>
<td>This option is used to generate an Income Test reminder letter for a veteran who effective co-pay exemption is based upon income. When the letter is generated, the field REMINDER LETTER DATE (#.16) in the BILLING EXEMPTIONS (#354.1) file will be updated, for the exemption record that is the basis for sending the reminder letter, with the current date.</td>
</tr>
<tr class="odd">
<td>IB SC DETERMINATION CHANGE RPT</td>
<td>This option creates a report to display patients that have a Service-Connected determination change for co-pays being reset.</td>
</tr>
<tr class="even">
<td>IB SITE DEVICE SETUP</td>
<td>This option allows associating devices as the default answer when printing forms. This is used to enter the default device for AR for follow-up activity.</td>
</tr>
<tr class="odd">
<td>IB SITE MGR MENU</td>
<td>This menu contains the options for the System Manager to check on the status of Integrated Billing, edit site parameters, and manage the background filer.</td>
</tr>
<tr class="even">
<td>IB SITE STATUS DISPLAY</td>
<td>This option displays information from the IB site parameter file and pertinent information about the status of the IB background filer.</td>
</tr>
<tr class="odd">
<td>IB SYSTEM DEFINITION MENU</td>
<td>This option allows the user to set up the MCCR parameters necessary for third party billing.</td>
</tr>
<tr class="even">
<td>IB THIRD PARTY BILLING MENU</td>
<td>This menu contains the options necessary to create, edit, review, authorize, print, and cancel third party bills.</td>
</tr>
<tr class="odd">
<td>IB THIRD PARTY OUTPUT MENU</td>
<td>This option allows the user to generate any of the Third-Party Outputs.</td>
</tr>
<tr class="even">
<td>IB TP FLAG OPT PARAMS</td>
<td>This option is used to flag stop codes and clinics as either non-billable for Third Party billing or to be ignored by the Third-Party auto biller. These parameters are all flagged by date and may be inactivated and re-activated.</td>
</tr>
<tr class="odd">
<td>IB TP LIST FLAGGED PARAMS</td>
<td>This output is used to generate a list of all stop codes and clinics that are flagged as non-billable for Third Party billing or that should not be auto billed by the Third-Party auto biller on a user-specified date.</td>
</tr>
<tr class="even">
<td>IB TRICARE DEL REJECT</td>
<td>This option is used to delete entries from the TRICARE PHARMACY REJECTS (#351.52) file. Entries to be deleted are usually transmitted in error originally and are not going to be re-submitted.</td>
</tr>
<tr class="odd">
<td>IB TRICARE ENGINE START</td>
<td>This option is used to start the TRICARE Pharmacy billing engine. The option will cause four queued tasks to be run - two primary This option is used to start the TRICARE Pharmacy billing engine tasks (one used to submit claims for prescriptions to the TRICARE fiscal intermediary, and one to accept AWP updates) and two secondary tasks as backups to the primary tasks. If either primary task fails, the secondary task will become the primary task and spawn another secondary task.</td>
</tr>
<tr class="even">
<td>IB TRICARE ENGINE STOP</td>
<td>This option is used to gracefully terminate the TRICARE Pharmacy billing engines. Use of this option will cause all four queued tasks to shut down.</td>
</tr>
<tr class="odd">
<td>IB TRICARE MENU</td>
<td>This menu contains options and reports related to the billing of prescriptions and medical care provided to TRICARE patients.</td>
</tr>
<tr class="even">
<td>IB TRICARE REJECT</td>
<td>This output provides a list of all billing transmissions that were rejected by the TRICARE fiscal intermediary.</td>
</tr>
<tr class="odd">
<td>IB TRICARE RESUBMIT</td>
<td>This option is used to submit a claim for a TRICARE prescription that was not previously billed.</td>
</tr>
<tr class="even">
<td>IB TRICARE REVERSE</td>
<td>This option is used to cancel a claim and co-payment for a TRICARE prescription that was billed in error.</td>
</tr>
<tr class="odd">
<td>IB TRICARE TRANSMISSION</td>
<td>This output provides a list, by prescription fill date, of all billing transmissions sent to the TRICARE fiscal intermediary.</td>
</tr>
<tr class="even">
<td>IB VIEW CANCEL BILL</td>
<td>This option allows the user to select and view a bill that is in cancelled status.</td>
</tr>
<tr class="odd">
<td>IBAEC LTC BILLING MENU</td>
<td>This menu holds all the LTC menu options.</td>
</tr>
<tr class="even">
<td>IBAEC LTC BILLING PROFILE</td>
<td>Prints "LTC Single Patient Billing Profile" report.</td>
</tr>
<tr class="odd">
<td>IBAEC LTC CLOCK EDIT</td>
<td>This option allows users to edit the LTC co-pay billing clock. Change the start date of the clock and edit the free days.</td>
</tr>
<tr class="even">
<td>IBAEC LTC CLOCK INQUIRY</td>
<td>This option prints "LTC Billing Clock Inquiry" report, containing detailed information about selected LTC Billing Clock.</td>
</tr>
<tr class="odd">
<td>IBARXM CAP TRANS PUSH</td>
<td>This option will allow the user to try to "push" outpatient medication co-payment cap transactions to the other treating facilities for the patient. This is used to try to resolve problems with transmissions. The problems are usually identified by mail messages sent to the IB RX CO-PAY CAP ERROR mail group. To resolve these error messages first IRM should verify that the HL7 logical links are working correctly. Then with this option the user can select individual transactions to attempt to send or All un-transmitted transactions.</td>
</tr>
<tr class="even">
<td>IBARXM CO-PAY QUERY</td>
<td>This option will produce a report that will show what medication co-payments a patient has been billed for and not billed for. This option will allow the user to query remote facilities to get all the information and verify its accuracy. If there is a discrepancy, the amounts will be updated as well.</td>
</tr>
<tr class="odd">
<td>IBARXM FACILITY CAP SUMM RPT</td>
<td>This option will generate the Facility Pharmacy Co-Pay Cap Summary Report. The purpose of this report is to delineate six data elements required by the VHA Chief Business Office on a yearly basis.</td>
</tr>
<tr class="even">
<td>IBARXM NONBILLABLE CO-PAY</td>
<td>This report will show what medication co-payments were not billable as a result of the medication co-payment cap for the specified month / year.</td>
</tr>
<tr class="odd">
<td>IBARXM PATIENT CAP REPORT</td>
<td>This option will produce a list of patients that have either met or are above the cap for the date specified. Specify either a month/year or just a year.</td>
</tr>
<tr class="even">
<td>IBAT EXCEL REPORT</td>
<td>This report will allow the user to select which fields to print in an excel format. It uses a pike (|) as the excel delimiter.</td>
</tr>
<tr class="odd">
<td>IBAT INPT PROSTHETIC ITEMS</td>
<td>This option will allow entering / editing / deleting of items that should be billed for inpatient prosthetics. Items in here will be automatically billed by the nightly background job for inpatients. No other inpatient issued items will be automatically billed.</td>
</tr>
<tr class="even">
<td>IBAT PATIENT LIST</td>
<td><p>This report will generate lists of transfer pricing patients by facility or VISN.</p>
<ol type="1">
<li><blockquote>
<p>The data available on the report will include patient name, date of birth, primary eligibility, SSN, and VISN.</p>
</blockquote></li>
<li><blockquote>
<p>2. The report will be able to be sorted by patient, treating facility, or by VISN.</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="odd">
<td>IBAT PATIENT REPORT</td>
<td><p>This report will create a detailed listing of a transfer pricing statement by patient. This report will also aid in determining whether a billable third party is involved.</p>
<ol type="1">
<li><blockquote>
<p>Select a VISN (home or preferred VISN) for detailed data to accumulate from.</p>
</blockquote></li>
<li><blockquote>
<p>Select a date range with summary data inclusive.</p>
</blockquote></li>
<li><blockquote>
<p>Detail data will be available per patient on the report along with a subtotal per patient and a Grand Total.</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="even">
<td>IBAT SUMMARY REPORT</td>
<td><p>This report will create a transfer pricing statement summary. This bottom line to this overall summary yields the total number of episodes and total amounts of those episodes per VISN / facility or groups of VISN / facilities.</p>
<ol type="1">
<li><blockquote>
<p>Select one or more VISN / facilities (home or preferred VISN / facility) for summary data to accumulate from.</p>
</blockquote></li>
<li><blockquote>
<p>Select a date range for which those services were provided with summary data inclusive.</p>
</blockquote></li>
<li><blockquote>
<p>There is summary data on the report for Inpatient, Outpatient, Pharmacy, and a Grand Total of the three.</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="odd">
<td>IBAT TP MANAGEMENT</td>
<td>This is the main entry option for viewing and editing patients and transactions.</td>
</tr>
<tr class="even">
<td>IBAT TRANSFER PRICING MENU</td>
<td>This menu will hold all the Transfer Pricing menu options.</td>
</tr>
<tr class="odd">
<td>IBAT WORKLOAD REPORT</td>
<td><p>This report shall enable the user to create a transfer pricing statement workload detail. The emphasis of this report is on work detail via Units</p>
<ol type="1">
<li><blockquote>
<p>The user shall be able to select one or more VISN / facilities (home or preferred VISN / facility) for workload data to accumulate from.</p>
</blockquote></li>
<li><blockquote>
<p>The user shall be able to select a date range with summary data inclusive.</p>
</blockquote></li>
<li><blockquote>
<p>Workload detail data shall be available on the report along with the Grand Total.</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="even">
<td>IBBA BATCH DFT</td>
<td><p>The menu option is used to schedule via TaskManager the PFSS Charge Batch Processor. Normally, this option should be scheduled to run once daily at a time of low system activity. When the batch processor starts, it will set data into two fields in the PFSS SITE PARAMETERS file (#372):</p>
<ol type="1">
<li><blockquote>
<p>The CHARGE PROCESSOR RUNNING field (#.1) will be set to "YES.”</p>
</blockquote></li>
<li><blockquote>
<p>The CHARGE PROCESS START TIME field (#.11) will be set to the current system date/time.</p>
</blockquote></li>
</ol>
<p>When charge batch processing is complete, then:</p>
<ol type="1">
<li><blockquote>
<p>The CHARGE PROCESSOR RUNNING field (#.1) will be set to "NO.”</p>
</blockquote></li>
<li><blockquote>
<p>The CHARGE PROCESS START TIME field (#.11) will be deleted.</p>
</blockquote></li>
</ol>
<p>When a charge batch processor job is started, it always checks the status of the CHARGE PROCESSOR RUNNING field. If this field is set to "YES," then the job quits immediately. This ensures that only one batch processor is running at any given time.</p></td>
</tr>
<tr class="odd">
<td>IBCE 837 EDI MENU</td>
<td>This menu contains the options needed to process and maintain EDI 837 bill submission functions.</td>
</tr>
<tr class="even">
<td>IBCE 837 EDI REPORTS</td>
<td>This menu contains the options needed to define the types of electronic reports from the clearinghouse that the site needs to see and defines the text that should / should not allow automatic review and file for informational status messages. It also contains an option to purge old status messages, reports for maintaining the integrity of the return message subsystem and the option for reviewing electronically returned messages.</td>
</tr>
<tr class="odd">
<td>IBCE 837 MANUAL TRANSMIT</td>
<td>This job batches and transmits bills that are in authorized or Request MRA status for insurance companies flagged to transmit electronically via EDI. This job can be executed at any time to transmit bills awaiting extract.</td>
</tr>
<tr class="even">
<td>IBCE BATCH STATUS DETAIL</td>
<td></td>
</tr>
<tr class="odd">
<td>IBCE BATCHES PENDING TOO LONG</td>
<td>This report lists all batches by batch type that have been in a PENDING status and have not yet received confirmation of receipt from Austin for more than 1 day. Report includes pending since date and mail message # the batch is contained in.</td>
</tr>
<tr class="even">
<td>IBCE CLAIMS STATUS AWAITING</td>
<td>Used by bill staff to review the most current status messages received for a bill(s) and do follow-up on the bills. Users will be able to select a bill from the list to view the details and the entire message text as well as to mark the message as reviewed or under review and document user comments.</td>
</tr>
<tr class="odd">
<td>IBCE COB MANAGEMENT</td>
<td>This will be a list manager screen with the option available to print an associated report. Using the screen, billing staff will be able to follow up on bills for secondary and tertiary billing for non-MRA bills</td>
</tr>
<tr class="even">
<td>IBCE EDI BATCHES INCOMPLETE</td>
<td>This report lists all batches that have been resubmitted, but not all bills were included. These are batches that have at least one bill still not resubmitted or canceled.</td>
</tr>
<tr class="odd">
<td>IBCE EDI VIEW/PRINT EXTRACT</td>
<td>This option will display the EDI extract data for a bill.</td>
</tr>
<tr class="even">
<td>IBCE ELEC REPORT DISPOSITION</td>
<td>This option allows the site to determine which clearinghouse generated electronic canned reports are to be sent to the EDI mail group and which should be totally ignored when received at the site.</td>
</tr>
<tr class="odd">
<td>IBCE ELECTRONIC ERROR REPORT</td>
<td>This report provides a tool for billing personnel to identify the who, what, and where of errors in electronic billing process.</td>
</tr>
<tr class="even">
<td>IBCE EXTRACT STATUS</td>
<td>This is a list manager screen that will display bills that are trapped in a ready for extract status due to the EDI/MRA parameter being turned off. From here, the valid actions are cancelling a bill, cancel / clone / authorize a bill without user interaction, or print the report.</td>
</tr>
<tr class="odd">
<td>IBCE LIST LOCAL</td>
<td>This report lists, by local print form, all the override fields for all local print forms for the site.</td>
</tr>
<tr class="even">
<td>IBCE MESSAGE SCREEN TEXT</td>
<td>This option allows for the display of a list of words or phrases that if found in the text of an informational status message, will either always require the message to be reviewed or will auto-file the message and flag it as not needing a review.</td>
</tr>
<tr class="odd">
<td>IBCE MESSAGES SERVER</td>
<td>This option controls the reading and storing of return messages generated as a result of the processing of Integrated Billing electronic transmissions with the Austin translator.</td>
</tr>
<tr class="even">
<td>IBCE MRA MANAGEMENT</td>
<td>This will be a list manager screen with the option available to print an associated report. Using the screen, billing staff will be able to follow up on bills for secondary and tertiary billing for MRA bills.</td>
</tr>
<tr class="odd">
<td>IBCE MSGS PENDING TOO LONG</td>
<td>This report lists EDI messages still waiting to be filed after a user specified number of days.</td>
</tr>
<tr class="even">
<td>IBCE OUTPUT FORMATTER</td>
<td>This option allows the user to access the utilities needed to set up and maintain local forms using the forms output utility.</td>
</tr>
<tr class="odd">
<td>IBCE PREV TRANSMITTED CLAIMS</td>
<td>This option allows a user to view or produce a report of claims that were previously transmitted as live claims or that were transmitted as test claims prior to turning EDI on for an insurance company.</td>
</tr>
<tr class="even">
<td>IBCE PRINT EOB</td>
<td>Print EOB.</td>
</tr>
<tr class="odd">
<td>IBCE PROVIDER ID QUERY</td>
<td><p>This option allows the site to run or re-run the provider id query report to report some of the invalid provider id set ups for insurance companies.</p>
<p>CONDITIONS TO IDENTIFY:</p>
<ol type="1">
<li><blockquote>
<p>BLUE CROSS LINKED TO CMS-1500 ONLY (1) THE ONLY HARD ERROR.</p>
</blockquote></li>
<li><blockquote>
<p>BLUE SHIELD LINKED TO UB92 ONLY (2) WARNING.</p>
</blockquote></li>
<li><blockquote>
<p>BLUE CROSS ID APPLIED TO BOTH FORMS (0) WARNING.</p>
</blockquote></li>
<li><blockquote>
<p>BLUE CROSS OR BLUE SHIELD IDs EXIST FOR AN INS CO, BUT ONE OR MORE OF THE INSURANCE COMPANY'S PLANS DOES NOT HAVE AN ELECTRONIC PLAN TYPE OF 'BL.’</p>
</blockquote></li>
<li><blockquote>
<p>NON BLUE CROSS/SHIELD ID FOR AN INS COMPANY WITH BLUE PLAN(S).</p>
</blockquote></li>
<li><blockquote>
<p>VAD000 as an ID but not flagged as a UPIN.</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="even">
<td>IBCE PROVIDER ID WORKSHEET</td>
<td>Allows the user to print off provider id worksheets on which to record special requirements for provider ids for insurance companies. Users may choose blank sheets or sheets populated with all BLUE CROSS, BLUE SHIELD and TRICARE insurance company names.</td>
</tr>
<tr class="odd">
<td>IBCE PROVIDER MAINT</td>
<td>This is the screen from which all provider id maintenance can be performed.</td>
</tr>
<tr class="even">
<td>IBCE PRVNVA FAC EDIT</td>
<td>This option allows for entering and editing of NON-VA facility information for billing.</td>
</tr>
<tr class="odd">
<td>IBCE QUERY PENDING BATCH</td>
<td>This report shows the current transmission status of a batch's mail message. It also includes the mail message number it was sent in along with the first and last dates / times it was sent.</td>
</tr>
<tr class="even">
<td>IBCE READY FOR EXTRACT REP</td>
<td>This report provides a list of claims held in a Ready for Extract status due to the EDI / MRA IB site parameter field being turned off.</td>
</tr>
<tr class="odd">
<td>IBCE RESUB FROM CSA RPT</td>
<td>This report is generated to provide a list of claims that have errors that but were resent without changes via the CSA worklist RESUBMITTED BY PRINT, or RETRANSMITTED, or PRINTED.</td>
</tr>
<tr class="even">
<td>IBCE RETURN MSG PROCESSING</td>
<td>This option allows for the display of a list of return messages that have been received at the site but have been left in the temporary STATUS MESSAGE file. This may have been because of a system error or the message may not have been received in a readable format. This option provides the means to delete the message or to attempt to reapply it against the VistA data base.</td>
</tr>
<tr class="odd">
<td>IBCE RULE MAINTENANCE</td>
<td>This option will allow for the adding of new electronic transmission rules and to modify existing ones.</td>
</tr>
<tr class="even">
<td>IBCE TRANSMIT SELECTED BILLS</td>
<td>This option allows a user to transmit one or more transmittable claims that are waiting to be transmitted and are in a WAITING FOR EXTRACT status.</td>
</tr>
<tr class="odd">
<td>IBCE TXMT MGMNT REPORTS</td>
<td>This menu contains the options needed to produce reports for the 837 EDI module that deal with the status of the transmission of electronic billing data.</td>
</tr>
<tr class="even">
<td>IBCE VIEW PENDING BILL</td>
<td>This option allows for the user to enter the ENTER / EDIT billing information screens in a view-only mode for a selected authorized bill whose transmission status is either WAITING AUSTIN CONFIRM or READY FOR EXTRACT.</td>
</tr>
<tr class="odd">
<td>IBCE VIEW PREV TRANS MESSAGE</td>
<td>This report will display test claim EDI transmission data and EDI status message data from file 361.4.</td>
</tr>
<tr class="even">
<td>IBCED EDI CLAIM STATUS REPORT</td>
<td>This report shows information about transmitted electronic claims. Selection criteria include division, payer, date last transmitted, and current EDI status. This report has 3 sort levels and 8 sorting criteria.</td>
</tr>
<tr class="odd">
<td>IBCEM MESSAGES WITHOUT REVIEW</td>
<td>This option allows for the display of all EDI return messages that were filed without needing a review based on the text entries in the message screen text file (#361.3). The report can be run for a user-selected date range on date the message was received at the site and may be sorted by message text that caused the message to not need a review or by bill #.</td>
</tr>
<tr class="even">
<td>IBCEM MRA MANAGEMENT MENU</td>
<td>This menu option holds all EDI Medicare Remittance Advice (MRA) related options.</td>
</tr>
<tr class="odd">
<td>IBCEM MRA REPORT PRINT</td>
<td>This menu option prints the MRA Reports given a Bill Number. Based on the Bill Type, this report will print either an Institutional Format (Part A) or a Professional Format (Part B). In addition, if more than one MRA are associated with the Bill, all MRA's will print.</td>
</tr>
<tr class="even">
<td>IBCEM MRA STATISTICS REPORT</td>
<td>The MRA Statistics Report displays statistics on Primary and Secondary MRA requests.</td>
</tr>
<tr class="odd">
<td>IBCEM NON-MRA REPORT</td>
<td>The Non-MRA Productivity Report displays information on Primary, Secondary and Tertiary non-MRA claims.</td>
</tr>
<tr class="even">
<td>IBCEM PATIENTS W/O MEDICARE</td>
<td>This report will show living patients that have active insurance, but no MEDICARE (WNR) insurance on file. The other active insurance must be Medigap, or Medicare Secondary type insurance. In these cases, MEDICARE (WNR) should be the primary insurance. This is for the MRA project.</td>
</tr>
<tr class="odd">
<td>IBCEM STATUS MESSAGE</td>
<td>This option contains the functionality to print/purge electronically returned status messages that have been in a final review status for a user selected number of days.</td>
</tr>
<tr class="even">
<td>IBCEM VIEW MRA EOB</td>
<td>This option will allow the user to choose a bill that has at least one Medicare Remittance Advice (MRA) Explanation of Benefits (EOB) on file. The user can then view the MRA EOB through the List Manager utility.</td>
</tr>
<tr class="odd">
<td>IBCEMC MULT CSA MSG MANAGEMENT</td>
<td>This option allows users to see rejected claims status messages that are not reviewed. The users can take the same action on multiple messages at the same time.</td>
</tr>
<tr class="even">
<td>IBCI ASSIGN CLAIMSMANAGER BILL</td>
<td>This option will allow users to assign bills to other users.</td>
</tr>
<tr class="odd">
<td>IBCI CLAIMSMANAGER ERROR RPT</td>
<td>This report prints bill information for those bills that have ClaimsManager errors.</td>
</tr>
<tr class="even">
<td>IBCI CLAIMSMANAGER FILE MENU</td>
<td>This is a menu option containing the options that extract VistA data and create export files for the ClaimsManager application.</td>
</tr>
<tr class="odd">
<td>IBCI CLAIMSMANAGER NPT FILE</td>
<td>Create ClaimsManager NPT file.</td>
</tr>
<tr class="even">
<td>IBCI CLAIMSMANAGER PAYOR FILE</td>
<td>Extract data from Insurance company file (#36) and build the ClaimsManager Payer file.</td>
</tr>
<tr class="odd">
<td>IBCI CLAIMSMANAGER RPT MENU</td>
<td>This is a menu that contains the ClaimsManager report options.</td>
</tr>
<tr class="even">
<td>IBCI CLAIMSMANAGER STATUS RPT</td>
<td>This report prints bill information for those bills that have gone through the ClaimsManager interface process.</td>
</tr>
<tr class="odd">
<td>IBCI CLAIMSMANAGER WORKSHEET</td>
<td>This report prints the ClaimsManager error messages for a single bill.</td>
</tr>
<tr class="even">
<td>IBCI CLEAR CLAIMSMANAGER QUEUE</td>
<td>This option exists primarily for programmers to be able to clear the ClaimsManager results queue so the ClaimsManager interface gets back in sync. This method is not always successful. If it does not work, then Ingenix must be called at 1-800-765-6818.</td>
</tr>
<tr class="odd">
<td>IBCI MULTIPLE CLAIM SEND</td>
<td>This option will allow users to access the IBCI SKIP LIST list template. This is where users can send claims that were in error due to communication errors.</td>
</tr>
<tr class="even">
<td>IBCN COVERAGE LIMITATION RPT</td>
<td>This report will generate a list of coverage limitations by company and group.</td>
</tr>
<tr class="odd">
<td>IBCN EXPIRE GROUP SUBSCRIBERS</td>
<td>This option allows users to enter an expiration date to expire all subscriber policies associated with a group plan without requiring to be moved to a new plan.</td>
</tr>
<tr class="even">
<td>IBCN GRP PLAN FILES RPT</td>
<td>This option runs the List Group Plans without Annual Benefits Report.</td>
</tr>
<tr class="odd">
<td>IBCN HPID CLAIM RPT</td>
<td>This option runs the Manually Added HPIDs to Billing Claim Report.</td>
</tr>
<tr class="even">
<td>IBCN ID DUP INSURANCE ENTRIES</td>
<td>This option allows users to search the Insurance Company (36#) File to identify duplicate entries. The file may be searched by Insurance Company name, address, city, or state. A listing of Insurance Company names, address and phone number that meet the search criteria will display.</td>
</tr>
<tr class="odd">
<td>IBCN INS BILL PROV FLAG RPT</td>
<td>This option was deleted as part of IB*2.0*516.</td>
</tr>
<tr class="even">
<td>IBCN INS RPTS</td>
<td>This is a menu to edit, view, and print insurance-related reports.</td>
</tr>
<tr class="odd">
<td>IBCN INS PLANS MISSING DATA</td>
<td>This report prints a listing of user selected Insurance Companies that contain fields with no data for one or more user selected fields.</td>
</tr>
<tr class="even">
<td>IBCN INSURANCE BUFFER PROCESS</td>
<td>Display screens and processing actions for the Insurance Buffer.</td>
</tr>
<tr class="odd">
<td>IBCN INSURANCE BUFFER PURGE</td>
<td>This option may be used to purge the Insurance Buffer of entries that were processed (accepted or rejected) at least one year ago.</td>
</tr>
<tr class="even">
<td>IBCN INSURANCE CO EDIT</td>
<td>This option allows edit insurance company information.</td>
</tr>
<tr class="odd">
<td>IBCN INSURANCE EDI REPORT</td>
<td>This report will display EDI related information from the Insurance Company file (#36).</td>
</tr>
<tr class="even">
<td>IBCN INSURANCE MGMT MENU</td>
<td>This is the main menu to edit, view, and print insurance information.</td>
</tr>
<tr class="odd">
<td>IBCN LIST NEW NOT VER</td>
<td>This option will list by patient new insurance entries that have never been verified. Run this report and then use the Patient Insurance Info View/Edit option and choose the Verify Coverage action to verify coverage for individual patients.</td>
</tr>
<tr class="even">
<td>IBCN LIST PLANS BY INS CO</td>
<td>This option lists insurance companies and the plans under each company. The user may select one, many or all in both cases. The report can be run with or without a listing of the patients under each policy.</td>
</tr>
<tr class="odd">
<td>IBCN MEDICARE INSURANCE INTAKE</td>
<td>This option provides users with a condensed input template to enter Medicare Insurance information from Medicare cards. The Name of the Beneficiary should be entered in the following format: Last Name, First Name, Middle Initial. The Medicare claim number should be entered exactly as it appears on the card. Both, the Part A and Part B effective dates from the card should also be entered. Two separate policies will be created for both Part A and Part B coverage, if an effective date was entered for each type of coverage. Users holding the IB Insurance Supervisor Security key will be able to verify the information after entry. The policy will be placed in the Insurance Buffer File for non-key holders.</td>
</tr>
<tr class="even">
<td>IBCN MOVE SUBSCRIB TO PLAN</td>
<td>This option allows users to move subscribers to a different plan. The plan may be with the same or different Insurance Company. Annual Benefits, plan attributes and coverage limitations may be moved as well.</td>
</tr>
<tr class="odd">
<td>IBCN NO COVERAGE VERIFIED</td>
<td>This option will list all Patients within the specified sort criteria that have a No Coverage Verification Date entered. Verification of no insurance coverage may need to be reviewed yearly.</td>
</tr>
<tr class="even">
<td>IBCN OUTPUT INS BUFF ACTIVITY</td>
<td>This report provides a summary of the activity within the Insurance Buffer for a specified date range. Counts, percentages, and average processing times are included for both processed and unprocessed entries. The report can be printed with totals only or with subtotals by month within the date range selected.</td>
</tr>
<tr class="odd">
<td>IBCN OUTPUT INS BUFF EMPLOYEE</td>
<td>This report provides a summary of entries in the Insurance Buffer by employee and a specified date range. There are two variations of this report, one is for those employees that create/enter new Buffer entries. The other variation is for those employees that verify or process (accept / reject) Buffer entries. The report may be printed for one selected employee or all employees using the Buffer. Counts and percentages are included and can be printed with totals only or by month.</td>
</tr>
<tr class="even">
<td>IBCN PATIENT INSURANCE</td>
<td>This option allows viewing and editing of patient insurance information.</td>
</tr>
<tr class="odd">
<td>IBCN POL W/NO EFF DATE REPORT</td>
<td>This option displays all Active Policies that have no effective date for the search criteria entered. The report separates Verified and Non-Verified policies and lists Patient information, Insurance information and patient policy information. This report should be queued.</td>
</tr>
<tr class="even">
<td>IBCN PT W/WO INSURANCE REPORT</td>
<td>This option provides a list of patients with or without insurance coverage. The report lists patients who received medical treatment within a user specified date range and may further be refined to only list patients whose names or 'terminal digit' falls within a specified range. When printing the report of patients who have insurance coverage, the report may be restricted to those patients who have coverage with specific companies (up to six) or a range of companies. Additionally, the report may also be restricted to only include patients whose age falls within a user specified date range. This report should be queued.</td>
</tr>
<tr class="odd">
<td>IBCN REMOTE INSURANCE QUERY</td>
<td>This option will perform a query on the selected patient for insurance information at remote VA sites.</td>
</tr>
<tr class="even">
<td>IBCN RESYNCH INS COMP</td>
<td>On the rare occasion that the associated insurance company provider IDs get out of synch, this option is to be used by EVS or the IRM to get the parent and child insurance companies to be the same. This option should not be linked to any menu. This runs for all insurance companies and locks the insurance company file before starting so no one can be editing an insurance company while it is running.</td>
</tr>
<tr class="odd">
<td>IBCN UPDATE SUBSCRIBER INFO</td>
<td>This option will update subscriber fields defined to the PATIENT FILE (#2) INSURANCE TYPE sub-file (#2.312).</td>
</tr>
<tr class="even">
<td>IBCN USER EDIT RPT</td>
<td>This option runs the new User Edit Report.</td>
</tr>
<tr class="odd">
<td>IBCN VIEW INSURANCE CO</td>
<td>This option allows viewing of insurance company information.</td>
</tr>
<tr class="even">
<td>IBCN VIEW INSURANCE DATA</td>
<td>This menu contains the view option to Patient Insurance and Insurance Company information.</td>
</tr>
<tr class="odd">
<td>IBCN VIEW PATIENT INSURANCE</td>
<td>This option allows viewing of patient insurance information.</td>
</tr>
<tr class="even">
<td>IBCNE AUTO MATCH BUFFER</td>
<td>This option allows the user to see insurance company names in the Insurance Buffer file that do not exist in the Insurance Company file (File# 36) and that do not exist or pattern match with anything in the Auto Match file (File# 365.11).</td>
</tr>
<tr class="odd">
<td>IBCNE AUTO MATCH ENTER/EDIT</td>
<td>This option allows the user to manage the entries in the Auto Match file.</td>
</tr>
<tr class="even">
<td>IBCNE EIV PAYER DOD REPORT</td>
<td>This option enables the user to generate a report of insurance carriers reporting patient deaths so that Insurance Verifiers can forward information to the VA registration offices for research.</td>
</tr>
<tr class="odd">
<td>IBCNE EIV PAYER LINK NOTIFY</td>
<td>This option sends a Mailman notification to the eIV mail group that contains total number of nationally active unlinked payers with potential insurance company matches along with the list of eIV nationally active linked payers that are eIV locally inactive.</td>
</tr>
<tr class="even">
<td>IBCNE EIV UPDATE REPORT</td>
<td>Generate eIV Patient Insurance Update Report based on eIV Inquiries and Responses for a given date range and current Patient Insurance data.</td>
</tr>
<tr class="odd">
<td>IBCNE HL7 RESPONSE REPORT</td>
<td>This option displays the time the request was sent to FSC and the Time the response was receive. It also shows the Buffer #, Payer #, and Patient #.</td>
</tr>
<tr class="even">
<td>IBCNE IIV AMBIGUOUS POLICY RPT</td>
<td>This report will allow a user to display any Ambiguous Payer Responses for insurance policies that the eIV software discovered while questioning Payers. These policies are not necessarily on the patient's insurance file. Ambiguous payer responses are those responses that do not have enough information to safely determine if the policy is active or not.</td>
</tr>
<tr class="odd">
<td>IBCNE IIV INACTIVE POLICY RPT</td>
<td>This report will allow a user to display any Inactive Insurance Policies that the eIV software discovered while questioning Payers. These policies are not necessarily on the patient's insurance file.</td>
</tr>
<tr class="even">
<td>IBCNE IIV MENU</td>
<td>This menu contains options related to Electronic Insurance Verification (eIV).</td>
</tr>
<tr class="odd">
<td>IBCNE IIV PAYER REPORT</td>
<td>Generate the eIV Payer Report based on eIV Responses received for a given date range by Payer.</td>
</tr>
<tr class="even">
<td>IBCNE IIV RESPONSE REPORT</td>
<td>Generate eIV Payer Report based on the eIV Responses for a given date range, Payer name range and Patient name range. All the response information is displayed for the selected responses.</td>
</tr>
<tr class="odd">
<td>IBCNE IIV STATISTICAL REPORT</td>
<td>Generate eIV Statistical Report based on eIV Inquiries and Responses for a given date range and current Insurance Buffer data.</td>
</tr>
<tr class="even">
<td>IBCNE INS COMPANY LINK REPORT</td>
<td>This report shows the relationship between the insurance companies in file #36 and the payers in file #365.12.</td>
</tr>
<tr class="odd">
<td>IBCNE PAYER EDIT</td>
<td>Option to allow users to update the Local Active flag for Payers and Payer applications.</td>
</tr>
<tr class="even">
<td>IBCNE PAYER LINK</td>
<td>This option allows the user to link payers to selected insurance companies.</td>
</tr>
<tr class="odd">
<td>IBCNE PAYER LINK REPORT</td>
<td>This report shows the relationship between the insurance companies in the file #36 and the payers in file #365.12.</td>
</tr>
<tr class="even">
<td>IBCNE PAYER MAINTENANCE MENU</td>
<td>This menu contains options related to maintaining the Payer file (#365.12).</td>
</tr>
<tr class="odd">
<td>IBCNE POTENTIAL COB LIST</td>
<td>This option creates a list of those patients whom Medicare has identified in a 271 HL7 response message as having insurance after Medicare Insurance.</td>
</tr>
<tr class="even">
<td>IBCNE PURGE IIV DATA</td>
<td>This option is responsible for purging data from the eIV Response file (#365) and from the eIV Transmission Queue file (#365.1). Only data that is older than 6 months can be purged.</td>
</tr>
<tr class="odd">
<td>IBCNE REQUEST INQUIRY</td>
<td>Option to allow users to force electronic inquiry of patient insurance information through the eIV application.</td>
</tr>
<tr class="even">
<td>IBCNF EDIT CONFIGURATION</td>
<td>eII Edit Configuration: Runs the IBCNFCON routine to edit the eII configuration parameters. IBCNF EDIT security key required.</td>
</tr>
<tr class="odd">
<td>IBCNF EII GET SERVER</td>
<td>This is a server type option (not used by any user) that runs the GAITCMSG^IBCNFRD routine. Members of the IBN, IBX, IBK and IBH mail groups will receive the AITC DMI Queue confirmation messages for the four types of Extract files. The IBN mail group will also receive the results file messages.</td>
</tr>
<tr class="even">
<td>IBCNIU INTERFACILITY INS UPDT</td>
<td>This option displays either all sent or received interfacility insurance update records. The report can be generated as a summary or detailed to provide insurance details.</td>
</tr>
<tr class="odd">
<td>IBCNR E-PHARMACY MENU</td>
<td>Contains options for the e-Pharmacy Project.</td>
</tr>
<tr class="even">
<td>IBCNR EDIT HIPAA NCPDP FLAG</td>
<td>This option allows the user to edit the HIPAA NCPDP ACTIVE FLAG (#350.9, 11.01) (master switch to control e-Pharmacy NCPDP transactions).</td>
</tr>
<tr class="odd">
<td>IBCNR EDIT NCPDP PROCESSOR</td>
<td>This option allows the user to edit the NCPDP PROCESSOR APPLICATION sub-file (#366.013). Specific to e-Pharmacy.</td>
</tr>
<tr class="even">
<td>IBCNR EDIT PAYER</td>
<td>This option allows the user to edit the PAYER APPLICATION sub-file (#365.121). Specific to e-Pharmacy.</td>
</tr>
<tr class="odd">
<td>IBCNR EDIT PBM</td>
<td>This option allows the user to edit the PHARMACY BENEFITS MANAGER (PBM) APPLICATION sub-file (#366.023). Specific to e-Pharmacy.</td>
</tr>
<tr class="even">
<td>IBCNR EDIT PLAN</td>
<td>This option allows the user to edit the PLAN APPLICATION sub-file (#366.033). Specific to e-Pharmacy.</td>
</tr>
<tr class="odd">
<td>IBCNR GROUP PLAN MATCH</td>
<td>This option allows a user to match multiple GROUP INSURANCE PLAN file (#355.3) records to a PHARMACY PLAN file (#366.03) record.</td>
</tr>
<tr class="even">
<td>IBCNR GROUP PLAN WORKSHEET</td>
<td>The Group Plan Worksheet allows a user to, for a given date range, view all authorized Bill / Claim activity for a Group Plan that has active Pharmacy coverage.</td>
</tr>
<tr class="odd">
<td>IBCNR PHARMACY PLAN REPORT</td>
<td>The Pharmacy Plan Report lists the Plan Name, Plan ID, Banking Identification Number (BIN), and Processor Control Number (PCN) for all entries. It can be sorted by Plan Name or BIN and PCN.</td>
</tr>
<tr class="even">
<td>IBCNR PLAN MATCH</td>
<td>This option allows a user to match a GROUP INSURANCE PLAN file (#355.3) record to a PHARMACY PLAN file (#366.03) record.</td>
</tr>
<tr class="odd">
<td>IBCNR PLAN STATUS INQUIRY</td>
<td>Group Plan Status Inquiry screen.</td>
</tr>
<tr class="even">
<td>IBCNR PLAN STATUS REPORT</td>
<td>IBCNR Group Plan Status Report.</td>
</tr>
<tr class="odd">
<td>IBCNR RELEASE OF INFORMATION</td>
<td>This option allows the tracking of Release of Information for sensitive diagnosis medications.</td>
</tr>
<tr class="even">
<td>IBCNR ROI EXPIRATION REPORT</td>
<td>This option displays a report that will allow users to see when Releases of Information (ROI) are becoming expired or soon will expire. It also allows the user to see the status of “Active” or “Inactive” for each ROI. The database for this report is file #356.25 – CLAIMS TRACKING ROI.</td>
</tr>
<tr class="odd">
<td>IBCNR SHARED MATCHES RPT TASK</td>
<td>EPHARMACY SHARED MATCHES REPORT TASKMAN - Initiates e-pharmacy Shared Plan Matches Report that generates and sends the report - for use with TASKMAN scheduling.</td>
</tr>
<tr class="even">
<td>IBCNR TEST PAYER SHEET MATCH</td>
<td>This option allows the user to override a payer sheet associated with a Pharmacy Plan with a test payer sheet. This option should only be used for testing purposes only.</td>
</tr>
<tr class="odd">
<td>IBCNSRVBP</td>
<td>This server option will facilitate on-demand review of insurance companies in IB patch 400 switchback mode.</td>
</tr>
<tr class="even">
<td>IBCR ADJUSTMENT ENTER/EDIT</td>
<td>Charge Master option for IRM. Allow enter / edit of Rate Schedule Adjustment field. This field is M code and therefore requires programmer access.</td>
</tr>
<tr class="odd">
<td>IBCR CHARGE MASTER IRM MENU</td>
<td>This menu contains all IRM options for the Integrated Billing Charge Master.</td>
</tr>
<tr class="even">
<td>IBCR CHARGE MASTER MENU</td>
<td>This menu contains options to define and support Third Party billing rates and charges.</td>
</tr>
<tr class="odd">
<td>IBCR DELETE CHARGE ITEMS</td>
<td>Reports and deletes Charge Items in a Charge Set based on date. All charges that become inactive before a user specified date may be deleted allowing old, no longer used charges to be removed from the system.</td>
</tr>
<tr class="even">
<td>IBCR DISPLAY CHARGE MASTER</td>
<td>Display screens and enter / edit options for Charge Master.</td>
</tr>
<tr class="odd">
<td>IBCR ENTER RC NATIONAL CHARGES</td>
<td>This option is used to enter the National Interim Reasonable Charges. These non-site-specific charges are provided when new CPT / HCPCS codes are released as interim charges until the next full release of Reasonable Charges.</td>
</tr>
<tr class="even">
<td>IBCR ENTER TP NEG RATES</td>
<td>This option is used to enter / edit Transfer Pricing Negotiated rates. Rates can be negotiated between another VA Facility or an entire network (VISN). This option can only be used to edit rates in charge sets that were previously set up using this option. The rates entered here are stored in Charge Master for use.</td>
</tr>
<tr class="odd">
<td>IBCR FAST ENTER BILLING RATES</td>
<td>This option is designed to speed the entry into the Charge Master of the Interagency and Tortuously Liable Billing Rates when released once a year.</td>
</tr>
<tr class="even">
<td>IBCR HOST FILE LOAD</td>
<td>This option includes functions necessary to load charges from a Host file into the Charge Master.</td>
</tr>
<tr class="odd">
<td>IBCR INACTIVE CODES</td>
<td>Reports and inactivates the charges in the Charge Master for all currently inactive CPT codes.</td>
</tr>
<tr class="even">
<td>IBCR RC EXTRACT</td>
<td>This option is used to extract Reasonable Charges rates from Charge Master in a format that can be imported to Excel. The extract will allow the user to create a text file that is delimitated by the circumflex / caret (^) character. When importing to Excel specify that delimiter. This can be used for any version of RC from 2.0 or above. The output device selected should be a Host File Server (HFS) or the Current Terminal (for screen capture).</td>
</tr>
<tr class="odd">
<td>IBCR RC FACILITY TYPE</td>
<td>This option allows the user to change the VA division’s Facility Type designation for Reasonable Charges from Provider Based to Non-Provider Based and vice versa, which determines the charges loaded and available for use for that division.</td>
</tr>
<tr class="even">
<td>IBCR REPORTS FOR CHARGE MASTER</td>
<td>Option to print Charge Master reports.</td>
</tr>
<tr class="odd">
<td>IBD EDS TRAINING</td>
<td></td>
</tr>
<tr class="even">
<td>IBD MANUAL DATA DISPLAY</td>
<td>This option will display the components of a form that are available for data entry, the selection rules, and any associated data qualifiers. Use this to determine if the form has been set up correctly.</td>
</tr>
<tr class="odd">
<td>IBD MANUAL DATA ENTRY BY CLIN</td>
<td>This option allows manual data entry of encounter data for the Ambulatory Data Capture project. The user selects a clinic, an appointment date, a patient and can then do data entry for the encounter. All forms for the encounter will be asked. If no forms were printed for the encounter the user can select the form to for data entry without having to print the form.</td>
</tr>
<tr class="even">
<td>IBD MANUAL DATA ENTRY BY FORM</td>
<td>This option allows manual data entry of encounter data for the Ambulatory Data Capture project. This option allows a user to do data entry on a single form at a time. Input is based on the form design.</td>
</tr>
<tr class="odd">
<td>IBD MANUAL DATA ENTRY GROUP</td>
<td>This option allows manual data entry of encounter data for the Ambulatory Data Capture project. The user selects a clinic and appointment date / time, and may de-select specific patient, otherwise after completing data entry for a single patient, the data will then be entered for all patients with the same appointment date / time. All forms for the encounter will be asked. If no forms were printed for the encounter the user can select the form to for data entry without having to print the form.</td>
</tr>
<tr class="even">
<td>IBD MANUAL DATA ENTRY MENU</td>
<td>This menu contains the AICS Manual Data Entry options to enter encounter data based on encounter form design.</td>
</tr>
<tr class="odd">
<td>IBD MANUAL DATA ENTRY PRE</td>
<td>This option will allow data entry of forms that are pre-printed without patient data for unscheduled visits such as occur in emergency rooms.</td>
</tr>
<tr class="even">
<td>IBD SCANNING WORKSTATION</td>
<td></td>
</tr>
<tr class="odd">
<td>IBDF AUTO PURGE FORM TRACKING</td>
<td>This option should be queued to run at the site’s convenience. It will purge old data from several AICS files including: ENCOUNTER FORM DEFINITION file (357.95) ENCOUNTER FORM TRACKING file (357.96) FORM SPECIFICATION file (359.2) AICS ERROR AND WARNING LOG file (359.3) Two parameters in the ENCOUNTER FORM PARAMETERS file (357.09) control how this option works. The option needs no device and has no output. It is recommended that this be tasked to run at least once weekly during a weekend or other slow time.</td>
</tr>
<tr class="even">
<td>IBDF BACKGRD EF PRINT QUEUE</td>
<td>This option prints encounter forms in the background. Jobs are run based on the queuing parameters set up using the option IBDF SETUP AUTO CLINIC PRINT.</td>
</tr>
<tr class="odd">
<td>IBDF CLINIC SETUP/EDIT FORMS</td>
<td>The form generator for creating encounter forms.</td>
</tr>
<tr class="even">
<td>IBDF COPY CPTS TO FORM</td>
<td>Allows the user to select a CPT Check-off Sheet and Encounter Form. The Check-off Sheet's CPT codes are then copied to the Encounter Form.</td>
</tr>
<tr class="odd">
<td>IBDF DEFINE AVAILABLE REPORT</td>
<td>Allows reports, other than Health Summaries, to be made available for use by the print manager.</td>
</tr>
<tr class="even">
<td>IBDF DEFINE AVLABLE HLTH SMRY</td>
<td>Allows a Health Summary to be made available for use by the print manager.</td>
</tr>
<tr class="odd">
<td>IBDF EDIT CLINIC REPORTS</td>
<td>Used to select reports that should print for the clinic.</td>
</tr>
<tr class="even">
<td>IBDF EDIT ENCOUNTER FORMS</td>
<td>Contains the options that involve editing encounter forms.</td>
</tr>
<tr class="odd">
<td>IBDF EDIT MARKING AREA</td>
<td>Allows the local sites to create a Marking Area to supplement those that come with the tool kit. Marking Areas are the areas on a selection list that are used for writing in to indicate choices.</td>
</tr>
<tr class="even">
<td>IBDF EDIT PACKAGE INTERFACE</td>
<td>This option only allows selection routines and output routines. It allows Package Interfaces to be created, edited, and deleted. However, Package Interfaces that are in use in any form should not be deleted. By creating Package Interfaces, local sites can display data on forms that is not provided for in the tool kit.</td>
</tr>
<tr class="odd">
<td>IBDF EDIT PRINTERS</td>
<td>This option allows editing of the Encounter Form Printers file. Specify whether a terminal type is PCL5 compatible and the proper escape sequences for simplex and duplex. Only PCL5 compatible printers can print scannable encounter forms and must be so indicated. Generally, HP laser printers are PCL5 compatible.</td>
</tr>
<tr class="even">
<td>IBDF EDIT SITE PARAM</td>
<td>This option will allow editing of AICS site parameters that affect the printing of forms, manual data entry, and the purge utility and scanning.</td>
</tr>
<tr class="odd">
<td>IBDF EDIT TOOL KIT</td>
<td>Menu containing the options that allow the user to edit forms and blocks contained in the tool kit.</td>
</tr>
<tr class="even">
<td>IBDF EDIT TOOL KIT BLOCKS</td>
<td>Allows tool kit blocks to be edited, created, and deleted.</td>
</tr>
<tr class="odd">
<td>IBDF EDIT TOOL KIT FORMS</td>
<td>Allows tool kit forms to be edited, created, and deleted.</td>
</tr>
<tr class="even">
<td>IBDF EF FORM COMPONENTS</td>
<td>This new display lists the contents of a form (without displaying). It lists the contents of each block, the name of the block, starting row and column, width and height of the block. Two actions are included on this screen, EX Expand Item and BC Block Components. Expand Item allows the user to do an inquiry of the block and its components listed in the Block file #357.1. The Block Components action gives the user a more exact makeup of the block and the data it displays. It lists the component, type it is (selection list, handprint field or data field) row, column, and block separators. For selection lists it also lists the sub-column information. The Type (text or marking), Data (code, short description), Width of the sub-column, Qualifier, Selection Rule and if it is editable.</td>
</tr>
<tr class="odd">
<td>IBDF ENCOUNTER FORM</td>
<td>Contains all the encounter form options.</td>
</tr>
<tr class="even">
<td>IBDF FORMS TRACKING</td>
<td>This option connects the user to the forms tracking display. This allows the user to see what encounter forms have been printed, scanned and those that have not. It also allows the user to get statistics on this data as well as display forms with a specific status.</td>
</tr>
<tr class="odd">
<td>IBDF FREE PENDING PAGES</td>
<td>This option will allow a user to send Forms Tracking entries that are in a pending pages status to PCE.</td>
</tr>
<tr class="even">
<td>IBDF IMPORT/EXPORT UTILITY</td>
<td>Allows forms and blocks to be transferred between sites.</td>
</tr>
<tr class="odd">
<td>IBDF IRM OPTIONS</td>
<td>The basic intent of this menu is to contain the options that should only be available to those technical users that can program in MUMPS, which is a requirement, for example, when, adding a new PACKAGE INTERFACE.</td>
</tr>
<tr class="even">
<td>IBDF LIST CLINICS USING FORMS</td>
<td>For each encounter form this option lists the clinics using it.</td>
</tr>
<tr class="odd">
<td>IBDF LIST CLINICS WITH NO FORM</td>
<td>This option gives a report that lists the clinics that do not have encounter forms.</td>
</tr>
<tr class="even">
<td>IBDF MANUAL PURGE FORM TRACK</td>
<td>This option cleans up old data in AICS files that has a very limited or no use. Sites can choose the type of data that is to be deleted and the number of days of data that should be retained. In addition, sites can choose whether to retain data on items where the AICS processing is incomplete. Sites that do not scan and do not use AICS Manual Data Entry should purge all files completely and retain the minimum amount of data. Sites that are actively scanning may choose to keep data for a longer period and purge only Completed records depending upon the speed of completing outpatient records. The option needs no device and has no output. It is recommended that this be tasked to run at least once weekly during a weekend or other slow time. It will purge old data from the several AICS files including: ENCOUNTER FORM DEFINITION file (357.95) ENCOUNTER FORM TRACKING file (357.96) FORM SPECIFICATION file (359.2) AICS ERROR AND WARNING LOG file (359.3) Use the option IBDF AUTO PURGE FORM TRACKING to automatically queue this option to run on a recurring basis.</td>
</tr>
<tr class="odd">
<td>IBDF MISCELLANEOUS CLEANUP</td>
<td>This option is intended to delete various data structures that are no longer in use. The Encounter Form Utilities were designed to automatically delete all data structures when no longer needed, so this option is a backup that should rarely be needed. Currently, the option deletes the compiled version of forms where the form itself no longer exists. It also deletes blocks that do not belong to any form.</td>
</tr>
<tr class="even">
<td>IBDF PRINT BLNK ENCOUNTER FORM</td>
<td>This option allows the user to select a clinic, and if an encounter form is defined for use with an embossed patient card the form will be printed.</td>
</tr>
<tr class="odd">
<td>IBDF PRINT ENCOUNTER FORMS</td>
<td>For printing an encounter form for appointments, either by division, clinic, or patient.</td>
</tr>
<tr class="even">
<td>IBDF PRINT ERROR LIST</td>
<td>During scanning errors reported by AICS or PCE are stored in the AICS Error Log file. This report will allow printing a list of the errors so that the encounter forms can be retrieved, and the data validated.</td>
</tr>
<tr class="odd">
<td>IBDF PRINT MANAGER</td>
<td>Contains all the options pertaining to the print manager, except for the IBDF DEFINE AVLABLE HLTH SMRY option - that option allows the user to enter mumps code, so it must be limited to IRM use.</td>
</tr>
<tr class="even">
<td>IBDF PRINT OPTIONS</td>
<td>Contains the options for printing encounter forms.</td>
</tr>
<tr class="odd">
<td>IBDF PRINT SAMPLE ALL CLINICS</td>
<td>This option will print out one copy of each form currently assigned to a clinic and that is in use. Use this to prepare a package of materials for review or sharing with other facilities.</td>
</tr>
<tr class="even">
<td>IBDF PRNT FORM W/DATA NO APPT.</td>
<td>Allows an encounter form to be printed with patient data but does not ask that an appt. be selected. Uses current time as the appointment time.</td>
</tr>
<tr class="odd">
<td>IBDF RECOMPILE ALL FORMS</td>
<td>Used to recompile all forms. The compiled version of every form and block is deleted. Each form is compiled the first time it is printed.</td>
</tr>
<tr class="even">
<td>IBDF REPORT CLINIC SETUPS</td>
<td>Reports on each clinic setup, listing the encounter forms and other reports defined for use by the clinic.</td>
</tr>
<tr class="odd">
<td>IBDF REPORTS MENU</td>
<td>This menu option will contain the reports and utilities for AICS.</td>
</tr>
<tr class="even">
<td>IBDF SCANNED W/BILL GEN</td>
<td>This option prints a report for those encounter forms that have been scanned that also have bills generated. The report displays this data for all clinics using encounter forms for one / many / all divisions for a specific date range. The data that is displayed is the number scanned, number insured, number of bills entered, number of bills printed, and average days from date of encounter to date of bill generation (printed).</td>
</tr>
<tr class="odd">
<td>IBDF SETUP AUTO CLINIC PRINT</td>
<td>This option allows users to enter Print Manager Queuing Parameters and to specify automatic queuing parameters.</td>
</tr>
<tr class="even">
<td>IBDF UTIL MAINTENANCE UTILITY</td>
<td>This is a maintenance utility for the AICS package. It allows the user to display and print a listing of the invalid ICD, CPT and VISIT codes that are on encounter forms. It also allows the user to delete the invalid codes from the forms. Another action of this option is displaying a complete listing of all invalid ICD, CPT, and VISIT codes.</td>
</tr>
<tr class="odd">
<td>IBDF VALIDATE FORMS</td>
<td>Report used to validate the data that will be passed to PCE when an Encounter Form is scanned. The report may be sorted by Division, Clinic Group, Clinic, or Form.</td>
</tr>
<tr class="even">
<td>IBDFC CONVERSION UTILITY</td>
<td>Used to convert a form that was designed for just printing to a form that can be scanned.</td>
</tr>
<tr class="odd">
<td>IBJ DIAGNOSTIC MEASURES MENU</td>
<td>The Diagnostic Measures Menu allows a facility to quantitatively measure various elements that are critical to the MCCR program.</td>
</tr>
<tr class="even">
<td>IBJ MCCR COORDINATOR</td>
<td>This menu contains the Joint Inquiry and the Diagnostic Measures reports.</td>
</tr>
<tr class="odd">
<td>IBJ MCCR SITE PARAMETERS</td>
<td>This option allows the user to view and edit MCCR site parameters. Security key IB PARAMETER EDIT required.</td>
</tr>
<tr class="even">
<td>IBJ THIRD PARTY JOINT INQUIRY</td>
<td>Set of actions and screens for Third Party AR / IB Joint Inquiry. Provides detailed information on any Third-Party Claim.</td>
</tr>
<tr class="odd">
<td>IBJD BILLING LAG TIME</td>
<td>The Billing Lag Time Report provides a measure of the amount of time between significant milestones that occur during the claim submission and receivables management processes.</td>
</tr>
<tr class="even">
<td>IBJD BILLING REPORTS</td>
<td>The Billing Reports allow measurement of the claim’s submission process.</td>
</tr>
<tr class="odd">
<td>IBJD DM DISABLE/ENABLE</td>
<td>This option allows a user to disable or re-enable the Diagnostic Measures Extraction background job or certain DM reports that go through the monthly DM Extraction background job. Once a report is disabled, it won't be queued to run via the DM extract process.</td>
</tr>
<tr class="even">
<td>IBJD DM EXTRACT MENU</td>
<td>This menu contains options related to the Diagnostic Measures Extraction Module.</td>
</tr>
<tr class="odd">
<td>IBJD DM MANUAL START</td>
<td>This option allows a user to restart the Diagnostic Measures Extraction background job if the DM report data has not been successfully extracted for the previous month.</td>
</tr>
<tr class="even">
<td>IBJD DM MANUAL TRANSMIT</td>
<td>This option allows a user to retransmit a Diagnostic Measures Extract file to FORUM for a month if that month's DM report data did not successfully transmit the first time.</td>
</tr>
<tr class="odd">
<td>IBJD DM VIEW/PRINT EXTRACTS</td>
<td>This option allows a user to see the results of previous Diagnostic Measures extractions. It shows whether certain reports made it through the extraction process.</td>
</tr>
<tr class="even">
<td>IBJD FOLLOW-UP AR PROD REPORT</td>
<td>This report shows clerk activity based on transaction types and timeframes.</td>
</tr>
<tr class="odd">
<td>IBJD FOLLOW-UP ASSIGN PRINT</td>
<td>This option allows the printing of selected or all Workload Assignments stored in file #351.73.</td>
</tr>
<tr class="even">
<td>IBJD FOLLOW-UP CHAMPVA/TRICARE</td>
<td>This option provides information for sites to use to conduct follow-up activities for CHAMPVA and TRICARE receivables.</td>
</tr>
<tr class="odd">
<td>IBJD FOLLOW-UP FIRST PARTY</td>
<td>This option provides information for sites to use to conduct follow-up activities for First Party receivables.</td>
</tr>
<tr class="even">
<td>IBJD FOLLOW-UP MISC BILLS</td>
<td>This option provides information for sites to use to conduct follow-up activities for miscellaneous receivables.</td>
</tr>
<tr class="odd">
<td>IBJD FOLLOW-UP REPAYMENT PLAN</td>
<td>This option provides information for sites to use to conduct follow-up on the Repayment Plans.</td>
</tr>
<tr class="even">
<td>IBJD FOLLOW-UP REPORTS</td>
<td>The Follow-Up Reports allow measurement of the receivable’s management function.</td>
</tr>
<tr class="odd">
<td>IBJD FOLLOW-UP SUMMARY REPORT</td>
<td>The Third-Party Follow-Up Summary Report provides a summary of the balances of all outstanding Third-Party receivables.</td>
</tr>
<tr class="even">
<td>IBJD FOLLOW-UP THIRD PARTY</td>
<td>The Third-Party Follow-Up Report provides information for sites to use to conduct follow-up activities for Third Party receivables.</td>
</tr>
<tr class="odd">
<td>IBJD FOLLOW-UP WORKLOAD</td>
<td>This option allows the entering/editing of Workload Assignments by clerk to be stored in file #351.73.</td>
</tr>
<tr class="even">
<td>IBJD INTAKE COMP REG</td>
<td>The Percentage of Completed Registrations report allows the facility to examine the percentage of registrations completed without an inconsistency.</td>
</tr>
<tr class="odd">
<td>IBJD INTAKE INS</td>
<td>The report of Patients with Unidentified Insurance provides a list of patients that have been treated, but not identified as having or not having insurance.</td>
</tr>
<tr class="even">
<td>IBJD INTAKE NO EMPL</td>
<td>The No Employer Listing provides a list of veterans who were treated within a specified timeframe and whose employer is not specified.</td>
</tr>
<tr class="odd">
<td>IBJD INTAKE OPT WORKLOAD</td>
<td>The Outpatient Workload Report provides a measure of the number and types of Outpatient Services provided in the facility.</td>
</tr>
<tr class="even">
<td>IBJD INTAKE POL NOT VER</td>
<td>The report of Insurance Policies Not Verified provides a list of policies entered the system (within a specified timeframe) but were never verified.</td>
</tr>
<tr class="odd">
<td>IBJD INTAKE REPORTS</td>
<td>The intake reports allow measurement of registration processes and workload reporting.</td>
</tr>
<tr class="even">
<td>IBJD INTAKE SC VETS</td>
<td>The report of SC Vets w/ NSC Episodes of Care Not Billed (Inpatient) provides a measure of how well sites are billing SC veterans for non-service-connected treatment.</td>
</tr>
<tr class="odd">
<td>IBJD INTAKE UNV ELIG</td>
<td>This report lists patients who have been treated at a facility, but whose eligibility has not been verified. This report will also list patients with verified eligibility for at least 2 years, if any.</td>
</tr>
<tr class="even">
<td>IBJD PERCENT PREREGISTERED</td>
<td>This report provides number of patients treated, the number of patients pre-registered, % of patients pre-registered, number of patients pre-registered past the pre-registration time frame, number of patients never pre-registered, the clinic exclusions, and the eligibility exclusions.</td>
</tr>
<tr class="odd">
<td>IBJD REASONS NOT BILLABLE</td>
<td>This option prints a list of Claims Tracking entries that cannot be billed to an insurance company for various reasons.</td>
</tr>
<tr class="even">
<td>IBJD UTILIZATION REPORTS</td>
<td>The Utilization Reports allow measurement of the Utilization Management process.</td>
</tr>
<tr class="odd">
<td>IBJD UTILIZATION WORKLOAD</td>
<td>The Utilization Workload Report provides a measure of the number of Insurance Reviews that are conducted at the facility.</td>
</tr>
<tr class="even">
<td>IBQL ACUTE DOWNLOAD</td>
<td>This option, prompted for date range asks for a report by Services, Treating Specialties, or Admitting Diagnosis will tally by month a downloaded list for Excel of Acute and Non-Acute entries and Non- Acute Reasons for Admission and Stay reviews.</td>
</tr>
<tr class="odd">
<td>IBQL ACUTE LIST</td>
<td>This option, prompted for date range asks for a report by Services, Treating Specialties, or Admitting Diagnosis will tally by month a list of Acute and Non-Acute entries and Non-Acute Reasons for Admission and Stay reviews.</td>
</tr>
<tr class="even">
<td>IBQL DOWNLOADS</td>
<td>This option controls the Download menu options for IBQ.</td>
</tr>
<tr class="odd">
<td>IBQL MAIN MENU</td>
<td>This option is the main menu for Utilization Management Rollup at the local site.</td>
</tr>
<tr class="even">
<td>IBQL MISSING DATA LIST</td>
<td>This option, prompted for date range, lists patients discharged from Claims Tracking with missing data for Random, Disease, and Local cases who would qualify for the national and local rollup.</td>
</tr>
<tr class="odd">
<td>IBQL NATIONAL ROLLUP</td>
<td>This option will load the UTILIZATION MANAGEMENT ROLLUP file with Random and Disease specific data for the national rollup. This option is queued to run at a site selected date between May 15 and June 15 and re-queued every six months. This data is pulled from the Hospital Review file (#356.1) based on discharged dates in the Claims Tracking file (#356).</td>
</tr>
<tr class="even">
<td>IBQL OUTPUTS</td>
<td>The Outputs menu option controls all the list menus for IBQ.</td>
</tr>
<tr class="odd">
<td>IBQL PATIENT LIST</td>
<td>This option, prompted for date range, lists all patients discharged from the Claims Tracking file (#356) for Random, Disease, and Local cases who will qualify for the national and local rollups.</td>
</tr>
<tr class="even">
<td>IBQL PATIENT REVIEW DOWNLOAD</td>
<td>This option, prompted for date range asks for a report by Services or Treating Specialties, will download patients, Admission and Stay review information.</td>
</tr>
<tr class="odd">
<td>IBQL PATIENT REVIEW LIST</td>
<td>This option, prompted for date range asks for a report by Services, Treating Specialties, or Providers will list patients, Admission and Stay review information.</td>
</tr>
<tr class="even">
<td>IBQL PURGE ROLLUP DATA</td>
<td>This option, prompted for Local or All Cases, will purge selected cases from the Utilization Management Rollup File.</td>
</tr>
<tr class="odd">
<td>IBQL ROLLUP</td>
<td>This option, prompted for date range, will load the Utilization Rollup file (#538) with qualifying patients discharged from Claims Tracking that have no missing data. This process will build a rollup file to be used by the UR for reports and downloading to spreadsheet.</td>
</tr>
<tr class="even">
<td>IBRFI 277 WORKLIST</td>
<td>This is a list manager screen, RFAI Management Worklist, to select RFI Messages to be worked.</td>
</tr>
<tr class="odd">
<td>IBT CODING VALIDATION MENU</td>
<td>This menu is for reports that relate to indicating which claims have been validated by coding staff.</td>
</tr>
<tr class="even">
<td>IBT EDIT APPEALS/DENIALS</td>
<td>This option allows for enter / editing appeals and denials and associated communications.</td>
</tr>
<tr class="odd">
<td>IBT EDIT BI TRACKING ENTRY</td>
<td>This option allows entry and display of claims tracking information that is needed to perform billing functions.</td>
</tr>
<tr class="even">
<td>IBT EDIT COMMUNICATIONS</td>
<td>This option allows enter / editing of MCCR / UR related communications that may or may not be associated with a claims tracking entry.</td>
</tr>
<tr class="odd">
<td>IBT EDIT HR REVIEWS TO DO</td>
<td>This option will create a list of pending work for Hospital UR personnel who do QM reviews. From this option most all screens and options needed to do the daily input are available.</td>
</tr>
<tr class="even">
<td>IBT EDIT HR TRACKING ENTRY</td>
<td>This option allows enter / editing of Claims Tracking Entries. Data associated with a CT entry may affect if or how it is billed and the types of reviews that may be or must be entered.</td>
</tr>
<tr class="odd">
<td>IBT EDIT IR REVIEWS TO DO</td>
<td>This option will create a list of pending reviews that Insurance Review personnel need to complete. Most of the input screens and options needed to do the daily work are available from this option.</td>
</tr>
<tr class="even">
<td>IBT EDIT IR TRACKING ENTRY</td>
<td>This option allows enter / editing of Claims Tracking Entries. Data associated with a CT entry may affect if or how it is billed and the types of reviews that may be or must be entered.</td>
</tr>
<tr class="odd">
<td>IBT EDIT REASON NOT BILLABLE</td>
<td>This option allows entry of a reason not billable. Entry of a reason will automatically be printed on the Patients with Insurance Reports and will cause the annotated care not to be automatically billed.</td>
</tr>
<tr class="even">
<td>IBT EDIT REVIEWS</td>
<td>This option allows viewing and editing of UR reviews of claims tracking entries. This includes pre-admission / pre-certification reviews, continuing stay reviews, and discharge reviews.</td>
</tr>
<tr class="odd">
<td>IBT EDIT REVIEWS TO DO</td>
<td>This option will list all reviews that have a next review date in the past seven days. All screens and actions necessary to complete the pending reviews are available from within this option. Select a different date range of pending reviews if desired. Both Hospital and Insurance reviews can be accessed with this option. Many pending reviews may have automatically been created by the computer when a patient is admitted.</td>
</tr>
<tr class="even">
<td>IBT EDIT TRACKING ENTRY</td>
<td>This option allows enter/editing of Claims Tracking Entries. Data associated with a CT entry may affect if or how it is billed and the types of reviews that may be or must be entered.</td>
</tr>
<tr class="odd">
<td>IBT EDIT TRACKING PARAMETERS</td>
<td>This option allows editing MCCR site parameters that affect the Claims Tracking Module. Security key IB PARAMETER EDIT required.</td>
</tr>
<tr class="even">
<td>IBT ENTERED NOT REVIEWED</td>
<td>This new report will allow the MCCF staff to identify encounters that have been: 1. Reviewed by the coders and are ready to bill (indicated by a non-blank findings type), and 2. Not reviewed by code (indicated by a blank findings type) The report prints all outpatient reimbursable insurance claims in file #399 with a status of Entered / Not Reviewed. The user input criteria for the report is the Event Date range. The user is prompted for the EVENT START DATE and EVENT END DATE.</td>
</tr>
<tr class="odd">
<td>IBT 278 CERTIFICATION REPORT</td>
<td>This option runs the 278 Certification Report.</td>
</tr>
<tr class="even">
<td>IBT 278 DISPOSITION REPORT</td>
<td>This option runs the 278 Deletion Disposition Report.</td>
</tr>
<tr class="odd">
<td>IBT 278 STATISTICAL REPORT</td>
<td>This option runs the 278 Statistical Report.</td>
</tr>
<tr class="even">
<td>IBT HCSR NIGHTLY PROCESS</td>
<td>This option should not be placed on any menu or run by any user; it is designed to be scheduled in TaskMan to be executed once a day during off-peak hours. This option is a nightly task that gathers data for Healthcare Services Review worklist and stores it in HCS REVIEW TRANSMISSION file.</td>
</tr>
<tr class="odd">
<td>IBT HCSR RESPONSE VIEW</td>
<td>Healthcare Services Review 278 response view.</td>
</tr>
<tr class="even">
<td>IBT HCSR WORKLIST</td>
<td>Healthcare Services Review worklist.</td>
</tr>
<tr class="odd">
<td>IBT MANAGER MENU</td>
<td>This is the main claims tracking menu. It contains the various user menus that can be assigned directly to UR or MCCR/UR personnel.</td>
</tr>
<tr class="even">
<td>IBT MONTHLY AUTO GEN AVE BILL</td>
<td>This option will calculate the number of bills and the average bill amounts for a month and store the data in the CLAIMS TRACKING UNBILLED AMOUNTS file (356.19). This data will then be used by the scheduled option Auto-Build Unbilled Amounts Report (IBT MONTHLY AUTO GEN UNBILLED) to generate the unbilled amounts data that needs to be reported by the 3rd workday of the month. Queue this option to run once monthly. Sites may choose the date it should run but it is suggested that it run after the 15th of the month when user activity is low (i.e., November 19, 1994 @ 2:00am). No device is necessary, the results are stored, and a completion mail message is sent to the mail group specified in the IB SITE PARAMETERS file.</td>
</tr>
<tr class="odd">
<td>IBT MONTHLY AUTO GEN UNBILLED</td>
<td>This option will automatically generate the unbilled amounts report that contains the data that needs to be input to our general ledger accounts by the 3rd workday of the month. Schedule this option to run once monthly on the 1st or 2nd day of the month. No device is needed, the results are sent in a mail message to the mail group specified in the IB SITE PARAMETERS file.</td>
</tr>
<tr class="even">
<td>IBT OUTPUT BILLING SHEET</td>
<td>This option allows printing of information from Claims Tracking about a specific visit. Included on the report is Visit Information, Insurance Information, Billing information (from Claims Tracking), Hospital Review information and Insurance Review information. Also included is provider, diagnosis, and procedure information. This report is the most complete summary of information about a single visit available in Claims Tracking.</td>
</tr>
<tr class="odd">
<td>IBT OUTPUT CLAIM INQUIRY</td>
<td>This option allows viewing or printing a detailed inquiry to any claims tracking entry. This includes showing all associated reviews and communications.</td>
</tr>
<tr class="even">
<td>IBT OUTPUT DENIED DAYS REPORT</td>
<td>This option prints a summary of days denied by insurance company for a user specified date range. A summary report by service is also generated.</td>
</tr>
<tr class="odd">
<td>IBT OUTPUT LIST VISITS</td>
<td>This option will print a list of visits that require either an insurance review, hospital review or both. In addition, only visits that are admissions may be printed. The user may select the date range of visits to print. This option can be used to list the Random Sample cases being tracked for Hospital Reviews by answering the prompts that only hospital reviews for admissions are wanted.</td>
</tr>
<tr class="even">
<td>IBT OUTPUT MCCR/UR SUMMARY</td>
<td>This report can be run for either admissions or discharges for a date range. It will summarize totals by admission or discharge, cases with insurance, billable inpatient cases, cases requiring reviews, days approved, amount collectible approved for billing, number of days denied, amount denied, and penalty dollars.</td>
</tr>
<tr class="odd">
<td>IBT OUTPUT MENU</td>
<td>This is the main reports menu for the Claims tracking module.</td>
</tr>
<tr class="even">
<td>IBT OUTPUT ONE ADMISSION SHEET</td>
<td>This option will print an admission sheet for one patient one admission at a time. It can be used to reprint an admission sheet if needed.</td>
</tr>
<tr class="odd">
<td>IBT OUTPUT PENDING ITEMS</td>
<td>This option will print a sorted list of Pending Reviews. It is different from printing from the Pending Reviews option in that it will limit the entries to those the user cares to see.</td>
</tr>
<tr class="even">
<td>IBT OUTPUT REVIEW WORKSHEET</td>
<td>This option will print an Insurance Review worksheet for the selected patient. If the patient is currently an inpatient, it will contain the current inpatient information.</td>
</tr>
<tr class="odd">
<td>IBT OUTPUT SCHED ADM W/INS</td>
<td>This option will print a list of Admission that are scheduled but not admitted and / or scheduled admissions that have been admitted. All admissions must be for patients who were insured on admission date.</td>
</tr>
<tr class="even">
<td>IBT OUTPUT UNSCHE ADM W/INS</td>
<td>This option will print a list of patients who were insured on admission date but were not scheduled admissions.</td>
</tr>
<tr class="odd">
<td>IBT OUTPUT UR ACTIVITY REPORT</td>
<td>This option prints by clinical service, information about the MCCR / UR activity.</td>
</tr>
<tr class="even">
<td>IBT QUICK REV CODING STAT</td>
<td>This report allows the MCCF staff to select a specific patient status of the to see whether it is ready for billing. The report input variable is: Patient Name Report is sorted by ENCOUNTER DATE/TIME The following fields are to be printed on this report: 1. Patient Social Security Number, 2. Outpatient Encounter Location, 3. Encounter Date and Time, 4. Reason Not Billable, 5. Billable Findings Type.</td>
</tr>
<tr class="odd">
<td>IBT RE-GEN AVE BILL AMOUNT</td>
<td>This option can be used to re-generate the monthly and yearly counts and amounts of inpatient and outpatient bills for a single month. If the month selected for input requires the calculation of previous month’s data in order to obtain its yearly values, this will be done when the option is executed. If the month selected has 12 prior months’ worth of data, the month selected will be recalculated. The months after the month selected (up to 12) will have yearly data recalculated. This information is used to compute the average bill amount for the Unbilled Amounts Report. The unbilled amount report is automatically generated for only the month selected after the average bill amounts are calculated.</td>
</tr>
<tr class="even">
<td>IBT RE-GEN UNBILLED REPORT</td>
<td>This option can be used to re-generate the Unbilled amounts report for a single month. This will re-compute the unbilled care for the month and update the unbilled amounts. To simply view previously computed data, use the View option.</td>
</tr>
<tr class="odd">
<td>IBT SEND TEST UNBILLED MESS</td>
<td>This option allows for sending of a test mail message to the mail group to receive the Unbilled Amounts messages. Using this prior to reporting problems can assist sites in determining whether the mail groups are set up correctly. The mail group to get the message should be specified in field UNBILLED MAIL GROUP (6.25) in the IB SITE PARAMETERS file (350.9).</td>
</tr>
<tr class="even">
<td>IBT SUP MANUALLY QUE ENCTRS</td>
<td>This option allows the user to select a date range of outpatient encounters to try to add these to the Claims tracking module. The option will automatically queue off a task to add encounters and when complete send the requesting user a mail message.</td>
</tr>
<tr class="odd">
<td>IBT SUP MANUALLY QUE RX FILLS</td>
<td>This option can be used to manually add RX refills to Claims tracking. The option will automatically queue off a task to add refills and when complete send the requesting user a mail message.</td>
</tr>
<tr class="even">
<td>IBT SUP MANUALLY QUE PRSTHTCS</td>
<td>This option allows the user to select a date range of prosthetics encounters and tries to add these to the Claims tracking module. The option will automatically queue off a task to add prosthetics and when complete send the requesting user a mail message.</td>
</tr>
<tr class="odd">
<td>IBT SUPERVISORS MENU</td>
<td>This option contains the supervisory options for the Claims tracking module. Site parameters may be edited. Table files may be maintained. Background jobs may be repeated or re-queued.</td>
</tr>
<tr class="even">
<td>IBT UNBILLED MENU</td>
<td>This menu contains the 4 user options available to regenerate and view the Unbilled Amounts report.</td>
</tr>
<tr class="odd">
<td>IBT UNREVIEWED CODING REPORT</td>
<td>This report is designed to be run by staff to determine which Claims Tracking events still require review. The user is prompted for the OUTPATIENT ENCOUNTER START DATE and OUTPATIENT ENCOUNTER END DATE.</td>
</tr>
<tr class="even">
<td>IBT USER COMBINED MCCR/UR MENU</td>
<td>This is the main menu for MCCR / UR persons who do both Hospital UR and MCCR UR (Insurance UR). It contains all the options necessary to do both hospital and Insurance Reviews. From this menu the claims tracking module can be edited, UR Reviews can be entered, Insurance Reviews can be entered, and reports printed. Supervisory functions will be available to those who hold the supervisory keys.</td>
</tr>
<tr class="odd">
<td>IBT USER MENU (BI)</td>
<td>This menu contains the options in Claims tracking designed specifically for billing clerks and billing supervisors who do not need to have any Utilization Review Input. Options include the ability to flag care as not billable, UR reports on billing case, and a claims tracking update option.</td>
</tr>
<tr class="even">
<td>IBT USER MENU (HR)</td>
<td>This is the main menu for UR personnel to enter Hospital Reviews into the Claims Tracking Module. From the menu the claims tracking module can be edited, UR Reviews can be entered, and reports printed. Supervisory functions will be available to those who hold the supervisory keys.</td>
</tr>
<tr class="odd">
<td>IBT USER MENU (IR)</td>
<td>This is the main menu for MCCR/UR persons who do MCCR / UR Reviews (Insurance Reviews). From the menu the claims tracking module can be edited, Insurance Reviews can be entered, and reports printed. Supervisory functions will be available to those who hold the supervisory keys.</td>
</tr>
<tr class="even">
<td>IBT VIEW UNBILLED AMOUNTS</td>
<td>This option can be used to view previously computed unbilled amounts without having to re-compile the data.</td>
</tr>
<tr class="odd">
<td>IBT MONTHLY AUTO GEN AVE BILL</td>
<td>This option will calculate the number of bills and the average bill amounts for a month and store the data in the CLAIMS TRACKING UNBILLED AMOUNTS file (356.19). This data will then be used by the scheduled option Auto-Build Unbilled Amounts Report (IBT MONTHLY AUTO GEN UNBILLED) to generate the unbilled amounts data that needs to be reported by the 3rd workday of the month. Queue this option to run once monthly. Sites may choose the date it should run but it is suggested that it run after the 15th of the month when user activity is low (i.e., November 19, 1994 @ 2:00am). No device is necessary, the results are stored, and a completion mail message is sent to the mail group specified in the IB SITE PARAMETERS file.</td>
</tr>
<tr class="even">
<td>IBT MONTHLY AUTO GEN UNBILLED</td>
<td>This option will automatically generate the unbilled amounts report that contains the data that needs to be input to our general ledger accounts by the 3rd workday of the month. Schedule this option to run once monthly on the 1st or 2nd day of the month. No device is needed, the results are sent in a mail message to the mail group specified in the IB SITE PARAMETERS file.</td>
</tr>
<tr class="odd">
<td>IBT RE-GEN AVE BILL AMOUNT</td>
<td>This option can be used to re-generate the monthly and yearly counts and amounts of inpatient and outpatient bills for a single month. If the month selected for input requires the calculation of previous month’s data in order to obtain its yearly values, this will be done when the option is executed. If the month selected has 12 prior months’ worth of data, the month selected will be recalculated. The months after the month select (up to 12) will have yearly data recalculated. This information is used to compute the average bill amount for the Unbilled Amounts Report. The unbilled amount report is automatically generated for only the month selected after the average bill amounts are calculated.</td>
</tr>
<tr class="even">
<td>IBT RE-GEN UNBILLED REPORT</td>
<td>This option can be used to re-generate the Unbilled amounts report for a single month. This will re-compute the unbilled care for the month and update the unbilled amounts. To simply view previously computed data, use the View option.</td>
</tr>
<tr class="odd">
<td>IBT UNBILLED MENU</td>
<td>This menu contains the 4 user options available to regenerate and view the Unbilled Amounts report.</td>
</tr>
<tr class="even">
<td>IBT VIEW UNBILLED AMOUNTS</td>
<td>This option can be used to view previously computed unbilled amounts without having to re-compile the data.</td>
</tr>
<tr class="odd">
<td>IBT MONTHLY AUTO GEN AVE BILL</td>
<td>This option will calculate the number of bills and the average bill amounts for a month and store the data in the CLAIMS TRACKING UNBILLED AMOUNTS file (356.19). This data will then be used by the scheduled option Auto-Build/Unbilled Amounts Report (IBT MONTHLY AUTO GEN UNBILLED) to generate the unbilled amounts data that needs to be reported by the 3rd workday of the month. Queue this option to run once monthly. Sites may choose the date it should run but it is suggested that it run after the 15th of the month when user activity is low (i.e. November 19, 1994 @ 2:00am). No device is necessary, the results are stored, and a completion mail message is sent to the mail group specified in the IB SITE PARAMETERS file.</td>
</tr>
<tr class="even">
<td>IBT MONTHLY AUTO GEN UNBILLED</td>
<td>This option will automatically generate the unbilled amounts report that contains the data that needs to be input to our general ledger accounts by the 3rd workday of the month. Schedule this option to run once monthly on the 1st or 2nd day of the month. No device is needed, the results are sent in a mail message to the mail group specified in the IB SITE PARAMETERS file.</td>
</tr>
<tr class="odd">
<td>IBT RE-GEN AVE BILL AMOUNT</td>
<td>This option can be used to re-generate the monthly and yearly counts and amounts of inpatient and outpatient bills for a single month. If the month selected for input requires the calculation of previous month’s data in order to obtain its yearly values, this will be done when the option is executed. If the month selected has 12 prior months’ worth of data, the month selected will be recalculated. The months after the month select (up to 12) will have yearly data recalculated. This information is used to compute the average bill amount for the Unbilled Amounts Report. The unbilled amount report is automatically generated for only the month selected after the average bill amounts are calculated.</td>
</tr>
<tr class="even">
<td>IBT RE-GEN UNBILLED REPORT</td>
<td>This option can be used to re-generate the Unbilled amounts report for a single month. This will re-compute the unbilled care for the month and update the unbilled amounts. To simply view previously computed data, use the View option.</td>
</tr>
<tr class="odd">
<td>IBT SEND TEST UNBILLED MESS</td>
<td>This option allows for sending of a test mail message to the mail group to receive the Unbilled Amounts messages. Using this prior to reporting problems can assist sites in determining whether the mail groups are set up correctly. The mail group to get the message should be specified in field UNBILLED MAIL GROUP (6.25) in the IB SITE PARAMETERS file (350.9).</td>
</tr>
<tr class="even">
<td>IBT UNBILLED MENU</td>
<td>This menu contains the 4 user options available to regenerate and view the Unbilled Amounts report.</td>
</tr>
<tr class="odd">
<td>IBT VIEW UNBILLED AMOUNTS</td>
<td>This option can be used to view previously computed unbilled amounts without having to re-compile the data.</td>
</tr>
<tr class="even">
<td>IBTAS EBILLING RPCS</td>
<td>This option contains the IB Remote Procedure Calls (RPCs) that are accessible via VistALink, using the IBTAS, APPLICATION PROXY user.</td>
</tr>
<tr class="odd">
<td>IBCN LIST PLANS BY INS CO</td>
<td>This option lists insurance companies and the plans under each company. The user may select one, many or all in both cases. The report can be run with or without a listing of the patients under each policy.</td>
</tr>
<tr class="even">
<td>IB RX REPRINT REMINDER</td>
<td>This option is used to generate an Income Test reminder letter for a veteran who effective co-pay exemption is based upon income. When the letter is generated, the field REMINDER LETTER DATE (#.16) in the BILLING EXEMPTIONS (#354.1) file will be updated, for the exemption record that is the basis for sending the reminder letter, with the current date.</td>
</tr>
<tr class="odd">
<td>IB TP FLAG OPT PARAMS</td>
<td>This option is used to flag stop codes and clinics as either non-billable for Third Party billing or to be ignored by the Third-Party auto biller. These parameters are all flagged by date and may be inactivated and re-activated.</td>
</tr>
<tr class="even">
<td>IB TP LIST FLAGGED PARAMS</td>
<td>This output is used to generate a list of all stop codes and clinics that are flagged as non-billable for Third Party billing or that should not be auto billed by the Third-Party auto biller on a user-specified date.</td>
</tr>
<tr class="odd">
<td>IBZ-MRA-SERVER</td>
<td></td>
</tr>
<tr class="even">
<td>IBUC MAIN MENU</td>
<td>This menu contains all the necessary utilities to update and to generate reports from the Urgent Care Visit Tracking Database (#351.82).</td>
</tr>
<tr class="odd">
<td>IBUC MULTI FAC COPAY PULL REQ</td>
<td>This option asks for a patient and requests UC copay information at any facility that patient has been treated at.</td>
</tr>
<tr class="even">
<td>IBUC VISIT INQUIRE</td>
<td>This option allows the user to review a veteran's Urgent Care visits for a specified calendar year or range of years.</td>
</tr>
<tr class="odd">
<td>IBUC VISIT MAINT</td>
<td>This menu option allows users to manually update the Urgent Care Visit Tracking entries store in the Urgent Care Visit Tracking File (#351.82). IBUC VISIT MAINT OVERRIDE key allows managers to add Free Visits for all Priority Groups.</td>
</tr>
<tr class="even">
<td>IBUC VISIT REPORT</td>
<td>This report allows users to review the Urgent Care Visit activity linked to veterans enrolled at the site, either summarized by month year or with the monthly totals listing the veterans who have been linked with Urgent Care visits. This report can be exported to Microsoft Excel.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633859" class="anchor"></span>Table : Criteria be met to Purge Billing Data

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Menu (under the System Manager's Integrated Billing Menu) provides archiving and purging capabilities for certain Integrated Billing files.

The Purge Update File option is used to delete all CPT entries from the temporary file, UPDATE BILLABLE AMBULATORY SURGICAL CODE (#350.41), after having been transferred to the permanent file, BILLABLE AMBULATORY SURGICAL CODES (#350.4). At this time, these files are obsolete as the regulation implementing billing of ambulatory surgery CPT codes uses HCFA rates was never passed.

The remainder of the options in the Purge Menu are used to archive and purge billing data. The files that may be archived and subsequently purged are the INTEGRATED BILLING ACTION file (#350) (pharmacy co-payment transactions only), the CATEGORY C BILLING CLOCK file (#351), and the BILL/CLAIMS file (#399).

At a minimum, billing data from the current and one previous fiscal year must be maintained on-line. With this version of Integrated Billing, data may be purged up through any date prior to the beginning of the previous fiscal year.

A separate routine is provided to purge entries from the BILLING EXEMPTIONS file (#354.1) with the Medication Co-payment Exemption patch. There is no output from this routine. It is provided for maintenance of this file until a more robust archiving and purging option can be written.

The following criteria must be met to purge billing data.

<table>
<caption><p><span id="_Toc127633860" class="anchor"></span>Table : Average Record Size</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>INTEGRATED BILLING ACTION file (#350)</p>
<p>(pharmacy co-payment actions)</p></td>
<td>The prescription that caused the action to be created must have been purged from the pharmacy database before the action may be archived. In addition, the bill must be closed in Accounts Receivable. The date the bill was closed is the date used to determine whether it will be included.</td>
</tr>
<tr class="even">
<td>CATEGORY C BILLING CLOCK file (#351)</td>
<td>Only clocks with a status of CLOSED or CANCELLED and a clock end date prior to the selected time frame are included.</td>
</tr>
<tr class="odd">
<td>BILL/CLAIMS file (#399)</td>
<td>The bill must be closed in Accounts Receivable. The date the bill was closed is the date used to determine whether it will be included.</td>
</tr>
<tr class="even">
<td>BILLING EXEMPTIONS file (#354.1)</td>
<td>Billing Exemptions may be purged using the new routine, IBPEX, if at least 1 year old, not the patient’s current exemption, do not contain dates of canceled charges in AR, and if active, must be one year older than the purge date for inactive exemptions.</td>
</tr>
</tbody>
</table>

<span id="_Toc127633860" class="anchor"></span>Table : Average Record Size

There are three steps involved in the archiving and purging of these files.

1.  A search is conducted to find all entries that may be archived through the Find Billing Data to Archive option. Choose which of the three files to include in the search. The entries found are temporarily stored in a sort (search) template in the SORT TEMPLATE file (#.401). An entry is also made to the IB ARCHIVE/PURGE LOG file (#350.6). This log may be viewed through the Archive/Purge Log Inquiry and List Archive/Purge Log Entries options.
2.  The List Search Template Entries option allows the user to view the contents of a search template. Delete entries from the search template using the Delete Entry from Search Template option.
3.  The entries are archived using the Archive Billing Data option. It is highly recommended to archive the entries to paper (print to a non-slave printer), as there is currently no functionality to retrieve or restore data that has been archived.
4.  The data is purged from the database using the Purge Billing Data option. The search template containing the purged entries is also deleted. An electronic signature code and the XUMGR security key are required to archive and purge data.

## Expected Disk Space Recovery from Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because of data retention requirements, it has not been possible to measure actual space recovered in a production environment with the use of the purge options. The following list shows the average record size of entries as measured at a test site (at approximately 70% efficiency).

| Record Type       | File | 1k Blocks Per Record |
|-------------------|------|----------------------|
| Pharmacy Co-pay   | 350  | .38                  |
| Billing Clocks    | 351  | .14                  |
| Third Party Bills | 399  | .75                  |

<span id="_Toc127633861" class="anchor"></span>Table : Software Packages

From testing of the software, we have determined that purging small numbers of entries (less than 200) will not yield measurable disk space. However, when large numbers of entries (over 1000) are purged, nearly 97% of the space is recovered. The actual percentage of the space recovered is relative to the number of consecutive entries purged. The number of consecutive records purged is relative to whether the site has closed the bills either by collecting the amount due or cancelling the bills.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The following packages need to be installed on the system prior to installing Integrated Billing V. 2.0.

| Package                    | Name          |
|----------------------------|---------------|
| Accounts Receivable V. 3.7 | IFCAP V. 4.0  |
| Kernel V. 7.1              | OE/RR V. 1.96 |
| Outpatient Pharmacy V. 5.6 | PIMS V. 5.3   |
| VA FileMan V. 20.0         |               |

<span id="_Toc127633862" class="anchor"></span>Table : Subscribing Package

5.  IB V. 2.0 has custodial integration agreements with the following packages.

| SUBSCRIBING PACKAGE           | ICR \# | NAME                                                                           |
|-------------------------------|--------|--------------------------------------------------------------------------------|
| ACCOUNTS RECEIVABLE           | 126    | DBIA126                                                                        |
| ACCOUNTS RECEIVABLE           | 300    | DBIA300                                                                        |
| ACCOUNTS RECEIVABLE           | 301    | DBIA301                                                                        |
| ACCOUNTS RECEIVABLE           | 307    | DBIA307                                                                        |
| ACCOUNTS RECEIVABLE           | 309    | DBIA309                                                                        |
| ACCOUNTS RECEIVABLE           | 1278   | DBIA1278                                                                       |
| ACCOUNTS RECEIVABLE           | 1457   | DBIA1457                                                                       |
| ACCOUNTS RECEIVABLE           | 2031   | DBIA2031                                                                       |
| ACCOUNTS RECEIVABLE           | 2035   | DBIA2035                                                                       |
| ACCOUNTS RECEIVABLE           | 2327   | DBIA2327                                                                       |
| ACCOUNTS RECEIVABLE           | 2328   | DBIA2328                                                                       |
| ACCOUNTS RECEIVABLE           | 3124   | DBIA3124                                                                       |
| ACCOUNTS RECEIVABLE           | 3130   | DBIA3130                                                                       |
| ACCOUNTS RECEIVABLE           | 3343   | DBIA3343                                                                       |
| ACCOUNTS RECEIVABLE           | 3345   | DBIA3345                                                                       |
| ACCOUNTS RECEIVABLE           | 3350   | DBIA3350                                                                       |
| ACCOUNTS RECEIVABLE           | 3733   | GMT Related IB utilities (IA#3733)                                             |
| ACCOUNTS RECEIVABLE           | 3804   | DBIA3804                                                                       |
| ACCOUNTS RECEIVABLE           | 3807   | DBIA3807                                                                       |
| ACCOUNTS RECEIVABLE           | 3808   | DBIA3808                                                                       |
| ACCOUNTS RECEIVABLE           | 3809   | DBIA3809                                                                       |
| ACCOUNTS RECEIVABLE           | 3810   | DBIA3810                                                                       |
| ACCOUNTS RECEIVABLE           | 3811   | DBIA3811                                                                       |
| ACCOUNTS RECEIVABLE           | 3820   | DBIA3820-A                                                                     |
| ACCOUNTS RECEIVABLE           | 3821   | DBIA3820-B                                                                     |
| ACCOUNTS RECEIVABLE           | 3822   | DBIA3820-C                                                                     |
| ACCOUNTS RECEIVABLE           | 3828   | DBIA3820-I                                                                     |
| ACCOUNTS RECEIVABLE           | 4042   | DBIA4042                                                                       |
| ACCOUNTS RECEIVABLE           | 4044   | DBIA4044                                                                       |
| ACCOUNTS RECEIVABLE           | 4045   | DBIA4045                                                                       |
| ACCOUNTS RECEIVABLE           | 4047   | DBIA4047                                                                       |
| ACCOUNTS RECEIVABLE           | 4048   | DBIA4048                                                                       |
| ACCOUNTS RECEIVABLE           | 4050   | DBIA4050                                                                       |
| ACCOUNTS RECEIVABLE           | 4051   | DBIA4051                                                                       |
| ACCOUNTS RECEIVABLE           | 4118   | ALLOW A/R TO UPDATE RATE TYPE FILE                                             |
| ACCOUNTS RECEIVABLE           | 4121   | A/R access to TPJI for patient name OR bill number                             |
| ACCOUNTS RECEIVABLE           | 4385   | MRA related function Calls from AR into IB                                     |
| ACCOUNTS RECEIVABLE           | 4391   | INSURANCE COMPANY FILE ACCESS                                                  |
| ACCOUNTS RECEIVABLE           | 4434   | DBIA4434                                                                       |
| ACCOUNTS RECEIVABLE           | 4435   | DBIA4435                                                                       |
| ACCOUNTS RECEIVABLE           | 4538   | AR ACCESS TO FILE 350.1                                                        |
| ACCOUNTS RECEIVABLE           | 4541   | AR access to INTEGRATED BILLING ACTION file 350                                |
| ACCOUNTS RECEIVABLE           | 4552   | DBIA4552                                                                       |
| ACCOUNTS RECEIVABLE           | 4602   | GET CURRENT INSURANCE                                                          |
| ACCOUNTS RECEIVABLE           | 4603   | FILE 361                                                                       |
| ACCOUNTS RECEIVABLE           | 4604   | FILE 365.12                                                                    |
| ACCOUNTS RECEIVABLE           | 4635   | ROUTINE IBRFN4                                                                 |
| ACCOUNTS RECEIVABLE           | 4777   | AR access to IB Patient Co-pay account data                                    |
| ACCOUNTS RECEIVABLE           | 4957   | DBIA4957                                                                       |
| ACCOUNTS RECEIVABLE           | 4996   | EEOB Worklist NPI inclusion                                                    |
| ACCOUNTS RECEIVABLE           | 5286   | PAY-TO PROVIDER PHONE NUMBER API                                               |
| ACCOUNTS RECEIVABLE           | 5671   | COPY FUNCTIONS FOR IB EOB FILE \#361.1                                         |
| ACCOUNTS RECEIVABLE           | 5710   | POTENTIAL CO-PAYMENT CHARGE AMOUNT                                             |
| AR (ACCOUNTS RECEIVABLE)      | 304    | DBIA304                                                                        |
| AR (ACCOUNTS RECEIVABLE)      | 306    | DBIA306                                                                        |
| AR (ACCOUNTS RECEIVABLE)      | 308    | DBIA308                                                                        |
| AR (ACCOUNTS RECEIVABLE)      | 310    | DBIA310                                                                        |
| AUTOMATED INFO COLLECTION SYS | 645    | DBIA186-E                                                                      |
| AUTOMATED INFO COLLECTION SYS | 1992   | DBIA1992                                                                       |
| AUTOMATED INFO COLLECTION SYS | 2351   | OUTPATIENT ENCOUNTER SEARCH                                                    |
| AUTOMATED MED INFO EXCHANGE   | 4594   | DBIA4589-F                                                                     |
| CMOP                          | 6243   | EPHARMACY BILLABLE STATUS                                                      |
| CMOP                          | 6244   | RETRIEVE SENSITIVE DIAGNOSIS DRUG FROM DRUG FILE                               |
| DSS EXTRACTS                  | 2786   | DBIA2786                                                                       |
| E CLAIMS MGMT ENGINE          | 4299   | DBIA4299                                                                       |
| E CLAIMS MGMT ENGINE          | 4692   | DBIA4692                                                                       |
| E CLAIMS MGMT ENGINE          | 4415   | DBIA4415                                                                       |
| E CLAIMS MGMT ENGINE          | 4693   | DBIA4693                                                                       |
| E CLAIMS MGMT ENGINE          | 4694   | DBIA4694                                                                       |
| E CLAIMS MGMT ENGINE          | 4695   | DBIA4695                                                                       |
| E CLAIMS MGMT ENGINE          | 4696   | DBIA4696                                                                       |
| E CLAIMS MGMT ENGINE          | 4697   | DBIA4697                                                                       |
| E CLAIMS MGMT ENGINE          | 4698   | DBIA4698                                                                       |
| E CLAIMS MGMT ENGINE          | 4710   | DBIA4710                                                                       |
| E CLAIMS MGMT ENGINE          | 4729   | API FOR RX BILLING INFO                                                        |
| E CLAIMS MGMT ENGINE          | 5185   | Update IB NDC NON COVERED BY PLAN FILE \#366.16                                |
| E CLAIMS MGMT ENGINE          | 5210   | IB DRUGS NON COVERED REPORT                                                    |
| E CLAIMS MGMT ENGINE          | 5355   | BILL INFORMATION                                                               |
| E CLAIMS MGMT ENGINE          | 5361   | IBOSRX                                                                         |
| E CLAIMS MGMT ENGINE          | 5572   | IBNCPDPU                                                                       |
| E CLAIMS MGMT ENGINE          | 5576   | DBIA5576                                                                       |
| E CLAIMS MGMT ENGINE          | 5711   | IB NCPDP EVENT LOG FILE                                                        |
| E CLAIMS MGMT ENGINE          | 5712   | PRINT IB ECME BILLING EVENTS REPORT                                            |
| E CLAIMS MGMT ENGINE          | 5713   | IB LIST MANAGER DISPLAY DATA                                                   |
| E CLAIMS MGMT ENGINE          | 5714   | IB PHARMACY INSURANCE                                                          |
| E CLAIMS MGMT ENGINE          | 6061   | IBCNHUT1 (HPID/OEID)                                                           |
| E CLAIMS MGMT ENGINE          | 6131   | IBNCPEV3                                                                       |
| E CLAIMS MGMT ENGINE          | 6136   | DB6136                                                                         |
| E CLAIMS MGMT ENGINE          | 6243   | EPHARMACY BILLABLE STATUS                                                      |
| E CLAIMS MGMT ENGINE          | 6244   | RETRIEVE SESITIVE DIAGNOSIS DRUG FROM DRUG FILE                                |
| E CLAIMS MGMT ENGINE          | 6250   | E-PHARMACY HL7 PROCESSING                                                      |
| ENROLLMENT APPLICATION SYSTEM | 3302   | DBIA3302                                                                       |
| ENROLLMENT APPLICATION SYSTEM | 3717   | DBIA3717                                                                       |
| ENROLLMENT APPLICATION SYSTEM | 3777   | DBIA3777                                                                       |
| ENROLLMENT APPLICATION SYSTEM | 4862   | DBIA4862                                                                       |
| FEE BASIS                     | 228    | DBIA228-A                                                                      |
| FEE BASIS                     | 396    | DBIA396                                                                        |
| FEE BASIS                     | 705    | DBIA228-B                                                                      |
| FEE BASIS                     | 4128   | REVENUE CODE                                                                   |
| FEE BASIS CLAIMS SYSTEM       | 5281   | FBCS File \#353.1 Read only                                                    |
| FEE BASIS CLAIMS SYSTEM       | 5282   | FBCS File \#353.2 Read only                                                    |
| INCOME VERIFICATION MATCH     | 257    | DBIA257                                                                        |
| INCOME VERIFICATION MATCH     | 324    | DBIA324                                                                        |
| INCOME VERIFICATION MATCH     | 944    | DBIA944                                                                        |
| INCOME VERIFICATION MATCH     | 945    | DBIA945                                                                        |
| INCOME VERIFICATION MATCH     | 946    | DBIA946                                                                        |
| INCOME VERIFICATION MATCH     | 947    | DBIA947                                                                        |
| INCOME VERIFICATION MATCH     | 948    | DBIA948                                                                        |
| INCOME VERIFICATION MATCH     | 949    | DBIA949                                                                        |
| INCOME VERIFICATION MATCH     | 950    | DBIA950                                                                        |
| INCOME VERIFICATION MATCH     | 951    | DBIA951                                                                        |
| INCOME VERIFICATION MATCH     | 952    | DBIA952                                                                        |
| INCOME VERIFICATION MATCH     | 2537   | DBIA2537                                                                       |
| INCOME VERIFICATION NAT'L DB  | 1045   | DBIA1045                                                                       |
| INCOME VERIFICATION NAT'L DB  | 1046   | DBIA1046                                                                       |
| INSURANCE CAPTURE BUFFER      | 3302   | DBIA3302                                                                       |
| INSURANCE CAPTURE BUFFER      | 5292   | INSURANCE CO FILE ACCESS                                                       |
| INSURANCE CAPTURE BUFFER      | 5293   | GROUP INSURANCE PLAN ACCESS                                                    |
| INSURANCE CAPTURE BUFFER      | 5294   | INSURANCE BUFFER FILE ACCESS                                                   |
| INSURANCE CAPTURE BUFFER      | 5296   | BILLING PATIENT ACCESS                                                         |
| INSURANCE CAPTURE BUFFER      | 5297   | IIV RESPONSE ACCESS                                                            |
| INSURANCE CAPTURE BUFFER      | 5298   | CLAIMS TRK REVIEW TYPE ACCESS                                                  |
| INSURANCE CAPTURE BUFFER      | 5299   | CLAIMS TRACKING ACTION ACCESS                                                  |
| INSURANCE CAPTURE BUFFER      | 5304   | PATIENT INSURANCE ACCESS                                                       |
| INSURANCE CAPTURE BUFFER      | 5305   | SOURCE OF INFORMATION ACCESS                                                   |
| INSURANCE CAPTURE BUFFER      | 5307   | DSIV CALLS TO IBCNBLL                                                          |
| INSURANCE CAPTURE BUFFER      | 5309   | DSIV CALL TO IBCNERP2                                                          |
| INSURANCE CAPTURE BUFFER      | 5312   | PLAN LIMITATION CATEGORY ACCESS                                                |
| INSURANCE CAPTURE BUFFER      | 5313   | CLAIMS TRACKING ACCESS                                                         |
| INSURANCE CAPTURE BUFFER      | 5314   | HOSPITAL TRACKING ACCESS                                                       |
| INSURANCE CAPTURE BUFFER      | 5339   | ANNUAL BENEFITS ACCESS                                                         |
| INSURANCE CAPTURE BUFFER      | 5340   | INSURANCE REVIEW ACCESS                                                        |
| INSURANCE CAPTURE BUFFER      | 5341   | PLAN COVERAGE LIMITATION                                                       |
| INSURANCE CAPTURE BUFFER      | 5353   | Accept/Reject Insurance Buffer data APIs                                       |
| INSURANCE CAPTURE BUFFER      | 5424   | INSURANCE FILING TIME FRAME                                                    |
| KERNEL                        | 4960   | INSURANCE CO AND PROVIDER ID                                                   |
| KERNEL                        | 4961   | GET PROVIDER ID FROM INSURANCE DATA                                            |
| KERNEL                        | 4962   | GET PROVIDER ID FROM FACILITY BILLING ID                                       |
| KERNEL                        | 4964   | GET FACILITY NAME & FED TAX NUMBER FROM IB SITE PARAMS                         |
| KERNEL                        | 4965   | GET ZERO NODE INFO FROM IB NON/OTHER VA BILLING PROVIDER                       |
| KERNEL                        | 4971   | DBIA4971                                                                       |
| KERNEL                        | 4972   | DBIA4972                                                                       |
| M DATA EXTRACTOR              | 3642   | DBIA3642                                                                       |
| MENTAL HEALTH                 | 794    | DBIA277-H                                                                      |
| MENTAL HEALTH                 | 2782   | DBIA2782                                                                       |
| OUTPATIENT PHARMACY           | 125    | DBIA125-A                                                                      |
| OUTPATIENT PHARMACY           | 592    | DBIA125-B                                                                      |
| OUTPATIENT PHARMACY           | 2030   | DBIA2030                                                                       |
| OUTPATIENT PHARMACY           | 2215   | DBIA2215                                                                       |
| OUTPATIENT PHARMACY           | 2216   | DBIA2216                                                                       |
| OUTPATIENT PHARMACY           | 2245   | DBIA2245                                                                       |
| OUTPATIENT PHARMACY           | 3877   | DBIA 3877                                                                      |
| OUTPATIENT PHARMACY           | 4115   | DBIA4115                                                                       |
| OUTPATIENT PHARMACY           | 4664   | PFSS ACCOUNT                                                                   |
| OUTPATIENT PHARMACY           | 4665   | PFSS CHARGE                                                                    |
| OUTPATIENT PHARMACY           | 4741   | PFSS ACCOUNT REFERENCE                                                         |
| OUTPATIENT PHARMACY           | 6243   | EPHARMACY BILLABLE STATUS                                                      |
| OUTPATIENT PHARMACY           | 6244   | RETRIEVE SENSITIVE DIAGNOSIS DRUG FROM DRUG FILE                               |
| PATIENT DATA EXCHANGE         | 271    | DBIA271-A                                                                      |
| PATIENT DATA EXCHANGE         | 766    | DBIA268-B                                                                      |
| PATIENT DATA EXCHANGE         | 773    | DBIA271-B                                                                      |
| PATIENT DATA EXCHANGE         | 774    | DBIA271-C                                                                      |
| PATIENT DATA EXCHANGE         | 2780   | DBIA2780                                                                       |
| PROSTHETICS                   | 612    | DBIA142-B                                                                      |
| REGISTRATION                  | 1936   | DBIA1936                                                                       |
| REGISTRATION                  | 2037   | DBIA2037                                                                       |
| REGISTRATION                  | 2538   | DBIA2538                                                                       |
| REGISTRATION                  | 2643   | DBIA2643                                                                       |
| REGISTRATION                  | 4288   | RETRIEVE INSURANCE DATA                                                        |
| REGISTRATION                  | 4524   | DBIA4524                                                                       |
| REGISTRATION                  | 4709   | PFSS PROCESS INSURANCE FROM DG REGISTRATION                                    |
| REGISTRATION                  | 4785   | INSURANCE BUFFER FILE ACCESS                                                   |
| REGISTRATION                  | 4786   | PATIENT FSC FILE ACCESS                                                        |
| REGISTRATION                  | 4787   | VISTA FSC FILE ACCESS                                                          |
| REGISTRATION                  | 4788   | COMMERCIAL INSURANCE FILE ACCESS                                               |
| REGISTRATION                  | 4789   | PFSS PLAN FILE ACCESS                                                          |
| REGISTRATION                  | 4790   | PFSS INSURANCE STATUS UPDATE                                                   |
| REGISTRATION                  | 6231   | Allows DATE OF DEATH entry to automatically terminate active patient policies. |
| SCHEDULING                    | 2781   | DBIA2781                                                                       |
| SCHEDULING                    | 4987   | IB BILLING DATA API                                                            |
| SCHEDULING                    | 5029   | VERIFY SC APPOINTMENT TYPE                                                     |
| SOCIAL WORK                   | 61     | DBIA61                                                                         |
| Unknown                       | 2034   | DBIA2034                                                                       |
| Unknown                       | 4419   | DBIA4419                                                                       |
| Unknown                       | 4663   | PFSS ON/OFF SWITCH                                                             |
| Unknown                       | 10147  | IBARXEU                                                                        |
| UTILIZATION MANAGEMENT ROLLUP | 1137   | DBIA1137                                                                       |
| UTILIZATION MANAGEMENT ROLLUP | 1327   | DBIA1327                                                                       |
| UTILIZATION MANAGEMENT ROLLUP | 1329   | DBIA1329                                                                       |
| UTILIZATION MANAGEMENT ROLLUP | 1351   | DBIA1351                                                                       |
| UTILIZATION MANAGEMENT ROLLUP | 1354   | DBIA1354                                                                       |

<span id="_Toc127633863" class="anchor"></span>Table : Package-wide Variables

6.  IB V. 2.0 has requested integration agreements with the following packages and have been approved.
1.  Accounts Receivable (ICR#s 127, 380-389,1452, 5549, 6237, and 6238)

    AR provides IB with the following:
    - A routine used for setting up a new charge for a debtor.
    - Allows the IB ACTION TYPE file (#350.1) to point to the ACCOUNTS RECEIVABLE CATEGORY file (#430.2).
    - Look-up to the ACCOUNTS RECEIVABLE file (#430).
    - Set the STATEMENT DAY field.
    - Reference to determine the internal number of decrease and increase adjustment types.
      - RCJIBFN2 APIs for ACCOUNTS RECEIVABLE file ( \#430)
      - RCDPAYER API reads payer contact information from ELECTRONIC REMITTANCE ADVICE file (#344.4).
    - Allows IB access to the AR EDI CARC DATA file (#345) and AR EDI CARC DATA file (#346) for Explanation of Benefits (EOB) displays and reports of adjustment reason codes.
2.  DRG Grouper (ICR#s 368, 369, 370, 371)

> DRG Grouper provides IB with the following:

- Direct reference to specific fields within the ICD DIAGNOSIS file (#80).
- Direct reference to specific fields within the ICD OPERATION/PROCEDURE file (#80.1).
- Store pointers to the DRG file (#80.2) to retrieve data at the time claims are generated.
- A call to calculate interim DRGs to determine the expected length of stay for a visit.
3.  Health Summary (ICR# 253)

> Health Summary allows IB to do lookups to the HEALTH SUMMARY TYPE file (#142) and to print health summaries.

4.  HINQ (ICR# 379)

> Hospital Inquiry (HINQ) provides IB a call to allow billing clerks to replace requests for HINQ inquiries for potentially billable patients with unverified eligibility.

5.  IFCAP (ICR# 353)

> IFCAP provides IB with the short description describing the name of a prosthetic device that is being billed on a claim to a third-party carrier.

6.  Kernel (ICR# 372)

> Kernel gives permission to IB to add entries to the INSTITUTION file (#4) when creating bills.

7.  List Manager (ICR# 367)

> List Manager provides IB with calls used to refresh the screen and reset the scrolling area while program control remains with an action.

8.  Outpatient Pharmacy (ICR#s 124, 237)

> Outpatient Pharmacy provides IB with the following:

- A call to display information from the PRESCRIPTION file (#52).
- Reference to determine prescription number and drug name.
- Printing of the Action Profile and Information Profile.
- Stores pointers to the PRESCRIPTION (#52) and DRUG (#50) files to retrieve data at the time claims are generated.
- Directly reference selected fields in the PRESCRIPTION (#52) and DRUG (#50) files.
- Directly reference the OUTPATIENT VERSION field (#49.99) of the PHARMACY SYSTEM file (#59.7).
9.  Patient Data Exchange (ICR# 272)

> PDX allows IB to directly reference fields in the VAQ-TRANSACTION (#394.61) and VAQ-DATA SEGMENT (#394.71) files.

10. Patient File (ICR# 187)

> The PATIENT file (#2) provides direct references to IB for the purpose of sorting and printing on a patient's Ambulatory Surgery Check-off Sheet.

11. Problem List (ICR# 354)

> Problem List provides IB with a call to obtain a list of a patient's active problems. It also provides a call for IB to access the EXPRESSIONS file

> (#757.01) to create lists of common problems by clinic.

12. Prosthetics (ICR#s 373, 374)

> Prosthetics provides IB with the following:

- Stores pointers to the RECORD OF PROS APPLIANCE/REPAIR (#660) and PROS ITEM MASTER (#661) files to retrieve data at the time claims are generated.
- Print item name on screens and bills.
- Call to find potentially billable prosthetic items.
- Call to find prosthetic items that may have been delivered to a patient within a specific date range.
- Direct reference to specific fields in the RECORD OF PROS APPLIANCE/REPAIR file (#660).
13. Registration (ICR# 186, 414-434, 5158, 6130, 7182)

> Registration provides IB with the following:

- Multiple calls to obtain Means Test data.
- Medical center division by which to sort and print various reports.
- Patient eligibility data to print on various documents.
- Patient Treatment File information for display and to bill.
- Patient Enrollment Group information.
- Patient Eligibility information for Urgent Care Visit Tracking Review.
14. Scheduling (ICR# 188, 397-411)

> Scheduling provides IB with the following:

- Multiple calls to get patient appointment data for check-off sheets and encounter forms.
- Calls to get clinic and division information for various reports.
15. Accounts Receivable (IA#380)
    - The following function calls are made to the routine PRCAFN.
    - Active B\*2.0\*432.
16. KERNEL (IA#2171)
    - Function API's to access parts of the Institution file.
    - Active IB\*2.0\*432.
17. KERNEL (IA#4129)
    - The IB package has MRA (Medicare Remittance Advice) functionality using a specific, non-human user in file 200.
    - Active IB\*2.0\*432.
18. KERNEL (IA#4677)
    - To support the J2EE middle tier the concept of an APPLICATION PROXY user was created. This is a username that an application sets that has a user class of Application Proxy
    - Active IB\*2.0\*432

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the IB V. 2.0 package options have been designed to stand alone.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Though there are no variables that can always be assumed to be present in Integrated Billing, the following is a list of common variables and meaning.

<table>
<caption><p><span id="_Toc127633864" class="anchor"></span>Table : FileMan Access Codes</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IBAFY</td>
<td>The current fiscal year.</td>
</tr>
<tr class="even">
<td>IBARTYP</td>
<td>The Accounts Receivable Category pointer value stored in the IB ACTION TYPE file (#350.1) for the current entry.</td>
</tr>
<tr class="odd">
<td>IBATYP</td>
<td>The pointer value to the IB ACTION TYPE file (#350.1) for the current entry.</td>
</tr>
<tr class="even">
<td>IBCHCDA</td>
<td>Pointer to IB Action - Inpatient IB Action Charge for co-payments.</td>
</tr>
<tr class="odd">
<td>IBCHPDA</td>
<td>Pointer to IB Action - Inpatient IB Action Charge for per diems.</td>
</tr>
<tr class="even">
<td>IBCLDA</td>
<td>Pointer to Cat C Billing Clock record (File #351).</td>
</tr>
<tr class="odd">
<td>IBCLDAY</td>
<td>Cat C Billing Clock Inpatient Days within one clock.</td>
</tr>
<tr class="even">
<td>IBCLDOL</td>
<td>Cat C Billing Clock Inpatient dollars for current 90 days of care.</td>
</tr>
<tr class="odd">
<td>IBCLDT</td>
<td>Cat C Billing Clock Start Date.</td>
</tr>
<tr class="even">
<td>IBDESC</td>
<td>The brief description to / from the INTEGRATED BILLING ACTION file (#350).</td>
</tr>
<tr class="odd">
<td>IBDUZ</td>
<td>The user DUZ as passed from an application. In the background filer, the user who caused the filer to be queued will be reflected in the DUZ variable; however, IBDUZ should equal the user causing the current transaction.</td>
</tr>
<tr class="even">
<td>IBEVCAL</td>
<td>IB Action Event last calculated date.</td>
</tr>
<tr class="odd">
<td>IBEVDA</td>
<td>Pointer to IB Action - Inpatient IB Action Event.</td>
</tr>
<tr class="even">
<td>IBEVDT</td>
<td>IB Action Event event date.</td>
</tr>
<tr class="odd">
<td>IBFAC</td>
<td>Institution from File #350.9 (points to File #4).</td>
</tr>
<tr class="even">
<td>IBHANG</td>
<td>The number of seconds the background filer should hang after finishing posting all transactions and waiting to look for more transactions to post.</td>
</tr>
<tr class="odd">
<td>IBIL</td>
<td>The AR bill number or Charge ID.</td>
</tr>
<tr class="even">
<td>IBJOB</td>
<td>Identifies IB job (1-Inpt BGJ, 2-Inpt Discharge job, etc.).</td>
</tr>
<tr class="odd">
<td>IBLAST</td>
<td>The most recent transaction for a given new transaction. If there have been no subsequent transactions to a new transaction, it will equal the new transaction. However, if a transaction has been cancelled or updated, this will be the pointer to the most recent (last) cancellation or update.</td>
</tr>
<tr class="even">
<td>IBLINE</td>
<td>Used to draw lines (79 or 80 dashes).</td>
</tr>
<tr class="odd">
<td>IBN</td>
<td>The pointer to the Integrated Billing Action file (#350) for the current action.</td>
</tr>
<tr class="even">
<td>IBND</td>
<td>The zero node from the Integrated Billing Action file (#350) - (e.g., IBND=^IB[IBN,O]).</td>
</tr>
<tr class="odd">
<td>IBNOS</td>
<td>The list of pointer values to the Integrated Billing Action file (#350) that are to be combined and passed to AR as one transaction.</td>
</tr>
<tr class="even">
<td>IBNOW</td>
<td>Contains the current date / time.</td>
</tr>
<tr class="odd">
<td>IBOP</td>
<td>Identifies IB Archive / Purge operation (1-Search, 2-Archive, 3-Purge).</td>
</tr>
<tr class="even">
<td>IBPARNT</td>
<td>The original NEW Integrated Billing Action for any action. This will be the pointer value. For NEW Actions, this will point to itself.</td>
</tr>
<tr class="odd">
<td>IBSEQNO</td>
<td><p>IB Action sequence number:</p>
<blockquote>
<p>1-New</p>
<p>2-Cancel</p>
<p>3-Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IBSERV</td>
<td>Service associated with billing application (points to File #49).</td>
</tr>
<tr class="odd">
<td>IBSITE</td>
<td>Institution site number.</td>
</tr>
<tr class="even">
<td>IBSL</td>
<td>IB Action soft link.</td>
</tr>
<tr class="odd">
<td>IBTOTL</td>
<td>Dollar amount passed to Accounts Receivable must be greater than zero to pass charges.</td>
</tr>
<tr class="even">
<td>IBTRAN</td>
<td>The AR Transaction number for a NEW IB Action, the value returned after passing a transaction to AR. More than one IB Action may have the same AR Transaction.</td>
</tr>
<tr class="odd">
<td>IBWHER</td>
<td>Codes to denote processing point in case of error.</td>
</tr>
<tr class="even">
<td>IBY</td>
<td>Error processing (equals 1 or -1^error code).</td>
</tr>
</tbody>
</table>

<span id="_Toc127633864" class="anchor"></span>Table : FileMan Access Codes

# How to Generate online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure Integrated Billing technical documentation. Online technical documentation pertaining to the Integrated Billing software, in addition to the help prompts and, on the help, screens that are found throughout the Integrated Billing package, may be generated through utilization of several Kernel options. These include but are not limited to %INDEX; Menu Management, Inquire (Option File) and Print Option File; VA FileMan Data Dictionary Utilities, List File Attributes.

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options that can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities that supply online technical information, please consult the DHCP Kernel Reference Manual.

## %Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adhere(s) to DHCP Programming Standards. The %INDEX output may include the following components: compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Globals, Label References, and External References. By running %INDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from DHCP Programming Standards that exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run %INDEX for the Integrated Billing package, specify the following namespace(s) at the "routine(s) ?\>" prompt: IB.

Integrated Billing initialization routines that reside in the UCI in which %INDEX is being run, as well as local routines found within the Integrated Billing namespace, should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

## Inquire (Option File)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Menu Management option provides the following information about a specified option: option name, menu text, option description, type of option, and lock, if any. In addition, all items on the menu are listed for each menu option.

To secure information about Integrated Billing options, the user must specify the name or namespace of the option(s) desired. The namespace associated with the Integrated Billing package is IB.

## Print Option File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This utility generates a listing of options from the OPTION file. The user may choose to print all the entries in this file or may elect to specify a single option or range of options. To obtain a list of Integrated Billing options, the following option namespace should be specified: IB.

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s).

- File name and description
- Identifiers
- Cross-references
- Files pointed to by the file specified
- Files that point to the file specified
- Input, print, and sort templates

In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location and description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output that lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates. For a comprehensive listing of Integrated Billing files, please refer to the Files Section of this manual.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File Protection 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Electronic Data Interface contains files that are standardized. Files carry a higher level of file protection regarding Delete, Read, Write, and LAYGO access, and should not be edited locally unless otherwise directed. The data dictionaries for all files should NOT be altered.

The following is a list of recommended VA FileMan access codes associated with each file contained in the KIDS build for the EDI interface.

| File \# | File Name                          | DD  | RD  | WR  | DEL | LAYGO | AUDIT |
|---------|------------------------------------|-----|-----|-----|-----|-------|-------|
| 36      | INSURANCE COMPANY                  | \#  |     | D   | d   | d     |       |
| 350.8   | IB ERROR                           | @   | @   | @   | @   | @     | @     |
| 350.9   | IB SITE PARAMETERS                 | @   | @   | @   | @   | @     | @     |
| 353.3   | IB ATTACHMENT REPORT TYPE          | @   | @   | @   | @   | @     | @     |
| 355.3   | GROUP INSURANCE PLAN               | @   |     | @   | @   | @     | @     |
| 355.33  | INSURANCE VERIFICATION PROCESSOR   | @   | @   | @   | @   | @     | @     |
| 355.93  | IB NON/OTHER VA BILLING PROVIDER   | @   |     |     |     |       | @     |
| 355.98  | IB ALTERNATE PRIMARY ID TYPES      | @   | @   | @   | @   | @     | @     |
| 361.1   | EXPLANATION OF BENEFITS            | @   | @   | @   | @   | @     | @     |
| 362.4   | IB BILL/CLAIMS PRESCRIPTION REFILL | @   |     | @   | @   | @     | @     |
| 364.1   | EDI TRANSMISSION BATCH             | @   | @   | @   | @   | @     | @     |
| 364.5   | IB DATA ELEMENT DEFINITION         |     |     |     |     |       |       |
| 364.6   | IB FORM SKELETON DEFINITION        |     |     |     |     |       |       |
| 364.7   | IB FORM FIELD CONTENT              |     |     |     |     |       |       |
| 366.03  | PLAN                               | @   |     |     |     |       |       |
| 366.14  | IB NCPDP EVENT LOG                 |     |     |     |     |       |       |
| 366.17  | IB NCPDP NON-BILLABLE REASONS      |     |     |     |     |       |       |
| 367     | HPID/OEID RESPONSE                 | @   |     |     |     |       |       |
| 367.1   | HPID/OEID TRANSMISSION QUEUE       | @   |     |     |     |       |       |
| 367.11  | INSURANCE COMPANY ID TYPE          | @   |     | @   | @   | @     |       |
| 399     | BILL/CLAIMS                        | @   | @   | @   | @   | @     |       |
| 399.6   | CMN FORM TYPES                     | @   | @   | @   | @   | @     | @     |

<span id="_Toc30513948" class="anchor"></span>Table : Acronyms and Abbreviations

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions and explanations for terms and acronyms relevant to the content presented within this document. For additional terms and acronyms, include references to other VA acronym and glossary repositories (e.g., VA Acronym Lookup and OIT Master Glossary).

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym or Term</th>
<th>Definition / Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Action Type</td>
<td>The type of event that an application passes to Integrated Billing.</td>
</tr>
<tr class="even">
<td>Admission Sheet</td>
<td><p>(a.k.a. Attestation Sheet)</p>
<p>This is a worksheet commonly used in the front of inpatient charts with a workspace available for concurrent reviews.</p></td>
</tr>
<tr class="odd">
<td>ADPAC</td>
<td>Automated Data Processing Applications Coordinator</td>
</tr>
<tr class="even">
<td>ADT</td>
<td>Admit, Discharge, and Transfer</td>
</tr>
<tr class="odd">
<td>AITC</td>
<td>Austin Information Technology Center</td>
</tr>
<tr class="even">
<td>ALOS</td>
<td>Average Length of Stay</td>
</tr>
<tr class="odd">
<td>AMIS</td>
<td>Automated Management Information System</td>
</tr>
<tr class="even">
<td>Annual Benefits</td>
<td>The amount or percentages of coverage for specific types of care under an insurance plan.</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Programming Interface</td>
</tr>
<tr class="even">
<td><p>AR,</p>
<p>A/R</p></td>
<td><p>Accounts Receivable.</p>
<p>This is a system of bookkeeping necessary to track VAMC debt collection.</p></td>
</tr>
<tr class="odd">
<td>Automated Biller</td>
<td>This is a new utility introduced in IB v2.0 for the purpose of establishing third party bills with no user intervention.</td>
</tr>
<tr class="even">
<td>Background Filer</td>
<td>A background job that accumulates charges and causes adjustment transactions to a bill.</td>
</tr>
<tr class="odd">
<td>BASC</td>
<td>Billable Ambulatory Surgical Code</td>
</tr>
<tr class="even">
<td>Benefits Used</td>
<td>The amounts or portions of a patient's insurance policy that have been used (i.e., deductibles, annual or lifetime maximums).</td>
</tr>
<tr class="odd">
<td>Billing Clock</td>
<td>A 365-day period, usually beginning when a patient is Means Tested and is placed in Category C, through which a patient's Means Test charges are tracked. An inpatient's Medicare deductible co-payment entitles the patient to 90 days of hospital / nursing home care. These 90 days must fall within the 365-day billing clock.</td>
</tr>
<tr class="even">
<td>Block</td>
<td>A rectangular region on an encounter form. Attributes include position, size, outline type, and header. All other form components are contained within a block, and the position is relative to the block's position.</td>
</tr>
<tr class="odd">
<td>Category C</td>
<td>Category C patients are responsible for making co-payments as a result of Means Test legislation.</td>
</tr>
<tr class="even">
<td>Check-off Sheet</td>
<td>A site configurable printed form containing CPT codes, descriptions, and dollar amounts (optional). Each check-off sheet may be assigned to an individual clinic or multiple clinics.</td>
</tr>
<tr class="odd">
<td>Claims Tracking</td>
<td>This is a new module in Integrated Billing that allows for the tracking of an episode of care from scheduling through final disposition of a bill.</td>
</tr>
<tr class="even">
<td>CMN</td>
<td>Certificate of Medical Necessity</td>
</tr>
<tr class="odd">
<td>Collateral Visit</td>
<td>A visit by a non-veteran patient whose appointment is related to or associated with a service-connected patient's treatment.</td>
</tr>
<tr class="even">
<td>Column</td>
<td>A selection list contains one or more columns, a column being a rectangular area that contains a portion of the entries on a selection list. Attributes include position and height.</td>
</tr>
<tr class="odd">
<td>Community Care</td>
<td>Medical care received outside of a VA facility.</td>
</tr>
<tr class="even">
<td>Concurrent Reviews</td>
<td>Review of patients by the hospital Utilization Review performed during the patient's hospital stay.</td>
</tr>
<tr class="odd">
<td>Consistency Checker</td>
<td>Review of patients by the hospital Utilization Review performed during the patient's hospital stay.</td>
</tr>
<tr class="even">
<td>Continuous Patient</td>
<td>Patients continuously hospitalized at the same level of care since July 1, 1986.</td>
</tr>
<tr class="odd">
<td>Converted Charges</td>
<td>During the conversion, the BILLS/CLAIMS file (#399) is checked to ensure that each outpatient visit has been billed. For each visit without an established bill, one is established and given a status of CONVERTED.</td>
</tr>
<tr class="even">
<td>Co-payment</td>
<td>The charges required by legislation, that a patient is billed for services or supplies.</td>
</tr>
<tr class="odd">
<td>CPT</td>
<td>Current Procedural Terminology. A coding method developed by the American Hospital Association to assign code numbers to procedures that are used for research, statistical, and reimbursement purposes.</td>
</tr>
<tr class="even">
<td>Data Field</td>
<td>A block component that is the means by which data from DHCP is printed to the form. The data is obtained at the time the form is printed (i.e., it is not stored with the form) and can be particular to the patient. A data field can have subfields, that are conceptually a collection of related data fields. Attributes include label, label type (underlined, bold, and invisible), position, data area, data length and position (area on the form allocated to the data), item number, and package interface (the routine used to get the data).</td>
</tr>
<tr class="odd">
<td>DHCP</td>
<td>Decentralized Hospital Computer Program</td>
</tr>
<tr class="even">
<td>Diagnosis Code</td>
<td>A numeric or alpha-numeric classification of the terms describing medical conditions, causes, or diseases.</td>
</tr>
<tr class="odd">
<td>Discharge Summary</td>
<td>An admission summary usually completed by the clinician upon the patient's discharge from the hospital.</td>
</tr>
<tr class="even">
<td>ECME</td>
<td>Electronic Claims Management Engine</td>
</tr>
<tr class="odd">
<td>EDI</td>
<td>Electronic Data Interchange</td>
</tr>
<tr class="even">
<td>EICD</td>
<td>Electronic Insurance Coverage Discovery – this refers to the added functionality IB*2*621 delivered to identify patient insurance through an electronic transaction sent to a contracted clearinghouse.</td>
</tr>
<tr class="odd">
<td>Encounter Form</td>
<td>A paper form used to display data pertaining to an outpatient visit and to collect additional data pertaining to that visit.</td>
</tr>
<tr class="even">
<td>Entry Action</td>
<td>An attribute of a package interface. It is MUMPS code that is executed before the interface's entry point is executed.</td>
</tr>
<tr class="odd">
<td>EP</td>
<td>Expert Panel</td>
</tr>
<tr class="even">
<td>Exit Action</td>
<td>An attribute of a package interface. It is MUMPS code that is executed after the interface's entry point is executed.</td>
</tr>
<tr class="odd">
<td>Form Line</td>
<td>A block component. A straight line that will be printed to the form. Attributes include orientation (horizontal, vertical), position, and length.</td>
</tr>
<tr class="even">
<td>Form Locator</td>
<td>A block on the UB or HCFA bill form.</td>
</tr>
<tr class="odd">
<td>FSC</td>
<td>Financial Services Center</td>
</tr>
<tr class="even">
<td>Group Plan</td>
<td>A specific health insurance plan that an insurance company offers.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="even">
<td>HCFA</td>
<td>Health Care Finance Administration</td>
</tr>
<tr class="odd">
<td>HCFA-1500</td>
<td>AMA approved health insurance claim form used for outpatient third party billings.</td>
</tr>
<tr class="even">
<td>HCSR</td>
<td>Health Care Service Review</td>
</tr>
<tr class="odd">
<td>HINQ</td>
<td>Hospital Inquiry</td>
</tr>
<tr class="even">
<td>HL7</td>
<td>Health Level 7</td>
</tr>
<tr class="odd">
<td>Hospital Review</td>
<td>The application of Utilization Review criteria to determine if admissions or continued stay in the hospital meets certain guidelines. Refers to QM mandated reviews.</td>
</tr>
<tr class="even">
<td>HPID</td>
<td>Health Plan Identifier</td>
</tr>
<tr class="odd">
<td>IB</td>
<td>Integrated Billing</td>
</tr>
<tr class="even">
<td>ICD-10</td>
<td><p>International Classification of Diseases, the Tenth Modification.</p>
<p>A coding system designed by the World Health Organization to assign code numbers to diagnoses and procedures for statistical, research, and reimbursement purposes.</p></td>
</tr>
<tr class="odd">
<td>ICD-9</td>
<td><p>International Classification of Diseases, the Ninth Modification.</p>
<p>A coding system designed by the World Health Organization to assign code numbers to diagnoses and procedures for statistical, research, and reimbursement purposes.</p></td>
</tr>
<tr class="even">
<td>ICR</td>
<td>Integration Control Registration replaces DBIA (Database Integration Agreement)</td>
</tr>
<tr class="odd">
<td>IdM</td>
<td>Identity Management Service</td>
</tr>
<tr class="even">
<td>Insurance Data Capture</td>
<td>This is a new module in Integrated Billing that is used to capture and store insurance company and patient insurance information.</td>
</tr>
<tr class="odd">
<td>Insurance Review</td>
<td>The input of UR information about insurance company contact and insurance company action.</td>
</tr>
<tr class="even">
<td>Integrated Billing Action</td>
<td>The billing record created when an application passes an event to Integrated Billing that may cause a charge adjustment (increase or decrease) in the amount a debtor may owe; or a supporting event to document an event that causes a charge adjustment to a debtor.</td>
</tr>
<tr class="odd">
<td>InterQual Criteria</td>
<td>A method of evaluating appropriateness of care.</td>
</tr>
<tr class="even">
<td>IRM</td>
<td>Information Resources Management</td>
</tr>
<tr class="odd">
<td>Item Number</td>
<td>An attribute that must be specified when defining a data field if the data field's package interface returns a list. The item number is used to specify which item on the list should be printed to the data field. For example, there is a package interface for returning service-connected conditions. The first data field created for a form for displaying a service-connected condition would specify item number one.</td>
</tr>
<tr class="even">
<td>Locality Rate - The Geographic Wage Index that is used to account for wage Modifier</td>
<td>The Geographic Wage Index that is used to account for wage differences in different localities when calculating the ambulatory surgery charge. It is multiplied by the wage component to get the final geographic wage component of the charge.</td>
</tr>
<tr class="odd">
<td>Marking Area</td>
<td>The areas on a selection list that the user marks to indicate selections from the list (e.g., ( ), [ ], { }).</td>
</tr>
<tr class="even">
<td>MAS</td>
<td>Medical Administration Service</td>
</tr>
<tr class="odd">
<td>MCCF</td>
<td>Medical Care Collection Fund</td>
</tr>
<tr class="even">
<td>MCCR</td>
<td><p>Medical Care Cost Recovery</p>
<p>The collection of monies by the Department of Veterans Affairs (VA).</p></td>
</tr>
<tr class="odd">
<td>Means Test</td>
<td>A financial report used to determine if a patient may be required to make co-payments for care.</td>
</tr>
<tr class="even">
<td>MIRMO</td>
<td>Medical Information Resources Management Office</td>
</tr>
<tr class="odd">
<td>NCPDP</td>
<td>National Council for Prescription Drug Programs</td>
</tr>
<tr class="even">
<td>NHIN</td>
<td>National Health Information Network</td>
</tr>
<tr class="odd">
<td>NIF</td>
<td>National Insurance File</td>
</tr>
<tr class="even">
<td>Non-MCCF</td>
<td>Refers to VA Facility staff whose Funds are collected for the Medical Services 360160.</td>
</tr>
<tr class="odd">
<td>OEID</td>
<td>Other Entity Identifier</td>
</tr>
<tr class="even">
<td>OIT</td>
<td>Office of Information and Technology</td>
</tr>
<tr class="odd">
<td>Options</td>
<td>The different functions within menus.</td>
</tr>
<tr class="even">
<td>Package Interface</td>
<td>A table that is the method by which the Encounter Form Utilities interface with other packages. Presently there are three types of package interfaces: for printing reports via the Print Manager, printing data to data fields, and for entering data to selection lists. Attributes include entry point, routine, entry action, exit action, protected variables, required variables, data type, data description, and custodial package.</td>
</tr>
<tr class="odd">
<td>PBM</td>
<td>Pharmacy Benefits Manager</td>
</tr>
<tr class="even">
<td>PDX</td>
<td>Patient Data Exchange</td>
</tr>
<tr class="odd">
<td>Per Diem</td>
<td>The daily co-pay charge for hospital or nursing home care.</td>
</tr>
<tr class="even">
<td>PIMS</td>
<td>Patient Information Management System</td>
</tr>
<tr class="odd">
<td>Policy</td>
<td>The specific patient information about a health insurance policy. A policy may reference a group plan.</td>
</tr>
<tr class="even">
<td>Principal Diagnosis</td>
<td>Condition established after study to be chiefly responsible for the patient's admission.</td>
</tr>
<tr class="odd">
<td>Print Manager</td>
<td>A utility used to define the reports and encounter forms that should be printed for clinics. It will then print the reports and forms in packets for each appointment specified.</td>
</tr>
<tr class="even">
<td>Problem List</td>
<td>This is a clinical software package used to track a patient's problems across clinical specialties.</td>
</tr>
<tr class="odd">
<td>Protected Variable</td>
<td>An attribute of a package interface. It is a variable that should be "new'ed" before calling the interface's entry point.</td>
</tr>
<tr class="even">
<td>Provider</td>
<td>A person, facility, organization, or supplier that furnishes health care services.</td>
</tr>
<tr class="odd">
<td>QM</td>
<td>Quality Management</td>
</tr>
<tr class="even">
<td>Reimbursable Insurance</td>
<td>Health insurance that will reimburse VA for the cost of medical care provided to its subscribers.</td>
</tr>
<tr class="odd">
<td>Required Variable</td>
<td>An attribute of a package interface. It is a variable that must exist for the interface's entry point to be called.</td>
</tr>
<tr class="even">
<td>Revenue Code</td>
<td>A code identifying the type of care provided on a third-party bill.</td>
</tr>
<tr class="odd">
<td>RFAI</td>
<td>Request For Additional Information</td>
</tr>
<tr class="even">
<td>RPC</td>
<td>Remote Procedure Calls</td>
</tr>
<tr class="odd">
<td>SACC</td>
<td>Standards and Conventions Committee</td>
</tr>
<tr class="even">
<td>Security Code</td>
<td>A code assigned to each user identifying him / her specifically to the system and allowing him/her access to the functions / options assigned to him / her.</td>
</tr>
<tr class="odd">
<td>Security Key</td>
<td>Used in conjunction with locked options or functions. Only holders of this key may perform these options/functions. Used for options that perform a sensitive task.</td>
</tr>
<tr class="even">
<td>Selection</td>
<td>A component of a selection list. It is a single entry on the list. It is stored with the form and is usually data taken from a file in DHCP such as a CPT code with its description.</td>
</tr>
<tr class="odd">
<td>Selection Group</td>
<td>A component of a selection list. It is a named group of selections on the list. Attributes include a header and the print order.</td>
</tr>
<tr class="even">
<td>Selection List</td>
<td>A block component whose purpose is to contain a list (e.g., a list of CPT codes). The list contains sub columns for marking areas, which are areas meant to be marked to indicate selections being made from the list. Attributes include headers, sub columns, sub column width, sub column type, package interface (the routine used to fill the list), and many attributes for the appearance of the list.</td>
</tr>
<tr class="odd">
<td>SSVI</td>
<td><p>System Shared Verified Insurance</p>
<p>A component that moves insurance data between multiple sites that are used by a single patient.</p></td>
</tr>
<tr class="even">
<td>Stop Code</td>
<td>A three-digit number corresponding to an additional stop/service a patient received in conjunction with a clinic visit. Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit.</td>
</tr>
<tr class="odd">
<td>Sub-column</td>
<td>A component of a selection list. It can contain either text such as a CPT code, or a marking area.</td>
</tr>
<tr class="even">
<td>Subfield</td>
<td>A component of a data field. It can display a single value, whereas a data field can be used to display a collection of related values. Attributes include those for the label and the area on the form to print the data. Also, for package interfaces that return records that have multiple values, the data must be specified.</td>
</tr>
<tr class="odd">
<td>Text Area</td>
<td>A rectangular area in a block that is used to display a word-processing field. The text is automatically formatted to fit within the block. Attributes include the word-processing field, the position, and size of the text area. The text is stored with the form.</td>
</tr>
<tr class="even">
<td>Third Party Billings</td>
<td>Billings where a party other than the patient is billed.</td>
</tr>
<tr class="odd">
<td>Tool Kit</td>
<td>A set of pre-configured encounter forms and blocks to facilitate sites' use of the Encounter Forms package.</td>
</tr>
<tr class="even">
<td>UB-82</td>
<td>AMA approved health insurance claim form used for Third Party billings.</td>
</tr>
<tr class="odd">
<td>UB-92</td>
<td>AMA approved health insurance claim form used for Third Party billings.</td>
</tr>
<tr class="even">
<td>UR</td>
<td><p>Utilization Review.</p>
<p>A review carried out by allied health personnel at pre-determined times during the hospital stay to assess the appropriateness of care.</p></td>
</tr>
<tr class="odd">
<td>Urgent Care</td>
<td>Urgent care is a category of walk-in clinic focused on the delivery of ambulatory care in a dedicated medical facility outside of a traditional emergency department (emergency room). Urgent care centers primarily treat injuries or illnesses requiring immediate care, but not serious enough to require an emergency department (ED) visit.</td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Veterans Integrated Service Network</td>
</tr>
<tr class="odd">
<td>Wage Percentage</td>
<td>The percentage of the rate group unit charge that is the wage component to be used in calculating the HCFA charge for ambulatory surgical procedures.</td>
</tr>
</tbody>
</table>