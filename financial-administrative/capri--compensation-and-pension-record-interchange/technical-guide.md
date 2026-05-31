---
title: CAPRI System Administration and Technical Guide (Updated DVBA*2.7*255)
doc_type: TG
doc_label: Technical Guide
doc_layer: anchor
doc_subject: null
app_code: CAPRI
app_name: Compensation and Pension Record Interchange
section: FIN
app_status: active
pkg_ns: CAPRI
patch_ver: 2.7
patch_id: CAPRI*2.7
group_key: CAPRI:CAPRI:2.7
file_numbers:
- '2'
- '4'
- '9'
- '38.1'
- '40.8'
- '43'
- '200'
- '391.91'
- '396'
- '396.1'
- '396.17'
- '396.2'
- '396.3'
- '396.4'
- '396.6'
- '396.96'
- '1201'
- '8925'
security_keys:
- DG RECORD ACCESS
- DG SECURITY OFFICER
- PROVIDER
menu_options: 3
description: Compensation and Pension Record Interchange (CAPRI)Software Version 2.7System Administration and Technical
audience: Technical implementers
keywords: []
page_count: 0
word_count: 28685
section_count: 42
table_count: 5
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: January 2026
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/DVBA_TM.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/DVBA_TM.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=133
audit_applied: '2026-05-31'
master_source: CAPRI System Administration and Technical Guide (Updated DVBA*2.7*255)
master_pub_date: January 2026
consolidated_from: 3 versions
prior_versions:
- CAPRI System Administration and Technical Guide (Updated DVBA*2.7*250)
- CAPRI System Administration and Technical Guide (Updated DVBA*2.7*254)
consolidated_title: capri system administration and technical guide
---

Compensation and Pension Record Interchange (CAPRI)Software Version 2.7System Administration and Technical Guide

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/001.png)

January 2026

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p>Table 1- CAPRI's MUMPS RPCs and GUI RPC Utilization details</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 58%" />
<col style="width: 18%" />
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
<td>01/2026</td>
<td>1.27</td>
<td><p>Updated to reflect changes for patch DVBA*2.7*255 that includes the following:</p>
<ul>
<li><blockquote>
<p>Section <u>2.2</u> Internal Clients- Updated title and information</p>
</blockquote></li>
<li><blockquote>
<p>Created section <u>2.2.3</u> Veteran Service Organization (VSO)</p>
</blockquote></li>
<li><blockquote>
<p>Updated <u>Appendix A</u>. added the following RPCs into the table:</p>
</blockquote></li>
</ul>
<blockquote>
<p><a href="#DVBACAPRIARPOPTSET">DVBA CAPRI ARP OPTSET</a><br />
<a href="#DVBACAPRIARPRSKDT">DVBA CAPRI ARP RSKDT</a><br />
<a href="#DVBACAPRILOOKUPOPTSET">DVBA CAPRI LOOKUP OPTSET</a><br />
<a href="#DVBACAPRINREHISTORY">DVBA CAPRI NRE HISTORY</a><br />
<a href="#DVBACAPRINRELOAD">DVBA CAPRI NRE LOAD</a><br />
<a href="#DVBACAPRINREMARK">DVBA CAPRI NRE MARK</a><br />
<a href="#DVBACAPRINREOPEN">DVBA CAPRI NRE OPEN</a><br />
<a href="#DVBACAPRINRERUNNOW">DVBA CAPRI NRE RUNNOW</a><br />
<a href="#DVBACAPRINRESAVE">DVBA CAPRI NRE SAVE</a><br />
<a href="#DVBACAPRINRESTATIC">DVBA CAPRI NRE STATIC</a><br />
<a href="#DVBACAPRINRESUMMARY">DVBA CAPRI NRE SUMMARY</a><br />
<a href="#DVBACAPRIOPENACCESSCHECK">DVBA CAPRI OPEN ACCESS CHECK</a></p>
<p><a href="#DVBACAPRICMTSIGFLDNUM">DVBA CAPRI CMT SIGFLD NUM</a><br />
<a href="#DVBACAPRISUPPORTMESSAGE">DVBA CAPRI SUPPORT MESSAGE</a></p>
</blockquote>
<ul>
<li><blockquote>
<p>RPCs to Sunset in 10/2025:</p>
</blockquote></li>
</ul>
<blockquote>
<p><a href="\l">DVBAD CONTRACTED EXAM CRYPTO</a></p>
<p><a href="#DVBADCONTRACTEDEXAMREPORTS">DVBAD CONTRACTED EXAM REPORTS</a></p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/2025</td>
<td>1.26</td>
<td><p>Updated to reflect changes for patch DVBA*2.7*254 that includes the following:</p>
<ul>
<li><blockquote>
<p>Updated Section <u>5.1</u> – CAPRI GUI Client Software – Highlighted text for visual</p>
</blockquote></li>
<li><blockquote>
<p>Updated Figure 7 VistA Sign-on – Change Access/Verify code</p>
</blockquote></li>
<li><blockquote>
<p>Updated Section <u>7.1</u> – CAPRI Application Software Maintenance – Fixed grammatical errors</p>
</blockquote></li>
<li><blockquote>
<p>Updated Section <u>7.2</u> – C&amp;P Worksheet Template Maintenance – Fixed grammatical errors</p>
</blockquote></li>
<li><blockquote>
<p>Updated Section <u>9.2</u> – CAPRI Remote Procedure Calls (RPCs) for MUMPS – Corrected format</p>
</blockquote></li>
<li><blockquote>
<p>Updated Section <u>11</u> – Archiving, Purging, and Frequency – Fixed grammatical errors</p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#appendix-a">Appendix A</a>, added RPCs:</p>
</blockquote></li>
</ul>
<blockquote>
<p><a href="\l">DVBA CAPRI CMT IEPD RESET</a></p>
<p><a href="#DVBACAPRICMTSKIPCOND">DVBA CAPRI CMT SKIP COND</a></p>
<p><a href="#DVBACAPRIMEDOPNFIELDS">DVBA CAPRI MED OPN FIELDS</a></p>
<p><a href="\l">DVBA SKIP CHILD RESET</a></p>
<p><a href="#DVBACAPRISKIPPARENTCHILD">DVBA CAPRI SKIP PARENTCHILD</a></p>
<p><a href="#DVBABCAPRIWORDWRAP">DVBA CAPRI WORD WRAP</a></p>
</blockquote>
<ul>
<li><blockquote>
<p>Updated <a href="#appendix-a">Appendix A</a>, updated information in table for the following RPCs:</p>
</blockquote></li>
</ul>
<blockquote>
<p><a href="#DVBACAPRIADDEXAM">DVBA CAPRI ADD EXAM</a></p>
<p><a href="#RANGE!A12">DVBA CAPRI CREATE WORKSHEET</a></p>
<p><a href="#RANGE!A15">DVBA CAPRI DELETE CHECK</a></p>
<p><a href="\l">DVBA CAPRI DELETE EXAM</a></p>
<p><a href="\l">DVBA CAPRI GET DBQ PDF</a></p>
<p><a href="\l">DVBA CAPRI GET EXAM REPORT</a></p>
<p><a href="#DVBACAPRIGETEXAMINERINFO">DVBA CAPRI GET EXAMINER INFO</a></p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><p>Continued updates to reflect changes for patch DVBA*254 that includes the following:</p>
<ul>
<li><blockquote>
<p>Updated <a href="#appendix-a">Appendix A</a>, updated information in table for the following RPCs:</p>
</blockquote></li>
</ul>
<blockquote>
<p><a href="#DVBACAPRIGETWORKSHEET">DVBA CAPRI GET WORKSHEET</a></p>
<p><a href="#RANGE!A37">DVBA CAPRI GET WORKSHEET LIST</a></p>
<p><a href="#DVBACAPRIPARAMINQ">DVBA CAPRI PARAM INQ</a></p>
<p><a href="#RANGE!A50">DVBA CAPRI PARAM UPDATE</a></p>
<p><a href="#DVBACAPRISAVEDBQXML">DVBA CAPRI SAVE DBQ XML</a></p>
<p><a href="#DVBACAPRISAVEEXAMPDF">DVBA CAPRI SAVE EXAM PDF</a></p>
<p><a href="#DVBACAPRISAVEREVIEWDATA">DVBA CAPRI SAVE REVIEW DATA</a></p>
<p><a href="#DVBACAPRITRAINEEDOCMANAGER">DVBA CAPRI TRAINEE DOC MANAGER</a></p>
<p><a href="#DVBACAPRIUNLOCKEXAM">DVBA CAPRI UNLOCK EXAM</a></p>
<p><a href="#DVBACAPRIUPDATEDBQTRANSTAT">DVBA CAPRI UPDATE DBQ TRANSTAT</a></p>
<p><a href="#DVBACAPRIWORKSHEETUPDATE">DVBA CAPRI WORKSHEET UPDATE</a></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>06/2025</td>
<td>1.25</td>
<td><p>Updated to reflect changes for patch DVBA*2.7*253 that includes the following:</p>
<ul>
<li><p>Section <u>1.2</u> – Reference Materials – Updated titles and URLs</p></li>
<li><p>Updated <u>Appendix A</u>, added RPCs:</p></li>
</ul>
<blockquote>
<p><a href="\l">DVBA CAPRI CMT IEPD RESET</a></p>
<p><a href="\l">DVBA CAPRI CMT SKIP COND</a></p>
<p><a href="\l">DVBA CAPRI SKIP CHILD RESET</a></p>
<p><a href="#DVBACAPRISKIPPARENTCHILD">DVBA CAPRI SKIP PARENTCHILD</a></p>
</blockquote>
<ul>
<li><p>Updated <u>Appendix A</u>, modified RPCs:</p></li>
</ul>
<blockquote>
<p><a href="#DVBACAPRIADDEXAM">DVBA CAPRI ADD EXAM</a></p>
<p><a href="#RANGE!A12">DVBA CAPRI CREATE WORKSHEET</a></p>
<p><a href="#RANGE!A15">DVBA CAPRI DELETE CHECK</a></p>
<p><a href="#RANGE!A16">DVBA CAPRI DELETE EXAM</a></p>
<p><a href="#RANGE!A22">DVBA CAPRI GET DBQ PDF</a></p>
<p><a href="#DVBACAPRIGETEXAMREPORT">DVBA CAPRI GET EXAM REPORT</a></p>
<p><a href="#DVBACAPRIGETEXAMINERINFO">DVBA CAPRI GET EXAMINER INFO</a></p>
<p><a href="#DVBACAPRIGETWORKSHEET">DVBA CAPRI GET WORKSHEET</a></p>
<p><a href="#RANGE!A37">DVBA CAPRI GET WORKSHEET LIST</a></p>
<p><a href="#DVBACAPRIPARAMINQ">DVBA CAPRI PARAM INQ</a></p>
<p><a href="#RANGE!A50">DVBA CAPRI PARAM UPDATE</a></p>
<p><a href="#DVBACAPRISAVEEXAMPDF">DVBA CAPRI SAVE EXAM PDF</a></p>
<p><a href="#DVBACAPRISAVEREVIEWDATA">DVBA CAPRI SAVE REVIEW DATA</a></p>
<p><a href="#DVBACAPRITRAINEEDOCMANAGER">DVBA CAPRI TRAINEE DOC MANAGER</a></p>
<p><a href="#DVBACAPRIUPDATEDBQTRANSTAT">DVBA CAPRI UPDATE DBQ TRANSTAT</a></p>
<p><a href="#DVBACAPRIUNLOCKEXAM">DVBA CAPRI UNLOCK EXAM</a></p>
<p><a href="#DVBACAPRIWORKSHEETUPDATE">DVBA CAPRI WORKSHEET UPDATE</a></p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>01/2025</td>
<td>1.24</td>
<td><p>Updated to reflect changes for patch DVBA*2.7*252 that includes the following:</p>
<ul>
<li><p>Section <u>6.7</u> – CAPRI News – Updated image.</p></li>
<li><p>Section <u>6.8</u>– CAPRI Alerts – Updated image.</p></li>
<li><p>Section <u>7.2</u> – C&amp;P Worksheet Template Maintenance – added note on functionality.</p></li>
<li><p>Updated <u>Appendix A</u>, added RPCs and parameter:</p></li>
</ul>
<blockquote>
<p><a href="#DVBACAPRICMTSSNVAR">DVBA CAPRI CMT SSN VAR</a></p>
<p><a href="\l">DVBA CAPRI CMT TOGGLE</a></p>
<p><a href="\l">DVBA CAPRI DBQ TRANS FAIL LIST</a></p>
<p><a href="\l">DVBA CAPRI DELETE CHECK</a></p>
<p><a href="#RANGE!A16">DVBA CAPRI DELETE EXAM</a></p>
<p><a href="#DVBACAPRIDELETEWORKSHEET">DVBA CAPRI DELETE WORKSHEE<span id="DVBACAPRIDELETEWORKSHEET" class="anchor"></span>T</a> <span id="DVBACAPRIEXAMRESTORE" class="anchor"></span></p>
<p><a href="#DVBACAPRIEXAMRESTORE">DVBA CAPRI EXAM RESTORE</a> <span id="DVBACAPRIGETEFOLDERTOKEN" class="anchor"></span></p>
<p><a href="#DVBACAPRIGETEFOLDERTOKEN">DVBA CAPRI GET EFOLDER TOKEN</a> </p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p><span id="DVBACAPRIINVALIDCHARLIST" class="anchor"></span>Continued updates to reflect changes for patch DVBA*252 that includes the following:</p>
<ul>
<li><p>Updated <u>Appendix A</u>, added RPCs and parameter:</p></li>
</ul>
<blockquote>
<p><a href="\l">DVBA CAPRI GET EXAM HISTORY</a> <span id="DVBACAPRIGETEXAMPDF" class="anchor"></span></p>
<p><a href="#DVBACAPRIGETEXAMPDF">DVBA CAPRI GET EXAM PDF</a> <span id="DVBACAPRIGETGITHUBDATA" class="anchor"></span></p>
<p><a href="#DVBACAPRIGETGITHUBDATA">DVBA CAPRI GET GITHUB DATA</a></p>
<p><a href="#DVBACAPRIGETGITHUBDATE">DVBA CAPRI GET GITHUB DATE</a></p>
<p><a href="\l">DVBA CAPRI GET SECID</a></p>
<p><a href="\l">DVBA CAPRI GITHUB LOCATION</a></p>
<p><a href="#DVBACAPRIIEPDDATA">DVBA CAPRI IEPD DATA</a></p>
<p><a href="#DVBACAPRIINVALIDCHARLIST">DVBA CAPRI INVALID CHAR LIST</a></p>
<p><a href="\l">DVBA CAPRI PASCAL CHECK</a></p>
<p><a href="\l">DVBA CAPRI PDF LOGIC TOGGLE</a> </p>
<p><a href="\l">DVBA CAPRI PDF SIG FIELD NAMES</a></p>
<p><a href="\l">DVBA CAPRI PN TOGGLE</a> </p>
<p><a href="\l">DVBA CAPRI SAVE SIGNER</a> <span id="DVBACAPRISECURITYTOGGLE" class="anchor"></span></p>
<p><a href="#DVBACAPRISECURITYTOGGLE">DVBA CAPRI SECURITY TOGGLE</a></p>
<p><a href="#DVBACAPRISTATUSCOUNT">DVBA CAPRI STATUS COUNT</a></p>
<p><a href="#DVBACAPRITEMPDEFLIST">DVBA CAPRI TEMP DEF LIST</a></p>
<p><a href="#DVBACAPRITRAINEESIGNATURE">DVBA CAPRI TRAINEE SIGNATURE</a></p>
<p><a href="#DVBACAPRIUNCOSIGNCOUNT">DVBA CAPRI UNCOSIGN COUNT</a></p>
<p><a href="#DVBACAPRIUNCOSIGNEDINFO">DVBA CAPRI UNCOSIGNED INFO</a></p>
<p><a href="#DVBACAPRIWORKSHEETBYEXAM">DVBA CAPRI WORKSHEET BY EXAM</a></p>
<p><a href="#DVBABTEMPLATEREPORTFULL">DVBAB TEMPLATE REPORT FULL</a></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>11/2023</td>
<td>1.23</td>
<td><p>Updated to reflect changes for patch DVBA*250 that includes the following:</p>
<ul>
<li><p>Updated <u>Appendix A</u>, added RPCS.</p></li>
</ul>
<blockquote>
<p>DVBA CAPRI GET DBQ XML</p>
<p>DVBA CAPRI UPDATE DBQ TRANSTAT</p>
<p>DVBA CAPRI DBQ TRANS FAIL LIST</p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>Cont. updates to reflect changes for patch DVBA*2.7*250 that include the following:</p>
<blockquote>
<p>DVBA CAPRI SAVE DBQ XML</p>
<p>DVBA CAPRI NF DATA</p>
<p>DVBA CAPRI GET EXAM REPORT</p>
</blockquote>
<ul>
<li><p>In Section <u>10.1.4</u> added new file 396.17 CAPRI Templates File</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td>05/2023</td>
<td>1.22</td>
<td><p>Updated to reflect changes for patch DVBA*247 that includes the following:</p>
<ul>
<li><p>Updated <u>Appendix A</u> added RPCs,<br />
DVBA CAPRI SPEC ADD</p></li>
</ul>
<blockquote>
<p>DVBA CAPRI SPEC INACTIVE</p>
<p>DVBA CAPRI SPEC STATUS</p>
<p>DVBA CAPRI WORKSHEET NAME ED</p>
<p>DVBA CAPRI WORKSHEET STATUS</p>
<p>DVBA CAPRI WORKSHEET STAT LIST</p>
</blockquote>
<ul>
<li><p>In Section <u>7.2,</u> removed URL to CAPRI PUSH DBQ Utility User Manual, the file is no longer available on the VDL.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>01/2023</td>
<td>1.21</td>
<td><p>Updated to reflect changes for patch DVBA*243 that includes the following:</p>
<ul>
<li><p>Updated <u>Appendix A</u>, added RPCs:</p></li>
</ul>
<blockquote>
<p>DVBAB CAPRI ALLOW CLINDOCS</p>
<p>DVBAB CAPRI EFOLDER LOCATION</p>
<p>DVBAB CAPRI PROVIDER</p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>11/2022</td>
<td>1.20</td>
<td><p>Updated to reflect changes for patch DVBA*242 that includes the following:</p>
<ul>
<li><p>Updated Section <u>9.1</u> CAPRI Remote Procedure Calls Logger to include new menu option and permission information.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/2022</td>
<td>1.19</td>
<td><p>Updated to reflect changes for patch DVBA*238 that includes the following:</p>
<ul>
<li><p>New section <u>6.10</u>- Paths for Transmitting Clinical Documents to eFolder, transmission error codes and messages.</p></li>
<li><p>Updated Section <u>10.1.4</u> FileMan Access Codes, added FileMan Access code 396.21 CAPRI Clinical eFolder Transmissions File.</p></li>
<li><p>Updated <u>Appendix A</u>, added RPCs:</p></li>
</ul>
<blockquote>
<p>DVBA CAPRI CLINDOC URLS</p>
<p>DVBA CAPRI GET TOGGLES</p>
<p>DVBAB VERSION</p>
<p>DVBA CAPRI SET METRICS</p>
<p>DVBA CAPRI PURGE MET</p>
<p>DVBA CAPRI GET MET RPT</p>
<p>DVBA CAPRI GET EFOLDER TOKEN</p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>02/14/2022</td>
<td>1.18</td>
<td>Updated Sections <u>6.7</u> CAPRI News, <u>13.10</u> DBQ Permanent Failure, <u>13.11</u> DBQ Transmission Errors</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/12/2021</td>
<td>1.17</td>
<td><ul>
<li><blockquote>
<p>Added Section <u>4.3</u> for re-route functionality and adding to mail group for patch 227</p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions, a Booz Allen company</td>
</tr>
<tr class="odd">
<td>05/01/2021</td>
<td>1.16</td>
<td><ul>
<li><blockquote>
<p>Updated for patch 226</p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>10/14/2020</td>
<td>1.15</td>
<td><ul>
<li><blockquote>
<p>Updated Sections <u>5.1</u> and <u>6.1</u> for patch 223</p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>06/22/2020</td>
<td>1.14</td>
<td><ul>
<li><p>Updated for patch 220</p></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>03/02/2020</td>
<td>1.13</td>
<td><ul>
<li><p>Updated for patch 216</p></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>10/3/2019</td>
<td>1.12</td>
<td><ul>
<li><blockquote>
<p>Removed reference to the DVBA C Purge 2507 option from page 26 for patch DVBA*2.7*215</p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>03/29/2019</td>
<td>1.11</td>
<td><ul>
<li><p>Section 12.1, Added CAPRI Remote Procedure Calls Logger section</p></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>02/19/2019</td>
<td>1.10</td>
<td><ul>
<li><p>Updated <strong><u>Appendix A</u></strong>, added a new Remote Procedure Call: DVBA CAPRI GET EDIPI</p></li>
<li><p>Section <strong><u>5.1</u></strong> CAPRI GUI Client Software, revised 193.11 to 209</p></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>05/24/2018</td>
<td>1.9</td>
<td><ul>
<li><p>Updated sections 2.2.2.1. and <strong><u>2.2.4</u></strong> The JLV tab replaced the VistAWeb tab in GUI version DVBA*2.7*193.12, so references to VistAWeb were removed.</p></li>
<li><blockquote>
<p>Updated section 2.2.1.1. Replaced reference to VistAWeb with JLV.</p>
</blockquote></li>
<li><blockquote>
<p>Replace Remedy with ServiceNow</p>
</blockquote></li>
<li><blockquote>
<p>DoD Tab has been disabled, and all references to DoD have been removed from the document.</p>
</blockquote></li>
<li><blockquote>
<p>Removed DataFlow Diagram from Section <mark></mark><strong><u>3</u></strong></p>
</blockquote></li>
<li><blockquote>
<p>Added description for Joint Longitudinal Viewer (JLV) function (Section <strong><u>2.2.4</u></strong>).</p>
</blockquote></li>
<li><blockquote>
<p>Section <strong><u>7.2</u></strong>, updated last paragraph with revisions from 1<sup>st</sup> Review.</p>
</blockquote></li>
<li><blockquote>
<p>Updated formatting for <strong><u>Appendix A</u></strong></p>
</blockquote></li>
<li><blockquote>
<p>Updated Dates to May on title page and in footers.</p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>4/16/2018</td>
<td>1.8</td>
<td>URL to include descriptions for all values. Updated <strong><u>Appendix A,</u></strong> RPC parameter DVBAB GET</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>09/30/2015</td>
<td>1.7</td>
<td>Updated <strong><u>Appendix A</u></strong></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>3/05/2015</td>
<td>1.6</td>
<td>Updated various sections based on stakeholder feedback.</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>2/25/2015</td>
<td>1.5</td>
<td>Updated <strong><u>Appendix A</u></strong></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>12/4/2014</td>
<td>1.4</td>
<td>Updated Section <strong><u>6.8</u></strong> with a new screen shot</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>9/9/2014</td>
<td>1.3</td>
<td>Updated Section 15.2 to only contain VDL link to CAPRI</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>4/9/2014</td>
<td>1.2</td>
<td>Updated CAPRI Distribution File listing</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>3/25/2013</td>
<td>1.1</td>
<td>Updated Sections <strong><u>0</u></strong> and <strong><u>6.4</u></strong> with changing the CLAIMS server FQDN from CLAIMS.FORUM.VA.GOV "to" CLAIMS.MED.VA.GOV on 03/25/2013</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>7/10/2012</td>
<td>1.0</td>
<td>Initial Publication</td>
<td>Liberty IT Solutions</td>
</tr>
</tbody>
</table>

Table 1- CAPRI's MUMPS RPCs and GUI RPC Utilization details

Preface

Purpose of the System Administration and Technical Guide

The System Administration and Technical Guide document describes the handling, functionality, and architecture of the CAPRI product. The guide includes detailed information about the technical architecture and components associated with CAPRI.

Reference Numbering System

This document uses a numbering system to organize its topics into sections and show the reader how these topics relate to each other. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2. A section numbered 2.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third topic of Chapter 2. This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

