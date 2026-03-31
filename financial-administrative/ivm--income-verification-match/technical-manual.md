---
title: IVM Version 2 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: IVM
app_name: Income Verification Match
section: FIN
app_status: archive
pkg_ns: IVM
patch_ver: 2
patch_id: IVM*2
group_key: "IVM:IVM:2"
file_numbers: 
  - 2
  - 4
  - 101
  - 301
  - 350
  - 389
  - 392
  - 771
  - 772
security_keys: []
menu_options: 6
description: 
audience: 
keywords: 
  - class
  - table
  - strong
  - even
  - segment
  - contents
  - redacted
  - patient
  - style
  - width
page_count: 0
word_count: 44186
section_count: 119
table_count: 99
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: October 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)_Archive/ivm_2_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)_Archive/ivm_2_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=265"
---

![](ivm-version-2-technical-manual/001.png)

inCOME VERIFICATION MATCH(IVM)TECHNICAL MANUAL

October 1994

Office of Enterprise Development

Management, Enrollment and Financial Systems (MEFS)

Revision History

<table>
<caption>Revision History table</caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 41%" />
<col style="width: 21%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Project Manager (beginning 1/19/05)</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/9/01</td>
<td>Added OBX segment to ORU~Z07 HL7 Message Definition in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/9/01</td>
<td>Updated OBX segment in ORF~Z11 and ORU~Z11 HL7 Message Definitions in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/9/01</td>
<td>Updated OBX Segment Table in Appendix B to include NTR data descriptions</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/9/01</td>
<td>Added VA0052 and VA0053 to Supported/User-Defined Tables section in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/19/01</td>
<td>Added OBX segment to ORF~Z07 HL7 Message Definition in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/19/01</td>
<td>Added ORU/ORF~Z10 HL7 Message Definitions in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/19/01</td>
<td>Added sequences 24 – 26 to ZMT segment table definition in appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/19/01</td>
<td>Added sequences to 22 – 23 to ZIC Segment Table Definition in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/19/01</td>
<td>Added sequences 6 – 13 to ZCD Segment Table Definition in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/19/01</td>
<td>Added ZIV to Segment Table Definitions in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/30/01</td>
<td>Added ORU/ORF to HL7 Message Events Table in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/7/01</td>
<td>Added ORF~Z06 to HL7 Message Definitions in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/7/01</td>
<td>Updated ZMT Segment Table in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/7/01</td>
<td>Added Table VA0051 to Supported/User-Defined Tables section in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/7/01</td>
<td>Updated Table VA15 in Supported/User-Defined Tables section in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/7/01</td>
<td>Updated Table VA0035 in Supported/User-Defined Tables section in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/2/2002</td>
<td>Updated Enrollment Trigger Events section in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/10/02</td>
<td>Added ZMH Segment Table to Segment Table Definitions in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/18/02</td>
<td>Changed narrative occurrences of HL7 V. 1.5 to reflect V. 1.6</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/18/02</td>
<td>Corrected descriptions of ORU/ORF~Z10 to reflect that they are communications FROM HEC</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/22/02</td>
<td>Updated date in footers</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/23/02</td>
<td>Updated ZEL Segment Table in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/23/02</td>
<td>Added PD1 Segment Table to Segment Table Definitions in Appendix B</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/31/02</td>
<td>Updated ZMT Segment Table in Appendix B to reflect new test type</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/1/02</td>
<td>Updated HL7 Message Definitions in Appendix A HL7 to support Address Indexing</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/7/02</td>
<td>Updated HL7 Segment Table Definitions in Appendix B to support Geographic Means Test and Address Indexing</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/4/02</td>
<td>Updated HL7 Appendices B to support Geographic Means Test and Address Indexing</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/5/02</td>
<td>Updated HL7 Appendices B to support Geographic Means Test and Address Indexing</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/19/02</td>
<td>Added Sequence 34 to ZEL Segment Table Definitions in Appendix B to support Geographic Means Test and Address Indexing</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/21/02</td>
<td>Added Appendix D – HL7 Flow Diagram</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>2/11/03</td>
<td>Added Table VA0040 to Appendix D to support Enrollment Sub-Priority Group</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2/12/03</td>
<td>Updated Table VA0035 in Appendix D to support Enrollment Sub-Priority Group</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>2/14/03</td>
<td>Updated Table VA 0004 in appendix D to include Purple Heart code</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/3/03</td>
<td>Updated MSH Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/4/03</td>
<td>Added FTI Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/4/03</td>
<td>Updated PID Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/4/03</td>
<td>Updated PD1 Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/4/03</td>
<td>Updated ZIC Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/4/03</td>
<td>Updated ZDP Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/4/03</td>
<td>Updated ZIR Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/4/03</td>
<td>Updated ZIV Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/4/03</td>
<td>Updated ZMT Segment Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/4/03</td>
<td>Updated HL7 Data Types Table in Appendix B (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/4/03</td>
<td>Updated HL7 Message Definitions in Appendix A (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/4/03</td>
<td>Updated list of HL7 Segments in Appendix A (IVM*2*69)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/7/03</td>
<td>Updates per team feedback</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/13/03</td>
<td>Updated ORF/ORU~Z07, ORF/ORU~Z11 message definitions in Appendix A (IVM*2*75)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/13/03</td>
<td>Updated ZEL Segment Table in Appendix B (IVM*2*75)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/19/03</td>
<td>Updated ORU~Z05 message definition in Appendix A (IVMB*2*739)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/19/03</td>
<td>Updated EDB references in Appendix A</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/8/03</td>
<td>Updated the VA-Specific Patient Information Segment (ZPD) in Appendix B HL7 Table Segment Definitions (IVM*2*85) to accommodate the additional Date of Death enhancement information (source of notification for date of death, date of last entry or update, and submitter/user information).</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/11/03</td>
<td>Updated ORU~Z05, ORU~Z07, ORF~Z07, ORU~Z11, and ORF~Z11 message definitions in Appendix A (IVMB*2*85)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/11/03</td>
<td>Updated the VA-Specific Patient Information Segment (ZPD) in Appendix B HL7 Table Segment Definitions (IVM*2*85) 31 and 32 based on team feedback.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/3/04</td>
<td>Removed the ZPD VA-Specific Patient Info Segment Sequence #s 31 &amp; 32 (IVM*2*85) from the Demographic Data Transmission - ORU~Z05 HL7 message definition in Appendix A.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/12/04</td>
<td><p>Added ZMH to the following message definitions in Appendix A:</p>
<ul>
<li><p>ORU/ORF~Z07</p></li>
<li><p>ORU/ORF~Z11</p></li>
</ul></td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/20/04</td>
<td><p>Added ZMT VA-Specific LTC Co-Pay Exemption Test Information segment sequences 1-4,7,9-10,12,16-18,22,25 to the ORF~Z10 message definition in Appendix A (IVM*2*56)</p>
<p>Added sequences to segments QRD, QRF, ZIC and ZMT in the ORF~Z10 message definition in Appendix A (IVM*2*56)</p></td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/20/04</td>
<td>Added sequences to segments PID, ZPD, ZIE, ZEL, ZCD and OBX in the ORF~Z11 message definition in Appendix A (IVM*2*56)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/20/04</td>
<td>Updated the VA-Specific Patient Ineligible Segment (ZIE) table for seq. #s 5, 6 and 7 in Appendix B HL7 Table Segment Definitions (IVM*2*56)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/20/04</td>
<td>Updated the VA-Specific Military History Segment (ZMH) table for seq. #s 2, 3 and 4 in Appendix B HL7 Table Segment Definitions (IVM*2*56)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/20/04</td>
<td>Added Table VA038 - Military History Type in Appendix D - Supported/User-Defined VA HL7 Tables (IVM*2*56)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/24/04</td>
<td>Updated the VA-Specific Emergency Contact Segment (ZCT) table TBL# for SEQ 8 &amp; 9 from VA01 To VA001 in Appendix B HL7 Table Segment Definitions (IVM*2*56)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/24/04</td>
<td>Updated the VA-Specific Patient Eligibility Segment (ZEL) table TBL# for seq. #s 2, 5, 8, 10, and 14-20 in Appendix B HL7 Table Segment Definitions (IVM*2*56). Also added missing information for seq. 29, Agent Orange Exposure Location, and new seq. #s 36, 37 and 38 in same VA-Specific Patient Eligibility Segment (ZEL) table.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/27/04</td>
<td>Added ZEL sequences 29, 37 &amp; 38 to the ORU~Z07/ ORF~Z07 message definitions in Appendix A (IVM*2*56)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/3/04</td>
<td>Added COMBAT VETERAN END DATE (.5295) Enrollment Trigger Event to the <em>Trigger Events Implemented via Cross-References</em> table in Appendix A (IVM*2*56)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/6/04</td>
<td>Added ZEL sequence 22 to the ORF/ORU~Z07 HL7 message definitions and ZEL sequence 38 to the ORF/ORU~Z11 HL7 message definitions in Appendix A. Added sequence 33, Filipino Veteran Proof, to the ZPD (VA Specific Patient Info Segment) HL7 Segment Table Definitions in Appendix B. Added ZPD sequence 33 to the ORF/ORU~Z07 HL7 message definition in Appendix A. Added new Table VA048 - Filipino Veteran Proof in Appendix D. (IVM*2*97)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/19/04</td>
<td>Corrected Sequence 24 in the VA-Specific Patient Eligibility Segment (ZEL) table in Appendix B.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/29/04</td>
<td>Updated table of contents to include ZMH segment table and several supported HL7 reference tables.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/04/04</td>
<td><p>Added PID (Patient Identification Segment) sequence 2, PD1 Patient Demographic 1 Segment (SEQ 3), ZMT VA-Specific Means Test Information Segment sequences 22-29, ZMT VA-Specific LTC Test Information Segment (SEQ 1-5,7,9-10,12,16-18,22,25), ZCD VA-Specific Catastrophic Disability Segment sequences 6-13, ZIC VA-Specific Income Segment sequences 22 &amp; 23, and OBX Observation/Result Segment sequence 12 to the ORF/ORU~Z07 HL7 message definitions in Appendix A.</p>
<p>Deleted Sequences 5-12 in the Patient Demographic 1 Segment (PD1) table in the HL7 Segment Table Definitions in Appendix B.</p></td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/10/04</td>
<td>Added curly brackets indicating a repeating segment to the ZMH segment in the ORF/ORU~Z07/Z11 HL7 message definitions in Appendix A.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>01/04/05</td>
<td>Checked and updated for 508 compliance by adding alt text to graphics.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/19/05</td>
<td>Updates to ORU~Z05 message definition in Appendix A</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/19/05</td>
<td>Updates to ZPD segment element names in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/22/05</td>
<td>Updated ZPD segment, sequence length of Sequence 33, in Appendix B per email discussion with ESR team members</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/22/05</td>
<td>Added Table 0048 to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/22/05</td>
<td>Added Table 0126 to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/22/05</td>
<td>Updated ORU~Z07 message definition in Appendix A per email from Laurie Sheppard</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/22/05</td>
<td>Added supplemental data tables following the ZMH segment table in Appendix B per email from Pat Wilson</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0017 (Transaction Type) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0105 (Source of Comment) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0005 (Race) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0006 (Religion) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0189 (Ethnic Group) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0136 (Yes/No Indicator) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0106 (Query/Response Format Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0091 (Query Priority) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0108 (Query Results Level) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0125 (Value Type) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0078 (Abnormal Flags) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0080 (Nature of Abnormal Testing) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0085 (Observation Result Status Codes Interpretation) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0283 (Referral Status) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0280 (Referral Priority) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0281 (Referral Type) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table 0282 (Referral Disposition) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/25/05</td>
<td>Added Table 0283 (Referral Category) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/25/05</td>
<td>Added Table VA041 (Determination Method) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added Table VA042 (Affected Extremity) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added Table VA043 (Condition Codes) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added Table VA045 (CD Permanent Indicator) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added Table VA017 (Enrollment Priority) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added Table VA022 (Radiation Exposure Method) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added Table VA036 (Military Sexual Trauma Status) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added placeholder for Table VA010 (Means Test Indicator) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table VA060 (Type of Financial Test) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added Table VA012 (Type of Insurance) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table 0176 (Master File Application Identifier) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added placeholder for Table 0102 (Delayed Acknowledgement Type) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added Table 0155 (Accept/Application Acknowledgement Conditions) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added Table 0211 (Alternate Character Sets) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added Table 0356 (Alternate Character Set Handling Scheme) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Removed Table VA021 (Enrollment Priority) from Appendix D. (Replaced by Table VA017).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added code column to Table VA033 (Fee Basis Treatment Code Type)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added code column to Table VA034 (Fee Basis Program)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Changed column heading Value to Code in all tables in Appendices C and D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added placeholder for Table 0072 (Insurance Plan ID) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table 0132 (Transaction Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added placeholder for Table 0024 (Fee Schedule) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table 0049 (Department Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added placeholder for Table 0018 (Patient Type) to Appendix C)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table 0051 (Diagnosis Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added placeholder for Table 0084 (Performed by Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table 0088 (Procedure Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added Placeholder for Table 0340 (Procedure Code Modifier) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table 0296 (Primary Language) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/29/05</td>
<td>Added placeholder for Table 0171 (Citizenship) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/29/05</td>
<td>Added placeholder for Table 0172 (Veterans Military Status) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Added Table VA010 (Means Test Indicator) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Added Table 0132 (Transaction Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Added Table VA060 (Type of Financial Test) to Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Removed placeholder for Table 0176 (Master File Application Identifier) in Appendix C; removed references from all segment tables in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Added Table 0024 (Fee Schedule) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Added Table 0018 (Patient Type) to Appendix C)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Added Table 0102 (Delayed Acknowledgement Type) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Added Table 0049 (Department Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Added Table 0051 (Diagnosis Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Removed placeholder for Table 0084 (Performed by Code) in Appendix C; removed references from all segment tables</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Added Table 0088 (Procedure Code) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Added Table 0340 (Procedure Code Modifier) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Removed placeholder for Table 0296 (Primary Language) from Appendix C; removed references from all segment tables in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Removed placeholder for Table 0171 (Citizenship) to Appendix C; removed references from all segment tables in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Added Table 0172 (Veterans Military Status) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Removed placeholder for Table 0072 (Insurance Plan ID) from Appendix C; removed references from all segment tables in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Removed references to IV tables from ZIV segment table in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Removed Table 0132 (Transaction Code) from Appendix C; removed reference from the FTI segment table in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/4/05</td>
<td>Updated the FTI segment table in Appendix B based on email from Pat.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/4/05</td>
<td>Updated the ZIV segment table in Appendix B based on email from Pat.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/20/05</td>
<td>Updated ZPD segment table in Appendix B (IVM*2.0*113)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/20/05</td>
<td>Updated ORU~Z07, ORF~Z07, ORU~Z11, and ORF~Z11 message definitions in Appendix A (IVM*2.0*113)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/22/05</td>
<td>Updated Enrolment Trigger Events in Appendix A</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/25/05</td>
<td>IVM Address Change Log File #301.7 added to Files List (IVM*2*108)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/16/05</td>
<td>IVM*2*109 – Enrollment VistA Changes Early Release – updated Table VA004 in Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/16/05</td>
<td>IVM*2*109 – Enrollment VistA Changes Early Release – updated Table VA015 in Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>2/9/06</td>
<td>IVM*2*109 – Enrollment VistA Changes Early Release – updated ZEL segment in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2/9/06</td>
<td>IVM*2*109 – Enrollment VistA Changes Early Release – modified the ORU~Z07 and ORF~Z07 message definitions in Appendix A</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>2/9/06</td>
<td>IVM*2*109 – Enrollment VistA Changes Early Release – modified the ORU~Z11 and ORF~Z11 message definitions in Appendix A</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/16/06</td>
<td>IVM*2*114 -Updated ORU~Z07, ORF~Z07, and ORF~Z11 message definitions in Appendix A</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/16/06</td>
<td>IVM*2*114 -Added Table VA026 Military Service Component in Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/18/06</td>
<td>IVM*2*114 -Updated Enrollment Trigger Events in Appendix A</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/19/06</td>
<td>IVM*2*114 -Updated ZPD segment table in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/22/06</td>
<td>IVM*2*105 – Enrollment VistA Changes Release 1 - Modified the ORU~Z07 and ORF~Z07 message definitions in Appendix A</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/22/06</td>
<td><p>IVM*2*105 – Enrollment VistA Changes Release 1 – updated the following segments in Appendix B:</p>
<ul>
<li><p>RF1</p></li>
<li><p>ZCT</p></li>
<li><p>ZDP</p></li>
<li><p>ZEL</p></li>
<li><p>ZIO</p></li>
<li><p>ZIR</p></li>
<li><p>ZMT</p></li>
<li><p>ZTA</p></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/23/06</td>
<td>IVM*2*105 – Enrollment VistA Changes Release 1 – Added a portion of Table 0115 (Servicing Facility) to Appendix C</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/13/06</td>
<td>IVM*2*21 (released 8/19/99) – National Reenrollment (a.k.a. Enrollment Phase Two) – removed Eligibility Code 21 (Catastrophically Disabled) from Table VA004 in Appendix D</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/30/06</td>
<td>DG*5.3*656 – Add Field Triggers for ORU~Z07s – added enrollment trigger events to Appendix A for multiple fields listed in patch description</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/14/06</td>
<td>Retrofit changes made by REDACTED for IVM*2*114 - Operation Enduring &amp; Iraqi Freedom (Z07 Enhancements) (See Revision History entries for 3/16/06-3/19/06.)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/12/2006</td>
<td>DG*5.3*656 – Add Field Triggers for ORU~Z07s – removed enrollment trigger events from Appendix A for five fields listed in patch description</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/28/06</td>
<td>IVM*2*105 – Enrollment VistA Changes Release 1 – Additional updates to segment tables in Appendix B</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/19/06</td>
<td>IVM*2*105 – Enrollment VistA Changes Release 1 – Updated footers to reflect correct release month and patch number</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/12/07</td>
<td>IVM*2*105 – Enrollment VistA Changes Release 1 – Updated footers to reflect correct release month and patch number. Removed Draft indicators.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/23/08</td>
<td>IVM*2*115 - Enrollment VistA Changes Release 2 – Changed Environmental Contaminants to SW Asia Conditions. Updated ORU~Z10, ORF~Z10, ORU~Z11 &amp; ORF~Z11 sections. Appendix B – HL7 Segment Table Definition updates.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/30/08</td>
<td>IVM*2*115 - Enrollment VistA Changes Release 2 – Updated ORU~Z07 &amp; ORF~Z07 sections.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/4/08</td>
<td>IVM*2*115 - Enrollment VistA Changes Release 2 – Updated footer date to reflect new Release Date. Changed <em>Austin Automation Center(AAC)</em> to <em>Austin Information Technology Center(AITC)</em>.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/07/08</td>
<td>IVM*2*115 - Enrollment VistA Changes Release 2 – Updated Z06, Z10 &amp; Z11 sections per SQA . Removed Draft indicators.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/18/09</td>
<td>IVM*2*115 - Enrollment VistA Changes Release 2 – Updated footers to reflect new Release Date.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/10/09</td>
<td>DG*5.3*803 – Relaxed Priority Group 8 Changes – Added Code 8 to Table VA017 in Appendix D. Added sub-categories ‘b’ and ‘d’ to Table VA035 in Appendix D.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/16/09</td>
<td><p>IVM*2*121 –Veteran Online Applications</p>
<p>Changes- Updated IVM Transmission Error Processing Option. Added IVM Upload Insurance Screen. Added new sequence fields to HL7 messages.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/19/10</td>
<td><p>IVM*2*121 –Veteran Online Applications</p>
<p>Changes – Updated ZCT, ZPD sequences of ORU~Z04, ZPD, ZRD, ZDP seq. of ORU~Z07, ZPD, ZEM, ZDP seq. of ORF~Z07, ZDP seq. of ORU~Z10, ZDP seq. of ORF~Z10, ZDP seq. of ORU~Z11 data transmissions.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/27/10</td>
<td><p>IVM*2*121 –Veteran Online Applications</p>
<p>Changes – Enrollment Trigger Events Implemented via File Cross-References were added.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/25/10</td>
<td><p>IVM*2*121 –Veteran Online Applications</p>
<p>Changes – ESR 3.1_<em>CCR10343</em> - removed PID-24 from the Z05 message.<br />
<em>CCR10345</em> - removed ZPD-6 &amp; ZPD-7 from the Z05 &amp; Z07 messages.<br />
<em>CCR10346</em> - removed ZEM-4 &amp; ZPD-6 from the Z07 messages for the Veteran.</p>
<p>Made changes to the ORF~Z07 PID segment to match the ORU~Z07 PID segment.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/7/11 – 3/16/11</td>
<td><p>IVM*2*TM_PF</p>
<p>DG*5.3*838 made changes to Preferred Facility and the Z11 receiver; no associated IVM patch was necessary.</p>
<p>Changes ESR 3.5_CR9620 –</p>
<p>Added ZEN-14 to the ORF-Z11 and ORU-Z11 messages.</p>
<p>Added Preferred Facility to the Triggers</p>
<p>Added ZEN 14 to the ZEN HL7 Message Segment</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/1/11</td>
<td><p>IVM*2*151 –Add a Person Changes – ESR 3.5</p>
<p><em>CCR10441</em> – reversal of code to allow ORU-Z05 ZTA, ZEM and ZCT segments</p>
<p><em>CCR10442</em> – reversal of code to allow ZPD-6 &amp; ZPD-7 in the Z05 and Z07 messages</p>
<p><em>CCR10443</em> – reversal of code to allow ZEM-4 &amp; ZPD-6 in the Z07 message</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/12/11</td>
<td><p>IVM*2*151 –Add a Person Changes – ESR 3.5</p>
<p>Removed Draft indicator for final. Updated footer date from July to December.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/19/2011</td>
<td><p>IVM*2.0*141 - Updated ZMH tables</p>
<ul>
<li><p>Added information to SL, SNL, and SNNL rows</p></li>
<li><p>Added MSD service indicators/qualifiers identified for the ZMH segment.</p></li>
</ul></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/30/2011</td>
<td>IVM*2.0*141 - Added MSD to the VA038 – Military History Type Table, updated footer dates to new Release Date.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/5/2011</td>
<td>IVM*2.0*141 - TW Review, minor formatting, removed Draft indicator for final review.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/26/2012</td>
<td><p>IVM*2*150 –VBA Pension Data Sharing Changes – ESR 3.6</p>
<p>New HL7 message segment ZE2 added to patient data exchange table, and to ORU~Z07, ORF~Z07, QRY, ORF~Z11, ORU~Z11 message definitions. Added <em>Pension Award</em> trigger events in Appendix A table. Added <em>VA-Specific Patient Eligibility (Addtl) Segment (ZE2)</em> table in seg. definition section in Appendix B. Added SEQ. 12&amp;13 <em>(Class II Dental)</em> to <em>VA-Specific Service Period Segment (ZSP)</em> table seg. definition section in Appendix B.</p>
<p>TW Review – updated footers, formatting.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/24/2012</td>
<td><p>IVM*2.0*152 – Permanent Address Verification Changes – ESR 3.8</p>
<p>Add new Referral Type PHH to RF1 segment</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/8/2013</td>
<td><p>IVM*2.0*152 – Permanent Address Verification Changes – ESR 3.8</p>
<p>Updated footer date to December 2012 Release date.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/16/2015</td>
<td>IVM*2.0*158 – Catastrophic Disability Descriptor Changes – ES 4.1, ZCD segment changes; added VA440 table</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/12/2015</td>
<td><p>IVM*2.0*160 – Contributed to Spouse and BT Financial Indicator Changes –</p>
<p>add Contributed to Spouse Indicator to VA-Specific Income Relation Segment (ZIR) HL7 Segment Table;</p>
<p>add BTFI to the VA-Specific Means Test Information Segment (ZMT) HL7 Segment Table;</p>
<p>add Contributed to Spouse - ZIR 15 to the ORF-Z07, ORU-Z07, ORF-Z10 and ORU-Z10 messages;</p>
<p>add BT Financial Indicator - ZMT 31 sequence to the ORU-Z06, ORF-Z07, ORU-Z07, ORF-Z10 and ORU-Z10 messages.</p>
<p>DG*5.3*906 – ACA Preference – add “ACA Preference” to Cancelled/Declined table</p>
<p>DG*5.3*871 – Health Benefit Plan –</p>
<p>add ZHP to the HL7 Segments;</p>
<p>add ZHP segment to the ORF-Z07, ORU-Z07, ORF-Z11 and ORU-Z11 messages; and</p>
<p>add VA-Specific Health Benefit Plan Segment (ZHP) to the HL7 Segment Tables.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/05/2015</td>
<td>TW review; DG_53_P891</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/23/15</td>
<td><p>DG*5.3*890 – Added Contributed to Spousal Support (E40822^DGRTRIG) to Trigger Events</p>
<p>TW review</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/21/2016</td>
<td><p>IVM*2.0*161 – Updated ZEL segment in ORU~Z07, ORF~Z07, ORF~Z11, and ORU~Z11 (Appendix A pp. 23, 25, 30, 31)</p>
<p>Added CL-V trigger information (pp. 36-37)</p>
<p>Added Camp Lejeune fields to the ZEL segment (p. 48).</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>09/06/2017</td>
<td><p>DG*5.3*940 – Modified the ORU/ORF-Z11 message definitions on pages 30 and 31. Sequence 15 was added to the ZEN segment of these message definitions.</p>
<p>Modified Appendix B - VA-Specific Enrollment Segment (ZEN). Added Sequence 15: Reason For Closed Application (Page 50).</p>
<p>Modified Appendix D Table VA015 Enrollment Status. Code 24 - Closed Application added to table (page 82).</p>
<p>New table VA117 - Reason For Closed Application added to Appendix D (Page 87).</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/06/2017</td>
<td><p>DG*5.3*935 – Modified the ORU/ORF~Z11 message definitions on pages 30 and 31. Sequence 8 was added to the ZMH segment of these message definitions. Updated ZMH table (Appendix B p. 56) to include Future Discharge Date (Seq 8).</p>
<p>IVM*2*167 - Updated ZMH table (Appendix B p. 56) with note that FDD will not occur on the ORU-07 and ORF-Z07.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/24/2018</td>
<td>DG*5.3*947 – Reason for Early Separation: Modified the ORU/ORF~Z11 message definitions on pages 30 and 31. Sequence 9 was added to the ZMH segment of these message definitions. Updated ZMH table (Appendix B p. 55) to include Reason for Early Separation (Seq 9).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/05/2018</td>
<td><p>DG*5.3*941 - Updated Table 0363 Source of Address to include VET360 code (p. 77).</p>
<p>IVM*2.0*164 – Added VA-Specific Address Validation Segment ZAV to HL7 Message Segment Table (p. 18), ORU~Z05 Transmission (p. 20), ORU~Z07 Transmission (p. 23), and ORF~Z07 Transmission (p. 25); Updated Enrollment Trigger Events Table to include field RESIDENTIAL ADDR CHANGE DT/TM (#.1158) with the PATIENT(#2) File (p. 32); Updated IVM Trigger Events Table to include Residential Address Cross-References IVM1151 – IVM1157 and IVM11571 – IVM11573 (p. 37); Added VA-Specific Address Validation Segment (ZAV) Table (p. 46).</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>01/21/2019</td>
<td>IVM*2.0*175 – Reason for Early Separation Code: Modified the ORU/ORF~Z11 message definitions on pages 30 and 31. Sequence 10 was added to the ZMH segment of these message definitions. Updated ZMH table (Appendix B p. 56) to include Reason for Early Separation Code (Seq 10).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/21/2019</td>
<td>IVM*2.0*172 – Other Health Insurance (OHI) to VistA: Updated the Insurance Segment (IN1) Table (Appendix B p. 40) to include VISTA Element Name and VISTA File Field or Expression for Insured’s Date of Birth (Seq. 18). Updated VA-Specific Message Processing Segment (ZIV) Table (Appendix B p. 54) to include Source of Information Code (Seq. 13).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>09/09/2019</td>
<td>IVM*2.0*180 – Updated ORU~Z07 and ORF~Z07 to include 7<sup>th</sup> – 10<sup>th</sup> sequence numbers in ZIO segment (p. 23, p. 25); Updated ORF~Z11 and ORU~Z11 to include ZIO segment (p. 30, p. 31); Updated ZIO segment to include Original Appointment fields 7 – 10 (p. 53).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/02/2019</td>
<td>IVM*2.0*183 – Medal of Honor (MOH) Awardees in Priority Group 1: Updated VA-Specific Military History Segment (ZMH) tables (Appendix B p. 57 and 58) to include MOH data elements in the existing fields.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/16/2020</td>
<td>IVM*2.0*184 – OTH: Updated ZEL segment to include OTH fields (#45-#47) and added new ZTE segment (p. 63-65).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/20/2020</td>
<td>IVM*2.0*191 – Updated the 4<sup>th</sup> sequence of a QRD segment in a QRY message to pass in the Integration Control Number (ICN) along with the patient’s DFN (p.30). Updated QRD table to change the length of the 4<sup>th</sup> sequence to 23 characters and add the ICN to be included in with the patient DFN (Appendix B p.43).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>03/27/2020</td>
<td>DG*5.3*1011 - EMERGENCY RESPONSE - PANDEMIC WORKLOAD REPORTING: Updated VA-Specific Patient Information Segment (ZPD) Table, SEQ 40 Emergency Response Indicator, to EMERGENCY RESPONSE INDICATOR Field (#.181) Value: P - PANDEMIC (p. 61).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/10/2020</td>
<td>IVM*2.0*193 - NOK/E-Contact Foreign Address, Hardship Expiration: Change<br />
ZGD 2 from required to optional in VA-Specific Guardian Segment (ZGD) Table (p. 51); added SEQ 32 to ZMT Segment of ORU-Z07 (p. 23), ORF-Z07 (p. 25), ORU-Z10 (p. 28), and ORF-Z10 (p. 29); added SEQ 32, Hardship Expiration Date to VA-Specific Means Test Information Segment (ZMT) Table, (p. 59).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/24/2020</td>
<td>IVM*2.0*162 – Registration Only Enrollment Status: Updated ORU~Z11 and ORF-Z11 to include 16<sup>th</sup> -19<sup>th</sup> sequence numbers in ZEN segment (p. 30, p. 31); Updated VA-Specific Enrollment Segment (ZEN) table to include 16<sup>th</sup>-19<sup>th</sup> sequence numbers (p. 50 - 51).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/02/2020</td>
<td><p>IVM*2.0*194: Added VA-Specific Community Care Eligibility Segment (ZCE) to HL7 Message Segments Table (p. 18); added ZCE Segment to ORU-Z07 (p. 23 ), ORF-Z07 (p. 25), ORF-Z11 (p. 30) and ORU-Z11 (p. 31); added ACCCP cross-references to Enrollment Trigger Events Table (p. 34); added VA-Specific Community Care Eligibility Segment (ZCE) Table (p. 47).</p>
<p>IVM*2.0*162 – Registration Only Enrollment Status: Updated Table VA015 Enrollment Status to include Code 25 Registration Only (p. 87).</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/14/2020</td>
<td>IVM*2.0*197: Added Table VA018 - Agency/Allied Country to Appendix D: Supported/User-Defined VA HL7 Tables (p. 87).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>03/18/2021</td>
<td>IVM*2.0*199: Updated Table VA018 – Agency/Allied Country to include 20 additional federal agencies (p. 87).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>04/07/2021</td>
<td>IVM*2.0*200: Updated Table VA018 – Agency/Allied Country to include 7 additional federal agencies (p. 87).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>06/30/2021</td>
<td><p>IVM*2.0*196: Renamed “ENROLLMENT APPLICATION DATE” to “APPLICATION DATE” (p. 33, 49).</p>
<p>Added missing update related to patch DG*5.3*993: Added Table VA0047 – PATIENT REGISTRATION ONLY REASON (p. 91)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>06/30/2021</td>
<td>IVM*2.0*198 – Add Space Force Branch of Service: Updated Table VA011 Period of Service to change “AIR FORCE—ACTIVE DUTY” to “USAF, USSF - ACTIVE DUTY” (p. 85).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>09/23/2021</td>
<td>IVM*2.0*201 – Send user identifying information and change date/time in newly created ZUD segment of HL7 ORU/ORF~Z07 when contact information is modified (p. 24 and p. 26; ZUD – VA Specific VistA User Data Segment Table, p. 65).</td>
<td>REDACTED</td>
<td><p>PM: REDACTED</p>
<p>Auth: Liberty ITS TW</p></td>
</tr>
<tr class="even">
<td>10/11/2021</td>
<td>IVM*2.0*202 – Added new eligibility codes (24 – COMPACT ACT ELIGIBLE and 25 – SPECIAL TX AUTHORITY CARE) to Table VA004 – Eligibility (p. 82).</td>
<td>REDACTED</td>
<td><p>PM: REDACTED</p>
<p>Auth: Liberty ITS TW</p></td>
</tr>
<tr class="odd">
<td>02/22/2022</td>
<td><p>IVM*2.0*204 – Added new contact types in Sequence #11 for ZCT segment in ORU/ORF~Z05 and ORU/ORF~Z07 (p. 20, 21, 23, 25); added enrollment trigger events for religious preference, race, and ethnicity to Trigger Events Implemented via File Cross-References Table (p. 32); added SEQ 11 to VA-Specific Emergency Contact Segment (ZCT) Table (p. 46).</p>
<p>In addition, made the following corrections to the manual: Added ZUD segment to the HL7 Message Segments Table (p. 18); fixed repeating segments for the Demographic Data Transmission (ORU~Z05) (p. 20); added ZPD segment sequence 41 to VA-Specific Patient Information Segment (ZPD) Table (p. 62).</p></td>
<td>REDACTED</td>
<td><p>PM: REDACTED</p>
<p>Auth: Liberty ITS TW</p></td>
</tr>
<tr class="even">
<td>07/05/2022</td>
<td>IVM*2.0*206 – Added new eligibility<br />
code 26 – HUD-VASH to<br />
Table VA004 – Eligibility (p. 82)</td>
<td>REDACTED</td>
<td><p>PM: REDACTED</p>
<p>Auth: Booz Allen Hamilton TW</p></td>
</tr>
<tr class="odd">
<td>08/08/2022</td>
<td>IVM*2.0*203 – Added SEQ 42 – 45 to ORU/ORF~Z07 ZPD Segment (p. 23 and 25) and SEQ 41 – 45 to ORF/ORU~Z11 Segment (p. 29 and 30); added SEQ 41 – 45 to VA-Specific Patient Information Segment (ZPD) Table (p. 62).</td>
<td>REDACTED</td>
<td><p>PM: REDACTED</p>
<p>Auth: Booz Allen Hamilton TW</p></td>
</tr>
<tr class="even">
<td>09/12/2022</td>
<td>IVM*2.0*207 – Updated Table VA004 – Eligibility with new eligibility code 27 – CLINICAL EVALUATION (p. 82)</td>
<td>REDACTED</td>
<td><p>PM: REDACTED</p>
<p>Auth: Booz Allen Hamilton TW</p></td>
</tr>
<tr class="odd">
<td>12/27/2022</td>
<td>IVM*2.0*208 – Added new Health Factor segment ZHF to ORF/ORU~Z07 and ORF/ORU~Z11 (p. 23, 25, 29, 30, 48-49).</td>
<td>REDACTED</td>
<td><p>PM: REDACTED</p>
<p>Auth: Booz Allen Hamilton TW</p></td>
</tr>
<tr class="even">
<td>02/27/2023</td>
<td><p>IVM*2.0*210 – Added SEQ 46 – 47 to ORU~Z05 ZPD Segment (p. 20), ORU/ORF~Z07 ZPD Segment (p. 23 and 25), and VA-Specific Patient Information Segment (ZPD) Table (p. 61).</p>
<p>Added PREFERRED LANGUAGE to Trigger Events Implemented via File Cross-References Table (p. 32).</p></td>
<td>REDACTED</td>
<td>PM: REDACTED Auth: Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>04/20/2023</td>
<td>IVM*2.0*211 – Added Codes 5 – 10 to Table VA022 Radiation Exposure Method (p. 87).</td>
<td>REDACTED</td>
<td>PM: REDACTED Auth: Booz Allen Hamilton TW</td>
</tr>
<tr class="even">
<td>12/11/2023</td>
<td>IVM*2.0*213 – Added SEQ 48 to ORF/ORU~Z11 ZEL Segment (p. 29 and 30) and VA-Specific Patient Eligibility Segment (ZEL) Table (p. 48).</td>
<td>REDACTED</td>
<td>PM: REDACTED Auth: Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>04/15/2024</td>
<td>IVM*2.0*214 – Upload PHONE NUMBER [WORK] directly to Patient (#2) File (Referral Information Segment (RF1) Table, p.44).</td>
<td>REDACTED</td>
<td>PM: REDACTED Auth: Booz Allen Hamilton TW</td>
</tr>
<tr class="even">
<td>10/23/2024</td>
<td><p>Applied updated VA OIT Template to document.</p>
<p>IVM*2.0*215 – Added SEQ 49, 50 to ORF/ORU~Z11 and ORF/ORU~Z07 ZEL Segment (p. 24, 26, 32-33 and VA-Specific Patient Eligibility Segment (ZEL) Table, p. 62); added SEQ 10 to ORF/ORU~Z05 and ORU~Z07 ZTA Segment (p. 24, 26 and VA-Specific Temporary Address Segment (ZTA) Table, p. 83).</p></td>
<td>REDACTED</td>
<td>PM: REDACTED Auth: Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>09/05/2025</td>
<td>IVM*2.0*217 – Added PHC identifier in ORF/ORU~Z05 RF1 Segment and ORF/ORU~Z07 RF1 Segment for Confidential Phone Number (Appendix B RF1 Table, p. 55 – 56).</td>
<td>REDACTED</td>
<td>PM: REDACTED Auth: Booz Allen Hamilton TW</td>
</tr>
</tbody>
</table>

Revision History table

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Background](#background)
  - [Functionality](#functionality)
- [Implementation and Maintenance](#implementation-and-maintenance)
- [Routines](#routines)
  - [Callable Routines](#callable-routines)
  - [Routines to Map](#routines-to-map)
  - [Routine List](#routine-list)
- [Files](#files)
  - [Globals to Journal](#globals-to-journal)
  - [File List](#file-list)
  - [File Flow (Relationships Between Files)](#file-flow-relationships-between-files)
- [Exported Options](#exported-options)
  - [Menu Diagram](#menu-diagram)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Package-wide Variables](#package-wide-variables)
  - [SACC Exemptions/Non-Standard Code](#sacc-exemptionsnon-standard-code)
- [External/Internal Relations](#externalinternal-relations)
  - [External Relations](#external-relations)
  - [DBIA Agreements](#dbia-agreements)
  - [Internal Relations](#internal-relations)
- [Security](#security)
  - [Security Management](#security-management)
  - [Security Keys](#security-keys)
  - [VA FileMan Access Codes](#va-fileman-access-codes)
- [How to Generate On-line Documentation](#how-to-generate-on-line-documentation)
  - [Xindex](#xindex)
  - [List File Attributes](#list-file-attributes)
- [Glossary](#glossary)
- [Appendix A – IVM Data Transmissions](#appendix-a-ivm-data-transmissions)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [General](#general)
  - [Communications Protocol](#communications-protocol)
  - [Background Messages](#background-messages)
  - [Batch Messages](#batch-messages)
  - [HL7 Message Event Types](#hl7-message-event-types)
  - [HL7 Message Segments](#hl7-message-segments)
  - [HL7 Message Definitions](#hl7-message-definitions)
    - [SSN Data Transmission – (ORUZ03)](#ssn-data-transmission-oruz03)
    - [Insurance Data Transmission – (ORUZ04)](#insurance-data-transmission-oruz04)
    - [Demographic Data Transmission – (ORUZ05)](#demographic-data-transmission-oruz05)
    - [Date of Death Transmission – (ORUZ05)](#date-of-death-transmission-oruz05)
    - [Guardian Data Transmission – (ORUZ05)](#guardian-data-transmission-oruz05)
    - [Means Test Data Transmission – (ORFZ06) NOTE: This message has been retired.](#means-test-data-transmission-orfz06-note-this-message-has-been-retired)
    - [Means Test Data Transmission – (ORUZ06)](#means-test-data-transmission-oruz06)
    - [Full Data Transmission – (ORUZ07)](#full-data-transmission-oruz07)
    - [Full Data Transmission – (ORFZ07)](#full-data-transmission-orfz07)
    - [Case Status Data Transmission – (ORUZ08) (Message has been retired)](#case-status-data-transmission-oruz08-message-has-been-retired)
    - [Billing/Collection Data Transmission – (ORUZ09)](#billingcollection-data-transmission-oruz09)
    - [Billing/Collection Data Transmission – (ORUZ09)](#billingcollection-data-transmission-oruz09-1)
    - [Income Test Data Transmission – (ORUZ10)](#income-test-data-transmission-oruz10)
    - [Income Test Data Transmission – (ORFZ10)](#income-test-data-transmission-orfz10)
    - [VISTA Initiated – Enrollment/Eligibility Query Data Transmission – (QRY)](#vista-initiated-enrollmenteligibility-query-data-transmission-qry)
    - [Enrollment/Eligibility Data Transmission – (ORFZ11)](#enrollmenteligibility-data-transmission-orfz11)
    - [Enrollment/Eligibility Data Transmission – (ORUZ11)](#enrollmenteligibility-data-transmission-oruz11)
  - [Trigger Events](#trigger-events)
    - [Enrollment Trigger Events](#enrollment-trigger-events)
    - [IVM Trigger Events](#ivm-trigger-events)
- [# Appendix B – HL7 Segment Table Definitions](#appendix-b-hl7-segment-table-definitions)
  - [HL7 Abbreviated Column Headings](#hl7-abbreviated-column-headings)
  - [HL7 Data Types](#hl7-data-types)
  - [HL7 Segment Tables](#hl7-segment-tables)
    - [Financial Transaction (FTI)](#financial-transaction-fti)
    - [Insurance Segment (IN1)](#insurance-segment-in1)
    - [Notes and Comments Segment (NTE)](#notes-and-comments-segment-nte)
    - [Patient Identification Segment (PID)](#patient-identification-segment-pid)
    - [Patient Demographic 1 Segment (PD1)](#patient-demographic-1-segment-pd1)
    - [Query Definition Segment (QRD)](#query-definition-segment-qrd)
    - [Observation/Result Segment (OBX)](#observationresult-segment-obx)
    - [Query Filter Segment (QRF)](#query-filter-segment-qrf)
    - [Referral Information Segment (RF1)](#referral-information-segment-rf1)
    - [VA-Specific Address Validation Segment (ZAV)](#va-specific-address-validation-segment-zav)
    - [VA-Specific Beneficiary Travel Segment (ZBT)](#va-specific-beneficiary-travel-segment-zbt)
    - [VA-Specific Catastrophic Disability Segment (ZCD)](#va-specific-catastrophic-disability-segment-zcd)
    - [VA-Specific Community Care Eligibility Segment (ZCE)](#va-specific-community-care-eligibility-segment-zce)
    - [VA-Specific Emergency Contact Segment (ZCT)](#va-specific-emergency-contact-segment-zct)
    - [VA-Specific Patient Dependent Information Segment (ZDP)](#va-specific-patient-dependent-information-segment-zdp)
    - [VA-Specific Patient Eligibility Segment (ZEL)](#va-specific-patient-eligibility-segment-zel)
    - [VA-Specific Health Factor Segment (ZHF)](#va-specific-health-factor-segment-zhf)
    - [VA-Specific Patient Eligibility (Addtl) Segment (ZE2)](#va-specific-patient-eligibility-addtl-segment-ze2)
    - [VA-Specific Employment Information Segment (ZEM)](#va-specific-employment-information-segment-zem)
    - [VA-Specific Enrollment Segment (ZEN)](#va-specific-enrollment-segment-zen)
    - [VA-Specific Fee Basis Segment (ZFE)](#va-specific-fee-basis-segment-zfe)
    - [VA-Specific Guardian Segment (ZGD)](#va-specific-guardian-segment-zgd)
    - [VA-Specific Income Information Segment (ZIC) – old format](#va-specific-income-information-segment-zic-old-format)
    - [VA-Specific Income Information Segment (ZIC) – Feb 2005 1010EZ format](#va-specific-income-information-segment-zic-feb-2005-1010ez-format)
    - [VA-Specific Health Benefit Plan Segment (ZHP)](#va-specific-health-benefit-plan-segment-zhp)
    - [VA-Specific Patient Ineligible Segment (ZIE)](#va-specific-patient-ineligible-segment-zie)
    - [VA-Specific Inpatient/Outpatient Information Segment (ZIO)](#va-specific-inpatientoutpatient-information-segment-zio)
    - [VA-Specific Income Relation Segment (ZIR)](#va-specific-income-relation-segment-zir)
    - [VA-Specific Message Processing Segment (Ziv)](#va-specific-message-processing-segment-ziv)
    - [VA-Specific Military History Segment (ZMH)](#va-specific-military-history-segment-zmh)
    - [VA-Specific Means Test Information Segment (ZMT)](#va-specific-means-test-information-segment-zmt)
    - [### VA-Specific Patient Information Segment (ZPD)](#va-specific-patient-information-segment-zpd)
    - [VA-Specific Rated Disabilities Segment (ZRD)](#va-specific-rated-disabilities-segment-zrd)
    - [VA-Specific Service Period Segment (ZSP)](#va-specific-service-period-segment-zsp)
    - [VA-Specific Temporary Address Segment (ZTA)](#va-specific-temporary-address-segment-zta)
    - [VA Specific Temporary Eligibility Segment (ZTE)](#va-specific-temporary-eligibility-segment-zte)
    - [ZUD – VA Specific VistA User Data Segment](#zud-va-specific-vista-user-data-segment)
    - [Batch Header Segment (BHS)](#batch-header-segment-bhs)
    - [Batch Trailer Segment (BTS)](#batch-trailer-segment-bts)
    - [Message Header Segment (MSH)](#message-header-segment-msh)
    - [Message Acknowledgment Segment (MSA)](#message-acknowledgment-segment-msa)
    - [Master File Identification Segment (MFI)](#master-file-identification-segment-mfi)
    - [Master File Entry Segment (MFE)](#master-file-entry-segment-mfe)
    - [Location Identification Segment (LOC)](#location-identification-segment-loc)
  - [# Appendix C – Supported/User-Defined Standard HL7 Tables](#appendix-c-supporteduser-defined-standard-hl7-tables)
  - [Table 0001 – Sex](#table-0001-sex)
  - [Table 0002 – Marital Status](#table-0002-marital-status)
  - [Table 0003 – Event Type Codes](#table-0003-event-type-codes)
  - [Table 0005 – Race](#table-0005-race)
  - [Table 0006 – Religion](#table-0006-religion)
  - [Table 0008 – Acknowledgment Code](#table-0008-acknowledgment-code)
  - [Table 0017 – Transaction Type](#table-0017-transaction-type)
  - [Table 0018 – Patient Type](#table-0018-patient-type)
  - [Table 0024 – Fee Schedule](#table-0024-fee-schedule)
  - [Table 0048 – What Subject Filter](#table-0048-what-subject-filter)
  - [Table 0049 – Department Code](#table-0049-department-code)
  - [Table 0051 – Diagnosis Code](#table-0051-diagnosis-code)
  - [Table 0076 – Message Type](#table-0076-message-type)
  - [Table 0078 – Abnormal Flags](#table-0078-abnormal-flags)
  - [Table 0080 – Nature of Abnormal Testing](#table-0080-nature-of-abnormal-testing)
  - [Table 0085 – Observation Result Status Codes Interpretation](#table-0085-observation-result-status-codes-interpretation)
  - [Table 0088 – Procedure Code](#table-0088-procedure-code)
  - [Table 0091 – Query Priority](#table-0091-query-priority)
  - [Table 0102 – Delayed Acknowledgement Type](#table-0102-delayed-acknowledgement-type)
  - [Table 0103 – Processing ID](#table-0103-processing-id)
  - [Table 0104 – Version ID](#table-0104-version-id)
  - [Table 0105 – Source of Comment](#table-0105-source-of-comment)
  - [Table 0106 – Query/Response Format Code](#table-0106-queryresponse-format-code)
  - [Table 0108 – Query Results Level](#table-0108-query-results-level)
  - [Table 0115 – Servicing Facility](#table-0115-servicing-facility)
  - [Table 0125 – Value Type](#table-0125-value-type)
  - [Table 0126 – Quantity Limited Request](#table-0126-quantity-limited-request)
  - [Table 0136 – Yes/No Indicator](#table-0136-yesno-indicator)
  - [Table 0155 – Accept/Application Acknowledgment Conditions](#table-0155-acceptapplication-acknowledgment-conditions)
  - [Table 0172 – Veterans Military Status](#table-0172-veterans-military-status)
  - [Table 0175 – Master File Identifier Code](#table-0175-master-file-identifier-code)
  - [Table 0178 – File Level Event Code](#table-0178-file-level-event-code)
  - [Table 0179 – Response Level](#table-0179-response-level)
  - [Table 0180 – Record Level Event Code](#table-0180-record-level-event-code)
  - [Table 0189 – Ethnic Group](#table-0189-ethnic-group)
  - [Table 0211 – Alternate Character Sets](#table-0211-alternate-character-sets)
  - [Table 0280 – Referral Priority](#table-0280-referral-priority)
  - [Table 0281 – Referral Type](#table-0281-referral-type)
  - [Table 0282 – Referral Disposition](#table-0282-referral-disposition)
  - [Table 0283 – Referral Status](#table-0283-referral-status)
  - [Table 0284 – Referral Category](#table-0284-referral-category)
  - [Table 0340 – Procedure Code Modifier](#table-0340-procedure-code-modifier)
  - [Table 0356 – Alternate Character Set Handling Scheme](#table-0356-alternate-character-set-handling-scheme)
  - [Table 0363 – Source of Address](#table-0363-source-of-address)
    - [# Appendix D – Supported/User-Defined VA HL7 Tables](#appendix-d-supporteduser-defined-va-hl7-tables)
  - [Table VA001 – Yes/No](#table-va001-yesno)
  - [Table VA002 – Current Means Test Status](#table-va002-current-means-test-status)
  - [Table VA003 – Employment Status](#table-va003-employment-status)
  - [Table VA004 – Eligibility](#table-va004-eligibility)
  - [Table VA005 – Disability Retirement From Military](#table-va005-disability-retirement-from-military)
  - [Table VA006 – Eligibility Status](#table-va006-eligibility-status)
  - [Table VA007 – Race](#table-va007-race)
  - [Table VA008 – Religion](#table-va008-religion)
  - [Table VA009 – Relationship Number](#table-va009-relationship-number)
  - [Table VA010 – Means Test Indicator](#table-va010-means-test-indicator)
  - [Table VA011 – Period of Service](#table-va011-period-of-service)
  - [Table VA012 – Type of Insurance](#table-va012-type-of-insurance)
  - [Table VA013 – Rated Disabilities](#table-va013-rated-disabilities)
  - [Table VA014 – Medication Copayment Exemption Status](#table-va014-medication-copayment-exemption-status)
  - [Table VA015 – Enrollment Status](#table-va015-enrollment-status)
  - [Table VA016 – Reason Enrollment Canceled/Declined](#table-va016-reason-enrollment-canceleddeclined)
  - [Table VA017 – Enrollment Priority](#table-va017-enrollment-priority)
  - [Table VA018 – Agency/Allied Country](#table-va018-agencyallied-country)
  - [Table VA022 - Radiation Exposure Method](#table-va022-radiation-exposure-method)
  - [Table VA026 - Military Service Component](#table-va026-military-service-component)
  - [Table VA033 - Fee Basis Treatment Code Type](#table-va033-fee-basis-treatment-code-type)
  - [Table VA034 - Fee Basis Program](#table-va034-fee-basis-program)
  - [Table VA035 - Enrollment Sub-Group](#table-va035-enrollment-sub-group)
  - [Table VA036 - Military Sexual Trauma Status](#table-va036-military-sexual-trauma-status)
  - [Table VA038 - Military History Type](#table-va038-military-history-type)
  - [Table VA0040 - Enrollment Group Threshold Type](#table-va0040-enrollment-group-threshold-type)
  - [Table VA041 - Determination Method](#table-va041-determination-method)
  - [Table VA042 - Affected Extremity](#table-va042-affected-extremity)
  - [Table VA043 - Condition Codes](#table-va043-condition-codes)
  - [Table VA045 - CD Permanent Indicator](#table-va045-cd-permanent-indicator)
  - [Table VA0047 - PATIENT REGISTRATION ONLY REASON Values](#table-va0047-patient-registration-only-reason-values)
  - [Table VA048 - Filipino Veteran Proof](#table-va048-filipino-veteran-proof)
  - [Table VA0051 - Means Test Signature Status](#table-va0051-means-test-signature-status)
  - [Table VA0052 - NTR Verification Method](#table-va0052-ntr-verification-method)
  - [Table VA0053 - NTR Qualifiers](#table-va0053-ntr-qualifiers)
  - [Table VA060 - Type of Financial Test](#table-va060-type-of-financial-test)
  - [Table VA061 - Invalid Address Reason](#table-va061-invalid-address-reason)
  - [Table VA0115 - Servicing Facility](#table-va0115-servicing-facility)
  - [Table VA117 - Reason For Closed Application](#table-va117-reason-for-closed-application)
  - [Table VA440 – CD Descriptors](#table-va440-cd-descriptors)

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Public Law 101-508 permits the Department of Veterans Affairs (VA) to verify income data with the Internal Revenue Service (IRS) and Social Security Administration (SSA) for veterans receiving VA health care services whose eligibility for medical care is based on income. The income verification match process for Veterans Health Administration (VHA) medical facilities is centralized and performed at the Health Eligibility Center (HEC) in Atlanta, Georgia.

## Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVM provides all of the functionality required to complete the eligibility verification process; electronically receive the revised VA Form 10-10F from the HEC; and automatically file the updated test in the V*ist*A Means Test module.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User Interactive Functions</strong></th>
<th><strong>Noninteractive Functions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>View/verify patient demographic, insurance, and SSN information received from SSA and IRS.</p></li>
<li><p>Upload verified data.</p></li>
<li><p>View billing/collection and Means Test activity.</p></li>
<li><p>Configure, monitor, and purge the IVM system.</p></li>
</ul></td>
<td><ul>
<li><p>Exchange of data, on an ad hoc basis, between your facility and the HEC via electronic transmissions.</p></li>
<li><p>Scheduled transmission to the HEC of all Means Tests meeting IVM criteria, as well as IVM-related billing and collections activity, via the <em>IVM Background Job</em> option.</p></li>
</ul>
<p><em>Note: Certain enrollment events, when they occur, are also sent to the HEC via the nightly background job.</em></p></td>
</tr>
</tbody>
</table>

Related Manuals

IVM V. 2.0 User Manual

IVM V. 2.0 Installation Guide

IVM V. 2.0 Release Notes

Integration

IVM V. 2.0 provides functionality that impacts Registration, Medical Care Cost Recovery (MCCR), and Information Resource Management (IRM) staff at your facility. It is highly integrated with the following packages.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package Name</strong></th>
<th><strong>Integration</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient Information Management System (PIMS)</td>
<td><ul>
<li><p>PIMS demographic, Means Test, enrollment, eligibility, and income information is sent to the HEC.</p></li>
<li><p>Means Test and demographic information verified by the HEC is uploaded into PIMS files.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Integrated Billing (IB)</td>
<td>IB provides billing and collections information, for billings resulting from IVM activity, that is transmitted back to the HEC and the Enrollment Database (EDB).</td>
</tr>
<tr class="odd">
<td>Health Level 7 (HL7)</td>
<td>Provides the foundation for all communications between your facility and the HEC.</td>
</tr>
</tbody>
</table>

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three parameters included with the IVM software. These parameters, which can be edited through the IVM Parameter Enter/Edit option, control whether notification messages are sent to the IVM MESSAGES mail group when SSN, demographic, and insurance information is received from the HEC. If no entry is made, the default action is to generate the messages. This option may be used to inactivate the messages.

The background option *IVM Background Job* must be queued to run daily. It is recommended that it is run during non-peak hours. The option will transmit the following information to the HEC: Means Test, patient demographic, eligibility, income test, insurance, enrollment, and IVM-related billing and collections.

All IVM notifications generated by the system are sent to the *IVM Messages* mail group. At a minimum, both the IRM Support Specialist and the IVM systems coordinator should be added as members of this group.

No data in the IVM files should be edited. This data is added and maintained automatically by the module.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per VHA Directive 10-93-142 regarding security of software that affects financial systems, most of the IVM routines may not be modified. The third line of routines that may not be modified is so noted. The IVM output routines in the IVMR\* namespace are exempt from this requirement.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IVM package has no supported callable routines.

## Routines to Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that the following routines be mapped.

IVML\*

IVMR\*

IVMU\*

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following steps to obtain a list of routines in the IVM V. 2.0 software:

1\. Programmer Options Menu

2\. Routine Tools Menu

3\. First Line Routine Print Option

4\. Routine Selector: IVM\*

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Globals to Journal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IVM global is the only global used with the IVM software and it should be journaled.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per VHA Directive 10-93-142 regarding security of software that affects financial systems, the IVM Data Dictionaries may not be modified. The file descriptions of these files are so noted.

| File Number | File Name                           | Global  |
|-----------------|-----------------------------------------|-------------|
| 301.5           | IVM PATIENT                             | ^IVM(301.5  |
| 301.6           | IVM TRANSMISSION LOG                    | ^IVM(301.6  |
| 301.61          | IVM BILLING TRANSMISSION                | ^IVM(301.61 |
| 301.63          | IVM EXTRACT MANAGEMENT                  | ^IVM(301.63 |
| 301.7           | IVM ADDRESS CHANGE LOG                  | ^IVM(301.7  |
| 301.9           | IVM SITE PARAMETER                      | ^IVM(301.9  |
| 301.91\*        | IVM REASONS FOR NOT UPLOADING INSURANCE | ^IVM(301.91 |
| 301.92\*        | IVM DEMOGRAPHIC UPLOAD FIELDS           | ^IVM(301.92 |
| 301.93\*        | IVM CASE CLOSURE REASON                 | ^IVM(301.93 |

\*File comes with data

Take the following steps to obtain information about the files and templates in the IVM software:

## File Flow (Relationships Between Files) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# or range of File \#s

5\. Select Listing Format: Standard

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say, “POINTER TO”.

Templates

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: Print Template

Sort Template

Input Template

List Template

4\. Sort by: Name

5\. Start with name: IVM

6\. Within name, sort by: \<RET\>

7\. First print field: Name

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following are the steps to obtain information about menus, exported protocols, exported options, and exported remote procedures relating to the IVM package.

## Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Programmers Options

2\. Menu Management Menu

3\. Display Menus and Options Menu

4\. Diagram Menus

5\. Select User or Option Name: O.IVM MAIN MENU

Exported Protocols

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: PROTOCOL

4\. Sort by: Name

5\. Start with name: IVM

6\. Within name, sort by: \<RET\>

7\. First print field: Name

Exported Options

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: OPTION

4\. Sort by: Name

5\. Start with name: IVM

6\. Within name, sort by: \<RET\>

7\. First print field: Name

Exported Remote Procedures

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: REMOTE PROCEDURE

4\. Sort by: Name

5\. Start with name: IVM

6\. Within name, sort by: \<RET\>

7\. First print field: Name

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving capabilities included with the IVM software.

## Purging 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge IVM Transmissions option allows IRM to purge entries from the IVM TRANSMISSION LOG File (#301.6) which are associated with closed cases (entries in the IVM PATIENT File (#301.5)) from the previous Means Test year).

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the IVM software package.

## SACC Exemptions/Non-Standard Code 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC Exemptions associated with the IVM software package.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Relations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following V*ist*A package versions (or higher) MUST be installed PRIOR to loading this version of IVM.

Kernel V. 7.1

VA FileMan V. 20.0

PIMS V. 5.3

Integrated Billing V. 2.0

OERR V. 2.5

V*IST*A HL7 V. 1.6

## DBIA Agreements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following steps to obtain database integration agreements for the IVM package.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Custodial Package</strong></th>
<th><strong>Subscriber Package</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>FORUM</p></li>
<li><p>DBA MENU</p></li>
<li><p>Integration Agreement Menu Custodial Package Menu</p></li>
<li><p>Active by Custodial Package Option</p></li>
<li><p>Select Package Name: IVM</p></li>
</ol></td>
<td><ol type="1">
<li><p>Forum</p></li>
<li><p>DBA MENU</p></li>
<li><p>Integration Agreement Menu</p></li>
<li><p>Subscriber Package Menu</p></li>
<li><p>Print Active by Subscriber Package Option</p></li>
<li><p>Start with subscriber package: IVM</p></li>
</ol></td>
</tr>
</tbody>
</table>

## Internal Relations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the IVM V. 2.0 package options have been designed to stand alone.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Public Law 101-508 permits the Department of Veterans Affairs (VA) to verify income data with the Internal Revenue Service (IRS) and Social Security Administration (SSA) for veterans receiving VA health care services whose eligibility for medical care is based on income. The IVM process for Veterans Health Administration (VHA) medical facilities is centralized and performed at the HEC in Atlanta, Georgia.

Per VHA Directive 10-93-142 regarding security of software that affects financial systems and central data bases, IVM routines may not be modified with the following exception: IVMR\* - IVM Reports. In compliance with this same directive, the IVM Data Dictionaries may not be modified.

## Security Keys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Take the following steps to obtain information about the security keys contained in the IVM software:

1.  VA FileMan Menu
2.  Print File Entries
3.  Output From What File: Security Key
4.  Sort By: Name
5.  Start With Name: First// IVM
6.  Go To Name: Last// IVMZ
7.  Within Name, Sort By: \<RET\>
8.  First Print Field: Name
9.  Then Print Field: Description

## VA FileMan Access Codes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of recommended VA FileMan access codes for the files in the IVM software.

| File Number | File Name                           | DD Access | RD Access | WR Access | DEL Access | LAYGO Access |
|-----------------|-----------------------------------------|---------------|---------------|---------------|----------------|------------------|
| 301.5           | IVM PATIENT                             | @             |               | @             | @              | @                |
| 301.6           | IVM TRANSMISSION LOG                    | @             |               | @             | @              | @                |
| 301.61          | IVM BILLING TRANSMISSION                | @             |               | @             | @              | @                |
| 301.63          | IVM EXTRACT MANAGEMENT                  | @             |               | @             | @              | @                |
| 301.7           | IVM ADDRESS CHANGE LOG                  | @             |               | @             | @              | @                |
| 301.9           | IVM SITE PARAMETER                      | @             |               | @             | @              | @                |
| 301.91          | IVM REASONS FOR NOT UPLOADING INSURANCE | @             |               | @             | @              | @                |
| 301.92          | IVM DEMOGRAPHIC UPLOAD FIELDS           | @             |               | @             | @              | @                |
| 301.93          | IVM CASE CLOSURE REASON                 | @             |               | @             | @              | @                |

# How to Generate On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure IVM technical documentation. On-line technical documentation pertaining to the IVM software, in addition to that which is located in the help prompts, may be generated through utilization of several Kernel options, including those listed in this section. Refer to the V*ist*A Kernel Reference Manual for further information about other utilities which supply on-line technical documentation.

## Xindex 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to V*ist*A Programming Standards. The XINDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references. By running XINDEX for a specified set of routines, the user might discover any deviations from V*ist*A Programming Standards which exist in the selected routine(s) and see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the IVM package, specify the IVM namespace at the “routine(s) ?\>” prompt. IVM initialization routines which reside in the UCI in which XINDEX is being run, as well as local routines found within the IVM namespace, should be omitted at the “routine(s)?\>” prompt. To omit routines from selection, preface the namespace with a minus sign (-).

## List File Attributes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Using this option via the “Standard” format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the “Global Map” format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates, when applicable. For a comprehensive list of IVM files, please refer to the FILES section of this manual.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary contains terms and their definitions as they relate to the IVM package.
Category A veteran A patient who, as a result of Means Testing, is in the mandatory category in regard to eligibility for VA care.
Category C veteran A patient who, as a result of Means Testing, is in the discretionary category in regard to eligibility for VA care.
Enrollment Database (EDB) Oracle database physically located at the Austin Information Technology Center (AITC), formerly known as the Austin Automation Center, that will be the central repository for enrollment, eligibility, means test and IVM data.
Full Data Transmission A complete information profile transmitted to the HEC containing patient demographic, eligibility, Means Test, income, insurance, and enrollment information.
HEC Health Eligibility Center (formerly IVM Center)
HL7 Health Level 7 is an interface specification designed to standardize the way in which health care information is transferred between systems. IVM utilizes the V*ist*A HL7 package to assist in transporting data using this specification.
IRS Internal Revenue Service
IVM Income Verification Match. A program designed to verify income and insurance data reported by the veteran with that received from IRS (Internal Revenue Service), SSA (Social Security Administration), and other sources.
Means Test Eligibility for VA hospital care and nursing home care is divided into two categories – mandatory and discretionary. An income assessment is made to determine whether a non service-connected veteran, who is not in receipt of VA monetary benefits or otherwise exempt from income assessment, is eligible for cost-free VA medical care. This income assessment is known as “Means Testing”. Patients whose income is above the defined income levels must agree to make copayments to VA for outpatient and inpatient care rendered.
SSA Social Security Administration
Suggested SSN Patient or spouse SSNs returned from SSA as possible matches based on name, sex, and date of birth. These SSNs will be validated by the HEC before being returned to the field facilities.
Third Party Claim When a party other than the patient, such as an insurance company, is billed.

# Appendix A – IVM Data Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Basic knowledge of the HL7 protocol is assumed and the information contained in the HL7 protocol will not be repeated *here.* Further information concerning the HL7 protocol may be found in the HL7 Interface Standards V. 2.3.1.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document specifies the purpose of the interface between the V*ist*A IVM package and the HEC (non- V*ist*A) system based on the HL7 protocol. It is intended that this interface form the basis for exchange of healthcare information between the V*ist*A IVM package and the HEC system.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the messages that are exchanged between the V*ist*A IVM package and the HEC (non- V*ist*A) system for the purpose of exchanging income test, demographic, insurance, and enrollment information.

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This application uses the abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events that occur in healthcare environments. For example, when a Means Test is added in V*ist*A, the event will trigger a Full Data Transmission message to the HEC.

## Communications Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 V. 1.6 of the VA MailMan lower level protocol (LLP) will be used to transmit HL7 messages between the local site and the HEC.

## Background Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On a daily basis, the data associated with various events that occur in V*ist*A will be transmitted to the HEC. The IVM Background Job option will be used to transmit a HL7 unsolicited Full Data Transmission (ORU~Z07) for each V*ist*A event occurring that day.

## Batch Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All HL7 unsolicited messages sent from the V*ist*A IVM application and received from the HEC (non- V*ist*A) system will be in a batch format. Each batch will contain 1-100 messages/records per batch.

## HL7 Message Event Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVM V. 2.0 supports the receipt and transmission of the following HL7 message event types (data transmissions).

| HL7 Transmission Name                                             | HL7 MESSAGE TYPE | HL7 Event Code |
|-----------------------------------------------------------------------|----------------------|--------------------|
| SSN Data Transmission                                                 | ORU                  | Z03                |
| Insurance Data Transmission                                           | ORU                  | Z04                |
| Follow-up Data Transmission                                           | ORU                  | Z04                |
| Demographic Data Transmission                                         | ORU                  | Z05                |
| Means Test Data Transmission                                          | ORF/ORU              | Z06                |
| Full Data Transmission                                                | ORF/ORU              | Z07                |
| Case Status Data Transmission                                         | ORU                  | Z08                |
| Billing/Collection Data Transmission                                  | ORU                  | Z09                |
| Income Test Data Transmission                                         | ORU/ORF              | Z10                |
| Enrollment/Eligibility Data Transmission                              | ORF/ORU              | Z11                |
| V*IST*A – Initiated Enrollment/Eligibility Query Transmission | QRY                  | QRY                |
| IVM – Initiated Query Transmission                                    | QRY                  | QRY                |

## HL7 Message Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVM V.2.0 utilizes the following HL7 segments to support the exchange of patient data.

| Segment ID | Segment Name                                      |
|----------------|-------------------------------------------------------|
| BHS            | Batch Header Segment                                  |
| BTS            | Batch Trailer Segment                                 |
| FT1            | Financial Segment                                     |
| IN1            | Insurance Segment                                     |
| LOC            | Location Identification Segment                       |
| MFA            | Master File Acknowledgement                           |
| MFE            | Master File Entry Segment                             |
| MFI            | Master File Identification Segment                    |
| MSA            | Message Acknowledgement                               |
| MSH            | Message Header                                        |
| NTE            | Notes And Comments Segment                            |
| OBX            | Observation/Result Segment                            |
| PD1            | Patient Demographic 1 Screen                          |
| PID            | Patient Identification Segment                        |
| QRD            | Query Definition Segment                              |
| QRF            | Query Filter Segment                                  |
| RF1            | Referral Information Segment                          |
| ZAV            | VA-Specific Address Validation Segment                |
| ZBT            | VA-Specific Beneficiary Travel Segment                |
| ZCD            | VA-Specific Catastrophic Disability Segment           |
| ZCE            | VA-Specific Community Care Eligibility Segment        |
| ZCT            | VA-Specific Emergency Contact Segment                 |
| ZDP            | VA-Specific Patient Dependent Information Segment     |
| ZEG            | VA Specific Enrollment Group Threshold Segment        |
| ZEL            | VA-Specific Patient Eligibility Segment               |
| ZE2            | VA-Specific Patient Eligibility (Addtl) Segment       |
| ZEM            | VA-Specific Employment Information Segment            |
| ZHP            | VA-Specific Health Benefit Plan Segment               |
| ZEN            | VA-Specific Enrollment Segment                        |
| ZFE            | VA-Specific Fee Basis Segment                         |
| ZGD            | VA-Specific Guardian Segment                          |
| ZIC            | VA-Specific Income Segment                            |
| ZIE            | VA-Specific Patient Ineligible Segment                |
| ZIO            | VA-Specific Inpatient/Outpatient Information Segment  |
| ZIR            | VA-Specific Income Relation Segment                   |
| ZIV            | VA-Specific Message Processing Segment                |
| ZMH            | VA-Specific Military History Segment                  |
| ZMT            | VA-Specific Means Test/Copay Test Information Segment |
| ZPD            | VA-Specific Patient Information Segment               |
| ZRD            | VA-Specific Rated Disabilities Segment                |
| ZSP            | VA-Specific Service Period Segment                    |
| ZTA            | VA-Specific Temporary Address Segment                 |
| ZTE            | VA Specific Temporary Eligibility Segment             |

## HL7 Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this section, the following elements will be defined for each HL7 message.

- Message Type
- Message Event Code
- Abstract Message Syntax (list of segments used in the message)
- List of Data Fields (sequence numbers used for each segment)

An HL7 message is composed of individual HL7 segments. Each individual segment contains logical groupings of data. The Braces { } indicate one or more repetitions of the enclosed group of segments. The Brackets \[ \] indicate that a segment may be optional. For each message, there will be a list of HL7 standard segments or VA-specific “Z” segments used in the message. The data fields (represented by sequence numbers) utilized in each segment will also be specified. The HL7 Transmission/Event Type Codes are annotated beside each message type.

*Please note that an ORF transmission contains the MSA and QRD segments, but the ORU transmission does not.*

### SSN Data Transmission – (ORU~Z03)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SSN data transmission transmits new veteran or spouse social security numbers to your facility from the HEC.

BHS Batch Header Segment

{MSH Message Header

PID Patient Identification Segment (*SEQ 1,3,5,7,19*)

ZIV VA-Specific Message Processing Segment (*SEQ 1-7,12*)

}

BTS Batch Trailer

### Insurance Data Transmission – (ORU~Z04)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The insurance data transmission transmits patient insurance information to your facility from HEC.

BHS Batch Header

{MSH message header

PID Patient Information Segment (*SEQ 1-3,5,7,19*)

IN1 Insurance Segment (*SEQ 1,4,5,7-9,12,13,15-18,28,36*)

ZIV VA-Specific Message Processing Segment (*SEQ 1,9,13*)

}

BTS Batch Trailer

Follow-up insurance data transmissions are transmitted from your facility to alert the HEC as to the action taken regarding insurance information acceptance or rejection. The format for the responding transmission follows (message will NOT be batched).

MSH Message Header

PID Patient Identification Segment (*SEQ 1,2,3,5,7,19*)

IN1 Insurance Segment (*SEQ 1,4, 36*)

ZIV VA-Specific Message Processing Segment (*SEQ 1,9-11*)

### Demographic Data Transmission – (ORU~Z05)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Newly identified or updated demographic-type information for a patient transmitted from the HEC to the VAMC.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (*SEQ 1-3, 5,7, 8, 10,11,13, 16-17, 19, 22,24)*

ZPD VA-Specific Patient Info Segment *(SEQ 1,6,7,30, 34,46,47)*

ZTA VA-Specific Temporary Address Segment (*SEQ 1-9)*

{ZAV VA-Specific Address Validation Segment *(SEQ 1-3)*

}

ZGD VA-Specific Guardian Segment *(SEQ 1)*

ZCT VA-Specific Emergency Contact Segment *(SEQ 1-7, 10)*

}

ZEM VA-Specific Employment Info Segment (*SEQ 1-7, 9)*

}

RF1 Referral Information Segment *(SEQ 3,6,7)*

BTS Batch Trailer

### Date of Death Transmission – (ORU~Z05)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Newly identified or updated date of death-type information for a patient transmitted from the HEC to the VAMC.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (*SEQ 1-3, 5,7, 8,19)*

ZPD VA-Specific Patient Info Segment *(SEQ 1, 9, 31,32)*

ZTA VA-Specific Temporary Address Segment (*SEQ)*

ZGD VA-Specific Guardian Segment *(SEQ)*

ZCT VA-Specific Emergency Contact Segment *(SEQ)*

ZEM VA-Specific Employment Info Segment (*SEQ)*

RF1 Referral Information Segment *(SEQ )*

BTS Batch Trailer

### Guardian Data Transmission – (ORU~Z05)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Newly identified or updated VA Guardian-type information for a patient transmitted from the HEC to the VAMC.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (*SEQ 1,2, 5,7, 8, 11, 19)*

ZPD VA-Specific Patient Info Segment *(SEQ 1, 8)*

ZTA VA-Specific Temporary Address Segment (*SEQ)*

ZGD VA-Specific Guardian Segment *(SEQ 1-8)*

ZCT VA-Specific Emergency Contact Segment *(SEQ)*

ZEM VA-Specific Employment Info Segment (*SEQ)*

RF1 Referral Information Segment *(SEQ)*

BTS Batch Trailer

### Means Test Data Transmission – (ORF~Z06) NOTE: This message has been retired.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The means test data transmission returns an observation of the means test signature in response to the site’s transmission of a means test image. (HEC to V*ist*A)

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (*SEQ 1,3,19*)

}

ZMT VA-Specific Means Test Info Segment (*SEQ 1-5,7-12,15,17-21*)

}

BTS Batch Trailer

### Means Test Data Transmission – (ORU~Z06)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The means test data transmission transmits the IVM-verified means test from the ES to your facility.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (*SEQ 1-3,5,7,8,19*)

ZIC VA-Specific Income Segment (*SEQ 1*)

ZIR VA-Specific Income Relation Segment (*SEQ 1*)

{ZDP VA-Specific Dependent Info Segment (*SEQ 1*)

ZIC VA-Specific Income Segment (*SEQ 1*)

ZIR VA-Specific Income Relation Segment (*SEQ 1*)

}

ZMT VA-Specific Means Test Info Segment (*SEQ 1-3,7,8,10,12,15,17,18,20,25,26,31*)

ZIV VA-Specific Message Processing Segment *(SEQ 1,2,8)*

}

BTS Batch Trailer

### Full Data Transmission – (ORU~Z07)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Full Data Transmission transmits a complete profile of patient demographic, eligibility, Means Test, income, insurance, and enrollment information to the HEC.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment *(SEQ 1-3, 5-7, 8, 10-14, 16, 17, 19,22, 24)*

PD1 Patient Demographic Segment *(SEQ 3)*

ZPD VA-Specific Patient Info Segment *(SEQ 1,6-9,11-13,17,19,30,31-34,35,40,41,42-45,46,47)*

ZTA VA-Specific Temporary Address Segment *(SEQ 1-10)*

{ZAV VA-Specific Address Validation Segment *(SEQ 1-3)*

}

ZIE VA-Specific Patient Ineligible Segment *(SEQ 1-3)*

{ZEL VA-Specific Patient Eligibility Segment *(SEQ 1,2,5-8,10,11,13-25,29,34,35,37,38-50 forprimary eligibility and SEQ 1,2 for all other eligibilities)*

}

{\[ZE2 VA-Specific Patient Eligibility (Addtl) Segment (1,2)

\]}

\[ZHF VA-Specific Health Factor Segment

\]

{\[ZTE VA Specific Temporary Eligibility Segment

\]}

\[{ZCE VA Specific Community Care Eligibility Segment (SEQ 1-4)

}\]

\[{ZHP VA-Specific Health Benefit Plan Segment (SEQ 1-4)

}\]

ZEN VA-Specific Enrollment Segment *(SEQ 1-19*)

ZCD VA-Specific Catastrophic Disability Segment *(SEQ 1-17)*\[{ZMH} VA-Specific Military History Segment *(SEQ 1-5)*

\]

{ZRD VA-Specific Rated Disabilities Segment *(SEQ 1-4, 12-14)*

}

ZCT VA-Specific Emergency Contact Segment *(SEQ 1-7,10)*

{ZEM VA-Specific Employment Info Segment *(SEQ 1-7 for Veteran and SEQ 1-7 for Spouse)*

}

{ZGD VA-Specific Guardian Segment *(SEQ 1-8)*

}

ZIC VA-Specific Income Segment *(SEQ 1-20 when ZMT SEQ 30 (version) is 0, SEQ 1-3,9,12-16,18-19 when ZMT SEQ 30 (version) is 1)*

ZIR VA-Specific Income Relation Segment *(SEQ 1-5,10,15)*

{ZDP VA-Specific Dependent Information Segment *(SEQ 1-14 for spouseand SEQ 1-7,9-11for all other dependents)*

ZIC VA-Specific Income Segment *(SEQ 1-12,16-20 for spouse, SEQ 1-12,15 for dependentswhen ZMT-30 (version) is 0) (SEQ 1-3,9,12,16,18-19 for spouse, SEQ1,2,3,9,12,15,16,19 for dependents when ZMT-30 (version) is 1)*

ZIR VA-Specific Income Relation Segment *(SEQ 1-3 for spouse, SEQ 1-5,6-9,14 for otherdependents)*

}

ZIO VA-Specific Patient Info Segment *(SEQ 1-10)*

{NTE Notes & Comments *(SEQ 1,3)*

}

{IN1 Insurance Segment *(SEQ 1, 4, 5,7-9,12,13,15-17,28,36)*

}

ZMT VA-Specific Means Test Information Segment *(SEQ 1-18,21-31, 32)*

ZMT VA-Specific CoPay Test Information Segment *(SEQ 1-7,9-10,12,15-18,21-22,25-26,30,31, 32)*

ZMT VA-Specific LTC Test Information Segment *(SEQ 1-5,7,9-10,12,16-18,22,25,30,31, 32)*

ZBT VA-Specific Beneficiary Travel Information Segment *(SEQ 1-4,7)*

\[{ZFE VA-Specific Fee Basis Segment (*SEQ 1-5*)

}\]

ZSP VA-Specific Service Period Segment *(SEQ 1-8,10,11)*

{\[OBX Observation/Result Segment

For Patient Sensitivity Information *(SEQ 2,3,5,11,14,16)*For NTR *(SEQ 2,3,5,11,12,14,15-17)*

\]}

{RF1 Referral Information Segment *(SEQ 3,6,7)*

}

{ZUD VA-Specific VistA User Data Segment *(SEQ 1-5)*

}

}

BTS Batch Trailer

### Full Data Transmission – (ORF~Z07)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Full Data Transmission transmits a complete profile of patient demographic, eligibility, Means Test, income, insurance, and enrollment information to the HEC.

MSH Message Header

MSA Message Acknowledgment

QRD Query Definition *(segment as submitted in HEC initiated query)*

PID Patient Identification Segment *(SEQ 1-3,5-7,8,10-14,16,17,19,22,24)*

PD1 Patient Demographic Segment *(SEQ 3)*

ZPD VA-Specific Patient Info Segment *(SEQ 1,6-9,11-13,17,19,30,31-34,35, 40,41,42-45,46,47)*

ZTA VA-Specific Temporary Address Segment *(SEQ 1-10)*

{ZAV VA-Specific Address Validation Segment *(SEQ 1-3)*

}

ZIE VA-Specific Patient Ineligible Segment *(SEQ 1-3)*

{ZEL VA-Specific Patient Eligibility Segment *(SEQ 1,2,5-8,10,11,13-25,29,34,35,37,38-50 forprimary eligibility and SEQ 1,2 for all other eligibilities)*

}

H{\[ZE2 VA-Specific Patient Eligibility (Addtl) Segment (1,2)

\]}

\[ZHF VA-Specific Health Factor Segment

\]

{\[ZTE VA Specific Temporary Eligibility Segment

\]}

\[{ZCE VA Specific Community Care Eligibility Segment (SEQ 1-4)

}\]

\[{ZHP VA-Specific Health Benefit Plan Segment (SEQ 1-4)

}\]

ZEN VA-Specific Enrollment Segment *(SEQ 1-19*)

ZCD VA-Specific Catastrophic Disability Segment *(SEQ 1-17)*

{ZMH} VA-Specific Military History Segment *(SEQ 1-5)*

{ZRD VA-Specific Rated Disabilities Segment *(SEQ 1-4, 12-14)*

}

ZCT VA-Specific Emergency Contact Segment *(SEQ 1-7,10)*

{ZEM VA-Specific Employment Info Segment *(SEQ 1-7 for Veteran and SEQ 1-7 for Spouse 7, 9)*

}

{ZGD VA-Specific Guardian Segment *(SEQ 1-8)*

}

ZIC VA-Specific Income Segment *(SEQ 1-20 when ZMT SEQ 30 (version) is 0, SEQ 1-3,9,12-16,18-19 when ZMT SEQ 30 (version) is 1))*

ZIR VA-Specific Income Relation Segment *(SEQ 1-5,10,15)*

{ZDP VA-Specific Dependent Information Segment *(SEQ 1-14 for spouseand SEQ 1-7,9-11 for all other dependents)*

ZIC VA-Specific Income Segment *(SEQ 1-12,16-20 for spouse, SEQ 1-12,15 for dependentswhen ZMT-30 (version) is 0 (SEQ 1-3,9,12,16,18-19 for spouse, SEQ1,2,3,9,12,15,16,19 for dependents when ZMT-30 (version) is 1)*

ZIR VA-Specific Income Relation Segment *(SEQ 1-3 for spouse, SEQ 1-5,6-9,14 fordependents)*

}

ZIO VA-Specific Patient Info Segment *(SEQ 1-10)*

{NTE Notes & Comments *(SEQ 1,3)*

}

{IN1 Insurance Segment *(SEQ 1,4,5,7-9,12,13,15-17,28,36)*

}

ZMT VA-Specific Means Test Information Segment *(SEQ 1-18, ,21-30,31, 32)*

ZMT VA-Specific CoPay Test Information Segment *(SEQ 1-7,9-10,12,15-18,21-22,25-26,30,31, 32)*

ZMT VA-Specific LTC Test Information Segment *(SEQ 1-5,7,9-10,12,16-18,22,25,30,31, 32)*

ZBT VA-Specific Beneficiary Travel Information Segment *(SEQ 1-4,7)*

\[{ZFE VA-Specific Fee Basis Segment (*SEQ 1-5*)

}\]

ZSP VA-Specific Service Period Segment *(SEQ 1-8,10, 11)*

{\[OBX Observation/Result Segment

For Patient Sensitivity Information *(SEQ 2,3,5,11,14,16)*

for NTR *(SEQ 2,3,5,11,12,14,15-17)*

\]}

{RF1 Referral Information Segment *(SEQ 3,6,7)*

}

{ZUD VA-Specific VistA User Data Segment *(SEQ 1-5)*

}

}

BTS Batch Trailer

### Case Status Data Transmission – (ORU~Z08) (Message has been retired)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The case status data transmission is generated by the HEC to alert your facility of closed cases.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (SEQ 1,3,5,7,19)

ZIV VA-Specific Message Processing Segment (SEQ 1,2,8)

}

BTS Batch Trailer

### Billing/Collection Data Transmission – (ORU~Z09)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The billing/collection data transmission transmits IVM-related billing and collections information to the HEC for cases that were closed via the HEC Legacy system.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (*SEQ 1,3,5,7,8,19*)

FT1 Financial Transaction (*SEQ 1,4,6,7,9,11*)

}

ZIC VA-Specific Income Segment (*SEQ 1,2*)

}

BTS Batch Trailer

### Billing/Collection Data Transmission – (ORU~Z09)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The billing/collection data transmission transmits IVM-related billing and collections information to the EDB for cases that were closed via a Z06 from EDB.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment (*SEQ 1-5,7,8,19*)

PD1 Patient Demographic Segment (*SEQ 1,3*)

{FT1 Financial Transaction (*SEQ 1,4,6,7,9,11,12*)

}

ZIC VA-Specific Income Segment (*SEQ 1,2*)

}

BTS Batch Trailer

### Income Test Data Transmission – (ORU~Z10)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The income test data transmission transmits income data for veteran, spouse, and dependents from the HEC. NOTE: The ORF~Z06 Means Test Transmission to VistA has been eliminated; instead, the Means Test Signature information will be sent to VistA in the Z10.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment *(SEQ 1,3,5,7,8,19)*

ZIC VA-Specific Income Segment *(SEQ 1-20 when ZMT SEQ 30 \[Version\] equals 0)(SEQ 1-3,9,12-16,18-19 when ZMT SEQ 30 \[Version\] equals 1 and income year 2008 or earlier) (SEQ 1-3,9,12 when ZMT SEQ 30 \[Version\] equals 1 and income year 2009 or later)*

ZIR VA-Specific Income Relation Segment *(SEQ 1-4,10, 15)*

{ZDP VA-Specific Dependent Information Segment *(SEQ 1-14 for spouse and SEQ 1-6,9-12 for dependents)*

ZIC VA-Specific Income Segment *(SEQ 1-12,16-20 for spouse and SEQ 1-12,15 for all other dependents when ZMT SEQ 30 \[Version\] is equal to 0)(SEQ 1-3,9,12,16,18-19 for spouse and SEQ 1-3,9,12,15-16,18-19 for dependents when ZMT SEQ 30 \[Version\] is equal to 1 and Income Year 2008 or earlier)(SEQ 1-3,9,12 when ZMT SEQ 30 \[Version\] is equal to 1 and Income Year 2009 or later)*

ZIR VA-Specific Income Relation *Segment (SEQ 1 for spouse and SEQ 1,3-4,6-9,14 for all other dependents)*

}

ZMT VA-Specific Means Test Information Segment *(SEQ 1-19,22-30 for Income Year 2008 or earlier) (SEQ 1-4,6-19,22-31, 32 for Income Year 2009 or later)*

ZMT VA-Specific Co-Pay Test Information Segment *(SEQ 1-4,9,10,12,15-19,22,25-26,30-31, 32)*

ZMT VA-Specific LTC Co-Pay Exemption Test Information Segment *(SEQ 1-4,7,9,10,12,16-18,22,25,30-31, 32)*

ZBT VA-Specific Beneficiary Travel Information Segment *(SEQ 1-4)*

}

BTS Batch Trailer

### Income Test Data Transmission – (ORF~Z10)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The income test data transmission transmits income data for veteran, spouse, and dependents from the HEC. NOTE: The ORF~Z06 Means Test Transmission to VistA has been eliminated; instead, the Means Test Signature information will be sent to VistA in the Z10.

MSH Message Header

MSA Message Acknowledgment

QRD Query Definition *(SEQ 1-4, 7-10,12)*

QRF Query Filter *(SEQ 1,4,5)*

PID Patient Identification Segment *(SEQ 1,3,5,7,8,19)*

ZIC VA-Specific Income Segment *(SEQ 1-20 when ZMT SEQ 30 \[Version\] equals 0)(SEQ 1-3,9,12-16,18-19 when ZMT SEQ 30 \[Version\] equals 1 and Income Year 2008 or earlier) (SEQ 1-3,9,12-15 when ZMT SEQ 30 \[Version\] equals 1 and Income Year 2009 or later)*

ZIR VA-Specific Income Relation Segment *(SEQ 1-4,10, 15)*

{ZDP VA-Specific Dependent Information Segment (SEQ 1-14 for spouse and SEQ 1-6,9-12 for all other dependents)

ZIC VA-Specific Income Segment (SEQ 1-12,16-20 for spouse and SEQ 1-12,15 for all other dependents *when ZMT SEQ 30 \[Version\] is equal to 0*)*(SEQ 1-3,9,12,16,18-19 for spouse and SEQ 1-3,9,12,15-16,18-19 for dependents when ZMT SEQ 30 \[Version\] is equal to 1 and Income Year 2008 or earlier)(SEQ 1-3,9,12-15 when ZMT SEQ 30 \[Version\] is equal to 1 and Income Year 2009 or later)*

ZIR VA-Specific Income Relation Segment *(SEQ 1 for spouse and SEQ 1,3,4,6-9,14 for all other dependents)*

}

ZMT VA-Specific Means Test Information Segment *(SEQ 1-19,22-30 for Income Year 2008 or earlier) (SEQ 1-19,22-31, 32 for Income Year 2009 or later)*

ZMT VA-Specific Co-Pay Test Information Segment *(SEQ 1-4,9-10,12,15-19,22,25-26,30,31, 32)*

ZMT VA-Specific LTC Co-Pay Exemption Test Information Segment *(SEQ 1-4,7,9-10,12,16-18,22,25,30,31, 32)*

ZBT A-Specific Beneficiary Travel Information Segment *(SEQ 1-4)*

BTS Batch Trailer

> **NOTE:** The ORU and ORF Z10- ZDP, ZIC, and ZIR segments will be contain data as follows:

1.  Vet has a spouse, spouse is active

ZDP – spouse data

ZIC – with data

ZIR – with data

2.  Vet does not have a spouse

ZDP – sequence 6 = 2

ZIC with no data

ZIR with no data

3.  Vet has an inactive spouse

ZDP – seq 6 set to 2

ZIC – no data

ZIR – no data

ZDP – inactive spouse to include all data

NO ZIC, ZIR

4.  Vet has a current and inactive spouse

ZDP – with data for current/active spouse

ZIC – with data

ZIR – with data

ZDP – inactive spouse to include all data

NO ZIC, ZIR

5.  Vet with spouse and active dependents

ZDP – spouse with data

ZIC – with data

ZIR – with data

ZDP – dependent with data

ZIC – with data

ZIR – with data

6.  Vet with inactive dependents, no spouse

ZDP – set seq 6 to 2

ZIC no data

ZIR – no data

ZDP – with inactive dependent data

NO ZIC, NO ZIR

### V*IST*A Initiated – Enrollment/Eligibility Query Data Transmission – (QRY)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH Message Header

QRD Query Definition *(SEQ 1-4,7-10,12)*

SEQ 1 – Query Date/Time

SEQ 2 – Query Format Code *(“R”: Record-Oriented)*

SEQ 3 – Query Priority *(“I”: Immediate)*

> SEQ 4 – Query ID *(Internal VISTA-specific Patient DFN\[component separator\]Integration Control Number (ICN)*

SEQ 7 – Quantity Limited Request *(“1~RD”: One/single record)*

SEQ 8 – Who Subject Filter *(VISTA-specific Patient SSN)*

SEQ 9 – What Subject Filter *(“OTH”: Other)*

SEQ 10 – What Department Data Code *(“ENROLLMENT”)*

SEQ 11 – What data code value

> (Date for which to return enrollment, if no date is specified assume the most recent enrollment data is being requested.)

SEQ 12 – Query Results Level *(“T”: Full Results)*

QRF Query Filter *(SEQ 1,4,5)*

SEQ 1 – Where Subject Filer *(“IVM”)*

SEQ 4 – What User Qualifier *(VISTA-specific Patient Date of Birth)*

SEQ 5 – Other Subject Query Filter *(VISTA-specific Patient Sex; “M” or “F”)*

### Enrollment/Eligibility Data Transmission – (ORF~Z11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enrollment/Eligibility Data Transmission transmits a veteran’s eligibility and enrollment information from the HEC to the VAMCs.

MSH Message Header

MSA Message Acknowledgment

QRD Query Definition *(segment as submitted in VISTA initiated query)*

QRF Query Filter *(segment as submitted in VISTA initiated query)*

PID Patient Identification Segment *(SEQ 1-3,5,7,8,19)*

ZPD VA-Specific Patient Info Segment *(SEQ 1,12,13,30,34,35,40,41-45)*

ZIE VA-Specific Patient Ineligible Segment *(SEQ 1-4)*

ZIO VA-Specific Patient Info Segment *(SEQ 1-10)*

{ZEL VA-Specific Patient Eligibility Segment *(SEQ 1,2,5-8,10,11,13-25,29,34,35,38-47, 48, 49,50 for primary eligibility and SEQ 1-2 for all other eligibilities)*

}

{\[ZE2 VA-Specific Patient Eligibility (Addtl) Segment (1-3)

\]}

\[ZHF VA-Specific Health Factor Segment

\]

{\[ZTE VA Specific Temporary Eligibility Segment

\]}

\[{ZCE VA Specific Community Care Eligibility Segment (SEQ 1-4)

}\]

\[{ZHP VA-Specific Health Benefit Plan Segment *(SEQ 1-4)*

}\]

ZEN VA-Specific Enrollment Segment *(SEQ 1-19)*

ZMT VA-Specific Means Test Information Segment *(SEQ 1,3)*

> In this message, the segment is meant only to convey the Means Test status on which the enrollment priority was based. The SET ID Field should contain a value of “1” (“1” means that the segment refers to a means test and “2” means that the segment refers to a copay test) and SEQ 3 should contain the means test status.

ZCD VA-Specific Catastrophic Disability Segment *(SEQ 1-17)*

ZSP VA-Specific Service Period Segment *(SEQ 1-4,6-8,10,13)*

{ZMH} VA-Specific Military History Segment *(SEQ 1-5, 8, 9, 10)*

{ZRD VA-Specific Rated Disabilities Segment *(SEQ 1-3,12-14)*

}

\[OBX Observation/Result Segment *(SEQ 1-3,5,11,12,14-17) – NTR(SEQ 2,3,5,11,14,16) – Sensitive Patient Information*

\]

### Enrollment/Eligibility Data Transmission – (ORU~Z11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enrollment/Eligibility Data Transmission transmits a veteran’s eligibility and enrollment information from the HEC to the VAMCs.

BHS Batch Header

{MSH Message Header

PID Patient Identification Segment *(SEQ 1-3,5,7,8,19)*

ZPD VA-Specific Patient Info Segment *(SEQ 1,12,13,30,34,35,40,41-45)*

ZIE VA-Specific Patient Ineligible Segment *(SEQ 1-4)*

ZIO VA-Specific Patient Info Segment *(SEQ 1-10)*

{ZEL VA-Specific Patient Eligibility Segment *(SEQ 1,2,5-8,10,11,13-25,29,34,35,38-47, 48, 49,50 for primary eligibility and SEQ 1,2 for all other eligibilities)*

}

{\[ZE2 VA-Specific Patient Eligibility (Addtl) Segment (1-3)

\]}

\[ZHF VA-Specific Health Factor Segment

\]

{\[ZTE VA Specific Temporary Eligibility Segment

\]}

\[{ZCE VA Specific Community Care Eligibility Segment (SEQ 1-4)

}\]

\[{ZHP VA-Specific Health Benefit Plan Segment *(SEQ 1-4)*

}\]

ZEN VA-Specific Enrollment Segment *(SEQ 1-19)*

ZMT VA-Specific Means Test Information Segment *(SEQ 1,3)* In this message

> the segment is meant only to convey the means test status on which the enrollment priority was based. The SET ID Field should contain a value of ‘1’ (‘1’ means that the segment refers to a means test and ‘2’ means that the segment refers to a copay test) and SEQ 3 should contain the means test status.

ZCD VA-Specific Catastrophic Disability Segment *(SEQ 1-17)*

ZSP VA-Specific Service Period Segment *(SEQ 1-4,6-8,10,13)*

{ZMH} VA-Specific Military History Segment *(SEQ 1-5, 8, 9, 10)*

{ZRD VA-Specific Rated Disabilities Segment *(SEQ 1-3,12-14)*

}

\[OBX Observation/Result Segment *(SEQ 1-3,5,11,12,14-17) – NTR(SEQ 2,3,5,11,14,16) – Sensitive Patient Information*

\]

}

BTS Batch Trailer

## Trigger Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enrollment Trigger Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following enrollment events in V*ist*A will trigger an HL7 Full Data Transmission (ORU~Z07) message to be sent to the HEC for a patient.

#### Trigger Events Implemented via File Cross-References

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 30%" />
<col style="width: 24%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name (File #)</strong></th>
<th><strong>Field Name (Field #)</strong></th>
<th><strong>Cross-Reference</strong></th>
<th><strong>API Call</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>PRIMARY ELIGIBILITY (.361)</td>
<td>AENR361</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>ELIGIBILITY (.01) in the PATIENT ELIGIBILITIES sub-file (2.0361)</td>
<td>AENR01</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>DATE OF DEATH (.351)</td>
<td>AENR351</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>SERVICE CONNECTED (.301)</td>
<td>AENR301</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>SERVICE CONNECTED PERCENTAGE (.302)</td>
<td>AENR302</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>POW STATUS INDICATED (.525)</td>
<td>AENR525</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>RECEIVING A&amp;A BENEFITS (.36205)</td>
<td>AENR36205</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>RECEIVING HOUSEBOUND BENEFITS (.36215)</td>
<td>AENR36215</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>RECEIVING A VA PENSION (.36235)</td>
<td>AENR36235</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>TOTAL ANNUAL VA CHECK AMOUNT (.36295)</td>
<td>AENR36295</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>DISABILITY RET. FROM MILITARY (.362)</td>
<td>AENR362</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>MEDICAID (.381)</td>
<td>AENR381</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>EXPOSED TO AGENT ORANGE (.32102)</td>
<td>AENR32102</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>RADIATION EXPOSURE (.32103)</td>
<td>AENR32103</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>SW ASIA CONDITIONS (.322013)</td>
<td>AENR322013</td>
<td>AUTOUPD^DGENA2</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>NAME (.01)</td>
<td>AENR01</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>SEX (.02)</td>
<td>AENR02</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>DATE OF BIRTH (.03)</td>
<td>AENR03</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>STREET ADDRESS [LINE 3] (.113)</td>
<td>AENR113</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>COUNTY (.117)</td>
<td>AENR117</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>PHONE NUMBER [RESIDENCE] (.131)</td>
<td>AENR131</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>PHONE NUMBER [WORK] (.132)</td>
<td>AENR132</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>INELIGIBLE DATE (.152)</td>
<td>AENR152</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>EMERGENCY RESPONSE INDICATOR (.181)</td>
<td>AENR181</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>COMBAT VETERAN END DATE (.5295)</td>
<td>AENR5295</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>*CLAIM FOLDER LOCATION (#.312)</td>
<td>AENR312</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>ADDRESS CHANGE DT/TM (#.118)</td>
<td>AENR118</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>RESIDENTIAL ADDR CHANGE DT/TM (#.1158)</td>
<td>AENR1158</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>APPOINTMENT REQUEST DATE (#1010.1511)</td>
<td>AENR10101511</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>APPOINTMENT REQUEST ON 1010EZ (#1010.159)</td>
<td>AENR1010159</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>BAD ADDRESS INDICATOR (#.121)</td>
<td>AENR121</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>CLAIM NUMBER (#313)</td>
<td>AENR313</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>CONFIDENTIAL ADDR CHANGE DT/TM (#.14112)</td>
<td>AENR14112</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>CONFIDENTIAL ADDRESS COUNTY (#.14111)</td>
<td>AENR14111</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>COVERED BY HEALTH INSURANCE? (#.3192)</td>
<td>AENR3192</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>CURRENT PURPLE HEART REMARKS (#.533)</td>
<td>AENR533</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>CURRENT PURPLE HEART STATUS (#.532)</td>
<td>AENR532</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>DATE MEDICAID LAST ASKED (#.382)</td>
<td>AENR382</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>DATE OF DEATH LAST UPDATED (#.354)</td>
<td>AENR354</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>DATE OF DECISION (#.392)</td>
<td>AENR392</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>DECIDED BY (#.391)</td>
<td>AENR391</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>ELIGIBILITY STATUS (#.3611)</td>
<td>AENR3611</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>ELIGIBILITY STATUS DATE (#.3612)</td>
<td>AENR3612</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>ELIGIBILITY VERIF. METHOD (#.3615)</td>
<td>AENR3615</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>EMPLOYER NAME (#.3111)</td>
<td>AENR3111</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>EMPLOYMENT STATUS (#.31115)</td>
<td>AENR31115</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>FACILITY MAKING DETERMINATION (#.393)</td>
<td>AENR393</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>INELIGIBLE REASON (#.307)</td>
<td>AENR307</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>INELIGIBLE VARO DECISION (#.1656)</td>
<td>AENR1656</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>INTEGRATED CONTROL NUMBER (#991.01)</td>
<td>AENR99101</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>MARITAL STATUS (#.05)</td>
<td>AENR05</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>METHOD OF DETERMINATION (#.395)</td>
<td>AENR395</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>P&amp;T (#.304)</td>
<td>AENR304</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>PERIOD OF SERVICE (#.323)</td>
<td>AENR323</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>PREFERRED LANGUAGE (#2.07,.02)</td>
<td>AC</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>PRIMARY NOK CHANGE DATE/TIME (#.21012)</td>
<td>AENR21012</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>RATED INCOMPETENT? (#.293)</td>
<td>AENR293</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>PENSION AWARD EFFECTIVE DATE(#.3851)</td>
<td>AENR3851</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>PENSION AWARD REASON(#.3852)</td>
<td>AENR3852</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>RECEIVING VA DISABILITY? (#.3025)</td>
<td>AENR3025</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>REVIEW DATE (#.394)</td>
<td>AENR394</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>SOURCE OF NOTIFICATION (#.353)</td>
<td>AENR353</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>TEMPORARY ADDRESS CHANGE DT/TM (#.12113)</td>
<td>AENR12113</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>TEMPORARY ADDRESS COUNTY (#.12111)</td>
<td>AENR12111</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>TEMPORARY PHONE NUMBER (#.1219)</td>
<td>AENR1219</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>USER ENROLLEE SITE (#.3618)</td>
<td>AENR3618</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>USER ENROLLEE VALID THROUGH (#.3617)</td>
<td>AENR3617</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>SECONDARY NOK CHANGE DATE/TIME (#.211012)</td>
<td>AENR211012</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>E-CONTACT CHANGE DATE/TIME (#.33012)</td>
<td>AENR33012</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>E2-CONTACT CHANGE DATE/TIME (#.33112)</td>
<td>AENR33112</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td>PATIENT (#2)</td>
<td>DESIGNEE CHANGE DATE/TIME (#.3412)</td>
<td>AENR3412</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT (#2)</td>
<td>PREFERRED FACILITY (#27.02)</td>
<td>AENR2702</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>RATED DISABILITIES SUB-FILE (#.3721)</p></td>
<td>DISABILITY % (#2)</td>
<td>AENR2</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>RATED DISABILITIES SUB-FILE (#.3721)</p></td>
<td>RATED DISABILITIES (VA) (#.01)</td>
<td>AENR01</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>RATED DISABILITIES SUB-FILE (#.3721)</p></td>
<td>SERVICE CONNECTED (#3)</td>
<td>AENR3</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE (#.3121)</p></td>
<td>*GROUP NUMBER (#2)</td>
<td>AENR2</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE (#.3121)</p></td>
<td>EFFECTIVE DATE OF POLICY (#8)</td>
<td>AENR8</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE(#.3121)</p></td>
<td>GROUP PLAN (#.18)</td>
<td>AENR18</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE (#.3121)</p></td>
<td>INSURANCE EXPIRATION DATE (#3)</td>
<td>AENR3</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE (#.3121)</p></td>
<td>INSURANCE TYPE (#.01)</td>
<td>AENR01</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE (#.3121)</p></td>
<td>NAME OF INSURED (#17)</td>
<td>AENR17</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE (#.3121)</p></td>
<td>SUBSCRIBER ID (#1)</td>
<td>AENR1</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>INSURANCE TYPE SUB-FILE (#.3121)</p></td>
<td>WHOSE INSURANCE (#6)</td>
<td>AENR6</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>CD STATUS DIAGNOSES SUB-FILE (#.396)</p></td>
<td>CD STATUS DIAGNOSES (#.01)</td>
<td>AENR01</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>CD STATUS PROCEDURES SUB-FILE (#.397)</p></td>
<td>AFFECTED EXTREMITY (#1)</td>
<td>AENR1</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>CD STATUS PROCEDURES SUB-FILE (#.397)</p></td>
<td>CD STATUS PROCEDURES (#.01)</td>
<td>AENR01</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>CD STATUS CONDITIONS SUB-FILE (#.398)</p></td>
<td>CD STATUS CONDITIONS (#.01)</td>
<td>AENR01</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td><p>PATIENT FILE (#2)</p>
<p>CD STATUS CONDITIONS SUB-FILE (#.398)</p></td>
<td>PERMANENT INDICATOR (#2)</td>
<td>AENR2</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="odd">
<td><p>PATIENT FILE (#2)</p>
<p>CD STATUS CONDITIONS SUB-FILE (#.398)</p></td>
<td>SCORE (#1)</td>
<td>AENR1</td>
<td>EVENT^IVMPLOG</td>
</tr>
<tr class="even">
<td>PATIENT FILE (#2) COMMUNITY CARE PROGRAM SUB-FILE (#.191)</td>
<td>CCP LAST UPDATED DATE (#.01)</td>
<td>ACCCP</td>
<td>EECHG^DGRPCTRG</td>
</tr>
<tr class="odd">
<td>PATIENT FILE (#2) COMMUNITY CARE PROGRAM SUB-FILE (#.191)</td>
<td>COMMUNITY CARE PROGRAM CODE (#1)</td>
<td>ACCCP</td>
<td>EECHG^DGRPCTRG</td>
</tr>
<tr class="even">
<td>PATIENT FILE (#2) COMMUNITY CARE PROGRAM SUB-FILE (#.191)</td>
<td>EFFECTIVE DATE (#2)</td>
<td>ACCCP</td>
<td>EECHG^DGRPCTRG</td>
</tr>
<tr class="odd">
<td>PATIENT FILE (#2) COMMUNITY CARE PROGRAM SUB-FILE (#.191)</td>
<td>END DATE (#3)</td>
<td>ACCCP</td>
<td>EECHG^DGRPCTRG</td>
</tr>
<tr class="even">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>EFFECTIVE DATE (#.08)</td>
<td>AENR08</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>ENROLLMENT DATE (#.01)</td>
<td>AENR01</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>ENROLLMENT DATE (#.1)</td>
<td>AENR1</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>ENROLLMENT END DATE (#.11)</td>
<td>AENR11</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>ENROLLMENT PRIORITY (#.07)</td>
<td>AENR07</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>ENROLLMENT STATUS (#.04)</td>
<td>AENR04</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>ENROLLMENT SUBGROUP (#.12)</td>
<td>AENR12</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>FACILITY RECEIVED (#.06)</td>
<td>AENR06</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>PATIENT ENROLLMENT (#27.11)</td>
<td>SOURCE OF ENROLLMENT (#.03)</td>
<td>AENR03</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>MST HISTORY (#29.11)</td>
<td>MST CHANGE STATUS DATE (#.01)</td>
<td>AENR01</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>MST HISTORY (#29.11)</td>
<td>MST STATUS (#3)</td>
<td>AENR3</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>MST HISTORY (#29.11)</td>
<td>SITE DETERMINING STATUS (#6)</td>
<td>AENR6</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>BILLING PATIENT (#354)</td>
<td>COPAY INCOME EXEMPTION STATUS (#.04)</td>
<td>AENR04</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>BENEFICIARY TRAVEL CERTIFICATION (#392.2)</td>
<td>DATE CERTIFIED (#.01)</td>
<td>AENR01</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>PATIENT RELATION (#408.12)</td>
<td>RELATIONSHIP (#.02)</td>
<td>AENR02</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td><p>PATIENT RELATION (#408.12)</p>
<p>EFFECTIVE DATE SUB-FILE (#75)</p></td>
<td>EFFECTIVE DATE (#.01)</td>
<td>AENR01</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME PERSON (#408.13)</td>
<td>DATE OF BIRTH (#.03)</td>
<td>AENR03</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INCOME PERSON (#408.13)</td>
<td>MAIDEN NAME (#1.1)</td>
<td>AENR11</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME PERSON (#408.13)</td>
<td>NAME (#.01)</td>
<td>AENR09</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INCOME PERSON (#408.13)</td>
<td>SEX (#.02)</td>
<td>AENR02</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME PERSON (#408.13)</td>
<td>SOCIAL SECURITY NUMBER (#.09)</td>
<td>AENR09</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>ALL OTHER INCOME (#.17)</td>
<td>AENR17</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>CASH, AMOUNTS IN BANK ACCOUNTS (#2.01)</td>
<td>AENR201</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>DEBTS (#2.05)</td>
<td>AENR205</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>EDUCATIONAL EXPENSES (#1.03)</td>
<td>AENR103</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>FUNERAL AND BURIAL EXPENSES (#1.02)</td>
<td>AENR102</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>INTEREST, DIVIDEND, OR ANNUITY (#.15)</td>
<td>AENR15</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>MEDICAL EXPENSES (#1.01)</td>
<td>AENR101</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>MILITARY RETIREMENT (#.11)</td>
<td>AENR11</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>OTHER PROPERTY OR ASSETS (#2.04)</td>
<td>AENR204</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>OTHER RETIREMENT (#.13)</td>
<td>AENR13</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>REAL PROPERTY (#2.03)</td>
<td>AENR203</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>SOCIAL SECURITY (NOT SSI) (#.08)</td>
<td>AENR08</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>STOCKS AND BONDS (#2.02)</td>
<td>AENR202</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>TOTAL INCOME FROM EMPLOYMENT (#.14)</td>
<td>AENR14</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>U.S. CIVIL SERVICE (#.09)</td>
<td>AENR09</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>U.S. RAILROAD RETIREMENT (#.1)</td>
<td>AENR1</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>UNEMPLOYMENT COMPENSATION (#.12)</td>
<td>AENR12</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>WORKERS COMP. OR BLACK LUNG (#.16)</td>
<td>AENR16</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INDIVIDUAL ANNUAL INCOME (#408.21)</td>
<td>YEAR (#.01)</td>
<td>AENR01</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME RELATION (#408.22)</td>
<td>AMOUNT CONTRIBUTED TO SPOUSE (#.07)</td>
<td>AENR07</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INCOME RELATION (#408.22)</td>
<td>CHILD 18-23 IN SCHOOL (#.18)</td>
<td>AENR18</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME RELATION (#408.22)</td>
<td>CHILD HAD INCOME (#.11)</td>
<td>AENR11</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INCOME RELATION (#408.22)</td>
<td>CONTRIBUTED TO SPOUSAL SUPPORT (#.21)</td>
<td>E40822</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME RELATION (#408.22)</td>
<td>CONTRIBUTED TO SUPPORT (#.1)</td>
<td>AENR1</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INCOME RELATION (#408.22)</td>
<td>DEPENDENT CHILDREN (#.08)</td>
<td>AENR08</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME RELATION (#408.22)</td>
<td>INCAPABLE OF SELF-SUPPORT (#.09)</td>
<td>AENR09</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INCOME RELATION (#408.22)</td>
<td>INCOME AVAILABLE TO YOU (#.12)</td>
<td>AENR12</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME RELATION (#408.22)</td>
<td>LIVED WITH PATIENT (#.06)</td>
<td>AENR06</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>INCOME RELATION (#408.22)</td>
<td>MARRIED LAST CALENDAR YEAR (#.05)</td>
<td>AENR05</td>
<td>DGRTRIG</td>
</tr>
<tr class="even">
<td>INCOME RELATION (#408.22)</td>
<td>NUMBER OF DEPENDENT CHILDREN (#.13)</td>
<td>AENR13</td>
<td>DGRTRIG</td>
</tr>
<tr class="odd">
<td>ANNUAL MEANS TEST (#408.31)</td>
<td>DATE/TIME TEST LAST EDITED (#2.02)</td>
<td>AENR202</td>
<td>DGRTRIG</td>
</tr>
</tbody>
</table>

#### Trigger Events Implemented via Event Drivers

| Event Driver     | Event Protocol               | API Call   |
|----------------------|----------------------------------|----------------|
| DG MEANS TEST EVENTS | DGEN AUTOMATIC ENROLLMENT UPDATE | AUTOUPD^DGENA2 |

#### Trigger Events Implemented via Routine Hook

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 28%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th><strong>API Call (Hook)</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DGMSTAPI</td>
<td>NEWSTAT^DGMSTAPI</td>
<td><p>Call to create a new MST HISTORY FILE (#29.11) entry.</p>
<p>Will also queue HL7 message for HEC database updates</p></td>
</tr>
</tbody>
</table>

### IVM Trigger Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IVM events in V*ist*A will trigger an HL7 Full Data Transmission (ORU~Z07) message to be sent to the HEC for a patient.

#### Trigger Events Implemented via File Cross-References

| File/Field \#                      | Cross-Reference | Function Call |
|----------------------------------------|---------------------|-------------------|
| *PATIENT (#2) FILE*                |                     |                   |
| NAME (.01)                             | IVM01               | DPT^IVMPXFR       |
| SEX (.02)                              | IVM02               | DPT^IVMPXFR       |
| DATE OF BIRTH (.03)                    | IVM03               | DPT^IVMPXFR       |
| SOCIAL SECURITY NUMBER (.09)           | IVM09               | DPT^IVMPXFR       |
| STREET ADDRESS \[LINE 1\] (.111)       | IVM111              | DPT^IVMPXFR       |
| STEEET ADDRESS \[LINE 2\] (-112)       | IVM112              | DPT^IVMPXFR       |
| STREET ADDRESS \[LINE 3\] (.113)       | IVM113              | DPT^IVMPXFR       |
| CITY (.114)                            | IVM114              | DPT^IVMPXFR       |
| STATE (.115)                           | IVM115              | DPT^IVMPXFR       |
| COUNTY (.117)                          | IVM117              | DPT^IVMPXFR       |
| ZIP+4 (.1112)                          | IVM1112             | DPT^IVMPXFR       |
| PHONE NUMBER \[RESIDENCE\] (.131)      | IVM131              | DPT^IVMPXFR       |
| PHONE NUMBER \[WORK\] (.132)           | IVM132              | DPT^IVMPXFR       |
| DATE OF DEATH (.351)                   | IVM351              | DPT^IVMPXFR       |
| RESIDENTIAL ADDRESS \[LINE 1\] (.1151) | IVM1151             | DPT^IVMPXFR       |
| RESIDENTIAL ADDRESS \[LINE 2\] (-1152) | IVM1152             | DPT^IVMPXFR       |
| RESIDENTIAL ADDRESS \[LINE 3\] (.1153) | IVM1153             | DPT^IVMPXFR       |
| RESIDENTIAL CITY (.1154)               | IVM1154             | DPT^IVMPXFR       |
| RESIDENTIAL STATE (.1155)              | IVM1155             | DPT^IVMPXFR       |
| RESIDENTIAL COUNTY (.1157)             | IVM1157             | DPT^IVMPXFR       |
| RESIDENTIAL ZIP+4 (.1156)              | IVM1156             | DPT^IVMPXFR       |
| RESIDENTIAL PROVINCE (.11571)          | IVM11571            | DPT^IVMPXFR       |
| RESIDENTIAL POSTAL CODE (.11572)       | IVM11572            | DPT^IVMPXFR       |
| RESIDENTIAL COUNTRY (.11573)           | IVM11573            | DPT^IVMPXFR       |

#### Trigger Events Implemented via File Event Drivers

| Event Driver     | Event Protocol   | Function Call |
|----------------------|----------------------|-------------------|
| DG MEANS TEST EVENTS | IVM MEANS TEST EVENT | EN^IVMPMTE        |

#### Trigger Events Implemented via Routine Hook

| Routine Name | API Call (Hook) | Description                                                                                                                                                                                                                                       |
|------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DGNTAPI          | FILENTR^DGNTAPI     | Call to create a new NTR HISTORY FILE (#28.11) entry. Will also queue HL7 message for HEC database updates.                                                                                                                                           |
| DGRPEIS2         | LOGDCD^IVMCUC       | Routine hook will monitor changes to the fields contained on Screen \#9 (Income Screening Data) of the Registration module.                                                                                                                       |
| DGENCLEA         | AUTOUPD^DGENA2      | Call to trigger an HL7 Full Data Transmission (ORU~Z07) message to be sent to the HEC for a Veteran when the Veteran’s Military Service Episodes are edited, and they no longer meet the eligibility qualifications to receive Camp Lejeune benefits. |
| DGRP6EF          | AUTOUPD^DGENA2      | Call to trigger an HL7 Full Data Transmission (ORU~Z07) message to be sent to the HEC for a patient when the Camp Lejeune question is answered by the user.                                                                                           |

# # Appendix B – HL7 Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each HL7 segment, the data elements contained in the segment are described in table format. These tables are described in the following sections. The abbreviated column headings contained in the tables and associated HL7 data types are also defined.

## HL7 Abbreviated Column Headings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Column Heading | Definition                                           |
|--------------------|----------------------------------------------------------|
| SEQ                | Sequence of data element in segment                      |
| LEN                | Maximum length of data element                           |
| DT                 | Data Type                                                |
| R/O                | Required/Optional (R = Required, blank = Optional)       |
| RP/#               | Repeats/Maximum number of repetitions (Y for repeats)    |
| TBL#               | Number of corresponding HL7 user defined/supported table |

## HL7 Data Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Data Type | Definition                                                      | VA FileMan Data Type |
|---------------|---------------------------------------------------------------------|--------------------------|
| AD            | Address                                                             | Free Text                |
| CE            | Coded Element                                                       | Set of Codes or Pointer  |
| CK            | Check Digit                                                         | No Equivalent            |
| CM            | Composite                                                           | No Equivalent            |
| CP            | Composite Price                                                     | Free Text                |
| CX            | Extended Composite ID with Check Digit                              | Set of Codes or Pointer  |
| DLN           | Driver’s License Number                                             | No Equivalent            |
| DT            | Date                                                                | Date Only                |
| EI            | Entity Identifier                                                   | Set of Codes or Pointer  |
| FT            | Formatted Text Data                                                 | No Equivalent            |
| HD            | Hierarchic Designator                                               | No Equivalent            |
| ID            | Coded Value                                                         | Set of Codes or Pointer  |
| IS            | Coded Value for user-defined tables                                 | Set of Codes or Pointer  |
| NM            | Numeric                                                             | Numeric                  |
| PN            | Person Name                                                         | Free Text                |
| PT            | Processing Type                                                     | No Equivalent            |
| SI            | Sequence ID                                                         | Numeric                  |
| ST            | String                                                              | Free Text                |
| TM            | Time                                                                | Time Only                |
| TN            | Telephone Number                                                    | Free Text                |
| TS            | Time Stamp                                                          | Date/Time                |
| TX            | Text                                                                | Word processing          |
| XCN           | Extended Composite ID Number and Name for Persons                   | No Equivalent            |
| XON           | Extended Composite Name and Identification Number for Organizations | No Equivalent            |
| XPN           | Extended Person Name                                                | No Equivalent            |
| XTN           | Extended Telecommunication Number                                   | No Equivalent            |
| XAD           | Extended Address (Complex)                                          | No Equivalent            |

## HL7 Segment Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Financial Transaction (FTI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 29%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>ELEMENT NAME</strong></th>
<th><strong>V<em>IST</em>A<br />
File# 301.61 – IVM BILLING TRANSMISSION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>0</td>
<td></td>
<td></td>
<td>Set ID-FT1</td>
<td>SEQUENTIAL NUMBER</td>
</tr>
<tr class="even">
<td>2</td>
<td>12</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Transaction ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>3</td>
<td>10</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Transaction Batch ID</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>4</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Transaction Date</td>
<td>DATE BILL CREATED (#.07)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Transaction Posting Date</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>8</td>
<td>IS</td>
<td>R</td>
<td></td>
<td>0017</td>
<td>Transaction Type</td>
<td><p>If BILL CANCELLED (#.11) then 2</p>
<p>If DATE BILL CLOSED (#.1) AND</p>
<p>DATE LAST TRANSMITTED (#.13)</p>
<p>Then 4</p>
<p>If AMOUNT COLLECTED (#.09) AND</p>
<p>DATE LAST TRANSMITTED (#.13)</p>
<p>Then 3</p>
<p>Else 1</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>80</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Transaction Code</td>
<td>This field is used to uniquely identify each bill or charge which is stored in this file. This number will be equal to the bill number for insurance claims, or to the REFERENCE NUMBER (#.01) for charges stored in File #350, INTEGRATED BILLING ACTIONS.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td>B</td>
<td></td>
<td></td>
<td>Transaction Description</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>40</td>
<td>ST</td>
<td>B</td>
<td></td>
<td></td>
<td>Transaction Description – Alt</td>
<td><p>4 Components:</p>
<p>CLASSIFICATION (#.03)</p>
<p>BILL TYPE (#.04)</p>
<p>BILL FROM (#.05)</p>
<p>BILL TO (#.06)</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>9</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Transaction Quantity</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>12</td>
<td>CP</td>
<td>O</td>
<td></td>
<td></td>
<td>Transaction Amount – Extended</td>
<td>AMOUNT COLLECTED (#.09)</td>
</tr>
<tr class="even">
<td>12</td>
<td>13</td>
<td>CP</td>
<td>O</td>
<td></td>
<td></td>
<td>Transaction Amount – Unit</td>
<td>AMOUNT BILLED (#.08)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0049</td>
<td>Department Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Insurance Plan Id</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>12</td>
<td>CP</td>
<td>O</td>
<td></td>
<td></td>
<td>Insurance Amount</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>Assigned Patient Location</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0024</td>
<td>Fee Schedule</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>18</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0018</td>
<td>Patient Type</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0051</td>
<td>Diagnosis Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>20</td>
<td>120</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Performed By Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>21</td>
<td>120</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Ordered By Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>22</td>
<td>12</td>
<td>CP</td>
<td>O</td>
<td></td>
<td></td>
<td>Unit Cost</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>23</td>
<td>22</td>
<td>EI</td>
<td>O</td>
<td></td>
<td></td>
<td>Filter Order Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>24</td>
<td>120</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Entered By Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>25</td>
<td>80</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0088</td>
<td>Procedure Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>26</td>
<td>80</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0340</td>
<td>Procedure Code Modifier</td>
<td>Not used</td>
</tr>
</tbody>
</table>

### Insurance Segment (IN1) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 29%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A File Field or Expression</strong></th>
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
<td>Set ID-Insurance</td>
<td>Sequential number.</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Insurance Plan ID</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>6</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Insurance Company ID</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>4</td>
<td>45</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Insurance Company Name</td>
<td>NAME Field (#.01) of INSURANCE COMPANY (#36) File.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td>Insurance Company Address</td>
<td>ADDRESS fields (#.111-.116) of INSURANCE COMPANY (#36) File.</td>
</tr>
<tr class="even">
<td>6</td>
<td>48</td>
<td>PN</td>
<td></td>
<td></td>
<td></td>
<td>Insurance Co. Contact Pers</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>TN</td>
<td></td>
<td></td>
<td></td>
<td>Insurance Co. Phone Number</td>
<td>PHONE NUMBER Field (#.131) of INSURANCE COMPANY (#36) File.</td>
</tr>
<tr class="even">
<td>8</td>
<td>12</td>
<td>ST</td>
<td>*R</td>
<td></td>
<td></td>
<td>Group Number</td>
<td>GROUP NUMBER Field (.04) of GROUP INSURANCE PLAN File. (#355.3).</td>
</tr>
<tr class="odd">
<td>9</td>
<td>35</td>
<td>ST</td>
<td>*R</td>
<td></td>
<td></td>
<td>Group Name</td>
<td>GROUP NAME Field (.03) of GROUP INSURANCE PLAN File (#355.3).</td>
</tr>
<tr class="even">
<td>10</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Insured’s Group Emp. ID</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>45</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Insured’s Group Emp. Name</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Plan Effective Date</td>
<td>EFFECTIVE DATE OF POLICY (Mult .312, Field #8) of PATIENT (#2) File.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Plan Expiration Date</td>
<td>INSURANCE EXPIRATION DATE (Mult .312, Field #4) of PATIENT (#2) File.</td>
</tr>
<tr class="even">
<td>14</td>
<td>55</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Authorization Information</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Plan Type</td>
<td>TYPE OF PLAN Field (#.09), of GROUP INSURANCE PLAN (#355.3) File.</td>
</tr>
<tr class="even">
<td>16</td>
<td>48</td>
<td>PN</td>
<td>*R</td>
<td></td>
<td></td>
<td>Name of Insured</td>
<td>NAME OF INSURED (Mult .312, Field #6) (Mult. .312, Field #17) of PATIENT (#2) File.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Insured’s Relation To Patient</td>
<td>WHOSE INSURANCE Field of PATIENT (#2) File.</td>
</tr>
<tr class="even">
<td>18</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Insured’s Date of Birth</td>
<td>INSURED’S DOB field (#60.08) of the INSURANCE VERIFICATION PROCESSOR file (#355.33)<br />
*Required if patient is not the policy holder.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td>Insured’s Address</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>20</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Assignment of Benefits</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Coordination of Benefits</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>22</td>
<td>2</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Cord. of Benefits Priority</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>23</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Notice of Admission Code</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>24</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Notice of Admission Date</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>25</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Rpt of Eligibility Code</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>26</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Rpt of Eligibility Date</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Release of Information Code</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>28</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Pre-Admit Cert. (Pac)</td>
<td>IS PRE-CERT. REQ. Field (#.06) of GROUP INSURANCE PLAN File (#355.3).</td>
</tr>
<tr class="odd">
<td>29</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Verification Date</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>30</td>
<td>60</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Verification By</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>31</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Type of Agreement Code</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>32</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Billing Status</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>33</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Lifetime Reserve Days</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>34</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Delay Before L. R. Day</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>35</td>
<td>8</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Company Plan Code</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>36</td>
<td>15</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Policy Number</td>
<td>INSURANCE NUMBER (Mult 2.312, Field #1) of PATIENT (#2) File.</td>
</tr>
<tr class="odd">
<td>37</td>
<td>12</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Policy Deductible</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>38</td>
<td>12</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Policy Limit – Amount</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>39</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Policy Limit – Days</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>40</td>
<td>12</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Room Rate – Semi Private</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>41</td>
<td>12</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Room Rate – Private</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>42</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Insured’s Employment Status</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>43</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Insured’s Sex</td>
<td>Not used at this time.</td>
</tr>
<tr class="even">
<td>44</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td>Insured’s Employer Address</td>
<td>Not used at this time.</td>
</tr>
</tbody>
</table>

- Field SEQ 8 and Field SEQ 9 – At a minimum, one of these fields is required.
- Field SEQ 16 – This field is required if Field SEQ 17 does not contain a “v” for veteran.

### Notes and Comments Segment (NTE) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
ANNUAL MEANS TEST (#408.31) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential number</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>ID</td>
<td></td>
<td></td>
<td>0105</td>
<td>Source of Comment</td>
<td>Not used at this time.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>120</td>
<td>TX</td>
<td></td>
<td></td>
<td></td>
<td>Comment</td>
<td>COMMENT Field (#50)</td>
</tr>
</tbody>
</table>

### Patient Identification Segment (PID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 36%" />
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
<th><strong>V<em>IST</em>A Description<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID – Patient ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>CX</td>
<td>O</td>
<td></td>
<td></td>
<td>Primary Long ID</td>
<td>Integrated Control # (ICN) (991.01) &amp; Checksum (991.02) – ICN &amp; “V” &amp; Checksum</td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td>CX</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (Internal ID)</td>
<td>Pointer to entry in PATIENT (#2) File</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>CX</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Alternate Patient ID</td>
<td>PRIMARY SHORT ID Field (#.364) or VA(“PID)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>48</td>
<td>XPN</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient Name</td>
<td>NAME Field (#.01)</td>
</tr>
<tr class="even">
<td>6</td>
<td>48</td>
<td>XPN</td>
<td>O</td>
<td></td>
<td></td>
<td>Mother’s Maiden Name</td>
<td>MOTHER’S MAIDEN NAME Field (#.2403)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Date/Time of Birth</td>
<td>DATE OF BIRTH (#.03)</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0001</td>
<td>Sex</td>
<td>SEX (#.02)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>48</td>
<td>XPN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Patient Alias</td>
<td>ALIAS (Multiple 1, Field #.01)</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0005</td>
<td>Race</td>
<td>Race</td>
</tr>
<tr class="odd">
<td>11</td>
<td>106</td>
<td>XAD</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Patient Address</td>
<td><p>ADDRESS Field Identified by Address Type</p>
<p>Permanent (USA: .111 - .115, .1112, .1173 Foreign: .111 - .114, .1171-.1173)</p>
<p>Confidential (USA: .141, .1411-.1418, .14111, .14116 Foreign: .141, .1411-.1414, .1417, .1418, .14114-.14116)</p>
<p>Residential (USA:.1151-.1157,.11573, Foreign: .1151-.1154,.11571-.11573)</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>4</td>
<td>IS</td>
<td>B</td>
<td></td>
<td></td>
<td>County Code</td>
<td>VA COUNTY CODE Field (#.117)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>40</td>
<td>XTN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Phone Number – Home</td>
<td><p>PHONE NUMBER (RESIDENCE) Field (#.131)</p>
<p>PHONE NUMBER (WORK) Field (#.132)</p>
<p>EMAIL ADDRESS (#.133)</p>
<p>PHONE NUMBER [CELLULAR] (#.134)</p>
<p>PAGER NUMBER (#.135)</p>
<p>CONFIDENTIAL PHONE NUMBER Field (#.1315)</p></td>
</tr>
<tr class="even">
<td>14</td>
<td>40</td>
<td>XTN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Phone Number – Business</td>
<td>PHONE NUMBER (WORK) Field (#.132)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Primary Language</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0002</td>
<td>Marital Status</td>
<td>MARITAL STATUS Field (#.05)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0006</td>
<td>Religion</td>
<td>Religion Field(#.08)</td>
</tr>
<tr class="even">
<td>18</td>
<td>20</td>
<td>CK</td>
<td>O</td>
<td></td>
<td></td>
<td>Patient Account Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>16</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>SSN Number – Patient</td>
<td>SOCIAL SECURITY NUMBER Field (#.09)</td>
</tr>
<tr class="even">
<td>20</td>
<td>25</td>
<td>DLN</td>
<td>O</td>
<td></td>
<td></td>
<td>Driver’s License Number – Patient</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>21</td>
<td>20</td>
<td>CK</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Mother’s Identifier</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0189</td>
<td>Ethnic Group</td>
<td>Ethnicity Information Multiple (#2.06.01)</td>
</tr>
<tr class="odd">
<td>23</td>
<td>60</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Birth Place</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>Multiple Birth Indicator</td>
<td>Multiple Birth Indicator Field (#994)</td>
</tr>
<tr class="odd">
<td>25</td>
<td>2</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Birth Order</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>26</td>
<td>4</td>
<td>IS</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Citizenship</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>27</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0172</td>
<td>Veterans Military Status</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>28</td>
<td>80</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Nationality</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>29</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Patient Death and Time</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>30</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>Patient Death Indicator</td>
<td>Not used</td>
</tr>
</tbody>
</table>

### Patient Demographic 1 Segment (PD1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 36%" />
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
<th><strong>V<em>IST</em>A Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>2</td>
<td>IS</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID</td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Living Arrangement</td>
<td>NOT USED</td>
</tr>
<tr class="odd">
<td>3</td>
<td>90</td>
<td>XON</td>
<td></td>
<td></td>
<td></td>
<td>CIRN (Master of Record) ~ ~ Station Number</td>
<td>CIRN MASTER OF RECORD (Field 991.03) ~ ~ STATION NUMBER (File #4 Field 99)</td>
</tr>
<tr class="even">
<td>4</td>
<td>90</td>
<td>XCN</td>
<td></td>
<td></td>
<td></td>
<td>PATIENT PRIMARY CARE PROVIDER NAME &amp; ID No</td>
<td><p>2 Sub-Components</p>
<p>Pointer to entry in NEW PERSON File (#200) &amp;</p>
<p>Facility Number (File #389.9 Field.04)</p>
<p>&lt;family name (ST) &gt;</p>
<p>&lt;last name prefix (ST)&gt;</p>
<p>&lt;given name (ST)&gt;</p>
<p>&lt;middle initial or name (ST)&gt;</p>
<p>&lt;suffix (e.g., JR or III) (ST)&gt;</p>
<p>&lt;prefix (e.g., DR) (ST)&gt;</p>
<p>&lt;degree (e.g., MD) (IS)&gt;</p>
<p>This will always be <strong>VA200</strong> (NEW PERSON File)</p></td>
</tr>
</tbody>
</table>

### Query Definition Segment (QRD) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | Element Name            | V*IST*A Description                                                                                                 |
|---------|---------|--------|---------|----------|----------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------|
| 1       | 26      | TS     | R       |          |          | Query Date/Time             | Date/Time query was generated.                                                                                          |
| 2       | 1       | ID     | R       |          | 0106     | Query Format Code           | See Table 0106 in Appendix C for codes.                                                                                 |
| 3       | 1       | ID     | R       |          | 0091     | Query Priority              | See Table 0091 in Appendix C for codes.                                                                                 |
| 4       | 23      | ST     | R       |          |          | Query ID                    | V*IST*A -specific internal entry number of PATIENT (#2) File and Integration Control Number (ICN) if available. |
| 5       | 1       | ID     |         |          |          | Deferred Response Type      | Not used at this time.                                                                                                  |
| 6       | 26      | TS     |         |          |          | Deferred Response Date/Time | Not used at this time.                                                                                                  |
| 7       | 10      | CQ     | R       |          | 0126     | Quantity Limited Request    | See Table 0126 in Appendix C for codes.                                                                                 |
| 8       | 20      | ST     | R       |          |          | Who Subject Filter          | SOCIAL SECURITY NUMBER (#.09) Field of PATIENT (#2) File.                                                               |
| 9       | 3       | ID     | R       | Y        | 0048     | What Subject Filter         | See Table 0048 in Appendix C for codes.                                                                                 |
| 10      | 20      | ST     | R       | Y        |          | What Department Data Code   | Computed Field (Income Year).                                                                                           |
| 11      | 20      | ST     | R       | Y        |          | What Data Code Value        | Not used at this time.                                                                                                  |
| 12      | 1       | ID     |         |          | 0108     | Query Results Level         | See Table 0108 in Appendix C for codes.                                                                                 |

### Observation/Result Segment (OBX) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 7%" />
<col style="width: 28%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A DESCRIPTION</strong></th>
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
<td>Set ID – OBX</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>0125</td>
<td>Value Type</td>
<td>CE</td>
</tr>
<tr class="odd">
<td>3</td>
<td>590</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Observation Identifier</td>
<td><p>38.1^SECURITY LOG (patient security)</p>
<p><strong>V</strong><em>IST</em><strong>A</strong> ~28.11 (NTR)</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td>C</td>
<td></td>
<td></td>
<td>Observation Sub-ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>65536<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>*</td>
<td>C</td>
<td>Y<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
<td></td>
<td>Observation Value</td>
<td><p>Sensitive = Y (patient security)</p>
<p>Not Sensitive = N (patient security)</p>
<p>NOTE: This will be a repeating field for NTR.</p>
<p>&lt;identifier (ST)&gt;~&lt;text (ST)&gt;~&lt;name of coding system (ST)&gt;|&lt;identifier #2 (ST)&gt;~&lt;text #2(ST)&gt;~&lt;name of coding system #2(ST)&gt;|etc…</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Units</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>References Range</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>5</td>
<td>ID</td>
<td>O</td>
<td>Y/5</td>
<td>0078</td>
<td>Abnormal Flags</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>5</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Probability</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td>Y</td>
<td>0080</td>
<td>Nature of Abnormal Test</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0085</td>
<td>Observ Result Status</td>
<td><p>R=Results entered, Not verified (patient security)</p>
<p>F=Final Results (NTR)</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Date Last Obs Normal Values</td>
<td>Diagnosed With Head and Neck Cancer Date/Time (NTR)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>20</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>User Defined Access Checks</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Date/Time of the Observation</td>
<td><p>Date/Time of the Observation (patient security)</p>
<p>Verification Method Date/Time (NTR)</p></td>
</tr>
<tr class="odd">
<td>15</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Producer’s ID</td>
<td>Station Number of Site Reporting Verification Method Status (NTR)</td>
</tr>
<tr class="even">
<td>16</td>
<td>80</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Responsible Observer</td>
<td><p>‘Security Assigned Remotely By’ = AITC (patient security)</p>
<p>Component #14, Sub-Component #2 – Station Number of Site Reporting Diagnosed With Head and Neck Cancer Status (NTR)</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Observation Method</td>
<td><p>Verification Method: (NTR)</p>
<p>S (Qual Military Srvc)</p>
<p>M (Military Med Rec)</p>
<p>N (Not Qualified)</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>The length of the observation value field is variable, depending upon value type. See Sequence 2 in OBX table above.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>May repeat for multipart, single answer results with appropriate data types, e.g., CE, TX, and FT data types.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

### Query Filter Segment (QRF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | Element Name           | V*IST*A Description                          |
|---------|---------|--------|---------|----------|----------|----------------------------|--------------------------------------------------|
| 1       | 20      | ST     | R       | Y        |          | Where Subject Filter       | Identifies Dept., System to Which Query Pertains |
| 2       | 19      | TS     |         |          |          | When Data Start Date/Time  | Not used at this time                            |
| 3       | 20      | TS     |         |          |          | When Data End Date/Time    | Not used at this time                            |
| 4       | 20      | ST     |         | Y        |          | What User Qualifier        | Specific Patient Date of Birth                   |
| 5       | 20      | ST     |         | Y        |          | Other Query Subject Filter | Specific Patient Sex; “M” or “F”                 |

### Referral Information Segment (RF1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0283</td>
<td>Referral Status</td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>2</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0280</td>
<td>Referral Priority</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0281</td>
<td>Referral Type</td>
<td><p>SAD = Street Address Change</p>
<p>CAD = Confidential Address Change</p>
<p>CPH = Cell Phone Number Change</p>
<p>PNO = Pager Number Change</p>
<p>EAD = E-Mail Address Change</p>
<p>PHH – Home Phone Number Change</p>
<p>PHC = Confidential Phone Number Change</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0282</td>
<td>Referral Disposition</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0284</td>
<td>Referral Category</td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>EI</td>
<td>R</td>
<td></td>
<td>0363</td>
<td>Originating Referral Identifier</td>
<td><p>4 components:</p>
<p>1 – Site of Change</p>
<p>SAD (Field #.12 of the Patient [#2] File)</p>
<p>CAD (Field #.14113 of the Patient [#2] File)</p>
<p>CPH (Field #.13111 of the Patient [#2] File)</p>
<p>PNO (Field #.1314 of the Patient [#2] File)</p>
<p>EAD (Field #.138 of the Patient [#2] File)</p>
<p>PHH (Field #.1323 of the Patient [#2] File)</p>
<p>PHW(Field #.132 of the Patient [#2] File)</p>
<p>PHC (Field #.14123 of the Patient [#2] File)</p>
<p>2 – Source of Change</p>
<p>SAD (Field #.119 of the Patient [#2] File)</p>
<p>CAD (n/a)</p>
<p>CPH (Field #.1311 of the Patient [#2] File)</p>
<p>PNO (Field #.1313 of the Patient [#2] File)</p>
<p>EAD (Field #.137 of the Patient [#2] File)</p>
<p>PHH (Field #.1322 of the Patient [#2] File)</p>
<p>PHC (Field #.14122 of the Patient [#2] File)</p>
<p>3 – Not Used</p>
<p>4 – Not used</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Effective Date</td>
<td><p>Date/Time of change</p>
<p>SAD (Field #.118 of the Patient [#2] File)</p>
<p>CAD (Field #.14112 of the Patient [#2] File)</p>
<p>CPH (Field #.139 of the Patient [#2] File)</p>
<p>PNO (Field #.1312 of the Patient [#2] File)</p>
<p>EAD (Field #.136 of the Patient [#2] File)</p>
<p>PHH (Field #.1321 of Patient [#2] File)</p>
<p>PHW (Field #.1326 of Patient [#2] File)</p>
<p>PHC (Field #.14121 of Patient [#2] File)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Expiration Date</td>
<td>Invalid Address Date (TBD at a later date)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Process Date</td>
<td>Date Checked by NCOA (TBD at a later date)</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>VA061</td>
<td>Referral Reason</td>
<td>Invalid Address Reason (TBD at a later date)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>30</td>
<td>EI</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>External Referral Identifier</td>
<td>Not Used</td>
</tr>
</tbody>
</table>

### VA-Specific Address Validation Segment (ZAV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A PATIENT File (#2) Field</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>5</td>
<td>IS</td>
<td>R</td>
<td></td>
<td></td>
<td>Address Type</td>
<td><p>Expected values:</p>
<p>P for Permanent Mailing Address</p>
<p>R for Residential Address</p>
<p>C for Temporary Mailing Address</p>
<p>CNF for Confidential Address</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>2</td>
<td>IS</td>
<td>R</td>
<td></td>
<td></td>
<td>Address Validation Indicator</td>
<td><p>Street Addr CASS Ind (Field #.1118)</p>
<p>Residential CASS Ind (Field #.1159)</p>
<p>Temporary Addr CASS Ind (Field #.12115)</p>
<p>Confidential Addr CASS Ind (Field #.14117)</p>
<p>Expected values:</p>
<p>Y – Certified</p>
<p>F – Failed</p>
<p>NC – Not Checked</p>
<p>PV – Processing</p></td>
</tr>
</tbody>
</table>

### VA-Specific Beneficiary Travel Segment (ZBT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A BENEFICIARY TRAVEL CERTIFICATION File (#392.2) Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date Certified</td>
<td>Date Certified Field (#.01) of File #392.2</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA01</td>
<td>Eligible</td>
<td>Eligible Field (#3) of File #392.2</td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Amount Certified</td>
<td>Amount Certified Field (#4) of File #392.2</td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA02</td>
<td>Means Test Status</td>
<td>Means Test Status (A;8) of File #392.2</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA04</td>
<td>Primary Eligibility Code</td>
<td>Primary Elig. Code (A;9) of File #392.2</td>
</tr>
<tr class="odd">
<td>7</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Travel Claim Date/Time</td>
<td>Claim Date/Time (#.01) of File #392</td>
</tr>
<tr class="even">
<td colspan="8">Fields are from BENEFICIARY TRAVEL CLAIM File (#392).</td>
</tr>
</tbody>
</table>

### VA-Specific Catastrophic Disability Segment (ZCD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 36%" />
<col style="width: 32%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>SEQUENTIAL NUMBER</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td>R</td>
<td></td>
<td></td>
<td>Review Date</td>
<td>REVIEW DATE (#394)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>35</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Decided by</td>
<td>DECIDED BY (.#391)</td>
</tr>
<tr class="even">
<td>4</td>
<td>7</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>VA0115</td>
<td>Facility Making Determination</td>
<td>FACILITY MAKING DETERMINATION (#393)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>8</td>
<td>DT</td>
<td>R</td>
<td></td>
<td></td>
<td>Date of Decision</td>
<td>DATE OF DECISION (#392)</td>
</tr>
<tr class="even">
<td>6</td>
<td>60</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>VA041</td>
<td>Determination Method</td>
<td>METHOD OF DETERMINATION Field (#395)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>CD Diagnosis</td>
<td>CD STATUS DIAGNOSES Field (#396)</td>
</tr>
<tr class="even">
<td>8</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>CD Procedure</td>
<td>CD STATUS PROCEDURES Field (#397)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>VA042</td>
<td>Affected Extremity</td>
<td>AFFECTED EXTREMITY Field (#397.1)</td>
</tr>
<tr class="even">
<td>10</td>
<td>4</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>VA043</td>
<td>CD Condition</td>
<td>CD STATUS CONDITIONS Field (#398)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>6</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Score</td>
<td>SCORE Field (#398.1). Valid Value any whole number.</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0136</td>
<td>Catastrophically Disabled</td>
<td>VETERAN CATASTROPHICALLY DISABLED? Field (#399.39)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>VA045</td>
<td>Permanent Indicator</td>
<td>PERMANENT INDICATOR Field (#398.2)</td>
</tr>
<tr class="even">
<td>14</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>Date Veteran Requested CD Evaluation</td>
<td>DATE VETERAN REQUESTED CD EVAL (#.3951)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>Date Facility Initiated Review</td>
<td>DATE FACILITY INITIATED REVIEW (#.3952)</td>
</tr>
<tr class="even">
<td>16</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>Date Veteran Was Notified</td>
<td>DATE VETERAN WAS NOTIFIED (#.3953)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td>R</td>
<td>VA440</td>
<td>CD DESCRIPTOR</td>
<td>CD DESCRIPTOR field (#.401)</td>
</tr>
</tbody>
</table>

### VA-Specific Community Care Eligibility Segment (ZCE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 31%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Community Care Program Code</td>
<td><p>Expected Values:</p>
<p>A – ART/IVF</p>
<p>C – Marriage/Family Counseling</p>
<p>I – Newborn</p>
<p>T – Transplant</p>
<p>COMMUNITY CARE PRORAM CODE (Sub-File #2.191, Field #1) of PATIENT (#2) File.</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>8</td>
<td>DT</td>
<td>R</td>
<td></td>
<td></td>
<td>Effective Date</td>
<td>EFFECTIVE DATE (Sub-File #2.191, Field #2) of PATIENT (#2) File.</td>
</tr>
<tr class="even">
<td>4</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>End Date</td>
<td>END DATE (Sub-File #2.191, Field #3) of PATIENT (#2) File.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>19</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>CCP Last Updated Date</td>
<td><p>Date/Time the Program Code was Assigned / Unassigned</p>
<p>CCP LAST UPDATED DATE (Sub-File #2.191, Field #.01) of PATIENT (#2) File.</p></td>
</tr>
</tbody>
</table>

### VA-Specific Emergency Contact Segment (ZCT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 31%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Contact Type</td>
<td>1=NOK, 2=2<sup>nd</sup> NOK, 3=E-Contact, 4=2<sup>nd</sup> E-Contact, 5=Designee</td>
</tr>
<tr class="odd">
<td>3</td>
<td>35</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Contact Name</td>
<td>Name of Contact Person (See note below.)</td>
</tr>
<tr class="even">
<td>4</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Contact Relationship</td>
<td>Relationship to Patient of Contact Person (See note below.)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td>Contact Address</td>
<td>Address of Contact Person (See note below.)</td>
</tr>
<tr class="even">
<td>6</td>
<td>40</td>
<td>TN</td>
<td></td>
<td></td>
<td></td>
<td>Contact Phone Number</td>
<td>Phone Number of Contact Person (See note below.)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>TN</td>
<td></td>
<td></td>
<td></td>
<td>Contact Work Phone Number</td>
<td>Work Phone Number of Contact Person (See note below.)</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Contact Address Same As NOK?</td>
<td>Address Same as Patient’s (See Note – NOK And NOK2 Only)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Contact Person Same As NOK?</td>
<td>Same as NOK? (See Note – First E-Contact And Designee Only)</td>
</tr>
<tr class="even">
<td>10</td>
<td>24</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Contact Date/Time Last Updated</td>
<td>PRIMARY NOK CHANGE DATE/TIME (#.21012)</td>
</tr>
<tr class="odd">
<td colspan="8">Note: Data is returned from various PATIENT File nodes based on the CONTACT TYPE:<br />
Type=1, Node=.21; Type=2, Node=.211; Type=3, Node=.33; Type=4, Node=.331; Type=5, Node=34.</td>
</tr>
</tbody>
</table>

### VA-Specific Patient Dependent Information Segment (ZDP) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>48</td>
<td>PN</td>
<td>R</td>
<td></td>
<td></td>
<td>Name</td>
<td>* NAME Field (#.01)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0001</td>
<td>Sex</td>
<td>* SEX Field (#.02)</td>
</tr>
<tr class="even">
<td>4</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date of Birth</td>
<td>* DATE OF BIRTH Field (#.03)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Social Security Number</td>
<td>* SOCIAL SECURITY NUMBER Field (#.09)</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA009</td>
<td>Relationship To Patient</td>
<td>RELATIONSHIP (#.02) Field of PATIENT RELATION (#408.12 ) File</td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Internal Entry Number</td>
<td>Internal Entry Number(IEN) of entry in PATIENT RELATION (#408.12) File</td>
</tr>
<tr class="even">
<td>8</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Spouse’s Maiden Name</td>
<td>MAIDEN NAME Field (#1.1) of INCOME PERSON File (#408.13)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Dependent Date</td>
<td>EFFECTIVE DATE (Mult 408.1275; Field #.01)</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Pseudo SSN Reason</td>
<td><p>PSEUDO SSN REASON (#.1)</p>
<p>R=REFUSED TO PROVIDE</p>
<p>S=SSN UNKNOWN/FOLLOW-UP REQUIRED</p>
<p>N=NO SSN ASSIGNED</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Inactivation Date</td>
<td><p>Calculated Value from 408.1275;.01 and</p>
<p>408.1275;.02</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>SSN Verification Status</td>
<td>SSN VERIFICATION STATUS (#..11)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>250</td>
<td>XAD</td>
<td></td>
<td></td>
<td></td>
<td>SPOUSE ADDRESS</td>
<td>SPOUSE ADDRESS (1.2, 1.3, 1.4, 1.5, 1.6, 1.7, (1.9)</td>
</tr>
<tr class="even">
<td>14</td>
<td>250</td>
<td>XTN</td>
<td></td>
<td></td>
<td></td>
<td>SPOUSE HOME PHONE NUMBER</td>
<td>SPOUSE HOME PHONE NUMBER (1.8)</td>
</tr>
</tbody>
</table>

### VA-Specific Patient Eligibility Segment (ZEL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number (1 is always Primary Elig.)</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA004</td>
<td>Eligibility Code</td>
<td>Eligibility Code</td>
</tr>
<tr class="odd">
<td>3</td>
<td>16</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Long ID</td>
<td>Long ID (Multiple 361, Field #.01)</td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Short ID</td>
<td>Short ID (Multiple 361, Field #.04)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0136</td>
<td>Military Disability Retirement</td>
<td><p>Military Disability Retirement Field (#.3602)</p>
<p>Data values:</p>
<p>1=YES, RECEIVING MILITARY RETIREMENT</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Claim Folder Number</td>
<td>CLAIM FOLDER NUMBER Field (#.313)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Claim Folder Location</td>
<td>*CLAIM FOLDER LOCATION Field (#.312)</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Veteran?</td>
<td>VETERAN? Field (#1901)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Type of Patient</td>
<td>TYPE OF PATIENT Field (#391)</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA006</td>
<td>Eligibility Status</td>
<td>ELIGIBILITY STATUS Field (#.3611)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Eligibility Status Date</td>
<td>ELIGIBILITY STATUS DATE Field (#.3612)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Eligibility Interim Response</td>
<td>ELIGIBILITY INTERIM RESPONSE Field (#.3614)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>50</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Eligibility Verification Method</td>
<td>ELIGIBILITY VERIFICATION METHOD Field (#.3615)</td>
</tr>
<tr class="even">
<td>14</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Receiving A&amp;A Benefits?</td>
<td>RECEIVING A&amp;A BENEFITS? Field (#.36205)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Receiving Housebound Benefits?</td>
<td>RECEIVING HOUSEBOUND BENEFITS? Field (#.36215)</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Receiving A VA Pension?</td>
<td>RECEIVING VA PENSION? Field (#.36235)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Receiving A VA Disability?</td>
<td>Receiving VA Disability? Field (#.3025)</td>
</tr>
<tr class="even">
<td>18</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Exposed To Agent Orange</td>
<td>AGENT ORANGE EXPOS. INDICATED Field (#.32102)</td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Radiation Exposure Indicated</td>
<td>RADIATION EXPOSURE INDICATED? Field (#.32103)</td>
</tr>
<tr class="even">
<td>20</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>SW Asia Conditions</td>
<td>SW ASIA CONDITIONS? Field (#.322013)</td>
</tr>
<tr class="odd">
<td>21</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Total Annual VA Check Amount</td>
<td>TOTAL ANNUAL VA CHECK AMOUNT Field (#.36295)</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA022</td>
<td>Radiation Exposure Method</td>
<td>RADIATION EXPOSURE METHOD Field (#.3212)</td>
</tr>
<tr class="odd">
<td>23</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA036</td>
<td>Current MST Status</td>
<td>Computed</td>
</tr>
<tr class="even">
<td>24</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>MST Status Change Date</td>
<td>Computed</td>
</tr>
<tr class="odd">
<td>25</td>
<td>7</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA0115</td>
<td>Site Determining MST status</td>
<td>Computed</td>
</tr>
<tr class="even">
<td>26</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Agent Orange Reg Date</td>
<td>AGENT ORANGE REGISTRATION DATE Field (#.32107)</td>
</tr>
<tr class="odd">
<td>27</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Agent Orange Exam Date</td>
<td>AGENT ORANGE EXAM DATE Field (#.32109)</td>
</tr>
<tr class="even">
<td>28</td>
<td>6</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Agent Orange Reg #</td>
<td>AGENT ORANGE REGISTRATION # Field (#.3211)</td>
</tr>
<tr class="odd">
<td>29</td>
<td>20</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Agent Orange Exposure Location</td>
<td>AGENT ORANGE EXPOSURE LOCATION Field (#.3213)</td>
</tr>
<tr class="even">
<td>30</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Radiation Exposure Date</td>
<td>RADIATION EXPOSURE DATE Field (#.32111)</td>
</tr>
<tr class="odd">
<td>31</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>SW Asia Conditions Exam Date</td>
<td>SW ASIA COND. EXAM DATE Field (#.322015)</td>
</tr>
<tr class="even">
<td>32</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>SW Asia Conditions Reg Date</td>
<td>SW ASIA COND.. REGISTRATION DATE Field (#.322014)</td>
</tr>
<tr class="odd">
<td>33</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Monetary Benefits Date</td>
<td>MONETARY BEN. VERIFY DATE Field (#.306)</td>
</tr>
<tr class="even">
<td>34</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>User Enrollee Valid Through</td>
<td>USER ENROLLEE STATUS (#.3617)</td>
</tr>
<tr class="odd">
<td>35</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>User Enrollee Site</td>
<td>USER ENROLLEE STIE (#.3618)</td>
</tr>
<tr class="even">
<td>36</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Eligibility Verification Source and Site</td>
<td>Not used at this time</td>
</tr>
<tr class="odd">
<td>37</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Combat Veteran Eligibility Indicator</td>
<td>COMBAT SERVICE INDICATED? Field (#.5291) (Computed)</td>
</tr>
<tr class="even">
<td>38</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Combat Veteran Eligibility End Date</td>
<td>COMBAT VETERAN END DATE Field (#.5295)</td>
</tr>
<tr class="odd">
<td>39</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0136</td>
<td>Discharge Due to Disability</td>
<td><p>Discharge Due to Disability Field (#.3603)</p>
<p>Data values:</p>
<p>1=YES, RECEIVING MILITARY RETIREMENT</p></td>
</tr>
<tr class="even">
<td>40</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td>0136</td>
<td>SHAD (Shipboard Hazard And Defense)</td>
<td>PROJ 112/SHAD (#.3215)</td>
</tr>
<tr class="odd">
<td>41</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td>Camp Lejeune</td>
<td>CAMP LEJEUNE INDICATED (#.321701)</td>
</tr>
<tr class="even">
<td>42</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Camp Lejeune Date</td>
<td>CAMP LEJEUNE DATE (#.321702)</td>
</tr>
<tr class="odd">
<td>43</td>
<td>10</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Camp Lejeune Change Site</td>
<td>CAMP LEJEUNE CHANGE SITE (#.321703)</td>
</tr>
<tr class="even">
<td>44</td>
<td>10</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Camp Lejeune Source</td>
<td>CAMP LEJEUNE SOURCE (#.321704)</td>
</tr>
<tr class="odd">
<td>45</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>OTH Eligibility Indicator</td>
<td><p>Values:</p>
<p>Blank – patient was never OTH</p>
<p>0 – patient was OTH, but not any longer</p>
<p>1 – patient is OTH</p></td>
</tr>
<tr class="even">
<td>46</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td>OTH Eligibility Factor Code</td>
<td><p>Values:</p>
<p>‘1’ – OTH-90</p>
<p>‘2’ – OTH-EXT</p></td>
</tr>
<tr class="odd">
<td>47</td>
<td>TS</td>
<td>19</td>
<td></td>
<td></td>
<td></td>
<td>OTH Eligibility Update Date</td>
<td>Date/Time of OTH Eligibility Change</td>
</tr>
<tr class="even">
<td>48</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>TOXIC EXPOSURE RISK ACTIVITY (TERA) INDICATOR</td>
<td>TOXIC EXPOSURE INDICATED? (.32116)</td>
</tr>
<tr class="odd">
<td>49</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>PERSIAN GULF INDICATOR</td>
<td>Persian Gulf Deployment Cohort (#.32117)</td>
</tr>
<tr class="even">
<td>50</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>PERSSIAN GULF INDICATOR CHANGE DATE/TIME</td>
<td>Persian Gulf Last Change Date (#.32118)</td>
</tr>
</tbody>
</table>

### VA-Specific Health Factor Segment (ZHF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression<br />
PRESUMPTIVE PSYCHOSIS CATEGORY CHANGES (#33.1) File Field or Expression</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>3</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Presumptive Psychosis (PP) Category</td>
<td><p>PRESUMPTIVE PSYCHOSIS CATEGORY</p>
<p>File# 2 (Field# .5601)</p>
<p>File# 33.1 (Field# .33.12, .02)</p>
<p>Values:</p>
<p>'REJ' = REJECTED DUE TO INCOME</p>
<p>'LES' = LESS THAN 24 MONTHS SERVICE</p>
<p>'OTH' = FSM WITH OTH (PP ONLY)</p>
<p>'DEC' = VETERAN DECLINES ENROLLMENT</p>
<p>'ACD’ = ACDUTRA</p>
<p>‘DVA’ = DVA 12D W/CH 17, SEEN FOR SC/MST</p>
<p>‘ENR’ = ENROLLED</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>PP Category Change Date</td>
<td><p>Date/Time of Presumptive Psychosis Category Change</p>
<p>File# 33.1 (Field# .33.12, .01)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>PP STATUS</td>
<td><p>CURRENT PP STATUS</p>
<p>(Not Used)</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>PP STATUS CHANGE DATE</td>
<td><p>PP CHANGE STATUS DATE</p>
<p>(Not Used)</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>7</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>PP STATUS SITE</td>
<td><p>SITE DETERMINING STATUS</p>
<p>(Not Used)</p></td>
</tr>
</tbody>
</table>

### VA-Specific Patient Eligibility (Addtl) Segment (ZE2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>109</td>
<td>DR</td>
<td>R</td>
<td></td>
<td></td>
<td>Pension Dates</td>
<td><p>2 components:</p>
<p>1 – Pension Award Effective Date (Field #.3851 of the Patient [#2] File)</p>
<p>2 – Pension Terminated Date (Field #.3853 of the Patient [#2] File</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>51</td>
<td>CWE</td>
<td></td>
<td></td>
<td></td>
<td>Pension Award Reason Code</td>
<td>Pension Award Reason (Field #.3852 of the Patient [#2] File</td>
</tr>
<tr class="odd">
<td>3</td>
<td>51</td>
<td>CWE</td>
<td></td>
<td></td>
<td></td>
<td>Pension Terminated Reason(s)</td>
<td><p>Pension Terminated Reason #1 (Field #.3854 of the Patient [#2] File</p>
<p>Pension Terminated Reason #2 (Field #.3855 of the Patient [#2] File</p>
<p>Pension Terminated Reason #3 (Field #.3856 of the Patient [#2] File</p>
<p>Pension Terminated Reason #4 (Field #.3857 of the Patient [#2] File</p></td>
</tr>
</tbody>
</table>

### VA-Specific Employment Information Segment (ZEM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Employment Person</td>
<td>1 if Patient, 2 if Spouse</td>
</tr>
<tr class="odd">
<td>3</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA003</td>
<td>Employment Status</td>
<td>Employment Status: Patient (#.31115) or Spouse (#.2515)</td>
</tr>
<tr class="even">
<td>4</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Employer Name</td>
<td>Employer Name: Patient (#.3111) or Spouse (#.251)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Occupation</td>
<td>Occupation (#.07) or Spouse’s Occupation (#.2514)</td>
</tr>
<tr class="even">
<td>6</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td>Employer Address</td>
<td>Employer Address: Patient (#.3113-#.3118) or Spouse (#.252-#.257)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>TN</td>
<td></td>
<td></td>
<td></td>
<td>Employer Phone</td>
<td>Employer Phone Number: Patient (#.3119) or Spouse (#.258)</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Government Agency</td>
<td>Government Agency (#.3112) (Patient Only)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date of Retirement</td>
<td><p>Date of Retirement Patient (#.31116) ,Spouse (#</p>
<p>.2516)</p></td>
</tr>
</tbody>
</table>

### VA-Specific Enrollment Segment (ZEN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 30%" />
<col style="width: 36%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Enrollment Date</td>
<td>ENROLLMENT DATE Field (#.1) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Source of Enrollment</td>
<td><p>SOURCE OF ENROLLMENT Field (#.03) of the PATIENT ENROLLMENT File (#27.11)</p>
<p>1 = VAMC; 2 = HEC; 3 = Other VAMC</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA015</td>
<td>Enrollment Status</td>
<td>ENROLLMENT STATUS Field (#.04) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA016</td>
<td>Reason Canceled/Declined</td>
<td>REASON CANCELED/DECLINED Field #.05) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="even">
<td>6</td>
<td>60</td>
<td>TX</td>
<td></td>
<td></td>
<td></td>
<td>Canceled/Declined Remarks</td>
<td>CANCELED/DECLINED REMARKS Field (#25) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>7</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA0115</td>
<td>Facility Received</td>
<td>FACILITY RECEIVED Field (#.06) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="even">
<td>8</td>
<td>7</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA0115</td>
<td>Preferred Facility</td>
<td>PREFERRED FACILITY Field (#27.02) of the PATIENT File (#2)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA017</td>
<td>Enrollment Priority</td>
<td>ENROLLMENT PRIORITY Field (#.07) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="even">
<td>10</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Effective Date</td>
<td>EFFECTIVE DATE Field (#.08) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Enrollment Date</td>
<td>ENROLLMENT DATE Field (#.01) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Enrollment End Date</td>
<td>ENROLLMENT END DATE Field (#.11) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA035</td>
<td>Enrollment Sub-group</td>
<td>ENROLLMENT SUB-GROUP Field (#.12) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="even">
<td>14</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Preferred Facility Source Designation</td>
<td><p>SOURCE DESIGNATION Field (#.2702) of the PATIENT File (#2)</p>
<p>V=VistA; E=ESR; PA=PCP Active; PI=PCP Inactive</p></td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA117</td>
<td>REASON FOR CLOSED APPLICATION (Z11 only)</td>
<td>REASON FOR CLOSED APPLICATION (.13)</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>PT APPLIED FOR ENROLLMENT?</td>
<td><p>PT APPLIED FOR ENROLLMENT? Field (#.14) of the PATIENT ENROLLMENT File (#27.11)</p>
<p>0 – No</p>
<p>1 – Yes</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td>REGISTRATION ONLY REASON</td>
<td><p>REGISTRATION ONLY REASON (.15) of the PATIENT ENROLLMENT File (#27.11) pointing to the PATIENT REGISTRATION ONLY REASON FILE (#408.43)</p>
<p>1 – C&amp;P DISABILITY BENEFITS EXAM</p>
<p>2 – ACTIVE DUTY</p>
<p>3 – SERVICE CONNECTED ONLY</p>
<p>4 – EXPOSURE REGISTRY EXAM</p>
<p>5 – RESEARCH</p>
<p>6 – HUMANITARIAN/EMERGENCY</p>
<p>7 – EMPLOYEE</p>
<p>8 – BENEFICIARY</p>
<p>9 – OTHER THAN HONORABLE (OTH)</p>
<p>10 – MARRIAGE/FAMILY COUNSELING</p>
<p>11 – COLLATERAL (OTHER)</p>
<p>12 – ART/IVF</p>
<p>13 – NEWBORN</p>
<p>14 – LEGISLATIVE MANDATE</p>
<p>15 – OTHER</p>
<p>16 – NORTH CHICAGO ACTIVE DUTY</p>
<p>17 – UNANSWERED</p>
<p>18 – CAREGIVER</p>
<p>19 – VHA TRANSPLANT PROGRAM</p></td>
</tr>
<tr class="even">
<td>18</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>REGISTRATION ONLY DATE</td>
<td>REGISTRATION ONLY DATE (.16) of the PATIENT ENROLLMENT File (#27.11)</td>
</tr>
<tr class="odd">
<td>19</td>
<td>8</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>SOURCE OF REGISTRATION</td>
<td><p>SOURCE OF REGISTRATION (.17) of the PATIENT ENROLLMENT File (#27.11)</p>
<p>Valid values:</p>
<p>1 – VAMC</p>
<p>2 – HEC</p>
<p>3 – HCA</p>
<p>4 – CARMA</p>
<p>5 – OTHER</p></td>
</tr>
</tbody>
</table>

### VA-Specific Fee Basis Segment (ZFE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 30%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A Field or Expression</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>200</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>VA033</td>
<td>Treatment Code</td>
<td>Treatment Code, shown as identifier and the name of the coding system. Ex: SHORT TERM FEE STATUS^^VA0033 is the identifier (SHORT TERM FEE STATUS) and the coding system (VA0033 table) The second piece of this string is null (text describing the identifier).</td>
</tr>
<tr class="odd">
<td>3</td>
<td>200</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>VA034</td>
<td>Fee Basis Program</td>
<td>Fee Basis Program, shown as the identifier and the name of the coding system. Ex: OUTPATIENT^^VA0034 is the identifier (OUTPATIENT) and the coding system (VA0034 table). The second piece of this string is null (text describing the identifier).</td>
</tr>
<tr class="even">
<td>4</td>
<td>26</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>Authorization From Date</td>
<td><p>Beginning date of the Fee Basis authorization</p>
<p>The date must be Y2K compliant.</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>Authorization To Date</td>
<td><p>Ending date of the Fee Basis authorization</p>
<p>The date must be Y2K compliant.</p></td>
</tr>
</tbody>
</table>

### VA-Specific Guardian Segment (ZGD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Guardian Type</td>
<td>1=VA Guardian; 2=Civil Guardian</td>
</tr>
<tr class="odd">
<td>3</td>
<td>35</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Guardian Name</td>
<td>Name of Guardian (See Note Below.)</td>
</tr>
<tr class="even">
<td>4</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Guardian Institution</td>
<td>Institution Where Guardian is Located (See Note Below.)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Guardian Relationship</td>
<td>Relationship To Patient of Guardian (See Note Below.)</td>
</tr>
<tr class="even">
<td>6</td>
<td>106</td>
<td>AD</td>
<td></td>
<td></td>
<td></td>
<td>Guardian Address</td>
<td>Address of Guardian (See Note Below.)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>TN</td>
<td></td>
<td></td>
<td></td>
<td>Guardian Phone Number</td>
<td>Phone Number of Guardian (See Note Below.)</td>
</tr>
<tr class="even">
<td>8</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date Ruled Incompetent</td>
<td>Date Ruled Incompetent (See Note Below.)</td>
</tr>
<tr class="odd">
<td colspan="8"><p>Data is returned from a different PATIENT File (#2) node depending on the GUARDIAN TYPE:</p>
<ul>
<li><p>If the GUARDIAN TYPE=1, data will be returned from the .29 node.</p></li>
<li><p>If the GUARDIAN TYPE=2, data will be returned from the .291 node.</p></li>
</ul></td>
</tr>
</tbody>
</table>

### VA-Specific Income Information Segment (ZIC) – old format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*This format of the ZIC segment is used when the Version of the means test is before FEB 2005 1010EZ (sequence 30 of the ZMT segment is equal to 0)*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
INDIVIDUAL ANNUAL INCOME (#408.21) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number (1 is always Primary Eligibility.)</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Income Year</td>
<td>YEAR Field (#.01) (Month and Date will be 0.)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Social Security</td>
<td>SOCIAL SECURITY (NOT SSI) Field (#.08)</td>
</tr>
<tr class="even">
<td>4</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Us Civil Service</td>
<td>U.S. CIVIL SERVICE Field (#.09)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Us Railroad Retirement</td>
<td>U.S. RAILROAD RETIREMENT Field (#.1)</td>
</tr>
<tr class="even">
<td>6</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Military Retirement</td>
<td>MILITARY RETIREMENT Field (#.11)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Unemployment Compensation</td>
<td>UNEMPLOYMENT COMPENSATION Field (#.12)</td>
</tr>
<tr class="even">
<td>8</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Other Retirement</td>
<td>OTHER RETIREMENT Field (#.13)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Employment Income</td>
<td>TOTAL INCOME FROM EMPLOYMENT Field (#.14)</td>
</tr>
<tr class="even">
<td>10</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Interest, Dividend, Annuity</td>
<td>INTEREST, DIVIDEND, ANNUITY Field (#.15)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Workers Comp/Black Lung</td>
<td>WORKERS COMP. OR BLACK LUNG Field (#.16)</td>
</tr>
<tr class="even">
<td>12</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Other Income</td>
<td>ALL OTHER INCOME Field (#.17)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Medical Expenses</td>
<td>MEDICAL EXPENSES Field (#1.01) (Veteran Only)</td>
</tr>
<tr class="even">
<td>14</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Funeral And Burial Expenses</td>
<td>FUNERAL AND BURIAL EXPENSES Field (#1.02) (Veteran Only)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Educational Expenses</td>
<td>EDUCATIONAL EXPENSES Field (#1.03) (Veteran Only)</td>
</tr>
<tr class="even">
<td>16</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Cash, Amount in Bank Accounts</td>
<td>CASH,AMOUNTS IN BANK ACCOUNTS Field (#2.01) [vet/spouse only]</td>
</tr>
<tr class="odd">
<td>17</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Stocks and Bonds</td>
<td>STOCKS AND BONDS Field (#2.02) (veteran/spouse only)</td>
</tr>
<tr class="even">
<td>18</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Real Property</td>
<td>REAL PROPERTY Field (#2.03) (veteran/spouse only)</td>
</tr>
<tr class="odd">
<td>19</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Other Property or Assets</td>
<td>OTHER PROPERTY OR ASSETS Field (#2.04) (veteran/spouse only)</td>
</tr>
<tr class="even">
<td>20</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Debts</td>
<td>DEBTS Field (#2.05) (veteran/spouse only)</td>
</tr>
<tr class="odd">
<td>21</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date Income Screening Collected</td>
<td>ENTERED ON Field (#102)</td>
</tr>
<tr class="even">
<td>22</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Site Conducting Test</td>
<td>SITE CONDUCTING TEST Field (#2.05)</td>
</tr>
<tr class="odd">
<td>23</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Source of Test</td>
<td>SOURCE OF TEST Field (#.23) – 1=VAMC, 2=IVM</td>
</tr>
</tbody>
</table>

### VA-Specific Income Information Segment (ZIC) – Feb 2005 1010EZ format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*This format of the ZIC segment is used when the Version of the means test is FEB 2005-101EZ (sequence 30 of the ZMT segment is equal to 1)*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
INDIVIDUAL ANNUAL INCOME (#408.21) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number (1 is always Primary Eligibility.)</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Income Year</td>
<td>YEAR Field (#.01) (Month and Date will be 0.)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Other Income Amounts (Soc. Sec., Compensation, Pension, Interest, Divid. Income)</td>
<td>SOCIAL SECURITY (NOT SSI) Field (#.08) [vet/spouse/child]</td>
</tr>
<tr class="even">
<td>9</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Total Employment Income (Wages, Bonuses, Tips)</td>
<td><p>TOTAL INCOME FROM EMPLOYMENT Field (#.14)</p>
<p>[vet/spouse/child]</p></td>
</tr>
<tr class="odd">
<td>12</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Net Income from Farm, Ranch, Property, Business</td>
<td>ALL OTHER INCOME Field (#.17) [vet/spouse/child]</td>
</tr>
<tr class="even">
<td>13</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Medical Expenses</td>
<td>MEDICAL EXPENSES Field (#1.01) [Veteran Only] <strong>The value is the adjusted medical expenses.</strong></td>
</tr>
<tr class="odd">
<td>14</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Funeral And Burial Expenses</td>
<td>FUNERAL AND BURIAL EXPENSES Field (#1.02) [Veteran Only]</td>
</tr>
<tr class="even">
<td>15</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Educational Expenses</td>
<td>EDUCATIONAL EXPENSES Field (#1.03) [Veteran Only]</td>
</tr>
<tr class="odd">
<td>16</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Cash, Amount in Bank Accounts (CDs, IRAs, Stocks, Bonds)</td>
<td>CASH,AMOUNTS IN BANK ACCOUNTS Field (#2.01) [vet/spouse/child]</td>
</tr>
<tr class="even">
<td>18</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Land, Bldgs Less Mortgage, Liens (Not Primary Home)</td>
<td>REAL PROPERTY Field (#2.03) [veteran/spouse/child]</td>
</tr>
<tr class="odd">
<td>19</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Other Property (Farm, Bus) or Assets (Art, Collectibles) Less Amt Owed</td>
<td>OTHER PROPERTY OR ASSETS Field (#2.04) [veteran/spouse/child]</td>
</tr>
</tbody>
</table>

### VA-Specific Health Benefit Plan Segment (ZHP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File, CURRENT HEALTH BENEFIT PLAN (#25.01) Sub-File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number (1 is always Primary Eligibility.)</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>HBP CODE</td>
<td>HBP CODE (#.01)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>19</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>HBP LAST UPDATE DATE</td>
<td>ASSIGNED DATE/TIME (#21)</td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>HBP LAST UPDATED BY</td>
<td>ASSIGNED ENTERED BY (#2)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>6</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>HBP LAST UPDATED BY STATION NUMBER</td>
<td>HBP LAST UPDATED BY STATION NUMBER</td>
</tr>
</tbody>
</table>

### VA-Specific Patient Ineligible Segment (ZIE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Ineligible Date</td>
<td>INELIGIBLE DATE Field (#.152)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Ineligible Reason</td>
<td>INELIGIBLE REASON Field (#.307)</td>
</tr>
<tr class="even">
<td>4</td>
<td>75</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Ineligible VARO Decision</td>
<td>INELIGIBLE VARO DECISION Field (#.1656)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Ineligible Twx City</td>
<td>INELIGIBLE TWX CITY (#.1653)</td>
</tr>
<tr class="even">
<td>6</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Ineligible Twx Source</td>
<td>INELIGIBLE TWX SOURCE (#.1651)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Ineligible Twx State</td>
<td>INELIGIBLE TWX STATE (#.1654)</td>
</tr>
</tbody>
</table>

### VA-Specific Inpatient/Outpatient Information Segment (ZIO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
V<em>IST</em>A Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Number of Inpatient Days Since Last Means Test</td>
<td>Computed field</td>
</tr>
<tr class="odd">
<td>3</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Number of Outpatient Days Since Last Means Test</td>
<td>Computed field</td>
</tr>
<tr class="even">
<td>4</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date of Last Visit</td>
<td>Computed field (Last Opt or Inpatient Stay)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0136</td>
<td>Appointment Request on 1010EZ</td>
<td>APPOINTMENT REQUEST ON 1010EZ (#1010.159)</td>
</tr>
<tr class="even">
<td>6</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Appointment Request Date</td>
<td>APPOINTMENT REQUEST DATE (#1010.1511)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Update Date/Time</td>
<td>Date/time stamp of appointment request on 1010E</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td>Original Appointment Request</td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Original Appointment Request Date</td>
<td></td>
</tr>
<tr class="even">
<td>10</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Update Date/Time</td>
<td>Date/time stamp of original appointment request</td>
</tr>
</tbody>
</table>

### VA-Specific Income Relation Segment (ZIR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 36%" />
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
<th><p><strong>V<em>IST</em>A Element Name</strong></p>
<p><strong>INCOME RELATION (#408.22) File Field or Expression</strong></p></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Married Last Calendar Year</td>
<td>MARRIED LAST CALENDAR YEAR Field (#.05)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Lived With Patient</td>
<td>LIVED WITH PATIENT Field (#.06)</td>
</tr>
<tr class="even">
<td>4</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Amount Contributed to Spouse</td>
<td>AMOUNT CONTRIBUTED TO SPOUSE Field (#.07)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Dependent Children</td>
<td>DEPENDENT CHILDREN Field (#.08)</td>
</tr>
<tr class="even">
<td>6</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Incapable of Self Support</td>
<td>INCAPABLE OF SELF-SUPPORT Field (#.09)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Contributed to Support</td>
<td>CONTRIBUTED TO SUPPORT Field (#.1)</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Child Had Income</td>
<td>CHILD HAD INCOME Field (#.11)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Income Available to You</td>
<td>INCOME AVAILABLE TO YOU Field (#.12)</td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Number of Dependent Children</td>
<td>NUMBER OF DEPENDENT CHILDREN Field (#.13)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>0</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Total Dependents</td>
<td>Computed: NUMBER OF DEPENDENT CHILDREN field (#.13) + 1 (If Spouse Indicated), (MARRIED LAST CALENDAR YEAR Field (#.05) or LIVED WITH PATIENT Field (#.06) or AMOUNT CONTRIBUTED TO SPOUSE Field (#.07)), otherwise, + 0</td>
</tr>
<tr class="even">
<td>12</td>
<td>0</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Patient Income</td>
<td>Computed: Income – same fields as ZIC incomes</td>
</tr>
<tr class="odd">
<td>13</td>
<td>0</td>
<td>ST</td>
<td></td>
<td></td>
<td>VA010</td>
<td>Total Dependents Not Applicable FOR MT Indicators AS,N,X,U</td>
<td>Computed: If MT Indicator not = to Cat A or Cat C, change number of dependents to XX (not applicable)</td>
</tr>
<tr class="even">
<td>14</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0136</td>
<td>Dependent Child School Indicator</td>
<td>CHILD 18-23 IN SCHOOL (#.18)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td>CONTRIBUTED TO SPOUSAL SUPPORT</td>
<td>CONTRIBUTED TO SPOUSAL SUPPORT (#.21)</td>
</tr>
</tbody>
</table>

### VA-Specific Message Processing Segment (Ziv)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 33%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>ELEMENT NAME</strong></th>
<th><strong>V<em>IST</em>A ELEMENT NAME<br />
V<em>IST</em>A Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential number</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Income Year</td>
<td>YEAR Field (#.01) Individual Annual Income (#408.21) File</td>
</tr>
<tr class="odd">
<td>3</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Client ID Error Message</td>
<td>No corresponding <strong>V</strong><em>IST</em><strong>A</strong> field at this time.</td>
</tr>
<tr class="even">
<td>4</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>New Client SSN</td>
<td>SSN Field (#.09) PATIENT (#2) File</td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Spouse ID Error Message</td>
<td>No corresponding <strong>V</strong><em>IST</em><strong>A</strong> field at this time.</td>
</tr>
<tr class="even">
<td>6</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>New Spouse SSN</td>
<td>SSN (.09) Income Person (#408.13) File</td>
</tr>
<tr class="odd">
<td>7</td>
<td>16</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Spouse ID (Internal Entry Number)</td>
<td>Internal Entry Number of PATIENT RELATION (#408.12) File</td>
</tr>
<tr class="even">
<td>8</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>IVM Care Status</td>
<td><p>0 – Cancel Z06 MT</p>
<p>1 – Create/Update Z06 MT and Close/Convert Case</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>16</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>IVM ID (Internal)</td>
<td>IVM SPECIFIC INTERNAL ENTRY ID Field (#.07)</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Insurance Upload Status</td>
<td><p>UPLOAD INSURANCE DATA (.04)</p>
<p>0 – NOT UPLOADED</p>
<p>1 – UPLOADED</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Reason Ins. Not Uploaded</td>
<td><p>REASON NOT UPLOADING INSURANCE Field (#.08)</p>
<p>1 – ALREADY HAVE INSURANCE POLICY</p>
<p>2 – DATA APPEARS TO BE INCORRECT</p>
<p>3 – INSURANCE COMPANY CLOSED</p>
<p>4 – POLICY PLAN TYPE IS HMO</p>
<p>5 – POLICY PLAN TYPE IS PPO</p>
<p>6 – POLICY COVERAGE EXPIRED</p>
<p>7 – POLICY BENEFITS FULLY USED</p>
<p>8 – BENEFITS NOT AVAILABLE</p>
<p>9 – COVERAGE FOR SPOUSE ONLY</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Client Date of Death</td>
<td>DATE OF DEATH Field (#.351) Patient (#2) File</td>
</tr>
<tr class="odd">
<td>13</td>
<td>2</td>
<td>NM</td>
<td>R</td>
<td></td>
<td></td>
<td>SOURCE OF INFORMATION CODE</td>
<td><p>EXPECTED VALUES:</p>
<p>3 – IVM</p>
<p>14 – Purchased Care CHOICE</p></td>
</tr>
</tbody>
</table>

### VA-Specific Military History Segment (ZMH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>ELEMENT NAME</strong></th>
<th><strong>VISTA ELEMENT NAME<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>SET ID – MILITARY HISTORY</td>
<td>SEQUENTIAL NUMBER</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>IF</td>
<td>R</td>
<td></td>
<td>VA038</td>
<td>MILITARY HISTORY TYPE</td>
<td>Varies based upon Service – (.321) or (.322) or (.52). See table below.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>SERVICE INDICATOR</td>
<td>Varies based upon Service – (.321) or (.322) or (.52). See table below</td>
</tr>
<tr class="even">
<td>4</td>
<td>29</td>
<td>DR</td>
<td>0</td>
<td></td>
<td></td>
<td>SERVICE ENTRY DATE AND SERVICE SEPARATION DATE</td>
<td>Varies based upon Service – (.321) or (.322) or (.52). See table below</td>
</tr>
<tr class="odd">
<td>5</td>
<td>8</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>VA026</td>
<td>SERVICE COMPONENT</td>
<td>Varies based upon Service – (.321) or (.322) or (.52). See table below</td>
</tr>
<tr class="even">
<td>6</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>FUTURE DISCHARGE DATE</td>
<td><p>FUTURE DISCHARGE DATE field # 2.3216,.08</p>
<p>The Future Discharge Date (FDD) will only occur on the ORU-Z11 or ORF-Z11 messages (NOTE: FDD will not occur on the ORU-07 and ORF-Z07). The FDD will only occur once. A patient cannot have more than one FDD. NOTE: The absence of the FDD record in the ZMH segment on the ORU-Z11 or ORF-Z11 HL7 message from ES will result in the deletion of the FDD record in VistA.</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>9</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>REASON FOR EARLY SEPARATION</td>
<td><p>REASON FOR EARLY SEPARATION field # 2.3216,.09</p>
<p>The Reason for Early Separation will only occur on the ORU-Z11 or ORF-Z11 messages (NOTE: Reason for Early Separation will not occur on the ORU-Z07 and ORF-Z07). The absence of the Reason for Early Separation on the ORU-Z11 or ORF-Z11 HL7 message from ES will result in the deletion of the Reason for Early Separation record in VistA.</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>10</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>SEPARATION REASON CODE</td>
<td><p>SEPARATION REASON CODE field # 2.3216,.1</p>
<p>The Separation Reason Code will only occur on the ORU-Z11 or ORF-Z11 messages (NOTE: Separation Reason Code will not occur on the ORU-Z07 and ORF-Z07). The absence of the Separation Reason Code on the ORU-Z11 or ORF-Z11 HL7 message from ES will result in the deletion of the Separation Reason Code record in VistA.</p></td>
</tr>
</tbody>
</table>

This table details the field number for each field \* - indicates multiple occurrences are possible

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Indicator #1</strong></th>
<th><strong>Indicator #2</strong></th>
<th><strong>Indicator #3</strong></th>
<th><strong>From Date</strong></th>
<th><strong>To Date</strong></th>
<th><strong>Service Component</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SL</td>
<td><p>Service Branch (#2.3216, .03)</p>
<p>OR</p>
<p>Service branch [Last] (.325)</p></td>
<td><p>Service Number (#2.3216, .05)</p>
<p>OR</p>
<p>Service number [Last] (.328)</p></td>
<td><p>Service Discharge Type (#2.3216, .06)</p>
<p>OR</p>
<p>Service Discharge Type [Last] (.324)</p></td>
<td><p>Service Entry Date (#2.3216, .01)</p>
<p>OR</p>
<p>Service Entry Date [Last] (.326)</p></td>
<td><p>Service Separation Date (#2.3216, .02)</p>
<p>OR</p>
<p>Service Separation Date [Last] (.327)</p></td>
<td><p>Service Component (#2.3216, .04)</p>
<p>OR</p>
<p>Service Component [Last] (.32911)</p></td>
</tr>
<tr class="even">
<td>SNL</td>
<td><p>Service Branch (#2.3216, .03)</p>
<p>OR</p>
<p>Service branch [NTL] (.3291)</p></td>
<td><p>Service Number (#2.3216, .05)</p>
<p>OR</p>
<p>Service number [NTL] (.3294)</p></td>
<td><p>Service Discharge Type (#2.3216, .06)</p>
<p>OR</p>
<p>Service Discharge Type [NTL] (.329)</p></td>
<td><p>Service Entry Date (#2.3216, .01)</p>
<p>OR</p>
<p>Service Entry Date [NTL] (.3292)</p></td>
<td><p>Service Separation Date (#2.3216, .02)</p>
<p>OR</p>
<p>Service Separation Date [NTL] (.3293)</p></td>
<td><p>Service Component (#2.3216, .04)</p>
<p>OR</p>
<p>Service Component [NTL] (.32912)</p></td>
</tr>
<tr class="odd">
<td>SNNL</td>
<td><p>Service Branch (#2.3216, .03)</p>
<p>OR</p>
<p>Service branch [NNTL] (.3296)</p></td>
<td><p>Service Number (#2.3216, .05)</p>
<p>OR</p>
<p>Service number [NNTL] (.3299)</p></td>
<td><p>Service Discharge Type (#2.3216, .06)</p>
<p>OR</p>
<p>Service Discharge Type [NNTL] (.3295)</p></td>
<td><p>Service Entry Date (#2.3216, .01)</p>
<p>OR</p>
<p>Service Entry Date [NNTL] (.3297)</p></td>
<td><p>Service Separation Date (#2.3216, .02)</p>
<p>OR</p>
<p>Service Separation Date [NNTL] (.3298)</p></td>
<td><p>Service Component (#2.3216, .04)</p>
<p>OR</p>
<p>Service Component [NNTL] (.32913)</p></td>
</tr>
<tr class="even">
<td>*MSD</td>
<td>Service Branch (#2.3216, .03)</td>
<td>Service Number (#2.3216, .05)</td>
<td>Service Discharge Type (#2.3216, .06)</td>
<td>Service Entry Date (#2.3216, .01)</td>
<td>Service Separation Date (#2.3216, .02)</td>
<td>Service Component (#2.3216, .04)</td>
</tr>
<tr class="odd">
<td>POW</td>
<td>POW Status Indicated (.525)</td>
<td>POW Confinement Location (.526)</td>
<td>Not used</td>
<td>POW from date (.527)</td>
<td>POW to date (.528)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>COMB</td>
<td>Combat Service Indicated (.5291)</td>
<td>Combat Service Location (.5292)</td>
<td>Not used</td>
<td>Combat from date (.5293)</td>
<td>Combat to date (.5294)</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>VIET</td>
<td>Vietnam Service Indicated (.32101)</td>
<td>Not used</td>
<td>Not used</td>
<td>Vietnam from date (.32104)</td>
<td>Vietnam to date (.32105)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>LEBA</td>
<td>Lebanon Service Indicated (.3221)</td>
<td>Not used</td>
<td>Not used</td>
<td>Lebanon from date (.3222)</td>
<td>Lebanon to date (.3223)</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>GREN</td>
<td>Grenada Service Indicated (.3224)</td>
<td>Not used</td>
<td>Not used</td>
<td>Grenada from date (.3325)</td>
<td>Grenada to date (.3226)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>PANA</td>
<td>Panama Service Indicated (.3227)</td>
<td>Not used</td>
<td>Not used</td>
<td>Panama from date (.3228)</td>
<td>Panama to date (.3229)</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>GULF</td>
<td>Persian Gulf Service (.32201)</td>
<td>Not used</td>
<td>Not used</td>
<td>Persian Gulf from date (.322011)</td>
<td>Persian Gulf to date (.322012)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>SOMA</td>
<td>Somalia Service Indicated (.322016)</td>
<td>Not used</td>
<td>Not used</td>
<td>Somalia from date (.322017)</td>
<td>Somalia to date (.322018)</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>YUGO</td>
<td>Yugoslavia Service Indicated (.322019)</td>
<td>Not used</td>
<td>Not used</td>
<td>Yugoslavia from date (.32202)</td>
<td>Yugoslavia to date (.322021)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>PH</td>
<td>Current PH Indicator (.531)</td>
<td>Current Purple Heart Status (.532)</td>
<td>Current Purple Heart Remarks (.533)</td>
<td>Not used</td>
<td>Not used</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>*OEIF</td>
<td>Location of Service (#2.3215,.01)</td>
<td>Entered by Site (#2.3215,.06)</td>
<td>Not used</td>
<td>From Date (#2.3215,.02)</td>
<td>To Date (#2.3215,.03)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>MH</td>
<td>Medal of Honor Indicator (ADR)</td>
<td>Not used</td>
<td>Not used</td>
<td>MOH Award Date</td>
<td>MOH Status Date</td>
<td>Not used</td>
</tr>
</tbody>
</table>

This table depicts the service indicators/qualifiers identified for the ZMH segment.

| Type | Indicator \#1                    | Indicator \#2    | Indicator \#3 | From Date  | To Date     | Service Component |
|----------|--------------------------------------|----------------------|-------------------|----------------|-----------------|-----------------------|
| SL       | Service branch                       | Service number       | Discharge type    | Entered        | Separated       | Service Component     |
| SNL      | Service branch                       | Service number       | Discharge type    | Entered        | Separated       | Service Component     |
| SNNL     | Service branch                       | Service number       | Discharge type    | Entered        | Separated       | Service Component     |
| MSD      | Service branch                       | Service number       | Discharge type    | Entered        | Separated       | Service Component     |
| POW      | Indicated – ‘Y’, ‘N’ or ‘U’          | Confinement Location | Not used          | From date      | To date         | Not used              |
| COMB     | Indicated – ‘Y’, ‘N’ or ‘U’          | Service Location     | Not used          | From date      | To date         | Not used              |
| VIET     | Indicated – ‘Y’, ‘N’ or ‘U’          | Not used             | Not used          | From date      | To date         | Not used              |
| LEBA     | Indicated – ‘Y’, ‘N’ or ‘U’          | Not used             | Not used          | From date      | To date         | Not used              |
| GREN     | Indicated – ‘Y’, ‘N’ or ‘U’          | Not used             | Not used          | From date      | To date         | Not used              |
| PANA     | Indicated – ‘Y’, ‘N’ or ‘U’          | Not used             | Not used          | From date      | To date         | Not used              |
| GULF     | Indicated – ‘Y’, ‘N’ or ‘U’          | Not used             | Not used          | From date      | To date         | Not used              |
| SOMA     | Indicated – ‘Y’, ‘N’ or ‘U’          | Not used             | Not used          | From date      | To date         | Not used              |
| YUGO     | Indicated – ‘Y’, ‘N’ or ‘U’          | Not used             | Not used          | From date      | To date         | Not used              |
| PH       | PH Indicator                         | PH Status            | Rejected Remarks  | Not used       | Not used        | Not used              |
| OEIF     | Location of Service                  | Entered By Site      | Not used          | From date      | To date         | Not used              |
| MH       | Medal of Honor Indicator – Y’ or ‘N’ | Not used             | Not used          | MOH Award Date | MOH Status Date | Not used              |

### VA-Specific Means Test Information Segment (ZMT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
ANNUAL MEANS TEST (#408.31) File Field or Expression</strong></th>
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
<td>*Set ID – Patient ID</td>
<td>Sequential Number (1= Means Test, 2 = Copay Test. 4 = LTC Copay Test Exemption Test)</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Means Test Date</td>
<td>DATE OF TEST Field (#.01)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA002</td>
<td>Means Test Status</td>
<td>STATUS Field (#.03)</td>
</tr>
<tr class="even">
<td>4</td>
<td>10</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Income</td>
<td>INCOME Field (#.04)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>10</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Net Worth</td>
<td>NET WORTH Field (#.05)</td>
</tr>
<tr class="even">
<td>6</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time of Adjudication</td>
<td>ADJUDICATION DATE/TIME Field (#.1)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Agreed to Pay Deductible</td>
<td>AGREED TO PAY DEDUCTIBLE Field (#.11)</td>
</tr>
<tr class="even">
<td>8</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Threshold A</td>
<td>THRESHOLD A Field (#.12)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>10</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Deductible Expenses</td>
<td>DEDUCTIBLE EXPENSES Field (#.15)</td>
</tr>
<tr class="even">
<td>10</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time MT Completed</td>
<td>DATE/TIME COMPLETED Field (#.07)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Previous Yr MT Threshold Flag</td>
<td>PREVIOUS YEARS THRESHOLD Field (#.16)</td>
</tr>
<tr class="even">
<td>12</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Total Dependents</td>
<td>TOTAL DEPENDENTS Field (#.18)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Hardship</td>
<td>HARDSHIP Field (#.2)</td>
</tr>
<tr class="even">
<td>14</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Hardship Review Date</td>
<td>HARDSHIP REVIEW DATE Field (#.21)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date Veteran Signed Test</td>
<td>DATE VETERAN SIGNED TEST Field (#.24)</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Declines to Give Income Info</td>
<td>DECLINES TO GIVE INCOME INFO Field (#.14)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA060</td>
<td>Type of Test</td>
<td><p>TYPE OF TEST Field (#.019)</p>
<p>1 = Means Test</p>
<p>2= Copay Test</p>
<p>4 = LTC Copay Exemption Test</p></td>
</tr>
<tr class="even">
<td>18</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>*Source of Test</td>
<td>SOURCE OF TEST Field (#.23) (1=VAMC, 2=IVM, 3=DCD, 4=Other Facility)</td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Primary Test?</td>
<td>PRIMARY INCOME TEST FOR YEAR? Field (#2)</td>
</tr>
<tr class="even">
<td>20</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date IVM Verif. MT Completed</td>
<td>DATE IVM VERIFIED MEANS TEST COMPLETED Field (#.25)</td>
</tr>
<tr class="odd">
<td>21</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Refused To Sign</td>
<td>REFUSED TO SIGN Field (#.26)</td>
</tr>
<tr class="even">
<td>22</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td>VA115</td>
<td>Site Conducting Test</td>
<td>SITE CONDUCTING TEST Field (#2.05)</td>
</tr>
<tr class="odd">
<td>23</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td>VA115</td>
<td>Hardship Review Site</td>
<td>SITE GRANTING HARDSHIP Field (#2.04)</td>
</tr>
<tr class="even">
<td>24</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Hardship Effective Date</td>
<td>HARDSHIP EFFECTIVE DATE Field (#2.01)</td>
</tr>
<tr class="odd">
<td>25</td>
<td></td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Last Edited</td>
<td>DATE/TIME LAST EDITED Field (#2.02)</td>
</tr>
<tr class="even">
<td>26</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA 02</td>
<td>Test determined Status</td>
<td>TEST DETERMINED STATUS Field (#2.03)</td>
</tr>
<tr class="odd">
<td>27</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA0051</td>
<td>*Means Test Signature Indicator</td>
<td>MEANS TEST SIGNED? Field (#.29)</td>
</tr>
<tr class="even">
<td>28</td>
<td>8</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>GMT Threshold</td>
<td>GMT THRESHOLD Field (#.27)</td>
</tr>
<tr class="odd">
<td>29</td>
<td>80</td>
<td>FT</td>
<td></td>
<td></td>
<td></td>
<td>Hardship Reason</td>
<td>HARDSHIP REASON Field (#2.09)</td>
</tr>
<tr class="even">
<td>30</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Means Test Version</td>
<td><p>MEANS TEST VERSION (#2.11)</p>
<p>0 = Before Feb 2005 format</p>
<p>1 = Feb 2005</p>
<p>2 = TBD (in case there is a need to expand into the future)</p></td>
</tr>
<tr class="odd">
<td>31</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>BT FINANCIAL INDICATOR</td>
<td>BT FINANCIAL INDICATOR (#4)</td>
</tr>
<tr class="even">
<td>32</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>HARDSHIP EXPIRATION DATE</td>
<td>HARDSHIP EXPIRATION DATE (#2.13) (Precise)</td>
</tr>
<tr class="odd">
<td colspan="8"><p>Notes:</p>
<ul>
<li><p>Deletion of a Test: SEQ 1 indicates the type of test to delete.</p></li>
</ul>
<blockquote>
<p>SEQ 2 will be used to indicate which income year test to delete. The income year is the year prior to the date of the means test.</p>
<p>SEQ 3 = HLQ will indicate that the test should be deleted.</p>
</blockquote>
<p> Deletion of a Hardship Determination:</p>
<blockquote>
<p>SEQ 24 = HLQ will indicate that the hardship determination should be deleted.</p>
<p>SEQ 2 will be used to indicate for which income year to delete the hardship determination . The income year is the year prior to the date of the means test.</p>
</blockquote>
<p>* Means Test Signature Indicator</p>
<blockquote>
<p>SEQ 27 was added by Patch IVMB*2*600 for the Implement Signed Means Test Strategy project. VAMCs receive and store data from SEQ 27, but do not include this sequence in transmissions to the HEC. VAMCs send means test signature images to the HEC via FAX. HEC staff processes those images using commercial software with updates to the HEC database via custom remote procedure calls (RPCs).</p>
</blockquote></td>
</tr>
</tbody>
</table>

### ### VA-Specific Patient Information Segment (ZPD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID – Patient ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>60</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Remarks</td>
<td>REMARKS Field (#.091)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Place of Birth City</td>
<td>PLACE OF BIRTH CITY Field (#.092)</td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Place of Birth State</td>
<td>PLACE OF BIRTH STATE Field (#.093) (Abbreviation Only)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA002</td>
<td>Current Means Test Status</td>
<td>CURRENT MEANS TEST STATUS Field (#.14)</td>
</tr>
<tr class="even">
<td>6</td>
<td>35</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Father’s Name</td>
<td>FATHER’S NAME Field (#.2401)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>35</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Mother’s Name</td>
<td>MOTHER’S NAME Field (#.2402)</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Rated Incompetent</td>
<td>RATED INCOMPETENT Field (#.293)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date of Death</td>
<td>DATE OF DEATH Field (#.351)</td>
</tr>
<tr class="even">
<td>10</td>
<td>48</td>
<td>PN</td>
<td></td>
<td></td>
<td></td>
<td>Collateral Sponsor</td>
<td>COLLATERAL SPONSOR Field (#.3601)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Active Health Insurance?</td>
<td>Active Health Insurance? (Computed)</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Eligible For Medicaid?</td>
<td>ELIGIBLE FOR MEDICAID? Field (#.381)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date Medicaid Last Asked</td>
<td>DATE MEDICAID LAST ASKED Field (#.382)</td>
</tr>
<tr class="even">
<td>14</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA007</td>
<td>Race</td>
<td>RACE Field (#.06)</td>
</tr>
<tr class="odd">
<td>15</td>
<td>3</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA008</td>
<td>Religion</td>
<td>RELIGION Field (#.08)</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Homeless Indicator</td>
<td>Homeless Indicator (Computed)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>POW Status Indicated?</td>
<td>POW STATUS INDICATED? Field (#.525) (Y = Yes; N = No; U = Unknown)</td>
</tr>
<tr class="even">
<td>18</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA012</td>
<td>Type of Insurance</td>
<td>TYPE OF INSURANCE (Computed)</td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA014</td>
<td>Medication Copayment Exemption Status</td>
<td>MEDICATION COPAY EXEMPTION STATUS (Computed) (#354) (.04)</td>
</tr>
<tr class="even">
<td>20</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td>POW Confinement Location</td>
<td>Not used at this time; sent in ZMH segment</td>
</tr>
<tr class="odd">
<td>21</td>
<td>2</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Primary Care Team (as defined in PCMM)</td>
<td>PRIMARY CARE TEAM (File# 404.51)</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>GI Insurance Policy</td>
<td>GIN INSURANCE POLICY? Field (#.36265)</td>
</tr>
<tr class="odd">
<td>23</td>
<td>6</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Amount of GI Insurance</td>
<td>AMOUNT OF GI INSURANCE Field (#.3626)</td>
</tr>
<tr class="even">
<td>24</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Most Recent Date of Care</td>
<td>MOST RECENT DATE OF CARE Field (#1010.151)</td>
</tr>
<tr class="odd">
<td>25</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Most Recent Location of Care</td>
<td>MOST RECENT LOCATION OF CARE Field (#1010.152)</td>
</tr>
<tr class="even">
<td>26</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>2<sup>nd</sup> Most Recent Date of Care</td>
<td>2<sup>nd</sup> MOST RECENT DATE OF CARE Field (#1010.153)</td>
</tr>
<tr class="odd">
<td>27</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>2<sup>nd</sup> Most Recent Location of Care</td>
<td>2<sup>nd</sup> MOST RECENT LOCATION OF CARE Field (#1010.154)</td>
</tr>
<tr class="even">
<td>28</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date Ruled Incompetent (Civil)</td>
<td>DATE RULED INCOMPETENT (CIVIL) Field (#.292)</td>
</tr>
<tr class="odd">
<td>29</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date Ruled Incompetent (VA)</td>
<td>DATE RULED INCOMPETENT (VA) Field (#.291)</td>
</tr>
<tr class="even">
<td>30</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Spinal Cord Injury</td>
<td>SPINAL CORD INJURY Field (#57.4) Values: 1:PARAPLEGIA-TRAUMATIC 2:QUADRIPLEGIA- TRAUMATIC 3: PARAPLEGIA-NONTRAUMATIC 4: QUADRIPLEGIA- NONTRAUMATIC X:NOT APPLICABLE</td>
</tr>
<tr class="odd">
<td>31</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Source of Notification</td>
<td>SOURCE OF NOTIFICATION FOR DATE OF DEATH Field (#.353) Values: 1:INPATIENT AT VAMC 2:NON-VA MEDICAL FACILITY 3:DEATH CERTIFICATE ON FILE 4:VBA 5:VA INSURANCE 6:SSA 7:NCA 8:NEXT OF KIN/FAMILY/FRIEND 9: OTHER</td>
</tr>
<tr class="even">
<td>32</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Date of Death Last Updated</td>
<td>DATE OF LAST ENTRY OR UPDATE Field (#.354)</td>
</tr>
<tr class="odd">
<td>33</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA048</td>
<td>Filipino Veteran Proof</td>
<td>FILIPINO VETERAN PROOF Field (#3214). Values: PP – US PASSPORT, BC – US BIRTH CERTIFICATE; BA – REPORT OF BIRTH ABROAD OF US CITIZEN, NA – VERIFICATION OF NATURALIZATION, PR – VERIFICATION OF PERMANENT RESIDENCY, VA – VA COMPENSATION AT FULL DOLLAR RATE, NO – NO PROOF.</td>
</tr>
<tr class="even">
<td>34</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Pseudo SSN Reason</td>
<td>PSEUDO SSN REASON Field (#.0906). Values: R – REFUSED TO PROVIDE, S – SSN UNKNOWN/FOLLOW-UP REQUIRED, N – NO SSN ASSIGNED</td>
</tr>
<tr class="odd">
<td>35</td>
<td>15</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA018</td>
<td>Agency/Allied Country</td>
<td>AGENCY/ALLIED COUNTRY Field (#.309). Pointer to OTHER FEDERAL AGENCY File (#35)</td>
</tr>
<tr class="even">
<td>36-39</td>
<td>TBD</td>
<td>TBD</td>
<td>TBD</td>
<td>TBD</td>
<td>TBD</td>
<td>TBD</td>
<td>TBD</td>
</tr>
<tr class="odd">
<td>40</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Emergency Response Indicator</td>
<td><p>EMERGENCY RESPONSE INDICATOR Field (#.181) Values:</p>
<p>P – PANDEMIC</p></td>
</tr>
<tr class="even">
<td>41</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td>VA001</td>
<td>VOA Attachments Indicator</td>
<td>This is for VOA only and it means that the applicant uploaded an attachment.<br />
Currently this field is set to blank.</td>
</tr>
<tr class="odd">
<td>42</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Indian Urban Indian?</td>
<td><p>INDIAN SELF IDENTIFICATION (.571)</p>
<p>Values:</p>
<p>1 - Yes</p>
<p>0 – No</p>
<p>Blank - Unknown</p></td>
</tr>
<tr class="even">
<td>43</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Indian Attestation Date</td>
<td><p>INDIAN ATTESTATION DATE (.573)</p>
<p>Format: YYYYMMDD</p>
<p>Required if INDIAN SELF IDENTIFICATION = Yes or No</p></td>
</tr>
<tr class="odd">
<td>44</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Start Date</td>
<td><p>INDIAN START DATE (.572)</p>
<p>Format: YYYYMMDD</p></td>
</tr>
<tr class="even">
<td>45</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>End Date</td>
<td><p>INDIAN END DATE (.574)</p>
<p>Format: YYYYMMDD</p></td>
</tr>
<tr class="odd">
<td>46</td>
<td>3</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Preferred Language</td>
<td>THREE LETTER CODE Field (#.03) of LANGUAGE File (#.85)</td>
</tr>
<tr class="even">
<td>47</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Preferred Language Update Date/Time</td>
<td>LANGUAGE DATE/TIME (Multiple 2.07 Field .01)</td>
</tr>
</tbody>
</table>

### VA-Specific Rated Disabilities Segment (ZRD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2.3721) Sub-File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Disability Condition *(See below.)</td>
<td>RATED DISABILITIES (VA) Field (#.01)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Disability %</td>
<td>DISABILITY % Field (#2)</td>
</tr>
<tr class="even">
<td>4</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Service Connected Rated Disability</td>
<td>SERVICE CONNECTED Field (#3)</td>
</tr>
</tbody>
</table>

DISABILITY CONDITION has the coded element data type, which is one of the composite data types. The ‘~’ is always used within the IVM and Enrollment packages as the component separator. The general format for the coded element data type, from the 2.3 version of the HL7 standard, is:

\<identifier (ST)\>~\<text (ST)\>~\<name of coding system (ST)\>~\<alternate identifier (ST\>~

The actual format for the DISABILITY CONDITION is:

\<4-digit DX CODE from the Disability Condition File (#31)\>~\<45-character NAME Field from the Disability Condition File\>

If the DISABILITY CONDITION Field is included in the segment then both of its components are required.

Here is an example of the ZRD segment: ZRD^1^5001~BONE DISEASE^30^1

### VA-Specific Service Period Segment (ZSP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>IS</td>
<td>R</td>
<td></td>
<td>VA001</td>
<td>Service Connected?</td>
<td>SERVICE CONNECTED? Field (#.301)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Service Connected Percentage</td>
<td>SERVICE CONNECTED PERCENTAGE Field (#.302)</td>
</tr>
<tr class="even">
<td>4</td>
<td>2</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA011</td>
<td>Period of Service</td>
<td>PERIOD OF SERVICE Field (#.323)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Vietnam Service Indicated?</td>
<td>VIETNAM SERVICE INDICATED? Field (#.32101)</td>
</tr>
<tr class="even">
<td>6</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>P&amp;T</td>
<td>P&amp;T Field (#.304)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Unemployable</td>
<td>UNEMPLOYABLE Field (#.305)</td>
</tr>
<tr class="even">
<td>8</td>
<td>19</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>SC Award Date</td>
<td>SC AWARD DATE Field (#.3012)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Service Verification Date</td>
<td>SERVICE VERIFICATION DATE (#.322)</td>
</tr>
<tr class="even">
<td>10</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>P&amp;T Effective Date</td>
<td>P&amp;T EFFECTIVE DATE (#.3013)</td>
</tr>
<tr class="odd">
<td>11</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Combined SC Percent Effective Date</td>
<td>EFF. DATE COMBINED SC% EVAL. (#.3014)</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Eligible For Class II Dental</td>
<td>CLASS II DENTAL INDICATOR (#.3858)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Class II Dental Application Due Before Date</td>
<td>DENTAL APPL DUE BEFORE DATE (#.3859)</td>
</tr>
</tbody>
</table>

### VA-Specific Temporary Address Segment (ZTA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>Set ID – Patient ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td>Temporary Address?</td>
<td>TEMPORARY ADDRESS ENTER/EDIT? Field (#.12105)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Temporary Address Start</td>
<td>TEMPORARY ADDRESS START DATE Field (#.1217)</td>
</tr>
<tr class="even">
<td>4</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>Temporary Address End</td>
<td>TEMPORARY ADDRESS END DATE Field (#.1218)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>106</td>
<td>XAD</td>
<td></td>
<td></td>
<td></td>
<td>Temporary Address</td>
<td>TEMPORARY ADDRESS Fields (For USA: #.1211-.1215, .12111, .12112, .1223 For Foreign: .1211-.1213, .12111 .1221-.1223)</td>
</tr>
<tr class="even">
<td>6</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Temporary Address County</td>
<td>TEMPORARY ADDRESS COUNTY Field (#.12111)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>40</td>
<td>TN</td>
<td></td>
<td></td>
<td></td>
<td>Temporary Address Phone</td>
<td>TEMPORARY PHONE NUMBER Field (#.1219)</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Temporary Address Date/Time Last Updated</td>
<td>TEMPORARY ADDRESS CHANGE DT/TM (.12113)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>10</td>
<td>NM</td>
<td></td>
<td></td>
<td>0115</td>
<td>Temporary Address Site of Change</td>
<td>TEMPORARY ADDRESS CHANGE SITE (#.12114)</td>
</tr>
<tr class="even">
<td>10</td>
<td>40</td>
<td>XTN</td>
<td></td>
<td></td>
<td></td>
<td>Temporary Address International Phone</td>
<td><p>TEMPORARY COUNTRY CODE (#.12116) TEMPORARY EXTENSION (#.12117) .121;17 NUMBER</p>
<p>TEMPORARY PHONE NUMBER (#.1219)</p></td>
</tr>
</tbody>
</table>

### VA Specific Temporary Eligibility Segment (ZTE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 32%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL #</th>
<th>ELEMENT NAME</th>
<th>VISTA<br />
File# 33 – OTH ELIGIBILITY PATIENT</th>
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
<td>SET ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>DATE REQUEST SUBMITTED</td>
<td><p>Date of request submission to CMO</p>
<p>Pending  - file 33, field .03</p>
<p>Approved – sub-file 33.11, field .03</p>
<p>Denied – sub-file 33.03, field .02</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>19</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>ORIGINAL REQUEST ENTERED DATE/TIME</td>
<td>System timestamp when request is originally entered</td>
</tr>
<tr class="even">
<td>4</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>AUTHORIZATION STATUS</td>
<td><p>AUTHORIZATION STATUS</p>
<p>A = Approved</p>
<p>P = Pending</p>
<p>D = Denied</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>19</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>DATE/TIME REQUEST UPDATED</td>
<td><p>Timestamp of last record modification</p>
<p>Pending  - file 33, field .05</p>
<p>Approved – sub-file 33.11, field .06</p>
<p>Denied – sub-file 33.03, field .05</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>60</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>REQUEST ENTERED BY</td>
<td><p>Name of the user who modified the record</p>
<p>Pending  - file 33, field .04</p>
<p>Approved – sub-file 33.11, field .05</p>
<p>Denied – sub-file 33.03, field .04</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>10</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>VA0115</td>
<td>SITE OF CHANGE</td>
<td><p>Facility (station number) that modified the record</p>
<p>Pending  - file 33, field .06</p>
<p>Approved – sub-file 33.11, field .08</p>
<p>Denied – sub-file 33.03, field .06</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>4</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>365 DAY PERIOD NUMBER</td>
<td><p>Sequential number of 365 day period. Only applicable to approved requests, blank for pending and denied requests.</p>
<p>Approved – sub-file 33.01, field .01</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>4</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>90 DAY PERIOD NUMBER</td>
<td><p>Sequential number of 90 day period. Only applicable to approved requests, blank for pending and denied requests.</p>
<p>Approved – sub-file 33.11, field .01</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>AUTHORIZATION DATE</td>
<td><p>Date when authorization was received from CMO. Only applicable to approved requests, blank for pending and denied requests.</p>
<p>Approved – sub-file 33.11, field .04</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>60</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>AUTHORIZED BY</td>
<td><p>Name of the person who approved the request. Only applicable to approved requests, blank for pending and denied requests.</p>
<p>Approved – sub-file 33.11, field .07</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>START DATE</td>
<td><p>Start date of the approved 90 day period. Only applicable to approved requests, blank for pending and denied requests.</p>
<p>Approved – sub-file 33.11, field .02</p></td>
</tr>
<tr class="odd">
<td>13</td>
<td>60</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>AUTHORIZATION COMMENT</td>
<td><p>Comment / reason for request denial. Only applicable to denied requests, blank for approved and pending requests.</p>
<p>Denied – sub-file 33.03, field .03</p></td>
</tr>
</tbody>
</table>

### ZUD – VA Specific VistA User Data Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL #</strong></th>
<th><strong>Element Name</strong></th>
<th><strong>V<em>IST</em>A Element Name<br />
PATIENT (#2) File Field or Expression</strong></th>
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
<td>SET ID</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>5</td>
<td>IS</td>
<td>R</td>
<td></td>
<td></td>
<td>CONTACT INFO TYPE</td>
<td><p>Seq 2 will be populated with one of the following codes to identify the type of information:</p>
<p>SAD = Street Address Change<br />
CAD = Confidential Address Change<br />
CPH = Cell Phone Number Change<br />
PNO = Pager Number Change<br />
EAD = E-Mail Address Change<br />
PHH = Home Phone Number Change<br />
RAD=Residential Address Change<br />
PHB=Business Phone Change<br />
PHC=Confidential Phone Change</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>19</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>LAST UPDATED DATE/TIME</td>
<td>UPDATE DATE/TIME (#) Date/time the contact information was updated</td>
</tr>
<tr class="even">
<td>4</td>
<td>35</td>
<td>XPN</td>
<td></td>
<td></td>
<td></td>
<td><p>UPDATED BY</p>
<p>Format:</p>
<p>LAST~FIRST~MIDDLE~SUFFIX</p></td>
<td>VistA User Name (200.01)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>9</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>USER NUMBER</td>
<td>VistA User Number (200.001)</td>
</tr>
</tbody>
</table>

### Batch Header Segment (BHS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Description</strong></th>
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
<p>Component = <strong>~</strong> (tilde)</p>
<p>Repeat = <strong>|</strong> (bar)</p>
<p>Escape = <strong>\</strong> (back slash)</p>
<p>Subcomponent = <strong>&amp;</strong> (ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Application</td>
<td><p>When originating from facility:</p>
<p><strong>IVM</strong></p>
<p>When originating from HEC:</p>
<p><strong>IVM CENTER</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Facility</td>
<td><p>When originating from facility:</p>
<p><strong>Station’s facility number</strong></p>
<p>When originating from HEC:</p>
<p><strong>724</strong></p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Application</td>
<td><p>When originating from facility:</p>
<p><strong>IVM CENTER</strong></p>
<p>When originating from HEC:</p>
<p><strong>IVM</strong></p></td>
</tr>
<tr class="even">
<td>6</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Facility</td>
<td><p>When originating from facility:</p>
<p><strong>724</strong></p>
<p>When originating from HEC:</p>
<p><strong>Station’s facility number</strong></p></td>
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
<td>Batch Name / ID / Type</td>
<td><p>The following fields in File #101:</p>
<p>#770.4</p>
<p>#770.6</p>
<p>#770.8</p>
<p>#770.9</p>
<p>#770.95</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>80</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Comment</td>
<td><p>Only used for acknowledgments</p>
<p>ERROR MESSAGE Field (#22) of File #772</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Control ID</td>
<td>MESSAGE ID Field (#2) of File #772</td>
</tr>
<tr class="even">
<td>12</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Reference Batch Control ID</td>
<td>MESSAGE ID Field (#2) of File #772</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Name/ID/Type</td>
<td><p>4 Components:</p>
<p>Component 1: Batch Name (Not used)</p>
<p>Component 2: Processing ID</p>
<p>Component 3: Message Type</p>
<p>Component 4: Version ID</p>
<p><em>These 4 components must be separated by the HL7 component separator. The processing ID, message type, and version ID correspond to fields of the same name in the MSH segment</em></p></td>
</tr>
<tr class="even">
<td>10</td>
<td>80</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Comment</td>
<td><p>2 Components:</p>
<p>Component 1: <em>Refer to Table 0008</em></p>
<p>Component 2: Text Message</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Control ID</td>
<td>Automatically generated by <strong>V</strong><em>IST</em><strong>A</strong> HL7 Package</td>
</tr>
<tr class="even">
<td>12</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Reference Batch Control ID</td>
<td>Batch Control ID of batch message being acknowledged</td>
</tr>
</tbody>
</table>

### Batch Trailer Segment (BTS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | Element Name    | V*IST*A Description                     |
|---------|---------|--------|---------|----------|----------|---------------------|---------------------------------------------|
| 1       | 10      | ST     |         |          |          | Batch Message Count | Number of messages within the batch message |
| 2       | 80      | ST     |         |          |          | Batch Comment       | Not used at this time                       |
| 3       | 100     | CM     |         | Y        |          | Batch Totals        | Not used at this time                       |

### Message Header Segment (MSH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Description</strong></th>
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
<td>Field Separator</td>
<td>Recommended value is <strong>^</strong> (caret) (File #771, Field #100)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = <strong>~</strong> (tilde)</p>
<p>Repeat = <strong>|</strong> (bar)</p>
<p>Escape = <strong>\</strong> (back slash)</p>
<p>Subcomponent = <strong>&amp;</strong> (ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Sending application (File #771, Field #.01)</td>
</tr>
<tr class="even">
<td>4</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending facility (File #771, Field #3)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Receiving application (File #771, Field #.01)</td>
</tr>
<tr class="even">
<td>6</td>
<td>180</td>
<td>HD</td>
<td>O</td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving facility (File #771 Field #3)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Date/Time of Message</td>
<td>Date and time message was created</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>2 Components:</p>
<p>Component 1: Refer to Table 0076 in Appendix C</p>
<p>Component 2 : Message Event Type Code</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by <strong>V</strong><em>IST</em><strong>A</strong> HL7 Package</td>
</tr>
<tr class="odd">
<td>11</td>
<td>3</td>
<td>PT</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td><strong>P</strong> (PRODUCTION) (File #101 Field #770.6)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version Id</td>
<td><strong>2.3.1</strong> (HL7 VERSION 2.3.1) (File #101 Field #770.95)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>AL – Always used (File #101 Field #770.8)</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL – Always used (File #101 Field #770.9)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td></td>
<td>Country Code</td>
<td>US (File #771 Field #7)</td>
</tr>
<tr class="even">
<td>18</td>
<td>6</td>
<td>ID</td>
<td>O</td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Principal Language Of Message</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>20</td>
<td>20</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0356</td>
<td>Alternate Character Set Handling Scheme</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Station #</td>
</tr>
<tr class="even">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time of Message</td>
<td>Date and time message was created</td>
</tr>
<tr class="odd">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td>0076</td>
<td>Message Type</td>
<td>MFN~M0F</td>
</tr>
<tr class="odd">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by <strong>V</strong><em>IST</em><strong>A</strong> HL7 Package</td>
</tr>
<tr class="even">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td><strong>P</strong> (Production)</td>
</tr>
<tr class="odd">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td><strong>2.3</strong> (Version 2.3)</td>
</tr>
<tr class="even">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used at this time</td>
</tr>
<tr class="odd">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used at this time</td>
</tr>
<tr class="even">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="odd">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="even">
<td>17</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>US</td>
</tr>
<tr class="odd">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used at this time</td>
</tr>
<tr class="even">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used at this time</td>
</tr>
</tbody>
</table>

### Message Acknowledgment Segment (MSA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | Element Name            | V*IST*A Description                          |
|---------|---------|--------|---------|----------|----------|-----------------------------|--------------------------------------------------|
| 1       | 2       | ID     | R       |          | 0008     | Acknowledgment Code         | Refer to Table 0008 in Appendix C                |
| 2       | 20      | ST     | R       |          |          | Message Control ID          | Message Control ID of message being acknowledged |
| 3       | 80      | ST     |         |          |          | Text Message                | Error text denoting why the message was rejected |
| 4       | 15      | NM     |         |          |          | Expected Sequence Number    | Not used                                         |
| 5       | 1       | ID     |         |          | 0102     | Delayed Acknowledgment Type | Not used                                         |
| 6       | 100     | CE     |         |          |          | Error Condition             | Not used                                         |

### Master File Identification Segment (MFI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | Element Name                   | V*IST*A Description                          |
|---------|---------|--------|---------|----------|----------|------------------------------------|--------------------------------------------------|
| 1       | 60      | CE     | R       |          | 0175     | Master File Identifier             | ‘5P12~POSTAL CODE~VHA’ or ‘5P13~COUNTY CODE~VHA’ |
| 2       | 180     | HD     | O       |          |          | Master File Application Identifier | Not used                                         |
| 3       | 3       | ID     | R       |          | 0178     | File-Level Event Code              | ‘UPD’                                            |
| 4       | 26      | TS     | O       |          |          | Entered Date/Time                  | Not used                                         |
| 5       | 26      | TS     | O       |          |          | Effective Date/Time                | Not used                                         |
| 6       | 2       | ID     | R       |          | 0179     | Response Level Code                | ‘NE’                                             |

### Master File Entry Segment (MFE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | Element Name        | V*IST*A Description  |
|---------|---------|--------|---------|----------|----------|-------------------------|--------------------------|
| 1       | 3       | ID     | R       |          | 0180     | Record-Level Event Code | ‘MAD’ or ‘MUP’           |
| 2       | 20      | ST     | C       |          |          | MFN Control ID          | Not used                 |
| 3       | 26      | TS     |         |          |          | Effective Date/Time     | Effective Date/Time      |
| 4       | 60      | CE     | R       | Y        |          | Primary Key Value       | Same as LOC Sequence \#1 |

### Location Identification Segment (LOC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 35%" />
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
<th><strong>V<em>IST</em>A Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>200</td>
<td>PL</td>
<td>R</td>
<td></td>
<td></td>
<td>Primary Key Value – LOC</td>
<td><p><strong>Postal Code:</strong> CODE Field (#.01) of the POSTAL CODE File (#5.12). This data was obtained from the U. S. Postal Service, but could include other external sources in the future as postal codes belonging to other countries are introduced to the system.</p>
<p><strong>County Code:</strong> 5-digit FIPS CODE Field (#.01) of the COUNTY CODE File (#5.13)</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>48</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Location Description</td>
<td><p><strong>Postal Code:</strong> Postal Code Master File Update</p>
<p><strong>County Code:</strong> County Code Master File Update</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>2</td>
<td>IS</td>
<td>R</td>
<td></td>
<td></td>
<td>Location Type – LOC</td>
<td>L</td>
</tr>
<tr class="even">
<td>4</td>
<td>90</td>
<td>XON</td>
<td>O</td>
<td></td>
<td></td>
<td>Organization Name – LOC</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>106</td>
<td>XAD</td>
<td>O</td>
<td></td>
<td></td>
<td>Location Address</td>
<td><p><strong>Postal Code:</strong> POSTAL CODE File (#5.12)</p>
<p><strong>County Code:</strong> COUNTY CODE File (#5.12)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>40</td>
<td>XTN</td>
<td>O</td>
<td></td>
<td></td>
<td>Location Phone</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>60</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>License Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>3</td>
<td>IS</td>
<td>O</td>
<td></td>
<td></td>
<td>Location Equipment</td>
<td>Not Used</td>
</tr>
</tbody>
</table>

## # Appendix C – Supported/User-Defined Standard HL7 Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table 0001 – Sex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| F        | FEMALE          |
| M        | MALE            |
| O        | OTHER           |
| U        | UNKNOWN         |

## Table 0002 – Marital Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| A        | SEPARATED       |
| D        | DIVORCED        |
| M        | MARRIED         |
| S        | SINGLE          |
| W        | WIDOWED         |

## Table 0003 – Event Type Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code    | Description              |
|-------------|------------------------------|
| M05 MFN/MFK | Patient location master file |

## Table 0005 – Race

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                           |
|----------|-------------------------------------------|
| 1002-5   | American Indian or Alaska Native          |
| 2028-9   | Asian                                     |
| 2054-5   | Black or African American                 |
| 2076-8   | Native Hawaiian or Other Pacific Islander |
| 2106-3   | White                                     |
| 2131-1   | Other Race                                |

## Table 0006 – Religion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                   |
|----------|---------------------------------------------------|
| ABC      | Christian: American Baptist Church                |
| AGN      | Agnostic                                          |
| AME      | Christian: African Methodist Episcopal Zion       |
| AMT      | Christian: African Methodist Episcopal            |
| ANG      | Christian: Anglican                               |
| AOG      | Christian: Assembly of God                        |
| ATH      | Atheist                                           |
| BAH      | Baha’i                                            |
| BAP      | Christian: Baptist                                |
| BMA      | Buddhist: Mahayana                                |
| BOT      | Buddhist: Other                                   |
| BTA      | Buddhist: Tantrayana                              |
| BTH      | Buddhist: Theravada                               |
| BUD      | Buddhist                                          |
| CAT      | Christian: Roman Catholic                         |
| CFR      | Chinese Folk Religionist                          |
| CHR      | Christian                                         |
| CHS      | Christian: Christian Science                      |
| CMA      | Christian: Christian Missionary Alliance          |
| CNF      | Confucian                                         |
| COC      | Christian: Church of Christ                       |
| COG      | Christian: Church of God                          |
| COI      | Christian: Church of God in Christ                |
| COL      | Christian: Congregational                         |
| COM      | Christian: Community                              |
| COP      | Christian: Other Pentecostal                      |
| COT      | Christian: Other                                  |
| CRR      | Christian: Christian Reformed                     |
| EOT      | Christian: Eastern Orthodox                       |
| EPI      | Christian: Episcopalian                           |
| ERL      | Ethnic Religionist                                |
| EVC      | Christian: Evangelical Church                     |
| FRQ      | Christian: Friends                                |
| FWB      | Christian: Free Will Baptist                      |
| GRE      | Christian: Greek Orthodox                         |
| HIN      | Hindu                                             |
| HOT      | Hindu: Other                                      |
| HSH      | Hindu: Shaivites                                  |
| HVA      | Hindu: Vaishnavites                               |
| JAI      | Jain                                              |
| JCO      | Jewish: Conservative                              |
| JEW      | Jewish                                            |
| JOR      | Jewish: Orthodox                                  |
| JOT      | Jewish: Other                                     |
| JRC      | Jewish: Reconstructionist                         |
| JRF      | Jewish: Reform                                    |
| JRN      | Jewish: Renewal                                   |
| JWN      | Christian: Jehovah’s Witness                      |
| LMS      | Christian: Lutheran Missouri Synod                |
| LUT      | Christian: Lutheran                               |
| MEN      | Christian: Mennonite                              |
| MET      | Christian: Methodist                              |
| MOM      | Christian: Latter-day Saints                      |
| MOS      | Muslim                                            |
| MOT      | Muslim: Other                                     |
| MSH      | Muslim: Shiite                                    |
| MSU      | Muslim: Sunni                                     |
| NAM      | Native American                                   |
| NAZ      | Christian: Church of the Nazarene                 |
| NOE      | Nonreligious                                      |
| NRL      | New Religionist                                   |
| ORT      | Christian: Orthodox                               |
| OTH      | Other                                             |
| PEN      | Christian: Pentecostal                            |
| PRC      | Christian: Other Protestant                       |
| PRE      | Christian: Presbyterian                           |
| PRO      | Christian: Protestant                             |
| QUA      | Christian: Friends                                |
| REC      | Christian: Reformed Church                        |
| REO      | Christian: Reorganized Church of Jesus Christ-LDS |
| SAA      | Christian: Salvation Army                         |
| SEV      | Christian: Seventh Day Adventist                  |
| SHN      | Shintoist                                         |
| SIK      | Sikh                                              |
| SOU      | Christian: Southern Baptist                       |
| SPI      | Spiritist                                         |
| UCC      | Christian: United Church of Christ                |
| UMD      | Christian: United Methodist                       |
| UNI      | Christian: Unitarian                              |
| UNU      | Christian: Unitarian Universalist                 |
| VAR      | Unknown                                           |
| WES      | Christian: Wesleyan                               |
| WMC      | Christian: Wesleyan Methodist                     |

## Table 0008 – Acknowledgment Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AA</td>
<td>Original Mode: Application Accept<br />
Enhanced Mode: Application Acknowledgment: Accept</td>
</tr>
<tr class="even">
<td>AE</td>
<td>Original Mode: Application Error<br />
Enhanced Mode: Application Acknowledgment: Error</td>
</tr>
<tr class="odd">
<td>AR</td>
<td>Original Mode: Application Reject<br />
Enhanced Mode: Application Acknowledgment: Reject</td>
</tr>
<tr class="even">
<td>CA</td>
<td>Enhanced Mode: Accept Acknowledgment: Commit Accept</td>
</tr>
<tr class="odd">
<td>CE</td>
<td>Enhanced Mode: Accept Acknowledgment: Commit Error</td>
</tr>
<tr class="even">
<td>CR</td>
<td>Enhanced Mode: Accept Acknowledgment: Commit Reject</td>
</tr>
</tbody>
</table>

## Table 0017 – Transaction Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| AJ       | Adjustment      |
| CD       | Credit          |
| CG       | Charge          |
| CO       | Co-payment      |
| PY       | Payment         |

## Table 0018 – Patient Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description       |
|----------|-----------------------|
| 00       | Surgical              |
| 10       | Medical               |
| 60       | Home Nursing Service  |
| 85       | Psychiatric Contract  |
| 86       | Psychiatric           |
| 95       | Neurological Contract |
| 96       | Neurological          |

## Table 0024 – Fee Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                         |
|----------|-----------------------------------------|
| 1        | Charge exceeds maximum payable          |
| 2        | Math error, 3-Not entitled to treatment |
| 4        | Other, 5-Previously Paid                |
| 6        | Exceed monthly dollar limitation        |
| 7        | Physician’s signature missing           |
| 8        | Patient’s signature missing             |
| 9        | Medication not emergent                 |
| A        | Pharmacist’s certification missing      |
| B        | Pharmacist’s signature missing          |
| C        | Required drug information missing       |
| D        | Item not on payable list                |
| E        | Veteran information missing             |
| F        | Personal items/Private Room             |
| G        | Vet refused transfer                    |
| H        | For recurring or refill medication      |
| I        | Payment made for Generic drug           |
| J        | Mill Bill Authority                     |

## Table 0048 – What Subject Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                              |
|----------|----------------------------------------------------------------------------------------------|
| ADV      | Advice/diagnosis                                                                             |
| ANU      | Nursing unit lookup (returns patients in beds, excluding empty beds)                         |
| APA      | Account number query, return matching visit                                                  |
| APM      | Medical record number query, returns visits for a medical record number                      |
| APN      | Patient name lookup                                                                          |
| APP      | Physician lookup                                                                             |
| ARN      | Nursing unit lookup (returns patients in beds, including empty beds)                         |
| CAN      | Cancel. Used to cancel a query                                                               |
| DEM      | Demographics                                                                                 |
| FIN      | Financial                                                                                    |
| GID      | Generate new identifier                                                                      |
| GOL      | Goals                                                                                        |
| MRI      | Most recent inpatient                                                                        |
| MRO      | Most recent outpatient                                                                       |
| NCK      | Network clock                                                                                |
| NSC      | Network status change                                                                        |
| NST      | Network statistic                                                                            |
| ORD      | Order                                                                                        |
| OTH      | Other                                                                                        |
| PRB      | Problems                                                                                     |
| PRO      | Procedure                                                                                    |
| RAR      | Pharmacy administration information                                                          |
| RDR      | Pharmacy dispense information                                                                |
| RER      | Pharmacy encoded order information                                                           |
| RES      | Result                                                                                       |
| RGR      | Pharmacy give information                                                                    |
| ROR      | Pharmacy prescription information                                                            |
| SAL      | All schedule related information, including open slots, booked slots, blocked slots          |
| SBK      | Booked slots on the identified schedule                                                      |
| SBL      | Blocked slots on the identified schedule                                                     |
| SOF      | First open slot on the identified schedule after the start date/time                         |
| SOP      | Open slots on the identified schedule between the begin and end of the start date/time range |
| SSA      | Time slots available for a single appointment                                                |
| SSR      | Time slots available for a recurring appointment                                             |
| STA      | Status                                                                                       |
| VXI      | Vaccine Information                                                                          |
| XID      | Get cross-referenced identifiers                                                             |

## Table 0049 – Department Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description     |
|----------|---------------------|
| 0        | NET 30              |
| 1        | Subject to interest |

## Table 0051 – Diagnosis Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description          |
|----------|--------------------------|
| 253.2    | PANHYPOPITUITARISM       |
| 253.3    | PITUITARY DWARFISM       |
| 253.4    | ANTER PITUITARY DIS NEC  |
| 253.5    | DIABETES INSIPIDUS       |
| 253.6    | NEUROHYPOPHYSIS DIS NEC  |
| 253.7    | IATROGENIC PITUITARY DIS |
| 253.8    | DISEASES OF THYMUS NEC   |
| 253.8    | DISEASES OF THYMUS NEC   |
| 253.9    | PITUITARY DISORDER NOS   |
| 254.1    | ABSCESS OF THYMUS        |

## Table 0076 – Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                |
|----------|--------------------------------|
| ADT      | ADT MESSAGE                    |
| ACK      | GENERAL ACKNOWLEDGMENT         |
| MFN      | MASTER FILE NOTIFICATION       |
| ORF      | OBSERV. RESULT/RECORD RESPONSE |
| ORU      | OBSERV RESULT/UNSOLICITED      |
| QRY      | QUERY                          |

*Note: This is not the complete table. It contains those message types used by the VISTA/HEC interface.*

## Table 0078 – Abnormal Flags

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                           |
|----------|-------------------------------------------------------------------------------------------|
| \<       | Below absolute low-off instrument scale                                                   |
| \>       | Above absolute high-off instrument scale                                                  |
| A        | Abnormal (applies to non-numeric results)                                                 |
| AA       | Very abnormal (applies to non-numeric units, analogous to panic limits for numeric units) |
| B        | Better–use when direction not relevant                                                    |
| D        | Significant change down                                                                   |
| H        | Above high normal                                                                         |
| HH       | Above upper panic limits                                                                  |
| I        | Intermediate. Indicates for microbiology susceptibilities only.                           |
| L        | Below low normal                                                                          |
| LL       | Below lower panic limits                                                                  |
| MS       | Moderately susceptible. Indicates for microbiology susceptibilities only.                 |
| N        | Normal (applies to non-numeric results)                                                   |
| null     | No range defined, or normal ranges don’t apply                                            |
| R        | Resistant. Indicates for microbiology susceptibilities only.                              |
| S        | Susceptible. Indicates for microbiology susceptibilities only.                            |
| U        | Significant change up                                                                     |
| VS       | Very susceptible. Indicates for microbiology susceptibilities only.                       |
| W        | Worse–use when direction not relevant                                                     |

## Table 0080 – Nature of Abnormal Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description             |
|----------|-----------------------------|
| A        | An age-based population     |
| B        | Breed                       |
| N        | None – generic normal range |
| R        | A race-based population     |
| S        | A sex-based population      |
| SP       | Species                     |
| ST       | Strain                      |

## Table 0085 – Observation Result Status Codes Interpretation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C        | Record coming over is a correction and thus replaces a final result                                                                                                         |
| D        | Deletes the OBX record                                                                                                                                                      |
| F        | Final results; Can only be changed with a corrected result.                                                                                                                 |
| I        | Specimen in lab; results pending                                                                                                                                            |
| N        | Not asked; used to affirmatively document that the observation identified in the OBX was not sought when the universal service ID in OBR-4 implies that it would be sought. |
| O        | Order detail description only (no result)                                                                                                                                   |
| P        | Preliminary results                                                                                                                                                         |
| R        | Results entered – not verified                                                                                                                                              |
| S        | Partial results                                                                                                                                                             |
| U        | Results status change to final without retransmitting results already sent as \_preliminary.\_ E.g., radiology changes status from preliminary to final                     |
| W        | Post original as wrong, e.g., transmitted for wrong patient                                                                                                                 |
| X        | Results cannot be obtained for this observation                                                                                                                             |

## Table 0088 – Procedure Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                |
|----------|------------------------------------------------|
| 10141    | INCISION AND DRAINAGE OF HEMATOMA; COMPLICATED |

## Table 0091 – Query Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| D        | Deferred        |
| I        | Immediate       |

## Table 0102 – Delayed Acknowledgement Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                               |
|----------|-----------------------------------------------|
| D        | Message received, stored for later processing |
| F        | Acknowledgment after processing               |

## Table 0103 – Processing ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| D        | DEBUGGING       |
| P        | PRODUCTION      |
| T        | TRAINING        |

## Table 0104 – Version ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| 2.0      | RELEASE 2.0     |
| 2.0D     | DEMO 2.0        |
| 2.1      | RELEASE 2.1     |
| 2.2      | RELEASE 2.2     |

## Table 0105 – Source of Comment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                    |
|----------|----------------------------------------------------|
| L        | Ancillary (filler) department is source of comment |
| O        | Other system is source of comment                  |
| P        | Orderer (placer) is source of comment              |

## Table 0106 – Query/Response Format Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                       |
|----------|---------------------------------------|
| D        | Response is in display format         |
| R        | Response is in record-oriented format |
| T        | Response is in tabular format         |

## Table 0108 – Query Results Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description           |
|----------|---------------------------|
| O        | Order plus order status   |
| R        | Results without bulk text |
| S        | Status only               |
| T        | Full results              |

## Table 0115 – Servicing Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Sample of possible values; the complete table in the Messaging Workbench.*

| Code | Description        |
|----------|------------------------|
| 327      | LOUISVILLE-RO          |
| 358      | MANILA-RO              |
| 402      | TOGUS VAMROC           |
| 402GA    | CARIBOU                |
| 402GC    | RUMFORD                |
| 402GD    | SACO VA CLINIC         |
| 402HB    | BANGOR                 |
| 402HC    | PORTLAND               |
| 402HK    | CALAIS/MACHIAS         |
| 405      | WHITE RIVER JCT VAMROC |

## Table 0125 – Value Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                      |
|----------|------------------------------------------------------|
| AD       | Address                                              |
| CE       | Coded Entry                                          |
| CF       | Coded Element With Formatted Values                  |
| CK       | Composite ID With Check Digit                        |
| CN       | Composite ID And Name                                |
| CP       | Composite Price                                      |
| CX       | Extended Composite ID With Check Digit               |
| DT       | Date                                                 |
| ED       | Encapsulated Data                                    |
| FT       | Formatted Text (Display)                             |
| MO       | Money                                                |
| NM       | Numeric                                              |
| PN       | Person Name                                          |
| RP       | Reference Pointer                                    |
| SN       | Structured Numeric                                   |
| ST       | String Data.                                         |
| TM       | Time                                                 |
| TN       | Telephone Number                                     |
| TS       | Time Stamp (Date & Time)                             |
| TX       | Text Data (Display)                                  |
| XAD      | Extended Address                                     |
| XCN      | Extended Composite Name And Number For Persons       |
| XON      | Extended Composite Name And Number For Organizations |
| XPN      | Extended Person Name                                 |
| XTN      | Extended Telecommunications Number                   |

## Table 0126 – Quantity Limited Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| CH       | Characters      |
| LI       | Lines           |
| PG       | Pages           |
| RD       | Records         |
| ZO       | Locally defined |

## Table 0136 – Yes/No Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| N        | No              |
| Y        | Yes             |

## Table 0155 – Accept/Application Acknowledgment Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description              |
|----------|------------------------------|
| AL       | Always                       |
| ER       | Error/reject conditions only |
| NE       | Never                        |
| SU       | Successful completion only   |

## Table 0172 – Veterans Military Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| N        | Non Veteran     |
| Y        | Veteran         |

## Table 0175 – Master File Identifier Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description           |
|----------|---------------------------|
| Z04      | VHA INSTITUTION (#4) File |
| 5P12     | POSTAL CODE (#5.12) File  |
| 5P13     | COUNTY CODE (#5.13) File  |

## Table 0178 – File Level Event Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                             |
|----------|---------------------------------------------------------------------------------------------|
| REP      | Replace current version of this master file with the version contained in this message      |
| UPD      | Change file records as defined in the record level event codes for each record that follows |

## Table 0179 – Response Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| NE       | Never. No application-level response needed                                                                                                |
| ER       | Error/Reject conditions only. Only MFA segments denoting errors must be returned via the application-level acknowledgment for this message |
| AL       | Always. All MFA segments (whether denoting errors or not) must be returned via the application-level acknowledgment message                |
| SU       | Success. Only MFA segments denoting success must be returned via the application-level acknowledgment for this message                     |

## Table 0180 – Record Level Event Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                      |
|----------|--------------------------------------------------------------------------------------|
| MAD      | Add record to master file                                                            |
| MDL      | Delete record from master file                                                       |
| MUP      | Update record for master file                                                        |
| MDC      | Deactivate: discontinue using record in master file, but do not delete from database |
| MAC      | Reactivate deactivated record                                                        |

## Table 0189 – Ethnic Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description        |
|----------|------------------------|
| H        | Hispanic or Latino     |
| N        | Not Hispanic or Latino |
| U        | Unknown                |

## Table 0211 – Alternate Character Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code  | Description                                                                                                                                                |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 8859/1    | The printable characters from the ISO 8859/1 Character set                                                                                                     |
| 8859/2    | The printable characters from the ISO 8859/2 Character set                                                                                                     |
| 8859/3    | The printable characters from the ISO 8859/3 Character set                                                                                                     |
| 8859/4    | The printable characters from the ISO 8859/4 Character set                                                                                                     |
| 8859/5    | The printable characters from the ISO 8859/5 Character set                                                                                                     |
| 8859/6    | The printable characters from the ISO 8859/6 Character set                                                                                                     |
| 8859/7    | The printable characters from the ISO 8859/7 Character set                                                                                                     |
| 8859/8    | The printable characters from the ISO 8859/8 Character set                                                                                                     |
| 8859/9    | The printable characters from the ISO 8859/9 Character set                                                                                                     |
| ASCII     | The printable 7-bit ASCII character set. (This is the default if this field is omitted)                                                                        |
| ISO IR14  | Code for Information Exchange (one byte)(JIS X 0201-1976). Note that the code contains a space, i.e. “ISO IR14”.                                               |
| ISO IR159 | Code of the supplementary Japanese Graphic Character set for information interchange (JIS X 0212-1990). Note that the code contains a space, i.e. “ISO IR159”. |
| ISO IR87  | Code for the Japanese Graphic Character set for information interchange (JIS X 0208-1990), Note that the code contains a space, i.e. “ISO IR87”.               |
| UNICODE   | The world wide character standard from ISO/IEC 10646-1-19931                                                                                                   |

## Table 0280 – Referral Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| A        | ASAP            |
| R        | Routine         |
| S        | STAT            |

## Table 0281 – Referral Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| Hom      | Home Care       |
| Lab      | Laboratory      |
| Med      | Medical         |
| Psy      | Psychiatric     |
| Rad      | Radiology       |
| Skn      | Skilled Nursing |

## Table 0282 – Referral Disposition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                 |
|----------|---------------------------------|
| AM       | Assume Management               |
| RP       | Return Patient After Evaluation |
| SO       | Second Opinion                  |
| WR       | Send Written Report             |

## Table 0283 – Referral Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| A        | Accepted        |
| E        | Expired         |
| P        | Pending         |
| R        | Rejected        |

## Table 0284 – Referral Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| A        | Ambulatory      |
| E        | Emergency       |
| I        | Inpatient       |
| O        | Outpatient      |

## Table 0340 – Procedure Code Modifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description      |
|----------|----------------------|
| 57       | DECISION FOR SURGERY |

## Table 0356 – Alternate Character Set Handling Scheme

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code      | Description                                                                                                                                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<null\>      | This is the default, indicating that there is no character set switching occurring in this message.                                                                                                                                                           |
| 2.3           | The character set switching mode specified in HL7 2.3, sections 2.8.28.6.1, and 2.9.2. Note that the escape sequences used in this mode do not use the ASCII “esc” character. They are “HL7 escape sequences” as defined in HL7 2.3, sec. 2.9 as defined in I |
| ISO 2022-1994 | This standard is titled “Information Technology – Character Code Structure and Extension Technique”. This standard specifies an escape sequence from basic one byte character set to specified other character set, and vice versa.                           |

## Table 0363 – Source of Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ADDRESS CHANGE SOURCE Field (#.119) of PATIENT File (#2)

| Code | Description                                                                                             |
|----------|-------------------------------------------------------------------------------------------------------------|
| USVAHEC  | US VA Health Eligibility Center                                                                             |
| USVAMC   | US VA Medical Center                                                                                        |
| USVAHBSC | US VA Health Benefits Service Center                                                                        |
| USNCOA   | US National Change Of Address                                                                               |
| USVABVA  | US VA Board of Veteran’s Appeals Application                                                                |
| USVAINS  | US VA Philadelphia Insurance Center                                                                         |
| USPS     | US COA electronic file from the US Postal Service with forwarding address generated from enrollment letters |
| USVA     | US Department of Veterans Affairs                                                                           |
| VET360   | VET360 address validation service                                                                           |

### # Appendix D – Supported/User-Defined VA HL7 Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table VA001 – Yes/No

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| 0        | NO              |
| 1        | YES             |

## Table VA002 – Current Means Test Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CODE (#.02) Field of MEANS TEST STATUS (#408.32) File

| Code | Description                         |
|----------|-----------------------------------------|
| 0        | EXEMPT (LTC CO-PAY EXEMPTION TEST)      |
| 1        | NON- EXEMPT (LTC CO-PAY EXEMPTION TEST) |
| A        | MT COPAY EXEMPT                         |
| B        | CATEGORY B                              |
| C        | MT COPAY REQUIRED                       |
| E        | EXEMPT                                  |
| G        | GMT COPAY REQUIRED                      |
| I        | INCOMPLETE                              |
| L        | NO LONGER APPLICABLE                    |
| M        | NON-EXEMPT                              |
| N        | NO LONGER REQUIRED                      |
| P        | PENDING ADJUDICATION                    |
| R        | REQUIRED                                |

## Table VA003 – Employment Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EMPLOYMENT STATUS (#.31115) Field of PATIENT (#2) File

| Code | Description      |
|----------|----------------------|
| 1        | EMPLOYED FULL TIME   |
| 2        | EMPLOYED PART TIME   |
| 3        | NOT EMPLOYED         |
| 4        | SELF EMPLOYED        |
| 5        | RETIRED              |
| 6        | ACTIVE MILITARY DUTY |
| 9        | UNKNOWN              |

## Table VA004 – Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Internal Entry Number of MAS ELIGIBILITY CODE (#8.1) File

| Code | Description               |
|----------|-------------------------------|
| 1        | SERVICE CONNECTED 50% to 100% |
| 2        | AID & ATTENDANCE              |
| 3        | SC LESS THAN 50%              |
| 4        | NSC – VA PENSION              |
| 5        | NSC                           |
| 6        | OTHER FEDERAL AGENCY          |
| 7        | ALLIED VETERAN                |
| 8        | HUMANITARIAN EMERGENCY        |
| 9        | SHARING AGREEMENT             |
| 12       | CHAMPVA                       |
| 13       | COLLATERAL OF VET.            |
| 14       | EMPLOYEE                      |
| 15       | HOUSEBOUND                    |
| 17       | WORLD WAR I                   |
| 18       | PRISONER OF WAR               |
| 19       | TRICARE                       |
| 20       | MEDICARE                      |
| 22       | PURPLE HEART                  |
| 23       | EXPANDED MH CARE NON-ENROLLEE |
| 24       | COMPACT ACT ELIGIBLE          |
| 25       | SPECIAL TX AUTHORITY CARE     |
| 26       | HUD-VASH                      |
| 27       | CLINICAL EVALUATION           |

## Table VA005 – Disability Retirement From Military

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISABILITY RET. FROM MILITARY? (#.362) Field of PATIENT (#2) File

| Code | Description                                               |
|----------|---------------------------------------------------------------|
| 0        | NO                                                            |
| 1        | YES, RECEIVING MILITARY RETIREMENT                            |
| 2        | YES, RECEIVING MILITARY RETIREMENT IN LIEU OF VA COMPENSATION |
| 3        | UNKNOWN                                                       |

## Table VA006 – Eligibility Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ELIGIBILITY STATUS (#.3611) Field of PATIENT (#2) File

| Code | Description         |
|----------|-------------------------|
| P        | PENDING VERIFICATION    |
| R        | PENDING RE-VERIFICATION |
| V        | VERIFIED                |

## Table VA007 – Race

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ABBREVIATION (#2) Field of RACE (#10) File

| Code | Description                  |
|----------|----------------------------------|
| 1        | HISPANIC, WHITE                  |
| 2        | HISPANIC, BLACK                  |
| 3        | AMERICAN INDIAN OR ALASKA NATIVE |
| 4        | BLACK, NOT OF HISPANIC ORIGIN    |
| 5        | ASIAN OR PACIFIC ISLANDER        |
| 6        | WHITE, NOT OF HISPANIC ORIGIN    |
| 7        | UNKNOWN                          |

## Table VA008 – Religion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CODE (#3) Field of RELIGION (#13) File

| Code | Description           |
|----------|---------------------------|
| 0        | CATHOLIC                  |
| 1        | JEWISH                    |
| 2        | EASTERN ORTHODOX          |
| 3        | BAPTIST                   |
| 4        | METHODIST                 |
| 5        | LUTHERAN                  |
| 6        | PRESBYTERIAN              |
| 7        | UNITED CHURCH OF CHRIST   |
| 8        | EPISCOPALIAN              |
| 9        | ADVENTIST                 |
| 10       | ASSEMBLY OF GOD           |
| 11       | BRETHREN                  |
| 12       | CHRISTIAN SCIENTIST       |
| 13       | CHURCH OF CHRIST          |
| 14       | CHURCH OF GOD             |
| 15       | DISCIPLES OF CHRIST       |
| 16       | EVANGELICAL COVENANT      |
| 17       | FRIENDS                   |
| 18       | JEHOVAH’S WITNESS         |
| 19       | LATTER-DAY SAINTS         |
| 20       | ISLAM                     |
| 21       | NAZARENE                  |
| 22       | OTHER                     |
| 23       | PENTECOSTAL               |
| 24       | PROTESTANT, OTHER         |
| 25       | PROTESTANT, NO PREFERENCE |
| 26       | REFORMED                  |
| 27       | SALVATION ARMY            |
| 28       | UNITARIAN; UNIVERSALIST   |
| 29       | UNKNOWN/NO PREFERENCE     |

## Table VA009 – Relationship Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RELATIONSHIP NUMBER (#.001) Field \[internal entry number\] of RELATIONSHIP (#408.11) File

| Code | Description     |
|----------|---------------------|
| 1        | SELF                |
| 2        | SPOUSE              |
| 3        | SON                 |
| 4        | DAUGHTER            |
| 5        | STEPSON             |
| 6        | STEPDAUGHTER        |
| 7        | FOSTER SON          |
| 8        | FOSTER DAUGHTER     |
| 9        | SON-IN-LAW          |
| 10       | DAUGHTER-IN-LAW     |
| 11       | BROTHER             |
| 12       | SISTER              |
| 13       | STEPBROTHER         |
| 14       | STEPSISTER          |
| 15       | BROTHER-IN-LAW      |
| 16       | SISTER-IN-LAW       |
| 17       | FATHER              |
| 18       | MOTHER              |
| 19       | STEPFATHER          |
| 20       | STEPMOTHER          |
| 21       | FATHER-IN-LAW       |
| 22       | MOTHER-IN-LAW       |
| 23       | GRANDFATHER         |
| 24       | GRANDMOTHER         |
| 25       | GREAT-GRANDFATHER   |
| 26       | GREAT-GRANDMOTHER   |
| 27       | GRANDSON            |
| 28       | GRANDDAUGHTER       |
| 29       | GREAT-GRANDSON      |
| 30       | GREAT-GRANDDAUGHTER |
| 31       | NEPHEW              |
| 32       | NIECE               |
| 33       | UNCLE               |
| 34       | AUNT                |
| 99       | OTHER               |

## Table VA010 – Means Test Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                                                                                                                                                                                              |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AN       | This Means Test category includes NSC veterans who are required to complete VA Form 10-10F (Financial Worksheet) and those NSC veterans in receipt of VA pension, aid and attendance, housebound allowance, or entitled to State Medicaid.                   |
| AS       | This Means Test category includes all compensable service-connected (0-100%) veterans and special category veterans.                                                                                                                                         |
| C        | This Means Test category includes those veterans who, based on income and/or net worth, are required to reimburse VA for care rendered.                                                                                                                      |
| N        | This Means Test category includes only non-veterans receiving treatment at VA facilities.                                                                                                                                                                    |
| U        | This Means Test category includes only those patients who require a Means Test, and the Means Test has not been done/completed. The Austin Information Technology Center (AITC) will not accept an OPC transaction unless the Means Test has been completed. |
| X        | This Means Test category includes treatment of patients who are not required to complete the Means Test for the care being provided.                                                                                                                         |

## Table VA011 – Period of Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Internal Entry Number of PERIOD OF SERVICE (#21) File

| Code | Description           |
|----------|---------------------------|
| 0        | KOREAN                    |
| 1        | WORLD WAR I               |
| 2        | WORLD WAR II              |
| 3        | SPANISH AMERICAN          |
| 4        | PRE-KOREAN                |
| 5        | POST-KOREAN               |
| 6        | OPERATION DESERT SHIELD   |
| 7        | VIETNAM ERA               |
| 8        | POST-VIETNAM              |
| 9        | OTHER OR NONE             |
| A        | ARMY—ACTIVE DUTY          |
| B        | NAVY, MARINE—ACTIVE DUTY  |
| C        | USAF, USSF - ACTIVE DUTY  |
| D        | COAST GUARD—ACTIVE DUTY   |
| E        | RETIRED, UNIFORMED FORCES |
| F        | MEDICAL REMEDIAL ENLIST   |
| G        | MERCHANT SEAMEN—USPHS     |
| H        | OTHER USPHS BENEFICIARIES |
| I        | OBSERVATION/EXAMINATION   |
| J        | OFFICE OF WORKERS COMP    |
| K        | JOB CORPS/PEACE CORPS     |
| L        | RAILROAD RETIREMENT       |
| M        | BENEFICIARIES-FOREIGN GOV |
| N        | HUMANITARIAN (NON-VET)    |
| O        | CHAMPUS RESTORE           |
| P        | OTHER REIMBURS. (NON-VET) |
| Q        | OTHER FEDERAL – DEPENDENT |
| R        | DONORS (NON-VET)          |
| S        | SPECIAL STUDIES (NON-VET) |
| T        | OTHER NON-VETERANS        |
| U        | CHAMPVA—SPOUSE, CHILD     |
| V        | CHAMPUS                   |
| W        | CZECHOSLOVAKIA/POLAND SVC |
| X        | PERSIAN GULF WAR          |
| Y        | CAV/NPS                   |
| Z        | MERCHANT MARINE           |

## Table VA012 – Type of Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description       |
|----------|-----------------------|
| 0        | NO INSURANCE          |
| 1        | MAJOR MEDICAL         |
| 10       | PRESCRIPTION          |
| 11       | MEDICARE SUPPLEMENTAL |
| 12       | ALL OTHER             |
| 2        | DENTAL                |
| 3        | HMO                   |
| 4        | PPO                   |
| 5        | MEDICARE              |
| 6        | MEDICAID              |
| 7        | CHAMPUS               |
| 8        | WORKMAN COMP          |
| 9        | INDEMNITY             |

## Table VA013 – Rated Disabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMBER (.001) Field \[internal entry number\] of the DISABILITY CONDITION (#31) File

*(Sample listing of possible values)*

| Code | Description        |
|----------|------------------------|
| 1        | OSTEOMYELITIS          |
| 2        | BONE DISEASE           |
| 3        | RHEUMATOID ARTHRITIS   |
| 4        | DEGENERATIVE ARTHRITIS |
| 5        | ARTHRITIS              |

## Table VA014 – Medication Copayment Exemption Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| 0        | NON-EXEMPT      |
| 1        | EXEMPT          |

## Table VA015 – Enrollment Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(#.04) Field of the PATIENT ENROLLMENT (#27.11) File

| Code | Description                            |
|----------|--------------------------------------------|
| 1        | Unverified                                 |
| 2        | Verified                                   |
| 3        | Inactive (not used at this time)           |
| 4        | Rejected (not used at this time)           |
| 5        | Suspended (not used at this time)          |
| 6        | Deceased                                   |
| 7        | Canceled/Declined                          |
| 8        | Expired (not used at this time)            |
| 9        | Pending (not used at this time)            |
| 10       | Not Eligible                               |
| 11       | Rejected; Fiscal Year                      |
| 12       | Rejected; Mid-cycle                        |
| 13       | Rejected; Stop New Enrollments             |
| 14       | Rejected; Initial Application by VAMC      |
| 15       | Pending, No Eligibility Code               |
| 16       | Pending; Means Test Required               |
| 17       | Pending; Eligibility Status is Unverified  |
| 18       | Pending; Other                             |
| 19       | Not Eligible; Refused to Pay Copay         |
| 20       | Not Eligible; Ineligible Date              |
| 21       | Pending; Purple Heart Unconfirmed          |
| 22       | Rejected; Below Enrollment Group Threshold |
| 23       | Not Applicable                             |
| 24       | Closed Application                         |
| 25       | Registration Only                          |

## Table VA016 – Reason Enrollment Canceled/Declined

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(#.05) Field of the PATIENT ENROLLMENT (#27.11) File

| Code | Description        |
|----------|------------------------|
| 1        | Dissatisfied with Care |
| 2        | Geographic Access      |
| 3        | Other Insurance        |
| 4        | Other                  |
| 5        | ACA Preference         |

## Table VA017 – Enrollment Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| 1        | Priority 1      |
| 2        | Priority 2      |
| 3        | Priority 3      |
| 4        | Priority 4      |
| 5        | Priority 5      |
| 6        | Priority 6      |
| 7        | Priority 7      |
| 8        | Priority 8      |

## Table VA018 – Agency/Allied Country

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code  | Description                |
|-----------|--------------------------------|
| ACF       | HHS – CHILDREN AND FAMILIES    |
| AUSTRALIA | AUSTRALIA                      |
| CANADA    | CANADA                         |
| CIV SER   | CIVIL SERVICE COMMISSION       |
| CZECH     | CZECHOSLOVAKIA                 |
| DCFCC     | DC FEDERAL CIRCUIT COURT       |
| DCSDNY    | US DC SOUTHERN DISTRICT OF NY  |
| DEA       | DOJ  - DRUG ENFORCEMENT ADMIN  |
| DFC       | DEVELOPMENT FINANCE CORP       |
| DHS       | DEPT OF HOMELAND SECURITY      |
| DOA       | DEPARTMENT OF AGRICULTURE      |
| DOD       | DEPARTMENT OF DEFENSE          |
| DOE       | DEPARTMENT OF ENERGY           |
| DOI       | DEPARTMENT OF INTERIOR         |
| DOJ       | DEPARTMENT OF JUSTICE          |
| DOL       | DEPARTMENT OF LABOR            |
| DOS       | DEPARTMENT OF STATE            |
| DOT       | DEPARTMENT OF TRANSPORTATION   |
| ED        | DEPARTMENT OF EDUCATION        |
| EPA       | ENVIRONMENTAL PROTECTION AGCY  |
| FAA       | FEDERAL AVIATION ADMIN.        |
| FDA       | HHS – FOOD AND DRUG ADMIN      |
| FRANCE    | FRANCE                         |
| GSA       | GENERAL SERVICES ADMIN         |
| HHS       | DEPT HEALTH AND HUMAN SERVICES |
| HHSOIG    | HHS – OFC OF THE INSP GENERAL  |
| HUD       | DEPT HOUSING AND URBAN DEV     |
| NARA      | NAT ARCHIVES AND RECORDS ADMIN |
| NZ        | NEW ZEALAND                    |
| OEO       | OFFICE OF ECONOMIC OPPURTUNITY |
| OFEC      | OFFICE OF EMPLOYEE’S COMP.     |
| OPM       | OFFICE OF PERSONNEL MANAGEMENT |
| OTHER     | OTHER                          |
| PC        | PEACE CORPS                    |
| POLAND    | POLAND                         |
| S. AFRICA | SOUTH AFRICA                   |
| SBA       | SMALL BUSINESS ADMINISTRATION  |
| SVH       | VA – STATE VETERANS HOME       |
| UK        | UK GRT BRITAIN AND N. IRELAND  |
| USDC      | DEPARTMENT OF COMMERCE         |
| USDT      | DEPARTMENT OF THE TREASURY     |
| USFJ      | US FEDERAL JUDICIARY           |
| USFS      | DOA – FOREST SERVICE           |
| USSR      | SOVIET UNION                   |
| VA        | VETERANS ADMINISTRATION        |

## Table VA022 - Radiation Exposure Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description         |
|----------|-------------------------|
| 2        | Nagasaki - Hiroshima    |
| 3        | Nuclear Testing         |
| 4        | H/N AND ATMOS TESTING   |
| 5        | UNDERGRD NUCLR TESTING  |
| 6        | EXPOS AT NUCLR FACILITY |
| 7        | OTHER                   |
| 8        | ENEWETAK                |
| 9        | EXPOS IN PALOMARES B52  |
| 10       | THULE AFB B52           |

## Table VA026 - Military Service Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description          |
|----------|--------------------------|
| R        | Regular                  |
| V        | Activated reserve        |
| G        | Activated national guard |

## Table VA033 - Fee Basis Treatment Code Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description       |
|----------|-----------------------|
| 1        | Short Term Fee Status |
| 2        | Home Nursing Services |
| 3        | For I.D. Card Status  |
| 4        | State Home            |

## Table VA034 - Fee Basis Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                  |
|----------|----------------------------------|
| 1        | CHAMPVA                          |
| 2        | Civil Hospital                   |
| 3        | Comp & Pension                   |
| 4        | Contract Halfway House           |
| 5        | Contract Nursing Home            |
| 6        | Contract Readjustment Counseling |
| 7        | Dental                           |
| 8        | Dialysis                         |
| 9        | Home Health Services             |
| 10       | Inpatient                        |
| 11       | Other Institutional Services     |
| 12       | Outpatient                       |
| 13       | Oxygen Services                  |
| 14       | Pharmacy                         |
| 15       | State Home                       |

## Table VA035 - Enrollment Sub-Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enrollment Sub-Group (.12) of Patient Enrollment File (#27.11)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>a</td>
<td>Non-compensable zero percent service connected veterans who were in an enrolled status on a specified date and who have remained continuously enrolled thereafter</td>
</tr>
<tr class="even">
<td>b</td>
<td><p>Non-compensable zero percent service connected veterans who apply for enrollment on or after 1/1/2009 AND the current Financial assessment identifies income above the VA MT or GMT threshold (whichever is higher) by 10% or less</p>
<p>OR</p>
<p>Non-compensable zero percent service connected veterans who submit a 2008 Income Year Means test or later that calculates the income (income minus medical and educational expenses) under the VA MT threshold and income plus assets are greater than or equal to $80K</p></td>
</tr>
<tr class="odd">
<td>c</td>
<td>Non-service connected veterans who were in an enrolled status on a specified date and who have remained continuously enrolled thereafter</td>
</tr>
<tr class="even">
<td>d</td>
<td><p>Non-service connected veterans who apply for enrollment on or after 1/1/2009 AND the most current financial assessment identifies income above the VA MT or GMT threshold (whichever is higher) by 10% or less</p>
<p>OR</p>
<p>Non-service connected veterans who submit a 2008 Income Year Means test or later that calculates the income (income minus medical and educational expenses) under the VA MT threshold and income plus assets are greater than or equal to $80K</p></td>
</tr>
<tr class="odd">
<td>e</td>
<td>0% non-compensable service-connected veterans who apply for enrollment on or after the EGT effective date</td>
</tr>
<tr class="even">
<td>g</td>
<td>Non-service-connected veterans who apply for enrollment on or after the EGT effective date</td>
</tr>
</tbody>
</table>

## Table VA036 - Military Sexual Trauma Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                  |
|----------|----------------------------------|
| D        | SCREENED, DECLINES TO ANSWER     |
| N        | NO, SCREENED DOES NOT REPORT MST |
| U        | UNKNOWN, NOT SCREENED            |
| Y        | YES, SCREENED REPORTS MST        |

## Table VA038 - Military History Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                  |
|----------|----------------------------------|
| SL       | SERVICE LAST EPISODE             |
| SNL      | SERVICE SECOND EPISODE           |
| SNNL     | SERVICE THIRD EPISODE            |
| MSD      | MILITARY SERVICE DATA            |
| POW      | PRISONER OF WAR                  |
| COMB     | COMBAT                           |
| VIET     | VIETNAM                          |
| LEBA     | LEBANON                          |
| GREN     | GRENADA                          |
| PANA     | PANAMA                           |
| GULF     | GULF WAR                         |
| SOMA     | SOMALIA                          |
| PH       | PURPLE HEART                     |
| YUGO     | YUGOSLAVIA                       |
| OEIF     | OPERATION ENDURING/IRAQI FREEDOM |

## Table VA0040 - Enrollment Group Threshold Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EGT Type (.04) of Enrollment Group Threshold File (#27.16)

| Code | Description                   |
|----------|-----------------------------------|
| 1        | ANNUAL FISCAL YEAR                |
| 2        | STOP NEW ENROLLMENTS DURING CYCLE |
| 3        | MID-CYCLE CHANGE                  |
| 4        | ENROLLMENT DECISION               |

## Table VA041 - Determination Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description         |
|----------|-------------------------|
| 1        | Automated Record Review |
| 2        | Medical Record Review   |
| 3        | Physical Examination    |

## Table VA042 - Affected Extremity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description             |
|----------|-----------------------------|
| 1        | RUE (Right Upper Extremity) |
| 2        | RLE (Right Lower Extremity) |
| 3        | LUE (Left Upper Extremity)  |
| 4        | LLE (Left Lower Extremity   |

## Table VA043 - Condition Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| 1        | KATZ            |
| 2        | FOLS            |
| 3        | RUG3            |
| 4        | FIM             |
| 5        | GAF             |

## Table VA045 - CD Permanent Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description |
|----------|-----------------|
| 1        | Permanent       |
| 2        | Not permanent   |
| 3        | Unknown         |

## Table VA0047 - PATIENT REGISTRATION ONLY REASON Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description              |
|-----------|------------------------------|
| 2         | ACTIVE DUTY                  |
| 12        | ART/IVF                      |
| 8         | BENEFICIARY                  |
| 1         | C&P DISABILITY BENEFITS EXAM |
| 18        | CAREGIVER                    |
| 11        | COLLATERAL (OTHER)           |
| 7         | EMPLOYEE                     |
| 4         | EXPOSURE REGISTRY EXAM       |
| 6         | HUMANITARIAN/EMERGENCY       |
| 14        | LEGISLATIVE MANDATE          |
| 10        | MARRIAGE/FAMILY COUNSELING   |
| 13        | NEWBORN                      |
| 16        | NORTH CHICAGO ACTIVE DUTY    |
| 15        | OTHER                        |
| 9         | OTHER THAN HONORABLE (OTH)   |
| 5         | RESEARCH                     |
| 3         | SERVICE CONNECTED ONLY       |
| 17        | UNANSWERED                   |
| 19        | VHA TRANSPLANT PROGRAM       |

## Table VA048 - Filipino Veteran Proof

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                      |
|----------|--------------------------------------|
| PP       | US Passport                          |
| BC       | US Birth Certificate                 |
| BA       | Report of Birth Abroad of US Citizen |
| NA       | Verification of Naturalization       |
| PR       | Verification of Permanent Residency  |
| VA       | VA Compensation at Full Dollar Rate  |
| NO       | No Proof                             |

## Table VA0051 - Means Test Signature Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                          |
|----------|----------------------------------------------------------|
| 1        | YES; Means Test image received and signed                |
| 0        | NO; Means Test image received, but unsigned              |
| 9        | DELETED; Means Test signature indicator has been deleted |

## Table VA0052 - NTR Verification Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                  |
|----------|--------------------------------------------------|
| S        | Qual Military Srvc (Qualifying Military Service) |
| M        | Military Med Rec (Military Medical Record)       |
| N        | Not Qualified                                    |

## Table VA0053 - NTR Qualifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                        |
|----------|------------------------------------------------------------------------|
| 1        | Received NTR Trmt (Received NTR Treatment)                             |
| 2        | Aviator Pre 1955 (Aviator Prior to 1955)                               |
| 3        | Sub Trainee pre 1965 (Navy Sub Trainee Prior 1965)                     |
| 4        | Dx With Head Neck Cancer (Diagnosed With Head and Neck Cancer)         |
| 5        | No NTR Trmt (No NTR Treatment)                                         |
| 6        | Not Aviator Pre 1955 (Not Aviator Prior to 1955)                       |
| 7        | Not Sub Trainee pre 1965 (Not Navy Sub Trainee Prior 1965)             |
| 8        | Not Dx With Head Neck Cancer (Not Diagnosed With Head and Neck Cancer) |
| 9        | NTR Trmt Unknown (NTR Treatment Unknown)                               |

## Table VA060 - Type of Financial Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description           |
|----------|---------------------------|
| 1        | MEANS TEST                |
| 2        | CO-PAY EXEMPTION TEST     |
| 4        | LTC CO-PAY EXEMPTION TEST |

## Table VA061 - Invalid Address Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1        | Address Does Not Exist (maps to Code 1 errors)                                                                                    |
| 2        | Veteran Does Not Reside at Address (maps to NCOA invalid address and mail returned by USPS due to Forwarding Order Expired, etc.) |
| 3        | Missing Required Address Field (maps to HEC Errors/AITC Errors)                                                                   |
| 4        | Death                                                                                                                             |
| 5        | Other                                                                                                                             |

## Table VA0115 - Servicing Facility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*(Sample listing of possible values)*

| Code | Description            |
|----------|----------------------------|
| 512 9AC  | Perry Point (Nursing Home) |

## Table VA117 - Reason For Closed Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(#.13) Field of the PATIENT ENROLLMENT (#27.11) File

| Code | Description       |
|----------|-----------------------|
| 1        | Abandoned Application |

## Table VA440 – CD Descriptors 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Code | Description                             |
|----------|---------------------------------------------|
| 1        | QUADRIPLEGIA                                |
| 2        | PARAPLEGIA                                  |
| 3        | PERSISTENT VEGETATIVE STATE                 |
| 4        | LEGAL BLINDNESS                             |
| 5        | AMPUTATION, DISARTICULATION, OR DETACHMENT  |
| 6        | DEFICIENCIES OF PHYSICAL OR MENTAL FUNCTION |
| 7        | DEAFNESS                                    |

Template Revision History

<table>
<caption>Template Revision History showing date template was created or revised, version number, description, and author.</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>July 2024</td>
<td>1.3</td>
<td>Updated to OIT Brand and OIT Production Documentation Standards.</td>
<td>OIT Documentation Standards Committee</td>
</tr>
<tr class="even">
<td>March 2024</td>
<td>1.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated organization references.</p></li>
<li><p>Updated Styles and formatting.</p></li>
<li><p>Updated instructional text throughout.</p></li>
</ul></td>
<td>OIT Documentation Standards Committee</td>
</tr>
<tr class="odd">
<td>July 2016</td>
<td>1.1</td>
<td>Updated instructional text to simplify content.</td>
<td>OIT Documentation Standards Committee</td>
</tr>
<tr class="even">
<td>June 2016</td>
<td>1.0</td>
<td>Initial version.</td>
<td>OIT Documentation Standards Committee</td>
</tr>
</tbody>
</table>

Template Revision History showing date template was created or revised, version number, description, and author.