Table of Contents

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Acronyms](#acronyms)
  - [Reference Materials](#reference-materials)
  - [CAPRI Technical Support](#capri-technical-support)
- [Agency Partners](#agency-partners)
  - [External Clients](#external-clients)
  - [Internal Clients](#internal-clients)
    - [Veteran's Health Administration](#veterans-health-administration)
    - [Veteran's Benefits Administration](#veterans-benefits-administration)
    - [Veteran Service Organization (VSO)](#veteran-service-organization-vso)
    - [Joint Longitudinal Viewer](#joint-longitudinal-viewer)
    - [National Cemetery Administration](#national-cemetery-administration)
    - [VA Office of Inspector General](#va-office-of-inspector-general)
- [Systems Relationship](#systems-relationship)
  - [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
    - [Custodial Agreements](#custodial-agreements)
    - [Subscriber Agreements](#subscriber-agreements)
- [Account Management](#account-management)
  - [Establishing CAPRI Account](#establishing-capri-account)
  - [Installing CAPRI](#installing-capri)
  - [Re-Route Functionality/Adding Member to Mail Group](#re-route-functionalityadding-member-to-mail-group)
- [CAPRI Distribution Files](#capri-distribution-files)
  - [CAPRI GUI Client Software](#capri-gui-client-software)
- [Logging onto CAPRI](#logging-onto-capri)
  - [Desktop Icon Shortcuts Setup](#desktop-icon-shortcuts-setup)
  - [Non-CAPRI Remote Users](#non-capri-remote-users)
  - [Regional Office CAPRI Remote Users](#regional-office-capri-remote-users)
  - [CAPRI Remote Users](#capri-remote-users)
  - [VistA Terminal](#vista-terminal)
  - [Terminal Server Users](#terminal-server-users)
  - [CAPRI News](#capri-news)
  - [CAPRI Alerts](#capri-alerts)
  - [Audit Kept](#audit-kept)
  - [Paths for Transmitting Clinical Documents to eFolder](#paths-for-transmitting-clinical-documents-to-efolder)
- [CAPRI Application Maintenance](#capri-application-maintenance)
  - [CAPRI Application Software Maintenance](#capri-application-software-maintenance)
  - [C&P Worksheet Template Maintenance](#cp-worksheet-template-maintenance)
- [Applications Development Tools and Usage](#applications-development-tools-and-usage)
  - [Code Repository Tool (Version Control)](#code-repository-tool-version-control)
  - [CAPRI Source Files for Delphi](#capri-source-files-for-delphi)
- [Remote Procedure Calls](#remote-procedure-calls)
  - [CAPRI Remote Procedure Calls Logger](#capri-remote-procedure-calls-logger)
  - [CAPRI Remote Procedure Calls (RPCs) for MUMPS](#capri-remote-procedure-calls-rpcs-for-mumps)
- [FileMan](#fileman)
  - [Installation Procedures and Usage](#installation-procedures-and-usage)
    - [Environmental Setup](#environmental-setup)
    - [Installation Guide](#installation-guide)
    - [Getting Started](#getting-started)
    - [FileMan Access Codes](#fileman-access-codes)
    - [Advanced User](#advanced-user)
    - [Programmer Manual](#programmer-manual)
    - [Package-wide Variables](#package-wide-variables)
    - [Technical Manual](#technical-manual)
- [Archiving, Purging, and Frequency](#archiving-purging-and-frequency)
- [Security](#security)
  - [Security Management](#security-management)
  - [General Security](#general-security)
    - [Remote Systems](#remote-systems)
    - [Contingency Planning](#contingency-planning)
    - [Interfacing](#interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [Security Keys](#security-keys)
- [CAPRI Troubleshooting and Error Information](#capri-troubleshooting-and-error-information)
  - [CAPRI Not Installed in VistA](#capri-not-installed-in-vista)
  - [CAPRI GUI Option Not Assigned to User in VistA](#capri-gui-option-not-assigned-to-user-in-vista)
  - [VistA Server Down](#vista-server-down)
  - [VistA Limits Ability to See Patient Records](#vista-limits-ability-to-see-patient-records)
  - [Network Problems](#network-problems)
  - [Institution File in VistA has Been Locally Modified](#institution-file-in-vista-has-been-locally-modified)
  - [Too Many Invalid Attempts at Access Code / Verify Code](#too-many-invalid-attempts-at-access-code-verify-code)
  - [Multiple Sign-Ons](#multiple-sign-ons)
  - [General Error Message](#general-error-message)
  - [Permanent Failure DBQ Transmission Error Message](#permanent-failure-dbq-transmission-error-message)
  - [Transmission Error DBQ Error Message](#transmission-error-dbq-error-message)
- [Appendix A](#appendix-a)
  - [CAPRI Remote Procedure Calls for MUMPS](#capri-remote-procedure-calls-for-mumps)
The Compensation and Pension Record Interchange (CAPRI) project is an information technology initiative to improve service to disabled veterans by promoting efficient communication between the Veterans Health Administration (VHA) and Veterans Benefits Administration (VBA). Online access to medical data enhances the timeliness of the benefits determination. Previous attempts to automate this process were hindered by the "roll and scroll" nature of the VHA computer interface of the Automated Medical Information Exchange (AMIE) II. The CAPRI software acts as a bridge between the VBA and VHA information systems. It offers VBA Rating Veteran Service Representatives and Decision Review Officers help in building the rating decision documentation through online access to medical data. It also offers VHA Compensation and Pension (C&P) staff an easy, standardized way of recording C&P Examination reports.
CAPRI provides VBA employees with a standardized, user-friendly method to rapidly access veterans' electronic medical records throughout the Department of Veterans Affairs (VA). CAPRI delivers leading edge "point and click" technology to the users' desktops. In addition, the learning curve for CAPRI is significantly less than that for character-based systems. CAPRI builds upon existing VHA information security approaches. In addition to using established mechanisms to ensure only authorized access to medical data, CAPRI adds a level of security by allowing VBA users to read but not alter electronic medical record information. CAPRI also provides innovative improvements for medical centers by integrating highly detailed (C&P) Rating examination results into the veterans' medical records. Previously, these reports were not retained online in medical center computer systems but were archived onto paper. This procedure precluded the sharing of clinically useful data.
Initially developed specifically for VBA, the utility of CAPRI has been expanded to other user groups that include VHA, Office of the Medical Inspector, Office of Information (OI), Research, and Veteran Service Officers. Recently, most of the newest features of CAPRI are specifically targeted at adding features to be used by VHA C&P providers and staff.
*Note: This document has extensive use of URLs to enable the user access to the best, current, and specific information available.*

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term      | Definition                                                                                                                     |
|-----------|--------------------------------------------------------------------------------------------------------------------------------|
| A&A       | Advisory & Assistance                                                                                                          |
| AHLTA     | Armed Forces Health Longitudinal Technology Application (formerly CHCS II, US DoD military health system)                      |
| AMIE      | Automated Medical Information Exchange                                                                                         |
| AWIV      | Advanced Web Image Viewer                                                                                                      |
| C&P       | Compensation and Pension                                                                                                       |
| CAPRI     | Compensation and Pension Record Interchange                                                                                    |
| CPRS      | Computerized Patient Record System                                                                                             |
| CPWM      | Compensation and Pension Worksheet Module                                                                                      |
| DBQ       | Disability Benefits Questionnaire                                                                                              |
| DoD       | Department of Defense                                                                                                          |
| DVBA      | The pre-fix for AUTOMATED MED INFO EXCHANGE (namespace). VBA's interface into VistA.                                           |
| EHR       | Electronic Health Record                                                                                                       |
| FHIE      | Federal Health Information Exchange                                                                                            |
| GUI       | Graphical User Interface                                                                                                       |
| HTML      | HyperText Markup Language                                                                                                      |
| IDE       | Interactive Development Environment                                                                                            |
| IAs       | Integration Agreements                                                                                                         |
| IRM       | Information Resources Management                                                                                               |
| IS        | Information Systems                                                                                                            |
| IT        | Information Technology                                                                                                         |
| MAS       | Medical Administration Service                                                                                                 |
| MUMPS / M | [Massachusetts General Hospital](http://en.wikipedia.org/wiki/Massachusetts_General_Hospital) Utility Multi-Programming System |
| NCIO      | Network Chief Information Officer                                                                                              |
| NPM       | National Patch Module                                                                                                          |
| OI        | Office of Information                                                                                                          |
| OIT       | Office of Information Technology                                                                                               |
| RDV       | Remote Data View                                                                                                               |
| RO        | Regional Office                                                                                                                |
| RPC       | Remote Procedure Call                                                                                                          |
| TIU       | Text Integration Utilities                                                                                                     |
| URL       | Universal Resource Locator (Internet Shortcut – file name extension)                                                           |
| VA        | Department of Veterans Affairs                                                                                                 |
| VAMC      | VA Medical Center                                                                                                              |
| VBA       | Veteran's Benefits Administration                                                                                              |
| VDL       | VA (Software) Document Library                                                                                                 |
| VHA       | Veteran's Health Administration                                                                                                |
| VISN      | Veterans Integrated Service Network                                                                                            |
| VistA     | Veteran's Health Information Systems and Technology Architecture                                                               |

## Reference Materials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains all referenced materials related to this document.

- Medical Disability Examination Office - Policy and Program Management - CAPRI
  - <https://vbaw.vba.va.gov/bl/21/MDEO/capri.htm>
- VA Software Document Library <http://www.va.gov/vdl/>
  - Application- Compensation and Pension Record Exchange: <http://www.va.gov/vdl/application.asp?appid=133>
  - Application: Automated Medical Information Exchange (AMIE) (DVBA) <http://www.va.gov/vdl/application.asp?appid=31>
  - Application FileMan (DI) <http://www.va.gov/vdl/application.asp?appid=5>
  - Application: VistALink (XOBV) <http://www.va.gov/vdl/application.asp?appid=163>

*DISCLAIMER: The appearance of external hyperlink references in the manual does not constitute endorsement by the VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and consistent with the stated purpose of the VA.*

## CAPRI Technical Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following link provides CAPRI specific information regarding obtaining CAPRI access, CAPRI Training, Advanced Web Image Viewer (AWIV) Desk Reference, CAPRI/Virtual VA interactions, and other useful information at: [VA Software Document Library: Compensation and Pension Record Interchange (CAPRI)](https://www.va.gov/vdl/application.asp?appid=133)

User support questions should be addressed to local IT support staff, Information Resources Management (IRM), or one of the National Service Desks. A ServiceNow ticket may be submitted for CAPRI related issues to the National Service Desk at 1-855-673-4357.

# Agency Partners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Clients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA users include external reviewers and researchers obtaining information from various VA administrations for their specific authorized purposes.

## Internal Clients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CAPRI is a VHA developed application. The other two administrations within the VA, VBA and the National Cemetery Administration, use CAPRI directly and/or indirectly.

### Veteran's Health Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following link (URL) provides a complete list of VHA Medical Centers, Outpatient Clinics, Community Based Outpatient Clinics, Vet Centers, and Veterans Integrated Service Network (VISN) locations where the VHA utilizes the CAPRI system.

<https://www.benefits.va.gov/benefits/>

The level of access granted to users will depend on job function, need to know, and the level of security placed on certain sensitive patient records.

#### VHA Data Portal

This VHA program coordinates access to many of VHA's health information resources that include national databases, EHRs, extracted datasets, and medical record data found in CPRS through CAPRI and Joint Longitudinal Viewer (JLV).

### Veteran's Benefits Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the VBA regional office (RO) locations with each of their VBA system name.

*Note: VBA IT continues to use the VA Office of Information Technology (OIT) naming convention method prior to its reorganization. This naming convention is organizational versus geographical in nature. This table reflects that as all VBA IT locations fall under Region 5. VHA IT currently uses the VA OIT current geographical naming convention. Additionally, VBA from a Business Line perspective doesn't use Region 5 but breaks Region 5 down into three separate NCIOs. (See map following this table).*

| VBA Region 5             |                                                                       |
|------------------------------|-----------------------------------------------------------------------|
| REGIONAL OFFICE LOCATION | SYSTEM_NAME                                                       |
| ST. PETERSBURG REGION    |                                                                       |
| Atlanta, GA                  | REGION 5 \> VBA \> St Petersburg Region \> VARO Atlanta \> LAN        |
| Baltimore, MD                | REGION 5 \> VBA \> St Petersburg Region \> VARO Baltimore \> LAN      |
| Columbia, SC                 | REGION 5 \> VBA \> St Petersburg Region \> VARO Columbia \> LAN       |
| Huntington, WV               | REGION 5 \> VBA \> St Petersburg Region \> VARO Huntington \> LAN     |
| Jackson, MS                  | REGION 5 \> VBA \> St Petersburg Region \> VARO Jackson \> LAN        |
| Little Rock, AR              | REGION 5 \> VBA \> St Petersburg Region \> VARO Little Rock \> LAN    |
| Louisville, KY               | REGION 5 \> VBA \> St Petersburg Region \> VARO Louisville \> LAN     |
| Montgomery, AL               | REGION 5 \> VBA \> St Petersburg Region \> VARO Montgomery \> LAN     |
| Nashville, TN                | REGION 5 \> VBA \> St Petersburg Region \> VARO Nashville \> LAN      |
| New Orleans, LA              | REGION 5 \> VBA \> St Petersburg Region \> VARO New Orleans \> LAN    |
| Newark, NJ                   | REGION 5 \> VBA \> St Petersburg Region \> VARO Newark \> LAN         |
| Roanoke, VA                  | REGION 5 \> VBA \> St Petersburg Region \> VARO Roanoke \> LAN        |
| St. Louis, MO                | REGION 5 \> VBA \> St Petersburg Region \> VARO St. Louis \> LAN      |
| St. Louis RMC, MO            | REGION 5 \> VBA \> St Petersburg Region \> VARO St. Louis RMC \> LAN  |
| St. Petersburg, FL           | REGION 5 \> VBA \> St Petersburg Region \> VARO St. Petersburg \> LAN |
| Washington, DC               | REGION 5 \> VBA \> St Petersburg Region \> VARO Washington \> LAN     |
| Winston-Salem, NC            | REGION 5 \> VBA \> St Petersburg Region \> VARO Winston-Salem \> LAN  |
| St. Paul Region          |                                                                       |
| Boston, MA                   | REGION 5 \> VBA \> St Paul Region \> VARO Boston \> LAN               |
| Buffalo, NY                  | REGION 5 \> VBA \> St Paul Region \> VARO Buffalo \> LAN              |
| Chicago, IL                  | REGION 5 \> VBA \> St Paul Region \> VARO Chicago \> LAN              |
| Cleveland, OH                | REGION 5 \> VBA \> St Paul Region \> VARO Cleveland \> LAN            |
| Des Moines, IA               | REGION 5 \> VBA \> St Paul Region \> VARO Des Moines \> LAN           |
| Detroit, MI                  | REGION 5 \> VBA \> St Paul Region \> VARO Detroit \> LAN              |
| Fargo, ND                    | REGION 5 \> VBA \> St Paul Region \> VARO Fargo \> LAN                |
| Hartford, CT                 | REGION 5 \> VBA \> St Paul Region \> VARO Hartford \> LAN             |
| Indianapolis, IN             | REGION 5 \> VBA \> St Paul Region \> VARO Indianapolis \> LAN         |
| Lincoln, NE                  | REGION 5 \> VBA \> St Paul Region \> VARO Lincoln \> LAN              |
| Manchester, NH               | REGION 5 \> VBA \> St Paul Region \> VARO Manchester \> LAN           |
| Milwaukee, WI                | REGION 5 \> VBA \> St Paul Region \> VARO Milwaukee \> LAN            |
| New York, NY                 | REGION 5 \> VBA \> St Paul Region \> VARO New York \> LAN             |
| Philadelphia, PA             | REGION 5 \> VBA \> St Paul Region \> VARO Philadelphia \> LAN         |
| Pittsburgh, PA               | REGION 5 \> VBA \> St Paul Region \> VARO Pittsburgh \> LAN           |
| Providence, RI               | REGION 5 \> VBA \> St Paul Region \> VARO Providence \> LAN           |
| Sioux Falls, SD              | REGION 5 \> VBA \> St Paul Region \> VARO Sioux Falls \> LAN          |
| St. Paul, MN                 | REGION 5 \> VBA \> St Paul Region \> VARO St. Paul \> LAN             |
| Togus, ME                    | REGION 5 \> VBA \> St Paul Region \> VARO Togus \> LAN                |
| White River Jct, VT          | REGION 5 \> VBA \> St Paul Region \> VARO White River Jct. \> LAN     |
| Wichita, KS                  | REGION 5 \> VBA \> St Paul Region \> VARO Wichita \> LAN              |
| Wilmington, DE               | REGION 5 \> VBA \> St Paul Region \> VARO Wilmington \> LAN           |
| SAN DIEGO REGION         |                                                                       |
| Albuquerque, NM              | REGION 5 \> VBA \> San Diego Region \> VARO Albuquerque \> LAN        |
| Anchorage, AK                | REGION 5 \> VBA \> San Diego Region \> VARO Anchorage \> LAN          |
| Boise, ID                    | REGION 5 \> VBA \> San Diego Region \> VARO Boise \> LAN              |
| Denver, CO                   | REGION 5 \> VBA \> San Diego Region \> VARO Denver \> LAN             |
| Cheyenne, WO                 | REGION 5 \> VBA \> San Diego Region \> VARO Cheyenne \> LAN           |
| Fort Harrison, MT            | REGION 5 \> VBA \> San Diego Region \> VARO Fort Harrison \> LAN      |
| Honolulu, HI                 | REGION 5 \> VBA \> San Diego Region \> VARO Honolulu \> LAN           |
| Houston, TX                  | REGION 5 \> VBA \> San Diego Region \> VARO Houston \> LAN            |
| Los Angeles, CA              | REGION 5 \> VBA \> San Diego Region \> VARO Los Angeles \> LAN        |
| Manila, PI                   | REGION 5 \> VBA \> San Diego Region \> VARO Manila \> LAN             |
| Muskogee, OK                 | REGION 5 \> VBA \> San Diego Region \> VARO Muskogee \> LAN           |
| Oakland, CA                  | REGION 5 \> VBA \> San Diego Region \> VARO Oakland \> LAN            |
| Phoenix, AZ                  | REGION 5 \> VBA \> San Diego Region \> VARO Phoenix \> LAN            |
| Portland, OR                 | REGION 5 \> VBA \> San Diego Region \> VARO Portland \> LAN           |
| Reno, NV                     | REGION 5 \> VBA \> San Diego Region \> VARO Reno \> LAN               |
| Salt Lake City, UT           | REGION 5 \> VBA \> San Diego Region \> VARO Salt Lake City \> LAN     |
| San Diego, CA                | REGION 5 \> VBA \> San Diego Region \> VARO San Diego \> LAN          |
| San Juan, PR                 | REGION 5 \> VBA \> San Diego Region \> VARO San Juan \> LAN           |
| Seattle, WA                  | REGION 5 \> VBA \> San Diego Region \> VARO Seattle \> LAN            |
| Waco, TX                     | REGION 5 \> VBA \> San Diego Region \> VARO Waco \> LAN               |

This is the VBA's Region 5 Business Line perspective Network map of CIOs:

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/002.png)

<span id="_Toc514706685" class="anchor"></span>Figure 1-1 VBA's Region 5 Business Line perspective Network map of CIOs

### Veteran Service Organization (VSO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VSO offices are co-located with VBA regional offices as shown in the table of the previous Section 2.2.2. The VSO has authorized CAPRI read-only permissions for specific claimant's EHR. This access allows the VSO to help a veteran who is preparing a VA benefit claim.

CAPRI offers VSO users:

- A national user account option with a single access/verify code, from which authorized users can view a Veteran's entire VA health record from any site where the Veteran has been seen
- Customizable reports and health summaries
- C&P exam requests and results
- A search feature that enables users to search for progress notes and discharge summaries for text
- Access to current and past AMIE C&P claims activity
- Access to Joint Longitudinal Viewer (JLV) for integrated read-only view of health data

### Joint Longitudinal Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The JLV provides an integrated read-only view of health data from all VA and VA community partner sites where the Veteran or Service member has received care.

### National Cemetery Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Cemetery Administration does not directly use the CAPRI application but receives its verified veteran information through VBA. VBA uses CAPRI to acquire this veteran information.

### VA Office of Inspector General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Office of Inspector General performs audits and conducts research for reports when directed using CAPRI accessed data.

# Systems Relationship

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a large amount of data as well as continual changes within the DBIAs. Therefore, it is recommended to follow these steps to obtain the most current and valid DBIAs for the CAPRI/AMIE package.

### Custodial Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A list of CAPRI/AMIE current custodial Integration Agreements (IAs) can be created by FORUM users with DBA Menu access by following these steps:

1\. Log on to FORUM

2\. DBA Menu

3\. Integration Control Registrations Menu

4\. Custodial Package Menu

5\. Active ICRs by Custodial Package Option

6\. Select Package Name: AMIE

### Subscriber Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A list of CAPRI/AMIE current subscriber IAs can be created by FORUM users with DBA Menu access by following these steps:

> 1\. Log on to FORUM

> 2\. DBA Menu

> 3\. Integration Control Registrations Menu

> 4\. Subscriber Package Menu

> 5\. Print Active by Subscriber Package Option

> 6\. Start with subscribing package: AUTOMATED MED INFO A

> 7\. Go to subscribing package: AUTOMATED MED INFO Z

# Account Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Establishing CAPRI Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CAPRI access for local VHA medical center users is managed by the local IRM/ISO staff at the medical center, just like any other application (i.e. roll-and-scroll VistA, CPRS, BCMA, etc.). HIA only manages CAPRI users that authenticate/authorize through the CLAIMS system.

Once you obtain access and depending on your role you will be able to create additional accounts using CAPRI tools. Refer to the latest version of the <u>CAPRI GUI User Manual</u> in the VA (Software) Document Library (VDL); see section "Edit Remote User Site Access" at the following URL:

<https://www.va.gov/vdl/application.asp?appid=133>

## Installing CAPRI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note: It is important that all users at your site remain on the same version.*

The AMIE package must be installed and maintained at VistA sites with patient data that will be accessed through the CAPRI GUI application. Installation and configuration of the AMIE package is described in the AMIE Installation Guide, Technical Manual, and Release Notes found at: <http://www.va.gov/vdl/application.asp?appid=31>

The AMIE package is maintained through patches in the Department of Veterans Benefits Administration (DVBA) namespace, issued through the VistA National Patch Module (NPM).

For the VBA, the new version runs when the user starts the application from Start/All Programs/VBAPPS/CAPRIREMOTE. The user can make new Windows desktop shortcuts (see Section 7.1) after starting the new version.

For the VHA, the IRM department will install the CAPRI desktop icon. Please check with them on the specifics of starting CAPRI. Normally, the user should find the CAPRI shortcut in the same place the user would find the Computerized Patient Record System (CPRS).

Local VistA Connection: The CAPRI shortcut can be set to connect to a specific VistA system. CAPRI will accept the command line parameters s=servername and p=portname, just like CPRS.

CAPRI REMOTE: CAPRI Remote users access CAPRI through the Claims system, which runs on the VHA Forum hardware. The server for those users should be set to CLAIMS.MED.VA.GOV, port 9400. For more details reference the latest version of the <u>CAPRI GUI User Manual,</u> see section "CAPRI Remote Functionality" at the following URL: <http://www.va.gov/vdl/application.asp?appid=133>

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/003.png)

<span id="_Ref200017770" class="anchor"></span>Figure 2 Test Claims Properties

## Re-Route Functionality/Adding Member to Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Those at the site who require access to the re-route capabilities in CAPRI will need to manually be added to the DVBA C 2507 REROUTE MAIL GROUP in order to successfully utilize the re-route functionality added in patch DVBA\*2.7\*227. Only Mail Group Coordinators can add people to the mail group, this mail group does not allow self-enrollment. To add someone to the mail group, please follow the instructions below.

Step 1 – Select the following MAIL GROUP NAME: DVBA C 2507 REROUTEStep 2 – Select the member you wish to add to the mail group. A prompt will ask if you are selecting said member as a new member. Type Yes.

Step 3 – Select the TYPE. User may select appropriate response.

# CAPRI Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CAPRI GUI Client Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation can be found on the VA Software Documentation Library at: <https://www.va.gov/vdl/>.

The following files will be available:

> <u>Required Distribution Files to Run the CAPRI Application</u>

> <u>File Name</u> <u>Contents</u> <u>Retrieval format</u>

| DVBA\_##\_P###\_##.ZIP | File(s) indented below | BINARY |
|------------------------|------------------------|--------|

Within the release patch zip file, the following contents are included:

| CAPRI.exe                  | CAPRI v### executable                     |
|----------------------------|-------------------------------------------|
| CAPRI.map                  | CAPRI error map                           |
| CAPRI_Help.chm             | CAPRI On-line Help                        |
| CAPRISession.rdox          | MicroFocus Reflection session             |
| CapriTerminalEmulators.ini | Configuration                             |
| DelZip192.dll              | Delphi Zip file support                   |
| DelZip192x64.dll           | Delphi Zip file support                   |
| libeay32.dll               | VLER /DAS dynamically linked library      |
| libgcc_s_dw2-1.dll         | Support PDF compression and Linearization |
| libstdc++-6.dll            | Support PDF compression and Linearization |
| qpdf.exe                   | Support PDF compression and Linearization |
| qpdf13.dll                 | Support PDF compression and Linearization |
| ssh_config                 | Secure Shell configuration                |
| Ssleay32.dll               | VLER /DAS dynamically linked library      |
| Tutil32.dll                | Windows O/S support files                 |
| UnzDll.dll                 | Delphi Unzip support files                |
| VACAPRIVVA.dll             | Virtual VA dynamically linked library     |

> <u>Optional Distribution Files Which Contain Important User Info</u>

> \- CAPRI_GUI_ISG.doc CAPRI GUI Installation Supplemental Guide

> <span class="mark">DVBA\_\_##\_P###\_RN.PDF Patch Release Notes BINARY</span>

> DVBA\_\_##\_P###\_UM.PDF Updated CAPRI User Manual BINARY

> CAPRI_SYSTEMADMINTECHGUIDE_DVBA_27_TM.PDF SAT GUIDE BINARY

*Note: The VDL web site is usually updated within 1-3 days of the release date and will contain the "Release Notes" and <u>if</u> updated the "CAPRI GUI User Manual" as shown in the highlighted text above. The VDL's URL is:* <http://www.va.gov/vdl/application.asp?appid=133>

# Logging onto CAPRI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information is this section is a combination from several different sources but most of the information can be found in the latest version of the <u>CAPRI GUI User Manual,</u> see section "Logging On" at the following URL: <http://www.va.gov/vdl/application.asp?appid=133>

Please check this main source, the latest version of the <u>CAPRI GUI User Manual,</u> for any updated information that may not be found here.

## Desktop Icon Shortcuts Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note: It is important that all users at your site remain on the same version. Additionally, there is no required fixed location for the CAPRI executable. The location is at the discretion of each installing facility. CAPRI is routinely installed in the Program Files/VistA/CAPRI directory of a user's workstation. Many sites install the GUI on a network share drive and place a shortcut on the user's workstations. Other sites install the GUI on a Citrix server for remote access.*

IT will install the CAPRI desktop icon. Please check with them on the specifics of starting CAPRI. Normally, the user should find the CAPRI shortcut in the same place the user would find the CPRS.

Local Vista Connection: The CAPRI shortcut can be set to connect to a specific VistA system. CAPRI will accept the command line parameters s=servername and p=portname, just like CPRS. See the "Additional Information" section; subsection "Installation," in the latest version of the <u>CAPRI GUI User Manual,</u> at the following URL: <http://www.va.gov/vdl/application.asp?appid=133>

## Non-CAPRI Remote Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1 – The user starts by double-clicking the CAPRI icon.

Step 2 – OPTIONAL – If the workstation has been configured with serverlist.exe by IRM, and if there is no server and port information in the CAPRI shortcut, a window will appear asking the user to select an initial server and port (see following screenshot). Selecting the down arrow in the upper right corner displays all the VHA sites the user can access. A scroll bar appears if the list is too long to be displayed. If the user has access to only one VHA facility, then the VistA sign on screen in Step 5 is displayed immediately.

Step 3 – OPTIONAL – The user scrolls to the name of the desired VHA facility, if it is not already visible, and clicks it to select it.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/004.png)

<span id="_Toc106050276" class="anchor"></span>Figure 3 Connect to Window

Step 4 – OPTIONAL – The user clicks <u>O</u>K

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/005.png)

<span id="_Toc106050277" class="anchor"></span>Figure 4 Connect to Window Selection

Step 5 – The user enters a VistA Access Code, presses the Tab key, and then enters the Verify Code. The user then presses Enter or clicks <u>O</u>K. This takes the user to the Patient Selector Screen.

> **NOTE:** New users without access codes should contact local IRM staff to get one.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/006.png)

<span id="_Ref200018198" class="anchor"></span>Figure 5 VistA Sign-on

## Regional Office CAPRI Remote Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most VBA users are CAPRI Remote users. Each CAPRI Remote user needs only one Access Code and one Verify Code to connect to authorized VA Medical Center (VAMC) sites.

Step 1 – From the Start/VBAPPS/CAPRI Remote/CAPRI Remote menu, the user clicks the CAPRI icon.

Step 2 –After entering the VistA Access Code, the user presses the Tab key to go to the next field and enters the Verify Code. Then the user presses Enter or clicks <u>O</u>K*Note: New users without access codes should contact local IRM staff to get one. The first time the user logs into a VistA application, only the Access Code should be entered. CAPRI will then prompt the user to create a Verify Code. Most users should have a valid Access and Verify Code combination by the time they use CAPRI.*

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/007.png)

<span id="_Toc106050279" class="anchor"></span>Figure 6 VistA Sign-on Enter Access/Verify

OPTIONAL – To change the Verify Code, the user selects the Change Verify Code checkbox on the sign-on dialog before clicking <u>O</u>K. The user will then be prompted to create a new Verify Code as shown in the steps in the following screenshot.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/008.png)

<span id="_Ref203378431" class="anchor"></span>Figure 7 VistA Sign-on – Change Access/Verify code

After selecting <u>O</u>K, the user is prompted to enter and confirm a New Verify Code

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/009.png)

<span id="_Toc106050281" class="anchor"></span>Figure 8 Change Verify Code

Step 3 – The CAPRI Remote site selection screen displays the user's authorized VHA facilities. (These accesses are established when an account is initially created and/or the user request specific facilities along with the proper approvals after the account creation. This facility information is located in the CAPRI file 396.96.) When the user selects a CAPRI Remote site executable it provides the authorized remote sites. If shown, the vertical scrollbar is used to scroll through all authorized sites. The user selects a site and then either double-clicks the site's name or clicks <u>O</u>K to access that site. CAPRI has been modified to include the city and state where each facility is located. In addition, the list may now be sorted by State. The following screenshot shows DEV/FEX Test System in Troy, New York as the selected VHA facility.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/010.png)

<span id="_Toc106050282" class="anchor"></span>Figure 9 CAPRI Remote Site Selection Screen

After CAPRI loads the VHA facility, the user is prompted with the Patient Selector screen. Instructions for use of the Patient Selector screen are found in section "[CAPRI – Using the Software](#_CAPRI_–_Use)" of the latest version of the <u>CAPRI GUI User Manual</u> at the following URL: <http://www.va.gov/vdl/application.asp?appid=133>

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/011.png)

<span id="_Toc106050283" class="anchor"></span>Figure 10 Patient Selector Screen

## CAPRI Remote Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CAPRI Remote users access CAPRI through the Claims system, which runs on the VHA Forum hardware. The server for those users should be set to (see screenshot below).

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/012.png)

<span id="_Toc106050284" class="anchor"></span>Figure 11 Test Claims Properties

CAPRI Remote users outside of VBA will normally obtain an access code from the Office of Information (OI) support staff, not from the local field site. Most VBA users are CAPRI Remote users. Most VHA users are local site users. If a user starts CAPRI and does not successfully connect to a VistA system within 90 seconds, CAPRI automatically shuts down.

When users log into CAPRI remotely, CAPRI alerts users when no email account is set up.

For additional information see the [CAPRI Remote Functionality](#_CAPRI_Remote_Functionality) section in the CAPRI GUI User Manual at the following URL: <http://www.va.gov/vdl/application.asp?appid=133>

## VistA Terminal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "Attachmate Reflections Secure Shell" application replaces the telnet window. CAPRI Remote users can launch a VistA Terminal session by selecting the VistA button to log into the local VistA system site they are assigned to. A dialog box is displayed when the VistA button is clicked that provides the user with the ability to choose between connecting using the secure shell application or telnet. The default is set to secure shell application.

> **NOTE:** Local CAPRI users will not have access to the VistA Terminal from CAPRI and the VistA button will not be available.

## Terminal Server Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1 – From the Hines terminal server application, the user double-clicks the CAPRI icon.

Step 2 – Follow the instructions in the previous Section [7.3](#regional-office-capri-remote-users), Regional Office CAPRI Remote Users, Steps 2 and 3.

## CAPRI News

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SharePoint initialization process has been removed from CAPRI. Functionality is now a Launch News dialog that pulls the SharePoint URL form VistA provides this URL to the user and has a button which can launch the SharePoint in an external browser. To access this functionality, select the Tools menu, then select "News…".

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/013.png)

<span id="_Toc106050285" class="anchor"></span>Figure 12 CAPRI News

## CAPRI Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When users of the CAPRI C&P Template functionality log into CAPRI, any existing CAPRI Template Alerts are displayed.

CAPRI automatically checks pending Compensation and Pension Worksheet Module (CPWM) Template statuses. Pending templates in the user's queue are displayed on the alert screen. The C&P Alert screen displays alerts according to template status. Alerts for template statuses are draft, awaiting signature, sent back from reviewer, requiring review, and documents to co-sign.

The user clicks the Resolve This Alert button to be taken to the section of CAPRI where the alert can be resolved. For example, if the user has unsigned templates, then he or she is taken to the Unsigned Templates window. The user may select Continue to bypass the alerts and go to the Patient Selector screen.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/014.png)

<span id="_Toc106050286" class="anchor"></span>Figure 13 CAPRI Alerts

## Audit Kept

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions are to view your audit log. This is an example only, use your correct information to locate your log.

Example: The log file is named - DVBA_2.7_BuildVersion_dd_mm_yy.TXT

Go to: C:\Documents and Settings\YourVAUserName\Local Settings\Temp\DVBA_2.7\_ BuildVersion_dd_mm_yy.txt

## Paths for Transmitting Clinical Documents to eFolder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram provides the current paths for transmitting clinical documents from CAPRI sent to eFolder using either PIV or Proxy for transmissions. The table below provides a list of error codes and messages when transmission to eFolder fails.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/015.png)

<span id="_Toc106050287" class="anchor"></span>Figure 14 Paths for Transmitting Clinical Docs to eFolder and Errors

The table below provides error codes and messages the end user may receive during a failed eFolder transmission.

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error</strong>:<br />
(Place on Figure 14 Paths for Transmitting Clinical Docs to eFolder and Errors where error occurs)</th>
<th><strong>Error Message</strong>:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>200 Success</td>
<td>Clinical Document(s) were successfully transmitted to the VBA eFolder.<br />
Document ID: ####</td>
</tr>
<tr class="even">
<td>400 Bad Request</td>
<td>Transmissions to VBA eFolder failed. Error code: ###<br />
Bad Request.<br />
Please contact your local IT or enter a service ticket.</td>
</tr>
<tr class="odd">
<td>400 MTLS error</td>
<td>Transmissions to VBA eFolder failed. Error code: ###<br />
 Unauthorized User.<br />
 Please contact your local IT or enter a service ticket.</td>
</tr>
<tr class="even">
<td>401 Unauthorized User</td>
<td>Transmissions to VBA eFolder failed. Error code: ###<br />
Unauthorized User.<br />
Please contact your local IT or enter a service ticket.</td>
</tr>
<tr class="odd">
<td>403 File number error</td>
<td>Transmissions to VBA eFolder failed. Error code: ###<br />
Veteran file number did not resolve.<br />
Please contact your local IT or enter a service ticket.</td>
</tr>
<tr class="even">
<td>500 Series Server Error</td>
<td>Transmissions to VBA eFolder failed. Error code: ###<br />
Please try again later.</td>
</tr>
<tr class="odd">
<td>900 Transmission Disabled</td>
<td>Transmission of Clinical Document(s) has been disabled for your site.</td>
</tr>
<tr class="even">
<td>901 Time Out</td>
<td>Transmission of Clinical Document timed out</td>
</tr>
<tr class="odd">
<td>Default</td>
<td>Transmissions to VBA eFolder failed. Error code: ###<br />
Please contact your local IT or enter a service ticket.</td>
</tr>
</tbody>
</table>

# CAPRI Application Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CAPRI Application Software Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Patch Module currently resides on the FORUM server and is used to release VistA patches nationally.

Updates to the CAPRI application are distributed through the VA FORUM National Patch Module (NPM) under the DVBA namespace. The DVBA namespace is shared with the Automated Medical Information Exchange (AMIE) package. Patch names follow the format "DVBA\*Version\*PatchNumber."

The patch consists of the patch description, routines, and VistA FileMan components in PackMan format for installation on the VistA server. The patch description consists of an overview description of the patch, a functional overview, a list of the components released by the patch, retrieval instructions for the software and documentation, and installation instructions for the VistA server portion of the patch.

CAPRI executable and documentation associated with the patch are retrieved from an FTP server designated by the VA for software downloads. The software retrieval instructions are always added by the developer in the SOFTWARE AND DOCUMENTATION RETRIEVAL section of the patch description. A separate installation guide is provided with each CAPRI patch that provides instructions for installing the CAPRI GUI. New versions of the CAPRI GUI do not require installation of previous versions.

The Associated Patches section of the Patch Description lists any previous patches that must be installed prior to the new patch. The Functional Overview section of the patch describes the functional and technical changes included in the patch. The Installation Requirements section provides detailed instructions on the installation of all patch components.

When a CAPRI patch includes new GUI, the Software and Documentation Retrieval section indicates the name of the GUI distribution (zip) file, the installed executable version, and the file size. This section also provides primary and alternative FTP download locations of the installation file, any Release Notes, and other updated documentation files. Updated patch documentation is uploaded to the VDL within three days of the patch release at the following URL:

<http://www.va.gov/vdl/application.asp?appid=133>

When a CAPRI patch contains a new GUI version, users should be aware of any notes regarding the timing of installation of the M components and providing the new GUI to users.

VA staff with access to FORUM can subscribe to receive notification of newly released CAPRI patches by selecting the FORUM "Patch User Menu" option, "Select Packages for Notification" sub-option, then selecting the AMIE package.

## C&P Worksheet Template Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following functionality is only used to process Pascal Script DBQs. With CMT, the list of DBQs is generated from the PDFs that are downloaded and stored in the users appdata\local\capri\iepd\pdfs folder.

CAPRI examination templates are stored in the CAPRI TEMPLATE DEFINITION file. This file maintains a list of definitions used to generate examination templates in the CAPRI Graphical User Interface (GUI). Entries in the CAPRI TEMPLATE DEFINITION file are used by the CAPRI application to create the examination templates in the CAPRI GUI. Retired template definitions are retained in the file for historical purposes. This file should remain standardized between all sites. No additions, modifications, or edits should be made to this file except through the remote PUSH utility.

Entries in the CAPRI TEMPLATE DEFINITION file are maintained remotely. The Business Engineering Services Team (BEST) team manages the CAPRI TEMPLATE DEFINITION file using the CAPRI Template PUSH utility. Organizationally, the (BEST) falls under Systems Management within the VHA Chief Business Office (CBO).

This utility is used only by VBA Comp Service. PUSH utility users log onto the CLAIMS Server for authentication and verification. The user performing a PUSH operation must be assigned the option DVBA MANAGE CAPRI TMPLTES GUI option. This option exists only on the CLAIMS and TEST CLAIMS systems since this is where the operator is authenticated and where the initial context is created. The option DVBA CAPRI GUI is used to create the context for connection to sites where the template definitions are updated.

# Applications Development Tools and Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Code Repository Tool (Version Control)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delphi application utilizes the GitHub Repository for version control. Its VA approval documentation is located at URL: <https://github.ec.va.gov/EPMO/capri-gui>

## CAPRI Source Files for Delphi

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAPRI application is developed in Delphi. Standard source file name extensions are preserved as required by the development tool. These file name extensions are .dfm, .pas, .res, and .drc.

The CAPRI source files are stored on a GitHub Repository. Your code must be checked into GitHub once modifications have passed testing by the developer.

Due to the longevity of the CAPRI project only limited unit description and usage is available. The developer will need to reference the CAPRI GUI User Manual to obtain and understand what logic occurs when executing the application. By using the CAPRI GUI User Manual, adding break points in the Delphi IDE, the developer will obtain an understanding of the Functions, Procedures, RPCs, input and output file, and parameter list and usage.

Select the latest version of the <u>CAPRI GUI User Manual</u> at the following URL: <http://www.va.gov/vdl/application.asp?appid=133>

For any additional assistance refer to Section 1.3, CAPRI Technical Support, for contact information.

# Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CAPRI Remote Procedure Calls Logger

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Logger was created to better identify errors received in the field. Only personnel who have the Fileman Access Code of "@" in their new person record in VistA will have the ability to access the RPC Broker Call History Help menu option (Figure 18) and view the log file.

By default, the RPC Logger is set to OFF and is controlled by a command line parameter in the Shortcut Target line. Below are the defined command line parameters accepted to control the status of the RPC Logger:

- CAPRI will accept the command line parameters CH=
- Omitting the CH= parameter or setting CH=0 will turn off the RPC Logger.
- The CH= parameter can be followed by any number. The number will represent the number of days to keep the log before writing over the data stored. For example, the command line parameter CH=2 will turn on the RPC Logger and store data for 2 days. On the 3<sup>rd</sup> day the logger will be deleted and start storing data for another 2 days.
- The EL parameter enables a menu option for sending an email of logs including the RPC Broker Call History (Figure 15),  
  Example of the parameters for command line,  
  Technician: CH=2

End User: EL

- When selecting the menu option Email RPC Broker Log Files, the user will be alerted (Figure 16) that selecting this option will generate an email with attachments (Figure 17) that may contain patient information and before sending the email, it must be encrypted.

> ![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/016.png)

<span id="_Ref114558146" class="anchor"></span>Figure 15 Menu Option - Email RPC Broker Log Files

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/017.png)

<span id="_Ref114748858" class="anchor"></span>Figure 16 Email RPC Broker Log Files Alert

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/018.png)

<span id="_Ref114748888" class="anchor"></span>Figure 17 Example Email of RPC Call Logs

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/019.png)

<span id="_Ref114748646" class="anchor"></span>Figure 18 Help Menu - RPC Broker Call History Buffer

## CAPRI Remote Procedure Calls (RPCs) for MUMPS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See ([Appendix A](\l)

[CAPRI Remote Procedure Calls for MUMPS](\l)) for a list of detailed RPCs used by the CAPRI Graphical User Interface (GUI) software.

To duplicate the list of RPCs in Appendix A do the following:

1\. Type "D P^DI" to start FileMan.

2\. At "Select OPTION:", select option 2, "PRINT FILE ENTRIES."

3\. At "OUTPUT FROM WHAT FILE:", enter "REMOTE PROCEDURE."

4\. Accept the default for "SORT BY: NAME//" by hitting RETURN.

5\. At "START WITH NAME: FIRST//", enter "DVBA" to start with the first CAPRI RPC name.

6\. At "GO TO NAME: LAST//", enter "DVBC" to list all of the CAPRI namespace RPCs.

7\. Accept the default for "WITHIN NAME, SORT BY:"

8\. At "FIRST PRINT FIELD:", Enter a "?" and then "Y" for "Do you want the entire nn-Entry FIELD list?". The list will be displayed for you to choose from.

9\. At "FIRST PRINT FIELD:" prompt, enter ".01" for NAME. At each successive "THEN PRINT FIELD:" prompt, enter the field numbers listed here:

.02 TAG

.03 ROUTINE

.04 RETURN VALUE TYPE

.06 INACTIVE

1 DESCRIPTION (word-processing)

2 INPUT PARAMETER

At "THEN PRINT INPUT PARAMETER SUB-FIELD:" after entering "2," click RETURN to bypass sub-fields.

3 RETURN PARAMETER DESCRIPTION

10\. At the next "THEN PRINT FIELD:", press RETURN to complete the list of desired fields.

11\. For the heading, answer "Replace" with "REM...," then answer "With" with RETURN to remove a heading or enter a heading.

12\. At the "STORE PRINT LOGIC IN TEMPLATE:" select or create a Print Template or take the default to bypass creating a print template.

13\. At "DEVICE:", answer "0;80;99999" to display the RPC listing to your screen.

Copy and paste the results into a word processing application for possible cleanup.

This is an example of the dialog:

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/020.png)

<span id="_Toc106050288" class="anchor"></span>Figure 19 Display the RPC listing to your screen

# FileMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Procedures and Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VA FileMan documentation is available on the VDL, accessible at the following URL: <http://www.va.gov/vdl/application.asp?appid=5>

There is also additional documentation regarding other FileMan information i.e. FileMan Tips, etc.... is accessible at: <http://www.hardhats.org/index.html>

*Note: Using the Freedom of Information Act this website obtained documentation from the VA for VISTA. In general, this site gathers information from multiple sources including the VA website.*

### Environmental Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>VA FileMan V.22 Key and Index Tutorial</u> document contains the environmental setup information at the following URL: <http://www.va.gov/vdl/application.asp?appid=5>

### Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access the <u>VA FileMan Installation Guide</u> at: [https://www.va.gov/vdl/appliction.asp?appid=5](https://www.va.gov/vdl/application.asp?appid=5)

### Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access the VA FileMan Getting Started User Manual at: <https://www.va.gov/vdl/application.asp?appid=5>

### FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table is a list of recommended VA FileMan access codes associated with each file contained in the AMIE software.

| FILE NUMBER | FILE NAME                        | DD ACCESS | RD ACCESS | WR ACCESS | DEL ACCESS | LAYGO ACCESS |
|-----------------|--------------------------------------|---------------|---------------|---------------|----------------|------------------|
| 31              | Disability Condition                 | @             | D             | @             | @              | @                |
| 396             | Form 7131                            | @             | \#            | \#            | \#             | \#               |
| 396.1           | AMIE Site Parameter                  | @             | \#            | \#            | @              | @                |
| 396.17          | CAPRI Templates File                 | @             | @             | @             | @              | @                |
| 396.2           | AMIE Report                          | @             | \#            | \#            | \#             | \#               |
| 396.21          | CAPRI Clinical eFolder Transmissions | @             | @             | @             | @              | @                |
| 396.3           | 2507 Request                         | @             | \#            | \#            | \#             | \#               |
| 396.4           | 2507 Exam                            | @             | \#            | \#            | \#             | \#               |
| 396.5           | 2507 Cancellation Reason             | @             | \#            | @             | @              | @                |
| 396.6           | AMIE Exam                            | @             | \#            | @             | @              | @                |
| 396.7           | 2507 Body System                     | @             | \#            | @             | @              | @                |
| 396.94          | 2507 Insufficient Reasons            | @             | \#            | @             | @              | @                |
| 396.95          | AMIE C&P Exam Tracking               | @             | \#            | \#            | \#             | \#               |

*Note: The code (symbol) "@" in this table is the programmer's access. The other codes are arbitrary and are determined by the developers during the design phase and assigned as needed to users by the Information Systems (IS) staff in the File Manager Access Code field of the New Person (#200) file.*

### Advanced User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access the <u>VA FileMan Advanced User Manual</u> at:

<https://www.va.gov/vdl/application.asp?appid=5>

### Programmer Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access the <u>VA FileMan Programmer Manual</u> at:

<https://www.va.gov/vdl/application.asp?appid=5>

### Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide or special variables in the AMIE software.

#### Key Variables

- PNAM = Patient name
- DFN = Internal ^DPT number
- SSN = Social security number
- CFLOC = Claim folder location
- DCHGDT = Discharge date
- ADMDT = Admission date

#### How to Generate Online Documentation

This section describes some of the various methods by which users may secure AMIE technical documentation. Online technical documentation pertaining to the AMIE software, in addition to that which is in the help prompts may be generated through utilization of several Kernel options. These include XINDEX and VA FileMan List File Attributes. Further information about other utilities which supply online technical documentation may be found in the Kernel Reference Manual.

#### XIndex

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to VistA Programming Standards. The XINDEX output may include the following components: compiles list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VistA Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the AMIE software, specify the following namespace at the "routine(s) prompt: DVBA\* and DVBC\*. AMIE initialization routines which reside in the UCI in which XINDEX is being run, as well as compiled template routines found within the AMIE namespace, should be omitted at the "routine(s) prompt. To omit routines from selection, preface the namespace with a minus sign (-).

#### Data Dictionary List File Attributes

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

For a comprehensive listing of AMIE files used by CAPRI, please use the following link (URL) to locate the "Files" section of the AMIE Technical Manual: <http://www.va.gov/vdl/application.asp?appid=31>

### Technical Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access the <u>VA FileMan Technical Manual</u> at:

<https://www.va.gov/vdl/application.asp?appid=5>

# Archiving, Purging, and Frequency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CAPRI relies on the AMIE application for any archiving and purging functionality.

Although the AMIE software has no archiving capabilities AMIE's purging capabilities are handled by the DVBA REGIONAL PURGING PROGRAM option. This option deletes all FINALIZED requests which are older than the date set in the AMIE SITE PARAMETER file (#396.1). It should normally be set to run daily on TaskMan, as it takes several minutes to run in programmer mode. In addition to purging the FORM 7131 file (#396), it also purges the AMIE REPORT file (#396.2).

The frequency is based on the amount of 7131 information purged by this program. It is determined by the NUMBER OF DAYS TO KEEP HISTORY parameter set through the Regional File Site Parameter Setup option. It is suggested to keep at least 30 days on file at all times, but no more than 120 days. The NUMBER OF DAYS TO KEEP HISTORY field (#9) of the AMIE SITE PARAMETER file (#396.1) will automatically keep 30 days of report data if no value is in that field.

While the AMIE software uses a very small amount of disk space, it is wise not to let the data accumulate if it is not needed by the hospital.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Directive 10-93-142 prohibits local modifications to VistA software.

## General Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CAPRI GUI security refer to the most current CAPRI User Manual. This manual includes instructions for setting up CAPRI users, as well as descriptions of all Security Keys used by the CAPRI GUI application.

See the CAPRI GUI User Manual at: <http://www.va.gov/vdl/application.asp?appid=133>

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMIE software does not transmit data to any remote systems. For CAPRI interactions with remote systems, refer to the Systems Architecture diagram in Section 3.1.1.

### Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your facility should have a local contingency plan in the event of application problems in a live environment. It should identify the procedure for maintaining functionality provided by the AMIE software as well as the CAPRI GUI application, in the event of system outage.

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special interfacing requirements for the AMIE or the CAPRI software.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAPRI GUI application uses electronic signatures. Use the following link to locate the CAPRI GUI User Manual: <http://www.va.gov/vdl/application.asp?appid=133>

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following steps to get information about the security keys used with the AMIE software.

> 1\. VA FileMan Menu

> 2\. Print File Entries Option

> 3\. Output from what File: SECURITY KEY

> 4\. Sort by: Name

> 5\. Start with name: DVBA to DVBC

> 6\. Within name, sort by: \<RET\>

> 7\. First print field: Name

> 8\. Then print field: Description

*Note: Some keys do not affect the menu operation. This is due to some options having several different functions which are limited in scope by the key. This limitation is done internally by the program being used.*

# CAPRI Troubleshooting and Error Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** In all cases, please print the error message for your local IRM staff.

A majority of CAPRI issues that are initially called into the Service Desk or are created into ServiceNow tickets are not often CAPRI related issues, but are due to other issues regarding networks and users' accesses/permissions, etc. Those few CAPRI issues that are identified as a CAPRI issue are forwarded onto the CAPRI Team. The team works to replicate and identify the issue, then to develop solutions or workarounds to correct or eliminate the issue. Some of these issues result in identification of a CAPRI defect or an issue that may become a future CAPRI enhancement. These issues are often unique and not reported in any significant numbers. The CAPRI Team forwards these specific issues onto the VA who will determine if the issue(s) is something that should be recognized as a defect or a possible CAPRI enhancement scheduled for one of the next CAPRI patch installation deployments.

The remainder of this section includes general CAPRI troubleshooting and error information that is located within the <u>CAPRI GUI User Manual</u> at the following URL: <http://www.va.gov/vdl/application.asp?appid=133>

Select the latest version of the document; refer to the section "Troubleshooting and Error Messages."

## CAPRI Not Installed in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user receives the message in the following screenshot if the VHA Medical Center has not loaded the VHA half of the CAPRI software. The user should contact local IRM staff after receiving this message.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/021.png)

<span id="_Toc106050289" class="anchor"></span>Figure 20 CAPRI Not Installed in VistA Error Message

## CAPRI GUI Option Not Assigned to User in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user receives the message in the following screenshot if the VHA medical center has not assigned the CAPRI option to RO users. The user must contact local IRM staff upon receiving this message.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/022.png)

<span id="_Toc106050290" class="anchor"></span>Figure 21 CAPRI GUI Option Not Assigned to User in VistA

## VistA Server Down

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user receives the message in the following screenshot, or a similar one such as WSAETIMEDOUT, when there are performance issues in the VA Wide Area Network (WAN), if a server is down, or if a server was not restarted after being down. When this happens, AMIE II may or may not connect, depending on the exact problem. The user should test the AMIE II connection.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/023.png)

<span id="_Toc106050291" class="anchor"></span>Figure 22 VistA Server Down Error Message

## VistA Limits Ability to See Patient Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user receives the message in the following screenshot if the medical facility made local permission modifications in VistA that prohibit users from seeing the contents of patient records.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/024.png)

<span id="_Toc106050292" class="anchor"></span>Figure 23 VistA Limits Ability to See Patient Records

## Network Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user receives the message in the following screenshot if the connection to the medical facility is lost unexpectedly. The user should try to connect to the medical facility again.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/025.png)

<span id="_Toc106050293" class="anchor"></span>Figure 24 Could not connect to Remote Server Error Message

## Institution File in VistA has Been Locally Modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may receive the message in the following screenshot when requesting exams, requesting 7131s, or entering new patients if the VHA medical facility has an incomplete or incorrect Regional Office list in their system.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/026.png)

<span id="_Toc106050294" class="anchor"></span>Figure 25 Incomplete or Incorrect Regional Office

## Too Many Invalid Attempts at Access Code / Verify Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user receives the message in the following screenshot if the user attempted to log on and entered the wrong Access Code / Verify Code combination three or more times.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/027.png)

<span id="_Toc106050295" class="anchor"></span>Figure 26 Device locked due to multiple sign-on message.

## Multiple Sign-Ons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may receive the message in the following screenshot if the user did not log out of CAPRI correctly or if the session was unexpectedly disconnected.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/028.png)

<span id="_Toc106050296" class="anchor"></span>Figure 27 Multiple Sign-on error Message.

## General Error Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may receive the message in the following screenshot for several reasons. Upon receiving this message, the user should cancel the current task, close CAPRI, and sign on again. If the user receives this error message again, local IRM staff should be contacted for assistance.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/029.png)

<span id="_Toc106050297" class="anchor"></span>Figure 28 General Error Message

## Permanent Failure DBQ Transmission Error Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a permanent Failure occurs, CAPRI will not allow these DBQs to be retransmitted as there was a failure that is unable to be resolved. CAPRI prompts users with an error message for the DBQ in the worksheet that experienced the error, with the status code and refers the user to the IT Service Desk.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/030.png)

<span id="_Toc106050298" class="anchor"></span>Figure 29 Permanent Failure Error

## Transmission Error DBQ Error Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each DBQ will be evaluated individually for transmission success/fail. If a transmission error occurs, then CAPRI will attempt to retransmit any DBQs which failed their previous transmission attempt.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/031.png)

<span id="_Toc106050299" class="anchor"></span>Figure 30 DBQ Transmission Error

CAPRI will iterate though the remaining DBQs, showing a transmission error message for each. After attempting to transmit the final DBQ in the worksheet, if any remain with a transmission error status, CAPRI will display the \# of attempts. The retransmission will time out after 5 attempts. To retransmit the DBQ, refer to section 2.13.6 of the CAPRI user manual.

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-255/032.png)

<span id="_Toc106050300" class="anchor"></span>Figure 31 DBQ Retransmission Attempts

# Appendix A 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CAPRI Remote Procedure Calls for MUMPS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DVBA CAPRI GUI menu option contains all the CAPRI RPCs.

Name: DVBA CAPRI GUI

Menu Text: Capri GUI (Broker)

Type: Broker (Client/Server)

Package: AUTOMATED MED INFO EXCHANGE

Description: This is the "B" type option used by CAPRI GUI client application. It contains all the RPCs used by the CAPRI GUI application.

The table that starts on the next page shows a correlation between CAPRI's MUMPS RPCs and GUI RPC Utilization details associated within supporting the CAPRI application.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><strong>MUMPS RPCs</strong></th>
<th colspan="4"><strong>GUI RPC Utilization Details</strong></th>
</tr>
<tr class="odd">
<th>NAME</th>
<th>TAG</th>
<th>ROUTINE</th>
<th>RETURN VALUE TYPE</th>
<th>DESCRIPTION</th>
<th>INPUT PARAM. (Multi.)</th>
<th>RETURN PARAMETER DESCRIPTION:</th>
<th>PROCEDURE NAME</th>
<th>LOCATIONS</th>
<th>BROKER NAME</th>
<th>PARAMETER</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DG SENSITIVE RECORD ACCESS</td>
<td>PTSEC</td>
<td>DGSEC4</td>
<td>ARRAY</td>
<td>This Remote Procedure Call (RPC) will:<br />
- Verify user is not accessing his/her own Patient file record if the Restrict Patient Record Access (#1201) field in the MAS parameters (#43) file is set to yes and the user does not hold the DG RECORD ACCESS security key. If parameter set to yes and user is not a key holder, a social security number must be defined in the New Person file for the user to access any Patient file record.<br />
- Determine if user accessing a sensitive record or an employee's record</td>
<td>NONE</td>
<td>RESULT(1) =<br />
-1-RPC/API failed Required variable not defined<br />
0-No display/action required Not an employee, not sensitive or not accessing own Patient record<br />
1-Display warning message Sensitive - inpatient or a DG SENSITIVITY key holder or Employee and DG SECURITY OFFICER key holder<br />
2-Display warning message, require OK to continue and call DG SENSITIVE RECORD BULLETIN RPC to update DG Security Log file and generate Sensitive Record Access mail message. Sensitive - not an inpatient and not a key holder or Employee/not a DG SECURITY OFFICER key holder<br />
3-Access to record denied Accessing own Patient file record<br />
4-Access to Patient file (#2) records denied SSN not defined RESULT(2-n) = error message or warning/Privacy Act message. Error and warning messages will begin in RESULT(2) array. The Privacy Act message is the longest message and will utilize RESULT(2)- RESULT(8).<br />
If RESULT(1)=1, the DG Security Log file is updated.<br />
If RESULT(1)=2, the user must acknowledge they want to access the restricted record and the application must call the DG SENSITIVE RECORD BULLETIN RPC to update the DG Security Log file and generate the Sensitive Record Access mail msg</td>
<td>TfrmPatientList.<br />
btnCvrSelectPtClick<br />
<br />
TfrmPatientList.<br />
FMCvrListBox1PtClick<br />
<br />
TfrmPatientListRestricted.<br />
ORListBox1Change<br />
<br />
TfrmPatientListRestricted.<br />
btnCvrSelectPtClick</td>
<td>patientlist.pas<br />
<br />
patientlistrestricted.pas</td>
<td>RPCBroker1</td>
<td>FMCvrListBox1Pt.GetselectedRecord.IEN<br />
FMCvrListBox2Pt.GetselectedRecord.IEN<br />
FMCvrListBox3Pt.GetselectedRecord.IEN<br />
PType := literal; for all params<br />
<br />
FMListBox1.GetSelectedRecord.IEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DG SENSITIVE RECORD BULLETIN</td>
<td>NOTICE</td>
<td>DGSEC4</td>
<td>SINGLE</td>
<td>This Remote Procedure Call (RPC) will add an entry to the DG SECURITY LOG (#38.1) file and/or generate the sensitive record access bulletin depending on the value in ACTION input parameter. If ACTION parameter not defined, defaults to update DG Security Log file and generate Sensitive Record Access mail message.</td>
<td>NONE</td>
<td>RESULT=<br />
1 - successfully added entry and/or generated sensitive record access bulletin<br />
0 - unsuccessfully</td>
<td>TfrmPatientList.<br />
btnCvrSelectPtClick<br />
<br />
TfrmPatientListRestricted.<br />
btnCvrSelectPtClick</td>
<td>patientlist.pas<br />
<br />
patientlistrestricted.pas</td>
<td>RpcBroker1</td>
<td>PatientIEN<br />
PType := literal;<br />
'DVBA CAPRI GUI^Capri GUI (Broker)'<br />
PType := literal;<br />
Value := '';<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIADDEXAM" class="anchor"></span>DVBA CAPRI ADD EXAM</td>
<td>ADDPDF</td>
<td>DVBCTPD2</td>
<td>SINGLE VALUE</td>
<td>Allows CAPRI user to add a new exam to an existing worksheet.</td>
<td>DVBIEN</td>
<td>Worksheet IEN:Exam Name:Exam Sequence Number</td>
<td>TCAPRIDbqPdf.<br />
AddPDFToWorksheet</td>
<td>clsDBQPDFHandler.pas<br />
frmPNCSMainVistA</td>
<td>RpcBroker1</td>
<td>WorksheetIEN, PDFName</td>
</tr>
<tr class="even">
<td>DVBA CAPRI ALERTS DATA</td>
<td>ALRTDATA</td>
<td>DVBSIGN2</td>
<td>GLOBAL ARRAY</td>
<td>Returns the data for the following worksheet review statuses:<br />
A=Awaiting Signature, D=Draft/Not ready, O=Outdated Template, P=Review Pending, S=Sent Back</td>
<td>DVBDUZ</td>
<td>Data will be returned in an array as follows:<br />
RET(&lt;worksheet ien&gt;)=Worksheet IEN^ID^Patient IEN^Patien name^Document manager IEN^Document manager name^Form title^Review status^Flag new^Flag green flag^Flag exclamation^&lt;exam count&gt;^&lt;exam 1 name&gt;,&lt;exam 2 name&gt;,...<br />
<strong>OR</strong><br />
=-1^No data available</td>
<td>TfrmCMTUnsignedForm.<br />
GetAlertDataFromVistA</td>
<td>frmCMTUnsigned.pas</td>
<td>RpcBroker1</td>
<td>UserFlag, Status, Owner Type</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIARPOPTSET" class="anchor"></span>DVBA CAPRI ARP OPSET</td>
<td>UOTASKS</td>
<td>DVBAARP</td>
<td>ARRAY</td>
<td>Setting out of order message and unschedule taskman jobs for AMIE options</td>
<td>DVBMSG<br />
DVBOPLIST</td>
<td>OPTION 1^TASK ID:RETURN CODE^TASK:RETURN CODE(<br />
<strong>OR</strong><br />
0=Did not unschedule taskman jobs<br />
1=Successfully unscheduled taskman jobs<br />
-1=No tasks scheduled</td>
<td>TPushUtilAsyncDisableOptions.<br />
PrepareRPCData</td>
<td>PushUtilAsyncDisableOptions.pas</td>
<td>LocRPCConnect</td>
<td>Out Of Order Message<br />
Option List to disable</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRIARPRSKDT" class="anchor"></span>DVBA CAPRI ARP RSKDT</td>
<td>COMBINE</td>
<td>DVBAARP</td>
<td>ARRAY</td>
<td>For enabling AMIE options and rescheduling AMIE options</td>
<td>DVBAOPTIONS<br />
DVBDATA</td>
<td>The AMIE Options and RUNTIMES which need to be rescheduled<br />
RETURN PARAMETER DESCRIPTION:<br />
First Return is AMIEOPTION:FLAG<br />
FLAG= 1 FOR SUCCESSFULL AND 0 FOR UNSUCCESSFUL<br />
NEXT RETURN WOULD BE AMIEOPTION^RUNTIME^FLAG<br />
FLAG = 1 FOR SUCCESSFULL<br />
No runtime specified for Option<br />
ERROR: Option Out of Order<br />
Option already scheduled</td>
<td>TPushUtilAsyncEnableOptions.<br />
PrepareRPCData</td>
<td>PushUtilAsyncEnableOptions.pas</td>
<td>LocRPCConnect</td>
<td>Option List to re-enable<br />
Task List^Runtime List</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI CLINDOCS URLS</td>
<td>CLNDCUR CLNDCU</td>
<td>DVBCTOG</td>
<td>ARRAY</td>
<td>This REMOTE PROCEDURE CALL returns the PIV URL, proxy URL and the priority of which transmission process is assigned.</td>
<td>NONE</td>
<td>NONE</td>
<td>CAPRISupport<br />
UpdateClinDocSetting</td>
<td>uDocumentUploadREST.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI CMT IEPD RESET</td>
<td>IEPDRESET</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>RPC will return value of DVBAB CAPRI CMT IEPD RESET parameter. This value is being used to determine if the CAPRI GUI will redownload the IEPD</td>
<td>NONE</td>
<td>Zero (0) or Date (MM/DD/YYYY)</td>
<td>uIEPD<br />
ForceIEPDDownload</td>
<td>uIEPD.pas<br />
FirstCheckOfDayForIEPDDownloadBegin</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRICMTSIGFLDNUM" class="anchor"></span>DVBA CAPRI CMT SIGFLD NUM</td>
<td>SIGFLDNUM</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>Returns value from Parameter: DVBAB CAPRI CMT SIGFLD NUM</td>
<td>NONE</td>
<td>Returns Number and delimiter for current IEPD placement of PDF Field names= "3^_"</td>
<td>TfrmMain.SetWorkSheetDBQFieldNameLocation</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRICMTSKIPCOND" class="anchor"></span>DVBA CAPRI CMT SKIP COND</td>
<td>CONDSKIP</td>
<td>DVBUTIL</td>
<td>ARRAY</td>
<td>Returns list of parameters in DVBAB CAPRI SKIP CONDFIELD</td>
<td>NONE</td>
<td>RTN(0)=Count<br />
RTN(1)=Conditional Logic to skip value<br />
OR<br />
-1^Parameter Empty</td>
<td>Main<br />
SetConditionalLogicSkipConditionalFieldFile</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI CMT SSN VAR</td>
<td>GETSSNVAR</td>
<td>DVBCTXM2</td>
<td>GLOBAL ARRAY</td>
<td>This RPC will be used by CAPRI to return CMT SSN Variances</td>
<td>NONE</td>
<td>This will return CMT SSN Variances's values stored in DVBAB CAPRI CMT SSN VAR parameter.</td>
<td>TfrmMain.<br />
actFileConnectExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI CMT TOGGLE</td>
<td>TOGGLE</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>This RPC is returning data from the DVBAB CAPRI CMT TOGGLE parameter.<br />
This value tells the CAPRI GUI which C&amp;P type is being used, CMT or Pascal</td>
<td>NONE</td>
<td>Value for display in the CAPRI GUI, 1=CMT button only, 2=PASCAL button only and 3=Both buttons</td>
<td>TfrmMain.<br />
FeatureTogglePascalOrCMT</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="RANGE!A12" class="anchor"></span>DVBA CAPRI CREATE WORKSHEET</td>
<td>CREATE</td>
<td>DVBCTPDF</td>
<td>ARRAY</td>
<td>Called by CAPRI to create a new entry in ^DVB(396.17) Will create new Worksheet IEN and save basic details.</td>
<td>DVBDATA</td>
<td>DVBPATIENT - Patients IEN<br />
DVBAUTHOR - Author IEN<br />
DVBIEPDVER - IEPD Version Number<br />
DVBDBQREF - DBQ Referal Flag<br />
DVBTRANSCRIB - Transcriber IEN<br />
DVBFORMNAME - Single Exam Name or 'Merged Form'<br />
INPUT PARAMETER: DVBEXAMLIST PARAMETER TYPE: LIST<br />
MAXIMUM DATA LENGTH: 250 REQUIRED: YES<br />
SEQUENCE NUMBER: 2<br />
DESCRIPTION: List of Exam Names</td>
<td>TPNCSMainVistA.<br />
CreateNewWorksheet</td>
<td>frmPNCSMainVistA.pas</td>
<td>RPCBroker1</td>
<td>PatientIEN,<br />
AuthorDUZ, CurrentIEPDVersion,<br />
' ',<br />
AuthorDUZ,<br />
WorksheetTitle,<br />
List of DBQ names</td>
</tr>
<tr class="even">
<td>DVBA CAPRI DBQ TRANS FAIL LIST</td>
<td>FAILIST</td>
<td>DVBCTXML</td>
<td>GLOBAL ARRAY</td>
<td>This RPC is returning a list of failed XML transmissions to the CAPRI GUI</td>
<td>DVBDUZ</td>
<td>This is the DUZ if that person is requesting only their own records to be returned in the list.</td>
<td>TDBQXmlRPCHandler.<br />
GetFailedExamsForSite</td>
<td>fManTranVista.pas<br />
Main.pas</td>
<td>RPCBroker1</td>
<td>DUZ</td>
</tr>
<tr class="odd">
<td><span id="RANGE!A15" class="anchor"></span>DVBA CAPRI DELETE CHECK</td>
<td>DELCHECK</td>
<td>DVBCTPDF</td>
<td>SINGLE VALUE</td>
<td>This will check if a user is able to delete a worksheet from File 396.17.</td>
<td>DVBIEN</td>
<td>RETURNING A 1 IF THE USER IS ALLOWED TO DELETE THE WORKSHEET, IF NOT THE FOLLOWING 2 ERRORS WILL BE RETURNED:<br />
-1^User is not Author or Transcriber<br />
-1^USER does not have Fileman Access<br />
-1^USER does not have DVBAB CPWM REVIEWER Security Key</td>
<td>TfrmMain.<br />
IsAuthorizedToDeleteWorksheet</td>
<td>Main.pas<br />
frmCMTUnsigned.pas<br />
unsigned.pas</td>
<td>RPCBroker1</td>
<td>WorksheetIEN</td>
</tr>
<tr class="even">
<td><span id="RANGE!A16" class="anchor"></span>DVBA CAPRI DELETE EXAM</td>
<td>DELETE EXAM</td>
<td>DVBCTPD2</td>
<td>SINGLE VALUE</td>
<td>Allows CAPRI to delete an exam from a worksheet</td>
<td>DVBIEN<br />
DVBSEQ<br />
DVBEXAMNAME</td>
<td>1 if completed, -1 with error message</td>
<td>TCAPRIDbqPdf.<br />
DeletePDFFromWorksheet</td>
<td>frmPNCSMainVistA.pas</td>
<td>RpcBroker1</td>
<td>WorksheetIEN,<br />
SequenceNumber,<br />
ExamName</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI DELETE WORKSHEET</td>
<td>DELETE</td>
<td>DVBCTPDF</td>
<td>SINGLE VALUE</td>
<td>RPC is deleting the worksheet from File 396.17</td>
<td>DVBIEN</td>
<td>Returns a 1 if successfully deleted or -1 if not</td>
<td>TfrmMain.<br />
DeleteWorksheet</td>
<td>Main.pas<br />
frmCMTUnsigned.pas<br />
unsigned.pas</td>
<td>RPCBroker1</td>
<td>WorksheetIEN</td>
</tr>
<tr class="even">
<td>DVBA CAPRI EXAM LINK TIU</td>
<td>LINK</td>
<td>DVBAXML</td>
<td>SINGLE VALUE</td>
<td>Links an exam in CAPRI TEMPLATES #396.17 to TIU DOCUMENT #8925</td>
<td>EXAMIEN<br />
TIUIEN</td>
<td>returns 1 if the exam has been successfully linked to the TIU DOCUMENT; otherwise return 0^error message</td>
<td>TTIUSignForm.<br />
ButtonOK2Click<br />
<br />
TCMTSignForm.<br />
btnSignClick</td>
<td>tiusign.pas<br />
frmCMTSign.pas</td>
<td>RpcBroker1</td>
<td>PNCSForm.xFMEdit2.IENS<br />
TIUNoteIEN<br />
<br />
PNCSMainVistA.WorksheetIEN<br />
TIUNoteIEN</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI EXAM RESTORE</td>
<td>RESTORE</td>
<td>DVBCTPD2</td>
<td>SINGLE VALUE</td>
<td>RPC will allow user to restore an exam, even ones deleted, to a previous version based on save sequence numbers displayed in the Exam History RPC.</td>
<td>DVBIEN<br />
DVBSEQ<br />
DVBEXAM<br />
DVBSAVE<br />
DVBDTM</td>
<td>Return 1 for successful restore<br />
-1^Missing_"Worksheet IEN,Exam Seq,Exam Name,Save Seq,Save DateTime"<br />
The first found piece missing will be listed above</td>
<td>TfrmCMTPdfLoadPreviousVersion.<br />
SaveRestoredPDFToVistA</td>
<td>fCMTPdfLoadPreviousVersion.pas</td>
<td>RpcBroker1</td>
<td>WorkSheet_IEN, SequenceNumber,<br />
ExamName, SaveSequenceNumber,<br />
DtTime</td>
</tr>
<tr class="even">
<td>DVBA CAPRI EXAM XML</td>
<td>FILEIN</td>
<td>DVBAXML</td>
<td>SINGLE VALUE</td>
<td>This RPC allows for the filling of the 2507 EXAM template in the XML version.</td>
<td>EXAMIEN<br />
DAS<br />
XML</td>
<td>XML is the array list format of the template being stored<br />
RETURN PARAMETER DESCRIPTION:<br />
Y Returns successful filing status or error message</td>
<td>TTIUSignForm.<br />
SendDbqsToVista</td>
<td>Tiusign.pas</td>
<td>RpcBroker1</td>
<td>AnExamIEN;<br />
PType := literal;<br />
<br />
CAPRI_InhouseExamXMLNote;<br />
PType := literal;<br />
<br />
List of files<br />
uuEncodedFile<br />
PType := list;</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI FAIL CHECK</td>
<td>FAILCHK</td>
<td>DVBCTXML</td>
<td>SINGLE VALUE</td>
<td>RPC will check if there are any failed transmissions in File 396.17. If there is at least 1 it will return a 1.</td>
<td>NONE</td>
<td>1 if there is at least one failed XML transmissions in File 396.17, 0 if there are none.</td>
<td>TDBQXmlRPCHandler.<br />
FailedTransmissionCheck</td>
<td>Main.pas</td>
<td>RpcBroker1</td>
<td>No params</td>
</tr>
<tr class="even">
<td><span id="RANGE!A22" class="anchor"></span>DVBA CAPRI GET DBQ PDF</td>
<td>FAILPDF</td>
<td>DVBCTPDF</td>
<td>GLOBAL ARRAY</td>
<td>This RPC is returning the DBQ PDF to retransmet DBQ's from the eFolder que</td>
<td>DVBIEN<br />
DVBCT</td>
<td>NONE</td>
<td>TCAPRIDbqPdf.<br />
GetDataFromVistA</td>
<td>clsDBQPDFHandler.pas</td>
<td>RPCBroker1</td>
<td>PDF_IEN, Index</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GET DBQ XML</td>
<td>FAILXML</td>
<td>DVBCTXML</td>
<td>GLOBAL ARRAY</td>
<td>This RPC is being used by CAPRI GUI to retrieve the XML document stored in File ^DVB(396.17).</td>
<td>DVBIEN</td>
<td>The entry number of which XML Document within the record</td>
<td>TDBQXmlRPCHandler.<br />
GetTemplateXmlData</td>
<td>Main.pas<br />
fManTransVista.pas</td>
<td>RPCBroker1</td>
<td>TemplateIEN, XMLIEN</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GET EDIPI</td>
<td>EDIPIQ</td>
<td>DVBCENQ</td>
<td>SINGLE VALUE</td>
<td>Capri Remote Procedure Call Returns EDIPI To Be Sent Via DBQ's To DoD</td>
<td>DFN</td>
<td>Capri Remote Procedure Call returns an EDIPI number from File 391.91. If no number is found, it returns 0</td>
<td>TfrmMain.<br />
GetPatientEDIPINumber<br />
<br />
TVlerDasClaim.ToXml</td>
<td>Main.pas<br />
<br />
VlerEDasClaim.pas</td>
<td>RPCBroker1</td>
<td>PatientIEN</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GET EFOLDER TOKEN</td>
<td>EFOLD</td>
<td>DVBABURL</td>
<td>NONE</td>
<td>CAPRI REMOTE PROCEDURE CALL RETURNS DVBAB CAPRI CDEFOLD TOKEN SECURITY CODE. EXISTING CODE WILL VERIFY THAT USER HAS THE DVBA CAPRI CLIN DOC-EFOLDER SECURITY KEY ASSIGNED, IF NOT A "-1" AND ERROR REASON IS RETURNED.</td>
<td>DUZ</td>
<td>NONE</td>
<td>TfrmMain.<br />
actFileConnectExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Authorien<br />
PType := literal</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GET EXAM HISTORY</td>
<td>EXAMHIST</td>
<td>DVBCTPD2</td>
<td>GLOBAL ARRAY</td>
<td>Allows the CAPRI user to get the exam history for a given worksheet.</td>
<td>DVNIEN</td>
<td>Exam Sequence Number^Exam Name^Exam Save Number^Exam save date^Save Message^Version^User<br />
Otherwise one of the following:<br />
-1^No worksheet IEN was provided<br />
-1^Worksheet IEN=&lt;ien&gt; does not exist<br />
-1^Worksheet IEN=&lt;ien&gt; has no exam history</td>
<td>TfrmCMTPdfLoadPreviousVersion.<br />
LoadWkstPreviousVersions</td>
<td>fCMTPdfLoadPreviousVersion.pas</td>
<td>RpcBroker1</td>
<td>WorkSheet_IEN</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GET EXAM IEN</td>
<td>GETEXAM</td>
<td>DVBXML</td>
<td>SINGLE VALUE</td>
<td>get an exam ien from the CAPRI TEMMPLATE #396.17 given a tiu ien from TIU DOCUMENT #8925</td>
<td>TIUIEN</td>
<td>returns an integer greater than zero if the exam can be found; otherwise return -1^error message</td>
<td>TTIUSignForm.<br />
LoadDBQForRendering<br />
<br />
TCMTSignForm.<br />
GetDBQWorksheetIENByTIUNoteIEN</td>
<td>tiusign.pas<br />
frmCMTSign.pas</td>
<td>RpcBroker1</td>
<td>TiuDocumentIen<br />
Ptype;=literal;</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GET EXAM PDF</td>
<td>PDFRTN</td>
<td>DVBCTPDF</td>
<td>GLOBAL ARRAY</td>
<td>This RPC will return to the CAPRI GUI the info needed for the Sharepoint IEPD process</td>
<td>DVBARRAY</td>
<td>The first piece is the IEN from file 396.17, second piece etc. is the name of the exam wanted.</td>
<td>TCAPRIDbqPdf.<br />
GetExamPDF</td>
<td>frmPNCSMainVistA.pas<br />
frmPDFMainVistA.pas</td>
<td>RPCBroker1</td>
<td>clsDBQPDFHandler</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIGETEXAMREPORT" class="anchor"></span>DVBA CAPRI GET EXAM REPORT</td>
<td>TRANSRPT</td>
<td>DVBCTPD2</td>
<td>GLOBAL ARRAY</td>
<td>Returns list of DBQ Name,Transmit Date, Patient, Status, Author, and Response Code.</td>
<td>DVBIEN<br />
DVBSDT<br />
DVBEDT</td>
<td>IEN provided returns all transmission history for that worksheet. Date Range provided returns all Worksheet transmission history for worksheets with XML origination date within range.</td>
<td>TDBQTransmissionHistoryReport.<br />
GetReportData</td>
<td>clsDBQTransmissionHistoryReport.pas</td>
<td>RPCBroker1</td>
<td>WorksheetIEN, StartDate, EndDate If the WorksheetIEN is blank but the start and end dates are provided the RPC will return all DBQ transmission for the site within that date range. If only the WorksheetIEN is passed to the RPC it will return the transmission history for that worksheet.</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRIGETEXAMINERINFO" class="anchor"></span>DVBA CAPRI GET EXAMINER INFO</td>
<td>EXINFO</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>This RPC returns data for a given user.</td>
<td>DVBDUZ<br />
DVBDVI</td>
<td>User's standard name(first MI last)^User's division name^User's division<br />
street address 1^User's division street address 2^User's division<br />
City^User's division state abbreviation^User's division zip code<br />
<strong>OR</strong><br />
-1^No user IEN was provided<br />
-1^No division IEN was provided <strong><br />
</strong>-1^User with IEN=&lt;ien&gt; does not exist<br />
-1^Division with IEN=&lt;ien&gt; does not exist</td>
<td>TCMTSignForm.<br />
AutoSignDBQExams</td>
<td>frmCMTSign.pas</td>
<td>RpcBroker1</td>
<td>SignerDUZ, UserDivisionIEN</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GET GITHUB DATA</td>
<td>GITTOK</td>
<td>DVBCTXML</td>
<td>SINGLE VALUE</td>
<td>This RPC will return the GITHUB location for C&amp;P Worksheet templates</td>
<td>NONE</td>
<td>NONE</td>
<td>TGitHubIEPDDownload.<br />
GetGitHubParameterInfo</td>
<td>uIEPD.pas<br />
FirstCheckOfDayForIEPDDownloadBegin</td>
<td>RPCBroker1</td>
<td>NONE</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GET GITHUB DATE</td>
<td>PARDATE</td>
<td>DVBCTXM2</td>
<td>SINGLE VALUE</td>
<td>This RPC will receive the GITHUB error date from the CAPRI GUI and set it in the DVBAB CAPRI GITHUB ERROR DATE parameter</td>
<td>DVBDATE</td>
<td>NONE</td>
<td>uIEPD<br />
GetIEPDFile<br />
<br />
uIEPD<br />
TGitHubIEPDDownload.DownloadFileFromGitHub</td>
<td>uIEPD.pas<br />
FirstCheckOfDayForIEPDDownloadBegin</td>
<td>RPCBroker1</td>
<td>use a blank not an empty string to clear the date</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GET MET RPT</td>
<td>RPCENTRY</td>
<td>DVBCTOG</td>
<td>ARRAY</td>
<td>This RPC is used by the CAPRI GUI to obtain a Metrics Report of Clinical Document Transmissions. Data stored in file ^DVB(396.21)</td>
<td>DVBBDT</td>
<td>Beginning date for report</td>
<td>Tfrmreports.<br />
GetTransMissionMetricsReport</td>
<td>Reports.pas</td>
<td>RPCBroker1</td>
<td>StartDate<br />
EndDate</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GET SECID</td>
<td>GETSECID</td>
<td>DVBSECID</td>
<td>SINGLE VALUE</td>
<td>Returns the SECID information for a NEW PERSON file entry.</td>
<td>DVBDUZ</td>
<td>DUZ / IEN from the NEW PERSON file.<br />
RETURN PARAMETER DESCRIPTION:<br />
1^SECID^SUBJECT ORGANIZATION^SUBJECT ORGANIZATION ID^UNIQUE USER ID^ADUPN<br />
<strong>OR</strong><br />
-1^Error Message</td>
<td>TfrmMain.<br />
SetUserIsValidForSecID</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>UserDUZ</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GET TOGGLES</td>
<td>GETTOG</td>
<td>DVBCTOG</td>
<td>SINGLE VALUE</td>
<td>This REMOTE PROCEDURE CALL returns the internal value of any parameter that meets the criteria of having an entity defined as PACKAGE and an instance that does not apply.</td>
<td>DVBTOG</td>
<td>The input parameter will be the name of a toggle</td>
<td>CAPRISupport<br />
UpdateClinDocSetting</td>
<td>CAPRISupport.pas<br />
fPostSSL.pas</td>
<td>RPCBroker1</td>
<td>DVBAB CAPRI PIV ACTIVE<br />
or<br />
DVBAB CAPRI PROXY ACTIVE</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRIGETWORKSHEET" class="anchor"></span>DVBA CAPRI GET WORKSHEET</td>
<td>PDFEXM</td>
<td>DVBCTPDF</td>
<td>GLOBAL ARRAY</td>
<td>This RPC will return the list of CAPRI Worksheet from file 396.17</td>
<td>DVBIEN</td>
<td>Return is:<br />
Worksheet common data<br />
seq no^tab order^exam name</td>
<td>TfrmExamDetails.<br />
btnViewPDFResultsClick<br />
TfrmMain.<br />
DisplayCMTWorksheet<br />
TfrmMain.<br />
CopyFromExistingWorkheet<br />
TfrmTIUCosign.<br />
btnPreviewPDFClick<br />
TfrmTIUCosign.<br />
btnPreviewPDFClick<br />
TUnsignedView.<br />
btnDisplayPDFClick<br />
untMiscMthds<br />
GetWorksheetByIEN<br />
TPNCSMainVistA.<br />
RebuildHeader<br />
TCMTSignForm.<br />
LoadWorksheetByIEN<br />
TfrmCMTUnsignedForm.<br />
btnDisplayPDFClick</td>
<td>examdet.pas<br />
Main.pas<br />
tiucosignature.pas<br />
unsigned.pas<br />
untMiscMthds.pas<br />
frmPNCSMainVistA.pas<br />
frmCMTSign.pas<br />
frmCMTUnsigned.pas</td>
<td>RPCBroker1</td>
<td>WorksheetIEN</td>
</tr>
<tr class="odd">
<td><span id="RANGE!A37" class="anchor"></span>DVBA CAPRI GET WORKSHEET LIST</td>
<td>PDFLST</td>
<td>DVBCTPDF</td>
<td>GLOBAL ARRAY</td>
<td>This RPC will return the list of CAPRI Worksheet from file 396.17</td>
<td>DVBIEN</td>
<td>Patient IEN from CAPRI<br />
RETURN PARAMETER DESCRIPTION:<br />
-1^ERROR MSG</td>
<td>TfrmMain.<br />
RefreshPDFList</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>PatientIEN</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GETCANCELREASON</td>
<td>CANRSN</td>
<td>DVBCANRS</td>
<td>ARRAY</td>
<td>This returns an array of active 2507 EXAM Cancellation Reasons. New active reasons added with Patch DVB*2.7*189. Old list of cancellation reasons set to inactive.</td>
<td>LIST</td>
<td>Returns a 1 when completed</td>
<td>TfrmExamDetails.<br />
btnCancelExamClick</td>
<td>ExamDetail.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GETCLAIMTYPE</td>
<td>GETCT</td>
<td>DVBACPR1</td>
<td>ARRAY</td>
<td>This RPC returns a list (array) of Claim Types associated with a valid 2507 Request</td>
<td>REQIEN</td>
<td>Returns all Claim Types associated to the valid 2507 Request</td>
<td>TfrmViewExam.<br />
GetClaimType</td>
<td>ViewExam.pas</td>
<td>RpcBroker1</td>
<td>RequestIEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GETCONTREMARKS</td>
<td>WPGET</td>
<td>DVBACREM</td>
<td>ARRAY</td>
<td>This gets the remarks sent to the contractor concerning the 2507 REQUEST in file 396.3. The remarks are stored in the word processing field #103 of the 2507 EXAM file 396.4.</td>
<td>DVBEIEN</td>
<td>Returns a 1 if remarks exist</td>
<td>TfrmManageReportsCCR.<br />
lstExamsRequestedChange</td>
<td>ManageReportsCCR.pas</td>
<td>RPCBroker1</td>
<td>[Exm]<br />
Exm is the IEN of one of the exams in the list of exams associated with an exam request.</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI GETSPCLCONSID</td>
<td>GETSC</td>
<td>DVBACPR1</td>
<td>ARRAY</td>
<td>This RPC returns an array of special considerations linked to a 2507 request.</td>
<td>2507 REQUEST IEN</td>
<td>NONE</td>
<td>TfrmViewExam.<br />
GetSpecialConsidations</td>
<td>ViewExam.pas</td>
<td>RpcBroker1</td>
<td>RequestIEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBA CAPRI GITHUB LOCATION</td>
<td>GITHUB</td>
<td>DVBCTXML</td>
<td>SINGLE VALUE</td>
<td>This RPC will return the GITHUB location for C&amp;P Worksheet templates</td>
<td>NONE</td>
<td>NONE</td>
<td>TGitHubIEPDDownload.<br />
GetGitHubRepositoryLocation</td>
<td>uIEPD.pas<br />
FirstCheckOfDayForIEPDDownloadBegin</td>
<td>RPCBroker1</td>
<td>NONE</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI IEPD DATA</td>
<td>SPIEPD</td>
<td>DVBCTXM2</td>
<td>SINGLE VALUE</td>
<td>This RPC will return to the CAPRI GUI the info needed for the SharePoint IEPD process.</td>
<td>NONE</td>
<td>NF Client^NF Tenant^NF Token^ NF SiteID URL^NF Drive ID URL^FileInfo URL^SP IEPD URL</td>
<td>uIEPD RetryIEPDDownload<br />
uIEPD GetCapriSPIEPDConnect</td>
<td>uIEPD.pas<br />
clsDBQPDFHandler.pas<br />
Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI INVALID CHAR LIST</td>
<td>INVALCHAR</td>
<td>DVBUTIL</td>
<td>ARRAY</td>
<td>RPC to provide list of invalid characters and replacement characters from DVBAB CAPRI INVALID CHARACTERS Parameter</td>
<td>NONE</td>
<td>Will return list with ASCII invalid character and replacement<br />
RETURN(1)=10^32<br />
RETURN(2)=128^63</td>
<td>TInvalidCharacterReplacement.<br />
GetInvalidCharactersFromVistA</td>
<td>clsDBQPDFHandler.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI LISTCLAIMTYPE</td>
<td>LSTCT</td>
<td>DVBACPR1</td>
<td>ARRAY</td>
<td>This RPC returns a list (array) of valid Claim Types</td>
<td>NONE</td>
<td>List of valid Claim Types</td>
<td>TfrmNewExam.<br />
LoadClaimTypeControlValues<br />
TfrmViewExam.<br />
LoadClaimTypeControlValues</td>
<td>NewExam.pas<br />
ViewExam.pas</td>
<td>RpcBroker1</td>
<td>No params</td>
</tr>
<tr class="even">
<td>DVBA CAPRI LISTINSUFRSN</td>
<td>LSTIR</td>
<td>DVBACPR1</td>
<td>ARRAY</td>
<td>This RPC returns a list (array) of valid Insufficient Reasons that can be linked to a 2507 exam.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmNewExam.<br />
btnSendRequestClick</td>
<td>NewExam.pas</td>
<td>RpcBroker1</td>
<td>No params</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI LISTSPCLCONSID</td>
<td>LSTSC</td>
<td>DVBACPR1</td>
<td>ARRAY</td>
<td>This RPC returns an array (listing) of valid special considerations that can be linked to a 2507 request.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmNewExam.<br />
LoadSpecialConsiderationControlValues<br />
TfrmViewExam.<br />
LoadSpecialConsiderationControlValues</td>
<td>NewExam.pas<br />
ViewExam.pas</td>
<td>RpcBroker1</td>
<td>No params</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRILOOKUPOPTSET" class="anchor"></span>DVBA CAPRI LOOKUP OPTSET</td>
<td>LOOKUP</td>
<td>DVBAARP</td>
<td>ARRAY</td>
<td>Verifies whether the AMIE Options exist<br />
Displays the schedule<br />
Displays the Task ID if it has one</td>
<td>DVBOPTLIST</td>
<td>AMIE Option name to Verify<br />
RETURN PARAMETER DESCRIPTION:<br />
AMIEOPTION^FLAG^MSG^SCHEDULE^TASKID<br />
FLAG 0 MEANS THE AMIE OPTION DOES NOT EXIST<br />
FLAG 1 MEANS THE AMIE OPTION DOES EXIST<br />
SCHEDULING DETAILS FOR THE AMIE OPTION<br />
TASK ID FOR THE AMIE OPTION</td>
<td>TPushUtilAsyncAMIEOptionsValidator.<br />
PrepareRPCData<br />
TPushUtilAsyncAMIEOptionsCompareServerState.<br />
PrepareRPCData</td>
<td>PushUtilAsyncAMIEOptionsValidator.pas<br />
PushUtilAsyncAMIEOptionsCompareServerState.pas</td>
<td>LocRPCConnect</td>
<td>Option List</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIMEDOPNFIELDS" class="anchor"></span>DVBA CAPRI MED OPN FIELDS</td>
<td>MEDOPFLDS </td>
<td>DVBUTIL</td>
<td>GLOBAL ARRAY</td>
<td>RPC to return values from parameter DVBAB CAPRI MED OPN FIELDS</td>
<td>NONE</td>
<td><p>Array containing remarks field and the fields to skip on the CMT DBQ  </p>
<p> Medical Opinion update. </p></td>
<td>TfrmMain.<br />
SetMedicalOpinionSummaryFields</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI NF DATA</td>
<td>NEWSFEED</td>
<td>DVBCTXM2</td>
<td>SINGLE VALUE</td>
<td>The RPC is returning the News Feed Client, Tenant and Token IDs, also the  Site ID, Drive ID and File Info URLs to the CAPRI GUI</td>
<td>NONE</td>
<td>NF Client^NF Tenant^NF Token^ NF SiteID URL^NF Drive ID URL^FileInfo URL</td>
<td>TfrmMain.<br />
actFileConnectExecute<br />
TformNews.<br />
FormShow</td>
<td>Main.pas<br />
News.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRINREHISTORY" class="anchor"></span>DVBA CAPRI NRE HISTORY</td>
<td>HISTORYRPC</td>
<td>DVBANRE</td>
<td>GLOBAL ARRAY</td>
<td>New Reports Export - Return export history<br />
IEN for the File 40.8 Division.<br />
Range Id, as passed by the RPC:DVBA CAPRI NRE STATIC</td>
<td>DVBDIVID<br />
DVBRANGEID</td>
<td>Array of history rows, each row a ^ delimited string processId ^ dateTimeString ^ description ^ hasFile ^ exportMark ^ runMethod<br />
-1 ^ &lt;error message&gt;<br />
For example:<br />
1000613^3250417.1221^Complete with 4 request(s) exported^1^new^AdHoc<br />
-1^Missing Division<br />
-1^Invalid Division<br />
-1^Range ID not specified/correct</td>
<td>TfrmNREConfig.GetExportsList</td>
<td>NewRequestsExportConfig.pas</td>
<td>RPCBroker1</td>
<td>Division<br />
DateRange</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRINRELOAD" class="anchor"></span>DVBA CAPRI NRE LOAD</td>
<td>LOADRPC</td>
<td>DVBANRE</td>
<td>SINGLE VALUE</td>
<td>Internal IEN for the division.  Pointer to file 40.8</td>
<td>DVBDIVID </td>
<td>Return division configuration<br />
Type &lt;Enter&gt; to continue or '^' to exit:<br />
divisionId^timeList^rowGroup^^^^^^^text summary^divisionName<br />
-1^&lt;error text&gt;<br />
For Example :<br />
1^0900,1000,1200,1400,1500^1^^^^^^^Next scheduled export Mar 10, 2025@10:00~0<br />
^ALBANY<br />
-1^Missing Division<br />
-1^Invalid Division</td>
<td>TfrmNREConfig.cbDivisionChange</td>
<td>NewRequestsExportConfig.pas</td>
<td>RPCBroker1</td>
<td>Division</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRINREMARK" class="anchor"></span>DVBA CAPRI NRE MARK</td>
<td>MARKRPC</td>
<td>DVBANRE</td>
<td>SINGLE VALUE</td>
<td>Mark status of an export<br />
Process Id of the export.  Taskman Name/Value storage DVBANREPROC(&lt;processId&gt;)</td>
<td>DVBPROCESSID<br />
DVBEXPORTMARK</td>
<td>0 (success)<br />
-1^Process ID not specified / not found<br />
-1^Invalid information mark</td>
<td>TfrmNREConfig.RunMarkRPC</td>
<td>NewRequestsExportConfig.pas</td>
<td>RPCBroker1</td>
<td>Export item<br />
MarkedText</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRINREOPEN" class="anchor"></span>DVBA CAPRI NRE OPEN</td>
<td>OPENRPC</td>
<td>DVBANRE</td>
<td>GLOBAL ARRAY</td>
<td>Return a file stream of an exported csv. Process Id of the export.  Taskman Name/Value storage DVBANREPROC(&lt;processId&gt;)</td>
<td>DVBPROCESSID</td>
<td>Return array of CSV rows forming the CSV file.</td>
<td>TfrmNREConfig.SaveAndOpenExportFile</td>
<td>NewRequestsExportConfig.pas</td>
<td>RPCBroker1</td>
<td>Export Item</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRINRERUNNOW" class="anchor"></span>DVBA CAPRI NRE RUNNOW</td>
<td>RUNNOWRPC</td>
<td>DVBANRE</td>
<td>SINGLE VALUE</td>
<td>Delimited string of entered config parameters divId ^ timeList ^ rowGroup<br />
> **NOTE:** This is the same string used for the NRE LOAD and NRE SAVE rpc</td>
<td>DVBSAVESTRING</td>
<td>Return ^ delimited string<br />
1. Status 0<br />
2. Notification text<br />
3. Next run text ~ outstanding count</td>
<td>TfrmNREConfig.btnRunNowClick</td>
<td>NewRequestsExportConfig.pas</td>
<td>RPCBroker1</td>
<td>Division</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRINRESAVE" class="anchor"></span>DVBA CAPRI NRE SAVE</td>
<td>SAVERPC</td>
<td>DVBANRE</td>
<td>SINGLE VALUE</td>
<td>Delimited string of entered config parameters divId ^ timeList ^ rowGroup<br />
> **NOTE:** This is the same string format returned by the NRE LOAD rpc</td>
<td>DVBSAVESTRING</td>
<td>Save status 0-1 status ^ notification text ^ next run text ~ outstanding count<br />
For Example:<br />
0^Configuration saved okay^Next scheduled export Mar 10, 2025@12:00~0<br />
-1^Invalid Division Id</td>
<td>TfrmNREConfig.btnSaveClick</td>
<td>NewRequestsExportConfig.pas</td>
<td>RPCBroker1</td>
<td>Division^RunTime^0</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRINRESTATIC" class="anchor"></span>DVBA CAPRI NRE STATIC</td>
<td>STATICRPC</td>
<td>DVBANRE</td>
<td>SINGLE VALUE</td>
<td>New Reports Export - Return meta data for the NRE screen</td>
<td>NONE</td>
<td>Returns static (meta) data string to draw the report screen<br />
Piece<br />
1 - Division List : &lt;divId&gt;~&lt;divName&gt;[, . . . ]<br />
2 - Date Range List : &lt;code&gt;~&lt;rangeName&gt;[, . . . ]<br />
3 - Bool - User Can View<br />
4 - Bool - User Can Edit<br />
5 - Bool - User Can RunNow<br />
6 - Bool - User Can Mark<br />
7 - Purge Interval Days</td>
<td>TfrmNREConfig.FormCreate</td>
<td>NewRequestsExportConfig.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRINRESUMMARY" class="anchor"></span>DVBA CAPRI NRE SUMMARY</td>
<td>SUMMARYRPC</td>
<td>DVBANRE</td>
<td>ARRAY</td>
<td>Returns a multi-line summary for all divisions</td>
<td>NONE</td>
<td>Array of text to display as the summary report Text Lines formated for direct display in mono-font in a text box</td>
<td>Tfrmreports.NRESummary</td>
<td>Reports.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIOPENACCESSCHECK" class="anchor"></span>DVBA CAPRI OPEN ACCESS CHECK</td>
<td>OPENCHECK</td>
<td>DVBCWKSHT</td>
<td>SINGLE VALUE</td>
<td>Given a worksheet IEN, it will determine if the user has permissions to open the worksheet for editing. Checking if the user holds the "DVBAB CPWM REVIEWER" Key, has FileMan access, or is listed as the Document Manager, Transcriber, or Worksheet Originator.</td>
<td>DVBBIEN</td>
<td>"-1^Missing Worksheet Number."<br />
"-1^No Worksheet data found."<br />
"-1^Missing Document Manager"<br />
"-1^Missing Transcriber"<br />
"-1^Missing Worksheet Originator"<br />
Return = 0 User can not open<br />
Return = 1 User can open</td>
<td>TfrmMain.IsAllowed2OpenExam</td>
<td>Main.pas<br />
pncsShow.pas<br />
tiucosignature.pas<br />
unsigned.pas<br />
frmCMTUnsigned.pas</td>
<td>RPCBroker1</td>
<td>IEN</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRIPARAMINQ" class="anchor"></span>DVBA CAPRI PARAM INQ</td>
<td>PARAMS</td>
<td>DVBCPUSH</td>
<td>ARRAY</td>
<td>This RPC will return all Parameters under the AMIE(DVBA) namespace. Multiple instances are separated by vertical bars ("|").</td>
<td>NONE</td>
<td>For each parameter in the DVB namespace:<br />
Parameter definition IEN^parameter name^&lt;instance 1 value&gt;|&lt;instance<br />
2 value&gt;|&lt;instance 3 value&gt;…</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
PopulateParameters</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="RANGE!A50" class="anchor"></span>DVBA CAPRI PARAM UPDATE</td>
<td>PARAMED</td>
<td>DVBCPUSH</td>
<td>SINGLE VALUE</td>
<td>This RPC allows CAPRI to update CAPRI Parameter values. If the parameter has multiples, then the multiple instance values are sent in the 3rd input parameter (DVBVAL) separated by vertical bars ("|").<br />
The RPC will delete all instances and replace them with the new values in DVBVAL. If a single null value is sent, then all instances are deleted.</td>
<td><p>PARAMETER</p>
<p>IEN VALUE</p></td>
<td>Return value will be one of the following:<br />
&lt;successful update count&gt;/&lt;total update count&gt; was(were) successful^&lt;unsuccessful instance and reason&gt;|&lt;unsuccessful instance and reason&gt;...<br />
<strong>OR</strong><br />
Missing parameter name<br />
<strong>OR</strong><br />
The entire parameter list has been deleted<br />
<strong>OR</strong><br />
An error message indicating why the parameter list was not deleted</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
UpdateParameters</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>Name, Value</td>
</tr>
<tr class="even">
<td>DVBA CAPRI PASCAL CHECK</td>
<td>PASCALCHK</td>
<td>DVBCTPDF</td>
<td>SINGLE VALUE</td>
<td>This is doing a check to confirm if the worksheet contains Pascal Script of CMT PDF exams.</td>
<td>DVBIEN</td>
<td>=-1^Error MSG<br />
P =contains Pascal<br />
C =contains CMT PDF</td>
<td>TfrmMain.<br />
PascalOrPDFWorksheetCheck</td>
<td>Main.pas<br />
fManTranVista.pas</td>
<td>RPCBroker1</td>
<td>WorksheetIEN</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI PDF LOGIC TOGGLE</td>
<td>DBQLOGIC</td>
<td>DVBUTIL</td>
<td>GLOBAL ARRAY</td>
<td>RPC will return Parameter results that list ALL, NONE, or the name(s) of the DBQs that need to skip the DBQ Conditional Logic.</td>
<td>NONE</td>
<td>Array will return at least one entry or the array of DBQ that need to skip the conditional logic.<br />
-1^Error Message<br />
RTN(1)="ALL"<br />
RTN(1)=0<br />
RTN(1)="Single DBQ_515"<br />
RTN(2)="Addtional DBQs_151"</td>
<td>TfrmMain.<br />
actFileConnectExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI PDF SIG FIELD NAMES</td>
<td>PDFSIGNM</td>
<td>DVBUTIL</td>
<td>GLOBAL ARRAY</td>
<td>Returns a list of all DBQ PDF field names to enable CMT PDF signing.</td>
<td>NONE</td>
<td>RET=&lt;total count&gt;<br />
RET(n)=n^&lt;signature field&gt;<br />
<strong>OR</strong><br />
-1^No data available<br />
<strong>OR</strong><br />
-1^Unable to retrieve data</td>
<td>TfrmMain.<br />
GetPDFSignatureFieldsFromVistA</td>
<td>Main.pas</td>
<td>RpcBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI PN TOGGLE</td>
<td>PNTOG</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>This RPC will return the value of the DVBAB CAPRI PN Toggle of 1 determines that TIU Notes text data should be populated in whole or 0 TIU Notes text data directing to review CAPRI for PDF text document.</td>
<td>NONE</td>
<td>1 sets TIU Note full value of the PDF, 0 sets TIU Note to abbreviated text to direct users to CAPRI to view PDF document.</td>
<td>Was called by<br />
TCMTSignForm.<br />
GenerateDBQProgressNote<br />
but this code is commented</td>
<td>RPC not used</td>
<td>None</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI PURGE MET</td>
<td>PURGEMET</td>
<td>DVBCPUSH</td>
<td>SINGLE VALUE</td>
<td>This RPC will allow the CAPRI GUI User with the correct security key to purge metrics data in File ^DVB(396.21).</td>
<td>DATE</td>
<td>Date for the data purge, all data from this date and before will be purged. For example, using May, a user enters May 9 as the purge date, data from May 1-May 9 will be purged. A response of 0 or 1 will be returned, 0 for unsuccessful and 1 for Successful</td>
<td>TfrmMain.<br />
actToolsPurgeTransmissionMetricsExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>DUZ, Date</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRISAVEDBQXML" class="anchor"></span>DVBA CAPRI SAVE DBQ XML</td>
<td>FAILXML</td>
<td>DVBCTXML</td>
<td>GLOBAL ARRAY</td>
<td>This RPC is being used by CAPRI GUI to retrieve the XML document stored in File ^DVB(396.17).</td>
<td>DVBIEN<br />
DVBCNT<br />
DVBXML<br />
DVBNAME<br />
DVBSTAT<br />
DVBRESP</td>
<td>PARAMETER TYPE: LITERAL REQUIRED: YES<br />
SEQUENCE NUMBER: 1<br />
DESCRIPTION:<br />
IEN of the requested XML Document<br />
INPUT PARAMETER: DVBCT PARAMETER TYPE: LITERAL<br />
REQUIRED: YES<br />
SEQUENCE NUMBER: 2<br />
DESCRIPTION:<br />
The entry number of which XML Document within the record</td>
<td>TDBQXmlRPCHandler.<br />
SaveDBQXml</td>
<td>tuisign.pas<br />
frmCMTSign.pas</td>
<td>RPCBroker1</td>
<td>[0] ExamName or templateIEN<br />
[1] XMLIEN<br />
[2] XML (text)<br />
[3] IsTransComplete<br />
[4] ResultCodeStr; // Response<br />
[5] inWorksheetIEN</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRISAVEEXAMPDF" class="anchor"></span>DVBA CAPRI SAVE EXAM PDF</td>
<td>PDFSAVE</td>
<td>DVBCTPDF</td>
<td>SINGLE VALUE</td>
<td>Used to save PDF details for each exam in ^DVB(396.17,*WorksheetIEN*,15,*Seq*</td>
<td>DVBIEN DVBSEQ<br />
DVBEXAMNAME DVBPDFDATA<br />
DVBTABIO DVBSMSG DVBVER</td>
<td>TABIO number to be sent back for proper display of data.</td>
<td>TCAPRIDbqPdf.<br />
SavePDFToVistA</td>
<td>frmPNCSMainVistA.pas</td>
<td>RPCBroker1</td>
<td>WorkSheet_IEN, SequenceNumber,<br />
ExamName,<br />
PDF data,<br />
Tab Order</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRISAVEREVIEWDATA" class="anchor"></span>DVBA CAPRI SAVE REVIEW DATA</td>
<td>REVIEWSAVE</td>
<td>DVBSIGN</td>
<td>SINGLE VALUE</td>
<td>CAPRI GUI will call RPC to save details for each review action</td>
<td>DVBIEN<br />
DVBTYP<br />
DVBREVCMT</td>
<td>-1^No Worksheet IEN sent<br />
-1^Invalid Worksheet IEN<br />
-1^Invalid Status<br />
-1^Invalid Comments<br />
-1^Invalid Trainee DUZ<br />
-1^Invalid Signer DUZ<br />
-1^New version not saved<br />
-1^Review Comments not Saved<br />
-1^Trainee DUZ and DIV not Saved<br />
-1^Worksheet not updated<br />
1^Review Details saved and Worksheet Updated</td>
<td>TPNCSMainVistA.<br />
SaveTraineeReview<br />
TPNCSMainVistA.<br />
SaveReviewStatus<br />
TPNCSMainVistA.<br />
SaveAwaitSignature</td>
<td>frmPNCSMainVistA.pas</td>
<td>RPCBroker1</td>
<td>WorksheetIEN, Status</td>
</tr>
<tr class="even">
<td>DVBA CAPRI SAVE SIGNER</td>
<td>SAVE<br />
SIGN</td>
<td>DVBSIGN</td>
<td>SINGLE VALUE</td>
<td>Saves Signer DUZ, CoSigner Required Flag, CoSigner DUZ, and updates<br />
Date/Time for worksheet.</td>
<td>DVBIEN</td>
<td>"2^Signed Ready for CoSignature"<br />
"1^Signed Ready for Transmission"<br />
"-1^Details not Saved"</td>
<td>untMiscMthds<br />
SaveSignerCosigner</td>
<td>frmCMTSign.pas</td>
<td>RpcBroker1</td>
<td>WorksheetIEN, CosignerIEN</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI SECURITY TOGGLE</td>
<td>SECTOG</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>This RPC is returning data from the DVBAB CAPRI SECURITY TOGGLE parameter. This value tells the CAPRI GUI which security field(s) must be validated to allow GUI access.</td>
<td>NONE</td>
<td>Value for toggle in the CAPRI GUI:<br />
1 = Additional SSN Check<br />
2 = Additional SecID Check<br />
3 = Additional SSN and SecID Check<br />
4 = No additional security checks</td>
<td>TfrmMain.<br />
SetUserSecurityOption</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI SET METRICS</td>
<td>EFOLDMET</td>
<td>DVBCPUSH</td>
<td>SINGLE VALUE</td>
<td>This RPC will create an entry ^DVB(396.21) for EFolder Transmission metrics reporting.</td>
<td>DVBAUTH</td>
<td>Authorized User IEN</td>
<td>TClinDocTransmissionMetrics.<br />
LogTransmissionMetrics</td>
<td>public function LogTransmissionMetrics not called</td>
<td>RPCBroker1</td>
<td>Sender_IEN, Patient_IEN, Transmission method (PIV or PROXY), Status (1 or 0), Documents sent List</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI SETCLAIMTYPE</td>
<td>SETCT</td>
<td>DVBACPR1</td>
<td>ARRAY</td>
<td>This RPC returns the status of Claim Types passed to be set to a valid 2507 Request</td>
<td>ARRACT</td>
<td>Returns status of Claim Type sets</td>
<td>TfrmNewExam.<br />
SetClaimType<br />
TfrmViewExam.<br />
SetClaimType</td>
<td>NewExam.pas<br />
ViewExam.pas</td>
<td>RpcBroker1</td>
<td>RequestIEN<br />
PType:= literal;<br />
<br />
cbClaimType.Items[cbClaimType.ItemIndex]<br />
PType := List</td>
</tr>
<tr class="even">
<td>DVBA CAPRI SETCONTREMARKS</td>
<td>WPSET</td>
<td>DVBACREM</td>
<td>LITERAL</td>
<td>The RPC sets remarks sent to the contractor into the new word processing field #103 of the 2507 EXAM file 396.4. The 2507 EXAMs are connected to the 2507 REQUEST file via a pointer.</td>
<td>EIEN</td>
<td>returns a 1 when set</td>
<td>DVBA CAPRI SETCONTREMARKS</td>
<td>frmContractedExamNewResend.pas:<br />
function TExntdCntrctdBaseFormNewRsnd.SendCntrctrRemarksToVista</td>
<td>RPCBroker1</td>
<td>[reqNmbr, ienslst], Lines req Nmbr is the IEN of exam request. ienslst is a string list which contains the iens of the selected exams. Lines contains the contractor request remarks.</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI SETSPCLCONSID</td>
<td>SETSC</td>
<td>DVBCAPR1</td>
<td>SINGLE VALUE</td>
<td>This RPC sets the passed-in special considerations and links them to the passed-in 2507 request</td>
<td>2507 REQUEST IEN<br />
SPECIAL CONSIDERATION LIST</td>
<td>NONE</td>
<td>TfrmNewExam.<br />
SetSpecialConsidations<br />
TfrmViewExam.<br />
SetSpecialConsidations</td>
<td>NewExam.pas<br />
ViewExam.pas</td>
<td>RpcBroker1</td>
<td>RequestIEN;<br />
PType := literal;<br />
<br />
chklstSpecialConsiderations.Items[i];<br />
PType := list;</td>
</tr>
<tr class="even">
<td>DVBA CAPRI SKIP CHILD RESET</td>
<td>CSKIPLOGIC</td>
<td>DVBUTIL</td>
<td>ARRAY</td>
<td>Returns list of parameters in DVBAB CAPRI SKIP CHILD RESET</td>
<td>NONE</td>
<td>RTN(0)=Count<br />
RTN(1)=Parent Field!Value</td>
<td>TfrmMain.<br />
SetConditionalLogicSkipChildResetAndSkipParentChild</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>NO PARAMS</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRISKIPPARENTCHILD" class="anchor"></span>DVBA CAPRI SKIP PARENTCHILD</td>
<td>PCHILDLOGIC</td>
<td>DVBUTIL</td>
<td>ARRAY</td>
<td>Returns list of parameters in DVBAB CAPRI SKIP PARENTCHILD</td>
<td>NONE</td>
<td>RTN(0)=Count<br />
RTN(1)=PARENT!CHILD</td>
<td>TfrmMain.<br />
SetConditionalLogicSkipChildResetAndSkipParentChild</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>NO PARAMS</td>
</tr>
<tr class="even">
<td>DVBA CAPRI SPEC ADD</td>
<td> </td>
<td>DVBCPUSH</td>
<td>SINGLE VALUE</td>
<td>This RPC is used by the CAPRI PUSH Utility Application to allow users to add new Special Considerations used by the 2507 process.</td>
<td>DVBNAME</td>
<td>The name of the Special Consideration to be added to file DVB(396.25).</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
AddNewSpecialConsideration</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>Special Consideration Name</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI SPEC INACTIVE</td>
<td>LISTSC</td>
<td>DVBCPUSH</td>
<td>ARRAY</td>
<td>This RPC will return to the CAPRI Push application the list of inactive Special Considerations.</td>
<td>NONE</td>
<td>This is the array of Inactive Special Considerations</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
PopulateInactiveSpecialConsiderations</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>None</td>
</tr>
<tr class="even">
<td>DVBA CAPRI SPEC STATUS</td>
<td>SPECDIS</td>
<td>DVBCPUSH</td>
<td>SINGLE VALUE</td>
<td>This RPC is used by the CAPRI PUSH Utility Application to allow users to disable or enable Special Considerations used by the 2507 process.</td>
<td>DVBIEN</td>
<td>Returns 1 for successful and 0 for unsuccessful</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
SpecialConsiderationStatusSet</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>IEN; PType := literal<br />
Status; PType := literal</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRISTATUSCOUNT" class="anchor"></span>DVBA CAPRI STATUS COUNT</td>
<td>STATCNT</td>
<td>DVBSIGN</td>
<td>SINGLE VALUE</td>
<td>This RPC will return the count for worksheets with the following statuses:<br />
A=Awaiting signature<br />
D=Draft/Not ready<br />
O=Outdataed template<br />
P=Review pending<br />
S=Sent back</td>
<td>NONE</td>
<td>Awaiting signature count^Draft/not ready count^Outdated template count^Review pending count^Sent back count</td>
<td>TfrmAlerts.<br />
GetCMTAlertCounts</td>
<td>Alerts.pas</td>
<td>RpcBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRISUPPORTMESSAGE" class="anchor"></span>DVBA CAPRI SUPPORT MESSAGE</td>
<td>HELPINFO</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>Returns support desk phone number to display to CAPRI user when they need to submit a support ticket.</td>
<td>NONE</td>
<td>String containing support desk phone number.</td>
<td>CAPRISupport<br />
SetSupportTicketPrompt</td>
<td>Main.pas</td>
<td>RpcBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRITEMPDEFLIST" class="anchor"></span>DVBA CAPRI TEMP DEF LIST</td>
<td>LISTTEMP</td>
<td>DVBCPSH2</td>
<td>ARRAY</td>
<td>This remote procedure for the DBQ Push Utility will filter the CAPRI Template Definitions in the EDIT LOCAL tab in a returned array sorted</td>
<td>DVBFILT<br />
DVBSORT</td>
<td>List of CAPRI Template Definitions filtered and sorted with the provided parameters<br />
Format: CAPRITemplateName^CAPRITemplateFileNumber<br />
Example: DVBRET(0)="AID AND ATTENDANCE OR HOUSEBOUND<br />
EXAMINATION~V18_3_XE10^2292"<br />
DVBRET(1)="DBQ ADMIN ADDENDUM OR CLARIFICATIONS~V17_3^2273"<br />
DVBRET(2)="DBQ ADMIN BVA MEDICAL OPINION~V17_3^2274"</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
PopulateLocalDBQTemplates</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>FilterType, SortType</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRITRAINEEDOCMANAGER" class="anchor"></span>DVBA CAPRI TRAINEE DOC MANAGER</td>
<td>DOCMAN</td>
<td>DVBSIGN</td>
<td>SINGLE VALUE*</td>
<td>RPC Used only to update Document Manager Field to Trainee before Signature Validation*</td>
<td>DVBIEN</td>
<td>Will return 1 if update processed<br />
or<br />
-1^No Worksheet IEN sent<br />
-1^Invalid Worksheet IEN<br />
-1^No Update</td>
<td>TCMTSignForm.<br />
btnSignClick</td>
<td>frmCMTSign.pas</td>
<td>RpcBroker1</td>
<td>WorksheetIEN</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRITRAINEESIGNATURE" class="anchor"></span>DVBA CAPRI TRAINEE SIGNATURE</td>
<td>TRAINSIG</td>
<td>DVBSIGN</td>
<td>SINGLE VALUE</td>
<td>Returns the DUZ and DIV for the Trainee that filled out the Worksheet.</td>
<td>DVBIEN</td>
<td>Trainee DUZ^DIV or -1^No Worksheet IEN sent<br />
-1^Invalid Worksheet IEN<br />
-1^No details found</td>
<td>TCMTSignForm.<br />
AutoSignDBQExams</td>
<td>frmCMTSign.pas</td>
<td>RpcBroker1</td>
<td>WorksheetIEN</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRIUNCOSIGNCOUNT" class="anchor"></span>DVBA CAPRI UNCOSIGN COUNT</td>
<td>ALERTCNT</td>
<td>DVBSIGN</td>
<td>SINGLE VALUE</td>
<td>To return count of DBQs that require Cosignature</td>
<td>NONE</td>
<td>0 if none are found, otherwise the number that require CoSignature</td>
<td>TfrmTIUCosign.<br />
GetCosignatureAlertsCount</td>
<td>Tiucosignature.pas</td>
<td>RpcBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIUNCOSIGNEDINFO" class="anchor"></span>DVBA CAPRI UNCOSIGNED INFO</td>
<td>UNCSINFO</td>
<td>DVBSIGN</td>
<td>GLOBAL ARRAY</td>
<td>Returns an array of info regarding all uncosigned worksheets.</td>
<td>NONE</td>
<td>Patient IEN^Patient name^Date last updated^"UNCOSIGNED &lt;TIU document name&gt;<br />
available for COSIGNATURE" or "UNCOSIGNED NON-&lt;TIU document name&gt;<br />
available for COSIGNATURE"^Worksheet IEN^TIU document number<br />
<strong>OR</strong><br />
-1^No data available</td>
<td>TfrmTIUCosign.<br />
GetCosignatureAlertsInfo</td>
<td>Tiucosignature.pas</td>
<td>RpcBroker1</td>
<td>None</td>
</tr>
<tr class="even">
<td><span id="DVBACAPRIUNLOCKEXAM" class="anchor"></span>DVBA CAPRI UNLOCK EXAM</td>
<td>LOCKUNLOCK</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>RPC is used by CAPRI GUI to unlock an exam being once a user closes the exam.</td>
<td>DVBIEN</td>
<td>Return is either a 1 for success or "-1^^Record currently locked by" and user info stored in Field 17 of File 396.17.</td>
<td>CAPRISupport<br />
UnlockWorksheet<br />
TfrmMain.<br />
IsAuthorizedToDeleteWorksheet</td>
<td>Main.pas<br />
frmPNCSMainVistA.pas<br />
frmCMTUnsigned.pas<br />
<br />
unsigned.pas</td>
<td>RPCBroker1</td>
<td>WorksheetIEN and 'U' (for unlock)</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIUPDATEDBQTRANSTAT" class="anchor"></span>DVBA CAPRI UPDATE DBQ TRANSTAT</td>
<td>STATUS</td>
<td>DVBCTXML</td>
<td>SINGLE VALUE</td>
<td>This RPC will update the DBQ transmission status in File ^DVB(396.17)</td>
<td>Template IEN<br />
STATUS<br />
RESULT RESPONSE</td>
<td>NONE</td>
<td>TDBQXmlRPCHandler.<br />
UpdateDBQStatus</td>
<td>Main.pas<br />
tiusign.pas<br />
fManTransVista.pas<br />
frmCMTSign.pas</td>
<td>RPCBroker1</td>
<td>TemplateIEN, XMLIEN, Status, ResultCode</td>
</tr>
<tr class="even">
<td><span id="DVBABCAPRIWORDWRAP" class="anchor"></span>DVBA CAPRI WORD WRAP</td>
<td>WORDWRAP</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>Max length of free text before word wrap. </td>
<td>NONE</td>
<td>Returns max length of free text before word wrap. Default=250 </td>
<td>TfrmMain.<br />
SetProgressNoteWordWrapLength</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>NONE</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIWORKSHEETBYEXAM" class="anchor"></span>DVBA CAPRI WORKSHEET BY EXAM</td>
<td>WKSHBYEXAM</td>
<td>DVBUTIL</td>
<td>SINGLE VALUE</td>
<td>NONE</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmExamDetails.<br />
btnViewPDFResultsClick</td>
<td>examdet.pas</td>
<td>RPCBroker1</td>
<td>Exam Reference #</td>
</tr>
<tr class="even">
<td>DVBA CAPRI WORKSHEET NAME ED</td>
<td>EXEDIT</td>
<td>DVBCPSH1</td>
<td>SINGLE VALUE</td>
<td>This RPC will allow the edit of an AMIE Worksheet Name in File DVB(396.6)</td>
<td>DVBIEN</td>
<td>IEN of AMIE Exam Name to be edited</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
updateWorksheetName</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>IEN, NAME; Ptype := literal</td>
</tr>
<tr class="odd">
<td>DVBA CAPRI WORKSHEET STAT LIST</td>
<td>LISTSTAT</td>
<td>DVBCPSH1</td>
<td>GLOBAL ARRAY</td>
<td>This RPC will return the list of AMIE Worksheet Exams according to status.</td>
<td>DVBSTAT</td>
<td>A=Active, I=Inactive</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
AIMEWorksheetStatusList</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>Status; Ptype := literal</td>
</tr>
<tr class="even">
<td>DVBA CAPRI WORKSHEET STATUS</td>
<td>EXINACT</td>
<td>DVBCPSH1</td>
<td>SINGLE VALUE</td>
<td>This RPC will set the status of an entry in File 396.6 to active or inactive</td>
<td>DVBIEN<br />
DVBSTAT</td>
<td>NONE</td>
<td>TfrmCAPRITmplteTrnsfrUtilMain.<br />
updateWorksheetStatus</td>
<td>CAPRITmplteTrnsfrUtil.pas</td>
<td>CCOWRPCBrkrRemote</td>
<td>IEN; PType := literal<br />
Status; PType := literal</td>
</tr>
<tr class="odd">
<td><span id="DVBACAPRIWORKSHEETUPDATE" class="anchor"></span>DVBA CAPRI WORKSHEET UPDATE</td>
<td>WKSHTSAVE</td>
<td>DVBWKSHT</td>
<td>ARRAY</td>
<td>Allows updates to Author, Transcriber, DBQ Referral, New Flag, Green Flag, ang ExClamation Flag.</td>
<td>DVBIEN<br />
DVBAUTH<br />
DVBTRAN<br />
DVBF19<br />
DVBF20<br />
DVBF21</td>
<td>Return will be an array for positive updates:<br />
DVBRTN(0)="1^Updated Record Date/Time"<br />
DVBRTN(1)="1^Author has been updated"<br />
DVBRTN(2)="1^Transcriber has been updated"<br />
DVBRTN(3)="1^DBQ Referral has been updated"<br />
DVBRTN(4)="1^New Flag has been updated"<br />
DVBRTN(5)="-1^Invalid Format"<br />
DVBRTN(6)="1^Exclamation Flag has been updated"</td>
<td>TfrmMain.<br />
SaveWorksheetHeader</td>
<td>Main.pas<br />
unsigned.pas<br />
frmPNCSMainVistA.pas<br />
frmCMTUnsigned.pas</td>
<td>RPCBroker</td>
<td>WorksheetIEN,<br />
Author,<br />
Transcriber,<br />
DBQRefferal,<br />
NFlag,<br />
GFlag,<br />
EFlag,</td>
</tr>
<tr class="even">
<td>DVBA CHECK PATCH</td>
<td>CHEC</td>
<td>DVBAB1B</td>
<td>SINGLE VALUE</td>
<td>This RPC is a wrapper for the supported $$PATCH^XPDUTL API to determine whether a given patch is installed or not.</td>
<td>DVBPATCH</td>
<td>Returns "1^Patch Is Installed" on success; otherwise returns "0^Patch Is Not Installed".</td>
<td>CAPRISupport<br />
IsPatchInstalled<br />
TfrmReRouteRequest.<br />
btnTestGuestLoginClick<br />
TfrmReRouteRequest.<br />
btnTestRemoteRPCClick</td>
<td>CAPRISupport.pas<br />
enterpt.pas<br />
examdet.pas<br />
main.pas<br />
managereports.pas<br />
newexam.pas<br />
patientlist.pas<br />
patientlistrestricted.pas<br />
pncsmain.pas<br />
reports.pas<br />
tiusign.pas<br />
uncosignedutility.pas<br />
viewaddress.pas<br />
viewexam.pas<br />
VlerDasClaim.pas<br />
frmPNCSMainVistA.pas<br />
frmCMTSign.pas<br />
uTIU.pas</td>
<td>RPCBroker1</td>
<td>Patch</td>
</tr>
<tr class="odd">
<td>DVBA MVI GET CORRESPONDING IDS</td>
<td>GETIDS</td>
<td>DVBAMVI2</td>
<td>LITERAL</td>
<td>This is the Integration Control Number (ICN) used to identify the patient that is selected from the MVI SEARCH PERSON web service results.<br />
Format: "1008523099V750710^NI^200M^USVHA^"</td>
<td>SOURCE ID</td>
<td>List of VAMC treating facilities associated with the passed identifier. Each line contains INSTITUTION (#4) file IEN, station name, and station number delimited by a caret ("^"). The first entry in the list contains the total number of stations returned. Format: instutionIEN^stationName^stationNumber<br />
Example:<br />
DVBOUT(0)=2<br />
DVBOUT(1)="516^BAY PINES VA HCS^516"<br />
DVBOUT(2)="523^BOSTON HCS VAMC^523"</td>
<td>TfrmMVIEnterpriseSearch.<br />
GetTreatingFacilities<br />
TfrmMVIEnterpriseSearch.<br />
btnGetTreatingFacilitiesClick</td>
<td>frmMVISearch.pas</td>
<td>RPCBroker1</td>
<td>MVISearchID</td>
</tr>
<tr class="even">
<td>DVBA MVI SEARCH PERSON</td>
<td>FINDPAT</td>
<td>DVBAMVI1</td>
<td>ARRAY</td>
<td>This remote procedure passes the delimited person traits to the MVI SEARCH PERSON web service and returns the results of the search.</td>
<td>PERSON TRAITS<br />
INITIAL QUANTITY<br />
NAME FORMAT</td>
<td>This RPC returns the MINIMUM version parameter and also checks if the GUI matches the MINIMUM version build or the PREVIOUS version build.<br />
If the GUI is the PREVIOUS version and falls outside of the grace period or the GUI is not the MINIMUM or PREVIOUS build this RPC will return the grace period date of January 1, 1980 enforcing GUI version control to recognize this version is no longer allowed sign on.<br />
The zero-array node returns the caret-delimited record count and search status results.<br />
Piece 1: Returned record count<br />
Piece 2: OK or error message text<br />
Array node 1 starts the list of caret-delimited matching patient records.<br />
Piece 1: FULLNAME<br />
Piece 2: SSN (9 digits)<br />
Piece 3: DATE OF BIRTH (external format)<br />
Pieces 4-7 contain the MVI ID components<br />
Piece 4: ID<br />
Piece 5: IdType<br />
Piece 6: Assigning Location<br />
Piece 7: Assigning Issuer</td>
<td>TfrmMVIEnterpriseSearch.<br />
btnMVISearchClick<br />
TfrmMVIEnterpriseSearch.<br />
btnSearchClick<br />
Tfrmhiaverifypatientlist.<br />
BitBtnhiaVerifyClick</td>
<td>frmMVISearch.pas<br />
HIAVerifyPatient.pas</td>
<td>RPCBroker1</td>
<td>SearchString<br />
PType:= literal;<br />
<br />
SearchResultNumParam<br />
PType:= literal;</td>
</tr>
<tr class="odd">
<td>DVBAB 2507 PENDING REPORT</td>
<td>STRT</td>
<td>DVBAB6</td>
<td>GLOBAL ARRAY</td>
<td>Generates a report based on the status of 2507 requests.</td>
<td>DVBCSORT<br />
RSTAT<br />
ERDAYS<br />
OLDAYS<br />
ELTYP</td>
<td>MSG is returned.</td>
<td>DVBAB 2507 PENDING REPORT</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="even">
<td>DVBAB 8861 NOTIFICATIONS</td>
<td>ENTER</td>
<td>DVBANTFY</td>
<td>SINGLE VALUE</td>
<td>This will perform MailMan notifications for Form 8861 Requests based on the status of the request.</td>
<td>IEN<br />
STAT</td>
<td>The RPC returns either a success or failure to send the MailMan notification, either 0 or 1.</td>
<td>TVocRehab.<br />
SendMailManMessage</td>
<td>VocRehabAssnConsults.pas<br />
VocRehabCancelExam.pas<br />
VocRehabMedicalRequest.pas</td>
<td>RPCBroker1</td>
<td>Value := frmVRMedicalRequest.SelectedMedicalRequestIEN,<br />
PType := literal<br />
<br />
Value := MsgType<br />
PType := literal</td>
</tr>
<tr class="odd">
<td>DVBAB AMIS REPORT</td>
<td>STRT</td>
<td>DVBAB3</td>
<td>ARRAY</td>
<td>Returns an AMIS report for specified search criteria.</td>
<td>BDATE<br />
EDATE</td>
<td>NONE</td>
<td>TfrmRemoteReports.<br />
AMIS290<br />
Tfrmreports.<br />
GetAMIS290Report</td>
<td>RemoteReports.pas<br />
Reports.pas</td>
<td>RPCBroker1</td>
<td>Value := DateTimePickerStart.Date;<br />
PType := literal;<br />
<br />
Value := DateTimePickerStop.Date;<br />
PType := literal;<br />
<br />
Value := aRegionalOffice + '^' + Piece(DivisionList.Strings[i], '^', 2);<br />
PType := literal;<br />
<br />
Value := 'N'; // Just say NO to mailman<br />
PType := literal;<br />
<br />
Value := AuthorIEN;<br />
PType := literal;<br />
<br />
Value:=PriorityFilter:<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBAB APPOINTMENT LIST</td>
<td>DPA</td>
<td>DVBAB1B</td>
<td>GLOBAL ARRAY</td>
<td>Returns a list of past, future or all appointments.</td>
<td>VAL1<br />
VAL2</td>
<td>Returns LIST of appointments for the patient based on value of CHOICE.</td>
<td>TfrmMain.<br />
btnPastClick<br />
TfrmMain.<br />
btnAllClick<br />
TfrmMain.<br />
btnFutureClick</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := PatientIEN;<br />
PType := literal;<br />
<br />
Value := 'P'; //A=All appt. F=Future appt. P=Past appt.<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB CAPRI ALLOW CLINDOCS</td>
<td>EFOLDER</td>
<td>DVBCENQ</td>
<td>SINGLE VALUE</td>
<td>This CAPRI RPC will validate if the user is a provider, VBA User, VHA User, with the required title to allow for sending of clinical documents to the eFolder</td>
<td>DFN</td>
<td>Returns 0 if not allowed, 1 if allowed and/or -1^error if an error is encountered.</td>
<td>TfrmMain.<br />
CanUserSendClinicalDocuments</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Authorien</td>
</tr>
<tr class="even">
<td>DVBAB CAPRI EFOLDER LOCATION</td>
<td>LOCATION</td>
<td>DVBCENQ</td>
<td>SINGLE VALUE</td>
<td>Returns the location to be used for Clinical Docs to be sent from CAPRI GUI</td>
<td>NONE</td>
<td>Returns the location to be used for Clinical Docs to be sent from CAPRI GUI</td>
<td>TfrmMain.<br />
CanUserSendClinicalDocuments</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>No params</td>
</tr>
<tr class="odd">
<td>DVBAB CAPRI PROVIDER</td>
<td>PROVIDER</td>
<td>DVBCENQ</td>
<td>SINGLE VALUE</td>
<td>APRI GUI verifies that the user is a Provider</td>
<td>DFN</td>
<td>RETURNS 0 IF NOT ALLOWED, 1 IF ALLOWED</td>
<td>TfrmMain.<br />
UserHasProviderKey</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Authorien</td>
</tr>
<tr class="even">
<td>DVBAB CCOW</td>
<td>CCOW</td>
<td>DVBABFRM</td>
<td>SINGLE VALUE</td>
<td>This remote procedure encapsulates the supported calls $$SITE^VASITE and $$PROD^XUPROD.<br />
Parameter TYPE 1 = Pass back local station number ($$SITE^VASITE) TYPE 2 = Pass back whether production account or not ($$PROD^XUPROD)</td>
<td>INFOTYPE<br />
<br />
TYPE</td>
<td>NONE</td>
<td>TfrmMain.<br />
actFileConnectExecute<br />
TfrmMain.<br />
GetDivision<br />
<br />
untBrkrMthds<br />
IsProductionAccount</td>
<td>Main.pas<br />
<br />
untBrkrMthds.pas</td>
<td>RPCBroker1,<br />
<br />
Brkr</td>
<td>Value := '1';<br />
PType := literal;<br />
<br />
Value := '2';<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB CHECK CREDENTIALS</td>
<td>CHKCRED</td>
<td>DVBAB1</td>
<td>SINGLE VALUE</td>
<td>Verifies the user has been granted access to AMIE II/CAPRI</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
btnEditAddressClick<br />
TfrmMain.<br />
btnAddExamClick<br />
TfrmMain.<br />
btnAddRequestClick<br />
TfrmMain.<br />
btnViewExamClick<br />
TfrmMain.<br />
btnAdd7131Click<br />
TfrmMain.<br />
btnView7131Click<br />
TfrmMain.<br />
btnGenerate7131ReportClick<br />
TfrmMain.<br />
btnGenerateReportClick<br />
<br />
TfrmAddress.<br />
ButtonEditAddressClick<br />
<br />
TfrmViewExam.<br />
btnInsufficientExamClick</td>
<td>Main.pas<br />
viewaddress.pas<br />
viewexam.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="even">
<td>DVBAB DATETIME</td>
<td>DTTM</td>
<td>DVBAB1</td>
<td>SINGLE VALUE</td>
<td>Returns the current date/time from VistA</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
GetServerDateTime<br />
<br />
Tfrmreports.<br />
OneItemPerPagePrint<br />
<br />
Tfrmreports.<br />
NormalPrint<br />
<br />
TFormTIUDisplay.<br />
Print<br />
<br />
TSplitExam.<br />
GetServerDateTime</td>
<td>Main.pas<br />
Reports.pas<br />
tiudisplayunit.pas<br />
SplitExamInfo.pas</td>
<td>RPCBroker1</td>
<td>No Parms</td>
</tr>
<tr class="odd">
<td>DVBAB DIVISION</td>
<td>DIVISION</td>
<td>DVBAB1</td>
<td>SINGLE VALUE</td>
<td>Returns list of divisions</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
actFileConnectExecute</td>
<td>Main.pas</td>
<td>RpcBroker1</td>
<td>No Params</td>
</tr>
<tr class="even">
<td>DVBAB EXAMS BY DATE</td>
<td>EXAMBYDT</td>
<td>DVBABEBD</td>
<td>GLOBAL ARRAY</td>
<td>Provides a report by date range of all AMIE/CAPRI exam requests.</td>
<td>BEGDT<br />
<br />
ENDT</td>
<td>NONE</td>
<td>Tfrmreports.<br />
Button9Click</td>
<td>Report.pas</td>
<td>RPCBroker1</td>
<td>Value := FMToDateConvert(FormatDateTime('mm/dd/yyyy', DateTimePicker1.DateTime));<br />
PType := literal<br />
<br />
Value := FMToDateConvert(FormatDateTime('mm/dd/yyyy', DateTimePicker2.DateTime))<br />
PType := literal</td>
</tr>
<tr class="odd">
<td>DVBAB FETCH 1U4N</td>
<td>U1N4</td>
<td>DVBABFRM</td>
<td>GLOBAL ARRAY</td>
<td>Retrieve the 1u4n field for the list of patient IENS provided as the only argument. Each IEN will be sent back with field .0905 appended after a caret.</td>
<td>ARR</td>
<td>List of Patient IENs in piece 1,followed by 1U4N in piece 2</td>
<td>TUnsignedView.<br />
FormatFormList1</td>
<td>unsigned.pas</td>
<td>RPCBroker1</td>
<td>Mult[IntToStr(i + 1)] := FMListBoxIPR1.GetSelectedRecord.IEN;<br />
PType := list;</td>
</tr>
<tr class="even">
<td>DVBAB FIND DUPS</td>
<td>DUP</td>
<td>DVBAB84</td>
<td>GLOBAL ARRAY</td>
<td>Find potential duplicates within the PATIENT File (#2) At least one of NAM, DOB, or SSN must be passed Possible matches are "better" when more than one of these is passed</td>
<td>NAM<br />
DOB<br />
SSN</td>
<td>BYREF - Passed by reference, will contain name of a TMP Global housing the results Subscript 0: -1^ERROR_MESSAGE (in the event of an error)<br />
OR<br />
Subscript 0: Number of potential matches found (if no errors)<br />
Subscript 1-K: Patient's matching ALL 3 of NAM, DOB, SSN have a weighting of 3 (see Note)<br />
Subscript K+1-L: Patient's matching ANY 2 of NAM, DOB, SSN have a weighting of 2 (see Note)<br />
Subscript L+1-M: Patient's matching ONLY 1 of NAM, DOB, SSN have a weighting of 1 (see Note)<br />
^TMP(1-M) = DFN^ZERO_NODE where DFN is the Patient IEN ZERO_NODE is the data from ^ DPT(DFN,0)<br />
<br />
> **NOTE:** Potential matches within a weighting (if any) will be sorted by Patient Name</td>
<td>TfrmEnterPt.<br />
Button8Click<br />
<br />
TfrmEnterPtSimple.<br />
Button8Click<br />
<br />
TfrmEnterPt140.<br />
Button8Click<br />
<br />
TfrmEnterPtSimple140.<br />
Button8Click</td>
<td>EnterPt.pas<br />
<br />
entersimple.pas<br />
<br />
enterpt140.pas<br />
<br />
enterptsimple140.pas</td>
<td>RPCBroker1</td>
<td>LastName.text + ',' + FirstName.text<br />
<br />
Date Of Birth<br />
<br />
SSN</td>
</tr>
<tr class="odd">
<td>DVBAB FIND EXAMS</td>
<td>FINDEXAM</td>
<td>DVBAB1</td>
<td>ARRAY</td>
<td>Lists all of the patient's AMIE II C&amp;P exam requests whether complete, new or pending.</td>
<td>INPUT1</td>
<td>NONE</td>
<td>TfrmExamRequestComments.<br />
FMExamRequestListboxClick<br />
<br />
TfrmMain.<br />
btnViewExamClick<br />
<br />
TfrmManageReports.<br />
FMExamRequestListboxClick<br />
<br />
TfrmNewExam.<br />
btnSendRequestClick<br />
<br />
TTIUSignForm.<br />
FMExamRequestListboxClick<br />
<br />
TfrmUncosigned.<br />
FMExamRequestListboxClick<br />
<br />
TfrmViewExam.<br />
btnAddSelExamsClick<br />
<br />
TfrmViewExam.<br />
btnViewSelectedExamClick<br />
<br />
TfrmViewExam.<br />
btnCancelAllExamsClick<br />
<br />
TCMTSignForm.<br />
FMExamRequestListboxClick</td>
<td>loadexamcomments.pas<br />
<br />
Main.pas<br />
<br />
ManageReports.pas<br />
<br />
newexam.pas<br />
<br />
tiusign.pas<br />
<br />
uncosignedutility.pas<br />
<br />
viewexam.pas<br />
<br />
frmCMTSign.pas</td>
<td>RPCBroker1</td>
<td>IEN<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBAB FORM COPY</td>
<td>COPY</td>
<td>DVBABFRM</td>
<td>SINGLE VALUE</td>
<td> Returns the IEN of the newly copied form.</td>
<td>DVBAB1<br />
DVBAB2</td>
<td>Copies a CAPRI form in file 396.17 to a new entry. Clears key field so the form becomes editable as a new draft document.<br />
DVBAB1 = IEN in 396.17 to copy<br />
DVBAB2 = IEN in patient file<br />
<br />
If DVBAB2 is null, the copied form will be filed under the same patient it previously belonged to.<br />
If DVBAB2 has a value, it'll be copied to the new patient.</td>
<td>TfrmMain.<br />
ButtonIPRCopyClick</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := FMListBoxIPR1.GetSelectedRecord.IEN;<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB FORM DATA BACKUP</td>
<td>BACKUP</td>
<td>DVBABFRM</td>
<td>SINGLE VALUE</td>
<td>Makes a backup copy of a CAPRI template in case of data loss. The backup is restored through the CAPRI GUI.</td>
<td>DVBIEN<br />
LISTBOX TEXT</td>
<td>NONE</td>
<td>TPNCSForm.<br />
ExecuteMoveOfFormData</td>
<td>PNCSMain.pas</td>
<td>RPCBroker1</td>
<td>Piece(xFMEdit2.IENS, ',', 1);<br />
PType := literal;<br />
<strong>or</strong><br />
'MANAGE TEMPLATES restore-point'<br />
PType := literal;<br />
<strong>or</strong><br />
'Template CLOSED / ' + VersionUser;<br />
PType := literal;<br />
<strong>or</strong><br />
'TEMPLATE RESTORE restore-point ';<br />
PType := literal;<br />
<strong>or</strong><br />
SaveName + ' / ' + VersionUser;<br />
PType := literal;<br />
<strong>or</strong><br />
frmMain.RPCBroker1.Param[2].Value + ' / ' + AuthorName<br />
PType := literal</td>
</tr>
<tr class="even">
<td>DVBAB FORM DATA BACKUP DELETE</td>
<td>DELETE</td>
<td>DVBABFRM</td>
<td>SINGLE VALUE</td>
<td>String returned is "^" piece separated, as follows: Piece Item 1</td>
<td>IEN</td>
<td>NONE</td>
<td>TTIUSignForm.<br />
ButtonOK2Click</td>
<td>tiusign.pas</td>
<td>RPCBroker1</td>
<td>Value := Piece(PNCSForm.xFMEdit2.IENS, ',', 1);<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB FORM DATA BACKUP RESTORE</td>
<td>RESTORE</td>
<td>DVBABFRM</td>
<td>SINGLE VALUE</td>
<td>NONE</td>
<td>IEN<br />
SIEN</td>
<td>NONE</td>
<td>TPNCSForm.<br />
RestorPreviousVersion</td>
<td>PNCSMain.pas</td>
<td>RPCBroker1</td>
<td>Piece(xFMEdit2.IENS, ',', 1);<br />
PType := literal;<br />
<br />
IntToStr(WhichVersionToLoad);<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBAB GET SET</td>
<td>GETSET</td>
<td>DVBABDDU</td>
<td>ARRAY</td>
<td>This remote procedure retrieves the SET OF CODES for a given file and field for use in populating controls.</td>
<td>DVBFIL<br />
DVBFLD</td>
<td>The results will be returned as an array of strings, each containing the internal set of codes value and the external set of codes value delimited by a caret ("^").<br />
Example results:<br />
DVBRSL T(1)="T^TERMINAL"<br />
DVBRSL T(2)="P^POW"<br />
DVBRSL T(3)="OS^ORIGINAL SC"<br />
DVBRSL T(4)="ON^ORIGINAL NSC"<br />
DVBRSL T(5)="I^INCREASE"<br />
DVBRSL T(6)="R^REVIEW"<br />
DVBRSL T(7)="OTR^OTHER"</td>
<td>TfrmNewExam.<br />
GetPriorityOfExamItemList<br />
<br />
TfrmVRCancelExam.<br />
PopulateCancelledList<br />
<br />
TVocRehab.<br />
GetReportStatusList</td>
<td>NewExam.pas<br />
VocRehabCancelExam.pas<br />
VocRehabClass.pas<br />
<br />
viewexam.pas<br />
VocRehabReportSetup.pas</td>
<td>RPCBroker1</td>
<td>'396.3'<br />
PType := literal<br />
<br />
'9'<br />
PType := literal<br />
<br />
'396.9'<br />
PType := literal<br />
<br />
'16'<br />
PType := literal<br />
<br />
'396.9'<br />
PType := literal<br />
<br />
'13'<br />
PType := literal</td>
</tr>
<tr class="odd">
<td>DVBAB GET URL</td>
<td>URL</td>
<td>DVBABURL</td>
<td>SINGLE VALUE</td>
<td>Returns a URL for some items used within CAPRI</td>
<td>INDEX</td>
<td>1=VBA's AMIE Worksheet Website<br />
2=CAPRI training website<br />
3=VistAWeb website<br />
5=HIA download website<br />
6=VIRTUAL VA web service server<br />
7=VICAP website<br />
8=VLER DAS web service server<br />
9=JLV website</td>
<td>TfrmMain.<br />
btnVistAWebHomeClick<br />
<br />
TfrmMain.<br />
ShowHIAUserDownloadWebsite<br />
<br />
TfrmMain.<br />
actFileConnectExecute<br />
<br />
TfrmMain.<br />
actHelpCAPRITrainingExecute<br />
<br />
TfrmMain.<br />
actToolsAMIEExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := '9'<br />
PType := literal<br />
Value := '3'<br />
PType := literal<br />
<br />
Value := '5'<br />
PType := literal<br />
<br />
Value := '6'<br />
PType := literal<br />
Value := '7'<br />
PType := literal<br />
Value := '8'<br />
PType := literal<br />
<br />
Value := '2'<br />
PType := literal<br />
<br />
Value := '1'<br />
PType := literal</td>
</tr>
<tr class="even">
<td>DVBAB GET VISIT INFO</td>
<td>VISIT</td>
<td>DVBABTIU</td>
<td>SINGLE VALUE</td>
<td>NONE</td>
<td>PATIENTNAME<br />
VISITDATE<br />
CLINICIEN</td>
<td>NONE</td>
<td>DVBAB GET VISIT INFO</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="odd">
<td>DVBAB GET VVA TOKEN</td>
<td>VVATOKEN</td>
<td>DVBABURL</td>
<td>SINGLE VALUE</td>
<td>This remote procedure retrieves the username, password, and token value passed to the Virtual VA web service.</td>
<td>NONE</td>
<td>Returns the values for username, password, and token as a single caret-delimited string. Example: capri^XXXXX^Username-1</td>
<td>TfrmMain.<br />
actFileConnectExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="even">
<td>DVBAB HEALTH SUMMARY TEXT</td>
<td>RPT</td>
<td>DVBAB1</td>
<td>GLOBAL ARRAY</td>
<td>This RPC retrieves the report text for a report selected on the Report tab. The report format on the roll 'n scroll version of CPRS</td>
<td>DFN<br />
REPORT ID<br />
HEALTHSUMMARYTYPE<br />
DATERANGE</td>
<td>NONE</td>
<td>DVBAB HEALTH SUMMARY TEXT</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="odd">
<td>DVBAB INCREASE EXAM COUNT</td>
<td>INCEXAM</td>
<td>DVBAB1</td>
<td>SINGLE VALUE</td>
<td>Used to record the number of exams pending for a specified patient.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmNewExam.<br />
btnSendRequestClick<br />
<br />
TfrmViewExam.<br />
btnAddSelExamsClick</td>
<td>newexam.pas<br />
<br />
viewexam.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="even">
<td>DVBAB INST LIST</td>
<td>INSTLIST</td>
<td>DVBAB1</td>
<td>GLOBAL ARRAY</td>
<td>Returns a list of Institutions.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
loadinstitutions</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>COMMENTED OUT – NO LONGER CALLED</td>
</tr>
<tr class="odd">
<td>DVBAB LABLIST</td>
<td>LABLIST</td>
<td>DVBAB1</td>
<td>GLOBAL ARRAY</td>
<td>Returns a list of the site's laboratory test names.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
ReportLab</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="even">
<td>DVBAB LOAD FORM</td>
<td>LOAD</td>
<td>DVBABFRM</td>
<td>GLOBAL ARRAY</td>
<td>Set DVBTPSV to 3 for a regular load, 9 for a load from the redundant save field and 10 for the cancellation field. If no value is set, the routine assumes a value of 3.</td>
<td>DVBIEN<br />
DVBTPSV</td>
<td>NONE</td>
<td>pcnShow<br />
PNCSShowModal<br />
<br />
TPNCSPanelLoaderForm.<br />
TryLoad</td>
<td>pcnShow.pas<br />
PNCSPanelLoader.pas</td>
<td>RPCBroker1</td>
<td>Value := frmMain.Piece(FMGetsIPRFile.IENS, ',', 1);<br />
PType := literal;<br />
<br />
CapriTemplateIEN</td>
</tr>
<tr class="odd">
<td>DVBAB MAIL INIT</td>
<td>INIT</td>
<td>DVBAB3</td>
<td>SINGLE VALUE</td>
<td>INIT Mailman variables</td>
<td>NONE</td>
<td>e-mail address^</td>
<td>TfrmMain.<br />
actFileConnectExecute<br />
TfrmMain.<br />
actToolsChangeAddressExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>No params</td>
</tr>
<tr class="even">
<td>DVBAB MPI ASSIGN ICN</td>
<td>MPI</td>
<td>DVBCPATA</td>
<td>SINGLE VALUE</td>
<td>This call should be made after a new patient is added into the patient file. It will call the MPI to assign an ICN. If no ICN can be obtained after 30 seconds, a local ICN will be assigned and the local ICN flag set.</td>
<td>DFN</td>
<td>NONE</td>
<td>TfrmEnterPt.<br />
Button3Click<br />
<br />
TfrmEnterPtSimple.<br />
Button3Click<br />
<br />
TfrmEnterPt140.<br />
Button3Click<br />
<br />
TfrmEnterPtSimple140.<br />
Button3Click</td>
<td>EnterPt.pas<br />
<br />
enterptsimple.pas<br />
<br />
enterpt140.pas<br />
<br />
enterptsimple140.pas</td>
<td>RPCBroker1</td>
<td>Value := Piece(PatientIEN, ',', 1);<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB NEW PERSON FILE</td>
<td>START</td>
<td>DVBAB84</td>
<td>GLOBAL ARRAY</td>
<td>NONE</td>
<td>NONE</td>
<td>NONE</td>
<td>DVBAB NEW PERSON FILE</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="even">
<td>DVBAB NOTE TITLES</td>
<td>NOTETL</td>
<td>DVBABTIU</td>
<td>ARRAY</td>
<td>Returns list of note titles from TIU in format name+" "+type+" "+status</td>
<td>NONE</td>
<td>NONE</td>
<td>TPNCSForm.<br />
FormCreate<br />
<br />
TPNCSMainVistA.<br />
LoadTIUTitles</td>
<td>PNCSMain.pas<br />
frmPNCSMainVistA.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="odd">
<td>DVBAB ORIGINAL PROCESSING DATE</td>
<td>XDA</td>
<td>DVBAB89</td>
<td>GLOBAL ARRAY</td>
<td> </td>
<td>DFN</td>
<td>NONE</td>
<td>Tfrmreports.<br />
RadioButton1_1Click</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := PatientIEN;</td>
</tr>
<tr class="even">
<td>DVBAB PENDING C&amp;P REPORT</td>
<td>STRT</td>
<td>DVBAB6</td>
<td>GLOBAL ARRAY</td>
<td>Generates a report containing the pending C&amp;P exam requests</td>
<td>DVBCSORT<br />
RSTAT<br />
ERDAYS<br />
OLDAYS<br />
ADIVNUM<br />
ELTYP</td>
<td>NONE</td>
<td>TfrmRemoteReports.<br />
PendingCnP<br />
TfrmRemoteReports.<br />
PendingCnPDelimited<br />
<br />
Tfrmreports.<br />
Button1Click</td>
<td>remotereports.pas<br />
<br />
REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Mulitpule parms are set depending on evaluation conditions, however all Values are of type Literal</td>
</tr>
<tr class="odd">
<td>DVBAB PTINQ</td>
<td>PTINQ</td>
<td>DVBAB1</td>
<td>GLOBAL ARRAY</td>
<td>Returns a patient inquiry text report.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
btnRefreshPtDemographicsClick<br />
TfrmMain.<br />
ORReportsAvailableClick</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := PatientIEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBAB REPORT 7131INQ</td>
<td>STRT</td>
<td>DVBAB71</td>
<td>GLOBAL ARRAY</td>
<td>Returns a 7131 inquiry report.</td>
<td>ZDFN<br />
RECIEN</td>
<td>NONE</td>
<td>TfrmMain.<br />
btnGenerate7131ReportClick</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := PatientIEN;<br />
PType := literal;<br />
<br />
Value := FMSeventyOne31RequestListbox.GetSelectedRecord.IEN;<br />
Ptype;=literal</td>
</tr>
<tr class="odd">
<td>DVBAB REPORT ADMINQ</td>
<td>ENBROKE2 </td>
<td>DVBAADRP</td>
<td>GLOBAL ARRAY</td>
<td>Generates an admission inquiry report, in either standard or delimited format for the specified parameters.</td>
<td>BDATE<br />
EDATE<br />
ROYESNO<br />
RONUM<br />
DVBADLMTR</td>
<td>NONE</td>
<td>Tfrmreports.<br />
GetAdmissionInquiryByDate</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := DateTimePicker1.DateTime<br />
PType := literal<br />
<br />
Value := DateTimePicker2.DateTime<br />
PType := literal<br />
<br />
Value := RegOfcYesNo<br />
Ptype;=literal<br />
<br />
Value := RegOfcNum<br />
Ptype;=literal<br />
<br />
Value := GetDelimitedParam(IsDelimited)<br />
PTYpe;=literal</td>
</tr>
<tr class="even">
<td>DVBAB REPORT ADMISSION INQUIRY</td>
<td>ENBROKER</td>
<td>DVBAADRP</td>
<td>ARRAY</td>
<td>Returns display text indicating when the report was last run</td>
<td>NONE</td>
<td>NONE</td>
<td>Tfrmreports.<br />
ORReportsAvailableClick</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="odd">
<td>DVBAB REPORT ADMISSIONS</td>
<td>STRT</td>
<td>DVBAB54</td>
<td>GLOBAL ARRAY</td>
<td>Generates an admission report, in either standard or delimited format for the specified date range.</td>
<td>BDATE<br />
EDATE<br />
DVBADLMTR</td>
<td>NONE</td>
<td>Tfrmreports.<br />
GetHospAdjReport<br />
<br />
Tfrmreports.<br />
GetHospAdjReportByDay</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := FromDate<br />
PType := literal<br />
<br />
Value- ToDate<br />
PType := literal<br />
<br />
Value := GetDelimitedParam(IsDelimited)<br />
PType := literal</td>
</tr>
<tr class="even">
<td>DVBAB REPORT CHECKLIST</td>
<td>REPORT1</td>
<td>DVBAB9</td>
<td>ARRAY</td>
<td>Generates an exam worksheet.</td>
<td>NONE</td>
<td>NONE</td>
<td>DVBAB REPORT CHECKLIST</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="odd">
<td>DVBAB REPORT CPDETAILS</td>
<td>STRT</td>
<td>DVBAB70</td>
<td>ARRAY</td>
<td>Returns a detailed summary of a specific C&amp;P request.</td>
<td>DFN<br />
ZREQDA</td>
<td>NONE</td>
<td>TfrmMain.<br />
btnGenerateReportClick</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := PatientIEN;<br />
PType := literal;<br />
<br />
Value := FMExamRequestListbox.GetSelectedRecord.IEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBAB REPORT DISCHARGE</td>
<td>STRT</td>
<td>DVBAB53</td>
<td>GLOBAL ARRAY</td>
<td>Generates a discharge report, in either standard or delimited format, for the specified parameters.</td>
<td>BDATE<br />
EDATE<br />
ADTYPE<br />
DVBADLMTR</td>
<td>NONE</td>
<td>Tfrmreports.<br />
GetHospAdjReport<br />
<br />
Tfrmreports.<br />
GetHospAdjReportByDay</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := FromDate<br />
PType := literal;<br />
<br />
Value := ToDate<br />
PType := literal;<br />
<br />
Value= DoYouWant<br />
PType := literal;<br />
<br />
Value=IsDelimited<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB REPORT EXAM CHKLIST</td>
<td>STRT</td>
<td>DVBAB4</td>
<td>ARRAY</td>
<td>Generates an exam worksheet.</td>
<td>NONE</td>
<td>NONE</td>
<td>Tfrmreports.<br />
ORReportsAvailableClick</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="even">
<td>DVBAB REPORT INCOMPVET</td>
<td>STRT</td>
<td>DVBAB51</td>
<td>GLOBAL ARRAY</td>
<td>Generates an incompetent veteran report, in either standard or delimited format, for the specified date range.</td>
<td>BDATE<br />
EDATE<br />
DVBADLMTR</td>
<td>NONE</td>
<td>Tfrmreports.<br />
GetHospAdjReport<br />
<br />
Tfrmreports.<br />
GetHospAdjReportByDay</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := FromDate<br />
PType := literal;<br />
<br />
Value := ToDate<br />
PType := literal;<br />
<br />
Value := IsDelimited<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB REPORT LISTS</td>
<td>LIST</td>
<td>DVBAB1</td>
<td>ARRAY</td>
<td>This remote procedure call returns a list of reports, Health Summary types and date ranges that can be displayed at the workstation. There are no input parameters for this RPC.</td>
<td>NONE</td>
<td>NONE</td>
<td>DVBAB REPORT LISTS</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="even">
<td>DVBAB REPORT NEW NOTICES DC</td>
<td>ENBROKER</td>
<td>DVBADSNT</td>
<td>GLOBAL ARRAY</td>
<td>Broker-enabled version of option DVBA NOTICE/DISCHARGE PRINT, Print New Notices of Discharge.</td>
<td>NONE</td>
<td>NONE</td>
<td>Tfrmreports.<br />
ORReportsAvailable2Click</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="odd">
<td>DVBAB REPORT PENDING7131</td>
<td>STRT</td>
<td>DVBAB57</td>
<td>GLOBAL ARRAY</td>
<td>Generates a list of pending 7131 requests.</td>
<td>SELDIV<br />
DIV<br />
DVBADLMTR</td>
<td>NONE</td>
<td>Tfrmreports.<br />
Button9Click</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := ''<br />
Ptype= literal;<br />
> **NOTE:** the Value param is set base on multiple conditions. See code for conditions.</td>
</tr>
<tr class="even">
<td>DVBAB REPORT READMIT</td>
<td>STRT</td>
<td>DVBAB56</td>
<td>GLOBAL ARRAY</td>
<td>Generates a re-admission report, in either standard or delimited format for the specified date range.</td>
<td>BDATE<br />
EDATE<br />
DVBAH<br />
DVBADLMTR</td>
<td>NONE</td>
<td>Tfrmreports.<br />
GetHospAdjReport<br />
<br />
Tfrmreports.<br />
GetHospAdjReportByDay</td>
<td>Reports.pas</td>
<td>RPCBroker1</td>
<td>Value := UserDUZHomeServer;<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB REPORT SPECIAL</td>
<td>SPECRPT</td>
<td>DVBASPD2</td>
<td>GLOBAL ARRAY</td>
<td>Generates a Special Report for Pension and Advisory &amp; Assistance (A&amp;A), in either standard or delimited format, for the specified parameters.</td>
<td>DCTYPES<br />
BDATE<br />
EDATE<br />
RONUM<br />
REP<br />
DVBADLMTR</td>
<td>NONE</td>
<td>TfrmSpecialReport.<br />
ButtonRunReportClick</td>
<td>specialreport.pas</td>
<td>RPCBroker1</td>
<td>This RPC has 6 possible parms that can be set base on evaluation conditions. All of the Parms have a Type set to Literal.</td>
</tr>
<tr class="even">
<td>DVBAB REPORTS</td>
<td>START</td>
<td>DVBAB82</td>
<td>GLOBAL ARRAY</td>
<td>CAPRI REGIONAL OFFICE 21 DAY CERTIFICATE PRINTING</td>
<td>REPORT TYPE<br />
REPORT STRING</td>
<td>NONE</td>
<td>TfrmMain.<br />
ORReportsAvailableClick<br />
TfrmMain.<br />
GetPatientProfileMAS<br />
TfrmMain.<br />
btnExamFinalReportClick<br />
TfrmMain.<br />
ButtonOKSurgeryReportsClick<br />
<br />
TfrmRemoteReports.<br />
CnPReprint<br />
<br />
Tfrmreports.<br />
ORReportsAvailableClick<br />
Tfrmreports.<br />
Button3Click<br />
Tfrmreports.<br />
Button5Click<br />
Tfrmreports.<br />
GetFeeBasisReport<br />
Tfrmreports.<br />
GetEpisodeOfCare<br />
Tfrmreports.<br />
ORReportsAvailable2Click<br />
Tfrmreports.<br />
GetRequestStatusReport<br />
<br />
TVocRehab.<br />
RunForm8861StatusReport</td>
<td>Main.pas<br />
<br />
remotereports.pas<br />
<br />
REPORTS.pas<br />
<br />
VocRehabClass.pas</td>
<td>RPCBroker1</td>
<td>Value := '1'; // 21 Day Cert Print<br />
PType := literal;<br />
<br />
Value := ''<br />
PType := literal;<br />
<br />
Has two Parms with the type equal to literal. This RPC is called 4 times depending on which report is to be executed.<br />
Value := '3'; // C&amp;P FINAL (MANUAL)<br />
PType := literal;<br />
<br />
Value := ''; //<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB RESTRICTED LIST PATIENTS</td>
<td>RSTLIST</td>
<td>DVBABFRM</td>
<td>GLOBAL ARRAY</td>
<td>Returns a list of restricted patients for CAPRI when in remote mode.</td>
<td>DUZ</td>
<td>NONE</td>
<td>TfrmMain.<br />
ShowPatientList</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := UserDUZHomeServer;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBAB SAVE FORM</td>
<td>SAVE</td>
<td>DVBABFRM</td>
<td>SINGLE VALUE</td>
<td>Set DVBIEN to the internal entry number of the form<br />
Set DVBLINES to the lines to be saved<br />
Set DVBLINEN to the starting line # in the global. This allows for forms to be sent in chunks.</td>
<td>DVBIEN<br />
DVBLINES<br />
DVBLINECOUNT<br />
DVBLINEN</td>
<td>NONE</td>
<td>TPNCSForm.<br />
SaveFormDataFields</td>
<td>PNCSMain.pas</td>
<td>RPCBroker1</td>
<td>Value := IEN<br />
PType := literal;<br />
<br />
Value := xFormDataTemp.lines[x + y];<br />
PType := list;<br />
<br />
Value := inttostr(y);<br />
PType := literal;<br />
<br />
Value := whichglobal;<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB SC VETERAN REPORT</td>
<td>EN</td>
<td>DVBAB4</td>
<td>ARRAY</td>
<td>Generates a service-connected veterans report.</td>
<td>INPUT1<br />
INPUT2</td>
<td>NONE</td>
<td>DVBAB SC VETERAN REPORT</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="even">
<td>DVBAB SEND MSG</td>
<td>MSG</td>
<td>DVBAB1</td>
<td>SINGLE VALUE</td>
<td>Used to generate e-mail messages for specific CAPRI actions, such as changing a C&amp;P exam request.</td>
<td>VAL1<br />
VAL2<br />
VAL3<br />
VAL4<br />
VAL5</td>
<td>NONE</td>
<td>CAPRISupport<br />
SendNotification<br />
<br />
TfrmEnterPt.<br />
Button3Click<br />
<br />
TfrmEnterPtSimple.<br />
Button3Click<br />
<br />
TfrmEnterPt140.<br />
Button3Click<br />
<br />
TfrmEnterPtSimple140.<br />
Button3Click</td>
<td>CAPRISupport.pas<br />
- managereports.pas<br />
- uncosignedutility.pas<br />
- viewexam.pas<br />
- frmCMTSign.pas<br />
<br />
EnterPt.pas<br />
<br />
enterptsimple.pas<br />
<br />
enterpt140.pas<br />
<br />
enterptsimple140.pas</td>
<td>RPCBroker1</td>
<td><strong>AuthorIEN</strong><br />
'CAPRI: New C&amp;P Veteran Added to Patient File'<br />
MailManBuffer.Lines<br />
'DVBA C NEW C&amp;P VETERAN<br />
<strong>AuthorIEN</strong><br />
'CAPRI: New C&amp;P Veteran Added to Patient File'<br />
'DVBA C NEW C&amp;P VETERAN'<br />
MailManBuffer.Lines[i]<br />
Value := AuthorIEN; //DUZ Of Author of Note<br />
PType := literal;<br />
Value := 'CAPRI: Cancellation of 2507 Exams'; //Max 45 Chars<br />
PType := literal;<br />
PType := list;<br />
Mult[IntToStr(i + 1)] := frmMain.MailManBuffer.Lines[i];<br />
Value := 'DVBA C 2507 CANCELLATION'; //Mail Group Name<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB SEND MSG TWO</td>
<td>MSG2</td>
<td>DVBAB1A</td>
<td>SINGLE VALUE</td>
<td>THIS RPC IS THE SECOND FOR THE CAPRI MSG 2507 EXAM THIS ONE PRODUCES A MESSAGE FOR EACH EXAM THAT IS COMPLETED</td>
<td>DUZ RIEN ELIST</td>
<td>ERR RETURNS THE ERROR MESSAGE OR THE 'MESSAGE SENT'</td>
<td>CAPRISupport<br />
SendNotificationTwo</td>
<td>tiusign.pas<br />
frmCMTSign.pas</td>
<td>RPCBroker1</td>
<td>Value := SenderDUZ;<br />
PType := literal;<br />
<br />
Value := RequestIEN;<br />
PType := literal;<br />
<br />
ExamIENs[I]<br />
PType := list;</td>
</tr>
<tr class="even">
<td>DVBAB SET DIVISION</td>
<td>DUZ2</td>
<td>DVBAB84</td>
<td>SINGLE VALUE</td>
<td>Set the Division</td>
<td>NUM</td>
<td>Return O^ERR_MESSAGE (upon failure) IEN^INSTITUTION_NAME (upon success)</td>
<td>TfrmMain.<br />
actFileConnectExecute<br />
TfrmMain.<br />
btnExamFinalReportClick<br />
<br />
Tfrmreports.<br />
FormActivate</td>
<td>Main.pas<br />
REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := RemoteUserDivisionNumber;<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB SURGERY CASE</td>
<td>START</td>
<td>DVBAB89</td>
<td>GLOBAL ARRAY</td>
<td>NONE</td>
<td>DFN</td>
<td>NONE</td>
<td>TfrmMain.<br />
ORReportsAvailableClick</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := PatientIEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>DVBAB TEAM PATIENTS</td>
<td>TEAMPTS</td>
<td>DVBAB1</td>
<td>GLOBAL ARRAY</td>
<td>Function returns an array of patients on a team.</td>
<td>TEAM ID</td>
<td>Array of patients on a team in the format: patient id (DFN)^patient name.</td>
<td>TfrmMain.<br />
actFileConnectExecute</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>Value := PatientSelectionList;<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB TEMPLATE DEFINITION</td>
<td>DEFINE</td>
<td>DVBABFRM</td>
<td>GLOBAL ARRAY</td>
<td>C&amp;P Worksheet Templates are made of 3 files: a form definition, a code definition, and a script definition.<br />
Set DVBIEN to the internal entry number of the form<br />
Set DVBTYPE to the definition you want: 1= Form, 2=Script, 3=Report</td>
<td>DVBIEN<br />
<br />
DVBTYPE</td>
<td>NONE</td>
<td>TfrmBrowseTemplates.<br />
ButtonGenerateTemplateClick<br />
<br />
TfrmManageTemplateDefinitions.<br />
ButtonImportOnlyClick<br />
TfrmManageTemplateDefinitions.<br />
ButtonImportOnlyTestClick<br />
<br />
pncsShow<br />
PNCSShowModal<br />
<br />
TfrmGenerateBlankTemplate.<br />
ButtonGenerateTemplateClick<br />
<br />
TPNCSPanelLoaderForm.<br />
TryLoad</td>
<td>browsetemplates.pas<br />
<br />
managetemplatedefs.pas<br />
<br />
pncsShow.pas<br />
<br />
printtemplate.pas<br />
<br />
PNCSPanelLoader.pas</td>
<td>RPCBroker1<br />
RPCBrokerDevAccount</td>
<td>IEN<br />
'1'</td>
</tr>
<tr class="even">
<td>DVBAB TEMPLATE LIST</td>
<td>TEMPLATE</td>
<td>DVBAB1</td>
<td>GLOBAL ARRAY</td>
<td>Returns complete list of CAPRI templates.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
actToolsPrintBlankExamExecute<br />
TfrmMain.<br />
BitBtnNewFormClick</td>
<td>Main.pas</td>
<td>RPCBroker1</td>
<td>None</td>
</tr>
<tr class="odd">
<td><span id="DVBABTEMPLATEREPORTFULL" class="anchor"></span>DVBAB TEMPLATE REPORT FULL</td>
<td>RPTSTAT</td>
<td>DVBAB85</td>
<td>GLOBAL ARRAY</td>
<td>Returns report of exam templates, including current status, Worksheet Originator name.</td>
<td>STRTDT<br />
<br />
ENDDT<br />
<br />
DVBDLMT</td>
<td>NONE</td>
<td>Tfrmreports.<br />
Button8Click</td>
<td>REPORTS.pas</td>
<td>RPCBroker1</td>
<td>Value := FMToDateConvert(FormatDateTime('mm/dd/yyyy', DateTimePicker3.DateTime));<br />
PType := literal;<br />
<br />
Value := FMToDateConvert(FormatDateTime('mm/dd/yyyy', DateTimePicker4.DateTime));<br />
PType := literal;<br />
<br />
ExportFormat '1' or '0'</td>
</tr>
<tr class="even">
<td>DVBAB VERSION</td>
<td>VERSION</td>
<td>DVBAB1</td>
<td>SINGLE VALUE</td>
<td>This RPC returns the MINIMUM version parameter and also checks if the<br />
GUI matches the MINIMUM version build or the PREVIOUS version build.<br />
<br />
If the GUI is the PREVIOUS version and falls outside of the grace period<br />
or the GUI is not the MINIMUM or PREVIOUS build this RPC will return<br />
the grace period date of January 1, 1980 enforcing GUI version control<br />
to recognize this version is no longer allowed sign on.</td>
<td>DVBGUIV</td>
<td>Version # of CAPRI GUI. Sets a variable DVBABVRx so that the error trap will display what version of the client software the user was utilizing.<br />
DVBGUIV is also used to determine if the GUI attempting sign on should be allowed.</td>
<td>TfrmMain.<br />
VersionControl</td>
<td>main.pas</td>
<td>RPCBroker1</td>
<td>Value := VersionUser;<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>DVBAB ZIP2CITY</td>
<td>ZIP2CITY</td>
<td>DVBABADR</td>
<td>ARRAY</td>
<td>The remote procedure returns a list containing city, county, and state for<br />
a given ZIP code.</td>
<td>DVBZIP</td>
<td>ZIP code value in ZIP+4 format.<br />
RESULT(0)=ResultCount_"^"_ErrorMsg<br />
RESULT(1)=City_"^"_County_"^"_State<br />
RESULT(n)=City_"^"_County_"^"_State</td>
<td>TfrmEnterPt.<br />
PopulateCtyCntySt<br />
<br />
TfrmEnterPtSimple.<br />
PopulateCtyCntySt</td>
<td>EnterPt.pas<br />
<br />
enterptsimple.pas</td>
<td>RPCBroker1</td>
<td>Zipcode as text</td>
</tr>
<tr class="even">
<td>DVBAD CONTRACTED EXAM CRYPTO*</td>
<td>EN</td>
<td>DVBACEM1</td>
<td>SINGLE VALUE</td>
<td>Allows the demTRAN (GUI) application to Encrypt/Decrypt information for storage to or retrieval from the VistA environment.</td>
<td>DVBAETYP<br />
<br />
DVBAIVAL</td>
<td>Encrypted or Decrypted result(s) based on the cryptography action performed. If multiple values passed ('^' delimitted) then the results Enter RETURN to continue or '^' to exit will be returned in the same position as the original value that was acted upon.</td>
<td>TVendorConnect.<br />
GetVndrConnInfo</td>
<td>clsVendConn.pas v254</td>
<td>ClmsSysCCOWBrkr</td>
<td>Value := '2';<br />
PType := literal;<br />
FUsername + '^' + FPassword;<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td><span id="DVBADCONTRACTEDEXAMREPORTS" class="anchor"></span>DVBAD CONTRACTED EXAM REPORTS*</td>
<td>CERPTS</td>
<td>DVBACER1</td>
<td>GLOBAL ARRAY</td>
<td>Allows demTRAN (GUI) to execute the Detailed, Summary and Timeliness contracted exam reports.</td>
<td>DVBARTYP<br />
<br />
DVBAFLTRS</td>
<td>NONE</td>
<td>TfrmRptRslts.<br />
GetReportData</td>
<td>frm508ReportRslts.pas v254</td>
<td>_CCOWBrkr</td>
<td>_RptType<br />
PType := literal;<br />
<br />
_RptParams.ValueFromIndex[i]<br />
PType := List;</td>
</tr>
<tr class="even">
<td>ORPRF GETFLG</td>
<td>GETFLG</td>
<td>ORPRF</td>
<td>ARRAY</td>
<td>NONE</td>
<td>NONE</td>
<td>NONE</td>
<td>ORPRF GETFLG changed to<br />
DVBAB GETFLG<br />
<br />
TFormPtRecordFlags.<br />
ORListBoxFlagsClick</td>
<td>frmptrecordflags.pas</td>
<td>RPCBroker1</td>
<td>labelPatientDFN.Caption<br />
PType := literal;<br />
<br />
Piece(ORListBoxFlags.Items[ORListBoxFlags.ItemIndex], '^', 1);<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>ORPRF HASFLG</td>
<td>HASFLG</td>
<td>ORPRF</td>
<td>ARRAY</td>
<td>NONE</td>
<td>NONE</td>
<td>NONE</td>
<td>ORPRF HASFLG changed to<br />
DVBAB HASFLG<br />
<br />
frmptrecordflags<br />
HasActPRFFlag<br />
<br />
TfrmPatientList.<br />
btnCvrSelectPtClick</td>
<td>frmptrecordflags.pas<br />
<br />
patientlist.pas</td>
<td>RPCBroker1</td>
<td>PatientDFN<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>ORPRF TRIGGER POPUP</td>
<td>TRIGRPOP</td>
<td>ORPRF</td>
<td>SINGLE VALUE</td>
<td>Returns 1 if popup flag display should be triggered for given patient upon patient selection. If not, returns 0. Does not require clean-up after calling it since it does not set arrays or globals.</td>
<td>NONE</td>
<td>Returns 1 if popup flag display should be triggered for given patient upon patient selection. If not, returns 0.</td>
<td>ORPRF TRIGGER POPUP changed to<br />
DVBAB PRF POPUP<br />
<br />
TfrmPatientList.<br />
FMCvrListBox1PtClick<br />
TfrmPatientList.<br />
btnCvrSelectPtClick</td>
<td>patientlist.pas</td>
<td>RPCBroker1</td>
<td>frmMain.Piece(FMCvrGets1Pt.IENS, ',', 1);<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>ORWCIRN FACLIST</td>
<td>FACLIST</td>
<td>ORWCIRN</td>
<td>ARRAY</td>
<td>Returns a list of the remote VA facilities at which the selected patient has been seen.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
ORReportsAvailableClick<br />
TfrmMain.<br />
ButtonRDVClick<br />
TfrmMain.<br />
ButtonOtherSitesClick<br />
<br />
TfrmPatientList.<br />
FMCvrListBox1PtClick<br />
checkfordoddata<br />
TfrmPatientList.<br />
FMCvrListBox1PtClick<br />
<br />
TfrmPatientList.<br />
btnCvrSelectPtClick<br />
checkCCOWfordoddata<br />
<br />
TfrmPatientList.<br />
ButtonOtherSitesClick<br />
<br />
TfrmPatientListRestricted.<br />
ORListBox1Change<br />
checkfordoddata<br />
TfrmPatientListRestricted.<br />
ORListBox1Change<br />
<br />
TfrmPatientListRestricted.<br />
ButtonOtherSitesClick</td>
<td>main.pas<br />
<br />
patientlist.pas<br />
<br />
patientlistrestricted.pas</td>
<td>RPCBroker1</td>
<td>frmMain.Piece(FMCvrGets1Pt.IENS, ',', 1);<br />
PType := literal;<br />
<br />
FMListBox1.GetSelectedRecord.IEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>ORWLRR CHART</td>
<td>CHART</td>
<td>ORWLRR</td>
<td>GLOBAL ARRAY</td>
<td>NONE</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmLabGraph.<br />
ButtonGraphClick</td>
<td>labgraph.pas</td>
<td>RPCBroker1</td>
<td>PatientIEN; // Patient IEN<br />
PType := literal;<br />
FMToDateConvert(FormatDateTime('mm/dd/yyyy', DateTimePicker2.Date)) + '.2359'; //Stop Date<br />
PType := literal;<br />
FMToDateConvert(FormatDateTime('mm/dd/yyyy', DateTimePicker1.Date)); //Start Date<br />
PType := literal;<br />
<br />
'0'; // 0 for "All Specimens"<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>ORWORB FASTUSER</td>
<td>FASTUSER</td>
<td>ORWORB</td>
<td>GLOBAL ARRAY</td>
<td>Function returns notifications for current user.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmTIUCosign.<br />
GetCosignatureAlerts</td>
<td>tiucosignature.pas</td>
<td>RPCBroker1</td>
<td>No Params</td>
</tr>
<tr class="even">
<td>ORWPT ADMITLST</td>
<td>ADMITLST</td>
<td>ORWPT</td>
<td>ARRAY</td>
<td>Returns a list of admissions for a patient (for visit selection).</td>
<td>NONE</td>
<td>NONE</td>
<td>TPNCSMainVistA.<br />
SignWorksheet<br />
<br />
TfrmMain.<br />
btnAdd7131Click<br />
TfrmMain.<br />
btnAdmissionsClick<br />
<br />
TPNCSForm.<br />
xFormOutputOKClick</td>
<td>frmPNCSMainVistA.pas<br />
main.pas<br />
PNCSMain.pas</td>
<td>RPCBroker1</td>
<td>xPatientIENS.Caption<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>ORWU DT</td>
<td>DT</td>
<td>ORWU</td>
<td>SINGLE VALUE</td>
<td>Returns date in internal VA FileMan format.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmEditPatientLists.<br />
Button11Click<br />
Button20Click<br />
Button1Click<br />
<br />
TfrmEnterPt.<br />
Button3Click<br />
<br />
TfrmEnterPt140.<br />
Button3Click<br />
<br />
TfrmEnterPtSimple.<br />
Button3Click<br />
<br />
TfrmEnterPtSimple140.<br />
Button3Click<br />
<br />
TCMTSignForm.<br />
ValidateXMLData<br />
SendDbqsToVlerAndVista<br />
ButtonGetApptsClick<br />
ReleaseExamToRO<br />
<br />
TfrmMailMan.<br />
FormClose<br />
<br />
TfrmMain.<br />
ReportLab<br />
actToolsPrintBlankExamExecute<br />
BitBtnVistAClick<br />
BitBtnNewFormClick<br />
<br />
TfrmManageReports.<br />
buttonReleaseClick<br />
<br />
TfrmManageTemplateDefinitions.<br />
ButtonImportOnlyClick<br />
ButtonImportOnlyTestClick<br />
<br />
TPNCSForm.<br />
DoLock<br />
ReconnectAndLock<br />
RepopulateControls<br />
ExecuteSaveOfFormData<br />
<br />
TfrmRemoteUserSitesEditor.<br />
FMListBoxCAPRISitesClick<br />
<br />
TfrmTIUCosign.<br />
SaveAddendum<br />
<br />
TTIUSignForm.<br />
ValidateXMLData<br />
SendDbqsToVlerAndVista<br />
ButtonGetApptsClick<br />
ReleaseExamToRO<br />
<br />
TfrmUncosigned.<br />
Button3Click<br />
<br />
TfrmViewExam.<br />
btnCloseClick</td>
<td>editpatientlists.pas<br />
enterpt.pas<br />
enterpt140.pas<br />
enterptsimple.pas<br />
enterptsimple140.pas<br />
frmCMTSign.pas<br />
MailMan.pas<br />
main.pas<br />
managereports.pas<br />
managetemplatedefs.pas<br />
PNCSMain.pas<br />
remoteusersiteseditor.pas<br />
tiucosignature.pas<br />
tiusign.pas<br />
uncosignedutility.pas<br />
viewexam.pas</td>
<td>RPCBroker1</td>
<td>Value := 'NOW'<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>ORWU VALIDSIG</td>
<td>VALIDSIG</td>
<td>ORWU</td>
<td>SINGLE VALUE</td>
<td>Validates a broker encrypted electronic signature.</td>
<td>NONE</td>
<td>NONE</td>
<td>TCMTSignForm.<br />
IsSignatureValid<br />
<br />
TTIUSignForm.<br />
IsSignatureValid</td>
<td>frmCMTSign.pas<br />
tiusign.pas</td>
<td>RPCBroker1</td>
<td>Value := encrypt(Edit3.Text);<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>TIU CREATE ADDENDUM RECORD</td>
<td>MAKEADD</td>
<td>TIUSRVP</td>
<td>SINGLE VALUE</td>
<td>This Remote Procedure allows the creation of addenda to TIU Documents.</td>
<td>NONE</td>
<td>This is the record number of the resulting addendum.<br />
> **NOTE:** If no addendum record may be created, then the return variable will look as follows: "-1^Could not create addendum."</td>
<td>TfrmTIUCosign.<br />
SaveAddendum</td>
<td>tiucosignature.pas</td>
<td>RPCBroker1</td>
<td>Value := CoSigTIUNoteIEN;<br />
PType := literal;<br />
Mult['1202'] := authorIEN;<br />
Mult['1301'] := dttm<br />
PType := list;<br />
Value := '1';<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>TIU CREATE RECORD</td>
<td>MAKE</td>
<td>TIUSRVP</td>
<td>SINGLE VALUE</td>
<td>This remote procedure allows the creation of TIU DOCUMENT records.</td>
<td>NONE</td>
<td>If the call is successful, this will be the record number (IEN) of the resulting entry in the TIU DOCUMENT FILE (#8925). In the event of a filing error, the first "^"-piece will be zero, and the second "^"-piece of this scalar return variable will be a textual message describing the nature of the error (e.g., 0^Invalid TITLE Selected.").</td>
<td>uTIU<br />
CreateTIURecord</td>
<td>uTIU.pas<br />
- frmCMTSign.pas<br />
- tiusign.pas</td>
<td>RPCBroker1</td>
<td>Value := PNCSform.xPatientIENS.Caption; // Patient<br />
PType := literal;<br />
Value := aTitleIEN; // Title PType := literal;<br />
Value := ''; // VDT PType := literal;<br />
Value := ''; // VLOC PType := literal;<br />
Value := ''; // VisitIDIEN; //VSIT<br />
PType := literal; Mult['1202'] := AuthorIEN;<br />
Mult['1301'] := Piece(aVisitIDIEN, ';', 2); // Reference Date<br />
Mult['1205'] := Piece(aVisitIDIEN, ';', 1); // Location<br />
Mult['1208'] := FMEdit16.Text; // Cosigner<br />
Mult['1701'] := ''; //Subject, PType := list;<br />
Value := aVisitIDIEN; // Visit Location; Date/Time; Service category (Optional)<br />
PType := literal; .Value := '1'; //Suppress? PType := literal;</td>
</tr>
<tr class="odd">
<td>TIU DELETE RECORD</td>
<td>DELETE</td>
<td>TIUSRVP</td>
<td>SINGLE VALUE</td>
<td>Deletes TIU Document records...Evaluates authorization.</td>
<td>NONE</td>
<td>Returns error message with ERR=1^Explanation text if the user is NOT authorized to delete the named record (e.g., it's his, but signed; or it's not his, and he better keep his paws off it).</td>
<td>uTIU<br />
DeleteTIURecord</td>
<td>uTIU.pas<br />
- frmCMTSign.pas<br />
- tiusign.pas</td>
<td>RPCBroker1</td>
<td>Value := aTIUNoteIEN;<br />
PType := literal;<br />
Value := Encrypt(aSignature);<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>TIU GET ALERT INFO</td>
<td>GETALRT</td>
<td>TIUSRVP</td>
<td>SINGLE VALUE</td>
<td>Given a TIU XQAID, return the patient anddocument type for the item being alerted.</td>
<td>NONE</td>
<td>TIUDA^DFN^gui tab indicator where TIUDA is the document IEN in ^TIU(8925DFN is the patient IEN gui tab indicator is an arbitrarily set constant based on the document type.</td>
<td>TfrmTIUCosign.<br />
PascalCosign</td>
<td>tiucosignature.pas</td>
<td>RPCBroker1</td>
<td>Value := frmMain.Piece(ORListBox1.Items[ORListBox1.ItemIndex], '^', 8);PType := literal;</td>
</tr>
<tr class="odd">
<td>TIU GET RECORD TEXT</td>
<td>TGET</td>
<td>TIUSRVR1</td>
<td>GLOBAL ARRAY</td>
<td>This RPC will get the textual portion of a TIU Document Record.</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmMain.<br />
ReportPNDS<br />
<br />
TfrmTIUCosign.<br />
ORListBox1Click<br />
<br />
TFormTIUDisplay.<br />
SpeedButtonCPRSClick<br />
<br />
TfrmUncosigned.<br />
ButtonSearchClick<br />
TfrmUncosigned.<br />
Button1Click<br />
<br />
uTIU<br />
GetTIUText</td>
<td>main.pas<br />
<br />
tiucosignature.pas<br />
<br />
tiudisplayunit.pas<br />
<br />
uncosignedutility.pas<br />
<br />
uTIU.pas<br />
- frmCMTSign.pas<br />
- tiusign.pas</td>
<td>RPCBroker1</td>
<td>Value := aTIUNoteIEN;<br />
PType := literal;<br />
<br />
Value := TIUNoteIEN; //TIU Document number<br />
PType := literal;<br />
<br />
Value := frmMain.Piece(frmMain.Piece(frmMain.Piece(ORListBox1.Items[ORListBox1.ItemIndex], '^', 8), ';', 1), 'U', 2);<br />
PType := literal;<br />
<br />
Value := editTIUDocumentNumber.text;<br />
PType := literal;<br />
<br />
No Params</td>
</tr>
<tr class="even">
<td>TIU LOAD BOILERPLATE TEXT</td>
<td>BLRSHELL</td>
<td>TIUSRVD</td>
<td>GLOBAL ARRAY</td>
<td>This RPC will load the boilerplate text associated with the selected title, and execute the methods for any objects embedded in the boilerplate text.</td>
<td>NONE</td>
<td>NONE</td>
<td>TPNCSForm.<br />
xMemoTIUObjectChange</td>
<td>PNCSMain.pas</td>
<td>RPCBroker1</td>
<td>Copy(PNCSForm.xFMPNTitles.Items[xFMPNTitles.ItemIndex], Pos(' IEN#', PNCSForm.xFMPNTitles.Items[xFMPNTitles.ItemIndex]) + 6, 99);<br />
PType := literal;<br />
xPatientIENS.Caption; {Patient IEN}<br />
PType := literal;</td>
</tr>
<tr class="odd">
<td>TIU REQUIRES COSIGNATURE</td>
<td>REQCOS</td>
<td>TIUSRVA</td>
<td>SINGLE VALUE</td>
<td>This Boolean RPC simply evaluates whether the current user requires cosignature for TIU DOCUMENTS, and returns a 1 if true, or a 0 if false.</td>
<td>NONE</td>
<td>Boolean result: 0 if FALSE, OR 1 if TRUE.</td>
<td>TCMTSignForm.<br />
PNTitlesChange<br />
<br />
TTIUSignForm.<br />
PNTitlesChange</td>
<td>frmCMTSign.pas<br />
tiusign.pas</td>
<td>RPCBroker1</td>
<td>Value := Copy(pncsForm.xFMPNTitles.Items[x], Pos(' IEN#', pncsForm.xFMPNTitles.Items[x]) + 6, 99);<br />
PType := literal;<br />
Value := '0';<br />
PType := literal;<br />
Value := AuthorIEN;<br />
PType := literal;</td>
</tr>
<tr class="even">
<td>TIU SET DOCUMENT TEXT</td>
<td>SETTEXT</td>
<td>TIUSRVPT</td>
<td>SINGLE VALUE</td>
<td>This RPC buffers the transmittal of text (i.e., the body of TIU Documents) from the Client to the Server. It allows documents of indefinite size to be filed, without risk of an allocate error on the M Server.</td>
<td>NONE</td>
<td>Four '^'-piece scalar result formatted as follows:<br />
If successful: &lt;IEN in TIU DOCUMENT FILE&gt;^&lt;LAST_PAGE_RECEIVED&gt;^&lt;TOTAL_PAGES_EXPECTED&gt;<br />
If unsuccessful: 0^0^0^Explanatory text</td>
<td>TfrmTIUCosign.<br />
SaveAddendum<br />
<br />
uTIU<br />
InitParams</td>
<td>tiucosignature.pas<br />
<br />
uTIU.pas</td>
<td>RPCBroker1</td>
<td>Value := addendIEN;<br />
PType := literal;<br />
Mult['"TEXT",' + inttostr(x + 1) + ',0'] := addendumtext.lines[x];<br />
<strong>or</strong><br />
Mult['"HDR"'] := '1^1';<br />
PType := list;<br />
Value := '0';</td>
</tr>
<tr class="odd">
<td>TIU SIGN RECORD</td>
<td>SIGN</td>
<td>TIUSRVP</td>
<td>SINGLE VALUE</td>
<td>This API Supports the application of the user's electronic signature to a TIU document while evaluating authorization and validating the user's electronic signature.</td>
<td>NONE</td>
<td>This is the error code which may result if the user enters an invalid code, or if the Authorization/Subscription Utility determines that the user is NOT authorized to sign (or cosign) the document, as specified by the site's business rules.</td>
<td>TfrmTIUCosign.<br />
SaveAddendum<br />
<br />
uTIU<br />
SignTIURecord</td>
<td>tiucosignature.pas<br />
<br />
uTIU.pas<br />
- frmCMTSign.pas<br />
- tiusign.pas</td>
<td>RPCBroker1</td>
<td>Value := aTIUNoteIEN;<br />
PType := literal;<br />
Value := Encrypt(aSignature);<br />
PType := literal;<br />
Value := addendIEN;<br />
PType := literal;<br />
Value := Encrypt(TIUSignForm.Edit3.Text);</td>
</tr>
<tr class="even">
<td>TIU UPDATE RECORD</td>
<td>UPDATE</td>
<td>TIUSRVP</td>
<td>SINGLE VALUE</td>
<td>This API updates the record named in the TIUDA parameter, with the information contained in the TIUX(Field #) array. The body of the modified TIU document should be passed in the TIUX("TEXT",i,0) subscript, where i is the line number (i.e., the "TEXT" node should be ready to MERGE with a word processing field). Any filing errors which may occur will be returned in the single valued ERR parameter (which is passed by reference).</td>
<td>NONE</td>
<td>NONE</td>
<td>TfrmTIUCosign.<br />
SaveAddendum</td>
<td>tiucosignature.pas</td>
<td>RPCBroker1</td>
<td>Value := addendIEN;<br />
PType := literal;<br />
Mult['1202'] := authorIEN;<br />
Mult['1301'] := dttm<br />
Mult['1701'] := '';<br />
PType := list;<br />
Value := '1';</td>
</tr>
<tr class="odd">
<td>XUS SET VISITOR</td>
<td>SETVISIT</td>
<td>XUSBSE1</td>
<td>SINGLE VALUE</td>
<td>NONE</td>
<td>NONE</td>
<td>NONE</td>
<td>XUS SET VISITOR'</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
<td>Not called in Delphi code</td>
</tr>
<tr class="even">
<td>XWB GET VARIABLE VALUE</td>
<td>VARVAL</td>
<td>XWBLIB</td>
<td>SINGLE VALUE</td>
<td>This RPC accepts the name of a variable which will be evaluated and its value returned to the server. For example, this RPC may be called with a parameter like DUZ which will be returned as 123456.</td>
<td>NONE</td>
<td>NONE</td>
<td>CAPRISupport<br />
GetVariableValue<br />
<br />
Tformessoselect.<br />
Timer1Timer<br />
<br />
TfrmMain.<br />
btnVistAWebHomeClick<br />
actFileConnectExecute (called 10 times)<br />
FormatReport<br />
actToolsPurgeTransmissionMetricsExecute<br />
BitBtnVistAClick<br />
TimeoutTimerTimer<br />
<br />
TPNCSForm.<br />
CheckConnectionAndRecordLock<br />
AddToReport<br />
<br />
Tfrmreports.<br />
OneItemPerPagePrint<br />
NormalPrint<br />
<br />
TSplitExam.<br />
ProcessTextToPDF<br />
<br />
TFormTIUDisplay.<br />
Print<br />
<br />
untBrkrMthds<br />
EnsureBrokerConnected<br />
<br />
TVocRehab.<br />
GetPointOfContactIEN</td>
<td>CAPRISupport.pas<br />
essoselect.pas<br />
main.pas<br />
PNCSMain.pas<br />
REPORTS.pas<br />
SplitExamInfo.pas<br />
tiudisplayunit.pas<br />
VocRehabClass.pas</td>
<td>RPCBroker1</td>
<td>PType := reference;<br />
Value := one of the following:<br />
DUZ<br />
DUZ(0)<br />
DUZ(2)<br />
DUZ("2")<br />
DTIME</td>
</tr>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: CAPRI System Administration and Technical Guide (Updated DVBA*2.7*254)

### Veterans Health Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following link (URL) provides a complete list of VHA Medical Centers, Outpatient Clinics, Community Based Outpatient Clinics, Vet Centers, and Veterans Integrated Service Network (VISN) locations where the VHA utilizes the CAPRI system.

<https://www.benefits.va.gov/benefits/>

The level of access granted to users will depend on job function, need to know, and the level of security placed on certain sensitive patient records.

#### VHA Data Portal

This VHA program coordinates access to many of VHA's health information resources that include national databases, EHRs, extracted datasets, and medical record data found in CPRS through CAPRI and Joint Longitudinal Viewer (JLV).

### Veterans Benefits Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the VBA regional office (RO) locations with each of their VBA system name.

*Note: VBA IT continues to use the VA Office of Information Technology (OIT) naming convention method prior to its reorganization. This naming convention is organizational versus geographical in nature. This table reflects that as all VBA IT locations fall under Region 5. VHA IT currently uses the VA OIT current geographical naming convention. Additionally, VBA from a Business Line perspective doesn't use Region 5 but breaks Region 5 down into three separate NCIOs. (See map following this table).*

| VBA Region 5             |                                                                       |
|------------------------------|-----------------------------------------------------------------------|
| REGIONAL OFFICE LOCATION | SYSTEM_NAME                                                       |
| ST. PETERSBURG REGION    |                                                                       |
| Atlanta, GA                  | REGION 5 \> VBA \> St Petersburg Region \> VARO Atlanta \> LAN        |
| Baltimore, MD                | REGION 5 \> VBA \> St Petersburg Region \> VARO Baltimore \> LAN      |
| Columbia, SC                 | REGION 5 \> VBA \> St Petersburg Region \> VARO Columbia \> LAN       |
| Huntington, WV               | REGION 5 \> VBA \> St Petersburg Region \> VARO Huntington \> LAN     |
| Jackson, MS                  | REGION 5 \> VBA \> St Petersburg Region \> VARO Jackson \> LAN        |
| Little Rock, AR              | REGION 5 \> VBA \> St Petersburg Region \> VARO Little Rock \> LAN    |
| Louisville, KY               | REGION 5 \> VBA \> St Petersburg Region \> VARO Louisville \> LAN     |
| Montgomery, AL               | REGION 5 \> VBA \> St Petersburg Region \> VARO Montgomery \> LAN     |
| Nashville, TN                | REGION 5 \> VBA \> St Petersburg Region \> VARO Nashville \> LAN      |
| New Orleans, LA              | REGION 5 \> VBA \> St Petersburg Region \> VARO New Orleans \> LAN    |
| Newark, NJ                   | REGION 5 \> VBA \> St Petersburg Region \> VARO Newark \> LAN         |
| Roanoke, VA                  | REGION 5 \> VBA \> St Petersburg Region \> VARO Roanoke \> LAN        |
| St. Louis, MO                | REGION 5 \> VBA \> St Petersburg Region \> VARO St. Louis \> LAN      |
| St. Louis RMC, MO            | REGION 5 \> VBA \> St Petersburg Region \> VARO St. Louis RMC \> LAN  |
| St. Petersburg, FL           | REGION 5 \> VBA \> St Petersburg Region \> VARO St. Petersburg \> LAN |
| Washington, DC               | REGION 5 \> VBA \> St Petersburg Region \> VARO Washington \> LAN     |
| Winston-Salem, NC            | REGION 5 \> VBA \> St Petersburg Region \> VARO Winston-Salem \> LAN  |
| St. Paul Region          |                                                                       |
| Boston, MA                   | REGION 5 \> VBA \> St Paul Region \> VARO Boston \> LAN               |
| Buffalo, NY                  | REGION 5 \> VBA \> St Paul Region \> VARO Buffalo \> LAN              |
| Chicago, IL                  | REGION 5 \> VBA \> St Paul Region \> VARO Chicago \> LAN              |
| Cleveland, OH                | REGION 5 \> VBA \> St Paul Region \> VARO Cleveland \> LAN            |
| Des Moines, IA               | REGION 5 \> VBA \> St Paul Region \> VARO Des Moines \> LAN           |
| Detroit, MI                  | REGION 5 \> VBA \> St Paul Region \> VARO Detroit \> LAN              |
| Fargo, ND                    | REGION 5 \> VBA \> St Paul Region \> VARO Fargo \> LAN                |
| Hartford, CT                 | REGION 5 \> VBA \> St Paul Region \> VARO Hartford \> LAN             |
| Indianapolis, IN             | REGION 5 \> VBA \> St Paul Region \> VARO Indianapolis \> LAN         |
| Lincoln, NE                  | REGION 5 \> VBA \> St Paul Region \> VARO Lincoln \> LAN              |
| Manchester, NH               | REGION 5 \> VBA \> St Paul Region \> VARO Manchester \> LAN           |
| Milwaukee, WI                | REGION 5 \> VBA \> St Paul Region \> VARO Milwaukee \> LAN            |
| New York, NY                 | REGION 5 \> VBA \> St Paul Region \> VARO New York \> LAN             |
| Philadelphia, PA             | REGION 5 \> VBA \> St Paul Region \> VARO Philadelphia \> LAN         |
| Pittsburgh, PA               | REGION 5 \> VBA \> St Paul Region \> VARO Pittsburgh \> LAN           |
| Providence, RI               | REGION 5 \> VBA \> St Paul Region \> VARO Providence \> LAN           |
| Sioux Falls, SD              | REGION 5 \> VBA \> St Paul Region \> VARO Sioux Falls \> LAN          |
| St. Paul, MN                 | REGION 5 \> VBA \> St Paul Region \> VARO St. Paul \> LAN             |
| Togus, ME                    | REGION 5 \> VBA \> St Paul Region \> VARO Togus \> LAN                |
| White River Jct, VT          | REGION 5 \> VBA \> St Paul Region \> VARO White River Jct. \> LAN     |
| Wichita, KS                  | REGION 5 \> VBA \> St Paul Region \> VARO Wichita \> LAN              |
| Wilmington, DE               | REGION 5 \> VBA \> St Paul Region \> VARO Wilmington \> LAN           |
| SAN DIEGO REGION         |                                                                       |
| Albuquerque, NM              | REGION 5 \> VBA \> San Diego Region \> VARO Albuquerque \> LAN        |
| Anchorage, AK                | REGION 5 \> VBA \> San Diego Region \> VARO Anchorage \> LAN          |
| Boise, ID                    | REGION 5 \> VBA \> San Diego Region \> VARO Boise \> LAN              |
| Denver, CO                   | REGION 5 \> VBA \> San Diego Region \> VARO Denver \> LAN             |
| Cheyenne, WO                 | REGION 5 \> VBA \> San Diego Region \> VARO Cheyenne \> LAN           |
| Fort Harrison, MT            | REGION 5 \> VBA \> San Diego Region \> VARO Fort Harrison \> LAN      |
| Honolulu, HI                 | REGION 5 \> VBA \> San Diego Region \> VARO Honolulu \> LAN           |
| Houston, TX                  | REGION 5 \> VBA \> San Diego Region \> VARO Houston \> LAN            |
| Los Angeles, CA              | REGION 5 \> VBA \> San Diego Region \> VARO Los Angeles \> LAN        |
| Manila, PI                   | REGION 5 \> VBA \> San Diego Region \> VARO Manila \> LAN             |
| Muskogee, OK                 | REGION 5 \> VBA \> San Diego Region \> VARO Muskogee \> LAN           |
| Oakland, CA                  | REGION 5 \> VBA \> San Diego Region \> VARO Oakland \> LAN            |
| Phoenix, AZ                  | REGION 5 \> VBA \> San Diego Region \> VARO Phoenix \> LAN            |
| Portland, OR                 | REGION 5 \> VBA \> San Diego Region \> VARO Portland \> LAN           |
| Reno, NV                     | REGION 5 \> VBA \> San Diego Region \> VARO Reno \> LAN               |
| Salt Lake City, UT           | REGION 5 \> VBA \> San Diego Region \> VARO Salt Lake City \> LAN     |
| San Diego, CA                | REGION 5 \> VBA \> San Diego Region \> VARO San Diego \> LAN          |
| San Juan, PR                 | REGION 5 \> VBA \> San Diego Region \> VARO San Juan \> LAN           |
| Seattle, WA                  | REGION 5 \> VBA \> San Diego Region \> VARO Seattle \> LAN            |
| Waco, TX                     | REGION 5 \> VBA \> San Diego Region \> VARO Waco \> LAN               |

This is the VBA's Region 5 Business Line perspective Network map of CIOs:

![](capri-system-administration-and-technical-guide-updated-dvba-2-7-254/002.png)

<span id="_Toc514706685" class="anchor"></span>Figure -1 VBA's Region 5 Business Line perspective Network map of CIOs  
Veteran Service Organization (VSO)

All VSO offices are co-located with VBA regional offices as shown in the table of the previous Section 2.2.2. The VSO has authorized CAPRI read-only permissions for specific claimant's EHR. This access allows the VSO to help a veteran who is preparing a VA benefit claim.

CAPRI offers VSO users:

- A national user account option with a single access/verify code, from which authorized users can view a Veteran's entire VA health record from any site where the Veteran has been seen
- Customizable reports and health summaries
- C&P exam requests and results
- A search feature that enables users to search progress notes and discharge summaries for text
- Access to current and past AMIE C&P claims activity
- Access to Joint Longitudinal Viewer (JLV) for integrated read-only view of health data
